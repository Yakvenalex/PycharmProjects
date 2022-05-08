import random

hello = []
phrase = []
chan = []
poka = []
def say_hello(hello):

    with open('hello_list.txt', 'r', newline='', encoding="utf-8") as file:
        for i in file:
            hello.append(i.strip())

    random_index = random.randint(0, len(hello) - 1)
    return hello[random_index]

def present(phrase):
    with open('present..txt', newline='', encoding="utf-8") as file:
        for i in file:
            i = i.strip().split('|')
            random_index = random.randint(0, len(i) - 1)
            phrase.append(i[random_index])
    my_phrase = ' '.join(phrase)
    return my_phrase

def present_chanel(chan):
    with open('chanel.txt', newline='', encoding="utf-8") as file:
        for i in file:
            i = i.strip().split('|')
            random_index = random.randint(0, len(i) - 1)
            chan.append(i[random_index])
    my_chanel = ' '.join(chan)
    return my_chanel

def poka_by(poka):
    with open('poka.txt', newline='', encoding="utf-8") as file:
        for i in file:
            i = i.strip().split('|')
            random_index = random.randint(0, len(i) - 1)
            poka.append(i[random_index])
    my_poka = ' '.join(poka)
    return my_poka