import time
import sched2

def tell_time(job):
	print(time.strftime('Time: %H:%M:%S'))

@sched2.times(2)
def say_hello_twice(job):
	print('Hello!')

sched2.Scheduler()\
	.add_job(
		callback=say_hello_twice,
		delay_seconds=0
	)\
	.start(delay_seconds=5)

start_at = time.time() + 60

sched2.Scheduler()\
	.add_job(
		callback=tell_time,
		delay_seconds=60,
		start_at=start_at)\
	.add_job(
		callback=say_hello_twice,
		delay_seconds=0)\
	.start(delay_seconds=15)
