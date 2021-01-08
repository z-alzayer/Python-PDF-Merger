#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 22:42:27 2021

@author: ziad
"""

from PyPDF2 import PdfFileReader, PdfFileMerger



class pdfMerger():
    
    def __init__(self, files, outputFname):
        self.readers = []
        self.merger = PdfFileMerger()
        
        self.openFiles(files)
        self.mergeFiles(self.readers)
        
        self.merger.write('/home/ziad/Documents/Python/PDF_Merger/Python PDF Merger/test.pdf')
        
    def openFiles(self, files):
        for file in files:
            print(file)
            self.readers.append(PdfFileReader(file))
    
    def mergeFiles(self, fileReaders):
        for reader in fileReaders:
            print(reader)
            self.merger.append(reader)
