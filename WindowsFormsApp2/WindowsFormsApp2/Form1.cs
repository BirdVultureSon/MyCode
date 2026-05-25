using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp2
{
	public partial class Form1 : Form
	{
		public Form1()
		{
			InitializeComponent();

			if (comboBox1.Items.Count == 0)
			{
				comboBox1.Items.AddRange(new object[] { "Low", "Medium", "High" });
				comboBox1.SelectedIndex = 1;
			}

			checkedListBox1.ItemCheck += CheckedListBox1_ItemCheck;
		}

		private void button1_Click(object sender, EventArgs e)
		{
			string task = textBox2.Text.Trim();
			string priority = comboBox1.Text;

			if (string.IsNullOrEmpty(task))
			{
				MessageBox.Show("Введите задачу.");
				return;
			}

			checkedListBox1.Items.Add($"[ ] {priority} - {task}");
			textBox2.Clear();
		}

		private void CheckedListBox1_ItemCheck(object sender, ItemCheckEventArgs e)
		{
			this.BeginInvoke(new Action(() => {
				if (e.NewValue == CheckState.Checked)
				{
					string text = checkedListBox1.Items[e.Index].ToString();

					if (!text.StartsWith("[✓] "))
					{
						checkedListBox1.Items[e.Index] = text.Replace("[ ] ", "[✓] ");
					}

					checkedListBox1.Items.RemoveAt(e.Index);
				}
			}));
		}

		private void button2_Click(object sender, EventArgs e)
		{
			int index = checkedListBox1.SelectedIndex;
			if (index < 0) return;

			object item = checkedListBox1.Items[index];
			string text = item.ToString();

			if (text.StartsWith("[ ] "))
			{
				checkedListBox1.Items[index] = text.Replace("[ ] ", "[✓] ");
				checkedListBox1.SetItemChecked(index, true);
			}
			else if (text.StartsWith("[✓] "))
			{
				checkedListBox1.Items[index] = text.Replace("[✓] ", "[ ] ");
				checkedListBox1.SetItemChecked(index, false);
			}
		}

		private void button3_Click(object sender, EventArgs e)
		{
			int index = checkedListBox1.SelectedIndex;
			if (index >= 0)
			{
				checkedListBox1.Items.RemoveAt(index);
			}
		}

		private void button4_Click(object sender, EventArgs e)
		{
			checkedListBox1.Items.Clear();
		}

		private void textBox2_TextChanged(object sender, EventArgs e) { }
		private void comboBox1_SelectedIndexChanged(object sender, EventArgs e) { }
		private void checkedListBox1_SelectedIndexChanged(object sender, EventArgs e) { }
	}
}