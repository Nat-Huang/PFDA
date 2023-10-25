from PIL import Image


def main():
    with Image.open("still_life_desk.png") as img:
        out_img = img.resize((img.width//10, img.height//10))
        out_img.save("thumbnail.jpg")


if __name__ == "__main__":
    main()