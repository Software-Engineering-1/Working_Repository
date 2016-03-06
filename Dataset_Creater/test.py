import nltk
import re
from nltk.corpus import stopwords
stop=set(stopwords.words('english'))
import pickle
word_set=set()
d=dict()
test_string=''
f=open('data_demo','r')
line=f.readline()
test_string+=line
print(f)
while(line):
      line=f.readline()
      print(line)
      test_string+=(' '+line)
clean(test_string)
print(test_string)
with open('testout.txt','w') as ff:
    ff.write(test_string)
'''with open('test.pkl','wb') as f:
    pickle.dump(d,f)'''
