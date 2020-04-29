import json
import csv
from scrape import gen_json
from sys import argv

contest = argv[1]
gen_json(contest)

with open('ranklist.json', 'r') as f:
    data = json.load(f)

username = [] # Get usernames from a file
ranks = []
f = open('ranks.csv', 'w')
fw = csv.writer(f, quoting=csv.QUOTE_ALL)
data = data["StandingsData"]
for i in data:
    if (i['UserName'] in username):
        fw.writerow([i['UserName'], i['Rank']])

f.close()