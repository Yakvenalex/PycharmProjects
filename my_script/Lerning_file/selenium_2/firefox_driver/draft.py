def follower(x):
    if '.' in x:
        if 'K' in x:
            K = '00'
            x = x.replace('K', '00')
            x = x.replace('.', '')
            return x
        elif 'M' in x:
            M = '00000'
            x = x.replace('M', '00000')
            x = x.replace('.', '')
            return x
    else:
        if 'K' in x:
            x = x.replace('K', '000')
            return x
        elif 'M' in x:
            M = '00000'
            x = x.replace('M', '000000')
            return x
    return x

a = follower('338.4K')
b = follower('338K')
c = follower('8.6M')
d = follower('6M')

print(a)
print(b)
print(c)
print(d)

