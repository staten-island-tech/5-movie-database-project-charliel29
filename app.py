import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)



""" a=0 """
"""  2018 > (data[a]['year']) > 2014 :
     prinfor i in data:
    ift (data[a]['title'])
    a=a+1 """
""" for i in data:
    if (data[a]['year']) == 2023 :
      print (data[a]['title'])
    a=a+1 """


def movie():
    a=0
    for i in data:
        print (data[a]['title'])
        a=a+1
    x = input("What movie you looking for")
    a=0
    for i in data:
        if x == (data[a]['title']):
            print (data[a])
        a=a+1
movie()



def genre():
