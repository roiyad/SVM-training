# import threading
#
# class Mission(threading.Thread):
#     def __init__(self, task):
#         threading.Thread.__init__(self, target=task)
#
#         if self.isAlive():
#             master.thread_enviar = self
#             self.start()