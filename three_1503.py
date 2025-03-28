
#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import random


file = open('metric.csv', 'w')

par = int(input("Insert Interval:"))
name = input("Insert Name:")
file.writelines(name)
measure = input("insert measure:")
file.writelines(measure)
sred = 0
numb = 0

list = []

for i in range(60):
    ran =random.randint(((-1)*par),par)
    sred += ran
    numb+=1
    list.append(str(sred/numb))
    time.sleep(1)
    print(sred/numb)

file.write("\n".join(list).join("\n"));


