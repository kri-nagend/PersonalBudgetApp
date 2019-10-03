import csv
import os
import shutil
import pandas as pd
import glob

def sayHey(location):
    print("From csvHanlder")

def getRange(location):
    with open(location) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        mydict = {}
        x = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                if row[0][0:7] in mydict:
                    mydict[row[0][0:7]] += 1
                else:
                    mydict[row[0][0:7]] = 1


        print(mydict)


def read(location):
    with open(location) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        mydict = {}
        sept = {}
        x = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                # print(f'\t on {row[0]} a {row[3]} {row[1]} was made at {row[2]} for ${row[4]}')
                if row[3] in mydict:
                    mydict[row[3]] += float(row[4])
                else:
                    mydict[row[3]] = float(row[4])

                if row[0][6] == '9':
                    if row[3] in sept:
                        sept[row[3]] += float(row[4])
                    else:
                        sept[row[3]] = float(row[4])

                print(row[0][0])

                line_count += 1
        print(f'Processed {line_count} lines.')

        del mydict['PAYMENT']

        for k, v in mydict.items():
            mydict[k] = round(v, 2)
            x += v

        for k, v in sept.items():
            sept[k] = round(v, 2)
            x += v
        mydict['TOTAL'] = round(sum(mydict.values()), 2)
        print(mydict)
        print(sept)
        return mydict
