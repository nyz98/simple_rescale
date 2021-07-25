# simple_rescale
A simple rescale script that helps resize all images in directory according to distance covered in filename

## Getting started
* cd into this directory
* Start with command line: python rescale.py 'directory' 'save directory' 'scale' 'org_size'

  * directory: directory containing images to be rescaled
  * save_directory: directory to save rescaled images (default to image directory if not specified)
  * scale: pixel to centimetre scale (px/cm) (default to 68.3)
  * org_size: save original image dimensions in filename if True
