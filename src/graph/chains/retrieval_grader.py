from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import AzureChatOpenAI
from pydantic import BaseModel, Field

#from typing import Dict, Any
import os

# Chain para identificar qué documentos son relevantes entre los recogidos por el retriever para la pregunta

llm = AzureChatOpenAI(azure_deployment=os.environ['AZURE_DEPLOYMENT_NAME'])

class GradeDocuments(BaseModel):
    """Binary score for relevance check on retrieved documents."""

    binary_score: str = Field(
        description="Documents are relevant to the question, 'yes' or 'no'"
    )

    #def to_dict(self) -> Dict[str, Any]:
    #    return {"binary_score": self.binary_score}

# LLM tiene que soportar function calling para adaptar la salida a la clase pydantic
#structured_llm_grader = llm.with_structured_output(GradeDocuments, method="function_calling")
#grade_documents_parser = PydanticOutputParser(pydantic_object=GradeDocuments)

system = f"""You're a grader assessing relevance of a retrieved document to a user question. \n
    f the document contains keyword(s) or semantic meaning related to the question, grade it as relevant. \n
    Give a binary score 'yes' or 'no' score to indicate wheter the document is relevant to the question."""

# Prompt que recibe LLM para evaluar la relevancia de un documento
grade_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "Retrieved document: \n\n {document} \n\n User question: {question}"),
    ]
)

# Chain para la evaluación de la relevancia de un documento
# retrieval_grader = grade_prompt | structured_llm_grader
# Se utiliza esta otra forma ya que LLM no soporta function calling o json_format
retrieval_grader = grade_prompt | llm.bind_tools(
    tools = [GradeDocuments], tool_choice="GradeDocuments"
)