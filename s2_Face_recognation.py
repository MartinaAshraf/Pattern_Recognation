import cv2
from cv2 import CascadeClassifier
from cv2 import rectangle

img = cv2.imread("3.PNG")
classifier = cv2.CascadeClassifier("haarcascade_frontalface.xml")
boxes = classifier.detectMultiScale(img) # عشان تتعرف على الوجه
for box in boxes: #بنلف على كل وجه تم اكتشافه
    x,y,width,height = box #x, y → بداية المستطيل (أعلى شمال)width, height → العرض والارتفاع
    x2,y2 = x + width,y + height #بنحسب نهاية المستطيل (أسفل يمين)
    #(x,y) → بداية المستطيل
    # (x2,y2) → النهاية
    # (0,255,0) → اللون أخضر
    # 3 → سمك الخط
    rectangle(img,(x,y),(x2,y2),(0,255,0),3)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()# يقفل كل النوافذ اللى قبله
