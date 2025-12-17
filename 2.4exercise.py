

# Exercise 2.4 ======================

class Scores:
    __solts__ = ["Python", "Java", "C_Plus"]

    def __init__(self, Python, Java, C_Plus):
        self.Python = Python
        self.Java = Java
        self.C_Plus = C_Plus

    def __getattr__(self, attrname):
        print(f"no attribute {attrname}.")

    def __lt__(self, other):
        sum_self = self.Python + self.Java + self.C_Plus
        sum_other = other.Python + other.Java + other.C_Plus
        return sum_self < sum_other

a = Scores(61, 75, 63)
b = Scores(71, 72, 73)
a.English
print(a < b)