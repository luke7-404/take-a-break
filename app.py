INTERVAL_TIME = 60  # Variable that dictates the baseline notification interval
REST_TIME = 15 # Variable that represents the time in between intervals 

# Libaries
import plyer.platforms.win.notification
from plyer import notification
import datetime
import time




prev_time = datetime.datetime.now()  # Get the current time

# Format the time as mm/dd/yyyy hr:min:sec
formatted_prev_time = prev_time.strftime("%m/%d/%Y %H:%M:%S")

# The next alert time (interval time with NO offset)
next_alert_time = prev_time + datetime.timedelta(minutes=INTERVAL_TIME)

# Send a notification with the formatted start time
notification.notify(
    title=f"Program Started at {formatted_prev_time}.",
    message=f"{INTERVAL_TIME} minutes has been set, counting down now",
    timeout=10
)

# Enter an infinite loop
while True:
    # Get and update the current time
    tnow = datetime.datetime.now()

    # if the current time has passed the alert time
    if tnow >= next_alert_time:
        
        # Post notifications 
        #print(f"{INTERVAL_TIME} minutes have passed.")
        notification.notify("Take A break", f"{INTERVAL_TIME} minutes have passed", timeout=30)
        
        # Update times
        prev_time = tnow
        formatted_prev_time = prev_time.strftime("%m/%d/%Y %H:%M:%S")
            
        # Set the next alert time WITH offset time
        next_alert_time = prev_time + datetime.timedelta(minutes=(INTERVAL_TIME + REST_TIME))

        # Delay the program for 15 minutes (900 seconds)
        time.sleep(REST_TIME * 60)
        
        # After delay, alert the start of the next cycle
        #print("New Cycle Started")
        notification.notify("New Cycle Started", f"Another {INTERVAL_TIME} minutes has been set", timeout=10)

    time.sleep(60)  # Check every minute


