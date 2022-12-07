def return_sheet(schem, sheet, step=1, wall=1, floor=0):

    from PIL import Image
    # step = 5
    # schem = 'image142.png'
    im = Image.open(schem)
    w, h = im.size
    pix = im.load()
    # sheet = 'sheet.txt'
    sheet = open(sheet, 'w')
    for y in range(0, h - step + 1, step):
        for x in range(0, w - step + 1, step):
            n = 0
            for i in range(step):
                for j in range(step):
                    r, g, b, a = pix[x+i, y+j]
                    if r / 16 > 15 and g / 16 > 15 and b / 16 > 15:
                        n += 1
            n = round(n / step**2)
            if not n:
                n = wall
            else:
                n = floor
            print(f'{n};', end='', file=sheet)
        print('', file=sheet)



