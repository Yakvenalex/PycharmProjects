import requests

def get_html(url):
    r = requests.get(url)
    return r.text




def main():
    url = 'https://www.youtube.com/c/coolpropaganda/videos'
    print(get_html(url))
if __name__ == '__main__':
    main()