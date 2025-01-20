# TalentScout Hiring Assistant Chatbot

Welcome to the **TalentScout Hiring Assistant Chatbot**! This chatbot is designed to assist in the initial screening of candidates for technology roles. It gathers essential information and asks relevant technical questions based on the candidate's declared tech stack.

---

## **Features**
- **Greeting**: The chatbot greets candidates and explains its purpose.
- **Information Gathering**: Collects candidate details such as name, email, years of experience, and tech stack.
- **Technical Questions**: Generates tailored technical questions based on the candidate's tech stack.
- **Context Handling**: Maintains the flow of conversation for a seamless experience.
- **Fallback Mechanism**: Handles unexpected inputs gracefully.

---

## **Example Conversation**
Here’s an example of how the chatbot interacts with a candidate:

![Screenshot](Screenshot%20(128).png)

```markdown

Getting Started
Prerequisites
Python 3.8 or higher

Streamlit (pip install streamlit)

Google Generative AI SDK (pip install google-generativeai)

Installation
Clone the repository:

bash
Copy
git clone https://github.com/your-username/talent-scout-chatbot.git
cd talent-scout-chatbot
Install the required dependencies:

bash
Copy
pip install -r requirements.txt
Set up your Google Gemini API key:

Create a .env file in the root directory.

Add your API key:

env
Copy
GEMINI_API_KEY=your_api_key_here
Running the Chatbot
Start the Streamlit app:

bash
Copy
streamlit run app.py
Open your browser and navigate to http://localhost:8501.

File Structure
Copy
talent-scout-chatbot/
│
├── app.py                  # Main Streamlit application
├── requirements.txt        # List of Python dependencies
├── README.md               # Project documentation
├── .env                    # Environment variables (e.g., API keys)
└── utils/                  # Utility functions
    ├── __init__.py         # Empty file to make utils a package
    ├── llm_handler.py      # Handles LLM interactions
    └── data_handler.py     # Simulates data storage (optional)
Technologies Used
Streamlit: For the frontend interface.

Google Gemini API: For generating responses and technical questions.

Python: Backend logic and integration.

Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.

Create a new branch (git checkout -b feature/YourFeatureName).

Commit your changes (git commit -m 'Add some feature').

Push to the branch (git push origin feature/YourFeatureName).

Open a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For questions or feedback, please contact:

Name: Dhiman Saha

Email: Dhiman.s@gmail.com

Copy

---
