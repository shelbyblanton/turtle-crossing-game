# Turtle Crossing Game (a la Frogger)

## **[100 Days of Code: The Complete Python Pro Bootcamp for 2023](https://www.udemy.com/course/100-days-of-code/)**

By Dr. Angela Yu

*Day 23 of 100:* The Turtle Crossing Capstone Project

## Project Specs

Using **[Turtle](https://docs.python.org/3/library/turtle.html)** Screen capabilities, program a Turtle Crossing game in the style of Frogger where a user guides a turtle across traffic to reach the other side. 

The game ends if the turtle collides with a car.

This application is written with Python 3.11.

![alt text](https://github-readme.s3.us-west-1.amazonaws.com/TurtleGame.png)

### Main Features
This game application features a turtle that needs to cross a road to get to the other side. It has to dodge traffic to do so.

Cars are made up of multi-color rectangles randomly added to the screen and constantly moving from right to left.

The current score is tracked at the top of the screen.  

## Usage & Requirements

This project uses three classes:
- Player
- Car Manager
- Scoreboard

### Workflow
The user guides the turtle through traffic by pressing the `up` and `down` arrow keys.

When the turtle makes it across, the use scores a point and two things happen: 
1. The turtle returns to the bottom of the screen to make its next attempt to cross
2. Traffic speeds up

If the turtle collides with any of the cars on the road, the game is stopped and the words "Game Over" display in the center of the screen.

![alt text](https://github-readme.s3.us-west-1.amazonaws.com/TurtleGame-gameover.png)

# Getting Started

All of the commands below should be typed into the Python terminal of your IDE (I use PyCharm for my Python Development).

First, clone the repository from Github and switch to the new directory:

    $ git clone git@github.com:shelbyblanton/turtle-crossing-game.git
    
Then open the project in PyCharm.

**Setup is complete!** 

Click Run in PyCharm to see the app in action.

# Game Adjustments

To increase or decrease the speed that traffic travels as the turtle successfully crosses the road, edit the `MOVE_INCREMENT = 10` constant variable in the `CarManager` class. 


# Author & Credits

Programmed by **[M. Shelby Blanton](https://www.linkedin.com/in/shelbyblanton/)** under the instructional guidance of **[Dr. Angela Yu](https://www.udemy.com/user/4b4368a3-b5c8-4529-aa65-2056ec31f37e/)** via **[Udemy.com](udemy.com)**.
