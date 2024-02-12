
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
EOF  help  quit

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
EOF  help  quit
(hbnb) 
$
```
With "cat" and a file containing help command:-
```bash
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```