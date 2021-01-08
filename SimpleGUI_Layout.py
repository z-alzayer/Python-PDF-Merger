#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 22:28:38 2021

@author: ziad
"""


import PySimpleGUI as sg

PDF_List = []

def MakeMainWindow():
    layout = [[sg.Text('PDF Merger'), sg.Text('      ', k='-OUTPUT-')],
              [sg.T('PDFs')],
              [sg.Listbox(values=PDF_List, size=(20, 12), key='-LIST-', enable_events=True)],
              [sg.Button('Add PDF'), sg.Button('Merge'), sg.Button('Exit')]]

    return sg.Window('Window Title', layout, location=(800,600), finalize=True)




window = MakeMainWindow()

while True:             # Event Loop
    window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'Add PDF':
        PDF_List.append("added pdf")
        window.Element('-LIST-').Update(values=PDF_List)
window.close()