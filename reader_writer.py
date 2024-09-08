import numpy
import os
from PIL import Image

test_image = numpy.array([
    [[255, 0, 0], [0, 255, 0], [0, 0, 255]],
    [[255, 0, 0], [0, 255, 0], [0, 0, 255]],
])

def write_meuif(pixel_data: numpy.array, filename: str) -> None:
    with open(filename, "w+b") as meuif_file:
        # Write magical bytes
        meuif_file.write(b"MEUIF")

        height, width, _ = pixel_data.shape
        file_size = (height * width * 3) + 13

        # Write file size
        meuif_file.write(file_size.to_bytes(4, "big"))

        # Write width and height
        meuif_file.write(width.to_bytes(2, "big"))
        meuif_file.write(height.to_bytes(2, "big"))

        # Write pixel data
        for i in range(height):
            for j in range(width):
                for k in range(3):
                    meuif_file.write(int(pixel_data[i][j][k]).to_bytes(1, "big"))


def read_meuif(filename: str) -> numpy.array:
    with open(filename, "r+b") as meuif_file:
        magical_bytes = meuif_file.read(5)

        if magical_bytes == b"MEUIF":
            file_size = int.from_bytes(meuif_file.read(4), "big")

            if file_size == os.path.getsize(filename):
                width = int.from_bytes(meuif_file.read(2), "big")
                height = int.from_bytes(meuif_file.read(2), "big")

                raw_pixel_data = meuif_file.read()
                formated_raw_pixel_data = [[[] for _ in range(width)] for _ in range(height)]

                current_pixel = 0
                for i in range(height):
                    for j in range(width):
                        formated_raw_pixel_data[i][j] = [raw_pixel_data[current_pixel],
                                                         raw_pixel_data[current_pixel+1],
                                                         raw_pixel_data[current_pixel+2]]
                        current_pixel += 3

                pixel_data = numpy.array(formated_raw_pixel_data).astype("uint8")
                return pixel_data

            else:
                raise Exception(
                    f"The size of the actual file does not match the one in the header of {filename}")
        else:
            raise Exception(f"The first five bytes of {filename} are not equal to MEUIF but instead are {magical_bytes}")

if __name__ == "__main__":
    image = Image.fromarray(read_meuif("3x3.meuif"), "RGB")
    image.show()
