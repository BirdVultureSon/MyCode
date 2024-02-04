color = "red"
def function():
    shape = "circle"
    global color
    color = "green"
    print (f"Цвет: {color}")

print (f"Цвет: {color}")
function()
print (f"Цвет: {color}")