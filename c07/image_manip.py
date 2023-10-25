from PIL import Image


def main():
    with Image.open("still_life_desk.png") as img:
        out_img = img.copy()
        out_img = out_img.convert('L')
        out_img.show()


if __name__ == "__main__":
    main()