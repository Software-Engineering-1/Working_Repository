import csv
jobs = {}
jobs=dict.fromkeys(set(range(226)))
v=[]
class_list=[]
classes=class_dict={}
glob_count=0
import numpy as n
import pickle
'''with open('skills_small.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        if(row[0] in dict_jobs.keys()):
            dict_jobs[row[0]].append(row[1])
        else:
            dict_jobs[row[0]] = [row[1]]'''

for i in jobs:
    jobs[i]={}

def vocab():
    global v,jobs,classes,glob_count
    ff=open('skills_small.csv','rb')
    reader = csv.reader(ff, delimiter=',')
    count=0
    for row in reader:
        if(row[1] not in v):
            v.append(row[1])
        count+=1
    glob_count=count

def get_vocab():
    global v,jobs,classes,class_list,class_dict,glob_count
    ff=open('skills_small.csv','rb')
    reader = csv.reader(ff, delimiter=',')
    count=0
    for row in reader:
        jobs[count]=dict.fromkeys(set(v))
        jobs[count][row[1]]=1
        if(row[1] not in v):
            v.append(row[1])
        class_list.append(row[0])
        count+=1
    class_set=set(class_list)
    class_dict=dict.fromkeys(class_set)
    count=0
    for i in class_dict:
        class_dict[i]=count
        count+=1
    print(class_dict)
    count=0
    ff=open('skills_small.csv','rb')
    reader = csv.reader(ff, delimiter=',')
    classes=dict.fromkeys(set(range(glob_count)))
    for row in reader:
        print('sgf')
        classes[count]=class_dict[row[0]]
        count+=1


def complete_dict():
    for i in jobs:
        print(jobs[i])

def make_array():
    x=n.zeros((len(v),glob_count))
    for j in range(glob_count):
        for i in range(len(v)):
            if(jobs[j][v[i]]==None):
                x[i,j]=0
            else:
                x[i,j]=1
    return(x)
def make_classes():
    y=n.zeros((glob_count,1))
    for i in classes:
        y[i,0]=classes[i]
    return(y)

vocab()
get_vocab()
complete_dict()
x1=make_array()
y1=make_classes()
with open('params.pkl','wb') as dump_file:
    pickle.dump([x1,y1],dump_file)
