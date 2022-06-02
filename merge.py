import csv
dataset1 = []
dataset2 = []

with open("final.csv") as f:
    csvReader = csv.reader(f)
    for row in csvReader:
        dataset1.append(row)

with open("dataSorted1.csv") as f:
    csvReader = csv.reader(f)
    for row in csvReader:
        dataset2.append(row)

headers1 = dataset1[0]
planet_data1 = dataset1[1:]
headers2 = dataset2[0]
planet_data2 = dataset2[1:]

headers = headers1 + headers2
planet_data = []
for index, dataRow in enumerate(planet_data1):
    planet_data.append(planet_data1[index]+ planet_data2[index])

with open("mergedDataset.csv", "a+")as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(planet_data)