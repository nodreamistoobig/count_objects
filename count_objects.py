import matplotlib.pyplot as plt
import numpy as np

up_mask = np.array([[1,1,0,0,1,1], [1,1,0,0,1,1], [1,1,1,1,1,1], [1,1,1,1,1,1]])
down_mask = np.array([[1,1,1,1,1,1], [1,1,1,1,1,1], [1,1,0,0,1,1], [1,1,0,0,1,1]])
right_mask = np.array([[1,1,1,1], [1,1,1,1], [1,1,0,0], [1,1,0,0], [1,1,1,1], [1,1,1,1]])
left_mask = np.array([[1,1,1,1], [1,1,1,1], [0,0,1,1], [0,0,1,1], [1,1,1,1], [1,1,1,1]])
full_hrz_mask = np.array([[1,1,1,1,1,1], [1,1,1,1,1,1], [1,1,1,1,1,1], [1,1,1,1,1,1]])
full_vrt_mask = np.array([[1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]])

def match (a, mask):
    if np.all(a==mask):
        return True
    return False

def count_objects (image):
    up = 0
    down = 0
    right = 0
    left = 0
    full_h = 0
    full_v = 0
    for y in range (2, image.shape[0] - 6):
        for x in range (2, image.shape[1] - 6):
            sub1 = image[y:y+4, x:x+6]
            if match(sub1, up_mask):
                up +=1
                print(f"up {x},{y}")
                continue
            if match(sub1, full_hrz_mask):
                full_h +=1
                print(f"fh {x},{y}")
                continue
            if match(sub1, down_mask):
                print(f"down {x},{y}")
                down +=1
                
            sub2 = image[y:y+6, x:x+4]
            if match(sub2, right_mask):
                right +=1
                print(f"right {x},{y}")
                continue
            if match(sub2, full_vrt_mask):
                full_v +=1
                print(f"fv {x},{y}")
                continue
            if match(sub2, left_mask):
                print(f"left {x},{y}")
                left +=1

    print (f"up {up}, down {down}, right {right}, left {left}, full vertical {full_v}, full horizontal {full_h}")

image = np.load("ps.npy.txt")
expended_image = np.zeros((image.shape[0]+4, image.shape[1]+4))
expended_image[2:-2,2:-2] = image

count_objects(image)

plt.imshow(expended_image)
plt.show()