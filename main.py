import PySimpleGUI as sg
import datetime
import sqlite3
from nbclient import execute
import pandas as pd

## Funções
def Menu():
    return [[sg.Text('Gerenciamento Escolar',background_color='#4B5694', justification='center', expand_x=True, font=('Arial', 32))],
            [sg.Button(button_text='Cadastros', key='-Cadastros-', font=('Arial', 20), button_color= '#7288AE', size=(30,1))],
            [sg.Button(button_text='Consultas', key='-Consultas-',font=('Arial', 20), button_color= '#7288AE', size=(30,1))],
            [sg.Button(button_text='Alterações', key='-Alteracoes-',font=('Arial', 20), button_color= '#7288AE', size=(30,1))],
            [sg.Button(button_text='Notas', key='-Notas-',font=('Arial', 20), button_color= '#7288AE', size=(30,1))],
            [sg.Button(button_text='Sair', key='-Sair-', font=('Arial', 20), button_color= '#7288AE', size=(20,1), pad=(0,70))],
            ]


def MostrarTela(nome_tela):
    window['-Tela_Menu-'].update(visible=False)
    window['-Tela_Cadastros-'].update(visible=False)
    window['-Tela_Alteracoes-'].update(visible=False)
    window['-Tela_Consultas-'].update(visible=False)
    window['-Tela_Notas-'].update(visible=False)
    window['-Tela_CadastroAluno-'].update(visible=False)

    window[nome_tela].update(visible=True)

def popup_sim_nao(mensagem, titulo='Confirmação'):
    layout = [
        [sg.Text(mensagem, font=('Arial', 14))],
        [
            sg.Button('Sim', key='Sim', size=(10, 1)),
            sg.Button('Não', key='Não', size=(10, 1))
        ]
    ]

    janela = sg.Window(titulo, layout, modal=True)

    event, values = janela.read()
    janela.close()
    return event


def apenas_numeros(texto):
    return ''.join(caractere for caractere in texto if caractere.isdigit())


def Cadastros():
    return [[sg.Text('Cadastros',background_color='#4B5694', justification='center', expand_x=True, font=('Arial', 32))],
            [sg.Button(button_text='Alunos', key='-AlunosCad-', font=('Arial', 20), button_color= '#7288AE', size=(30,1))],
            [sg.Button(button_text='Disciplina', key='-DisciplinaCad-', font=('Arial', 20), button_color= '#7288AE', size=(30,1))],
            [sg.Button(button_text='Professor', key='-ProfessorCad-',font=('Arial', 20), button_color= '#7288AE', size=(30,1))],
            [sg.Button(button_text='Matricula', key='-MatriculaCad-',font=('Arial', 20), button_color= '#7288AE', size=(30,1))],
            [sg.Button(button_text='Turmas', key='-TurmasCad-', font=('Arial', 20), button_color= '#7288AE', size=(30,1))],
            [sg.Button(button_text='Voltar', key='-Voltar_Cadastros-', font=('Arial', 20), button_color= '#7288AE', size=(20,1), pad=(0,10))]
            ]


def Alteracoes():
    return [[sg.Text('Alterações',background_color='#4B5694', justification='center', expand_x=True, font=('Arial', 32))],
            [sg.Button(button_text='Alunos', key='-AlunosAlt-', font=('Arial', 20), button_color= '#7288AE', size=(30,1))],
            [sg.Button(button_text='Disciplina', key='-DisciplinaAlt-', font=('Arial', 20), button_color= '#7288AE', size=(30,1))],
            [sg.Button(button_text='Professor', key='-ProfessorAlt-',font=('Arial', 20), button_color= '#7288AE', size=(30,1))],
            [sg.Button(button_text='Matricula', key='-MatriculaAlt-',font=('Arial', 20), button_color= '#7288AE', size=(30,1))],
            [sg.Button(button_text='Turmas', key='-TurmasAlt-', font=('Arial', 20), button_color= '#7288AE', size=(30,1))],
            [sg.Button(button_text='Voltar', key='-Voltar_Alteracoes-', font=('Arial', 20), button_color= '#7288AE', size=(20,1), pad=(0,10))]
            ]


