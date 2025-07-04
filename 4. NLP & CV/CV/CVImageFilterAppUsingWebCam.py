import cv2

cap = cv2.VideoCapture(0)       # Start the webcam 0 means we are using defaul laptop cam
mode = 'normal'                 # Default filter is "normal"

while True:
    returnValue, frame = cap.read()    # Read a frame from the webcam
    if not returnValue:
        break                           # If no frame is captured, exit the loop

    
    # Apply different filters based on mode
    if mode == 'gray':
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elif mode == 'blur':
        frame = cv2.GaussianBlur(frame, (7, 7), 0)
    elif mode == 'edge':
        frame = cv2.Canny(frame, 100, 200)

    # Show the filtered frame
    cv2.imshow('Image Filter App', frame)

    key = cv2.waitKey(1)            # Check which key is pressed

    # Change the filter mode based on key
    if key == ord('g'):         #ord('g') will give ASCII value here it's Output: 103
        mode = 'gray'
    elif key == ord('b'):
        mode = 'blur'
    elif key == ord('e'):
        mode = 'edge'
    elif key == ord('n'):
        mode = 'normal'
    elif key == ord('q'):
        break            # Quit the app

cap.release()            # Turn off the webcam
cv2.destroyAllWindows()  # Close the window