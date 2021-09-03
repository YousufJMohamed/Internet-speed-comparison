from flask import Flask, render_template, request
import pytesseract as tess
import numpy as np
import cv2


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def upload():
    return render_template("ima.html")

@app.route("/upload", methods=["GET", "POST"])
def upload_image():
    ima = []
    if request.method == 'POST':
        files1 = request.files['img1'].read()
        files2 = request.files['img2'].read()
        files3 = request.files['img3'].read()
        files4 = request.files['img4'].read()
        files5 = request.files['img5'].read()
        files6 = request.files['img6'].read()
        print(type(files1))

        # convert bytes to numpy array
        npimg1 = np.fromstring(files1, np.uint8)
        npimg2 = np.fromstring(files2, np.uint8)
        npimg3 = np.fromstring(files3, np.uint8)
        npimg4 = np.fromstring(files4, np.uint8)
        npimg5 = np.fromstring(files5, np.uint8)
        npimg6 = np.fromstring(files6, np.uint8)
        print(type(npimg1))

        # convert numpy array to image
        img1 = cv2.imdecode(npimg1, cv2.IMREAD_COLOR)
        img2 = cv2.imdecode(npimg2, cv2.IMREAD_COLOR)
        img3 = cv2.imdecode(npimg3, cv2.IMREAD_COLOR)
        img4 = cv2.imdecode(npimg4, cv2.IMREAD_COLOR)
        img5 = cv2.imdecode(npimg5, cv2.IMREAD_COLOR)
        img6 = cv2.imdecode(npimg6, cv2.IMREAD_COLOR)
        print(type(img1))

        #to get a exact dimensions
        face1 = img1[96:248,0:670]
        face2 = img2[96:248,0:670]
        face3 = img3[96:248,0:670]
        face4 = img4[96:248,0:670]
        face5 = img5[96:248,0:670]
        face6 = img6[96:248,0:670]

       

        gray1 = cv2.cvtColor(np.array(face1), cv2.COLOR_RGB2BGR)
        sharpen_kernel1 = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        sharpen1 = cv2.filter2D(gray1, -1, sharpen_kernel1)

        
        gray2 = cv2.cvtColor(np.array(face2), cv2.COLOR_RGB2BGR)
        sharpen_kernel2 = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        sharpen2 = cv2.filter2D(gray2, -1, sharpen_kernel2)

        gray3 = cv2.cvtColor(np.array(face3), cv2.COLOR_RGB2BGR)
        sharpen_kernel3 = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        sharpen3 = cv2.filter2D(gray3, -1, sharpen_kernel3)

        gray4 = cv2.cvtColor(np.array(face4), cv2.COLOR_RGB2BGR)
        sharpen_kernel4 = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        sharpen4 = cv2.filter2D(gray4, -1, sharpen_kernel4)

        gray5 = cv2.cvtColor(np.array(face5), cv2.COLOR_RGB2BGR)
        sharpen_kernel5 = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        sharpen5 = cv2.filter2D(gray5, -1, sharpen_kernel5)

        gray6 = cv2.cvtColor(np.array(face6), cv2.COLOR_RGB2BGR)
        sharpen_kernel6 = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        sharpen6 = cv2.filter2D(gray6, -1, sharpen_kernel6)



        text1 = tess.image_to_string(sharpen1, lang='eng')
        text2 = tess.image_to_string(sharpen2, lang='eng')
        text3 = tess.image_to_string(sharpen3, lang='eng')
        text4 = tess.image_to_string(sharpen4, lang='eng')
        text5 = tess.image_to_string(sharpen5, lang='eng')
        text6 = tess.image_to_string(sharpen6, lang='eng')

        user1 = ''.join(filter(lambda i: i.isdigit(), text1))
        user2 = ''.join(filter(lambda i: i.isdigit(), text2))
        user3 = ''.join(filter(lambda i: i.isdigit(), text3))
        user4 = ''.join(filter(lambda i: i.isdigit(), text4))
        user5 = ''.join(filter(lambda i: i.isdigit(), text5))
        user6 = ''.join(filter(lambda i: i.isdigit(), text6))

      

        result = max(user1, user2, user3, user4, user5, user6)

        # print(result)
        if result == user1:
            ima = "[IMAGE-1] has high internet speed"
        elif result == user2:
            ima = "[IMAGE-2] has high internet speed"
        elif result == user3:
            ima = "[IMAGE-3] has high internet speed"
        elif result == user4:
            ima = "[IMAGE-4] has high internet speed"
        elif result == user5:
            ima = "[IMAGE-5] has high internet speed"
        elif result == user6:
            ima = "[IMAGE-6] has high internet speed"

    return render_template("ima.html", ima=ima)

if __name__ == "__main__":
    app.run(debug=True)
