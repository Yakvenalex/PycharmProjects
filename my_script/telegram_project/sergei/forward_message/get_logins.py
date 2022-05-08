logins = []
with open('logins.txt', newline='', encoding="utf-8") as file:
    for i in file:
        logins.append(i.strip())