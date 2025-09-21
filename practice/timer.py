from threading import Timer

def task(msg): print(msg)

t = Timer(1, task, ['task finished'])
t.start()
