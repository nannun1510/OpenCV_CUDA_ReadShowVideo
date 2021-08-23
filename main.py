import cv2
from time import sleep, time
import threading


frames={}

# while True:
#     start = time()
#     _,frame = vod.read()
#     frame = cv.resize(frame,(640,360),interpolation = cv.INTER_AREA)
#     end = time()
#     fps_label = "FPS: %.2f " % (1 / (end - start))
#     cv.putText(frame, fps_label, (0, 45), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#     cv.imshow('ss', frame)
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break


def readvid(i):
    vod = cv2.VideoCapture("./img/sea.mp4")
    while True:
        try:
            ret, frame = vod.read()
            gpu_frame = cv2.cuda_GpuMat()
            gpu_frame.upload(frame)
            img = cv2.cuda.cvtColor(gpu_frame, cv2.COLOR_BGR2BGRA)
            frames[i] = img.download()
        except:
            pass


def showvid():
    while True:
        try:
            start = time()
            frame = frames[1]
            end = time()
            fps_label = "FPS: %.2f " % (1 / (end - start))
            cv2.putText(frame, fps_label, (0, 45), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow('ss', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        except:
            pass


if __name__ == '__main__':
    load = threading.Thread(target=readvid,args=(1,))
    show = threading.Thread(target=showvid,args=())

    load.start()
    show.start()
