import threading

print("current thread that is running: ", threading.current_thread().getName())

if threading.current_thread() == threading.main_thread():
    print("main thread")
    
else:
    print("other")