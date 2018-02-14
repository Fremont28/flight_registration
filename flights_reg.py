
import json 
f=open("manila_flights.json","r")
flights_x=json.load(f)
flights_x.keys
type(flights_x) #dictionary 

#check if long/lat exists in the dataframe
match=[i for i in x1 if "Lat" in i]
len(match) #6654 

array_xx=np.arange(1,6654)
#convert array to a list 
list_xx=np.array(array_xx).tolist() 

#output lat/long
for i in list_xx:
    print(match[i]["Lat"],match[i]["Long"])

#outputs country   
country=[]
for i in list_xx:
    print(match[i]["Cou"])
