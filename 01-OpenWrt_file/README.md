# To Open a File
Is a common practice to open a file in python. to open a file we use the function open(). This function takes the name of a file as parameter and opens it. there are two ways to open a file.
1. open the file and assign a variable to it
2. Using the "with" keyword
## Open and assign
To do this we open the file and assign a variable to it.
Example:
```
File=open(name_of_file)
```
## Using 'with' keyword
To use the 'with' keyword we do it as follows:
```
with open(name_of_file) as file:
	file.read()
```
## Note
is a good practice to use the 'with' keyword.
when you use it, you dont have to close it. The with keyword will close the file once control leaves the 'with' indentation.
But in the other one, you must close it.
Example:
```
file=open(fileName)
file.read()
file.close()
```
when you close the file you cant read it again. Trying to do that will throw an error.
# To write
to write in the file we use.
file.write()

