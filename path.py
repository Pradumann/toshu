import time
import os 
import pandas

while True:
    if os.path.exists("Files/temps_today.csv"):
        data = pandas.read_csv("Files/temps_today.csv")   
        print(data.mean())  
    
    else:
        print("File does not exists.")
    time.sleep(10)    