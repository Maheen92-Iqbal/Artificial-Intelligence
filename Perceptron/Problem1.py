import csv
import math
import numpy as np
import matplotlib.pyplot as plt

files = 'D:/python/Artificial Intelligence/Perceptron/input1.csv'

pairs = list()

with open(files, 'rb') as filename:
    
    reader = csv.reader(filename)
    
    for row in reader:
        
        pairs.append(((1,int(row[0]),int(row[1])),int(row[2])))
        
        
output_label = 0
weight_set = [1,0,0]

list_set = pairs
iteration = 0
learned = True

while learned:
    
   error = 0
   for i in range(0,len(list_set)):
    
     data = list_set[i]
    
     weighted_data = weight_set[0]*data[0][0] + weight_set[1]*data[0][1] + weight_set[2]*data[0][2]
     output_label = math.sin(weighted_data)
    
     if output_label >= 0:
       output_label = 1
     else:
       output_label = -1
       
     if output_label == 1:
         plt.plot(data[0][1],data[0][2],'or')
     elif output_label == -1:
         plt.plot(data[0][1],data[0][2],'ob')

     if output_label != data[1]:
       error_rate = data[1]-output_label
       updated_value = [a*(error_rate)*0.001 for a in data[0]]
       weight_set = [a+b for a,b in zip(updated_value,weight_set)]
       
       error += abs(error_rate)
   
   iteration += 1
   
   ymin, ymax = plt.ylim()
   xx = np.linspace(ymin, ymax)
   yy = (weight_set[1] * xx + weight_set[0])/ -weight_set[2]
   plt.plot(yy,xx, 'k-')
   
   
   if error == 0 or iteration >=1000:
      print iteration
      learned = False
      
plt.show()
   
