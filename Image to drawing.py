import PIL.Image


ASCII_CHARS = ["@", "#", "S", "%", "?", "+", "*", ";", ":", ",", ".", ]


def resize_image(image, new_width = 100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio )
    resize_image = image.resize((new_width, new_height))
    return resize_image



def greyify(image):
    grayscale_image = image.convert("l")
    return grayscale_image



def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join(ASCII_CHARS[pixels//25] for pixel in pixels)
    return characters



def main():
    path = input("")

    try:
        image = PIL.Image.open()

    except:
        print(path, "")
