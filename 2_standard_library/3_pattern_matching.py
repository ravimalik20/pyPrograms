import re

# Using regex for pattern matching
input_string = "which foot or hand fell fastest"
res = re.findall(r'\bf[a-z]*', input_string)
print(res)

# Simple replacement using string methods

str1 = "tea for too"
print (str1.replace("too", "two"))
