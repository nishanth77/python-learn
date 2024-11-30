
import copy
dic = {'a':11,'b':2,'c':3,'d':4}
print("--")
print(sum(dic.values()))
su = (dic[values] for values in dic)
print(su)
a=[1,2,3,[4,5]]
b=a.copy()
[3][0]=44
print(a)
print(b)
d = [1,2,3,4]
print(sum(d))
print(dic.keys())
# a = int(input())
# print(a)
# import pandas as pd
# txt = "sampletext"

# x = txt.join("","qwerty")

# print(x)

original_list = [1, [2, 3]]
# deep_copied_list = copy.copy(original_list)
deep_copied_list = original_list.copy()
original_list[0] = 22
print(original_list)
print(deep_copied_list)

list = [30, 45, 20, 15, 60]

print(list[-1::-1])

n = 5
print(abs(n))

import requests, json

methods = {"Content-Type":"application/json"}
url = "https://www.google.com/search"
response = requests.get(headers=methods, url=url,params="what")
print(response.status_code)
p = response.text
print(p)

