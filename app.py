from io import StringIO
import streamlit as st 
import os
import Summarizer2 as s

def main():
    st.markdown("<h1 style='text-align: centre;'> Extractive Summary</h1>", unsafe_allow_html= True)
   # cwd = os.getcwd()

   # input_type = st.radio("Input Type:", ["URL", "Raw Text"])
    st.markdown("<h3 style = 'text-align: center;'> Input</h3>", unsafe_allow_html=True)

    col1,col2 = st.columns(2)


    
    with col1:
        with open("articles/article21.txt") as f:
            sample_text = f.read()
        text = st.text_area("", sample_text, 500)   
    result = st.button('Submit')
    if(result):
        with open("articles/article21.txt", 'w') as file:
            file.write(text)
            print(text)
        
        input_fp = "articles/article21.txt"
        print(input_fp)   
        output_fp = "outputs/article21.txt"
        s.executeForAFile(input_fp,output_fp)

        with col2:
            with open("outputs/article21.txt") as file:
                t = file.read()
         #   st.markdown("<h3 style='text-align: centre;'> Summary</h3>", unsafe_allow_html= True)
            st.text_area("", t, 500)
           # st.markdown(f"<p align= 'justify'> {t}</p>", unsafe_allow_html= True)

        
        #upload_file = st.file_uploader("Choose a File")
        #print(upload_file)

        #if upload_file is not None:
              #stringio = StringIO(upload_file.getvalue().decode("utf-8"))
              #st.write(stringio)
              #string_data = stringio.read()
              #st.write(string_data)
            
            

    
    

if __name__ == "__main__":
    main()
   
