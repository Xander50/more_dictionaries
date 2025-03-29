# food = {
#     "food1":"Chicken",
#     "food2":"Apple",
#     "food3":"Pork",
#     "food4":"crackers"
# }

# print(food["food2"])

# countries = {
#     "Country1":"U.S.A",
#     "Country2":"Brazil",
#     "Country3":"Russia",
#     "Country4":"Haiti",
#     "Country5":"Dominique Republic"
# }

# for country in countries:
#     print(country)

# for country in countries:
#     c = countries[country]
#     print(c)

# friends={
#     "friend1":"Alexandre",
#     "friend2":"Jalil",
#     "friend3":"Johny",
#     "friend4":"Gabriel",
#     "friend5":"Dario"
# }

# for friend in friends:
#     f = friends[friend]
#     print(f)

# file_types = {
#     ".txt":"text file",
#     ".pdf":"pdf document",
#     ".png":"image"
# }

# print(".pdf" in file_types)
# print(".mp4" not in file_types)

# friends={
#      "friend1":"Alexandre",
#      "friend2":"Jalil",
#      "friend3":"Johny",
#     "friend4":"Gabriel",
#     "friend5":"Dario"
# }

# last_names={
#     "friend1":" Da Silva",
#     "friend2":" Baker",
#     "friend3":" Nyugen",
#     "friend4":" Rodeiguez",
#     "friend5":" Roberts"
# }

# result = {key:friends[key]+last_names.get(key,'') for key in friends.keys()}
# print(result)

# nums =[1,2,3,53,567,47863,6295,542986,59929,22]
# result={index:value for index, value in enumerate(nums)}
# print(result)

dict1 = {'a':1,'b':3,'c':532,'d':283,'e':2332}
list_from_dict = [*dict1.items()]
print(type(dict1))
print(list_from_dict)
print(type(list_from_dict))