from PIL import Image

filename = "still_life_desk.png"
img = Image.open(filename)
img.show()
img.close()