#!/usr/bin/env python

import csv
import sys


callsign = raw_input("Enter callsign: ")
operators = raw_input("Enter space separated list of operators: ")
score = raw_input("Enter claimed score: ")

csvfile = open(sys.argv[1], 'rt')
try:
    reader = csv.reader(csvfile)
    print '''
START-OF-LOG: 3.0
CONTEST: ARRL-VHF-SEP
CALLSIGN: {0}
LOCATION: EMA
OPERATORS: {1}
CATEGORY-ASSISTED: ASSISTED
CATEGORY-OPERATOR: MULTI-OP
CATEGORY-POWER: LOW
CATEGORY-STATION: ROVER-LIMITED
CATEGORY-TRANSMITTER: LIMITED
CLAIMED-SCORE: {2}
NAME: K1SIG
ADDRESS: PO Box 853
ADDRESS: Westford, MA 01824
SOAPBOX: 
'''.format(callsign,operators,score)
    for row in reader:
        logstring = "QSO: {0} {1} {2} {3} {4} {5} {6} {7}".format(row[0],row[1],row[2],row[3],'K1SIG/R',row[4],row[6],row[5])
        print logstring
    
    print "END-OF-LOG:"

finally:
    csvfile.close()

    
