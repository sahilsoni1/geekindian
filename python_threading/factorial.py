from threading import Lock,RLock,Thread

lock = Lock()
out=0;
def factorial(n):
    assert n > 0
    global out
    if n == 1:
        return 1

    print(lock.acquire())

    out = n * factorial(n - 1)
    return out

if __name__ == '__main__':
    t1 = Thread(name="test1",target=factorial,args=(5,)) 
    t1.start()
    t1.join()
    print(out)
