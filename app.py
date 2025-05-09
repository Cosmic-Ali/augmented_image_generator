import streamlit as st
import numpy as np
import cv2
import warnings
warnings.filterwarnings('ignore')


st.title("Augmented Image Generator")

# Transformation Functions:

def Translation(img,n=5):
    # for i in range(n):
        tx=np.random.randint(2,45)
        ty=np.random.randint(1,40)
        tm=np.array([[1,0,tx],[0,1,ty]],dtype=np.float32)
        tr_img=cv2.warpAffine(img,tm,dsize=(img.shape[1],img.shape[0]),borderMode=cv2.BORDER_REFLECT)
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
        sh_img=cv2.warpAffine(img,shm,(img.shape[1],img.shape[0]),borderMode=cv2.BORDER_REFLECT)
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

img = cv2.imread("/Users/ali/Desktop/data_science/ML/computer_vision/Apple-logo-1977.jpg")

st.file_uploader("Upload image",type="zip",accept_multiple_files=True)


with st.form(key='transformation'):

    trans = st.pills("**Select transformations**",options=["Translation","Rotation","Shearing","Cropping","Scaling"],selection_mode="multi")

    preview = st.form_submit_button("Preview")
    if preview: 

        def combined_trans(selected):
            trans_img = img
            for i in selected:
                trans_img = eval(f"{i}(trans_img)")
            return trans_img

        
        st.image(combined_trans(trans))

# with st.container():

#     trans = st.pills("Select transformations",options=["Translation","Rotation","Shearing","Cropping","Scaling"],selection_mode="multi")

#     def combined_trans(selected):
#         trans_img = img
#         for i in selected:
#             trans_img = eval(f"{i}(trans_img)")
#         return trans_img

        
#     st.image(combined_trans(trans))


if len(trans)>0:

    with st.popover("Click to view selected transformations"):
        # st.write("**Selected transformations**",)
        for n,i in enumerate(trans,start=1):
            st.write(n,i)
        st.write("(Press 'Preview' to confirm change in selection)")

    data = 0
    with st.form(key='download'):
        img_count = st.slider("Select number of images to download",1,50)
        confirm = st.form_submit_button("Confirm")

    if confirm:
        st.download_button("Download",data,"data.csv")
      

