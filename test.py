import threading
import time

def func1(sec):
    print(f"Sleeping for {sec} sec")
    time.sleep(sec)
    print(f"done {sec}")

# def func2():
#     print("sleeping for 3 sec")
#     time.sleep(3)
#     print("done")

# def func3():
#     print("sleeping for 1 sec")
#     time.sleep(1)
#     print("done")


t1 = threading.Thread(target=func1,args=[5])
t2 = threading.Thread(target=func1,args=[3])
t3 = threading.Thread(target=func1,args=[1])
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()

print("completed")