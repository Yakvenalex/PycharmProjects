def good_tel(tel):
    tel = tel.split()
    tel[0] = '7'
    tel = ''.join(tel)
    tel = tel.replace('(', '')
    tel = tel.replace(')', '')
    tel = tel.replace('-', '')
    return tel

tel = '+7 (953) 006-53-29'

print(good_tel(tel))