import datetime

name = input("Enter your Name")
# Date = input("Enter your Name")
d = str(datetime.datetime.now())

letter = """ Dear <|Name|> , \n \t You are Selected ! \n <|Date|>"""
letter= letter.replace("<|Name|>", name)
letter = letter.replace("<|Date|>",d)

print(letter)

# str = "Omkar"
# str.replace()