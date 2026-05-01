import speech_recognition
reco = speech_recognition.Recognizer()
      # with بتضمن إنه يفتح ويقفل الميكروفون بشكل آمن
      # ,source هو المتغير اللي بيمثل الميكروفون
      #هنا بنستخدم الميكروفون كمصدر للصوت.
with speech_recognition.Microphone() as source:
    print("Say something!.....")
    #بيظبط حساسية الميكروفون حسب الضوضاء اللي حواليك.
    #duration=1 يعني بياخد ثانيه يقيس البيئة اللى حواليك
    reco.adjust_for_ambient_noise(source,duration=1)
    my_audio=reco.listen(source) #الصوت بيتخزن في my_audio.
    my_text=reco.recognize_google(my_audio) #هنا بيحول الصوت لنص باستخدام خدمة Google.محتاجة نت
    print(my_text)
