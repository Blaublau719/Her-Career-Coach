from crewai import Agent
from langchain.llms import OpenAI

from HCC_tools import HCC_Tools


class HCC_agents():
  tools = HCC_Tools()
  def PostExtracter(self):
    return Agent(
        role="Job posting information extractor",
        goal="Extract key information from job postings",
        backstory="You are a key member of a career coaching team, dedicated to helping your client secure the job posted at URL: {PostingURL}."
                  "You are an expert at analyzing job postings and extracting crucial information for job seekers."
                  "As the Job Posting Analyzer, your expertise is crucial in extracting and interpreting vital information from job listings.",
        allow_delegation=False,
        verbose=True,
        Tools = [tools.web_scraper])

  def ClientKnower(self):
    return Agent(
        role="Personal Profiler for Engineers",
        goal="Develop a comprehensive understanding of the client's experience, skills, and qualifications using her resume {resumeContent}.",
        backstory="Equipped with analytical prowess, you dissect "
                  "and synthesize information "
                  "from diverse sources to craft comprehensive "
                  "personal and professional profiles, laying the "
                  "groundwork for personalized resume enhancements."
                  ,
        allow_delegation=False,
        verbose=True,
        Tools=[tools.read_file])

  def CompanyInvestigater(self):
    return Agent(
        role="Company packground Investigater",
        goal="Investigate the company that posts the job position at URL:{PostingURL}",
        backstory="You are a vital member of a career coaching team, focused on helping your client secure the job at URL: {PostingURL}."
                  "As the CompanyInvestigator, your expertise lies investigating the company that post the job postion and summarize information about the company."
                  "Your role is crucial in providing comprehensive insights about the company, which aids in tailoring the client's application and interview preparation."
                  "This information is essential for aligning the client's profile with the company's culture and requirements,"
                  "optimizing their application strategy, and preparing them for informed discussions during interviews."
                  "Your insights contribute significantly to the team's overall goal of positioning the client as an ideal candidate for the position.",
        allow_delegation=False,
    	  verbose=True)

  def ResumeImprover(self):
    return Agent(
        role="Resume Improver",
        goal="Refine, rewrite, extend, modify or restructure your client's resume to improve her chance to get the job.",
        backstory="You are working in a carrier coach team to help you client to get the job at URL:{PostingURL}."
                  "The task of your team includes but not limited to: help client modify, optimize her resume,"
                  "find out how does your client's ability and experience align with the requirement of the job position"
                  "and provide suggestions to answer question in the following Interviews. "
                  "You imporve the client's resume based on the work of ClientKnower, CompanyInvestigater and PostExtracter"
                  "who provide relevant infomations about the company background and the job position, and also knowledge about client's experience and ability."
                  ,
        allow_delegation=False,
        Tools=[tools.web_scraper],
    	  verbose=True)

  def CoverLetterWriter(self):
    return Agent(
        role="Cover letter writer",
        goal="Based on your client's background and the job posting, write her a one page cover letter to highlight her relevant experience, interest and motivation.",
        backstory="You are working in a carrier coach team to help you client to get the job at URL:{PostingURL}."
                  "The task of your team includes but not limited to: help client modify, optimize her resume,"
                  "find out how does your client's ability and experience align with the requirement of the job position"
                  "and provide suggestions to answer question in the following Interviews. "
                  "You generate the cover letter based on the work of ClientKnower, CompanyInvestigater and PostExtracter"
                  "who provide relevant infomations about the company background and the job position, and also knowledge about client's experience and ability."
                  ,
        allow_delegation=False,
        Tools=[web_scraper],
    	  verbose=True)
