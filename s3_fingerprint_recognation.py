import cv2
image=cv2.imread("fp.jpg")
         #تحويل الصورة من ألوان (BGR) إلى رمادي (Grayscale)
          # ده مهم لأن خوارزمية SIFT بتشتغل على الصور الرمادية
image_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
sift=cv2.SIFT_create() #SIFT = طريقة لاكتشاف النقاط المهمة في الصورة (Features)
             # detectAndCompute:
                 # بيحدد النقاط المهمة (Keypoints)
                 # وبيحسب وصف لكل نقطة (Descriptor)
                    # image_keypoints → أماكن النقاط المهمة
                    # image_descriptor → بيانات رقمية لكل نقطة (بتستخدم في المقارنة)
image_keypoints,image_descriptor=sift.detectAndCompute(image_gray,None)
sift_image=cv2.drawKeypoints(image_gray,image_keypoints,image) ## بيرسم النقاط المهمة على الصورة
imag = cv2.resize(sift_image, (800, 800))
cv2.imshow("image",imag )
cv2.imwrite("sift feature.jpg",sift_image) #حفظ الصورة الناتجة في ملف جديد
cv2.waitKey(0)
cv2.destroyAllWindows()
