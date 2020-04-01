# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:          test2
# Author:        xiaohuo
# Date:          2020/3/30
# Prohect_Name:  data_structure
# IEDA_Name:     PyCharm
# Create_Time:   15:00 
# -------------------------------------------------------------------------------
"""
模拟打印进行打印
"""
import random
from Queues.queuebase import Queue


class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm  # 打印速度(每分钟打印的数量)
        self.currentTask = None  # 打印状态
        self.timeRemaining = 0  # 打印时间

    def tick(self):
        """
        执行判断是否有任务在执行
        :return:
        """
        if self.busy():
            self.timeRemaining -= 1
            if self.timeRemaining <= 0:
                self.currentTask = None  # 没有打印任务

    def busy(self):
        """
        判断打印机状态
        :return:
        """
        return True if self.currentTask != None else False

    def startNext(self, newtask):
        """
        打印机处于工作状态的时候
        :param newtask:下一个打印任务
        :return:
        """
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60 / self.pagerate    # 打印者打印所需的时间


class Task:
    def __init__(self, time, pages):
        self.timestamp = time                           # 进入打印机的时间
        self.pages = pages                              # 打印者需要打印的页数

    def getStamp(self):
        """
        返回时间戳
        :return:
        """
        return self.timestamp

    def getPages(self):
        """
        返回页数
        :return:随机生成的页数
        """
        return self.pages

    def waitTime(self, currentime):
        """
        打印任务等待时间
        :param currentime: 打印任务进入时间戳
        :return: 等待时间
        """
        return currentime - self.timestamp


class PrintQueue:
    def newPrintTask(self):
        """
        随机生成时间，当等于180时生成一个打印任务
        :return:
        """
        num = random.randrange(1, 181)
        return True if num==180 else False

    def simulation(self, numSeconds, pagesPerMinute):
        labprinter = Printer(pagesPerMinute)    # 打印速度
        printerQueue = Queue()                  # 打印机对象队列
        waitingtimes = []                       # 等待时间列表

        for currentSecond in range(numSeconds):     # 3600
            if self.newPrintTask():
                task = Task(currentSecond, random.randrange(1, 21))
                printerQueue.enqueue(task)
            if not labprinter.busy() and not printerQueue.isEmpty():
                nexttask = printerQueue.dequeue()
                waitingtimes.append(nexttask.waitTime(currentSecond))
                labprinter.startNext(nexttask)

            labprinter.tick()

        print(waitingtimes)
        print(len(waitingtimes))
        if len(waitingtimes) == 0:
            raise  Exception("除数为零")
        else:
            averageWait = sum(waitingtimes) / len(waitingtimes)         # 计算平均等待时间
        print("Average Wait %6.2f secs %3d tasks remaining." %(averageWait, printerQueue.size()))


if __name__ == '__main__':
    printerQueue = PrintQueue()
    # for i in range(random.randrange(1, 100)):
    printerQueue.simulation(3600, random.randrange(1, 30))






























































