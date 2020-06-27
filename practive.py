from nltk import word_tokenize
from nltk import RegexpParser
from nltk import sent_tokenize
import nltk
from myfunction import *
text = "Phoebe Thomas played Cheryl Cassidy, Pauline's friend and also a year 11 pupil in Simon's class."
text2 = "Michael Billington in The Guardian wrote ``Few dramatists in history have painted a more devastating picture of the emotional damage wrought by bullying men,'' and described Martin's misguided affection for his girlfriends as ``an instant image of a grisly inheritance''"
text3 = "Reb Asher's brother Rabbi Shlomo Arieli is the author of a critical edition of the novallae of Rabbi Akiva Eiger"
print(nltk.pos_tag(word_tokenize(text2)))
print(get_subject_in_sentence(text2))
