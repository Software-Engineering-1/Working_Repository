import nltk
import numpy as n
import pickle
import time
class Softmax:
      def __init__(self,k,x,classes,epochs,alpha):
            self.x=x.T
            self.m=x.shape[0]
            self.n=x.shape[1]
            self.k=k
            self.classes=classes
            self.alpha=alpha
            self.epochs=epochs
            rand = n.random.RandomState(int(time.time()))
            self.theta = 0.005 * n.asarray(rand.normal(size = (self.k*self.n, 1)))
            self.theta=self.theta.reshape(self.k,self.n)
            #print(self.n)
            self.ans=[1,1]
      def compute_truth(self):
            truth=n.zeros((self.k,self.m))
            count=0
            for i in n.nditer(self.classes.T):
                  i=int(i)
                  truth[i,0]=1
                  count+=1
            return(truth)
      
      def cost_function(self):
            truth=self.compute_truth()
            thetadotx=n.dot(self.theta,self.x)
            hypo=n.exp(thetadotx)
            probs=hypo/n.sum(hypo,axis=0)
            probsbytruth=n.multiply(truth, n.log(probs))
            cost= -(n.sum(probsbytruth)/(self.m))

            gradient = -1 * (n.dot(truth - probs,n.transpose(self.x)))
            gradient = gradient / self.m
            gradient = n.array(gradient)
            #theta_grad = theta_grad.flatten()
            return([cost,gradient])
            
      def grad_descent(self):
            for i in range(self.epochs):
                  self.ans=self.cost_function()
                  gradient=self.ans[1]
                  self.theta=self.theta-n.multiply(self.alpha,gradient)

      def test_vals(self,test_data):
            m1=test_data.shape[1]
            n1=test_data.shape[0]
            thetadotx=n.dot(self.theta,test_data)
            hypo=n.exp(thetadotx)
            probs=hypo/n.sum(hypo,axis=0)  # k x m matrix
            for i in range(m1):
                  matrix=n.zeros((3,1))
                  #matrix[:,1]=n.arange(3)
                  matrix[:,0]=test_data[:,m1]
                  job=n.max(matrix[:,0])
                  #top_job_list=find_top(matrix)
                  print('For the example %d, the tope jobs are :-',i)
                  print(job)
            

with open('params.pkl','rb') as f:
      data=pickle.load(f)
      x=data[0]
      classes=data[1]
softmax=Softmax(3,x,classes,100,0.5)
softmax.grad_descent()
print(softmax.theta)
print("ok........................")
