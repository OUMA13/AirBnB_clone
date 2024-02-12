# AirBnB Clone - The Console
![Project Logo](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240210%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240210T000431Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ff4595f0326ac16d4b94ff6a7833dad8f7b6e498b41e639b94ccb61bfbd13920)


## Introduction
This project is part of my journey to becoming a software engineer. The goal is to build a clone of the AirBnB, implementing features step by step. The project consists of a command interpreter to manipulate data without a visual interface, a website with static and dynamic functionalities, a database or files that store data, and an API for communication between the front and backend.

## Console
The console, or command interpreter, is the tool for creating, updating, destroying, storing, and persisting objects to a JSON file. It serves as a validation tool for the storage engine.

###Console  Commande 
The HolbertonBnB console supports the following commands:
- create: Creates a new instance of BaseModel.
- show: Prints the string representation of an instance based on the class name and ID.
- destroy: Deletes an instance based on the class name and ID.
- all: Prints string representations of all instances based on the class name.
- update: Updates an instance based on the class name and ID.

## BaseModel class
The BaseModel class serves as the parent class for other classes and defines common attributes and methods. It includes methods for initialization, saving, converting to a dictionary, and providing a string representation of instances.

## File Storage
The FileStorage class manages the storage of HBNB models in a JSON file. It includes methods for storing, retrieving, and serializing/deserializing objects to/from the JSON file.

## Testing 
Unit tests are implemented to ensure the correctness and reliability of the code. These tests cover various aspects of functionality and help maintain code quality.

To run the unit tests, execute the following command:
sh
python3 -m unittest test_file.py


## Problems Faced
One of the challenges encountered was with importing modules, especially the models module. Setting the PYTHONPATH environment variable was necessary to resolve this issue.


## Authors

*Wissal Leknouch
* El-khanchoufi
