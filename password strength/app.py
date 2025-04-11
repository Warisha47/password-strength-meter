
import streamlit as st
import re

st.set_page_config(page_title="Password Strength Meter", page_icon="🔒")

st.title("🔐 Password Strength Meter")
st.markdown("""
## Welcome to the ultimate password strength checker!☺️
Use this simple tool to check the strength of your password and get suggestions on how to make it stronger.
            We will give you helpful tips to create a **Strong Password** 🔐
""")


password=st.text_input("Enter Your Password ", type="password",help="Ensure your password is strong🔐")
if st.button("✅ Check Password Strength"):
   feedback=[]

   score = 0

# condition
   if password:
      if len(password) >= 8:
        score+=1
      else:
        feedback.append("❌Password should be atleast 8 character long")   

      if re.search(r"[A-Z]",password)and re.search(r"[a-z]",password):
        score+=1

      else:
        feedback.append("❌Password should contain both uppercase and lowercase characters")

      if re.search(r"\d",password):
        score+=1
      else:
        feedback.append("❌Password should contain atlest one digit")
      if re.search(r"[*!@#$]",password):
        score+=1       
      else:
        feedback.append("❌Password should contain atleast one special character")    
   
#    yahan par check hoga k agar score pura he to strong show hoga
      if score == 4:
        st.success("✅Your password is strong!💪 ")

      elif score == 3:
        st.info("⚠️ Your password strength is normal. It could be stronger")

      else:
        st.error("❗ Your password is weak. please make it stronger.")
# feedback
      if feedback:
        st.markdown("## Improvement Suggestions")
        for tip in feedback:
            st.write(tip)
      else:
       st.info("Please enter your password get started. ")                



                
