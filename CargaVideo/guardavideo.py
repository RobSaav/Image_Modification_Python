import cv2
#Captura de video#
video = cv2.VideoCapture(0)

forcg = cv2.VideoWriter_fourcc(*'DIVX')

out = cv2.VideoWriter('out.avi', forcg, 20.0, (640,480))


while (video.isOpened()):
    ret, frame = video.read()

    if ret == True:
        frame = cv2.flip(frame, 0)
        out.write(frame)
        gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('imagenGRIS', gris)
        #cv2.waitKey(0)
        #cv2.imshow('frameinvertido', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
     break

video.release()
out.release()
cv2.destroyAllWindows()
