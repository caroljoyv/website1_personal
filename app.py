import streamlit as st


st.set_page_config(page_title = "My Webpage", page_icon = ":tada:",layout = "wide")


#--------Header Section-----------#
with st.container():
    st.subheader("Hi, I am Carolene :wave:")
    st.title("A Machine Leaning enthusiast ")
    st.write("I am passionate about solving solutions for complex problems using machine learning algorithms.")




#------what i do------#

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("Who am I ?")
        st.write("##")   # page break
        st.write(
            """
            I enjoy the challenge of finding innovative solutions to real-world problems and are always looking for ways to improve your skills in this area.

            Despite my love for technology, I also enjoy spending time in the great outdoors. 
            When it comes to food,I am an adventurous eater who loves trying out new flavors and cuisines. I have a keen palate and enjoy the process of discovering new tastes and food combinations.
            I enjoy exploring diverse interests and staying engaged in both mind and body.
            """
        )


