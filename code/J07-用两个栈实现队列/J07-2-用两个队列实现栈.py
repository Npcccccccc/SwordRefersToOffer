from queue import Queue

class Solution:
    def __init__(self):
        self.queue1 = Queue(50)
        self.queue2 = Queue(50)

    def push(self, node):
        if self.queue1.empty():
            self.queue2.put(node)
        elif self.queue2.empty():
            self.queue1.put(node)
    
    def pop(self):
        if not self.queue1.empty():
            while self.queue1.qsize() != 1:
                self.queue2.put(self.queue1.get())
            return self.queue1.get()
        elif not self.queue2.empty():
            while self.queue2.qsize() != 1:
                self.queue1.put(self.queue2.get())
            return self.queue2.get()
