from ml_detection import detect_traffic
from scheduler import select_node

traffic = detect_traffic()

print("Traffic Type:", traffic)

if traffic == "attack":
    print("Traffic Blocked")
else:
    print("Running SPES Scheduler...")
    node = select_node()
    print("Selected Node:", node)