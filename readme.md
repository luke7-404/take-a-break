# Take A Break Python Script
This project is intended for window users to have a pomodoro-like notification system. The libaries used in ``app.py`` are ``plyer``, ``datetime``, and ``time``. 

## How to edit the script:
To change the interval time (the amount of working time) alter the ``INTERVAL_TIME`` variable (the units are in minutes).

To change the time between the time intervals alter the ``REST_TIME`` variables with the number of minutes between the intervals.

## Benchmarking ``app.py``:
There is a file in this repo, called ``benchmark.py`` that allows for the ``app.py`` script to be benchmarked. I encourage that before having the ``app.py`` script run on your machine, the script should be benchmarked!

## Build and use script (Windows instructions)
Once configuring ``app.py`` and benchmarking it, to make the script into a windows executable use ``pyinstaller``.
<ol>
    <li>Install <code>pyinstaller</code>: 
        <ol>
            <code>pip install pyinstaller</code>
        </ol>
    </li>
    <li>Create a <code>.exe</code>:
        <ol>
            <code>pyinstaller --name "Take-A-Break" -- onefile --noconsole app.py
            </code>
            <br>
            This generates an executable file in the dist/ folder.</br>
        </ol>
    </li>
</ol>

### How to make the script run on start up
<ol>
    <li>Create a shortcut for the <code>Take-A-Break.exe</code>
    </li>
    <li>Add shortcut to startup folder:
        <ol>
            <li>Run the command <code>win + r</code></li>
            <li>In the window type <code>shell:startup</code></li>
            <li>Add the <code>Take-A-Break.exe</code> shortcut to the folder that opened</li>
        </ol>
    </li>
</ol>

###### <br><br>This program uses the MIT License, please look at the license page for more information</br></br>