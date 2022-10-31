from djitellopy import Tello
import cv2, math, time

# tello = Tello()
# tello.connect()


# tello.streamon()
# frame_read = tello.get_frame_read()


def tello_takeoff():
    if key == ord('t'):
        #tello.takeoff()
        pass

def tello_land(): 

    if key == ord('l'):
       # tello.land()
        pass

cap = cv2.VideoCapture(0) #comment drone part and uncomment cap to use system default camera source
count =1

while True:

    # img = frame_read.frame
    # cv2.imshow("drone", img)

    ret ,img1= cap.read()
    cv2.imshow("drone", img1)

    key = cv2.waitKey(1) & 0xff

    if key == ord('c'):
        if count <= 30:
            cv2.imwrite("./cal_images_pc/cal_image_"+str(count)+".jpg",img1)
            print("Count",count)
            count += 1
            time.sleep(1)

        else:
            print('limit reached!')
            break

    

    #tello_takeoff()
    tello_land()

    if key == 27 or key == ord("q"): # ESC
        break
    # elif key == ord('w'):
    #     tello.move_forward(30)
    # elif key == ord('s'):
    #     tello.move_back(30)
    # elif key == ord('a'):
    #     tello.move_left(30)
    # elif key == ord('d'):
    #     tello.move_right(30)
    # elif key == ord('e'):
    #     tello.rotate_clockwise(30)
    # elif key == ord('q'):
    #     tello.rotate_counter_clockwise(30)
    # elif key == ord('r'):
    #     tello.move_up(30)
    # elif key == ord('f'):
    #     tello.move_down(30)


