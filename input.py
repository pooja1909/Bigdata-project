import csv
from collections import defaultdict
def loadCsv(filename):
    clusterfile = open('output.csv', 'w')
    columns = defaultdict(list)
    f = open("input.csv", "rb")
    reader = csv.reader(f)
    headers = reader.next()
    clusterfile.write(headers[12])
    clusterfile.write(",")
    clusterfile.write(headers[13])
    clusterfile.write(",")
    clusterfile.write(headers[9])
    clusterfile.write("\n")
    with open("input.csv", "rb") as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            for (k,v) in row.items():
                columns[k].append(v)  
        
        for i in range(len(columns["Lon"])):
            clusterfile.write(columns["Lon"][i])
            clusterfile.write(",")
            clusterfile.write(columns["Lat"][i])
            clusterfile.write(",")
            clusterfile.write(columns["Text_General_Code"][i])
            clusterfile.write("\n")
def main():
    filename = 'input.csv'
    loadCsv(filename)
main()
