import numpy as np

def calculate(list):
  if len(list)==9:
    map(int, list)
    arr = np.array(list)
    arr = arr.reshape(3,3)
    calculations = {}
    calculations['mean'] = [arr.mean(axis = 0) , arr.mean(axis = 1) , arr.flatten().mean()]
    calculations['variance'] = [arr.var(axis = 0) , arr.var(axis = 1) , arr.flatten().var()]
    calculations['standard deviation'] = [arr.std(axis = 0) , arr.std(axis = 1) , arr.flatten().std()]
    calculations['max'] = [arr.max(axis = 0) , arr.max(axis = 1) , arr.flatten().max()]
    calculations['min'] = [arr.min(axis = 0) , arr.min(axis = 1) , arr.flatten().min()]
    calculations['sum'] = [arr.sum(axis = 0) , arr.sum(axis = 1) , arr.flatten().sum()]
    for key , value in calculations.items():
      for i in range(len(value)):
        value[i] = value[i].tolist()
    
    return calculations
  else:
    raise ValueError("List must contain nine numbers.")
 
  