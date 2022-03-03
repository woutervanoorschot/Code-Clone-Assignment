import csv
import matplotlib.pyplot as plt



jquerylengths = []

with open('lines.csv', mode='r') as inp:
    reader = csv.reader(inp)
    for row in reader:
        jquerylengths.append( [row[0],row[1],row[2],row[3], row[4], int(row[4])+int(row[3])+int(row[2]) ])

jquerylengths.sort(key = lambda x: [int(y) for y in x[0].split('.')])

print(jquerylengths)


versions = list([item[0] for item in jquerylengths])
values = list([item[5] for item in jquerylengths])
fig = plt.figure(figsize = (10, 5))
#  Bar plot
plt.bar(versions, values, color ='green',
        width = 0.5)
plt.xlabel("jQuery versions")
plt.ylabel("#lines")
plt.title("jQuery lines of code, comment and whitespace in versions")
plt.xticks(rotation=90)
plt.show()
