#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 00:58:15 2021

@author: ziad
"""


from pdfMerge import pdfMerger
from SimpleGUI_Layout import MakeMainWindow
import PySimpleGUI as sg


PDF_List = []

window = MakeMainWindow(PDF_List)

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
        pdfMerger(PDF_List , values['-OUT-'])


window.close()