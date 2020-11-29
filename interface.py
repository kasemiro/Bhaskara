from PySimpleGUI import PySimpleGUI as sg

#layout
sg.theme ('Reddit')
layout = [
    [sg.Text('Valor de Ax²'), sg.Input(key='Valor de A')],
    [sg.Text('Valor de Bx'), sg.Input(key='Valor de B')],
    [sg.Text('Valor de C'), sg.Input(key='Valor de C')]
    
]