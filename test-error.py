import threading
import sched2

def say_hello(job):
	print('Hello')

sch = sched2.Scheduler()\
	.add_job(
		callback=say_hello,
		delay_seconds=10,
		start_at=None)

for t in [
	threading.Thread(target=lambda : sch.start()).start(),
	threading.Thread(target=lambda : sch.start()).start()
]:
	t.join()
