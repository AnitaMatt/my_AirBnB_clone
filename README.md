# This project is to practice using a console to interact with a storage engine and manipulate data as needed

## This console would be able to create a new user or a new place or any other data object
* Create
* Do operations on objects
* Update attributes of an object
* Destroy an object

**********
Basically CRUD functions

### In interactive Mode
```
$  ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

### Also in non-interactive mode
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
