import cv2
img=cv2.imread("image.jpg")
cv2.imshow('image',img)  #'image' هو اسم النافذة img هي الصورة اللي عايزين نعرضها
cv2.waitKey(0) #لرقم 0 معناه "استنى للأبد لحد ما المستخدم يضغط زر"
