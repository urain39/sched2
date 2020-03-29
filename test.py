import time
import sched2
from datetime import datetime, timedelta

def tell_time(job):
	print(time.strftime('Time: %H:%M:%S'))

@sched2.times(1)
def say_hello_once(job):
	print('Hello!')

sched2.Scheduler()\
	.add_job(
		callback=say_hello_once,
		delay_seconds=0
	)\
	.start(delay_seconds=5)

start_at = datetime.now().replace(minute=0, second=0) + timedelta(hours=1)

sched2.Scheduler()\
	.add_job(
		callback=tell_time,
		delay_seconds=60,
		start_at=time.mktime(start_at.timetuple()))\
	.add_job(
		callback=say_hello_once,
		delay_seconds=0)\
	.start(delay_seconds=15)
