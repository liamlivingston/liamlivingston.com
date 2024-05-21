import csv
filename = "SSP_CMIP6_201811.csv"

fields = []
rows = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        if (not row[1] == "SSP3-LowNTCF" and not row[1] == "SSP5-34-OS"):
            for x in range(len(row)):
                try:
                    row[x] = round(float(row[x]), 2)
                except:
                    pass
            rows.append(row)
    print("Total no. of rows: %d" % (csvreader.line_num))

a = [fields]

for col in rows:
    if col[2] == "World" and col[3] == "CMIP6 Emissions|CO2":
        a.append(col)

with open('out.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(a)

print(a)