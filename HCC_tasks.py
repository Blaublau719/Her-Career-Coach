from crewai import Task
from HCC_tools import HCC_Tools
from job_description import JobDescription
from company_description import CompInfo
from some_task_library import Task  # Replace with the actual library you are using

class HCC_Tasks():
  def AboutJob(self, PostingURL):
    return Task(
        description=(
            "Analyze the job posting at {PostingURL} and extract the following information:\n"
            "If any information is not found, state 'Information not available'."
            "Use the original language of the job posting."
            "Use markdown formatting for better readability."
            "Use the original language of the job posting."
            "Read through the job posting carefully, and list all possible locations for the job if there are multiple" #still can't list all cities
            "For the requirements, qualifications, and responsibilities, use original text in that url."
        ),
        expected_output=(
            "A structured summary of the job posting containing the following information:\n"
            "1. Job Title\n"
            "2. Company Name\n"
            "3. Job Description (brief summary and a comprehensive summary)\n"
            "4. Key Responsibilities\n"
            "5. Qualifications and Requirements\n"
            "6. Location\n"
            "7. Benefits and Salary (if available)\n"
            "8. Company Overview (brief)\n"
            "If any information is not found, state 'Information not available'."
        ),
        output_json=JobDescription,
        output_file="job_description.json",  # Specify the file where the output will be saved
        agent=PostExtracter,
        Tools=[web_scraper])

  def AboutClient(self, resumeContent, Personal_Statement):
    return Task(
      description=(
          "Compile a detailed personal and professional profile "
          "based on the client's resume. Utilize tools to extract and "
          "synthesize information from her resume from {resumeContent} and her {Personal_Statement}."
          "Use the original language of the job posting."
          "Use markdown formatting for better readability."
      ),
      expected_output=("A comprehensive profile document based on the client's resume that includes her skills, "
          "project experiences, educations, contributions, interests. in markdown format")
          ,
      agent=ClientKnower,
      Tools=[read_file],
      output_file="client_profile.md")

  def AboutCompany(self):
    return Task(
      description=(
          "Compile a structured summary of the company, including key information such as:"
          "The company's core business, products, or services"
          "The company's location"
          "The company's kununu score, reputation overall employee reviews"
          #"Financial stability and growth" may need integrate external tool to assess this
          "Company size, structure and number of employees"
          "If you can find some of the key informations, don't fake it just say you can't find it"
          "Use the original language of the job posting."
      ),
      expected_output="A clear and well structured summary of the company, including key information such as:"
                      "The company's core business, products, or services"
                      "The company's position. If there are multiple list all of them"
                      "The company's kununu score, reputation overall employee reviews"
                      "Financial stability and growth" #may need integrate external tool to assess this
                      "Company size, structure and number of employees"
          ,
      agent=CompanyInvestigater,
      #Tools=[serper_tool, web_scraper], still can't identify company name correctly, need to fix serper function
      context=[AboutJob])

  def RefineResume(self, resumeContent):
    return Task(
      description=(
          "Refine, rewrite, extend, modify or restructure your client's resume {resumeContent} to improve her chance to get the job."
          "Make use of information provided by ClientKnower to tailor her resume for the job, highlighting her skills and experiences most relevant to that position."
          "If the client's experience or ability align with job requirement, use keywords from the job posting to help her resume pass applicant tracking systems (ATS)."
          "Here are the principles of how you should improve her resume:"
                "1. Make sure the information of client that align with the job's requirement is prioritized in the resume."
                "2. Make use of information provided by ClientKnower to make the resume comprehensive"
                "3. Use action verbs and concrete examples rather than vague statements"
                "4. Use a clean, professional font and formatting that is easy to read"
                "5. Proofread carefully for any errors or typos"
                "6. Do not fake any information that is not true about the client"
                "7. Use the original language of the job posting."
                "8. Use markdown formatting for better readability."
      ),
      expected_output=("A comprehensive and well structured resume document in markdown format"
                      "using the original resume overall structure and text style."
                      "Complemented with any additional background information that are align with the position requirement."
                      "With the most relevant expereience or ability prioritized in each section.")
          ,
      agent=ResumeImprover,
      context=[AboutClient, AboutJob], # Need tool: pdfGenerator, save the refined resume in the company's folder
      output_file="refined_resume.md",
      # output_file=f"RefCV4_{comp_name}_{job_position}")
      
  def WriteCL(self, resumeContent):
    return Task(
      description=(
          "Write a compelling cover letter for your client that effectively showcases their qualifications for the job position."
          "Follow these guidelines:"
          "1. Tailor the content to the specific job and company, using information from AboutJob and AboutClient."
          "2. Highlight the client's most relevant skills and experiences that align with the job requirements."
          "3. Use a professional yet approachable tone, avoiding overly complex language."
          "4. Incorporate keywords from the job posting to improve ATS compatibility."
          "5. Structure the letter with a clear introduction, body paragraphs, and conclusion."
          "6. Keep the content concise and limit it to one page."
          "7. Use the original language of the job posting."
          "8. Proofread carefully for any errors or typos."
          "9. Use markdown formatting for better readability."
      ),
      expected_output=(
          "A well-crafted, one-page cover letter in markdown format that:"
          "- Is tailored to the specific job and company"
          "- Highlights the client's most relevant qualifications"
          "- Uses a professional but easily understandable tone"
          "- Incorporates relevant keywords from the job posting"
          "- Is free of errors and typos"
      ),
      agent=CoverLetterWriter,
      context=[AboutClient, AboutJob],
      output_file="cover_letter.md")
    
