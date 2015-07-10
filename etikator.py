#!/usr/bin/env python

# etikreator.py
#

# Copyright 2015 Jorge Tornero Nunez http://imasdemase.com
#
# This file is part of Etikreator, V1.0
#
# Etikreator is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Etikreator is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Etikreator. If not, see <http://www.gnu.org/licenses/>.

import sys
import socket
from PyQt4 import QtCore, QtGui
import labelprinter

class Etikator(QtGui.QMainWindow):
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.dlg = labelprinter.Ui_LabelPrinter()
        self.dlg.setupUi(self)
         
        
        self.dlg.lab_date.setDate(QtCore.QDate.currentDate())
        ip_validator=QtGui.QRegExpValidator(QtCore.QRegExp("((1{0,1}[0-9]{0,2}|2[0-4]{1,1}[0-9]{1,1}|25[0-5]{1,1})\\.){3,3}(1{0,1}[0-9]{0,2}|2[0-4]{1,1}[0-9]{1,1}|25[0-5]{1,1})"))
        self.dlg.printer_ip.setValidator(ip_validator)
        self.dlg.printer_ip.setInputMask("000.000.000.000")
        
        self.dlg.print_lab_labels_btn.clicked.connect(self.process_lab_labels)
        self.dlg.print_srv_labels_btn.clicked.connect(self.process_srv_labels)
        
    def process_srv_labels(self):
        # Gather values for label fields
        survey_text = self.dlg.srv_survey_combo.currentText()
        srv_species_text = self.dlg.srv_species_combo.currentText()
        haul_number = "Pesca %i" %self.dlg.srv_haul_spinbox.value()
        srv_start_number =self.dlg.srv_start_spinbox.value()
        srv_end_number = self.dlg.srv_end_spinbox.value()

        labels=self.create_labels(survey_text,srv_species_text,haul_number,srv_start_number,srv_end_number)
        
        self.send_labels_to_printer(labels)
        
    
    def process_lab_labels(self):
        # Gather values for label fields
        # Gather values for label fields
        lab_origin_text = unicode(self.dlg.lab_origin_combo.currentText())
        lab_species_text = self.dlg.lab_species_combo.currentText()
        lab_date_text =self.dlg.lab_date.date().toString('dd/MM/yyyy')
        lab_start_number =self.dlg.lab_start_spinbox.value()
        lab_end_number = self.dlg.lab_end_spinbox.value()
          
        labels=self.create_labels(lab_species_text,lab_origin_text,lab_date_text,lab_start_number,lab_end_number)
        
        self.send_labels_to_printer(labels)
    
    def send_labels_to_printer(self,labels):
        
        printer_ip = self.dlg.printer_ip.text()
        printer_port = self.dlg.printer_port.value()
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((printer_ip, printer_port))
        
        font_selection_command = """
                                 ^XA
                                 ^CWI,E:GIL000.FNT^
                                 ^CWJ,E:GIL001.FNT^
                                 ^CWK,E:GIL002.FNT^
                                 ^XZ
                                 """
        sock.send(font_selection_command.encode('utf-8'))
        for label in reversed(labels):
            print label
            sock.send(label.encode('utf-8'))
        sock.close()
    
    def create_labels(self,line1,line2,line3,start,end):
        
        labels = []
        
        tens=int(start/10)
        plate_start = start
        plate_end = (tens+1)*10
        
        while True:
                
                
                
                if plate_end >= end:
                    plate_end = end
                    print '----',tens, plate_start,plate_end
                    label = """
                                ^XA
                                ^CI28
                                ^PW305
                                ^FO0,30^FB250,3,0,C,0^AK,21^FD%s\&%s\&%s^FS
                                ^FO60,30^FB400,3,0,C,0^AI,24^FD%i\&a\&%i^FS
                                ^XZ"""%(line1,line2,line3,plate_start,plate_end)
                    labels.append(label)
                    break
                
                
                
                else:
                    print tens, plate_start,plate_end
                    label = """
                                ^XA
                                ^CI28
                                ^PW305
                                ^FO0,30^FB250,3,0,C,0^AK,20^FD%s\&%s\&%s^FS
                                ^FO60,30^FB400,3,0,C,0^AI,24^FD%i\&a\&%i^FS
                                ^XZ"""%(line1,line2,line3,plate_start,plate_end)
                    labels.append(label)
                    tens+=1
                    plate_end = (tens+1)*10
                    plate_start = (tens*10)+1
        
                
            
        
        return labels

    
app=QtGui.QApplication(sys.argv)
etik = Etikator()
etik.show()
sys.exit(app.exec_())
