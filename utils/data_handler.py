candidate_data = {}

def save_candidate_info(name, email, tech_stack):
    """
    Simulates saving candidate information.
    """
    candidate_data[name] = {
        "email": email,
        "tech_stack": tech_stack,
    }
    return f"Thank you, {name}! Your information has been saved."

def get_candidate_info(name):
    """
    Simulates retrieving candidate information.
    """
    return candidate_data.get(name, "No information found.")