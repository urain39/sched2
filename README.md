# sched2
极简主义化的Scheduler实现。

### 使用方法
```py
import sched2

def say_hello(job):
	print('Hello')

sched2.Scheduler()\
	.add_job(
		callback=say_hello,
		delay_seconds=10,
		start_at=None)\
	.start(delay_seconds=5)
```

# 高级用法
```py
import time
import sched2
from datetime import datetime, timedelta

def tell_time(job):
	print(time.strftime('Time: %H:%M:%S'))

def say_hello_once(job):
	print('Hello!')
	job.stop()

start_at = datetime.now().replace(minute=0, second=0) + timedelta(hours=1)

sched2.Scheduler()\
	.add_job(
		callback=tell_time,
		delay_seconds=60,
		start_at=time.mktime(start_at.timetuple()))\
	.add_job(
		callback=say_hello_once,
		delay_seconds=0
	)\
	.start(10)
```

用户自定义的`callback`函数接收一个参数，这个参数就是`callback`被包装后的
`Job`实例，一般用于将一个任务关闭。这样设计目的是让用户不用显示的实例化`Job`
，简化流程。

## 关于`start_at`的“bug”
`start_at`可能会造成间隔时间不起作用的问题，原因是因为`start_at`会被赋值到
`Job`中的`next_time`属性上，而这个属性会基于`delay_seconds`在每次执行完后
自增，当自增后`next_time`依然小于`time.time()`时就会发生这样的情况。

简而言之就是`Job`的`next_time`太小了造成的。默认的`next_time`是`time.time()`，
而一般情况下这个值比`time.time()`大一些就不会出现这个“bug”了。
