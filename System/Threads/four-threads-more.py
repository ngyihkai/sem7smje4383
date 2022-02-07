"""
nested scope state an bound methods further cloud the coding choices
"""

import threading, _thread

# a non-thread class with state, OOP
class Power:
    def __init__(self, i):
        self.i = i
    def action(self):
        print(self.i ** 32)

obj = Power(2)
#thread 1
threading.Thread(target=obj.action).start()        # thread runs bound method

# nested scope to retain state
def action(i):
    def power():   
        print(i ** 32)
    return power

#thread 2
threading.Thread(target=action(2)).start()         # thread runs returned function

# both with basic thread module
#thread 3, get the class method
_thread.start_new_thread(obj.action, ())           # thread runs a callable object
#thread 4, get the function
_thread.start_new_thread(action(2), ())