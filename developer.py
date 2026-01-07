
import PyPDF2
import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore, storage


def project_developer_page():

  

    st.subheader('NBS Project Submission Evaluation')

    def initialize_firebase():
        cred = credentials.Certificate('serviceAccountKey.json')
        if not firebase_admin._apps:
            firebase_admin.initialize_app(cred, {
                'storageBucket': 'verifyx-a1164.appspot.com'  # Replace with your actual bucket name
            })
            
    # Initialize Firebase
    initialize_firebase()
    # Firestore and Storage clients
    db = firestore.client()
    bucket = storage.bucket()
    
    def extract_text_from_pdf(uploaded_file, start_page, end_page):
        if uploaded_file is None:
            return ""  # Return an empty string if no file is uploaded
        
        reader = PyPDF2.PdfReader(uploaded_file)
        num_pages = len(reader.pages)
    
        if start_page < 0 or start_page >= num_pages:
            start_page = 0
        if end_page < start_page or end_page >= num_pages:
            end_page = num_pages - 1
    
        text = ''
        for page_num in range(start_page, end_page + 1):
            page = reader.pages[page_num]
            text += page.extract_text()
    
        return text

    def upload_pdf_to_storage(pdf_file):
        pdf_file.seek(0)  # Move to the start of the file
        blob = bucket.blob(pdf_file.name)
        blob.upload_from_file(pdf_file)
        blob.make_public()  # Make the file publicly accessible
        return blob.public_url  # Return the public URL of the uploaded PDF
    pdf_file = st.file_uploader("Upload a project submission", type="pdf")
    
    if pdf_file is not None:
        start_page = 0
        end_page = 117  # Adjust as necessary
        submission_text = extract_text_from_pdf(pdf_file, start_page, end_page)
        # Upload PDF to Firebase Storage
        pdf_url = upload_pdf_to_storage(pdf_file)
        # Save the PDF URL and extracted text to Firestore
        if st.button("Upload"):
            # Add the document and store the reference
            doc_ref = db.collection('pdf_uploads').add({
                'filename': pdf_file.name,
                'text': submission_text,
                'pdf_url': pdf_url,
                'upload_time': firestore.SERVER_TIMESTAMP
            })
            doc_ref = doc_ref[1]
            # Access the document ID correctly
            st.success(f"File uploaded successfully with ID: {doc_ref.id}")  # Accessing the id
        
    
    # Rest of your code remains the same
    
    
    
    
    pdf_path = 'VCS-Standard.pdf'
    start_page = 0  # Start extracting from the first page (0-based index)
    end_page = 93    # Extract up to the third page (0-based index)
    vcs_text = extract_text_from_pdf(pdf_path, start_page, end_page)
    print(vcs_text)
    
    pdf_path = 'VCS-Methodology-Requirements.pdf'
    start_page = 0  # Start extracting from the first page (0-based index)
    end_page = 89    # Extract up to the third page (0-based index)
    methodology_text = extract_text_from_pdf(pdf_path, start_page, end_page)
    print(methodology_text)
    
    pdf_path = 'VCS-Project-Description-Template-v4.4-FINAL2.docx.pdf'
    start_page = 0  # Start extracting from the first page (0-based index)
    end_page = 34    # Extract up to the third page (0-based index)
    template_text = extract_text_from_pdf(pdf_path, start_page, end_page)
    print(template_text)
    
    # deploy a llm and use 'text' as the input.
    
    # Commented out IPython magic to ensure Python compatibility.
    # %pip install google-generativeai
    
    import pathlib
    import textwrap
    
    import google.generativeai as genai
    
    from IPython.display import display
    from IPython.display import Markdown
    
    
    def to_markdown(text):
      text = text.replace('•', '  *')
      return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
    
    
    
    GOOGLE_API_KEY="AIzaSyC7TpzrIH_3-dppWE8exqdZX3DAdE6cy8w"
    genai.configure(api_key=GOOGLE_API_KEY)
    
    for m in genai.list_models():
      if 'generateContent' in m.supported_generation_methods:
        print(m.name)
    
    #For text-only prompts, use a Gemini 1.5 model or the Gemini 1.0 Pro model:
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    
    # Commented out IPython magic to ensure Python compatibility.
    if st.button("Evaluate", 2):
    #   %%time
      response = model.generate_content("You are a project verifier officer at Verra, the leading registry for projects used to generate carbon credits. Your job is to look into project submissions from project developers who create an implement nature-based solutions in order to generate carbon credits. You go through the content of the project submissions to investigate whether the submission fits into the vcs standards, methodology requirements, and touches everything on the project description template. A verifier has to compare the submission to these 3 main criteria.  As a verifier, I want you to evaluate the project submission below based on the resources listed below. The output should be in the format of summary of the project submission, the level of adherence to the standards, what needs to be fixed, and notes for improvement for project developers. The output needs to have project-specific feedback. You can bolster your feedback with quotes from the submission or referencing numbers mentioned in the submission. Here is the project submission:" + submission_text + "Here is the vcs standards:" + vcs_text + "Here is the methodology requirement:" + methodology_text + "Here is the project description template:" + template_text)
      to_markdown(response.text)
      st.write(response.text)