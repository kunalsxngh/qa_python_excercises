class students:

    def __init__(self, name, age, className = "student"):
        self.name = name
        self.age = age
        self.className = className

    
    def average_test_scores(self, test1, test2, test3):
        return round(((test1 + test2 + test3) / 3), 2)