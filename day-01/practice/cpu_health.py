import psutil

print("In Day 01 Task, We will take threshold value from user.")

def check_cpu_threshold():
    cpu_threshold = int(input("Please provide the CPU threshold value: "))
    current_cpu = psutil.cpu_percent(interval=1)
    if current_cpu > cpu_threshold:
        print(f"Current CPU usage is {current_cpu}, Alert Email Sent...")
    else:
        print("CPU in safe state.")

check_cpu_threshold()