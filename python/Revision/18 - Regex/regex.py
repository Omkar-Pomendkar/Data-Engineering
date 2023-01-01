import re
# Here r represents Raw String
print('\tTab')
print(r'\tTab')

# pattern = re.compile(r'abc')
# pattern = re.compile(r'omkarpomendkar\.com')
pattern = re.compile(r'\b')

text_to_search = """abcdfkfkgdfkgmdgdfgognOOFONFNFJabc ofgofsfabc

omkarpomendkar.com
"""

print(text_to_search[47:65])
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)

# print(text_to_search[0:3])
# print(text_to_search[31:34])
# print(text_to_search[42:45])

matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

nameage = "Omkar is 22 and Surbhi 33 Sanjay is 44 and Shraddha is 40"
ages = re.findall(r'\d{1,3}',nameage)
print(ages)

names = re.findall(r'[A-Z][a-z]*',nameage)
print(names)

agedict= {}
x = 0
for eachname in names:
    agedict[eachname] = ages[x]
    x+=1
print(agedict)