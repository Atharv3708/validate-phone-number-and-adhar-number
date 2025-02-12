import re

def validate_phone_number(phone):
    pattern = r"^[6-9]\d{9}$"  # Indian phone numbers start with 6-9 and have 10 digits
    return bool(re.fullmatch(pattern, phone))

def validate_aadhaar_number(aadhaar):
    pattern = r"^\d{4}\s\d{4}\s\d{4}$"  # Aadhaar format: 4 digits space 4 digits space 4 digits
    return bool(re.fullmatch(pattern, aadhaar))

# User input
phone = input("Enter phone number: ")
aadhaar = input("Enter Aadhaar number: ")

# Validation
print("\nValidation Results:")
print(f"Phone Number ({phone}): {'Valid' if validate_phone_number(phone) else 'Invalid'}")
print(f"Aadhaar Number ({aadhaar}): {'Valid' if validate_aadhaar_number(aadhaar) else 'Invalid'}")
