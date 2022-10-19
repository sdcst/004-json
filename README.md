## SDSS Computing Studies Python Assignment
### Assignment #xx <Title> (Total Marks xx)

Objectives:
* To use the json module to code/decode a complex data structure into a string

Python has more complex variables:
* list
* tuple
* dictionary
* set
* lists of lists, tuples or dictionaries
* objects

Converting them to a standard format for transport so that they can be unpacked at the "other end" is a useful practice, and this is where json comes in. JSON stands for "JavaScript Object Notation" and is a standard way to convert a variable into a single string that can be later decoded:
x = 3
json value: '3'

x = "3"
json value: '"3"'

x = [3,5,"hello"]
json value: '[3, 5, "hello"]'

x = {
    "a" : "math",
    "b" : "english"
}
json value: '{"a": "math", "b": "english"}'

Note that each of these is converted into a single string

Encoding:
json.dumps( variable ) to convert a variable into a json encoded string

Decoding:
json.loads( variable ) to convert the json encoded string back into a regular variable


### XX Tasks

##### Task 1
(x points) 

