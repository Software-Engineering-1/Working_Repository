import re
import nltk
import pickle
from nltk.corpus import stopwords
stop=set(stopwords.words('english'))

word_set=set()
d=dict()
class_=dict()
index=0

def clean(tweet):
    global index,word_set,hashtag_set
    #remove spl chars
    tweet=re.sub(r'[?\.:;\"\'.\(\)]','',tweet)
    tweet=re.sub(r'[,]',' ',tweet)
    #make everything lower case
    tweet=tweet.lower()
    #remove word RT
    #tweet=re.sub('RT','',tweet)
    #remove @.*?
    tweet=re.sub(r'@\w+?\W','',tweet)
    #remove web-link
    tweet=re.sub(r'http\w?\W','',tweet)
    tweet=re.sub(r'technology','',tweet)
    #get hash-tags
    tweet=re.sub(r'(#\w+?)\W','',tweet)
    tweet=re.sub(r'\d','',tweet)
    list_words=nltk.word_tokenize(tweet)
    set_words=set(list_words)-stop
    d[index]=dict.fromkeys(set_words)
    for i in list_words:
        if i in set_words:
            d[index][i]=1 if d[index][i]==None else d[index][i]+1
    #for i in p:
     #   d[index][i]=1
    word_set|=set_words
#import csv
f=open('dbadmin.txt','r')
print(f)
line=f.readline()
#print(line)
while(line):
    line=f.readline()
    clean(line)
    class_[index]='Sales and Marketing'
    index+=1
    '''for i in f:
        clean(i[0])
        class_[index]=i[1]
data=[word_set,d,class_]
with open('data.py','wb') as f:
    pickle.dump(data,f)'''
f=open('webdev.txt','r')
print(f)
line=f.readline()
#print(line)
while(line):
    line=f.readline()
    clean(line)
    class_[index]='Web Developer'
    index+=1
print(class_)
data=[word_set,d,class_]
with open('data.pkl','wb') as f:
    pickle.dump(data,f)
