import streamlit as st
from pathlib import Path
import base64
#Main Function
st.set_page_config(page_title='Swetha Saravanan',
    page_icon='papalogo.png',
    layout="wide",
    initial_sidebar_state="expanded",)
#Image function Start
def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded
#Image function End
#Sidebar Start
def cs_sidebar():
    st.sidebar.markdown('''<img src='data:image/png;base64,{}' class='img-fluid' width=225 height=280>'''.format(img_to_bytes("papu.jpg")), unsafe_allow_html=True)
    st.sidebar.title("Swetha Saravanan")
    st.sidebar.markdown("Date of Birth : 02-05-2005")
    st.sidebar.markdown("Place : Karur")
    st.sidebar.markdown("Age : 19")
    st.sidebar.markdown('''id : [sswetha0205@gmail.com](mailto:sswetha0205@gmail.com)''', unsafe_allow_html=True)
    st.sidebar.markdown('''Phone : [+91 9360449240](tel:+919360449240)''', unsafe_allow_html=True)
    data = "logo.jpg"
    st.sidebar.download_button('My Resume', data)   
#Sidebar End
def body1():
    st.title("Myself")
    st.markdown("Hey Guys,I'm Swetha Saravanan,Currently pursuing B.Tech in the stream of Artificial Intelligence and Data Science. As a passionate learner, I focusing on enhancing my skills in Python with Data Science.I am eager to contribute my creativity skills to build efficient and user-friendly Data manipulations and other AI based applications.Connect with me to collaborate on exciting projects!!!")
def body2():
#A,B Starts
    a,b = st.columns(2)
    a.title("Education")
    a.header("High School & Grade 12")
    a.markdown("2021 - 2022")
    a.markdown("Cheran Matric.Hr.Sec.School")
    a.markdown("I have passed my higher secondary schooling with 89% marks with good communication skills")
#College    
    a.header("B.Tech & Artificial Intelligence and Data Science")
    a.markdown("2022 - 2026")
    a.markdown("M.Kumarasamy College of Engineering")
    a.markdown("I'm currently pursuing my Bachelor of Technology in great way in this institution")
    a.title("Languages")
    a.markdown("* Sourashtra - 100%")
    a.markdown("* Tamil      - 100%")
    a.markdown("* Telugu     - 40%")
    a.markdown("* English    - 80%")
#Project Translator
    b.title("Projects")
    b.header("Language Translator - Sourashtra")
    b.markdown("Completed Year : 2024")
    b.latex("Translator Application")
    b.markdown("* This is an AI based model and quick responsible")
    b.markdown("* It is a project which is very easy in translation as well as fully controlled by AI Pre-trained model")
    b.markdown("* This Project motive is to translate the other indian or foreign language to this language and it is very useful to the begineers who are intrested to learn this language")
    b.markdown("* Based on my personal thing only I have developed this project")
#Project Ayurveda
    b.header("Drug Analysis on Ayurveda For Practitioners")
    b.markdown("Completed Year : 2023 - 2024")
    b.latex("Analyisis Software for Trainers")
    b.markdown("* This is an application based project")
    b.markdown("* It helps the Practitioners who are studying Ayurveda")
    b.markdown("* This is the project based on Artificial Intelligence Models")
    b.markdown("* Based on my survey most of the people asked to make like this by their request I had made this project")
    st.markdown("---")
#A,B End
#C,D Starts
    c,d=st.columns(2)
    c.title("Technical Skills")
    c.markdown("* Python     - 80%")
    c.markdown("* C Programming     - 90%")
    c.markdown("* Java - 60%")
    c.markdown("* HTML    - 50%")
    c.markdown("* CSS   - 25%")
    c.markdown("* Django    - 40%")
    d.title("Soft Skills")
    d.markdown("* Leadership      - 100%")
    d.markdown("* Teamwork    - 80%")
    d.markdown("* Adaptability - 40%")
    d.markdown("* Time Management    - 50%")
    d.markdown("* Team Management   - 25%")
    st.markdown("---")
    st.title("Certificates")
#C,D End
#Certificate Starts
    e,f,g=st.columns(3)
    e.markdown('''<img src='data:image/png;base64,{}' class='img-fluid' width=275 height=180>'''.format(img_to_bytes("c1.png")), unsafe_allow_html=True)
    f.markdown('''<img src='data:image/png;base64,{}' class='img-fluid' width=275 height=180>'''.format(img_to_bytes("p2.png")), unsafe_allow_html=True)
    g.markdown('''<img src='data:image/png;base64,{}' class='img-fluid' width=275 height=180>'''.format(img_to_bytes("p5.png")), unsafe_allow_html=True)
    st.markdown("---")
    h,i,j=st.columns(3)
    h.markdown('''<img src='data:image/png;base64,{}' class='img-fluid' width=275 height=180>'''.format(img_to_bytes("c2.png")), unsafe_allow_html=True)
    i.markdown('''<img src='data:image/png;base64,{}' class='img-fluid' width=275 height=180>'''.format(img_to_bytes("p1.png")), unsafe_allow_html=True)
    j.markdown('''<img src='data:image/png;base64,{}' class='img-fluid' width=275 height=180>'''.format(img_to_bytes("p6.png")), unsafe_allow_html=True)
    st.markdown("---")
    k,l,m=st.columns(3)
    k.markdown('''<img src='data:image/png;base64,{}' class='img-fluid' width=275 height=180>'''.format(img_to_bytes("p3.png")), unsafe_allow_html=True)
    l.markdown('''<img src='data:image/png;base64,{}' class='img-fluid' width=275 height=180>'''.format(img_to_bytes("p4.png")), unsafe_allow_html=True)
    m.markdown('''<img src='data:image/png;base64,{}' class='img-fluid' width=275 height=180>'''.format(img_to_bytes("w1.png")), unsafe_allow_html=True)
    st.markdown("---")
    n,o,p=st.columns(3)
    n.markdown('''<img src='data:image/png;base64,{}' class='img-fluid' width=275 height=180>'''.format(img_to_bytes("w2.png")), unsafe_allow_html=True)
    st.markdown("---")
#Certificate Ends
#Contact Starts
    st.title("Contact Me")
    am,pm=st.columns(2)
    am.header("Address")
    am.markdown("29,Rajivgandhi Nagar,")
    am.markdown("Vengamedu,")
    am.markdown("Karur - 639006")
    pm.header("Social Profiles")
    pm.markdown('''LinkedIn : [Swetha Saravanan](https://www.linkedin.com/in/swetha-s-8b49012b3/)''', unsafe_allow_html=True)
    pm.markdown('''Mail Id : [sswetha0205@gmail.com](mailto:sswetha0205@gmail.com)''', unsafe_allow_html=True)
    pm.markdown('''Twitter : [sswetha0205](https://twitter.com/sswetha0205)''', unsafe_allow_html=True)
    pm.markdown('''Github : [sswethasaravanan](https://github.com/sswethasaravanan)''', unsafe_allow_html=True)
    st.markdown("---")
    with st.form(key="submit"):
        na,ma=st.columns(2)
        username = na.text_input('Name')
        password = ma.text_input('E-Mail')
        message = st.text_input('Message')
        st.form_submit_button('Hire Me')
    st.markdown("---")
#Contact Ends
    st.markdown("Developed by")
    st.title("Swetha Saravanan")
    st.markdown("All Rights Received Copyright - 2024")
cs_sidebar()
body1()
body2()