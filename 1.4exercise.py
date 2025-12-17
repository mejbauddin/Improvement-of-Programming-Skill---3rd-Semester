
# Exercise 1.4 ======================

class Student:
    def __init__(self, name, student_Id):
        self.__name = name
        self.__student_Id = student_Id
        self.__scores = []

        print (f"I am {name} and my Student Id {student_Id}")

    def add_score(self, score):
        self.__scores.append(score)

    def get_average(self):
        if not self.__scores:
            return 0
        return sum(self.__scores) / len(self.__scores)


st = Student("Uddin Mejbah", "20243120031")
st.add_score(95)
st.add_score(90)
print(st.get_average())
