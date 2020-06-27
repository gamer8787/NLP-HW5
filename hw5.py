import nltk
from gap_scorer import *
from constants import *
from nltk import word_tokenize
from bs4 import BeautifulSoup
import requests
from myfunction import *
import csv
#print (run_scorer("gap-test.tsv", "gap-system_output (example).tsv" ))
f = open("gap-development.tsv", 'r')
data = f.read()
line = data.split("\n")[1:-1]
line_list = []
for l in line:
    a = l.split("\t")
    line_list.append(a)
print(len(line_list))
# 1: text   2: pronoun  3: pronoun offset   4:A     5:A-offset    6:A-TF     7:B     8:B-offset      9:B-TF      10:URL
f_write = open("develop_check.tsv", "w",-1, "utf-8", newline='') 
wr = csv.writer(f_write, delimiter='\t')
for i,line in enumerate(line_list):
    print(i+1)
    paragraph_to_line = sent_tokenize(line[1]) 
    a_line = paragraph_to_line[index_to_sen_num(line[1],line[5])[0]]
    b_line = paragraph_to_line[index_to_sen_num(line[1],line[8])[0]]
    A = get_subject_in_sentence(a_line)[0] in line[4]
    B = get_subject_in_sentence(b_line)[0] in line[7]
    wr.writerow(['development-'+str(i+1), A, B])