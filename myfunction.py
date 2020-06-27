import nltk
from gap_scorer import *
from constants import *
from nltk import word_tokenize
from nltk import RegexpParser
from nltk.tree import ParentedTree
from bs4 import BeautifulSoup
from nltk import sent_tokenize
import requests
def index_to_sen_num(paragraph, index): #return order of sentence, index
    sent_list = sent_tokenize(paragraph)
    index = int(index)
    for i in range(1,len(sent_list)):
        sent_list[i] = " " + sent_list[i]   #first space is removed, so add
    sen_num = 0
    for sen in sent_list:
        index -= len(sen)
        sen_num += 1
        if(index < 0):
            return (sen_num-1, index+len(sen), sent_list[sen_num-1])

def index_to_word_num(sentence, word): #return order of word index
    word_list = word_tokenize(sentence)
    index = sentence.index(word)
    for i in range(1,len(word_list)):
        if(word_list[i]!="'s"):
            word_list[i] = " " + word_list[i]   #first space is removed, so add
    word_num = 0
    for word in word_list:
        index -= len(word)
        if(index < 0):
            return word_num
        word_num += 1
        
def next_tuple(sentence, word):
    pos_tags = nltk.pos_tag(word_tokenize(sentence))
    index = index_to_word_num(sentence, word)
    length = len(word_tokenize(word))
    try:
        return pos_tags[index+length]
    except:
        return (" "," ")

def next_next_tuple(sentence, word):
    pos_tags = nltk.pos_tag(word_tokenize(sentence))
    index = index_to_word_num(sentence, word)
    length = len(word_tokenize(word))
    try:
        return pos_tags[index+length+1]
    except:
        return (" "," ")
        
def before_tuple(sentence, word):
    pos_tags = nltk.pos_tag(word_tokenize(sentence))
    index = index_to_word_num(sentence, word)
    try:
        return pos_tags[index-1]
    except:
        return (" "," ")

def get_subject_in_sentence(sentence):
    pos_tags = nltk.pos_tag(word_tokenize(sentence))
    grammar = r"""
        NNP:   {<NNP>+} 
        """
    cp = nltk.RegexpParser(grammar)
    result = cp.parse(pos_tags)
    NNP_list = []
    Main_NNP_list = []
    for NNP in result.subtrees(filter=lambda x: x.label() == 'NNP'):
        n = []
        for N in NNP:
            n.append(N[0])
        n = " ".join(n)
        NNP_list.append(n)
    for NNP in NNP_list:
        if (before_tuple(sentence, NNP)[1] =="IN"  or before_tuple(sentence, NNP)[1] =="DT"):
            NNP_list.remove(NNP)
    for NNP in NNP_list:
        (word, tag) = next_tuple(sentence,NNP)
        if( ( word == ","and next_next_tuple(sentence,NNP)[1] == "NNP" ) or ( word == "is") or (word == "was") ) :
            #print(( word == ","and next_tuple(sentence,word)[1] == "NNP" ))
            Main_NNP_list.append(NNP)
    if(len(Main_NNP_list) == 0):
        if(len(NNP_list) == 0):
            return ["None"]
        else:
            return NNP_list
    else:
        return Main_NNP_list
def get_html(url):
    html = ""
    resp = requests.get(url)
    if resp.status_code == 200:
        _html = resp.text
    else :
        return None 
    return _html

def get_gender(word):   #0:defualt  1:male  2:female    3:both  ignore Abbreviation name now => improvement
    if(word.lower() in ["he","his","him"]):
        return 1
    elif(word.lower() in ["she","her","hers"]):
        return 2
    URL = "https://en.wiktionary.org/wiki/"+word
    html = get_html(URL)
    if(html == None):
        return 0
    soup = BeautifulSoup(html, 'html.parser')
    category = soup.find("div",
        {"class": "mw-normal-catlinks"})
    if(category==None): 
        return 0
    female = category.find("a",
        {"title": "Category:English female given names"})      
    male = category.find("a",
        {"title": "Category:English male given names"})      
    if(male == None and female ==None):
        return 0
    elif(male !=None and female == None):
        return 1
    elif(male ==None and female != None):
        return 2    
    elif(male !=None and female != None):
        return 3
if __name__ == "__main__":
    print(get_gender("Mike"))