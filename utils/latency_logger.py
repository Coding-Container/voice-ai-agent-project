import time

def start_timer():
    return time.time()

def end_timer(start):
    latency = time.time() - start
    print("Latency:", latency)

def measure_latency(func):

    def wrapper(*args, **kwargs):

        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        latency = end - start

        print(f"⚡ Latency: {latency:.4f} seconds")

        return result

    return wrapper