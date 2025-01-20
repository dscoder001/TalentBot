from openai import OpenAI
from config import OPENAI_API_KEY, MODEL_NAME

client = OpenAI(api_key=OPENAI_API_KEY)

class ChatHandler:
    def __init__(self):
        self.current_step = "greeting"
        self.tech_questions = {
            "python": [
                "Explain the difference between lists and tuples in Python.",
                "How does Python handle memory management?",
                "What are decorators and how do you use them?"
            ],
            "javascript": [
                "Explain closure in JavaScript.",
                "How does prototypal inheritance work?",
                "Explain event bubbling and capturing."
            ],
            "react": [
                "What are React hooks?",
                "Explain virtual DOM.",
                "How do you manage state in React?"
            ]
        }

    def get_system_prompt(self):
        prompts = {
            "greeting": "You are a hiring assistant. Greet the candidate and ask for their name.",
            "name": "Ask for the candidate's email address.",
            "email": "Ask for the candidate's phone number.",
            "phone": "Ask for years of experience.",
            "experience": "Ask for the desired position.",
            "position": "Ask for current location.",
            "location": "Ask for tech stack (programming languages, frameworks, databases).",
            "tech_stack": "Generate technical questions based on their tech stack.",
            "assessment": "Thank the candidate and end the conversation."
        }
        return prompts.get(self.current_step, "")

    def process_input(self, user_input, candidate_info):
        messages = [
            {"role": "system", "content": self.get_system_prompt()},
            {"role": "user", "content": user_input}
        ]

        if self.current_step == "email" and not validate_email(user_input):
            return "Please provide a valid email address.", self.current_step
            
        if self.current_step == "phone" and not validate_phone(user_input):
            return "Please provide a valid phone number.", self.current_step

        if self.current_step == "tech_stack":
            technologies = [tech.strip().lower() for tech in user_input.split(',')]
            questions = []
            for tech in technologies:
                if tech in self.tech_questions:
                    questions.extend(self.tech_questions[tech][:2])
            if questions:
                return "\n\n".join(questions[:3]), "assessment"
            
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages
        )
        
        # Update step
        steps = ["greeting", "name", "email", "phone", "experience", "position", "location", "tech_stack", "assessment"]
        current_index = steps.index(self.current_step)
        next_step = steps[min(current_index + 1, len(steps) - 1)]
        
        return response.choices[0].message.content, next_step