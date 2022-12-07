from math import sin, pi, cos
position = 0, 0
x, y = position
text = list(map(lambda a: list(a.strip('\n')), open('sheet2.txt', 'r').readlines()))
sector = 360
step = 1
view = 180
view %= 360
anchor = 'center'
start = (view - sector // 2) if anchor == 'center' else view
stop = (view + sector // 2 + sector % 2) if anchor == 'center' else view + sector
length = 3
schem = [['?' for _ in range(2 * length)] for __ in range(2 * length)]
# print(*schem, sep='\n')
for degree in range(start, stop, step):
    for ln in range(0, length):
        if degree == 180:
            degree1 = 0
        elif degree > 180:
            degree1 = 180 - degree
        else:
            degree1 = degree
        y1 = round(sin(degree1 / 180 * pi) * ln)
        x1 = round(cos(degree1 / 180 * pi) * ln)
        if degree >= 180:
            x1 = - x1
        if x1 == y1 == 0:
            schem[length][length] = 'I'
        elif len(text) < y + y1 or y + y1 < 0 or len(text[0]) < x + x1 or x + x1 < 0:
            schem[y1 + length][length + x1] = 'x'
        elif text[y+y1][x+x1] == '1':
            schem[y1+length][length+x1] = '1'
            break
        else:
            schem[y1+length][length+x1] = '0'
print(*list(map(lambda x: ''.join(x), schem)), sep='\n')