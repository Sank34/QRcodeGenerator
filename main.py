import qrcode#importing the module
from PIL import Image
print("Welcome to the qrCode generator.")
ls = input(print("Please type here your link:"))#ls will store the link
img = qrcode.make(ls)#making the qrCode
img.save("Link.png")#saving the qrCode
print("thanks for using our generator,please see your project files for the qr code.(Link.png)")#change it if you want