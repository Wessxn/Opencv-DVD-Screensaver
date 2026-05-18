import cv2 as cv 
import numpy as np

canvas = np.zeros((1000, 1000, 3), dtype="uint8")
dx, dy = 1, 1
x, y = 500, 500
score = 0
while True: 
    canvas_gray = cv.cvtColor(canvas, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(canvas_gray, x, y)
  
    canvas[:] = 0
    cv.putText(canvas, "Score: " + str(score), (500, 25), cv.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 1, cv.LINE_AA)
    cv.putText(canvas, "DVD",(x, y), cv.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.6, (0, 255, 0), 2, cv.LINE_AA)
    cv.imshow("DVD Bouncer", canvas)
    x += dx
    y += dy

    key = cv.waitKey(1) & 0xFF 

    if key == ord('q'):
        break

cv.destroyAllWindows()




