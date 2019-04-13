from PIL import Image
from functools import reduce
import numpy as np
import matplotlib.pyplot as plt
import time


def threshold(imageArray):
    balanceAr = []#balance array
    newAr = imageArray#複製一份imageArray 並命名為 new array 

    for eachRow in imageArray:#每row
        for eachPix in eachRow:#row中的Pixel (element)
            #print(eachPix)#試印每一橫排
            #time.sleep(3)#delay 3 seconds

            #不需要eachPix中的第四個值(alpha)
            avgNum = reduce(lambda x,y: x+y, np.uint(eachPix[:3]))/len(np.uint(eachPix[:3]))
            balanceAr.append(avgNum)
            
    #計算出整張圖的平均像素值, 所有像素值(0-255)加總/所有像素的數量
    balance = reduce(lambda x,y: x+y, balanceAr)/len(balanceAr)

    #print(f'balance: {balance}')

    for eachRow in newAr:
        for eachPix in eachRow:
            #如果「這一點」的平均像素值比總平均還大(代表「這一點」較亮)
            thisPixel = reduce(lambda x,y: x+y, np.uint(eachPix[:3]))/len(np.uint(eachPix[:3]))
            
            if reduce(lambda x,y: x+y, np.uint(eachPix[:3]))/len(np.uint(eachPix[:3])) > np.uint(balance):
                    
                #print(f'thisPixel: {thisPixel} is bigger than balance: {balance}')
                
                #「這一點」全部轉成白色
                
                eachPix[0] = 255#r
                eachPix[1] = 255#g
                eachPix[2] = 255#b
                eachPix[3] = 255#alpha
                
            else:
                #print(f'thisPixel: {thisPixel} is smaller than balance: {balance}')           
                #「這一點」全部轉成黑色
                
                eachPix[0] = 0#r
                eachPix[1] = 0#g
                eachPix[2] = 0#b
                eachPix[3] = 255#alpha
                
            #time.sleep(3)
    return newAr#將轉換完的array返回

#黑白反轉
def black2white(imageArray):
    
    for eachRow in imageArray:
        for eachPix in eachRow:
            eachPix[0] = 255 if eachPix[0]==0 else 0
            eachPix[1] = 255 if eachPix[1]==0 else 0
            eachPix[2] = 255 if eachPix[2]==0 else 0
    return imageArray
            
            

i = Image.open('images/numbers/0.1.png')
iar = np.array(i)

i2 = Image.open('images/numbers/y0.4.png')
iar2 = np.array(i2)

i3 = Image.open('images/numbers/y0.5.png')
iar3 = np.array(i3)

i4 = Image.open('images/sentdex.png')
iar4 = np.array(i4)

black2white(threshold(iar3))
threshold(iar2)

threshold(iar4)



fig = plt.figure()
#subplot2grie(shape, loc,rowspan, colspan)
ax1 = plt.subplot2grid((8,6), (0,0), rowspan=4, colspan=3)
ax2 = plt.subplot2grid((8,6), (4,0), rowspan=4, colspan=3)
ax3 = plt.subplot2grid((8,6), (0,3), rowspan=4, colspan=3)
ax4 = plt.subplot2grid((8,6), (4,3), rowspan=4, colspan=3)

ax1.imshow(iar)
ax2.imshow(iar2)
ax3.imshow(iar3)
ax4.imshow(iar4)

plt.show()


