predefined_responses = {
    "What is AJCL ?": "AJCL Private Limited, one of the leading business houses of Pakistan, is a diversified trading, distribution and technical service provider, providing project management, sales and consultancy services to clients in the public and private sector. ",
    "Opening Hours ?": "AJCL is open from 9 AM to 6 PM, Monday to Friday.",
    "Services Available ?": "Strategic Partnerships, Lead Business Development, Negotiation Leader, Provides Contract Execution Support, Customer Relationship Management, Supply Chain Management, After-Sales & Engineering Support, Financial Regulatory Adviser, Streamlined Payment Process",
    "hello": "Hello! How can I assist you today?",
    "default": "Sorry, I didn't understand that. Can you please clarify?"
}

# Define a mapping of keywords to the respective predefined response keys
keywords_mapping = {
    "AJCL": "What is AJCL ?",
    "what": "What is AJCL ?",
    "opening": "Opening Hours ?",
    "Opening": "Opening Hours ?",
    "hours": "Opening Hours ?",
    "Hours": "Opening Hours ?",
    "services": "Services Available ?",
    "Services": "Services Available ?",
    "Available": "Services Available ?",
    "available": "Services Available ?",
    "hello": "hello",
    "Hello": "hello"
}

def get_best_response(user_message):
    user_message_lower = user_message.lower()

    # Check if any keyword is present in the user's message
    for keyword, response_key in keywords_mapping.items():
        if keyword in user_message_lower:
            return predefined_responses[response_key]

    # Default response if no keywords are matched
    return predefined_responses["default"]
