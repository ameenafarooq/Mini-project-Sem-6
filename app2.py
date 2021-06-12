import streamlit as st
import pandas as pd
st.title("Home Budget Prediction")
tab=st.sidebar.radio('Select',['Home','Prediction'])
if tab=='Home':
    st.image('Home.jpg')
    st.write('Home budget....')
else:
    title='<p style="font-family:Courier; color:Blue; font-size:22px">Know Your Budget</p>'
    st.markdown(title,unsafe_allow_html=True)
    file1=st.file_uploader("Please upload an image of frontal elevation",type=["jpg"])
    file2=st.file_uploader("Please upload an image of bedroom",type=["jpg"])
    file3=st.file_uploader("Please upload an image of bathroom",type=["jpg"])
    file4=st.file_uploader("Please upload an image of kitchen",type=["jpg"])
    
    
