import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)



a=0
for i in data:
    if 2018 > (data[a]['year']) > 2014 :
     print (data[a]['title'])
    a=a+1
for i in data 
