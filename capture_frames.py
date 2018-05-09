import argparse
import numpy as np
import cv2
import os
from time import sleep

def capture_frames(nframes=int, path=str):
    gst = "nvcamerasrc ! video/x-raw(memory:NVMM), width=(int)1280, " + \
          "height=(int)720,format=(string)I420, framerate=(fraction)24/1 ! " + \
          " nvvidconv flip-method=4 ! video/x-raw, format=(string)BGRx ! " + \
          " videoconvert ! video/x-raw, format=(string)BGR ! appsink"
    cap = cv2.VideoCapture(gst)

    print("Setting up camera...")

    # Sleep is because the camera takes some time to adapt itself to the light.
    sleep(1)
    print("Capturing images.")

    cv2.namedWindow('tx1Cam')
    for i in xrange(nframes):
        ret,frame = cap.read() # return a single frame in variable `frame`
        frame_name = 'frame' + str(i)
        frame_path = path + '/frame' + str(i) + '.png'
        print(frame_name + ' ' + frame_path)
        #cv2.imshow(frame_name, frame) #display the captured image
        cv2.imshow('tx1Cam', frame) #display the captured image
        cv2.waitKey(200) # show and wait 200 ms
        cv2.imwrite(frame_path, frame) # save image

    cv2.destroyAllWindows() # close window

    cap.release()

def main():
    parser = argparse.ArgumentParser(description = 'Captures n frames and saves' + \
                                    ' them to the chosen path.')
    parser.add_argument('-n', '--nframes', type=int, default=5,
                        help='Amount of frames to be captured. Default is 5 frames.')
    parser.add_argument('-p', '--path', type=str, default= os.getcwd() + '/images/',
                        help='Path where the pictures will be saved. Default' + \
                        ' to current directory.')
    
    arguments = parser.parse_args()

    if not os.path.exists(arguments.path):
        os.makedirs(arguments.path)

    print(arguments.path)
    capture_frames(arguments.nframes, arguments.path)

if __name__ == '__main__':
    main()
