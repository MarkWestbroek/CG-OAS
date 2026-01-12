import FreeSimpleGUI as sg # Just change this line!

layout = [[sg.Text("Hello from the Free Version!")], [sg.Button("OK")]]
window = sg.Window("My App", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "OK":
        break
window.close()