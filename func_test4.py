import  time

# print(time.time())
# time.sleep(3)

def timmer(func):
    def wrapper():
        start_time = time.time()
        func()
        start_time=time.time()
        print('函数运行了 %s 秒' %(start_time-start_time))
    return wrapper

@timmer
def i_can_sleep():
    time.sleep(8)

# start_time = time.time()

i_can_sleep()
# start_time=time.time()
# print('函数运行了 %s 秒' %(start_time-start_time))