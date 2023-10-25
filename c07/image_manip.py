from PIL import Image


def rgba_to_greyscale(pixel):
    r, g, b, a = pixel
    ave_value = (r + g + b) // 3
    return (ave_value, ave_value, ave_value, a)


def main():
    with Image.open("still_life_desk.png") as img:
        out_img = img.copy()
        for y in range(img.height):
            for x in range(img.width//2):
                pix = img.getpixel((x, y))
                out_img.putpixel((x, y), rgba_to_greyscale(pix))
        out_img.show()


if __name__ == "__main__":
    main()