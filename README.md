### Her-Career-Coach
This LLM-powered digital career coach leverages the CrewAI framework and the GPT-3.5-turbo model by OpenAI. Designed by Lan, serves as a personalized tool to enhance her job applications and career opportunities.

## To initialize
You will need to get your own OpenAI API key at: https://platform.openai.com/api-keys. And then save it in the variable 'openai_api_key'. To ensure successful use of API key, you may need to add payment methods and charge your OpenAI first...

## Understand the framework
This tool is build up on basic CrewAI framwork with some self written tools. The structure is super easy to understand:
1. Agents defined (PostExtractor, ClientKnower, CompanyInvestigator, ResumeImprover and CoverLetterWriter currently available)
2. Tasks defined (AboutJob, AboutClient, AboutCompany, RefineResume, and WriteCL currently available)
3. Crew defined (tell the crew what tasks need to be done/ in what sequence, the 1st agent in the agent list with be in charge of the 1st Task, and 2nd Agent in charge of 2nd Task and so on...)
4. Kick off your crew (with proper inputs that your Agents or Tasks need)
To understand the parameter and co.: https://docs.crewai.com/
Feel free to write your own Agents and Tasks or adjust prompts for your personalized requirements. :)

