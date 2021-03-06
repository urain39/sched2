import time

"""
基础使用方法：
import sched2

def say_hello(job):
	print('Hello')

sched2.Scheduler()\
	.add_job(
		callback=say_hello,
		delay_seconds=10,
		start_at=None)\
	.start(delay_seconds=5)
"""


def times(count):
	"""
	限制某个任务执行次数的装饰器。
	"""
	def wrapper(fn):
		c = [0]
		def wrapped(job):
			if c[0] < count:
				fn(job)
				c[0] += 1
			else:
				job.stop()
		return wrapped
	return wrapper


class SchedulerError(Exception):
	pass


class Scheduler():
	"""
	用于管理任务计划的类。
	"""
	def __init__(self):
		self.jobs = []
		self.is_running = False

	def add_job(self, *args, **kwargs):
		"""
		添加一个任务。
		"""
		self.jobs.append(Job(*args, **kwargs))
		return self

	def start(self, delay_seconds=10):
		"""
		开始执行任务表。
		"""
		if self.is_running:
			raise SchedulerError('Scheduler has already running!')
		self.is_running = True
		jobs = [job for job in self.jobs if job.is_running]
		while len(jobs) > 0:
			for job in jobs:
				if time.time() >= job.next_time:
					job.run()
			# 检测任务列表是否有已停止的任务
			for job in jobs:
				if not job.is_running:
					# 如果有则过滤掉已停止的任务
					jobs = [job for job in jobs if job.is_running]
					break
			time.sleep(delay_seconds)
		self.is_running = False

class Job():
	"""
	用于包装用户任务的类。
	"""
	def __init__(self, callback, delay_seconds, start_at=None):
		self.callback = callback
		self.delay_seconds = delay_seconds
		self.next_time = start_at if isinstance(
			start_at, (int, float)) else time.time()
		self.is_running = True  # 创建即运行

	def __bool__(self):
		return self.is_running

	def run(self):
		"""
		执行当前任务。
		"""
		self.callback(self)
		self.next_time += self.delay_seconds

	def stop(self):
		"""
		通过设置flag停止当前的任务。
		"""
		self.is_running = False
