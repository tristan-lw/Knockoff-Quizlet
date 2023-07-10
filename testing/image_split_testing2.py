from PIL import Image
import cv2
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

path = "C:/Users/Tristan/source/repos/Python/Knockoff Quizlet/testing/"
image = cv2.imread(path + "words.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (3,3), 0)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1] 
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
invert = 255 - opening
cv2.imwrite(path + "gray.png", gray)
cv2.imwrite(path + "blur.png", blur)
cv2.imwrite(path + "thresh.png", thresh)
cv2.imwrite(path + "opening.png", opening)
cv2.imwrite(path + "invert.png", invert)

image = invert

(h, w) = image.shape[:2]

first_part = image[0:h, 0:int(w/2)]

second_part = image[0:h, int(w/2):w]

cv2.imwrite(path + "first.png", first_part)
cv2.imwrite(path + "second.png", second_part)

data = tess.image_to_string(second_part, lang='eng')
lines = data.split('\n')
image_words = list(filter(None, lines))
print(image_words)