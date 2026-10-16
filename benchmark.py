
import time

from my_advanced_lib import (
    batch_generator,
    fibonacci_generator,
)


def benchmark_fibonacci():
    start = time.perf_counter()
    list(fibonacci_generator(10000))
    end = time.perf_counter()

    print(f"Fibonacci generator: {end - start:.6f} seconds")


def benchmark_batch():
    data = range(100000)

    start = time.perf_counter()
    list(batch_generator(data, 1000))
    end = time.perf_counter()

    print(f"Batch generator: {end - start:.6f} seconds")


def main():
    print("Library Performance Benchmark")
    print("-" * 35)

    benchmark_fibonacci()
    benchmark_batch()


if __name__ == "__main__":
    main()
