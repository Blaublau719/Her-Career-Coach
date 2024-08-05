from crewai import Agent, Task, Crew, process
import openai
from openai import OpenAI
from HCC_agents import HCC_Agents
from HCC_tasks import HCC_Tasks
from HCC_tools import HCC_Tools
from dotenv import load_dotenv


load_dotenv()

class HCCCrew:

  def __init__(self, PostingURL, Personal_Statement, resumeContent, Motivation):
    self.PostingURL = PostingURL
    self.Personal_Statement = Personal_Statement
    self.resumeContent = resumeContent
    self.Motivation = Motivation

  def run(self):
    agents = HCC_Agents()
    tasks = HCC_Tasks()

    PostExtracter = agents.PostExtracter()
    ClientKnower = agents.ClientKnower()
    CoverLetterWriter = agents.CoverLetterWriter()

    AboutJob = tasks.AboutJob(
      PostExtracter,
      self.PostingURL
    )
    AboutClient = tasks.AboutClient(
      ClientKnower,
      self.resumeContent,
      self.Personal_Statement
    )
    WriteCL = tasks.WriteCL(
      CoverLetterWriter,
      Motivation
    )

    crew = Crew(
    agents=[PostExtracter, ClientKnower, CoverLetterWriter],
    tasks=[AboutJob, AboutClient, WriteCL],
    verbose=2
    )

    result = crew.kickoff()
    return result

if __name__ == "__main__":
  # Initialize using OpenAI API key
  openai_api_key = userdata.get('openai_api_key')
  # Check if the API key is retrieved correctly
  if openai_api_key:
      print("API Key retrieved successfully.")
  else:
      print("API Key retrieval failed.")
  
  # Set the environment variable
  os.environ['OPENAI_API_KEY'] = openai_api_key
  
  # Optionally, you can also set the model name
  os.environ["OPENAI_MODEL_NAME"] = 'gpt-3.5-turbo'

  client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

  print(response)
  print("## Welcome to Her Career Coach")
  print('-------------------------------')
  PostingURL = input(
    dedent("""
      Please input the URL link of your interested Job Posting.
    """))

  Personal_Statement = input(
    dedent("""
      Feel free to tell me more about your self, you can provide me more personal information that your resume do not cover like your career plan, professional interet or hobbies.
    """))

  Motivation = input(
    dedent("""
      Tell me about your motivation for the job.
    """))
  
  tools = HCC_Tools()
  resumeContent = tools.read_file("/content/drive/MyDrive/CVs/cv.md") # You need to change the path to your resume path
  
  HCC_crew = HCCCrew(PostingURL, Personal_Statement, resumeContent, Motivation)
  result = HCC_crew.run()
  print("\n\n########################")
  print("## Here is a summary of your interested job and a suggested cover letter")
  print("########################\n")
  print(result)
