d = {
    "fast":"In a quick Manner",
    "Omkar":"A Coder",
    "Marks" : [1,2,3,4],
    "Another Dict" : { 1: "One"}
}
# print(d.keys())
# print(d.values())
print(d.items())   # Returns Tuple for all contains (key,value)
# print(d.pop("fast"))
# print(d)
# print(d.popitem())
# print(d.popitem())
# print(d.popitem())
print(d.get("fast"))
print(d)
# Update 
ud = {
    "name" : "omkar"
}
d.update(ud) # Update the Dictionary for Adding Dictionary
print(d)

# differencr between .get and [] bracket Syntax
print(d["name1"])  # Here you know name is present in Dicitionary
print(d.get("name1"))   # Returns None as name1 is not present in Dictionary


