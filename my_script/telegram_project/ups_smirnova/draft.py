import random
l = []

with open('hello_list.txt', 'r', newline='', encoding="utf-8") as file:
    for i in file:
        l.append(i.strip())

random_index = random.randint(0, len(l) - 1)
print(l[random_index])