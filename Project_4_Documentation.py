"""
-----------------------------------------------------------------------------------
CIT-287
Project 4 Final Examination
Student: Aliaksei Petrusevich
Date Submitted: May 5, 2018
-----------------------------------------------------------------------------------
Description:
-----------------------------------------------------------------------------------
    The project is a simulation of a popular card game - blackjack. The purpose
of the game is to get a score of 21 by taking a specific number of cards from
the deck. If the player outplays the dealer, he wins. In this case, there is
no dealer, and he player continues taking cards until he reaches 21, in which
case he wins. If the player goes over 21, the loses. The game continues while user
has sufficient funds and wishes to continue playing when prompted by a dialog box.
    The goal of this project is to summarize the knowledge of Python programming
language as well as use the graphical library of Python - tkinter - for creating
a suitable graphical user interface.
-----------------------------------------------------------------------------------
Design:
-----------------------------------------------------------------------------------
    Based on the requirements of the project, the game must use a deck of
52 cards - 4 suits of 13 cards each. An ace may be used as a 1 and 11
favoring the user based on his score.
    With these requirements, I have decided to create a list of cards
made out of dictionary entries containing suit, name, and value of each card.
The list will be reshuffled every time the user plays the game, and the used
cards will be disregarded as the list will be populated with entries again.
    Control elements such as labels, buttons, and frames posed no challenge
as tkinter library has very easy and convenient way of managing these elements.
However, due to abscence of knowledge of static variables or pointers,
some variables were made global and were used in this way thoughout the program.
    Calculations part had no issues of any kind.
-----------------------------------------------------------------------------------
Testing:
-----------------------------------------------------------------------------------
    After multiple testing runs, the program appears to be running as designed:
     - The balance is decreased/increased according to the result of the game
     - In-game logic guides user through the dialogs as expected
    Overall, no bugs or problems were noticed, concluding that the program
operates as required by the project's specifications.
-----------------------------------------------------------------------------------
"""
