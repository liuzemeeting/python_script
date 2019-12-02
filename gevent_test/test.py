# gevent是python的一个并发框架，以微线程greenlet为核心,使用了epoll事件监听机制以及诸多其他优化而变得高效
# 当一个greenlet遇到IO操作时，比如访问网络/睡眠等待,就自动切换到其他的greenlet,等到IO操作完成，再在适当的时候切换回来继续执行
import gevent
from gevent import monkey, lock, Greenlet
sem = lock.Semaphore(1)


def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # gevent.sleep(2)

list = []


def test1(n):
    gevent.kill(n)
    for i in range(n):
        print("run test1, this is", i)
        for item in range(1003000):
            list.append(i)


def test2(n):
    for i in range(n):
        print("run test2, this is", i)


if __name__ == '__main__':
    g1 = gevent.spawn(f, 5)
    g2 = gevent.spawn(f, 6)
    g3 = gevent.spawn(f, 7)
    t1 = gevent.spawn(test1, 7)
    t2 = gevent.spawn(test2, 10)
    # g1.join()
    # g2.join()
    # g3.join()
    gevent.joinall([t2])