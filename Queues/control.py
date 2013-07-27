import threading
import Queue

class Control(threading.Thread):
	def __init__(self, queue, exit_marker):
		threading.Thread.__init__(self)
		self.queue = queue
		self.exit = exit_marker
		self.fh = open('./result.html', 'w')

	def run(self):
		while True:
			modem = self.queue.get()
			if modem is self.exit:
				break
			print (str(modem.thread_id))
			self.fh.write('Thread ID: ' + str(modem.thread_id) + '\n')
			self.queue.task_done()

	def close(self):
		self.fh.write('Methodes can still be called after join()...')
		self.fh.close()
