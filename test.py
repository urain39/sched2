import time
import sched2
from datetime import datetime

def tell_time(job):
	print(time.strftime('Time: %H:%M:%S'))

def say_hello_once(job):
	print('Hello!')
	job.stop()

sched2.Scheduler()\
	.add_job(
		callback=tell_time,
		delay_seconds=60,
		start_at=time.mktime(
			datetime.now().replace(second=0).timetuple()))\
	.add_job(
		callback=say_hello_once,
		delay_seconds=0
	)\
	.start(15)
