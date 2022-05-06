def good_number(text):
    text[0] = '7'
    text = '-'.join(text)
    text = text.split('-')
    text = ''.join(text)
    return text

x = '+7 994 014-83-32'

print(good_number(x.split()))


