import csv
data = []
with open("data.csv") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        data.append(row)

headers = data[0]
planet_data = data[1:]
for dataPoint in planet_data:
    dataPoint[2] = dataPoint[2].lower()

planet_data.sort(key = lambda planet_data:planet_data[2])

with open("dataSorted.csv", "a+") as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(planet_data)

with open ("dataSorted.csv")as input, open("dataSorted1.csv","w",newline = "")as output:
    writer = csv.writer(output)
    for row in csv.reader(input):
        if any(field.strip() for field in row):
            writer.writerow(row)