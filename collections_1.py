from collections import Counter
from collections.abc import Mapping
str1 = 'The quick Fox was too fast for the big, slow and lazy Elephant'
count = {}
countstr =1
dic = {"t":20}
if "t" in dic:
    print("ppffodk")
test = Counter(str1)
print(test)
  
for j in str1:

    if j.isalpha():
        
        if j not in count:

            count[j] = 1
        else:
            count[j] += 1
    # countstr = 1

print(count)
print(list(count))
# c=Counter
c=Counter(a=4,b=2,c=5)
print(c.elements())

