## implementing a context manager in our own classes : start
# to use context manager with a custom class, you must implement the __enter__ and __exit__ functions in the class
class ManagedFile:
    def __init__(self, filename):
        self.filename = filename
        pass

    def __enter__(self):
        print('enter')
        self.file = open(self.file, 'w')
        return self.file


    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        print('exit')


with ManagedFile('notes.txt') as file:
    print('do some stuff')
    file.write('some todoo ')
## implementing a context manager in our own classes : end

## use context manager as a function : start
from contextlib import contextmanager

@contextmanager
def open_managed_file(filename):
    f = open(filename, 'w')
    try:
        yield f
    finally:
        f.close()

with open_managed_file('notes.txt') as f:
    f.write('some todoo....')
## use context manager as a function : end
