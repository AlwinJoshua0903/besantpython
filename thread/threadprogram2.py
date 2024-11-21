import threading
import requests
import time
'''
print("________________________without thread_____________________________")

# List of URLs to fetch data from
urls = [
    "https://jsonplaceholder.typicode.com/posts",
    "https://jsonplaceholder.typicode.com/comments",
    "https://jsonplaceholder.typicode.com/albums",
    "https://jsonplaceholder.typicode.com/photos",
    "https://jsonplaceholder.typicode.com/todos",
    "https://jsonplaceholder.typicode.com/users"
]

# Function to fetch data from a URL
def fetch_data(url):
    print(f"Starting fetch for {url}")
    response = requests.get(url)
    print(response.json())
    if response.status_code == 200:
        print(f"Successfully fetched data from {url}")
    else:
        print(f"Failed to fetch data from {url}")
    time.sleep(1)  # Simulate a delay
    print(f"Completed fetch for {url}")

# Measure the start time
start_time = time.time()

# Fetch data from each URL sequentially
for url in urls:
    fetch_data(url)

# Measure the end time
end_time = time.time()

# Calculate the duration
duration = end_time - start_time
print(f"All fetch operations completed in {duration:.2f} seconds.")

'''
print("________________________with thread_____________________________")


# List of URLs to fetch data from
urls = [
    "https://jsonplaceholder.typicode.com/posts",
    "https://jsonplaceholder.typicode.com/comments",
    "https://jsonplaceholder.typicode.com/albums",
    "https://jsonplaceholder.typicode.com/photos",
    "https://jsonplaceholder.typicode.com/todos",
    "https://jsonplaceholder.typicode.com/users"
]

# Function to fetch data from a URL
def fetch_data(url):
    print(f"Starting fetch for {url}")
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Successfully fetched data from {url}")
    else:
        print(f"Failed to fetch data from {url}")
    time.sleep(1)  # Simulate a delay
    print(f"Completed fetch for {url}")

# Measure the start time
start_time = time.time()

# List to hold threads
threads = []

# Create a thread for each URL
for url in urls:
    thread = threading.Thread(target=fetch_data, args=(url,))
    print(thread)
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Measure the end time
end_time = time.time()

# Calculate the duration
duration = end_time - start_time
print(f"All fetch operations completed in {duration:.2f} seconds.")


