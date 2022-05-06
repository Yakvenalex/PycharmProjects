from bs4 import BeautifulSoup

def get_copyr(tag):
    whois = tag.find('div', id='wwhois').text.strip()
    if 'Copywriter' in whois:
        return tag
    else:
        return None


def main():
    file = open('index.html').read()
    soup = BeautifulSoup(file, 'lxml')
    persons = soup.find_all('div', class_='row')
    print(persons)

    copirs = []

    for person in persons

    # row = soup.find_all('div', {'class': 'row'})
    #
    # alena = soup.find('div', text='Alena').find_parent(class_=)
    # print(alena)



if __name__ == '__main__':
    main()