# Take A Break Python Script
This project is for window users to have a pomodoro-like notification system. This script currently is <ins>**only**</ins> developed for windows users. The libaries used in ``app.py`` are ``plyer``, ``datetime``, and ``time``. 

### How to edit the script:
To change the interval time (the amount of working time) access the ``intervalTime`` variable (the units are in minutes).

To change the break time delay (the time in between cycles) access the line with the second mention of ``next_alert_time`` and change the number that is added to ``intervalTime``. On the line below it, update the sleep time (in seconds) to correspond to the same offset.

## Benchmarking ``app.py``:
There is a file in this repo, called ``benchmark.py`` that allows for the ``app.py`` script to be benchmarked. On my machine, the results I get are:

``CPU Usage: 0.0%`` <br>``Memory Usage: 1.6640625 MB``</br>

I encourage that before having the ``app.py`` script run on your machine, the script should be benchmarked!

## Make the script a task
Once configuring ``app.py`` and benchmarking it, add the ``app.py`` script or the executable to your windows machine.



###### <br><br><br><br><br><br><br><br>This program uses the MIT License, please look at the license page for more information</br></br></br></br></br></br></br></br>