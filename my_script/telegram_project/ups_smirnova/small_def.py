import random

hello = []

def say_hello(hello):

    with open('hello_list.txt', 'r', newline='', encoding="utf-8") as file:
        for i in file:
            hello.append(i.strip())

    random_index = random.randint(0, len(hello) - 1)
    return hello[random_index]

print(say_hello(hello))