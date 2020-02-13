# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 21:25:21 2018

@author: 17639
"""

from PIL import Image
im = Image.open('D:/BaiduNetdiskDownload/fict.png')
img_size = im.size
print("图片的宽度和高度分别是{}".format(img_size))

box = (539,1438.5,1617,2877)
region = im.crop(box)
region.save('D:/BaiduNetdiskDownload/fictHD1.png')
