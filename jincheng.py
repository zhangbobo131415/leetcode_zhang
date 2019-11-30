import multiprocessing as mp
import os

# Run phase
def v():
    print('Run', os.getpid())
    print(__name__, os.getpid())

# Initialization phase
print('Initialize', os.getpid())
print(__name__, os.getpid())

if __name__ == '__main__':
    # start a new Process to execute function `v` and wait for it
    p = mp.Process(target=v)
    p.start()
    p.join()