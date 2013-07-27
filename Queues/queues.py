from control import Control
import threading
import Queue
#import time

exit_marker = object()

class Modem(threading.Thread):
	def __init__(self, thread_id, queue):
		threading.Thread.__init__(self)
		self.thread_id = thread_id
		self.queue = queue
	
	def run(self):
		self.queue.put(self)
		
class MacDomain:
	def __init__(self, queue):
		all_threads = []
		for x in range(5):
			modem = Modem(x, queue)
			all_threads += [modem]
			modem.start()
		for thread in all_threads:
			thread.join
		global exit_marker
		queue.put(exit_marker)

def main():
	queue = Queue.Queue()
	control = Control(queue, exit_marker)
	control.start()
	mac_domain = MacDomain(queue)
	control.join()
	
	#time.sleep(10)
	print (control.is_alive())
	control.close()
	del control
	
if __name__ == "__main__":
		main()
