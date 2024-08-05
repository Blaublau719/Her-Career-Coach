from pydantic import BaseModel
# Define a pydantic model for company descriptions

class CompInfo (BaseModel):
    company_name: str
    company_core_business: str
    company_location: str
    company_kununu_score: str
    employee_reviews: str
    number_employee: str
