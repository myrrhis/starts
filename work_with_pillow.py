from PIL import Image, ImageDraw
from glob import glob


def change_ext(first, second):
    result = glob(f'*.{first}')
    for i in result:
        name = i.split('.')[0]
        Image.open(i).save(f'{name}.{second}')


def draw_hello():
    im = Image.new(mode='RGB', size=(100, 100))
    draw = ImageDraw.Draw(im)
    draw.multiline_text((35, 35), 'Hello,\nworld!', (0, 0, 255))
    del draw
    im.save('test.png')


draw_hello()
change_ext('png', 'jpg')