def Consultas():
    return [[sg.Text('Consultas',background_color='#4B5694', justification='center', expand_x=True, font=('Arial', 32))],
            [sg.Button(button_text='Alunos', key='-AlunosCon-', font=('Arial', 20), button_color= '#7288AE', size=(30,1))],
            [sg.Button(button_text='Disciplina', key='-DisciplinaCon-', font=('Arial', 20), button_color= '#7288AE', size=(30,1))],
            [sg.Button(button_text='Professor', key='-ProfessorCon-',font=('Arial', 20), button_color= '#7288AE', size=(30,1))],
            [sg.Button(button_text='Matricula', key='-MatriculaCon-',font=('Arial', 20), button_color= '#7288AE', size=(30,1))],
            [sg.Button(button_text='Turmas', key='-TurmasCon-', font=('Arial', 20), button_color= '#7288AE', size=(30,1))],
            [sg.Button(button_text='Voltar', key='-Voltar_Consultas-', font=('Arial', 20), button_color= '#7288AE', size=(20,1), pad=(0,10))]]


def Notas():
    return [[sg.Text('Notas',background_color='#4B5694', justification='center', expand_x=True, font=('Arial', 32))],
            [sg.Button(button_text='Lançar Nota', key='-Cadastros-', font=('Arial', 20), button_color= '#7288AE', size=(30,1))],
            [sg.Button(button_text='Consultar Notts', key='-Consultas-',font=('Arial', 20), button_color= '#7288AE', size=(30,1))],
            [sg.Button(button_text='Alterar Notas', key='-Alteraçes-',font=('Arial', 20), button_color= '#7288AE', size=(30,1))],
            [sg.Button(button_text='Voltar', key='-Voltar_Notas-', font=('Arial', 20), button_color= '#7288AE', size=(20,1), pad=(0,90))],
            ]


def Cadastro_Alunos():
    return [[sg.Text('Cadastrar Aluno',background_color='#4B5694', justification='center', expand_x=True, font=('Arial', 32))],
            [sg.Text('Nome:', font=('Arial',20), size=(8,1)), sg.Input('Digite o nome' , key='-Nome_Aluno-',do_not_clear=True,font=('Arial',20), size=(40,1), text_color='gray')],
            [sg.Text('CPF:', font=('Arial',20), size=(8,1)), sg.Input('Apenas numeros', key='-CPF_Aluno-',do_not_clear=True,font=('Arial',20), size=(40,1), text_color='gray')],
            [sg.Text('Data de nascimento:', font=('Arial',20), size=(17,1)), sg.Input('dd/mm/aaaa', key='-Nascimento_Aluno-',do_not_clear=True,font=('Arial',20), size=(20,1), text_color='gray')],
            [sg.Text('Telefone:', font=('Arial',20), size=(8,1)), sg.Input('(00) 00000-0000', key='-Telefone_Aluno-',do_not_clear=True,font=('Arial',20), size=(30,1), text_color='gray')],
            [sg.Text('Endereço:', font=('Arial',20), size=(8,1)), sg.Input('Digite o endereço', key='-Endereco_Aluno-',do_not_clear=True,font=('Arial',20), size=(40,1), text_color='gray')],
            [sg.Button(button_text='Voltar', key='-Voltar_CadastroAluno-', font=('Arial', 20), button_color= '#7288AE', size=(20,1), pad=(0,30)),
             sg.Button(button_text='Salvar', key='-Salvar_CadastroAluno-', font=('Arial', 20), button_color= '#7288AE', size=(20,1), pad=(10,30))]
            ]


def Limpar_Cadastro():
    for key, texto in placeholders.items():
        window[key].update(texto, text_color='gray')


