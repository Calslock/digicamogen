from PIL import Image
from numpy.random import choice as rnd
import argparse

parser = argparse.ArgumentParser(description='Create digital camo pattern.')
parser.add_argument('-W', '--width', type=int, default=256, help="Width of generated image (default: 256)")
parser.add_argument('-H', '--height', type=int, default=256, help="Height of generated image (default: 256)")
parser.add_argument('-C', '--color', type=str, default="b877b4", help="Color of camo pattern in hex (default: b877b4)")
parser.add_argument('-F', '--filename', type=str, default="camo", help="Filename (default: camo)")
parser.add_argument('-P', '--prob', type=int, default=10, help="Variance in colors (higher - more variance)(default: 10)")
args = parser.parse_args()

colors = [(19, 19, 19), (230, 230, 230), tuple(int(args.color[i:i+2], 16) for i in (0, 2, 4))]
img = Image.new('RGB', (args.width,args.height), color = "white")
imlist = list(img.getdata())
size = args.width*args.height
ldpr = 0

for i in range(size):
    if i/(size/100) != ldpr:
        print('\r%s %d %%' % ("Generating:", i/(size/100)), end='\r')
    ldpr = i/(size/100)
    colorsprob = [1.0, 1.0, 1.0]
    y = i//args.width
    x = i-(y*args.width)
    r = rnd(3, 1)
    r = r[0]
    sum = 0.0
    if x == 0 and y == 0:
        imlist[i] = colors[r]
    else:
        if y == 0:
            for z in range(3):
                if colors[z] == imlist[i-1]:
                    colorsprob[z]+=args.prob
        elif x == 0:
            for z in range(3):
                if colors[z] == imlist[i-args.width]:
                    colorsprob[z]+=args.prob
        else:
            for z in range(3):
                if colors[z] == imlist[i-1]:
                    colorsprob[z]+=args.prob
                if colors[z] == imlist[i-args.width]:
                    colorsprob[z]+=args.prob
        for l in range(3):
                sum+=colorsprob[l]
        for l in range(3):
                colorsprob[l]/=sum
        clr = rnd(3, 1, p=colorsprob)
        clr = clr[0]
        imlist[i] = colors[clr]

img.putdata(imlist)
img.save(args.filename + ".png")