# AI-Powered "Hello World" Generator Using Groq API  

## Overview  
This project integrates **Groq's Llama 3.1-8B-Instant model** to generate a **unique and creative "Hello World" message** using AI. The goal is to demonstrate **API integration** and **gain experience with generative AI models**.  

---

## Technologies Used  
- **Python 3.x**  
- **Groq API** (Llama 3.1-8B-Instant Model)  
- **Requests Library** (For API calls)  

---

## Documentation  

### API Integration Steps  
1. **Sign Up on Groq**  
   - Visit [Groq Console](https://console.groq.com/) and create an account.  
   - Navigate to **API Keys** and generate a new API key.  

2. **Set Up Python Virtual Environment (Recommended)**  
   - Create a virtual environment (venv):  
     ```sh
     python -m venv env
     ```
   - Activate the virtual environment:  
     - **Windows:**  
       ```sh
       env\Scripts\activate
       ```
     - **Mac/Linux:**  
       ```sh
       source env/bin/activate
       ```
   - Install dependencies:  
     ```sh
     pip install -r requirements.txt
     ```

3. **Run the Application**  
   ```sh
   python main.py

# Installation & Setup Guide

## Prerequisites
Before running the project, ensure you have the following:
- Python 3.x installed (Check using `python --version` or `python3 --version`).
- An active **Groq API key** (Get it from [Groq Console](https://console.groq.com/)).

---

## **Step 1: Clone the Repository**
Run the following command to clone the project from GitHub:
```sh
git clone https://github.com/yourusername/HCI_AI.git
cd HCI_AI
```
# Set Up a Virtual Environment (Recommended)  

It is **highly recommended** to create a **virtual environment** to manage dependencies.

## Create a virtual environment  
```sh
python -m venv env
```
## Activate the virtual environment
Windows : 
```sh
env\Scripts\activate
```
Mac/Linux:
```sh
source env/bin/activate
```
## Install Dependencies
```sh
pip install -r requirements.txt
```
## Add Your Groq API Key
1. Open helloworld_ai.py.
2. Replace "YOUR_GROQ_API_KEY_HERE" with your actual Groq API key.


## Expected Output
Running the script generates a fun AI-generated “Hello World” message, such as:
```sh
"Galactic greetings, Space Cowboy! Your spaceship has landed in a dimension of infinite possibilities, where bytes are the constellations and code is the cosmic rhythm guiding the universe. Welcome to World 1.0 - where magic meets motherboard!"
```
Note : the Message will vary each time because it makes the call to Groq AI to generate a Hello World Message each time it is run.

# Documentation  

## 🛠 Code Overview  
This project integrates **Groq's Llama 3.1-8B-Instant model** to generate a **creative "Hello World" message**. The application makes an API call to Groq's AI model and retrieves a dynamically generated response.  
The Steps I took to integrate the code as the same as specified in installation guide mentioned in above.To integrate the API, I compared multiple AI Models and their ease of usability with APIs as well as pricing tier (Groq was chosen because of their free tier and ease of use ) and API Keys and I found Groq to be the most simple and also allowed access to multiple AI Models using APIs. I then followed the Groq API Guidelines and Documentation to integrate the API. 
First, I created the Groq Account and I created an API Key(Not published here for security concerns) and then proceeded to follow the guidelines mentioned in the Groq API Documentation to make the call to API and print the output.

# Reflection  

## Challenges Faced  
- **Setting up API authentication**: Ensuring the Groq API key was correctly integrated and handled securely.  
- **Understanding API response structure**: Parsing and extracting useful data from the API response.  
- **Prompt engineering**: Fine-tuning the input prompt to generate more creative and meaningful responses.  

## What I Learned  
- How to **integrate an external AI API** into a Python application.  
- The importance of **clear API documentation** when working with new services.  
- Best practices for **handling API keys** and **securing sensitive credentials**.  
- How **generative AI models** process input and create dynamic text responses.  

## Future Applications  
- Expanding this project into a **real-time AI chatbot** with interactive conversations.  
- Using AI-generated responses for **automated creative content generation** (blog writing, storytelling, etc.).  
- Experimenting with **other Groq models** and comparing them with models from OpenAI, Cohere, and Hugging Face.  
- Exploring AI-powered applications for **educational and research purposes**.  
