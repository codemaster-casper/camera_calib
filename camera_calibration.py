from email.mime import image
import time
import numpy as np
import cv2 as cv
import glob

cb_width = 8
cb_height = 5
sq_size = 26 #mm

# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((cb_width*cb_height,3), np.float32)
objp[:,:2] = np.mgrid[0:cb_width,0:cb_height].T.reshape(-1,2) * sq_size

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.
try:
    images = glob.glob('./cal_images_pc/*.jpg')
    print("Number of images:", len(images))
except:
    print("no images found")


#cv.waitKey(0)
for fname in images:
    img = cv.imread(fname,1)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('imag',gray)   
    

    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(gray, (cb_width,cb_height), None)

    print(ret)
    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners2)

        # Draw and display the corners
        cv.drawChessboardCorners(img, (cb_width,cb_height), corners2, ret)
        cv.imshow('img', img)
        cv.waitKey(500)
cv.destroyAllWindows()

print("objpoints",objpoints)
print("imgpoints",imgpoints)
ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

print("Calibrating Matrix:")
print(mtx)
print("Distortion:")
print(dist)

#save results
filename_mtx = "./cal_images_tello/cameraMatrix_pc.txt"
np.savetxt(filename_mtx, mtx, delimiter=",")

filename_dist = "./cal_images_tello/cameraDistortion_pc.txt"
np.savetxt(filename_dist, dist, delimiter=",")