import argparse
import sys
from tiffslide import TiffSlide
from PIL import Image


def display_slide(svsfile):
    slide = TiffSlide(svsfile)

    # check the # of levels/tiffs in the slide. Usually 4 with one for thumbnail.
    dims = slide.level_dimensions
    num_levels = len(dims)
    print("Number of levels in this image are:", num_levels)
    print("Dimensions of various levels in this image are:", dims)

    # Selecting the region of the image to read and plot(pixels)
    x1, x2 = 10000, 19000
    y1, y2 = 10000, 19000

    # Display the Region of interest
    ROI_dim = dims[0]  
    ROI_img = slide.read_region((x1, x2), 0, (x2, y2), as_array=True)
    ROI_img = Image.fromarray(ROI_img[y1:y2, x1:x2, :])
    ROI_img_RGB = ROI_img.convert('RGB')
    ROI_img_RGB.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Specify the fully qualified Path of the SVS file: ')
    parser.add_argument('--filename', type=str, help='filename')

    args = parser.parse_args(sys.argv[1:])
    svsfile = args.filename

    if svsfile:
        display_slide(svsfile)
    else:
        parser.print_help()
