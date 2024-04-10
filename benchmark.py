import subprocess
import psutil

# Launch the app.py as a separate process
process = subprocess.Popen(["python", "app.py"])

# Get the process ID of the launched script
pid = process.pid

# Create a Process object using the process ID
process = psutil.Process(pid)

# Get CPU usage
cpu_percent = process.cpu_percent()
print(f"CPU Usage: {cpu_percent}%")

# Get memory usage
memory_info = process.memory_info()
memory_usage = memory_info.rss / 1024 / 1024  # Convert from bytes to megabytes
print(f"Memory Usage: {memory_usage} MB")