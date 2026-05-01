import cv2
import easyocr
img=cv2.imread("text.jpg")
    #['en'] معناها اللغة الإنجليزية.
    #gpu=False يعني هيشتغل على المعالج العادي (CPU) مش كارت الشاشة.
reader = easyocr.Reader(['en'],gpu=False)
   #هنا بيحلل الصورة ويطلع النصوص اللي فيها.
   # result عبارة عن قائمة (list)، كل عنصر فيها فيه:
   # مكان النص في الصورة (coordinates)
   # النص نفسه
   # نسبة الثقة
result = reader.readtext(img)
for text in result:
    #إحداثيات المستطيل اللي حوالين النص.
    p1=text[0][0]
    p2=text[0][2]
    #النص اللي تم التعرف عليه.
    detectedtext=text[1]
    print(detectedtext)
       #بيرسم مستطيل حوالين النص.
        # img = الصورة
        # p1 و p2 = الزوايا
        # (0,255,0) = اللون الأخضر (BGR)
        # 3 = سمك الخط
    cv2.rectangle(img,p1,p2,(0,255,0),3)
      #بيكتب النص على الصورة
       #الصوره
       #النص
       #مكان الكتابه
       #نوع الخط
       #حجم الخط
       #لون اخضر
       #سمك الخط
    cv2.putText(img,detectedtext,p1,cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
cv2.imshow("text detection",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
