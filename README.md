#Data Summarizer

## Objective
Summarization is basically condensing a piece of text to a shorter version.With the aim to retain key information elements and contextual meaning.Automatic text Summarization -> Producing a concise and fluent summary without any human help while preserving the meaning of the original text.

##How Data Summarization is Performed
###Extractive Based Approach 
*Identifies the important sections of the text  
*Crops out the text and stich the portions of the content with relevance of the summary score ans generates a summary 

###Data Pipline
![Untitled](https://user-images.githubusercontent.com/54850155/176252322-df443786-7795-4853-8f90-dd3f5509431e.png)

##Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to download the neccessary packages 



First Step: Make a local environment

```bash
python3 -m venv packages
source packages/bin/activate
```
Second Step: Install Important Packages from the requirement file 

```bash
pip3 install -r requirements.txt
```

##Usage 

There are two ways to use the summarizer:

First way: Using Streamlit to access the web interface use this

```bash
streamlit run app.py
```
Second Way:

- Under the articles/ folder
- Make a file with name article1.txt
- Add content in article1.txt
- Save the txt file 
- Goto terminal and run

```bash
python3 run Summarizer.py
```









