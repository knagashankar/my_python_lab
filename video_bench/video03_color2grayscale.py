#  importing opencv library
import cv2

# creating handle for video capture
# 0=default or primary cam, 1 = secondary cam and so on
cam_handle = cv2.VideoCapture(0)

# setting the resolution of video capture
# chosing lesser values to avoid lag during test
cam_handle.set(3, 320)
cam_handle.set(4, 240)
    
# entering an infinite loop for continous capture
while(True):
    
    # reading from the camera handle
    return_value, img_frame = cam_handle.read()
    
    # flipping the frame
    flip_frame = cv2.flip(img_frame,1)

    # converting the BGR frame into gray scale
    gray_frame = cv2.cvtColor(flip_frame, cv2.COLOR_BGR2GRAY)
    
    # displaying the frame in a window with window_title
    cv2.imshow("window_title1", img_frame)
    cv2.imshow("window_title2", flip_frame)
    cv2.imshow("window_title3", gray_frame)
    
    # waitKey(time_in_msec) to wait after displaying the frame,
    # Usse this to control the frame rate
    # 
    # 0xFF to check if specified key is pressed on keyboard
    # exit loop only if specified key if pressed
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

# releasing the camera handle
cam_handle.release()

# closes all open windows
cv2.destroyAllWindows()

# closes specific window
# cv2.destroyWindow("window_title")