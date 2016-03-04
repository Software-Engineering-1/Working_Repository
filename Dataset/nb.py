import nltk
import pickle
import math
import random

with open('data.pkl','rb') as f:
    [word_set,data,class_]=pickle.load(f)

with open('test.pkl','rb') as f:
    test_data=pickle.load(f)

'''test_data={i:data[i] for i in data if i>0.8*len(data)}
data={i:data[i] for i in data if i<=0.8*len(data)}'''

table={'Sales and Marketing':{},'Web Developer':{}}
def train():
    global p_c1,p_c2,prob,table
    c1=0
    c2=0
    for i in data:
       # print(type(i))
        if class_[i]=='Sales and Marketing':
            t=table['Sales and Marketing']
            c1+=1
            for word in data[i]:
                t[word]=t.get(word,0)+data[i][word]
        else:
            c2+=1
            t=table['Web Developer']
            for word in data[i]:
                t[word]=t.get(word,0)+data[i][word]
    p_c1=c1/float(c1+c2)
    p_c2=c2/float(c1+c2)
    prob={'Sales and Marketing':{},'Web Developer':{}}
    for i in table:
        t=table[i]
        denominator=float(sum(t.values()))
        prob[i]={j:t[j]/denominator for j in t}
#    print table


def test(test_data):
    count1=float(sum(table['Sales and Marketing'].values()))#corresponds to 2
    count2=float(sum(table['Web Developer'].values()))#corresponds to 1/3
    wrong=0
    for i in test_data:
        tweet=test_data[i]
        pt_c1=1
        pt_c2=1
        for word in tweet:
            pt_c1*=prob['Sales and Marketing'].get(word,1/count1)
            pt_c2*=prob['Web Developer'].get(word,1/(count2))
        pt_c1=pt_c1*p_c1
        pt_c2=pt_c2*p_c2
        if pt_c1>pt_c2:
            print('sales')
        else:
            print('dev')
#        print pt_c1,pt_c2
    #print wrong
    #print len(test_data)
    

print(test_data)
train()
test(test_data)
