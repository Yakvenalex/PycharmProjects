import csv

def write_csv(data):
    with open('names.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow((data['name'],
                         data['surname'],
                         data['age']))
def write_csv2(data):
    with open('names.csv', 'a', newline='') as file:
        order = ['name','surname','age']
        writer = csv.DictWriter(file, fieldnames=order)

        writer.writerow(data)

def main():
    d = {'name': 'Petr', 'surname': 'Ivanov', 'age': 21}
    d1 = {'name': 'Gleb', 'surname': 'Petrov', 'age': 31}
    d2 = {'name': 'Sergey', 'surname': 'Yakov', 'age': 45}
    l = [d, d1, d2]

    with open('plugins.csv') as file:
        fieldnames = ['name', 'link', 'rate']
        reader = csv.DictReader(file, fieldnames=fieldnames)

        for row in reader:
            print(row)


if __name__ == '__main__':
    main()