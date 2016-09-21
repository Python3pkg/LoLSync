# League of Legends Friend Sync

## Keep in LoL-Sync with your friends!

*@author Jason Lin, jason0@stanford.edu*

## Requirements

This script uses python 3.4 and below, must be run on Mac OS X, and you must have
a valid League of Legends username in the North American region to search for. 
(If you don't know any, try searching the for players on the leaderboards at 
http://www.lolking.net/leaderboards#/na/1, as these are the players that will likely
be online.)

## Running the program

The program is a simple command line function that is started through entering
'python3 lol-sync.py' in the command line. Ensure that necessary libraries have 
been imported through the requirements.txt file. Enter in the username of a friend
that you have on League of Legends, and then the script will tell you whether or
not they are free to play a game!

## Code Design

I start the process off with a main method that continuously prompts the user for 
a valid League of Legends username to keep track of. The method used to check whether
a user's League of Legends username is valid is called and makes a GET request to the
Riot Games API. The API either returns 404 if not found or the user id of the user if
the user is valid. Once a GET request is made that finds a valid user, it returns the 
user id of the user to the main method, which then calls the check_in_game method. 
This method makes a GET request to find a user's current game status. If the response 
is not found, then the client can successfully start a game with the entered user! 
However, if the user is in a game, then check_in_game will turn the returned request 
information into a json dictionary. It then prints out the time the game started, the 
champion that the user is playing, and shows the game length, which is continuously 
updated each second to represent an actual timer. There is then a while loop which 
continuously makes a GET request to find the user's current game until a 404 is returned, 
whereas then a subprocess is called to execute an OS X desktop notification to the user.

## Modules

I have imported several modules to help with this script. First of all, I imported
the requests module to help simplify making HTTP GET requests to the League of Legends
API. Next, I imported the Time module to help with waiting seconds to print out the
time as well as waiting to make the next GET request to avoid going over the request
limit for the API. I also used the Terminal class from the Blessings module along with
os in order to clear the game time displayed every second in order to simulate an actual 
clock. Finally, subprocess was used to call the terminal-notifier executable in order
to show the client a desktop notification that their friend has finished a game.

## Bugs

There is a bug when requesting the user's game length and game start time as soon as they
begin a game, as both times are off in the returned api request. I have made a post on
the Riot developer forums to get more info on what these are returning and how I can fix
them. There are also some features that I plan to add in later over the summer, such as 
being able to search for multiple friends, cancel a search without using ctrl-c, and 
making this app into a chrome extension!

## Credits/Acknowledgements

This wouldn't have been possible without the help of the Sam and the rest of the TAs for
answering any questions I had on the project. Also, thanks to Riot for making their API
freely available to use for developers, which made getting information about users
many times easier. Finally, thanks to my friends who started games of League of Legends
without me for the inspiration to make this project!
