# python library: mushroom-voxel-pattern-generator
# Reese Chahal, Sonia Roberts Lab and Yu Nong Khew Wesleyan Spr' 2024

#---------------------------------------------------------------------
'''
Notes

Required Prerequisites of all input image patterns:
- PNG format
- Black & white pixels only, check the image pixel array if incorrect knit pattern is produced 

Functions includes:
- printinstruct()
- mirror()
- customflip_pattern()

'''


#---------------------------------------------------------------------

'''
Import External Libraries:
'''
import numpy as np
import cv2
import matplotlib.pylab as plt
%matplotlib inline


'''
Function printinstruct(outputimg_path) 
- input: path to desired image PNG 
- output: printed knit pattern instructions for each row in PNG

'''
def printinstruct(outputimg_path):
  image2 = cv2.imread(outputimg_path)
  
  # Get image dimensions
  height, width, _ = image2.shape

  # Define functions to check if a pixel is black or white
  def is_black(pixel):
      return all(value == 0 for value in pixel)

  def is_white(pixel):
      return all(value == 255 for value in pixel)

  # intial variables
  long_column = 0
  prev_black_pixels = 0

  # Iterate over each column
  for x in range(width):
      black_pixels = 0
      for y in range(height):
          pixel = image2[y, x]
          if is_black(pixel):
              black_pixels += 1

      if black_pixels < long_column:
        if black_pixels != prev_black_pixels:
          print("Row {}: K{}, turn.".format(x+1, black_pixels))

        else: # black_pixels == prev_black_pixels:
          print("Row {}: K{}".format(x+1, black_pixels))
      else: # black_pixels > long_column:
        print("Row {}: K{}".format(x+1, black_pixels))
        long_column = black_pixels

      prev_black_pixels=black_pixels



'''
Function mirror(mirrorimage_path) 
- input: path to desired image PNG  
- output: knit pattern instructions & tranformed PNG by mirroring over x axis, and shifting 1 row over to right

Replace these variables:
input image path: '/content/half_cropped_globe.png'
output image name: 'mirror_image.png'

'''
def mirror(mirrorimage_path):
  image1 = cv2.imread('half_cropped_globe.png')

  flipped_image = cv2.flip(image1, 0)

  shifted_flipped_image = np.roll(flipped_image, 1, axis=1)

  height, width, _ = image1.shape

  combined_image = np.zeros((height * 2, width, 3), dtype=np.uint8)

  combined_image[:height, :, :] = image1
  combined_image[height:, :, :] = flipped_image
  combined_image[height:, :, :] = shifted_flipped_image

  cv2.imwrite('mirror_image.png', combined_image)

  plt.imshow(combined_image)
  plt.axis('off')
  plt.show()

  # fxn call printinstruct() by passing the new output image as argument
  printinstruct('mirror_image.png')

# input string path for input png 
imgpath2 = '/content/half_cropped_globe.png'

# fxn call mirror()
mirror(imgpath2)



'''
Function customflip_pattern(flipimage_path, num_trans_user)
- input: (path to original image PNG, user input number of flip transformations in desired output pattern)
- output: tranformed PNG by flipping over y axis a given number of times & knit pattern instructions

Replace these variables:
input image path: '/content/quad_input.png' 
output image name: 'customfilp_v3.png'
'''
def customflip_pattern(flipimage_path, num_trans_user):
  original_image = cv2.imread(flipimage_path)

  # set user input as number of transformations
  num_transformations = num_trans_user
  
  flipped_images = []

  # flip the input image across the y-axis 'num_transformations' times
  for _ in range(num_transformations):
      original_image = cv2.flip(original_image, 1)
      flipped_images.append(original_image.copy())

  # get the new image dimensions
  height = max(image.shape[0] for image in flipped_images)
  width = sum(image.shape[1] for image in flipped_images)

  # make a new output image canvas
  combined_image = np.zeros((height, width, 3), dtype=np.uint8)

  # add each image onto the new output image
  x_offset = 0
  for image in flipped_images:
      combined_image[:image.shape[0], x_offset:x_offset+image.shape[1], :] = image
      x_offset += image.shape[1]

  # save the combined image
  cv2.imwrite('customfilp_v3.png', combined_image)


  # display image output
  plt.imshow(combined_image)
  plt.axis('off')
  plt.show()

  # fxn call printinstruct() by passing new output image as argument
  printinstruct('customfilp_v3.png')



# input string path for input png 
imgpath3 = '/content/quad_input.png'

# fxn call customflip_pattern() 
customflip_pattern(imgpath3, int(input("Enter the number of times to transform the original image: ")))









