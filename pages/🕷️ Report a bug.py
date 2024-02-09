import streamlit as st

def bug_report():
    st.title("Bug Reporting")

    st.write(
        "If you encountered a bug while using our app, please provide details "
        "about the issue below. Your feedback helps us improve our app!"
    )

    bug_description = st.text_area("Describe the bug in detail:")
    user_email = st.text_input("Your email (optional):")

    attachment = st.file_uploader("Attach screenshots or files (optional):", type=["png", "jpg", "jpeg", "pdf", "txt"])

    if st.button("Submit Bug Report"):
        st.success("Bug report submitted successfully! Thank you for your feedback.")

if __name__ == "__main__":
    bug_report()
