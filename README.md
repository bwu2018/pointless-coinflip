# Pointless-Coinflip

Simulates coin flips and counting repeated head or tail flips. At the end the program will log max heads/tails streak.

## Usage

The simulator can be run from the command line using python:
`$ python sim.py`

This program supports command line arguments as well, `-q` will prevent the program from outputting to the terminal until the program is terminated
```
usage: sim.py [-h] [--quiet]

Simulates coin flips

optional arguments:
  -h, --help   show this help message and exit
  --quiet, -q  Run in quiet mode. Do not print out new max streaks
  ```
  
  To quit the simulation, enter `ctrl+c`.
  
  Run Example: 
  ```
  User@DESKTOP-K03KE3P MINGW64 ~/Documents/GitHub/pointless-coinflip (main)
$ python sim.py
New max streak 1 heads
New max streak 2 tails
New max streak 3 heads
New max streak 4 tails
New max streak 5 heads
New max streak 7 tails
New max streak 8 heads
New max streak 10 heads
New max streak 12 tails
New max streak 13 heads
New max streak 14 heads
New max streak 18 heads
New max streak 19 tails
KeyboardInterrupt
19 tails 
```
