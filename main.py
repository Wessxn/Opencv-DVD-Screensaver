import cv2 as cv 
import random 
import numpy as np

width, height = 900, 900
canvas = np.zeros((width, height, 3), dtype="uint8")
dvd_text_colour = (0, 255, 0)
dvd_text = "DVD"
dvd_font = cv.FONT_HERSHEY_SCRIPT_SIMPLEX
font_scale = 0.6
thickness = 2
dx, dy = 2, 2
x, y = 500, 500
score = 0
size, _ = cv.getTextSize(dvd_text, dvd_font, font_scale, thickness)
text_w, text_h = size
key = cv.waitKey(1) & 0xFF 


def change_colour():
    global dvd_text_colour 
    dvd_text_colour = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

while True: 
    canvas[:] = 0
    cv.putText(canvas, "Score: " + str(score), (450, 50), cv.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 1, cv.LINE_AA)
    cv.putText(canvas, dvd_text,(x, y), dvd_font, font_scale, dvd_text_colour, thickness, cv.LINE_AA)
    cv.imshow("DVD Bouncer", canvas)

    x += dx
    y += dy

    if x <= 0 or x + text_w >= width:  
        dx = -dx
        change_colour()

    if y <= 0 or y + text_h >= height:
        dy = -dy
        change_colour()

    if key == ord('q'):
        break

cv.destroyAllWindows()




