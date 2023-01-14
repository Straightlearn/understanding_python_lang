# Json Data in Python

Before we dive into the json Data in python, i think is important to understand what json really means.

### Json
json is an acronym for JavaScript Object Notation.
json is a data storing format. it is used to transfer data,gathering information through API and storing data in a document database.
So in short we can say that json is a formal way of storing and exchanging data.
Example of json data format
```
employees=[{"firstName":"john","age": 37,"position":"assistant"}
	  {"firstName":"mark","age":30,"position":"cleaner"}]
```
check the web for more examples.

## working with Json data format
To work with json we dont have to install it, because its already included in the native python. so what we need do is to import it.
exampe:
```
import json
```
### Terms used
1. sterialization: This is the process of encoding json. it is the transformation of data into a series of bytes,to be stored or transmitted accross a network. it is just the convertion of a data to a form in which it can be stored or tansfered. we can see encoding as writing to a disk.
2. Desterialization: this is the process of decoding data, which have been stored or transfered in json standard. Basically we can see decoding as readin data into a memory.

## Sterialization

We use dump() to write Python data to a file-like object.
that is its use to write to an external JSON file.
There is also dumps() which is used to write to a python string.

Simple objects are translated to json, see below

| PYTHON   |  JSON    |
| ---------| :--------|
| dict     |  object  |
| list     |  array   |
| tuple    |  array   |
| str      |  string  |
| int,long |  number  |
| float    |  number  |
| True     |  true    |
| False    |  false   |
| None     |  null    |

Example: 
```
data= {
      "president":{
	      "name":"Goodluck jonathan",
	      "age":67,
	}
      }
```
 the above is an example of a data in json format. it is similar to python python list and dictionary data structures.
 if you dont know dictionary in python, you can check it up.

 to work with the json example above, you can write it 
 1. To a file
 2. or to a python object.
### Writing To a file
To write our previous example to a file.
Then firstly you have to create a file using your text editor i.e vi, emacs etc. 
The file name will have a .json file extension. 
i.e mainyFile.json.
Then to write it:
```
with open("mainFile.json","w") as myfile:
	json.dump(data,myfile)
```
in the example above the 'with' line is used to open the file in write mode i.e and then json.dump(data,file).
is used to dump or let say write the content of the python
string object named "data" into the object like file named
"myfile".
so the dump() method takes two positional arguements.
The first one is the data object to be sterialized(content to write into the json file) 
and the second is the file-like object to write into. 

## Deserializing json
in deserialization we use the method load() and loads() 
for turning json encoded data into python objects.
examlple:
```
Login={"pass":"askey232ash"}
encodedLogin=json.dumps(Login)
decodedLogin=json.loads(encodedLogin)
```
but if you want to work with already existing json file,
thats an encoded json file. you do it as below
```
with open("file.json","r") as read_file:
	data=json.load(read_file)
```
looking at the above example, we would observe that we used
load() and not loads().It is so because we are loading from
a file and not from a string object. 
