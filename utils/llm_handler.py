import google.generativeai as genai
# Configure Gemini API
genai.configure(api_key="AIzaSyDkKO0RbRwrfoglpzH_7yxVvfVqo3KeC_o")

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-pro")

def generate_response(messages):
    """
    Generates a response using Google's Gemini API.
    """
    # Combine all messages into a single prompt
    conversation = "\n".join([f"{msg['role']}: {msg['content']}" for msg in messages])
    
    # Define a clear system prompt
    system_prompt = (
        "You are a hiring assistant for TalentScout, a recruitment agency. "
        "Your task is to gather information from candidates and ask relevant technical questions. "
        "Follow these steps:\n"
        "1. Greet the candidate and ask for their name.\n"
        "2. Ask for their email address.\n"
        "3. Ask about their years of experience.\n"
        "4. Ask which technologies they are proficient in.\n"
        "5. Based on their tech stack, ask 2-3 technical questions.\n"
        "Keep your responses professional and concise."
    )
    full_prompt = f"{system_prompt}\n{conversation}\nAssistant:"

    # Generate response
    response = model.generate_content(full_prompt)
    return response.text