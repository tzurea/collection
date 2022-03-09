import sqlite3
import json
from datetime import date

con = sqlite3.connect("/home/zuplex/.usr/academic/engentrance/engdote/build/db/data.db")
cur = con.cursor()

cur.execute("SELECT * from daily_question_ids")
questions = cur.fetchall()

for value in questions:
    if value[1] == str(date.today()):
        last = value[2]

header = """---
title: "Daily Capsule"
author: [FSF, GNU Entrance Preparation]
date: "{}"
keywords: [Entrance, Capsule]
...""".format(date.today())

print(header)
print(str(date.today()))      
print()

count = 1
for index,talue in enumerate(json.loads(last)):
    string = "SELECT * FROM questions WHERE id=" + str(talue) +";"
    cur.execute(string)
    output = cur.fetchall()
    print(str(count) + "." + str(output[0][4]))
    print()
    print(output[0][5])
    print()
    print(output[0][6])
    print()
    print(output[0][7])
    print()
    print(output[0][8])
    print()
    count = count + 1
