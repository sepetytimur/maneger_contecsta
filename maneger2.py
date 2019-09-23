


class Dateserch:
    def __init__(self, mode = 'rt'):
       self.file = open(mode)
    def __enter__(self):
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
with Dateserch('cookbook', 'r') as f:
