import streamlit as st

def main():
    st.title("Welcome to My Simple Website")
    
    st.header("About This Site")
    st.write("""
    This is a basic website created with Streamlit.
    It's super easy to make interactive apps in Python!
    """)
    
    st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png",
             width=200)
    
    if st.button("Click me!"):
        st.success("Thanks for clicking the button! 🎉")
    
    st.write("---")
    st.write("Made with ❤️ using Streamlit")

if __name__ == "__main__":
    main()
