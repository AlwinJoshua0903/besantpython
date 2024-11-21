import threading
import time
import datetime
'''
print("________________________without thread_____________________________")
sq = []
cu = []

def square(Threadname, endpoint, delay):
    for i in range(1, endpoint + 1):
        sq.append(i ** 2)
        print(f"Thread name was={Threadname} and sq value is={sq}")
        time.sleep(delay)

def cube(Threadname, endpoint, delay):
    for i in range(1, endpoint + 1):
        cu.append(i ** 3)
        print(f"Thread name was={Threadname} and cu value is={cu}")
        time.sleep(delay)

# Measure the start time
start_time = time.time()

# Perform square calculations sequentially
square("thread1", 10, 2)
print("---------------------------------------------")

# Perform cube calculations sequentially
cube("thread2", 10, 2)

# Measure the end time
end_time = time.time()

# Calculate the duration
duration = end_time - start_time
print(f"All operations completed in {duration:.2f} seconds.")


print("________________________with thread_____________________________")


sq = []
cu = []

def square(thread_name, endpoint, delay):
    for i in range(1, endpoint + 1):
        sq.append(i * i)
        print(f"Thread name: {thread_name}, square value: {sq}")
        time.sleep(delay)

def cube(thread_name, endpoint, delay):
    for i in range(1, endpoint + 1):
        cu.append(i ** 3)  # Corrected to cube calculation
        print(f"Thread name: {thread_name}, cube value: {cu}")
        time.sleep(delay)

# Measure the start time
start_time = time.time()

# Create threads
square_thread = threading.Thread(target=square, args=("thread-1", 10, 2))
cube_thread = threading.Thread(target=cube, args=("thread-2", 10, 2))

# Start threads
square_thread.start()
cube_thread.start()

# Wait for both threads to complete
square_thread.join()
cube_thread.join()

# Measure the end time
end_time = time.time()

# Calculate the duration
duration = end_time - start_time
print(f"All operations completed in {duration:.2f} seconds.")



'''

print("________________________with thread_____________________________")

def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(threadName, datetime.datetime.now())

# Create two threads as follows
try:
    thread1 = threading.Thread(target=print_time, args=("Thread-1", 2,))
    thread2 = threading.Thread(target=print_time, args=("Thread-2", 4,))

    # Start threads
    thread1.start()
    thread2.start()

    # Wait for both threads to complete
    thread1.join()
    thread2.join()
except Exception as e:
    print(f"Error: unable to start thread due to {e}")

print("All threads have completed execution.")
