from threading import *

def disp(a):
	print('Thread is running with value',a)

for i in range(5):
	t = Thread(target=disp,args=(12,))
	t.start()
