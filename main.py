import csv

with open('bday.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t on {row[0]} a {row[3]} {row[1]} was made at {row[2]} for ${row[4]}')
            line_count += 1
    print(f'Processed {line_count} lines.')