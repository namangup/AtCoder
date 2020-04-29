import json
import csv
from scrape import gen_json
from sys import argv

usernames = []
with open(argv[1],'r') as f:
    fr = csv.reader(f, delimiter=',')
    for row in fr:
        usernames.append(row[1].strip())

print(usernames)
contest = argv[2]
gen_json(contest)

with open('ranklist.json', 'r') as f:
    data = json.load(f)

ranks = []
f = open('ranks.csv', 'w')
fw = csv.writer(f, quoting=csv.QUOTE_ALL)
data = data["StandingsData"]
for i in data:
    if (i['UserName'] in usernames):
        fw.writerow([i['UserName'], i['Rank']])

f.close()