from PIL import Image

png_image = Image.open(r"C:\Users\LAPTOP\Desktop\GUI\Gui-learning\imgs\ye.jpg")

png_image.save('ye.ico')
ico_image = Image.open("ye.ico")
print("ICO Image format: ", ico_image)