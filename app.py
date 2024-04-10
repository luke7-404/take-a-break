# Libaries
from win10toast import ToastNotifier
import datetime
import time

notif = ToastNotifier() # Create toaster notifier object
intervalTime = 60 # Variable that dictates the baseline notification interval
prev_time = datetime.datetime.now() # Get the current time

# The next alert time (iterval time with NO offset)
next_alert_time = prev_time + datetime.timedelta(minutes=intervalTime) 

# Print the time that the program started before the loop
print(f"Start time: {prev_time}")

# Enter an infinite loop
while True:
    # Get and update the current time
    tnow = datetime.datetime.now()

    # if the current time has passed the alert time
    if tnow >= next_alert_time:
        
        # Post notifications 
        print(f"{intervalTime} minutes have passed.")
        notif.show_toast("Take A break", f"{intervalTime} minutes have passed", icon_path=None, duration=30, threaded=True)
        
        # Update times
        prev_time = tnow
            
        # Set the next alert time WITH offset time
        next_alert_time = prev_time + datetime.timedelta(minutes=(intervalTime+15))  

        # Delay the program for 15 minutes (900 seconds)
        time.sleep(900)
        
        # After delay, alert the start of the next cycle
        print("New Cycle Started")
        notif.show_toast("New Cycle Started", f"Another {intervalTime} minutes has been set", icon_path=None, duration=10, threaded=True)

    time.sleep(60)  # Check every minute
