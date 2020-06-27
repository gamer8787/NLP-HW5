import pickle
from myfunction import *
f = open("gap-development.tsv", 'r')
data = f.read()
line = data.split("\n")[1:-1]
line_list = []
for l in line:
    a = l.split("\t")
    line_list.append(a)

with open('list.txt', 'wb') as f2:
    for i,line in enumerate(line_list[20:40]):
        print(i)
        gender_pro = get_gender(line[2])
        gender_A = get_gender(line[4].split(" ")[0])
        gender_B = get_gender(line[7].split(" ")[0])
        pickle.dump([gender_pro, gender_A, gender_B], f2)
with open('list.txt', 'rb') as f2:
    while(True):
        try:
            data = pickle.load(f2)
        except :
            break
        print(data)