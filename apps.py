# importing the qrcode library  
import qrcode  as  QR
import pandas as pd
# generating a QR code using the make() function  
df = pd.read_csv("rollno.csv")
rollno=df['rollno']
print(rollno)
for i in range(len(rollno)):
   code = QR.QRCode(
    box_size=5,
    border=2
)
   data = str(rollno[i])
   code.add_data(data)
   code.make(fit=True)
   img = QR.make(str(rollno[i]),fill_color='green',back_color='white')
   img.save(str(rollno[i])+"q.jpg")
   # qr_img = QR.make(str(rollno[i]))  
   # # saving the image file  
   img.save(str(rollno[i])+"q.jpg")  
   
   