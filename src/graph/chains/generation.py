from langchain_core.output_parsers import StrOutputParser
from langchain_openai import AzureChatOpenAI
from langchain import hub

import os

# Chain para generar una respuesta utilizando un contexto (RAG)

llm = AzureChatOpenAI(azure_deployment=os.environ['AZURE_DEPLOYMENT_NAME'])
prompt = hub.pull("rlm/rag-prompt")

generation_chain = prompt | llm | StrOutputParser()