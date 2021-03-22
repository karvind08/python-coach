import time
import concurrent.futures
start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second')
    time.sleep(seconds)
    return 'Done Sleeping'

if __name__ == '__main__':
	with concurrent.futures.ProcessPoolExecutor() as executor:
		f1=executor.submit(do_something,1)
		print(f1.result())


finish = time.perf_counter()
print(f'Finished in {round(finish-start,2)} second(s)')