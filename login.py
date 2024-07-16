import streamlit as st
import webbrowser

st.markdown("""
<style>
.css-nqowgj.e1ewe7hr3{
visibility:hidden;
}
.css-h5rgaw.e1g8pov61{
visibility:hidden;
}
</style>
""",unsafe_allow_html=True)
st.markdown("<h1 style='text-align:center'>Food selecty</h1>",unsafe_allow_html=True)
with st.form("Login",clear_on_submit=True):
    usr=st.text_input("Username")
    pas=st.text_input("Password",type="password")
    state=st.link_button("Login", "https://diet-recommendation-system.streamlit.app/")
    state2=st.form_submit_button()
    if state:
        if usr=="":
            st.warning("Fill the username")
        elif pas=="":
            st.warning("Don't act smart give the password")
        else:
            st.success("Redirecting...")
            webbrowser.open("https://diet-recommendation-system.streamlit.app/")
st.markdown("<p style='text-align:center'>New user <a href='http://localhost:8502/'>signup</a></p>",unsafe_allow_html=True)
