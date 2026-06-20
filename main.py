import PySimpleGUI as sg

## Funções
def Menu():
    return [[sg.Text('Gerenciamento Escolar',background_color='#4B5694', justification='center', expand_x=True, font=('Arial', 32))],
            [sg.Button(button_text='Cadastros', key='-Cadastros-', font=('Arial', 20), button_color= '#7288AE', size=(30,1))],
            [sg.Button(button_text='Consultas', key='-Consultas-',font=('Arial', 20), button_color= '#7288AE', size=(30,1))],
            [sg.Button(button_text='Alterações', key='-Alteracoes-',font=('Arial', 20), button_color= '#7288AE', size=(30,1))],
            [sg.Button(button_text='Notas', key='-Notas-',font=('Arial', 20), button_color= '#7288AE', size=(30,1))],
            [sg.Button(button_text='Sair', font=('Arial', 20), button_color= '#7288AE', size=(20,1), pad=(0,70))],
            ]


def MostrarTela(nome_tela):
    window['-Tela_Menu-'].update(visible=False)
    window['-Tela_Cadastros-'].update(visible=False)
    window['-Tela_Alteracoes-'].update(visible=False)
    window['-Tela_Consultas-'].update(visible=False)
    window['-Tela_Cadastros-'].update(visible=False)

    window[nome_tela].update(visible=True)


def Cadastros():
    return [[sg.Text('Cadastros',background_color='#4B5694', justification='center', expand_x=True, font=('Arial', 32))],
            [sg.Button(button_text='Alunos', key='-AlunosCad-', font=('Arial', 20), button_color= '#7288AE', size=(30,1))],
            [sg.Button(button_text='Disciplina', key='-DisciplinaCad-', font=('Arial', 20), button_color= '#7288AE', size=(30,1))],
            [sg.Button(button_text='Professor', key='-ProfessorCad-',font=('Arial', 20), button_color= '#7288AE', size=(30,1))],
            [sg.Button(button_text='Matricula', key='-MatriculaCad-',font=('Arial', 20), button_color= '#7288AE', size=(30,1))],
            [sg.Button(button_text='Turmas', key='-TurmasCad-', font=('Arial', 20), button_color= '#7288AE', size=(30,1))],
            [sg.Button(button_text='Voltar', key='-Voltar-', font=('Arial', 20), button_color= '#7288AE', size=(20,1), pad=(0,10))]
            ]


def Alteracoes():
    return [[sg.Text('Alterações',background_color='#4B5694', justification='center', expand_x=True, font=('Arial', 32))],
            [sg.Button(button_text='Alunos', key='-AlunosAlt-', font=('Arial', 20), button_color= '#7288AE', size=(30,1))],
            [sg.Button(button_text='Disciplina', key='-DisciplinaAlt-', font=('Arial', 20), button_color= '#7288AE', size=(30,1))],
            [sg.Button(button_text='Professor', key='-ProfessorAlt-',font=('Arial', 20), button_color= '#7288AE', size=(30,1))],
            [sg.Button(button_text='Matricula', key='-MatriculaAlt-',font=('Arial', 20), button_color= '#7288AE', size=(30,1))],
            [sg.Button(button_text='Turmas', key='-TurmasAlt-', font=('Arial', 20), button_color= '#7288AE', size=(30,1))],
            [sg.Button(button_text='Voltar', key='-Voltar-', font=('Arial', 20), button_color= '#7288AE', size=(20,1), pad=(0,10))]
            ]


def Consultas():
    return [[sg.Text('Consultas',background_color='#4B5694', justification='center', expand_x=True, font=('Arial', 32))],
            [sg.Button(button_text='Alunos', key='-AlunosCon-', font=('Arial', 20), button_color= '#7288AE', size=(30,1))],
            [sg.Button(button_text='Disciplina', key='-DisciplinaCon-', font=('Arial', 20), button_color= '#7288AE', size=(30,1))],
            [sg.Button(button_text='Professor', key='-ProfessorCon-',font=('Arial', 20), button_color= '#7288AE', size=(30,1))],
            [sg.Button(button_text='Matricula', key='-MatriculaCon-',font=('Arial', 20), button_color= '#7288AE', size=(30,1))],
            [sg.Button(button_text='Turmas', key='-TurmasCon-', font=('Arial', 20), button_color= '#7288AE', size=(30,1))],
            [sg.Button(button_text='Voltar', key='-Voltar-', font=('Arial', 20), button_color= '#7288AE', size=(20,1), pad=(0,10))]]

def Notas():
    return [[sg.Text('Gerenciamento Escolar',background_color='#4B5694', justification='center', expand_x=True, font=('Arial', 32))],
            [sg.Button(button_text='Lançar Nota', key='-Cadastros-', font=('Arial', 20), button_color= '#7288AE', size=(30,1))],
            [sg.Button(button_text='Consultar Notts', key='-Consultas-',font=('Arial', 20), button_color= '#7288AE', size=(30,1))],
            [sg.Button(button_text='Alterar Notas', key='-Alteraçes-',font=('Arial', 20), button_color= '#7288AE', size=(30,1))],
            [sg.Button(button_text='Voltar', font=('Arial', 20), button_color= '#7288AE', size=(20,1), pad=(0,90))],
            ]

    
layout = [
        [sg.Column(Menu(), key='-Tela_Menu-', visible=True),
        sg.Column(Cadastros(), key='-Tela_Cadastros-', visible=False),
        sg.Column(Alteracoes(), key='-Tela_Alteracoes-', visible=False),
        sg.Column(Consultas(), key='-Tela_Consultas-', visible=False),
        sg.Column(Notas(), key='-Tela_Notas-', visible=False)]
        ]

window = sg.Window('Teste', layout, size=(900,500))
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == '-Cadastros-':
        MostrarTela('-Tela_Cadastros-')
    elif event == '-Alteracoes-':
        MostrarTela('-Tela_Alteracoes-')
    elif event == '-Consultas-':
        MostrarTela('-Tela_Consultas-')
    elif event == '-Notas-':
        MostrarTela('-Tela_Notas-')


window.close()             

