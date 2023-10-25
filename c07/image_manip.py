from PIL import Image, ImageFilter


def main():
    with Image.open("still_life_desk.png") as img:
        blur_img = img.filter(ImageFilter.GaussianBlur(radius=10))
        sharp_img = img.filter(ImageFilter.UnsharpMask(percent=200))
        img.show()
        blur_img.show()
        sharp_img.show()


if __name__ == "__main__":
    main()