from PIL import Image

width = 1000
height = 700
image = Image.new('RGB', (width, height), (0,156,59))

'''Drawing the losango'''
horizontal_losango = 0.83 * width
space = int((width - horizontal_losango) / 2)

a = -53/83
b = 404.2771

for x in range(space, width - space):
    for y in range(space, height - space):
        if (y >= int(-a*x +b - 638)) and (y >= int(a*x + b)) and (y <= int(a*x + b + 530)) and (y <= int(-a*x + 295.7228)):
            image.putpixel((x,y), (255,255,0))

'''Drawing the circle'''
r = height // 4
center_x, center_y = width//2, height//2

for x in range(center_x - r, center_x + r):
    for y in range(center_y - r, center_y + r):
        if (((x - center_x)**2 + (y - center_y) ** 2) <= r ** 2):
            image.putpixel((x,y), (0,39,118))

'''Drawing the white band'''
#center_x_w = width//2 - 100
#center_y_w = height
center_white = (width//2 - 100, height)
r1 = width * 4 // 10
r2 = width * 4.25 // 10

for x in range(center_x - r, center_x + r):
    for y in range(center_y - r, center_y + r):
        if (x - center_white[0])**2 + (y- center_white[1])**2 >= r1**2 and (x - center_white[0])**2 + (y- center_white[1])**2 <= r2**2 and (((x - center_x)**2 + (y - center_y) ** 2) <= r ** 2):
            image.putpixel((x,y), (255,255,255))


image.save('brazil.jpg')