import streamlit as st
import pandas as pd
import numpy as np
arr=[]
tab1, tab2= st.tabs(["Home", "About"])

st.title("🏦LOAN PREDICTION WEBSITE📈")
st.subheader("Using Machine learning to predict your :red[loan approval status].",divider='rainbow')

st.divider()
#NAME
st.markdown("<p style='font-size:30px';>Please Enter your name below",unsafe_allow_html=True)
st.text_input("",key="name",placeholder="Name")
a= (st.session_state.name).upper()
if a:
    st.success(f"Hi {a}, welcome to our website!😇")

st.write("Do you agree to our :red[Terms]?")
expander = st.expander("See Terms and Conditions")
expander.write(" Nothing much, you just need to like the post!!🤩")



on = st.toggle("Agreed!")

if on:
    st.success("Thanks!")
    st.markdown("<p style='font-size:30px';>Enter the following necessary details",unsafe_allow_html=True)
    col1,col2,col3 = st.columns([1,1,1],gap="small")
    with col1:
        c1 = ["Male",'Female']
        option1 = st.selectbox('Gender',c1,index=None,placeholder="Select Gender")
    if option1 == "Male":
        arr.append(1)
    else:
        arr.append(0)

        
    with col2:
        c2 = ['Married','Not Married']
        option2 = st.selectbox("Marital Status",c2,index=None)
        # add_selectbox = st.sidebar.selectbox(
        # 'How would you like to be contacted?',
        # ('Email', 'Home phone', 'Mobile phone'))
    if option2 == "Married":
        arr.append(1)
    else:
        arr.append(0)

    with col3:
        c3 = [0,1,2,'3+']
        option3 = st.selectbox("No. of Dependents",c3,index=None)
        arr.append(option3)

    container1 = st.container()
    container2 = st.container()
    container3 = st.container()
    container4 = st.container()
    container5 = st.container()

    with container1:
        col4,col5= st.columns([1,1])
        with col4:
            c4 = ["Graduate",'Not Graduate']
            option4 = st.selectbox('Education',c4,index=None)
        if option4 == "Graduate":
            arr.append(1)
        else:
            arr.append(0)
            
        with col5:
            c5 = ["Yes",'No']
            option4 = st.selectbox('Self-Employed',c5,index=None,placeholder="Are you Self Employed?")
        if option4 == "Yes":
            arr.append(1)
        else:
            arr.append(0)
            
    with container2:
        col5,col6= st.columns([1,1])
        with col5:
            number1 = st.number_input("Applicant Income",placeholder="Please Enter Applicant Income")
            arr.append(number1)
        with col6:
            number2 = st.number_input("Co applicant Income",placeholder="Please Enter CoApplicant Income")
            arr.append(number2)

            
    with container3:
        col7,col8= st.columns([1,1])
        with col7:
            number3 = st.number_input(":red[Loan Amount]",placeholder="Please Enter the Loan Amount")
            arr.append(number3)
        with col8:
            number4 = st.number_input("Loan Amount Term (days)",placeholder="Please enter in days",step=1)
            arr.append(int(number4))

    with container4:
        col9,col10= st.columns([1,1])
        with col9:
            c9 = ["Rural","Semi-Urban","Urban"]
            option9 = st.selectbox('Property_Area',c9,index=None)
            
        if option9 == "Urban":
            arr.append(2)
        elif option9 == "Rural":
            arr.append(0)
        else:
            arr.append(1)
        
        
        with col10:
                c10 = [1,0]
                option10 = st.selectbox('Credit History',c10,index=None)
                arr.append(option10)
                
    with container5:
            c11 = ["Absolutely!","Maybe..","I don't think so"]
            option10 = st.selectbox('Do you think your loan will be approved💰?',c11,index=None,placeholder="What do you think?😅")
    bt= st.button("Submit",type='primary')
    



else:
    st.warning("You need to agree.")

#COLUMNS


    

    
    

    


    
    
    













