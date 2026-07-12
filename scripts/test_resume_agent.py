from backend.agents.resume_agent import ResumeAgent
from backend.tools.pdf_parser import PDFParser

parser = PDFParser()

text = parser.extract_text("storage/uploads/sample_resume.pdf")

agent = ResumeAgent()

response = agent.analyze(text)

print(response)