from pydantic import BaseModel
# Define a pydantic model for Job Descriptions

class JobDescription(BaseModel):
    Job_Title: str
    Company_Name: str
    Job_Description: str
    Key_Responsibilities: str
    Qualifications_and_Requirements: str
    Location: str
    Benefits_Salary: str
    Company_Overview: str
