#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 22:28:38 2021

@author: ziad
"""


import PySimpleGUI as sg


def MakeMainWindow(PDF_List):
    layout = [[sg.Text('PDF Merger'), sg.Text('      ', k='-OUTPUT-')],
              [sg.T('PDFs')],
              [sg.Listbox(values=PDF_List, size=(100, 12), key='-LIST-', enable_events=True)],
              [sg.FileBrowse('Add PDF', key="-IN-", change_submits=True, file_types=(("pdf files", "*.pdf"),("all files","*.*"))), sg.Button("Confirm File")],
              [sg.FileBrowse('Save Directory', key="-OUT-", change_submits=True), sg.Input("")],
              [sg.Button("Remove PDF"), sg.Button('Merge'), sg.Button('Exit')]]

    return sg.Window('Window Title', layout, location=(800,600), finalize=True,
                     size = (400,400))


