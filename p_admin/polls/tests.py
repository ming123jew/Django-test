from django.test import TestCase
from threading import Thread
from loguru import logger
import time
# Create your tests here.

# ============= TEST polls models TEST =============
from .tests_files.model import *

# ============= TEST polls views TEST =============
from .tests_files.views import *


# ============= TEST selenium TEST =============
from .tests_files.selenium import *


# def test_polls_views_vote():
#
#     # 并发投票
#     class vote(Thread):
#
#         def __init__(self, name):
#             super(vote, self).__init__()
#             self.name = name
#
#         def run(self) -> None:
#             print(1)
#
#
#     logger.info('=' * 33 + 'START' + '=' * 33)
#     QUIT_TIME = time.time() + 3600 * 24 * 1
#     # 监控进程列表
#     process_list = [
#         'product_1',
#         'product_2',
#         # 'consume',
#     ]
#     threads = []
#
#     for process_name in process_list:
#         t = vote(name=process_name)
#         t.setDaemon(True)
#         t.start()
#         threads.append(t)
#
#     while True:
#         for thread in threads:
#             if not thread.is_alive():
#                 exit(0)
#         time.sleep(2)
#
#     logger.info('=' * 33 + 'QUIT' + '=' * 33)

