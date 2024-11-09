import threading
import time

num_philosophers = 6
forks = [threading.Semaphore(1) for _ in range(num_philosophers)]

def philosopher(index):
    left_cs = forks[index]
    right_cs = forks[(index + 1) % num_philosophers]
    while True:
        print(f"Philosopher {index} is thinking")
        time.sleep(1)
        left_cs.acquire()
        right_cs.acquire()
        print(f"Philosopher {index} is eating")
        time.sleep(1)
        left_cs.release()
        right_cs.release()

if __name__ == "__main__":
    threads = [threading.Thread(target=philosopher, args=(i,)) for i in range(num_philosophers)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
