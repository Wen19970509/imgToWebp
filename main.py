import glob
from PIL import Image

jpg = glob.glob('./raw/*.[jJ][pP][gG]')
png = glob.glob('./raw/*.[pP][nN][gG]')

print('start convert . . . ')

for i in jpg:
    print(i)
    im = Image.open(i)
    name = i.lower().split('/')[::-1][0]
    webp = name.replace('jpg', 'webp')
    im.save(f'./converted/{webp}', 'WebP', quality=40, )

for i in png:
    print(i)
    im = Image.open(i)
    name = i.lower().split('/')[::-1][0]
    webp = name.replace('png', 'webp')
    im.save(f'./converted/{webp}', 'WebP', quality=40, )
