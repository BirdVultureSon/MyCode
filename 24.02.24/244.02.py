from argparse import ArgumentParser, FileType
from os import get_terminal_size
from sys import stdout

from cv2 import VideoCapture
from pydub import AudioSegment
from simpleaudio import play_buffer

from mp_terminal.terminal_player import TerminalPlayer
from mp_terminal.video_meta import get_video_meta


def _get_video_size(display_ratio: tuple[int, int], terminal_size: tuple[int, int]):
    width_ratio, height_ratio = display_ratio
    width, height = terminal_size

    while width and height:
        while width > 0 and width % width_ratio != 0:
            width -= 1

        while height > 0 and height % height_ratio != 0:
            height -= 1

        if width / width_ratio == height / height_ratio:
            return width, height

        if width / width_ratio > height / height_ratio:
            width -= 1
        else:
            height -= 1

    return terminal_size


def view_video(video_path: str):
    audio_segment = AudioSegment.from_file(video_path)
    meta = get_video_meta(video_path)

    terminal_size = get_terminal_size()
    resolution = _get_video_size(
        meta.resolution,
        (terminal_size.columns, terminal_size.lines),
    )
    vidcap = VideoCapture(video_path)

    terminal_player = TerminalPlayer(stdout, resolution, meta.fps, meta.duration)
    playback = play_buffer(
        audio_segment.raw_data,
        num_channels=audio_segment.channels,
        bytes_per_sample=audio_segment.sample_width,
        sample_rate=audio_segment.frame_rate,
    )
    terminal_player.start()
    try:
        while True:
            sucess, frame = vidcap.read()
            if not sucess:
                break

            terminal_player.render_frame(frame)
    except KeyboardInterrupt:
        terminal_player.reset(True)
        raise
    except:
        terminal_player.reset(False)
        raise
    else:
        terminal_player.reset(True)
    finally:
        playback.stop()


def _parse_args():
    parser = ArgumentParser()
    parser.add_argument("--mp4-file", type=FileType(), required=True)

    return parser.parse_args()


def main():
    args = _parse_args()

    try:
        view_video(args.mp4_file.name)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()


from functools import cached_property
from time import monotonic, sleep
from typing import TextIO, Tuple

from cursor import hide as cursor_hide
from cursor import show as cursor_show
from cv2 import INTER_AREA, resize
from numpy import ndarray

_RESET_FG = "\x1b[0m"
_CLEAR_TERMINAL = chr(27) + "[2J"


class TerminalPlayer:
    def __init__(
        self,
        stream: TextIO,
        resolution: Tuple[int, int],
        fps: float,
        duration: float,
    ):
        self._stream = stream
        self._resolution = resolution
        self._fps = fps
        self._duration = duration

        self._width, self._height = resolution

        self._frames_count: int = 0
        self._start_time: float = 0.0

    @property
    def _video_resolution(self) -> Tuple[int, int]:
        return (self._video_width, self._video_height)

    @cached_property
    def _frame_duration(self) -> float:
        return 1 / self._fps

    @property
    def _video_height(self) -> int:
        return self._height - 1

    @property
    def _video_width(self) -> int:
        return self._width * 2

    def render_frame(self, frame: ndarray):
        delta = (self._frame_duration * self._frames_count) - (
            monotonic() - self._start_time
        )
        if delta > 0:
            sleep(delta)

        self._frames_count += 1
        if delta < 0:
            return

        self._stream.write(f"\x1b[{self._video_height + 1}A")

        for line in _resize_frame(frame, self._video_resolution):
            for pixel in line:
                blue, green, red = pixel
                self._stream.write(f"\x1b[48;2;{red};{green};{blue}m ")
            self._stream.write("\n")

        self._stream.write(_RESET_FG + self._get_status_line() + "\n")
        self._stream.flush()

    def _get_status_line(self) -> str:
        line = f"{_format_time(monotonic() - self._start_time)}/{_format_time(self._duration)}".center(
            self._video_width
        ).rstrip()
        line += f"FPS: {self._fps:.2f}".rjust(self._video_width - len(line), " ")

        return line

    def start(self):
        self._start_time = monotonic()
        cursor_hide(self._stream)
        self._stream.write(_CLEAR_TERMINAL)

    def reset(self, clear_terminal: bool = True):
        self._stream.write(_RESET_FG)
        cursor_show(self._stream)
        if clear_terminal:
            self._stream.write(_CLEAR_TERMINAL)


def _resize_frame(frame: ndarray, window_size: tuple[int, int]) -> ndarray:
    return resize(frame, window_size, interpolation=INTER_AREA)


def _format_time(seconds: float):
    minutes = int(seconds / 60)
    if minutes:
        seconds -= minutes * 60

    return f"{minutes:-02}:{int(seconds):-02}"

from dataclasses import dataclass
from typing import Any, Dict

from ffmpeg import probe



@dataclass
class VideoMeta:
    duration: float
    frames_number: int
    resolution: tuple[int, int]
    fps: float


def _get_duration(video_stream_info: Dict[str, Any]) -> float:
    if (duration := video_stream_info.get("duration")) is not None:
        return float(duration)
    
    if (tags := video_stream_info.get("tags")) is not None:
        if (duration := tags.get("DURATION")) is not None:
            # 00:22:46.006000000
            hours, minutes, seconds = duration.split(":", maxsplit=3)
            return (int(hours) * 60 + int(minutes)) * 60 + float(seconds)
    raise ValueError("Unable to find video duration")
    

def _get_frames_number(video_stream_info: Dict[str, Any]) -> int:
    if (nb_frames := video_stream_info.get("nb_frames")) is not None:
        return int(nb_frames)

    if (tags := video_stream_info.get("tags")) is not None:
        if (nb_frames := tags.get("NUMBER_OF_FRAMES")) is not None:
            return int(nb_frames)

    raise ValueError("Unable to find video frames number")

def _get_resolution(video_stream_info: Dict[str, Any]) -> tuple[int, int]:
    if (display_aspect_ratio := video_stream_info.get("display_aspect_ratio")) is not None:
        return tuple(map(int, display_aspect_ratio.split(":")))

    raise ValueError("Unable to find video resolution")

def _get_fps(video_stream_info: Dict[str, Any]) -> float:
    if (avg_frame_rate := video_stream_info.get("avg_frame_rate")) is not None:
        x, y = map(int, avg_frame_rate.split('/', maxsplit=1))
        return x / y

    raise ValueError("Unable to find video resolution")

def get_video_meta(video_path: str) -> VideoMeta:
    info = probe(video_path)
    
    video_stream: Dict[str, Any] = info["streams"][0]
    return VideoMeta(
        duration=_get_duration(video_stream),
        frames_number=_get_frames_number(video_stream),
        resolution=_get_resolution(video_stream),
        fps=_get_fps(video_stream)
    )
    
