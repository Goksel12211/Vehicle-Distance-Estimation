import cv2
import numpy as np
import time
import tkinter as tk    
from tkinter import *
from PIL import  ImageTk,Image
import math
import random



#Guı Ekranı Açılması Ve Tasarımı
root=Tk()
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))#Ekran Boyutu
root.winfo_toplevel().title("Bilgisayar Biliminde Yeni Teknolojiler")
root.configure(bg="white")#Arkaplanı Beyaz Yapar. 
Label(root,text="İki Cisim Arasındaki Mesafe Tespiti",font=("times new roman",30,"bold"),bg="white",fg="black",pady=10).pack() 

#Video Frame' in Bulunduğu Alan
f1=LabelFrame(root)
f1.pack(side="left")
L1=Label(f1)
L1.pack()


#İki Cisim Arasındaki Mesafeler Euclidean Mesafe Hesaplama Algoritması İle Çözülür.
def mesafe_hesapla(x,y,x1,y1):
    mesafe = math.isqrt(int( math.pow(math.fabs(x-x1),2))+int(math.pow(math.fabs(y-y1),2)))
    return mesafe

#Nesne Tespiti İçin Kullanılan Yolov3 weights ve config dosyalarının yüklenmesi.
yolo = cv2.dnn.readNet("yolo/yolov3.weights", "yolo/yolo3.cfg")
classes = []
with open("yolo/coco.names", "r") as f:  
    classes = [line.strip() for line in f.readlines()]
layer_names = yolo.getLayerNames()


#Çıktıların Sonucu Olan Cisimler
output_layers = [layer_names[i-1] for i in yolo.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))

# Loading camera
#cap = cv2.VideoCapture(0) # webcam icin
cap = cv2.VideoCapture("input/video5.mp4")
font = cv2.FONT_HERSHEY_PLAIN
baslangic_zamani = time.time() # FPS Ölçümü İçin Kullanılan Başlangıç Zamanı
frame_id = 0
tablo=[]
while True:
    _, frame = cap.read() # Video ' yu Framelere Bölerek Object Detection'ın Kullanımını Sağlar.
    
    for satir in tablo: # Ekranın Yenilenmesini Sağlar.
        satir.destroy()

    frame_id += 1
    height, width, channels = frame.shape

    # Object Detection İşlemi Yapılır.
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    yolo.setInput(blob) 
    outs = yolo.forward(output_layers) 
    # Framede Bulunan Objelerin Özellikleri
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5 : # Doğruluk Değerleri 0.5 ten Büyük Nesnelerin Bilgileri Tutulur.
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                #  Kutu Bilgileri Tutulur.
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.4, 0.3)

    for i in range(len(boxes)):
            if i in indexes and str(classes[class_ids[i]])=="car": # Sadece Araba Olan Nesnelerin Karşılaştırılması Yapılır.
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                color = colors[class_ids[i]]
                son_yazi = str(i)
                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                cv2.rectangle(frame, (x, y), (x + w, y + 30), color, -1)
                cv2.putText(frame, son_yazi, (x, y + 30), font, 3, (255,255,255), 3) #bulunan nesnelerin uzerinde yazan nesnenin turu ve dogruluk degeri
    
    cizilecekler = []
    toplam_genislik =0
    for i in range(len(boxes)): # Bir Araca En Yakın İki Aracın Bilgileri Alınır.
        list = []
        key = 0
        for j in range(len(boxes)):
            if i in indexes and str(classes[class_ids[i]])=="car" and i!=j:
                key=1
                x, y, w, h = boxes[i]
                x_1, y_1, w_1, h_1 = boxes[j]
                label = str(classes[class_ids[i]])
                color = colors[class_ids[i]]
                # d = İki Araç Arasındaki Mesafe
                d =  str(round(mesafe_hesapla(x+round(w/2), y+round(h/2),x_1+(round(w_1/2)),y_1+round(h_1/2))))
                # Araçların Arasındaki Mesafelerin Kıyaslanması
                if len(list)==0:
                    list.append(j)
                    toplam_genislik=toplam_genislik+w_1
                elif len(list)==1:
                    if list[0]>j:
                        temp = list[0]
                        list[0]=j
                        list.append(temp)
                        toplam_genislik=toplam_genislik+w_1
                    else:
                        list.append(j)
                        toplam_genislik=toplam_genislik+w_1
                else:
                    if list[0]>j:
                        temp = list[0]
                        list[0]=j
                        list[1]=temp
                        toplam_genislik=toplam_genislik+w_1
                    elif list[1]>j:
                        list[1]=j
                        toplam_genislik=toplam_genislik+w_1
        if key !=0:
            list.append(i)
            cizilecekler.append(list)
    # Araçların Boyutuna Göre Ortalama Mesafe Hesaplama (Ortalama Genislik 220 cm İle Denk)
    ortalama_genislik = toplam_genislik/(len(cizilecekler*2))
    for i in range(len(boxes)):
        sayi = random.randrange(1,80)
        color_1= colors[sayi]
        for j in range(len(boxes)):
            for d in cizilecekler:
                if (i == d[2])and(d[0]==j or d[1]==j) :
                    x, y, w, h = boxes[i]
                    x_1, y_1, w_1, h_1 = boxes[j]
                    label = str(classes[class_ids[i]])
                    color = colors[class_ids[i]]

                    d = round(mesafe_hesapla(x+round(w/2), y+round(h/2),x_1+(round(w_1/2)),y_1+round(h_1/2)))
                    x= x+round(w/2)
                    y= y+round(h/2)
                    x_1=x_1+round(w_1/2)
                    y_1=y_1+round(h_1/2)
                    d = int (round((220 * d)/ortalama_genislik ))
                    d = str(d)
                    if round(mesafe_hesapla(x+round(w/2), y+round(h/2),x_1+(round(w_1/2)),y_1+round(h_1/2))):
                        cv2.line(frame, (x, y), (x_1, y_1), color_1, 2)
                        cv2.putText(frame,d, (round((x+x_1)/2)+20,round((y+y_1)/2)), font, 2, color_1, 3)
                        tablosatiri=Label(root,text= "Arac1 "+ str(i) +" Arac2 :"+ str(j)+ " Uzaklik : "+str(d)+" cm",font=("times new roman",10,"bold"),fg="blue",pady=10)
                        tablo.append(tablosatiri)
                        tablosatiri.pack()
    
    # FPS Ölçümü Yapılır.
    gecen_zaman = time.time() - baslangic_zamani
    fps = frame_id / gecen_zaman
    cv2.putText(frame, "FPS: " + str(round(fps, 2)), (10, 50), font, 3, (0, 0, 0), 3)
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    #Ekrana Videonun Frame'i Atılır.
    frame=ImageTk.PhotoImage(Image.fromarray(frame).resize((1000,700)))
    L1['image']=frame
    root.update()
    
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()
root.mainloop()



    