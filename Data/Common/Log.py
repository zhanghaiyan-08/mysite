#!/usr/bin/env python3 
# -*- coding:utf-8 -*-
__author__ = 'zhanghaiyan'

import os
import logging
from logging.handlers import TimedRotatingFileHandler
import Data.Common.getFilePath  as getpath
import time

path = getpath.get_Path()
log_path = os.path.join('D:\QIyun_API', 'result')  # 存放log文件的路径

class Logger(object):
    def __init__(self, logger_name='logs…'):
        self.logger = logging.getLogger(logger_name)
        logging.root.setLevel(logging.NOTSET)
        logname=time.strftime("%Y-%m-%d", time.localtime()) + '-logs'
        self.log_file_name = logname  # 日志文件的名称
        self.backup_count = 5  # 最多存放日志的数量
        # 日志输出级别
        self.console_output_level = 'DEBUG'
        self.file_output_level = 'DEBUG'
        # 日志输出格式
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def get_logger(self):
        """在logger中添加日志句柄并返回，如果logger已有句柄，则直接返回"""
        if not self.logger.handlers:  # 避免重复日志
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)

            # 每天重新创建一个日志文件，最多保留backup_count份
            file_handler = TimedRotatingFileHandler(filename=os.path.join(log_path, self.log_file_name), when='D',
                                                    interval=1, backupCount=self.backup_count, delay=True,
                                                    encoding='utf-8')
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)
        return self.logger


logger = Logger().get_logger()
'''
日志级别： debug < info < warning < error < critical
logging.debug('debug级别，最低级别，一般开发人员用来打印一些调试信息')
logging.info('info级别，正常输出信息，一般用来打印一些正常的操作')#在处理请求或者服务器状态变化等日常事务中
logging.warning('waring级别，一般用来打印警信息')
logging.error('error级别，一般用来打印一些错误信息')#比如抛出异常，IO 操作失败或者连接问题等。
logging.critical('critical 级别，一般用来打印一些致命的错误信息,等级最高')
logger.debug('this is a log')
logger.info('this is a log')

'''
# import os
# import logging
# from datetime import datetime
# import threading
#
# localReadConfig = readConfig.ReadConfig()
#
#
# class Log:
#     def __init__(self):
#         global logPath, resultPath, proDir
#         proDir = readConfig.proDir
#         resultPath = os.path.join(proDir, "result")
#         if not os.path.exists(resultPath):
#             os.mkdir(resultPath)
#         logPath = os.path.join(resultPath, str(datetime.now().strftime("%Y%m%d%H%M%S")))
#         if not os.path.exists(logPath):
#             os.mkdir(logPath)
#         self.logger = logging.getLogger()
#         self.logger.setLevel(logging.INFO)
#
#         # defined handler
#         handler = logging.FileHandler(os.path.join(logPath, "output.log"))
#         # defined formatter
#         formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#         handler.setFormatter(formatter)
#         self.logger.addHandler(handler)
#
#     def get_logger(self):
#         """
#         get logger
#         :return:
#         """
#         return self.logger
#
#     def build_start_line(self, case_no):
#         """
#         write start line
#         :return:
#         """
#         self.logger.info("--------" + case_no + " START--------")
#
#     def build_end_line(self, case_no):
#         """
#         write end line
#         :return:
#         """
#         self.logger.info("--------" + case_no + " END--------")
#
#     def build_case_line(self, case_name, code, msg):
#         """
#         write test case line
#         :param case_name:
#         :param code:
#         :param msg:
#         :return:
#         """
#         self.logger.info(case_name+" - Code:"+code+" - msg:"+msg)
#
#     def get_report_path(self):
#         """
#         get report file path
#         :return:
#         """
#         report_path = os.path.join(logPath, "report.html")
#         return report_path
#
#     def get_result_path(self):
#         """
#         get test result path
#         :return:
#         """
#         return logPath
#
#     def write_result(self, result):
#         """
#
#         :param result:
#         :return:
#         """
#         result_path = os.path.join(logPath, "report.txt")
#         fb = open(result_path, "wb")
#         try:
#             fb.write(result)
#         except FileNotFoundError as ex:
#             logger.error(str(ex))
#
#
# class MyLog:
#     log = None
#     mutex = threading.Lock()
#
#     def __init__(self):
#         pass
#
#     @staticmethod
#     def get_log():
#
#         if MyLog.log is None:
#             MyLog.mutex.acquire()
#             MyLog.log = Log()
#             MyLog.mutex.release()
#
#         return MyLog.log
#
# if __name__ == "__main__":
#     log = MyLog.get_log()
#     logger = log.get_logger()
#     logger.debug("test debug")
#     logger.info("test info")
