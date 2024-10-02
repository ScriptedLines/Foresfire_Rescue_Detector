import cv2 as cv
import numpy as np
import os
main_folder="D:\\Python Projects\\open CV\\UAS Project\\Images"
img_list=os.listdir(main_folder)

n_houses=[]
priority_houses=[]
priority_ratio=[]
img_list.sort(key=lambda x: int(x.split('.')[0]))
img_list_copy=img_list.copy()


for img in img_list:
    img_path=os.path.join(main_folder,img)
    img_read=cv.imread(img_path)
    if img_read is None:
        continue
    hsv_img=cv.cvtColor(img_read,cv.COLOR_BGR2HSV)
    lower_green = np.array([35,78,0])   
    upper_green = np.array([85,255,184]) 

    lower_brown = np.array([0,0,0])  
    upper_brown = np.array([22,255,94]) 
    green_mask=cv.inRange(hsv_img,lower_green,upper_green)
    solid_yellow=np.zeros((int(green_mask.shape[0]),int(green_mask.shape[1]),3),dtype=np.uint8)
    solid_yellow[:]=(0,255,255)

    green_img=cv.bitwise_and(solid_yellow,solid_yellow,mask=green_mask)
    # green_bgr=cv.cvtColor(green_mask,cv.COLOR_GRAY2BGR)
    g_contours,hie=cv.findContours(green_mask,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    cv.drawContours(green_mask,g_contours,-1,(255,255,255),-1)
    


    brown_mask=cv.inRange(hsv_img,lower_brown,upper_brown)
    solid_cyan=np.zeros((int(brown_mask.shape[0]),int(brown_mask.shape[1]),3),dtype=np.uint8)
    solid_cyan[:]=(255,255,0)

    brown_img=cv.bitwise_and(solid_cyan,solid_cyan,mask=brown_mask)
    br_contours,hie=cv.findContours(brown_mask,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    cv.drawContours(brown_mask,br_contours,-1,(255,255,255),-1)

    land_img=cv.bitwise_or(green_img,brown_img)

    lower_red=np.array([0,121,71])
    upper_red=np.array([9,255,255])
    red_mask=cv.inRange(hsv_img,lower_red,upper_red)
    red_bgr=cv.cvtColor(red_mask,cv.COLOR_GRAY2BGR)
    r_contours,hie=cv.findContours(red_mask,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    cv.drawContours(red_bgr,r_contours,-1,(0,0,255),-1)

    lower_blue=np.array([95,231,0])
    upper_blue=np.array([161,255,255])
    blue_mask=cv.inRange(hsv_img,lower_blue,upper_blue)
    blue_bgr=cv.cvtColor(blue_mask,cv.COLOR_GRAY2BGR)
    bl_contours,hie=cv.findContours(blue_mask,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    cv.drawContours(blue_bgr,bl_contours,-1,(255,0,0),-1)

    house_img=cv.bitwise_or(blue_bgr,red_bgr)

    green_red=cv.bitwise_and(green_mask,red_mask)
    green_blue=cv.bitwise_and(green_mask,blue_mask)

    brown_red=cv.bitwise_and(brown_mask,red_mask)
    brown_blue=cv.bitwise_and(brown_mask,blue_mask)


    # green_red_bgr=cv.bitwise_and(green_bgr,red_bgr)
    # green_blue_bgr=cv.bitwise_and(green_bgr,blue_bgr)

    # brown_red_bgr=cv.bitwise_and(brown_bgr,red_bgr)
    # brown_blue_bgr=cv.bitwise_and(brown_bgr,blue_bgr)

    pb=2
    pr=1
    blue_house_green=0
    red_house_green=0
    blue_house_brown=0
    red_house_brown=0

    contour_green_red,hie=cv.findContours(green_red,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    for x in contour_green_red:
        if cv.arcLength(x,True)>80 and cv.arcLength(x,True)<300:
            red_house_green+=1

    contour_green_blue,hie=cv.findContours(green_blue,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    for x in contour_green_blue:
        if cv.arcLength(x,True)>80 and cv.arcLength(x,True)<300:
            blue_house_green+=1
    

    contour_brown_red,hie=cv.findContours(brown_red,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    for x in contour_brown_red:
        if cv.arcLength(x,True)>80 and cv.arcLength(x,True)<300:
            red_house_brown+=1

    contour_brown_blue,hie=cv.findContours(brown_blue,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    for x in contour_brown_blue:
        if cv.arcLength(x,True)>80 and cv.arcLength(x,True)<300:
            blue_house_brown+=1

    n_house=[]
    n_house.append(blue_house_brown+red_house_brown)
    n_house.append(blue_house_green+red_house_green)
    n_houses.append(n_house)

    priority_house=[]
    priority_house.append(((blue_house_brown)*pb)+((red_house_brown)*pr))
    priority_house.append(((blue_house_green)*pb)+((red_house_green)*pr))
    priority_houses.append(priority_house)

    priority_ratio_temp=((blue_house_brown+blue_house_green)*pb)/((red_house_brown+red_house_green)/pr)
    priority_ratio.append(priority_ratio_temp)


    final_img=cv.bitwise_or(land_img,house_img)
 

    cv.imshow("gevedve",final_img)

    cv.waitKey(0)


print("The list of number of house in burnt grass and no.of hosues in green grass:\n",n_houses)
print("The total priority of houses on the burnt grass (Pb) and the total priority of houses on the green grass (Pg):\n",priority_houses)
print("A rescue ratio of priority Pr where Pr = Pb / Pg:\n",priority_ratio)

sorted_img=[]
priority_ratio_copy=priority_ratio.copy()

sorted_priority_ratio=priority_ratio.copy()
sorted_priority_ratio.sort(reverse=True)

for x in sorted_priority_ratio:

    index=priority_ratio_copy.index(x)
   
    sorted_img.append(img_list_copy[index])
    img_list_copy.pop(index)
    priority_ratio_copy.pop(index)
print("A list of the names of the input images , arranges in descending order of their rescue ratio:\n",sorted_img)









    # color_greeen_mask=np.zeros((int(green_mask.shape[0]),int(green_mask.shape[1]),3),dtype=np.uint8)
    # color_greeen_mask[:]=(255,255,0)
    # final_green=cv.bitwise_and(color_greeen_mask,color_greeen_mask,mask=green_mask)

    # color_brown_mask=np.zeros((int(green_mask.shape[0]),int(green_mask.shape[1]),3),dtype=np.uint8)
    # color_brown_mask[:]=(0,255,255)
    # final_brown=cv.bitwise_and(color_brown_mask,color_brown_mask,mask=brown_mask)
    # final_img=cv.bitwise_or(final_brown,final_green)
    # gray_img=cv.cvtColor(img_read,cv.COLOR_BGR2GRAY)
    # blur_img=cv.GaussianBlur(gray_img,(5,5),cv.BORDER_DEFAULT)
    # _,thresh=cv.threshold(blur_img,70,250,cv.THRESH_BINARY)
    # canny_img=cv.Canny(gray_img,200,220)
    # contours,hie=cv.findContours(gray_img,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
    # cv.drawContours(img_read,contours,-1,(180,220,59),5)
    # cv.imshow("fcnfc",img_read)
    # cv.waitKey(0)
    # new_hie=np.delete(hie,0,axis=0)
    # print(hie)
    # print(new_hie)
    # for i,contour in enumerate(contours):
    #     if i==0:
    #         continue
    #     if new_hie[i-1][2]!=-1:
    #         print("land")
        


