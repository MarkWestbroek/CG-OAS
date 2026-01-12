import PySimpleGUI as sg

# 1. Define the layout (Rows and Columns)
layout = [
    [sg.Text("Hello, World!", font=("Helvetica", 16))],
    [sg.Button("OK")]
]

# 2. Create the Window
window = sg.Window("My App", layout, margins=(50, 30))

# 3. The Event Loop
while True:
    event, values = window.read()
    
    # If user closes window or clicks OK
    if event == sg.WIN_CLOSED or event == "OK":
        break

# 4. Cleanup
window.close()