from concurrent.futures import ProcessPoolExecutor
import os


def task():
    print('Executing our task on process: {}'.format(os.getpid()))


def main():
    executor = ProcessPoolExecutor(max_workers=2)
    task1 = executor.submit(task)
    task2 = executor.submit(task)


if __name__ == '__main__':
    main()
