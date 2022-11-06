import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('./Salary_Data.csv')

X = df['YearsExperience'].values
Y = df['Salary'].values
# our parameter w,b
w = 0.5 
b = 0.8
lr = 0.020
hypothesis = [] 
for e in range(100000):
    hypothesis = b + w*X
    Cost = (hypothesis - Y)
    temp = w - lr*np.mean(Cost*X)
    temp2 = b - lr*np.mean(Cost)
    #update our parameters
    w = temp 
    b = temp2
    print('w:',w,'\nb:',b,'\n')
    
print(np.mean(hypothesis))   
plt.scatter(X,Y,color='blue') 
plt.plot(X,hypothesis,color='red')
plt.show()   
    
    
