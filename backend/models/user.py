from pydantic import BaseModel, EmailStr, constr, field_validator
import re

# This model is ONLY for validating incoming data from the signup form.

class User(BaseModel):
    name: constr(min_length=5)
    email: EmailStr
    password: constr(min_length=8)
    phone: str

    @field_validator('phone')
    def validate_phone_number(cls, value):
        phone_str = str(value)
        indian_phone_regex = r'^(\+91)?[6-9]\d{9}$'
        if not re.match(indian_phone_regex, phone_str):
            raise ValueError('Invalid phone number format.')
        return phone_str

    @field_validator('password')
    def validate_password_strength(cls, value):
        if not re.search(r'[a-z]', value):
            raise ValueError('Password must contain a lowercase letter.')
        if not re.search(r'[A-Z]', value):
            raise ValueError('Password must contain an uppercase letter.')
        if not re.search(r'\d', value):
            raise ValueError('Password must contain a digit.')
        if not re.search(r'[@$!%*?&]', value):
            raise ValueError('Password must contain a special character.')
        return value