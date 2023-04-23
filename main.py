# Dictionary
# ==========
# https://www.pythonsheets.com/notes/python-dict.html

# Get all keys
a = {"1":1, "2":2, "3":3}
b = {"2":2, "3":3, "4":4}
print(a.keys())

# Get Key and Value
a = {"1":1, "2":2, "3":3}
print(a.items())

a = {"1":1, "2":2, "3":3}
b = {"2":2, "3":3, "4":4}
print([_ for _ in a.keys() if _ in b.keys()])

