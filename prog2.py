
from time import sleep
from threading import Thread

lista = ['a','b','c','d','e']

def infinite_loop():
    while True:
        for iten in lista:
            print(iten)
            sleep(2)

if __name__ == '__main__':
    Thread(target=infinite_loop).start()
