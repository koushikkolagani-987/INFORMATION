import streamlit as st
from helper import extract_text_from_pdfs, process_text


def main():
    st.set_page_config(page_title="INFORMATION")
    st.header("INFORMATION SYSTEM")

    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader(
            "Upload PDF files",
            accept_multiple_files=True,
            type=["pdf"]
        )

        if st.button("Submit & Process"):
            if not pdf_docs:
                st.warning("Please upload at least one PDF")
                return

            with st.spinner("Processing PDFs..."):
                raw_text = extract_text_from_pdfs(pdf_docs)
                result = process_text(raw_text)

            st.success("Done")
            st.subheader("Result")
            st.write(result)


if __name__ == "__main__":
    main()
