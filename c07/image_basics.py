from PIL import Image

filename = "still_life_desk.png"
img = Image.open(filename)
img.show()
print(img.format)
print(img.size)
print(img.mode)
print(img.info)