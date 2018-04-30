import argparse
import numpy as np
import cv2
import os

def capture_frames(nframes=int, path=str):
    
    for i in xrange(nframes):
        cap = cv2.VideoCapture(0) # video capture default source camera
        ret,frame = cap.read() # return a single frame in variable `frame`
        frame_name = 'frame' + str(i)
        frame_path = path + '/frame' + str(i) + '.png'
        print(frame_name +' '+frame_path)
        cv2.imshow(frame_name,frame) #display the captured image
        cv2.waitKey(200) # show and wait 200 ms
        cv2.imwrite(frame_path,frame) # save image
        cv2.destroyAllWindows() # close window
        cap.release()

def main():
    parser = argparse.ArgumentParser(description = 'Captures n frames and saves them to the chosen path.')
    parser.add_argument('-n', '--nframes', type=int, default=5,
                        help='Amount of frames to be captured. Default is 5')
    parser.add_argument('-p', '--path', type=str, default= os.getcwd() + '/images/',
                        help='Path where the pictures will be saved. Default to current dir')
    
    arguments = parser.parse_args()

    if not os.path.exists(arguments.path):
        os.makedirs(arguments.path)

    print(arguments.path)
    capture_frames(arguments.nframes, arguments.path)

if __name__ == '__main__':
    main()