import os 
files = [i for i in os.listdir(os.getcwd())]
for i in files: 
  if i.endswith('ore'):
    return False
return True
  
