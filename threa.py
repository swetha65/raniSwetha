import threading
def func(n):
    print('Thread {} is runnning'.format(n))

print('Main beginning')
x = [threading.Thread(target = func, args = (i,)) for i in range(10)]
for t in x:
    t.start()
print('Main all done')
