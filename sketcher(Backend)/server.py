import flask
import werkzeug
import base64
import numpy as np
import imageio
import scipy.ndimage
import cv2
import math
app = flask.Flask(__name__)

def grayscale(rgb):
    return np.dot(rgb[..., :3], [0.299, 0.587, 0.114])

def dodge(front,back):
    result = front*255/(255-back)   
    result[result>255] = 255
    result[back==255] = 255    
    return result.astype('uint8')



def cv2GrayScale(img):
    s = imageio.imread(img)
    print("type: ", type(s))
    g = grayscale(s)
    # abc = "jajsasdasndjn"
    i = 255 - g

    blurImg = scipy.ndimage.filters.gaussian_filter(i,sigma=10)

    sketchImg = dodge(blurImg, g)

    cv2.imwrite('1.jpg',sketchImg)

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    imagefile = flask.request.files['image']
    filename = werkzeug.utils.secure_filename(imagefile.filename)
    print("\nReceived image File name : " + imagefile.filename)

    # imgName = imagefile.filename
    imagefile.save(filename)
    # print("\nData: " + data_uri)    

    img = imagefile.filename
    print("Img: "+ img)
    cv2GrayScale(img)
    data_uri = base64.b64encode(open(img, 'rb').read()).decode('utf-8')
    return data_uri



app.run(host="0.0.0.0", port=5000, debug=True)