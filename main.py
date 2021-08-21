import cv2

vod = cv2.VideoCapture('./img/VID_milk.mp4')

while True:
    ret, frame = vod.read()
    gpu_frame = cv2.cuda_GpuMat()

    gpu_frame.upload(frame)
    frame = cv2.cuda.resize(gpu_frame, (852,480))
    frame.dowload()
    ret,frame = vod.read()

# while True:
#     _,img = vod.read()
#     cv2.imshow('ss', img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
    