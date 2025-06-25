import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(
            temperature=0,
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model_name="llama-3.3-70b-versatile"
        )

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """  
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ###Instruction:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing 
            the following keys: 'role', 'experience', 'skills', and 'description'.
            Only return valid JSON.
            ###valid json (no preamble):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={'page_data': cleaned_text})

        try:
            json_parser = JsonOutputParser()
            parsed_res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        
        return parsed_res if isinstance(parsed_res, list) else [parsed_res]

    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
            Job Description:
            {job_description}
            ### Instruction:
            I am Vishwa, a Business Development Executive at Goldmanscas. We have an AI software consulting company. Over the years, we have empowered numerous enterprises with tailored solutions, fostering process optimization, cost reduction, and heightened overall efficiency.     
            Your task is to write a cold email to the client regarding the job mentioned above, fulfilling their needs. Also, include the most relevant items from the following portfolio links to showcase your expertise. Remember, you are Vishwa.
            Do not provide any preamble.
            ### EMAIL (NO PREAMBLE):
            """
        )
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "linklist": links})
        return res.content


if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))

