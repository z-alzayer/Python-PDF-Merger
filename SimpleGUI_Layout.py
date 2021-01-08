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
              [sg.Listbox(values=PDF_List, size=(100, 12), key='-LIST-', enable_events=True)],
              [sg.FileBrowse('Add PDF', key="-IN-", change_submits=True), sg.Button("Confirm File")],
              [sg.Button("Remove PDF"), sg.Button('Merge'), sg.Button('Exit')]]

    return sg.Window('Window Title', layout, location=(800,600), finalize=True,
                     size = (400,400))


window = MakeMainWindow()

while True:             # Event Loop
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event  == 'Remove PDF':
        PDF_List.pop(-1)
        window.Element('-LIST-').Update(values=PDF_List)
    elif event == 'Confirm File':
        PDF_List.append(values["-IN-"])
        window.Element('-LIST-').Update(values=PDF_List)
    elif event == "Merge":
        print("Merging PDFS")


window.close()