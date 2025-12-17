text_list = ["Hello World", "Python", "Artificial Intelligence", "Yunnan University"]
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
d = {phrase: sum(1 for char in phrase if char in vowels) for phrase in text_list}
print(d)