# Proposal

## What will (likely) be the title of your project?

String of Bombs

## In just a sentence or two, summarize your project. (E.g., "A website that lets you buy and sell stocks.")

We are going to make a bomb diffuser game using python. Diffusing the bomb will involve a speed typing challenge using a random section of a text and a timer will count down
until you finished typing the text.

## In a paragraph or more, detail your project. What will your software do? What features will it have? How will it be executed?

To start we will make an interactive board using pygame where you will be given a string of text and a timer and you have to correctly type the string before time runs out or else the bomb
goes off and you lose the game. In order to get a random string of text we will read a file of a book online from a database and pull randomize the selection of strings from sentence
to sentence. With each round you succesfully type the string before time runs out you will be given a new string and less time. After a certain amount of rounds won you will win the game.

## If planning to combine 1051's final project with another course's final project, with which other course? And which aspect(s) of your proposed project would relate to 1051, and which aspect(s) would relate to the other course?

TODO, if applicable

## If planning to collaborate with 1 or 2 classmates for the final project, list their names, email addresses, and the names of their assigned TAs below.

Cole Heilman, tuk05640@temple.edu, Jeremy Fan
Kale Wiley, tui97036@temple.edu, Joanne Nichols

## In the world of software, most everything takes longer to implement than you expect. And so it's not uncommon to accomplish less in a fixed amount of time than you hope.

### In a sentence (or list of features), define a GOOD outcome for your final project. I.e., what WILL you accomplish no matter what?

We will accomplish at least one successful round of the bomb diffuser. This means that the player will be givem a string and be asked to type the string exactly correct and if that is completed once
then that will be one round of the game.

### In a sentence (or list of features), define a BETTER outcome for your final project. I.e., what do you THINK you can accomplish before the final project's deadline?

We are hoping to make multiple rounds and include a time limit because that will make the game more engaging and high stakes. If the strings get longer and the time gets progressively shorter the game will feel
much more complete and create more of a do or die scenario. 

### In a sentence (or list of features), define a BEST outcome for your final project. I.e., what do you HOPE to accomplish before the final project's deadline?

The best outcome of this project would include the game having multiple bombs to diffuse. This means that you will have a timer that counts down and doesn't reset. In order to diffuse all
the bombs you need to correctly type in multiple strings consecutively for each bomb. This will make the game even more high stakes and engaging to play.

## In a paragraph or more, outline your next steps. What new skills will you need to acquire? What topics will you need to research? If working with one of two classmates, who will do what?

In order to make our game successful we will need to learn how to create a board using pygame and make interactive features on that board so that you can play the game within the board instead
of idle. Making an interactive board will require us to make a text box and allow the user to put inputs into the text boxes. With pygame we hope to learn how to make little animations for 
the bombs if they go off or they are successfully diffused by the player. With these features that pygame allows us to do we hope that the game will be more immersive and fun to play. We will
also need to research how to use the built in time and date library. This library will allow us to make a time limit to diffuse the bomb or bombs. Having a time limit will really elevate our game
and make it much more fun to play. We were planning on splitting the project up by having one of us handle the background functionality of the game where the program reads in a file and takes
a random string from the file that prompts for the user input. Then the program will confirm if that input does match the given string character for character. The other person will be tasked with
creating the board using pygame and making a functional timer.