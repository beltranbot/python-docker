from queue import Queue

q = Queue()

q.put(1)
q.put(2)
q.put(3)

first = q.get()
print(first)

q.task_done() # a formerly enqueued tasks has been completed
q.join() # all the items on the queue have been processed


print('end main')