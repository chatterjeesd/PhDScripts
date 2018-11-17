#!/usr/bin/python
import numpy
import sys, glob
import string 
import itertools 

#This program checks the consistency between the NMR resonance assignments of two field data sets in Bruker protein dynamics software suit. This is important for Lipari-Szabo Model Free analysis to assign protein dynamics models.(Soumya Deep Chatterjee, Leiden University

#1. Enter the protein sequence with one-letter amino acid abbreviation followed by the sequence number. For e.g. A111 for Alanine 111.

sequence= ['R2','A3','I5','E7','K9','G11','D12','L13','I14','E15','I16','F17','R18','P19','F20','Y21','R22','H23','W24','A25','I26','Y27','V28','G29','D30','G31','Y32','V33','V34','H35','L36','A37','S40','E41','V42','A43','G44','A45','G46','A47','A48','S49','V50','M51','S52','A53','L54','T55','D56','K57','A58','I59','V60','K61','K62','E63','L64','L65','Y66','D67','V68','A69','G70','S71','D72','K73','Y74','Q75','V76','N77','N78','K79','H80','D81','D82','K83','Y84','S85','P86','L87','P88','C89','S90','K91','I92','I93','Q94','R95','A96','E97','E98','L99','V100','G101','Q102','E103','V104','L105','Y106','K107','L108','T109','V100','E111','N112','C113','E114','H115','F116','V117','N118','E119','L120','R121','Y122','G123','V124','A125']

#2. Enter the resonance assignments from HSQC.

assignment=['R2','A3','I5','E7','K9','G11','D12','L13','I14','E15','I16','F17','R18','F20','Y21','R22','H23','W24','A25','I26','Y27','V28','G31','Y32','V33','V34','H35','L36','A37','S40','E41','V42','A43','G44','G46','S49','V50','M51','S52','A53','L54','T55','D56','K57','A58','I59','V60','K61','K62','E63','L64','L65','Y66','D67','V68','A69','G70','S71','D72','K73','Y74','Q75','V76','N77','N78','K79','H80','D81','D82','K83','Y84','S85','L87','S90','K91','I92','I93','Q94','R95','A96','E97','E98','L99','V100','G101','Q102','E103','V104','L105','Y106','K107','L108','T109','E111','N112','C113','E114','H115','F116','V117','N118','E119','L120','R121','Y122','G123','V124','A125']

#3. Enter the file name for your peaklist xml file.
xmlpeaklist='peaklist.xml'

#-------Program Starts Here. Do Not Change the Code without permission-----
fo=open(xmlpeaklist,'r')
fr=open("test.txt", 'w')

fr.write("list= [")

for lines in fo: 
	if "annotation" in lines:
		data= lines.split()[4][12:-1]
		if data not in sequence:		
			print "Errors in the peaklist: "+str(data)
		fr.write("'"+data+"',")
fr.write("]"+"\n")
		
fr.close()
ft=open("test.txt", 'r')
for ps in ft:
	for ast in assignment:
		if ast not in ps:
			print ast
					
print "Peaks that couldnt be assigned by the authors:"+str(set(sequence).difference(set(assignment)))
fo.close()




