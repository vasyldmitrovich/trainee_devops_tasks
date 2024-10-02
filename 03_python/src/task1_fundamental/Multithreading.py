from multiprocessing import Process, Lock
import threading
import time
import datetime
import asyncio

# Count for function
call_count = 0


def somePrint(lock, string):
    global call_count  # Use global variable
    with lock:
        call_count += 1  # Increment
        print(f"print: {string}, call count: {call_count}")  # Print line and count


# Shared counter
counter = 0


# Function to increment the counter
def increment_counter():
    global counter
    for _ in range(100000):  # Increment the counter 100,000 times
        temp = counter  # Read the current value of the counter
        time.sleep(0.00001)  # Simulate a small delay
        counter = temp + 1  # Increment the counter


# ---

# Shared counters
counter_a = 0
counter_b = 0

# Create a lock for each counter
lock_a = threading.Lock()
lock_b = threading.Lock()


# Function to increment counter A
def increment_counter_a():
    global counter_a
    for _ in range(100000):  # Increment counter A 100,000 times
        with lock_a:  # Acquire the lock for counter A
            temp = counter_a  # Read the current value of counter A
            time.sleep(0.00001)  # Simulate a small delay
            counter_a = temp + 1  # Increment counter A


# Function to increment counter B
def increment_counter_b():
    global counter_b
    for _ in range(100000):  # Increment counter B 100,000 times
        with lock_b:  # Acquire the lock for counter B
            temp = counter_b  # Read the current value of counter B
            time.sleep(0.00001)  # Simulate a small delay
            counter_b = temp + 1  # Increment counter B


# ---

# Shared resources (variables)
dedlock_var_a = 0
dedlock_var_b = 0

# Two locks for the resources
dedlock_a = threading.Lock()
dedlock_b = threading.Lock()

# Semaphores for controlling access to resources
semaphore_a = threading.Semaphore(1)  # Changed from Lock to Semaphore
semaphore_b = threading.Semaphore(1)  # Changed from Lock to Semaphore


# Thread 1 tries to acquire lock_a first, then lock_b
def thread_1_task():
    global dedlock_var_a, dedlock_var_b
    print("Thread 1: Attempting to acquire lock_a...")
    #    with dedlock_a:
    with semaphore_a:
        print("Thread 1: Acquired lock_a, working...")
        time.sleep(1)
        print("Thread 1: Attempting to acquire lock_b...")
        #        with dedlock_b:
        with semaphore_b:
            print("Thread 1: Acquired lock_b, updating variables.")
            dedlock_var_a += 1
            dedlock_var_b += 1


# Thread 2 tries to acquire lock_b first, then lock_a
def thread_2_task():
    global dedlock_var_a, dedlock_var_b
    print("Thread 2: Attempting to acquire lock_b...")
    #    with dedlock_b:
    with semaphore_a:
        print("Thread 2: Acquired lock_b, working...")
        time.sleep(1)
        print("Thread 2: Attempting to acquire lock_a...")
        #        with dedlock_a:
        with semaphore_b:
            print("Thread 2: Acquired lock_a, updating variables.")
            dedlock_var_a += 1
            dedlock_var_b += 1


# ---

s = threading.Semaphore(3)


def semaphore_func(payload: int):
    s.acquire()
    now = datetime.datetime.now().strftime('%H:%M:%S')
    print(f'{now=}, {payload=}')
    time.sleep(2)
    s.release()


# ---

# Asynchronous function (coroutine) that simulates a task
async def async_task(name, delay):
    print(f"Task {name} started, will take {delay} seconds...")
    await asyncio.sleep(delay)  # Simulate some asynchronous work
    print(f"Task {name} completed.")


# Add this code in the main method at the end:
async def main_async():
    await asyncio.gather(
        async_task("A", 2),  # Task A will take 2 seconds
        async_task("B", 3)  # Task B will take 3 seconds
    )


# ---

if __name__ == '__main__':
    print("Some examples of multithreading")
    lock = Lock()  # Create Lock object
    p1 = Process(target=somePrint, args=(lock, 'bob'), daemon=True)
    p2 = Process(target=somePrint, args=(lock, 'stinger'), daemon=True)

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    # ---
    t1 = threading.Thread(target=somePrint, args=(lock, 'bob',), daemon=True)
    t2 = threading.Thread(target=somePrint, args=(lock, 'alice',), daemon=True)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    # ---
    # Create two threads that will increment the counter
    thread1 = threading.Thread(target=increment_counter)
    thread2 = threading.Thread(target=increment_counter)

    # Start the threads
    thread1.start()
    thread2.start()

    # Wait for both threads to finish
    thread1.join()
    thread2.join()

    # Print the final value of the counter
    print(f"Final counter value: {counter}")

    # ---

    print("Demonstrating race condition resolution with multiple threads")

    # Create two threads for incrementing counter A
    thread1_a = threading.Thread(target=increment_counter_a)
    thread2_a = threading.Thread(target=increment_counter_a)

    # Create two threads for incrementing counter B
    thread1_b = threading.Thread(target=increment_counter_b)
    thread2_b = threading.Thread(target=increment_counter_b)

    # Start the threads for counter A
    thread1_a.start()
    thread2_a.start()

    # Start the threads for counter B
    thread1_b.start()
    thread2_b.start()

    # Wait for all threads to finish
    thread1_a.join()
    thread2_a.join()
    thread1_b.join()
    thread2_b.join()

    # Print the final values of the counters
    print(f"Final value of counter A: {counter_a}")  # Should be 200000
    print(f"Final value of counter B: {counter_b}")  # Should be 200000

    # ---

    # Create threads
    dead_lock1 = threading.Thread(target=thread_1_task)
    dead_lock2 = threading.Thread(target=thread_2_task)

    # Start threads
    dead_lock1.start()
    dead_lock2.start()

    # Wait for both threads to finish
    dead_lock1.join()
    dead_lock2.join()

    print(f"Final values: dedlock_var_a = {dedlock_var_a}, dedlock_var_b = {dedlock_var_b}")

    # ---

    threads = [threading.Thread(target=semaphore_func, args=(i,)) for i in range(7)]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    # ---

    asyncio.run(main_async())
