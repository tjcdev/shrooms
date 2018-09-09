import scripts.label_image as li
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--image", help="image to be processed")
args = parser.parse_args()

if args.image:
    img = args.image

li.predict(img)
