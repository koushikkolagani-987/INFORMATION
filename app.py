# app.py
import streamlit as st




def main ():
    st.set_page_config("INFORMATION")
    st.header("INFORMATION SYSTEM")
    

    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF files here and click on the button to extract the information", accept_multiple_files=True)
        if st.button("Submit & process"):

            with st.spinner("Processing..."):
             
             
             st.success("Done")


     
if __name__ == "__main__":
    main()
