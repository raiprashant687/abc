from pathlib import Path
import csv
import os
configfiledir = 'config'
file_name = 'Info.csv'


basedir = Path(__file__).resolve().parent.parent
file_new = basedir.joinpath(configfiledir).joinpath(file_name)

def getdatafromcsv():
    with open (file_new,'r') as csvfile:
        m = csv.reader(csvfile)
        next(m)
        data = [tuple(row) for row in m ]
        return data

