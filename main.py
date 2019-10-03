import csv
import os
import shutil
import pandas as pd
import glob

path = r'./Files/RogersMC/'
frame = pd.concat([pd.read_csv(f, sep=',') for f in glob.glob(path + "/*.csv")], ignore_index=True)

frame.to_csv( "./Files/RogersMC/res/combined_csv.csv", index=False, encoding='utf-8-sig')

with open('./Files/RogersMC/res/combined_csv.csv') as csv_file:
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
        mydict[k] = round(v,2)
        x += v

    for k, v in sept.items():
        sept[k] = round(v,2)
        x += v
    mydict['TOTAL'] = round(sum(mydict.values()),2)
    print(mydict)
    print(sept)