import os
import cv2
import re
import argparse
import sys


def img_resize(img_dir, save_dir, scale, og_size):
    for img in os.listdir(img_dir):
        img_path = os.path.join(img_dir, img)
        image = cv2.imread(img_path, -1)

        # Save original dimensions of image for later use
        og_width = str(image.shape[1])
        og_height = str(image.shape[0])

        # Replace _ with . to find dimensions with regular expressions
        info = img_path.replace("_", ".")
        dimensions = re.findall("\d\d\.\d\d", info)
        dim_3digits = re.findall("x\d\.\d\d", info)
        if len(dim_3digits) > 0:
            dimensions.append(dim_3digits[0][1:])
        print(dimensions)

        # Calculate new width and height and resize
        width = round(float(dimensions[0]) * 68.3)
        height = round(float(dimensions[1]) * 68.3)
        dim = (width, height)
        resized_image = cv2.resize(image, dim, interpolation=cv2.INTER_CUBIC)

        if og_size:
            img_filename = f"{img[:-4]}_{og_width}x{og_height}.png"
        else:
            img_filename = img

        save_path = os.path.join(save_dir, img_filename)
        cv2.imwrite(save_path, resized_image)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-d", "--dir", required=True, default="image_folder"
                    help="path to the image directory")
    ap.add_argument("-a", "--save_dir", type=str, default="rescaled_image_folder",
                    help="path to save rescale image directory (default to image directory)")
    ap.add_argument("-s", "--scale", type=str, default="68.3",
                    help="resize scale (px/cm)")
    ap.add_argument("-o", "--org_size", type=bool, default=True,
                    help="whether to save original size at the end of filename")

    args = vars(ap.parse_args())

    root_dir = sys.path[0]
    img_dir = os.path.join(root_dir, args["dir"])
    save_dir = os.path.join(root_dir, args["save_dir"])
    print("Process Starting...")
    print(f"{len([i for i in os.listdir(img_dir)])} number of files")
    img_resize(img_dir, save_dir, args["scale"], args["org_size"])
    print("Process Complete")
