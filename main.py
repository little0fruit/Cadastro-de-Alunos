import PySimpleGUI as sg

## Funções
def Cadastros():
    print


##Layout
def Menu():
    layout = [[sg.Text('Gerenciamento Escolar',background_color='#4B5694', justification='center', expand_x=True, font=('Arial', 32))],
            [sg.Button(button_text='Cadastros', font=('Arial', 20), button_color= '#7288AE', size=(30,1))],
            [sg.Button(button_text='Consultas', font=('Arial', 20), button_color= '#7288AE', size=(30,1))],
            [sg.Button(button_text='Alteraçes', font=('Arial', 20), button_color= '#7288AE', size=(30,1))],
            [sg.Button(button_text='Notas', font=('Arial', 20), button_color= '#7288AE', size=(30,1))],
            [sg.Button(button_text='Sair', font=('Arial', 20), button_color= '#7288AE', size=(20,1), pad=(0,70))],
            ]
    return layout
window = sg.Window('Teste', Menu(), size=(900,500))
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

window.close()             

