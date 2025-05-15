# External libraries
import streamlit as st
import numpy as np
import cv2

#Python modules
import warnings
warnings.filterwarnings('ignore')
import os
from zipfile import ZipFile
import zlib     # for compression="zipfile.ZIP_DEFLATED"
import shutil
import gc       # for garbage collection
gc.enable()       



st.title("Augmented Image Generator")


# Transformation Functions:

def Translation(img,n=5):
    # for i in range(n):
        tx=np.random.randint(2,45)
        ty=np.random.randint(1,40)
        tm=np.array([[1,0,tx],[0,1,ty]],dtype=np.float32)
        tr_img=cv2.warpAffine(img,tm,dsize=(img.shape[1],img.shape[0]))
        return tr_img
        # save_image_and_show(trans_img)


def Rotation(img,n=5):
    # for i in range(n):
        angle=np.random.choice([90, 180, -90])
        scale=np.round(np.random.uniform(1,1.6),2)
        r_x=img.shape[0]//2
        r_y=img.shape[1]//2
        rm=cv2.getRotationMatrix2D((r_y,r_x),angle,scale)
        ro_img=cv2.warpAffine(img,rm,(img.shape[1],img.shape[0]))
        return ro_img
        # save_image_and_show(r_img)


def Scaling(img,n=5):
    # for i in range(n):
        sx=np.round(np.random.uniform(1,1.6),2)
        sy=np.round(np.random.uniform(1,1.6),2)
        tx=np.random.randint(1,16)
        ty=np.random.randint(1,12)
        sm=np.array([[sx,0,tx],[0,sy,ty]],dtype=np.float32)
        sc_img=cv2.warpAffine(img,sm,(img.shape[1],img.shape[0]))
        return sc_img
        # save_image_and_show(s_img)


def Shearing(img,n=5):
    # for i in range(n):
        sx=np.round(np.random.uniform(1,1.5),2)
        shx=np.round(np.random.uniform(0,0.4))
        tx=np.random.randint(1,15)
        shy=np.round(np.random.uniform(0,0.4))
        sy=np.round(np.random.uniform(1,1.2),2)
        ty=np.random.randint(1,20)
        shm=np.array([[sx,shx,tx],[shy,sy,ty]],dtype=np.float32)
        sh_img=cv2.warpAffine(img,shm,(img.shape[1],img.shape[0]))
        return sh_img
        # save_image_and_show(img_shear)


def Cropping(img,n=5):
    # for i in range(n):
        x_1=np.random.randint(20,60)
        y_1=np.random.randint(110,160)
        x_2=np.random.randint(20,60)
        y_2=np.random.randint(110,160)
        cr_img=img[x_1:y_1,x_2:y_2]
        return cr_img
        # save_image_and_show(img_crop)

def Flip_h(img):
    fliphor_img = cv2.flip(img, 1) 
    return fliphor_img

def Flip_v(img):
    flipver_img = cv2.flip(img, 0)
    return flipver_img


# Function for combining and applying transformations on a single image
def combined_trans(trans_types,img):
    trans_img = img
    for i in trans_types:
        trans_img = eval(f"{i}(trans_img)")
    return trans_img


# Taking Files from the User
# img = cv2.imread("/Users/ali/Desktop/data_science/ML/computer_vision/Apple-logo-1977.jpg")    #example image
files = st.file_uploader("Upload image",type=["jpg","png","zip"],accept_multiple_files=True)    
# Future Improvements: Add functionality to accept compressed zip files and then extract them.

# Reading/Converting files to cv2.image()/array 
images = []
for i,file in enumerate(files):

    # 1) converting to a 1D uint8 NumPy array
    np_arr = np.frombuffer(file.read(), dtype=np.uint8)     #file.read() is to read bytes from the UploadedFile

    # 2) decoding into an OpenCV image (BGR color by default)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    # Appending image arrays to images list
    images.append(img)

    files[i] = None     # Clearing files simultaneous to the conversion

# Deleting files from RAM
del files
# ;del file;del img;del np_arr  



with st.form(key='transformation'):

    trans_types = st.pills("**Select transformations**",options=["Translation","Rotation","Shearing","Cropping","Scaling","Flip_h","Flip_v"],selection_mode="multi")

    preview = st.form_submit_button("Preview")
    if preview:
        c1,c2 = st.columns(2)
        for i in range(2):
            with c1:
                st.image(combined_trans(trans_types,cv2.cvtColor(images[0],cv2.COLOR_BGR2RGB)))  #converting image defualt bgr to rgb because st displays rgb
            with c2:
                st.image(combined_trans(trans_types,cv2.cvtColor(images[0],cv2.COLOR_BGR2RGB)))  #converting image defualt bgr to rgb because st displays rgb
        st.info("Previewing 4 transformed images with the selected combination")

# with st.container():
#     trans = st.pills("Select transformations",options=["Translation","Rotation","Shearing","Cropping","Scaling"],selection_mode="multi")
#     def combined_trans(selected):
#         trans_img = img
#         for i in selected:
#             trans_img = eval(f"{i}(trans_img)")
#         return trans_img        
#     st.image(combined_trans(trans))


if len(trans_types)>0:

    with st.popover("Click to view selected transformations"):
        for n,i in enumerate(trans_types,start=1):
            st.write(f"{n}.{i}")
        st.write("(Press 'Preview' to confirm change in selection)")

    
    with st.form(key='download'):
        img_count = st.slider("Select number of images to download",1,50)
        confirm = st.form_submit_button("Confirm")
        
    if confirm:

        if not os.path.exists("data/augmented_images"):
            os.mkdir("data/augmented_images")
        # Creating a folder, and writing images files to it one by one

        for i,img in enumerate(images):
            for n in range(img_count):
                try:
                    cv2.imwrite(f"data/augmented_images/{i}{n}.jpg",combined_trans(trans_types,img))
                except AttributeError:  # instead of exception handling, write a condition using regex to extract only the acceptable files
                    continue

        # Zipping/archiving the augmented_images folder
        shutil.make_archive("data/augmented_images","zip",base_dir="data/augmented_images")

        with open("data/augmented_images.zip",'rb') as f:
            download_button = st.download_button("Download images",f,file_name="augmented_images.zip")

  
        os.remove("data/augmented_images.zip")
        shutil.rmtree("data/augmented_images")
        #Deleting the files from dir after user download completes




# improvements and bug fixes:

# 1. Display the total number of images that are going to be downloaded. 
#    And change the download slider text to "Select the number of augmented images per given image"
# 2. Instead of exception handling, write a condition using regex to extract only the acceptable files
# 3. Write a st.spinner to display loading animation when the images are loading
# 4. Fix the cropping function 
