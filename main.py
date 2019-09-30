import csv

mydict = {}

with open('bday.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    mydict = {}
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t on {row[0]} a {row[3]} {row[1]} was made at {row[2]} for ${row[4]}')
            if row[3] in mydict:
                mydict[row[3]] += float(row[4])
            else:
                mydict[row[3]] = float(row[4])

            line_count += 1
    print(f'Processed {line_count} lines.')

    for k, v in mydict.items():
        mydict[k] = round(v,2)

    print(mydict)

