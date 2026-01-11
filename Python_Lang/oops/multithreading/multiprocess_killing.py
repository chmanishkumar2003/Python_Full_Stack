import multiprocessing
import time

def task():
    print("This is a separate process!")
    time.sleep(5)  # Simulate some work

if __name__ == "__main__":
    process = multiprocessing.Process(target=task)

    process.start()
    print(f"Process started: {process.pid}")

    time.sleep(2)  # Wait before killing/terminating

    if process.is_alive():
        process.terminate()  # cross-platform method
        print("Process terminated")

    process.join()  # Wait for cleanup
    print("Process joined (cleaned up)")
