def return_can_move(schem, start, size, position='center', step=1):

    from PIL import Image

    # schem = 'image.png'
    # start = 5, 5
    im = Image.open(schem)
    w, h = im.size
    pix = im.load()
    # size = 10, 10
    # position = 'center'
    x, y = start
    a = input()
    if a == '>':
        x += step
    elif a == '<':
        x -= step
    elif a == 'v':
        y += step
    elif a == '^':
        y -= step
    x0 = (x - size[0] // 2) if position == 'center' else x - size[0]
    y0 = (y - size[1] // 2) if position == 'center' else y - size[1]
    x1 = (x + size[0] // 2) if position == 'center' else x
    y1 = (y + size[1] // 2) if position == 'center' else y
    f = True
    for x2 in range(max(x0, 0), min(x1 + 1, w)):
        for y2 in range(max(y0, 0), min(y1 + 1, h)):
            r, g, b = pix[x2, y2]
            if r / 16 > 15 and g / 16 > 15 and b / 16 > 15:
                pass
            else:
                f = False
                break
        if not f:
            break
    if not f:
        if a == '>':
            x -= step
        elif a == '<':
            x += step
        elif a == 'v':
            y -= step
        elif a == '^':
            y += step

    print(x, y)
    return x, y, (x, y) == start


