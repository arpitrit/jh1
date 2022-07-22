# class webseries:
#     show_name = 'Suites'
#     show_length = '234'


# web_series_obj = webseries()
# print(web_series_obj.show_name)
# print(web_series_obj.show_length)


from sys import set_asyncgen_hooks
from unicodedata import name


class Webseries:
    def __init__(self,name,season,episode):
       self.name = name
       self.season = season
       self.episode = episode
       print('I am hit')

web_1 = Webseries("Game of Thrones -",1,1)
web_2 = Webseries("Hatim",1,2)
print(web_1.name,web_2.name)