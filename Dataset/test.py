import nltk
import re
from nltk.corpus import stopwords
stop=set(stopwords.words('english'))
import pickle

word_set=set()
d=dict()
index=0
def clean(tweet):
    global index,word_set
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

test_string=''
f=open('test.txt','r')
line=f.readline()
test_string+=line
print(f)
while(line):
      line=f.readline()
      test_string+=(' '+line)
clean(test_string)
with open('test.pkl','wb') as f:
    pickle.dump(d,f)
