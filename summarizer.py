from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers  import StrOutputParser
from dotenv import load_dotenv

load_dotenv()


def summarize_text(text: str, option: str) -> str:
  system_prompt = """
  Summarize the user's text following the rule below.
  If the rule is not "Bullet points" you have to summarize in paragraphs.
  Write just the summary, with no additional content.

  Rule: {option} summary.
  """

  prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("user", "{text}"),
  ])

  llm = ChatGroq(temperature=0.0, model="openai/gpt-oss-120b")

  output_parser = StrOutputParser()

  pipeline = (
    {
      "text": lambda x: x["text"],
      "option": lambda x: x["option"]
    }
    | prompt_template
    | llm
    | output_parser
  )

  return pipeline.invoke({"text": text, "option": option})
