import streamlit as st

st.title("Hello ML cohort 2.0")
st.header("This is a heading")
st.subheader("This is a sub heading")
st.text("Hey eveyone please be active!")
# st.balloons()


with st.form("Registration form"):
    st.title("Registration form")
    name = st.text_input("Enter your name")
    email = st.text_input("Enter your email")
    gender = st.radio("Select your gender", ("Male", "Female", "Prefer not to say"))
    if(gender == "Male"):
        st.success("You have selected Male")
    elif(gender == "Female"):
        st.success("You have selected Female")
        st.info("We have a new policy for women")
    else:
        st.warning("Choose one gender")

    country = st.selectbox("Country", ["India", "Amaerica", "Africa", "Canada"])

    age = st.slider("Enter your age", min_value=16, max_value=55)
    st.write(age)

    submit = st.form_submit_button("Register with Codess")

# model.save("name_of_model.h5")

# model.save("name_of_the_model.sav") --binary file 

