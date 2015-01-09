import csv

zyante = {}
# csv column layout on Zyante: 'Last name', 'First name', 'Email', 'Total'
with open("PennStateIST240Spring2015_report_2015-01-08_0042.csv", 'r') as zf:
    reader = csv.reader(zf)
    # skip the first row of csv which contains headers
    next(reader)
    for row in reader:
        # eamil as a key
        zyante[row[2].strip()] = float(row[3])
zf.close()

canvas = {}
# csv column layout on Canvas:'Student', 'ID', 'SIS User ID', 'SIS Login ID'
with open('Grades-Introduction_to_Computer_Languages_(402748,442069).csv', 'r') as cf:
    reader = csv.reader(cf)
    # skip the first two row of csv which contains headers
    next(reader)
    next(reader)
    for row in reader:
        if row[2].strip() in zyante.keys():
            canvas[row[2].strip()] = {'Student':row[0].strip(), 'ID':row[1].strip(), 'Section':row[4].strip(), 'Read chapters 1-3 and do exercises (6566548)':zyante[row[2].strip()]}
        else:
            # students who haven't register on Zyante yet
            print row[0]
cf.close()

with open('hw1_grade.csv', 'w') as of:
    # The output file contains only necessary columns: 'Student', 'ID', 'Section'
    header = ['Student', 'ID', 'Section', 'Read chapters 1-3 and do exercises (6566548)']
    writer = csv.DictWriter(of, fieldnames=header, lineterminator='\n')
    writer.writeheader()
    for row in canvas:
        writer.writerow(canvas[row])
of.close()



