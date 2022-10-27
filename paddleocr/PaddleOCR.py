# https://ithelp.ithome.com.tw/articles/10275518

from paddleocr import PaddleOCR,draw_ocr
from matplotlib import pyplot as plt 
import cv2 #opencv
import os 

# Setup model
ocr_model = PaddleOCR(lang='en',use_gpu=False) #chinese_cht ch en

img_path = os.path.join('.', '001.jpg')
# Run the ocr method on the ocr model
result = ocr_model.ocr(img_path)


f = open('output.txt')

count = 0
for res in result:
    for ress in res:
        print(ress[1][0])
    # print(res[1][0])
    # print('\n')
    # f.write(str(res))
    # f.write('\n')


# f.writelines(result)
f.close()

# with open('output.txt', 'w') as f:
#     f.write(result)