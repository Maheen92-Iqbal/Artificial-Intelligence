import csv
import ast
import numpy as np
import matplotlib.pyplot as plt

files = 'D:/python/Artificial Intelligence/Linear Regression/input2.csv'

inputs = list()
height = list()
age = list()
weight = list()
x_data = list()
y_data = list()

with open(files, 'rb') as filename:
    
    reader = csv.reader(filename)
    
    for row in reader:
        
        age.append(ast.literal_eval(row[0]))
        weight.append(ast.literal_eval(row[1]))
        inputs.append([ast.literal_eval(row[0]),ast.literal_eval(row[1])])
        height.append(ast.literal_eval(row[2]))
    
for i in range(0,len(inputs)):
    
    inputs[i][0] = (inputs[i][0] - np.mean(age))/np.std(age)
    inputs[i][1] = (inputs[i][1] - np.mean(weight))/np.std(weight)
    x_data.append(inputs[i][0])
    y_data.append(inputs[i][1])
    
    
Betas = [1,0,0]
alpha = 0.9
learned = True
iteration = 0
while learned:
    
  loss1 = []
  loss2 = []
  loss3 = []
  
  for i in range(0,len(x_data)):
    
    predicted_label = Betas[0]*1 + Betas[1]*x_data[i] + Betas[2]*y_data[i]
    loss1.append((predicted_label - height[i])*1)
    loss2.append((predicted_label - height[i])*x_data[i])
    loss3.append((predicted_label - height[i])*y_data[i])
    
  Betas[0] = Betas[0] - (alpha*(1.0/len(x_data)))*sum(loss1)
  Betas[1] = Betas[1] - (alpha*(1.0/len(x_data)))*sum(loss2)
  Betas[2] = Betas[2] - (alpha*(1.0/len(x_data)))*sum(loss3)
 
  iteration += 1
  
  if iteration >= 100:
      learned = False

result = []
x,y = np.meshgrid(x_data,y_data)

for i in range(0,len(x_data)):
    
    result.append(Betas[0]*1 + Betas[1]*x[i] + Betas[2]*y[i])

fig = plt.figure()
plot3d = fig.gca(projection='3d')
plot3d.plot_surface(x,y,result, color='blue', alpha=0.2)
plot3d.scatter(x_data,y_data, height, s=20, color='red',marker='*')

plt.gca().set_xlabel('AGE')
plt.gca().set_ylabel('WEIGHT')
plt.gca().set_zlabel('HEIGHT')
plt.gca().set_title('LINEAR REGRESSION')
plt.show()
