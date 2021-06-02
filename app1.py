import sqlite3
import streamlit as st
conn=sqlite3.connect('data.db')
c=conn.cursor()
def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')
def add_userdata(username,password):
    c.execute('INSERT INTO userstable(username,password) VALUES(?,?)',(username,password))
    conn.commit()
def login_user(username,password):
    c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
    data=c.fetchall()
    return data
def main():
    st.title("Home budget prediction")
    menu = ["Login","SignUp"]
    choice = st.sidebar.selectbox("Menu",menu)
    if choice=='Login':
        st.subheader("Login Section")
        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password",type='password')
        if st.sidebar.checkbox("Login"):
            create_usertable()
            result=login_user(username,password)
            if result:
                st.success("Logged in as {}".format(username))
            else:
                st.warning("Incorrect username/password")
    else:
        st.subheader("Create New Account")
        new_user = st.text_input("Username")
        new_password = st.text_input("Password",type='password')
        if st.button("Signup"):
            create_usertable()
            add_userdata(new_user,new_password)
            st.success("You have successfully created a valid account")
            st.info("go to login menu to login")
if __name__=='__main__':
    main()
    

              
    