# from server import handle_request
# import numpy as np
# import imageio
# import scipy.ndimage
# import cv2



# # img = handle_request.imgName
# img = "androidFlask.jpg"
# print("Img: "+ img)


# def grayscale(rgb):
#     return np.dot(rgb[..., :3], [0.2, 0.587, 0.114])

# def dodge(front,back):
#     result = front*255/(255-back)   
#     result[result>255] = 255
#     result[back==255] = 255    
#     return result.astype('uint8')




# s = imageio.imread(img)
# print("type: ", type(s))
# g = grayscale(s)
# # abc = "jajsasdasndjn"
# i = 255 - g

# blurImg = scipy.ndimage.filters.gaussian_filter(i,sigma=10)

# sketchImg = dodge(blurImg, g)

# cv2.imwrite('1.jpg',sketchImg)