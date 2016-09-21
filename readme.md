# League of Legends Friend Sync

## Keep in LoL-Sync with your friends!

*@author Jason Lin, jason0@stanford.edu*

## Installation

This script only works on MacOS!

Download [Python 3.4](https://www.python.org/downloads/release/python-343/) if needed.

Make sure /Library/Frameworks/Python.framework/Versions/3.4/bin (The path to execute
Python 3.4 files) is in your [Shell Path](https://coolestguidesontheplanet.com/add-shell-path-osx/).

#### Pip3

Install or upgrade [Pip3](https://pip.pypa.io/en/stable/installing/) if necessary.
(Follow the above instructions, but type python3 get-pip.py instead of python for pip3)

Install the script

~~~
pip3 install lolsync
~~~

#### Manual

Download the tarball [here](https://pypi.python.org/pypi/lolsync), then download [requests](http://docs.python-requests.org/en/master/user/install/#install) and [blessings](https://pypi.python.org/pypi/blessings).

## Usage

Run the script

~~~
lolsync
~~~

Enter in the username of a friend that you have on League of Legends, and then the script 
will tell you whether or not they are free to play a game!

## Design

I start the process off with a main method that continuously prompts the user for 
a valid League of Legends username to keep track of. The method used to check whether
a user's League of Legends username is valid is called and makes a GET request a personal 
server, which uses an Apache reverse proxy that then sends the request to Riot's API. The 
API either returns 404 if not found or the user id of the user if the user is valid. 

Once a GET request is made that finds a valid user, it returns the 
user id of the user to the main method, which then calls the check_in_game method. 
This method makes a GET request to find a user's current game status. If the response 
is not found, then the client can successfully start a game with the entered user! 
However, if the user is in a game, then check_in_game will turn the returned request 
information into a json dictionary. 

It then prints out the time the game started, the champion that the user is playing, 
and shows the game length, which is continuously updated each second to represent an actual 
timer. There is then a while loop which continuously makes a GET request to find the user's 
current game until a 404 is returned, whereas then a subprocess is called to execute an OS X 
desktop notification to the user.

## Troubleshooting

Riot's API acts strangely when requesting game time soon after a user starts a game. Be
aware that this may return weird times when doing so. Also, sometimes requests to the API
can bug out, causing bad information to be returned. Simply restart the script when this
happens.
