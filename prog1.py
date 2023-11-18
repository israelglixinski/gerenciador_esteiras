
from time import sleep
from threading import Thread

lista = [1,2,3,4,5]

def infinite_loop():
    while True:
        for iten in lista:
            print(iten)
            sleep(2)

if __name__ == '__main__':
    Thread(target=infinite_loop).start()
