from PIL import Image
import cv2
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

path = "C:/Users/Tristan/source/repos/Python/Knockoff Quizlet/testing/"
image = cv2.imread(path + "words.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (7,7), 0)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1] 
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,13))
#opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
#invert = 255 - opening
dilate = cv2.dilate(thresh, kernel, iterations=1)
cv2.imwrite(path + "gray.png", gray)
cv2.imwrite(path + "blur.png", blur)
cv2.imwrite(path + "thresh.png", thresh)
#cv2.imwrite(path + "opening.png", opening)
#cv2.imwrite(path + "invert.png", invert)
cv2.imwrite(path + "kernel.png", kernel)
cv2.imwrite(path + "dilate.png", dilate)

cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
cnts = sorted(cnts, key=lambda x: cv2.boundingRect(x)[0])

for c in cnts:
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(image, (x, y), (x+w, y+h), (36, 255, 12), 2)

cv2.imwrite(path + "final_image.png", image)

'''
data = tess.image_to_string(english, lang='eng')
lines = data.split('\n')
english_words = list(filter(None, lines))
print(english_words)
'''