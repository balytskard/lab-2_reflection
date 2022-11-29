from PIL import Image, ImageDraw

img = Image.new('L', (960, 540), 255)
draw = ImageDraw.Draw(img)

with open(r"DS2.txt", "r") as file:
    for line in file:
        coordinates_list = line.split()
        i = int(coordinates_list[1])
        j = int(coordinates_list[0])
        draw.line((i, j, i + 1, j + 1))

img.show()
img.save('shown_dataset.png')
