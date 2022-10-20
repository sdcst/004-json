## SDSS Computing Studies Python Assignment
### Assignment #xx <Title> (Total Marks xx)

Objectives:
* Make use of the requests module to retrieve data from the Internet
* To use the json module to code/decode a complex data structure into a string
* Deconstruct a complex dictionary json object to retrieve important information

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

Working with JSON is especially important when you want to retrieve information from the Internet, such as when using the REQUESTS module.
There are two kinds of requests we can make for data:

_get requests_
these are when information is added to the URL. 
eg: https://www.google.com/search?q=google+get+request&oq=google+get+request&aqs=chrome..69i57.4464j0j1&sourceid=chrome&ie=UTF-8
Notice all the additional information included after the ? symbol?
That is part of the actual request.  It is great for making sense of what data is being requested, but very bad if you are including password or authentication information

_post requests_
send data to a site with hidden information that is not seen or included in the URL.  This is typical of login data when you are connecting to a website.

### Assignment:
Use the Weather API builder at https://open-meteo.com/en/docs to generate an API call for a city.
We are going to make use of the REQUESTS.Request method to retrieve this data and unpack it with json.loads into a variable that we can use.

