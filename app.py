 

import streamlit as st
import requests



st.set_page_config(page_title="Tiny House Questions", page_icon=":rabbit:",layout="wide")


# Header section

st.title("So we can help you find the best Tiny Home")
st.header("Please answer all questions" )


#Contact Form
contact_form = """
<form action="https://formsubmit.co/adutinyhouse@gmail.com" method="POST">
     <input type="text" name="name" placeholder="Your Name"required>
     <input type="email" name="email" placeholder="Your Email"required>
      <input type="text" name="city" placeholder="Your City"required>
       <input type="text" name="Phone" placeholder="Your Phone Number"required>
        <input type="text" name="budget" placeholder="Budget?"required>
         <input type="text" name="Loan" placeholder="Need Loan?(Y/N)"required>
          <input type="text" name="FICO" placeholder="FICO above 680?(Y/N)"required>
          <input type="text" name="FICO" placeholder="Downpayment Amount?"required>
          <input type="text" name="Cash" placeholder="Do you want to pay cash?"required>
          <input type="text" name="location" placeholder=" Location for Tiny"required>
           <input type="text" name="Wheels" placeholder="Tiny House on Wheels(Y/N)"required> 
           <input type="text" name="foundation" placeholder="Tiny on a foundation(Y/N)"required>
           <input type="text" name="Comments" placeholder="Anything else we need to know"required>
           <input type="hidden" name="_captcha" value="false">
           <button type="submit">Submit</button>
           
          
           
</form>
"""
left_column, right_column = st.columns(2)
with left_column:
     st.markdown(contact_form, unsafe_allow_html=True)
     with right_column:
          st.empty()
#st.write("jASJHS SJIQJ JQIJWI")
#st.write("[Learn More](https://www.farouttinyhomes.com/)")

 
