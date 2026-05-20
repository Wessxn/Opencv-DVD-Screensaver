import cv2 as cv 
import random 
import numpy as np
import os.path

width, height = 900, 900
canvas = np.zeros((width, height, 3), dtype="uint8")
dvd_text_colour = (0, 255, 0)
dvd_text = "DVD"
dvd_font = cv.FONT_HERSHEY_SCRIPT_SIMPLEX
font_scale = 0.6
thickness = 2
dx, dy = random.choice([-5, 5]), random.choice([-5, 5])
x, y = 500, 500
score = 0
size, _ = cv.getTextSize(dvd_text, dvd_font, font_scale, thickness)
text_w, text_h = size
highscore_file = r"C:\Users\Navi\Documents\highscore.txt"

def is_corner_hit(x, y, text_w, text_h, width, height):
    corners = [
        (0, 0), 
        (width - text_w, 0),  
        (0, height - text_h),  
        (width - text_w, height - text_h)  
    ]
    for cx, cy in corners:
        if abs(x - cx) <= 1 and abs(y - cy) <= 1:
            return True
    return False

if not os.path.isfile(highscore_file):
    with open(highscore_file, "w") as f:
        f.write("0")

def change_colour():
    global dvd_text_colour 
    dvd_text_colour = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

def save_highscore(highscore):
    with open(highscore_file, "w") as f: 
        f.write(str(highscore))

while True: 
    canvas[:] = 0
    key = cv.waitKey(1) & 0xFF
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

    if is_corner_hit(x, y, text_w, text_h, width, height):
        score += 1

    if key == ord('q'):
        with open(r"C:\Users\Navi\Documents\highscore.txt", "r") as f: 
            highscore = int(f.read())
            if highscore < score:
                save_highscore(score)
        break


cv.destroyAllWindows()




