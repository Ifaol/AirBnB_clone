
# 0x00. AirBnB clone - The console

## Learning Objectives:

At the end of this project, you should be able to:

- Create a Python package
- Develop a command interpreter in Python using the cmd module
- Implement Unit testing in a large project
- Serialize and deserialize a Class
- Read and write JSON files
- Manage datetime
- Utilize UUID
- Understand and use *args and **kwargs
- Handle named arguments in a function

## Description of the project:

Welcome to the AirBnB clone project! This project aims to create a command-line interface to manage AirBnB objects, as well as implement various supporting functionalities.

### Implimented functionalities:

#### Parent Class (BaseModel):

We will put in place a parent class, BaseModel, to handle the initialization, serialization, and deserialization of future instances.

#### Serialization/Deserialization Flow:

A simple flow of serialization/deserialization will be established, allowing seamless conversion between instances, dictionaries, JSON strings, and files.

#### AirBnB Classes:

All classes related to AirBnB functionality, such as User, State, City, Place, etc., will be created, inheriting from the BaseModel.

#### Abstracted Storage Engine:

The project will include the development of the first abstracted storage engine, specifically focusing on file storage.

#### Unit Tests:

Comprehensive unit tests will be implemented to validate all classes and the storage engine, ensuring robustness and reliability.

### Command Interpreter

The command interpreter allows you to manage AirBnB objects by performing various operations:

#### Targeted operations:

##### Create a New Object:

You can create new objects such as User, Place, etc., using the appropriate commands.

##### Retrieve an Object:

Objects can be retrieved from a file, database, etc., to access their information or perform operations.

##### Operations on Objects:

Various operations can be performed on objects, including counting, computing statistics, and more.

##### Update Attributes:

You can update the attributes of an existing object as needed.

##### Destroy an Object:

Objects can be deleted or destroyed when they are no longer needed or relevant.

#### How to Start It:

To start the command interpreter, in an interactive mode, execute the "console.py" script. 

```bash
$ ./console.py
```

#### How to Use It:

In an interactive mode, once started, you can interact with the interpreter by entering commands. But both interactive and non-interactive mode works. Use the help command to see the list of available commands and their usage.

Interactive mode:-
```bash
$ ./console.py
(hbnb) help
```
Non-interactive mode:-
```bash
$ echo "help" | ./console.py
```

#### Examples:

##### Interactive mode:

###### For help:

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) quit
$
```

```bash
$ ./console.py
(hbnb) help create 
usage: create <class>
        Create a new class instance and print its id.
(hbnb) help EOF
EOF signal to exit the program.
(hbnb) help show
usage: show <class> <id> or <class>.show(<1d>)
        Display the string representation of a class instance of a given id.
(hbnb) quit
$
```

###### For count:

```bash
$ ./console.py
(hbnb) help count
usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class.
(hbnb) count BaseModel
0
(hbnb) BaseModel.count()
0
(hbnb) quit
$
```

###### For create:

```bash
$ ./console.py
(hbnb) count BaseModel
0
(hbnb) create BaseModel
b2350d4f-7238-4745-9671-2bd9b6acadfb
(hbnb) count BaseModel
1
(hbnb) quit
$
```

###### For destroy:

```bash
$ ./console.py
(hbnb) help destroy
usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id.
(hbnb) count BaseModel
1
(hbnb) destroy BaseModel b2350d4f-723 8-4745-9671-2bd9b6acadfb
(hbnb) count BaseModel
0
(hbnb) quit
$
```

##### Non-interactive mode:

###### For help:

With "echo" and help command:-

```bash
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  sho\w  update

(hbnb)
$
```
With "cat" and a file containing help command:-
```bash
$ cat test_help | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  sho\w  update

(hbnb)
$
```

###### For count, create and show:

With "echo" and the commands:-

```bash
$ echo "count BaseModel" | ./console.py
(hbnb) 0
(hbnb)
$ echo "create BaseModel" | ./console.py
(hbnb) 42ebf5d5-1b93-470d-9c74-83cbf5 cfbc98
(hbnb)
$ echo "count BaseModel" | ./console.py
(hbnb) 1
(hbnb)
$ echo "show BaseModel 42ebf5d5-1b93-470d-9c74-83cbf5cfbc98" | ./console.py
(hbnb) [BaseModel] (42ebf5d5-1b93-470 d-9c74-83cbf5cfbc98) {'id': '42ebf5d5-1b93-470d-9c74-83cbf5cfbc98', 'created_at': datetime.datetime(2024, 2, 12 , 6, 24, 54, 319126), 'updated_at': datetime.datetime(2024, 2, 12, 6, 24, 54, 319134)}
(hbnb)
$
```
