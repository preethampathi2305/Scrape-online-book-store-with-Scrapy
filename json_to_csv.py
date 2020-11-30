import json,csv
with open('final.json') as f:
    d=json.load(f)

cfile= open('final.csv','w',newline='')
writ=csv.writer(cfile)
header=d[0].keys()
writ.writerow(header)

for i in d:
    writ.writerow(i.values())
cfile.close()