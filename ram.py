import psutil
import time

def get_ram():
    # Get the system RAM information
    ram = psutil.virtual_memory()
    return ram.total

def run_as_service():
    while True:
        total_ram = get_ram()
        print("Total system RAM: ", total_ram)
        # Sleep for 5 seconds before checking again
        time.sleep(60)
run_as_service()