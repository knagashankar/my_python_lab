#  importing opencv library
import cv2

# creating handle for video capture
# 0=default or primary cam, 1 = secondary cam and so on
cam_handle = cv2.VideoCapture(0)
    
# entering an infinite loop for continous capture
while(True):
    
    # reading from the camera handle
    return_value, img_frame = cam_handle.read()
    
    # displaying the frame in a window with window_title
    cv2.imshow("window_title", img_frame)
    
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
# cv2.destroyAllWindows()

# closes specific window
cv2.destroyWindow("window_title")
