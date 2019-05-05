import cv2
import urllib.request as urllib
import urllib.parse as urlparse
import matplotlib.pyplot as plt

def download_image(url):
    try:
        with urllib.urlopen(url) as dlFile:
            content = dlFile.read()
            filename = urlparse.urlparse(url).path.replace('/', '') + ".png"
            file = open(filename, "wb")
            file.write(content)
            file.close
        print(url + " was saved as " + filename)
        return filename
    except Exception as e:
        print(e)

def find_face_eyes_and_show_image(fn):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    img = cv2.imread(fn)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,255),2)
        
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
