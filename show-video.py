import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the (optional) video file")
args = vars(ap.parse_args())

# se um video nao foi informado, abre a webcam
if not args.get("video", False):
    camera = cv2.VideoCapture(0)
# senao, abre a referencia ao arquivo/url do video
else:
    camera = cv2.VideoCapture(args["video"])

while True:
    # pega o atual frame
    (grabbed, frame) = camera.read()
    # se estamos vendo um vídeo e não conseguiu abrir o frame
    # então sai do loop
    if args.get("video") and not grabbed:
        break
    # redimensiona o quadro para 400 pixels de largura
    frame = imutils.resize(frame, width=600)
    # exibe o quadro
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    # se 'q' foi pressionada, para o loop
    if key == ord("q"):
        break

# libera o uso da camera e fecha a janela aberta
camera.release()
cv2.destroyAllWindows()
