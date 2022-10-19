#!python3
import json
x = {
    "a" : "math",
    "b" : "english"
}
y = json.dumps(x)
print("json.dumps")
print(y)
print(type(y))
print("")

print('json.loads')
z = json.loads(y)
print(z)
print(type(z))
