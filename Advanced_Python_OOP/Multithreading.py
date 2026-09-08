
""" 
# Multithreading in Python allows for concurrent execution of code, enabling multiple threads to run simultaneously. This can be useful for tasks that are I/O-bound or require parallel processing.

Thread-- It is a smaller unit of work inside a program





# without multithreading
import time


def download_file(file_name):
    print(f"Starting download of {file_name}...")
    # Simulate a time-consuming download task
    import time
    time.sleep(2)
    print(f"Finished downloading {file_name}.")

    # we will calculate the time
start_time = time.time()
download_file("python.pdf")
download_file("Info.pdf")
download_file("deploy.pdf")
end_time = time.time()
print(f"Total time taken: {end_time - start_time:.2f} seconds")
"""
# with multithreading
import threading
import time

def download_file(file_name):
    print(f"Starting download of {file_name}...")
    # Simulate a time-consuming download task
    time.sleep(2)
    print(f"Finished downloading {file_name}.")

# Create threads for each file download
threads = []
start_time = time.time()

for file_name in ["python.pdf", "Info.pdf", "deploy.pdf"]:
    thread = threading.Thread(target=download_file, args=(file_name,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

end_time = time.time()
print(f"Total time taken: {end_time - start_time:.2f} seconds")