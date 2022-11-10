from Adafruit_IO import Client
from base64 import b64encode
import argparse
import random
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=True, help="video to send")
ap.add_argument("-u", "--user", required=True, help="Adafruit IO username")
ap.add_argument("-k", "--key", required=True, help="Adafruit IO Key")
ap.add_argument("-f", "--feed", required=True, help="Adafruit IO feed")
args = vars(ap.parse_args())

clientREST = Client(username=args["user"], key=args["key"])

# se um video nao foi informado, abre a webcam
if not args.get("video", False):
    camera = cv2.VideoCapture(0)
# senao, abre a referencia ao arquivo/url do video
else:
    camera = cv2.VideoCapture(args["video"])

totalFrames = camera.get(cv2.CAP_PROP_FRAME_COUNT)
randomFrameNumber = random.randint(0, totalFrames)
# set frame position
camera.set(cv2.CAP_PROP_POS_FRAMES,randomFrameNumber)
(grabbed, frame) = camera.read()

if grabbed:
    frame = imutils.resize(frame, width=200)
    cv2.imshow("Frame", frame)
    stream = b64encode(frame)
    if len(stream) <= 102400:
        clientREST.send(args["feed"], stream.decode('utf-8'))
        print("Imagem enviada com sucesso.")
    else:
        print("[ERROR] Encoded image size cannot be larger than 102400 bytes:", len(stream))