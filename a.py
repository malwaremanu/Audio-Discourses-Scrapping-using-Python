import os, json, requests
os.system("clear")

url = "https://oshoworld.com/wp-content/uploads/2020/11/Hindi%20Audio/"

data = open("conent.html")

discs = set()
dicts = {}
for d in data:
    ddd = d.split('###')[1][:-7]
    name = d.split('###')[1]    
           
    print(url + name)
    os.system("wget " + url + name )    