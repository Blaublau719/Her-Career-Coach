import langchain
from langchain_community.document_loaders import AsyncChromiumLoader
from langchain_community.document_transformers import BeautifulSoupTransformer

class HCC_Tools():
  
  def web_scraper(url): # compared different methods (and FirecrawlScrapeWebsiteTool and ScrapeWebsiteTool(cant handle antiscraping) provided by crewAI), this one most recommended
    loader = AsyncChromiumLoader(url)
    html = loader.load()
    # Transform
    bs_transformer = BeautifulSoupTransformer()
    docs_transformed = bs_transformer.transform_documents(html, tags_to_extract=["span"])
    return docs_transformed

  def read_file(file_path: str) -> str:
      """
      Reads the content of a file at the given file path.
  
      Args:
          file_path (str): The path to the file to be read.
  
      Returns:
          str: The content of the file if successfully read, or an error message if an exception occurs.
      """
      try:
          with open(file_path, 'r') as file:
              content = file.read()
          return content
      except FileNotFoundError:
          return f"Error: File not found at {file_path}"
      except IOError:
          return f"Error: Unable to read file at {file_path}"
      except Exception as e:
          return f"An unexpected error occurred: {str(e)}"
