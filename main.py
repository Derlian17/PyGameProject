from PIL import Image

schem = 'image.png'
start = 5, 5
im = Image.open(schem)
w, h = im.size
pix = im.load()
size = 10, 10
position = 'center'
x, y = start
while True:
    a = input()
    if a == '>':
        x += 1
    elif a == '<':
        x -= 1
    elif a == 'v':
        y += 1
    elif a == '^':
        y -= 1
    x0 = (x - size[0] // 2) if position == 'center' else x - size[0]
    y0 = (y - size[1] // 2) if position == 'center' else y - size[1]
    x1 = (x + size[0] // 2) if position == 'center' else x
    y1 = (y + size[1] // 2) if position == 'center' else y
    f = True
    for x in range(x0, x1 + 1):
        for y in range(y0, y1 + 1):
            r, g, b = pix[x, y]
            if r / 16 > 15 and g / 16 > 15 and b / 16 > 15:
                pass
            else:
                f = False
                break
        if not f:
            break
    if not f:
        if a == '>':
            x -= 1
        elif a == '<':
            x += 1
        elif a == 'v':
            y -= 1
        elif a == '^':
            y += 1

    print(x, y)


