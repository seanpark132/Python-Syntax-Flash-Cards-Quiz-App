# Python Syntax Flash Cards/Quiz App

A flash cards/quiz app built on Python using the **tkinter** Graphical User Interface (GUI) module. 
The purpose of this app is to provide users with an interface where they can test their knowledge of a subject, such as
Python syntax. 

By default, the program reads the python_functions.csv file which has the syntax of inputs, outputs, and definitions of common 
built-in Python functions. Other .csv files with the same format (three columns: **Input**, **Output**, **Definition**) can
also be used to test knowledge on other subjects. 

Each entry from the .csv is made into a flash card with two sides.\
The first side (Input Side) shows: 
* The lines of code that are the input 
* An entry box that allows the user to enter what they think the output of that code is. 
* A "FLIP" button
* A timer
* The user's score (questions correct/total questions)

The second side (Output Side) shows:
* The correct output
* The user's answer
* *CORRECT* if the user is correct, *INCORRECT* if the user is incorrect
* The definition of the function used

On the input side of the card, the user has 30 seconds to enter what they think the correct output to the function will be. They can also click the "FLIP" button
to instantly flip the card. 
