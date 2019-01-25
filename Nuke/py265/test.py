# -*- coding: utf-8 -*-
print "=======================threading.Thread继承实现多线程============="
import threading
import time

class DemoThread(threading.Thread):
#Python的所有属性必须给出初始值，否则会出现变量名未定义异常
    data = []
    id = 1
    interval = 0
    __stop = False

    def __init__(self, interval=1):
        #不要忘了父类的
        threading.Thread.__init__(self)
        self.interval = interval
        self.id = DemoThread.getId()

    #覆盖父类run方法定义循环
    def run(self):
        count = 0
        #最好用私有属性作为终止条件
        while count < 2 and not self.__stop:
            print "Thread-%d,休眠间隔：%d,current Time:%s"%(self.id, self.interval, time.ctime())
        #使当前线程休眠指定时间，interval为浮点型的秒数，不同于Java中的整形毫秒数
            time.sleep(self.interval)
            #Python不像大多数高级语言一样支持++操作符，只能用+=实现
            count += 1
            self.data.append(count)
        else:
            print "Thread-%d is over" % self.id

    @staticmethod
    def getId():
        DemoThread.id += 1
        return DemoThread.id

    def stop(self):
        self.__stop = True

newthread = DemoThread(1)
#当主线程结束时，该线程同时结束，只能在start之前设置；false时，不随主线程结束
newthread.setDaemon(True)
newthread.start()
# newthread2.start()
newthread.join()
# newthread2.join()
# for i in range(3):
#     if i == 0:
#         newthread.start()
#     else:
#         newthread.run()
#     newthread.join()
#而这种方式是不需要主线程等待子线程结束的


b = []
c = [0,0]
aa = [1,3,4,5,8,9]
flag = False
for i,a in enumerate(aa):
    if i<len(aa)-2:
        if a != aa[i+1]-1:
            print a
            print aa[i+1]-1
            b.append(a)
            flag = False
            b.append(c)
        else:
            print a
            if not flag:
                c[0] = a
                c[1] = aa[i+1]
                flag = True
            else:
                c[1] = aa[i+1]
    else:
        if a != aa[i-1]+1:
            b.append(a)
            flag = False
        else:
            if flag:
                c[1] = a
    #print a
    #print c