import re
def remove_pii(text):
    pii_patterns = {
        "email": r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b',
        "phone": r'\b(?:\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})\b',
        "ssn": r'\b\d{3}-\d{2}-\d{4}\b',
        "credit_card": r'\b(?:\d{4}[-\.\s]?){3}\d{4}\b',    
    }
    for pattern in pii_patterns.values():
        text = re.sub(pattern, "[CENSORED]", text)
    return text


input_text = "Anish's email is test@temp.com and his phone number is 123-456-7890, SSN is 765-433-123"
output = remove_pii(input_text)
print(output)