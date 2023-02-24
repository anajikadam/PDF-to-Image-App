import PySimpleGUI as sg

layout = [[sg.Text('Very basic Window')],
          [sg.Text('Click X in titlebar or the Exit button')],
          [sg.Button('Go'), sg.Button('Exit')]]

window = sg.Window('Window Title', layout, enable_close_attempted_event=True)

while True:
    sg.popup_scrolled("By: Ankit", title="Credits", font=('Arial', 20))
    event, values = window.read()
    print(event, values)
    if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == 'Exit') and sg.popup_yes_no('Do you really want to exit?') == 'Yes':
        break

window.close()