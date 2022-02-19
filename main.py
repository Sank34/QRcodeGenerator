import qrcode  # importing the module
try:
  print("Welcome to the qrCode generator.\nRemember that you can put also text,not just links.")
  ls = input("Please type here your link or message:")  # var ls will store the link
  print("Your link/message:" + ls)
  img = qrcode.make(ls)  # making the qrCode
  img.save("Link.png")  # saving the qrCode
  print("thanks for using our generator,please see your project files for the QR code.(Link.png)")  # final message
# if an error is detected
except:
    print("An unknown error ocurred during processing your QRcode,plese contact support.")

