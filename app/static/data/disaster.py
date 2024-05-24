import csv
filename = "natural-disasters.csv"

fields = []
rows = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
            rows.append(row)
    print("Total no. of rows: %d" % (csvreader.line_num))

a = []

for col in rows:
    if col[0] == "Japan":
        a.append([col[0], col[1], col[32]])

with open('japan.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(a)

print(a)
a = []

for col in rows:
    if col[0] == "Philippines":
        a.append([col[0], col[1], col[32]])

with open('philippines.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(a)

print(a)