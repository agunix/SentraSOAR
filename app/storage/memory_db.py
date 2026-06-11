class MemoryDB:
    def __init__(self):
        self.alerts = []
        self.incidents = []
        self.counter = 1


db = MemoryDB()