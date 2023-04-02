from PIL import Images
import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title = "My Webpage", page_icon = ":tada:",layout = "wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    


#--------Header Section-----------#
with st.container():
    st.subheader("Hi, I am Carolene :wave:")
    st.title("A Machine Leaning enthusiast ")
    st.write("I am passionate about solving solutions for complex problems using machine learning algorithms.")



#--------Load assets-------------#
lottie = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_tr1pjkop.json")



#------what i do------#
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Who am I ?")
        st.write("##")   # page break
        st.write(
            """
            I enjoy the challenge of finding innovative solutions to real-world problems with machine learning and am always looking for ways to improve my skills in this area.

            Despite my love for technology, I also enjoy spending time in the great outdoors. 
            When it comes to food,I am an adventurous eater who loves trying out new flavors and cuisines. I have a keen palate and enjoy the process of discovering new tastes and food combinations.
            I enjoy exploring diverse interests and staying engaged in both mind and body.

            I am a cat person who love dogs!!
            """
        )

with right_column:
    st_lottie(lottie, height = 300, key = "coding")




with st.container():
    st.write("---")
    st.header("")
    st.write("##")

    image_column, text_column = st.columns(1,2)