def Salvar_Cadastro_Alunos(values):
    nomeAluno = values['-Nome_Aluno-']
    nomeAluno = nomeAluno.upper()
    cpfAluno = values['-CPF_Aluno-']
    cpfAluno = cpfAluno.replace('.', '').replace('-', '').strip()
    nascimentoAluno = apenas_numeros(values['-Nascimento_Aluno-'])
    nascimentoAluno = nascimentoAluno.replace('/', '').strip()
    telefoneAluno = apenas_numeros(values['-Telefone_Aluno-'])
    telefoneAluno = telefoneAluno.replace('(','').replace(')','').replace('-','').strip()
    enderecoAluno = values['-Endereco_Aluno-']
    enderecoAluno = enderecoAluno.upper()
    cpfinvalido = 0
    nascimentoinvalido = 0
    telefoneinvalido = 0


    if len(cpfAluno) != 11 or not cpfAluno.isdigit():# Verificando se o CPF tem 11 dígitos e se é composto apenas por números
        cpfinvalido = 1
    elif len(nascimentoAluno) != 8 or not nascimentoAluno.isdigit() or nascimentoAluno[0:2] > '31' or nascimentoAluno[2:4] > '12' or nascimentoAluno[4:8] > str(datetime.datetime.now().year):# Verificando se a data de nascimento tem o formato correto e se os valores são válidos
        nascimentoinvalido = 1
    elif len(telefoneAluno) != 11 or not telefoneAluno.isdigit():
        telefoneinvalido = 1
    else:
        dia = int(nascimentoAluno[0:2])
        mes = int(nascimentoAluno[2:4])
        ano = int(nascimentoAluno[4:8])
        nascimentoAluno = str(ano) + '-' + str(mes) + '-' + str(dia)

    if cpfinvalido == 1:
        sg.popup_error('CPF invalido!',no_titlebar=True)
    elif nascimentoinvalido == 1:
        sg.popup_error('Data de Nascimento invalida!',no_titlebar=True)
    elif telefoneinvalido == 1:
        sg.popup_error('Telefone invalido',no_titlebar=True)
    else:
        cadastrar = popup_sim_nao('Deseja salvar o cadastro?')
        if cadastrar == 'Sim':
            cursor.execute('INSERT INTO Aluno (Nome, Data_nascimento, CPF, Telefone, Endereco) VALUES (?, ?, ?, ?, ?)', (nomeAluno, nascimentoAluno, cpfAluno, telefoneAluno, enderecoAluno))
            conn.commit()
            sg.popup('Aluno cadastrado com sucesso!',no_titlebar=True)
            continuar = popup_sim_nao('Deseja continuar cadastrando?')
            if continuar == 'Sim':
                Limpar_Cadastro()
            elif continuar == 'Não':
                MostrarTela('-Tela_Menu-')
        elif cadastrar == 'Não':
            sg.popup('Operação cancelada.')
        


database = 'escola.db'
conn = sqlite3.connect(database)
cursor = conn.cursor()

layout = [
        [sg.Column(Menu(), key='-Tela_Menu-', visible=True),
        sg.Column(Cadastros(), key='-Tela_Cadastros-', visible=False),
        sg.Column(Alteracoes(), key='-Tela_Alteracoes-', visible=False),
        sg.Column(Consultas(), key='-Tela_Consultas-', visible=False),
        sg.Column(Notas(), key='-Tela_Notas-', visible=False),
        sg.Column(Cadastro_Alunos(), key='-Tela_CadastroAluno-', visible=False)]
        ]
placeholders = {
    '-Nome_Aluno-': 'Digite o nome',
    '-CPF_Aluno-': 'Apenas numeros',
    '-Nascimento_Aluno-': 'dd/mm/aaaa',
    '-Telefone_Aluno-': '(00) 00000-0000',
    '-Endereco_Aluno-': 'Digite o endereço'
}

window = sg.Window('Teste', layout, finalize=True,size=(900,500))
for key in placeholders:
    window[key].bind('<FocusIn>', '+FOCUS_IN')
    window[key].bind('<FocusOut>', '+FOCUS_OUT')

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    #Menu Principal
    elif event == '-Cadastros-':
        MostrarTela('-Tela_Cadastros-')
    elif event == '-Alteracoes-':
        MostrarTela('-Tela_Alteracoes-')
    elif event == '-Consultas-':
        MostrarTela('-Tela_Consultas-')
    elif event == '-Notas-':
        MostrarTela('-Tela_Notas-')
    elif event == '-Sair-':
        break
    elif event in ('-Voltar_Cadastros-', '-Voltar_Alteracoes-', '-Voltar_Consultas-', '-Voltar_Notas-'):
        MostrarTela('-Tela_Menu-')
    #Configurações placeholders
    elif event.endswith('+FOCUS_IN'):
        key = event.replace('+FOCUS_IN', '')
        if values[key] == placeholders[key]:
            window[key].update('', text_color='black')
    elif event.endswith('+FOCUS_OUT'):
        key = event.replace('+FOCUS_OUT', '')
        if values[key] == '':
            window[key].update(placeholders[key], text_color='gray')
    #Cadastros            
    elif event in ('-Voltar_CadastroAluno-'):
        MostrarTela('-Tela_Cadastros-')
        Limpar_Cadastro()
    elif event == '-AlunosCad-':
        MostrarTela('-Tela_CadastroAluno-')
    elif event == '-Salvar_CadastroAluno-':
        Salvar_Cadastro_Alunos(values)

window.close()             

