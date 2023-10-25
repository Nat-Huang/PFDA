from PIL import Image, ImageFilter


def main():
    with Image.open("still_life_desk.png") as img:
        blur_img = img.filter(ImageFilter.GaussianBlur())
        img.show()
        blur_img.show()


if __name__ == "__main__":
    main()