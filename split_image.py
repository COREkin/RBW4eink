import os
import cv2 
import numpy as np

#R+B+G =White
#R^c + B^c +G^c =Black
#R^c + B + G = Red
#invert it!

def ConvertRBW(filename):
    print('create palette')
    #os.system('magick xc:red xc:black xc:white  +append palette.png')
    os.system('magick xc:"rgb(0,0,0)" xc:"rgb(255,0,0)" xc:"rgb(255,255,255)" +append palette.png')
    
    #you need to change code to your path!!!!
    picdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pic')
    #print(picdir)
    print('setfile name as ' + filename)
    path = os.path.join(picdir, str(filename)+'.png')
    #print(path)
    print('remap file') 
    
    #picture, photo etc
    os.system('magick ' + os.path.join(picdir, str(filename)+'.png') +'  -dither FloydSteinberg -define dither:diffusion-amount=66% -remap palette.png ' + os.path.join(picdir, str(filename)) +'R.png')
    #text
    #os.system('magick ' + os.path.join(picdir, str(filename)+'.png') +'  +dither -remap palette.png ' + os.path.join(picdir, str(filename)) +'R.png')

    nfilename = filename + 'R'
    npath = os.path.join(picdir, str(nfilename)+'.png')

    img = cv2.imread(npath,1)

    print('split into rbw')
    imagem = cv2.bitwise_not(img)
    b,g,r = cv2.split(img)
    be,ge,re = cv2.split(imagem)

    Black = r 
    Red = re + b + g

    img_number = 0

    for color in [Black,Red]:
        print('save'+str(img_number)+'.bmp')
        cv2.imwrite(os.path.join(picdir,str(nfilename)+str(img_number)+".bmp"),color)
        img_number+=1
    return nfilename

if __name__ == '__main__':
    filename = input('please input file name:')
    ConvertRBW(filename)
