from nltk import word_tokenize
from gap_scorer import *
#print(run_scorer("gap-development.tsv","develop_check.tsv"))
print(run_scorer("gap-test.tsv","test_check.tsv"))