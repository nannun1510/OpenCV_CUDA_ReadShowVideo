import cv2 as cv
from time import sleep, time


vod = cv.VideoCapture('./img/sea.mp4')

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


ret, frame = vod.read()
scale = 0.5
gpu_frame = cv.cuda_GpuMat()

while ret:
    start = time()
    gpu_frame.upload(frame)

    resized = cv.cuda.resize(gpu_frame, (int(1280 * scale), int(720 * scale)))
    resized = resized.download()

    end = time()
    fps_label = "FPS: %.2f " % (1 / (end - start))
    cv.putText(resized, fps_label, (0, 45), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv.imshow('ss', resized)


    if cv.waitKey(1) & 0xFF == ord('q'):
        break

    ret, frame = vod.read()

vod.release()
cv.destroyAllWindows()

    