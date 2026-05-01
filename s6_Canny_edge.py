import cv2
img=cv2.imread("image.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#ده بيسهّل عمليات زي اكتشاف الحواف.
    #      الرقم اللى على الشمال اقل قيمه و الى على اليمين اعلى قيمه
    # الصورة الناتجة حواف بس
canny_edge=cv2.Canny(gray,40,55)
cv2.imshow("canny edge",canny_edge) #عرض صورة الحواف في نافذة
cv2.waitKey(0)
cv2.destroyAllWindows()
output=f"canny_edge.jpg"
cv2.imwrite(output,canny_edge)
edges=cv2.bitwise_not(canny_edge) #عكس الألوان: الابيض هيبقي اسود و الحواف تبقي سوده والخلفية بيضه
cv2.imshow("edges",edges) #عرض الصورة بعد العكس
cv2.waitKey(0)
cv2.destroyAllWindows()
output=f"edges.jpg"
cv2.imwrite(output,edges)
cv2.imwrite("palm.jpg",edges) #حفظ نفس الصورة باسم جديد "palm.jpg" (مكرر عمليًا).
palm=cv2.imread("palm.jpg")#إعادة قراءة الصورة من الملف
   # دمج صورتين
   #palm (الحواف المعكوسة)
   #img (الصورة الأصلية)
   #0.3 للحواف
   #0.7 للصورة الأصلية
   #0 قيمة جاما و هي قيمة ثابته لازم تتكتب بتعبر عن اضائة الصوره لو بقي 50 هتبقي افتح و هكذا
image=cv2.addWeighted(palm,0.3,img,0.7,0)
cv2.imshow("final",image)#عرض الصورة النهائية.
cv2.waitKey(0)
cv2.destroyAllWindows()
output=f"final.jpg"
cv2.imwrite(output,image)
