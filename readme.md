# Take A Break Python Script
This project is for window users to have a pomodoro-like notification system. This script currently is <ins>**only**</ins> developed for windows users. The libaries used in ``app.py`` are ``win10toast``, ``datetime``, and ``time``. 

### How to edit the script:
To change the interval time (the amount of working time) access the ``intervalTime`` variable; the units are in minutes.

To change the break time delay (the time in between cycles) access the line with the second mention of ``next_alert_time`` and change the number that is added to ``intervalTime``. On the line below it, update the sleep time (in seconds) to correspond to the same offset.

## Benchmarking the ``app.py`` script:
There is a file in this repo that allows for the ``app.py`` script to be benchmarked. On my machine, the results I get are:

``CPU Usage: 0.0%``
``Memory Usage: 1.65234375 MB``

I encourage that before having the ``app.py`` script run on you machine, it is benchmarked before

## Make the script a task
<<<<<<< HEAD
Once configuring ``app.py`` and benchmarking it, add the ``app.py`` script to your windows machine's registry. (There are alternative methods for having it run if adding to the windows registry does not work)


=======
Once configuring the python script, add the script to your windows machine's registry (for personal logins) or other methods of having the python program run in the background.
>>>>>>> 48f5b0522585459f9f2ff1a4dd65fde640d08fb2

###### <br><br><br><br><br><br><br><br>This program uses the MIT License, please look at the license page for more information</br></br></br></br></br></br></br></br>
