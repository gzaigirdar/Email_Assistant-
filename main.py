import streamlit as st
from ollama import chat
from ollama import ChatResponse
import pyperclip
from email_llm import Email_AI
# creating a modal that expands email if clicked

llm = Email_AI()
#Model function 
@st.dialog('expand',width='medium')
def open_Modal(text):
    st.write('Full view of the email')
    st.session_state.current_text = st.text_area('Full email',value=text,height=300,key='modal_text')
    if st.button('Copy'):
        pyperclip.copy(st.session_state.current_text)
        st.success('Copied!')
# Function that takes the input and runs feeds llm and updates the email boxes 
# generating session states fot text boxes
for key in ['text1', 'text2', 'text3']:
    if key not in st.session_state:
        st.session_state[key] = ''
if 'input' not in st.session_state:
    st.session_state.input = ''
if 'option' not in st.session_state:
    st.session_state.option = '***Send***'
def get_reply():
    gen_type = st.session_state.option 
    llm_input = st.session_state.input 
    final_input = gen_type + '\n' + llm_input 
    with st.spinner('Generating the email now', width="stretch"):
        res = llm.Generate_email(final_input)
    
        st.session_state.text1 = res['Professional']
        st.session_state.text2 = res['Casual']
        st.session_state.text3 = res['Friendly']



st.set_page_config(page_title="Email assistant",page_icon="./icon.png")
st.header('Email assistant')

with st.container():
   
    st.text_input('Please provide a brief context of the email or paste the email you would like to reply to:',key='input')
    st.radio("Select reply or send ",["***Send***","***Reply***"],index=None,horizontal=True,key='option')
    if st.button('Generate',type="primary"):
        get_reply()


with st.container():
    
    col1,col2,col3 = st.columns(3)

    with col1:

        st.markdown(
        '<div style="background-color:#09212e; padding:5px; border-radius:5px;">'
        '<label style="color:white;">Professional</label></div>', unsafe_allow_html=True
        )
        st.text_area('', height=150, key='text1')
        if st.button("Open Professional",type="primary"):
        
            open_Modal(st.session_state.text1)
        

    with col2:
        st.markdown(
        '<div style="background-color:#09212e; padding:5px; border-radius:5px;">'
        '<label style="color:white;">Casual</label></div>', unsafe_allow_html=True
        )
        
        st.text_area('', height=150, key='text2')
        if st.button("Expand Casual",type="primary"):
            open_Modal(st.session_state.text2)


    with col3:
        st.markdown(
        '<div style="background-color:#09212e; padding:5px; border-radius:5px;">'
        '<label style="color:white;">Friendly</label></div>', unsafe_allow_html=True
        )
        
        text3 = st.text_area('', height=150, key='text3')
        if st.button('Expand Friendly',type="primary"):
            open_Modal(st.session_state.text3)
        
        

