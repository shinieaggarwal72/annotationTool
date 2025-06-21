import os
import cv2


imagefol="/home/shinie/Downloads/annotationimagesucs547"
annotationfol="/home/shinie/annotation"

if not os.path.exists(annotationfol): 
    os.makedirs(annotationfol)


imlist=os.listdir(imagefol) #imlist will have all the imagenames as a list

font = cv2.FONT_HERSHEY_SIMPLEX 
fontScale = 1
color = (0, 0, 255) 
thickness = 2

for im in imlist:
    img=cv2.imread(os.path.join(imagefol,im))  #img is a 3d array containing the RGB image
    # no. of bits for the image = rows*cols*3*8
    # rgb 2 gray is not equally weighted
    (r,c,ch)=img.shape

    org = (00, 20) 
    img = cv2.putText(img, "next", org, font, fontScale,  color, thickness, cv2.LINE_AA)
    img = cv2.rectangle(img, (0, 0), (100, 40), color, thickness)

    org = (500, 20) 
    img = cv2.putText(img, "car", org, font, fontScale,  color, thickness, cv2.LINE_AA)
    img = cv2.rectangle(img, (500, 0), (600, 40), color, thickness)


    org = (1000, 20) 
    img = cv2.putText(img, "person", org, font, fontScale,  color, thickness, cv2.LINE_AA)
    img = cv2.rectangle(img, (1000, 0), (1100, 40), color, thickness)


    frame= im[:-4]
    dst_txt =  frame + '.txt'

    with open(os.path.join(annotationfol, dst_txt), 'a') as f:

        while(1):
            r = cv2.selectROI(img) #returns x0 y0 width height

            if r[0]< 50 and r[1] < 50:  
                break
            
            
            r1 = cv2.selectROI(img) #returns x0 y0 width height
            s = ""

            if r1[0]>500 and r1[0] < 600 and r1[1]> 0 and r1[1] < 40:  
                s="car"  

            if r1[0]> 1000 and r1[0] < 1100 and r1[1]> 0 and r1[1] < 40:  
                s="person" 
            # boxess=[]

            # boxess=[r[0],r[1],r[0] + r[2], r[1] + r[3]]
            # f.write('{} {} {} {}'.format(*boxess)+'\n')
            line= s + " " + str(r[0]) + " " + str(r[1]) + " " + str(r[2]) + " " + str(r[3]) + "\n"
            f.write(line)


    f.close()




