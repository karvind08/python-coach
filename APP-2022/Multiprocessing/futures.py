import time
from concurrent.futures import ProcessPoolExecutor
start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second')
    time.sleep(seconds)
    return 'Done Sleeping'


if __name__ == '__main__':
    with ProcessPoolExecutor() as executor:
        f1 = executor.submit(do_something, 2)
        print(f1.result())
        finish = time.perf_counter()
        print(f'Finished in {round(finish-start,2)} second(s)')
