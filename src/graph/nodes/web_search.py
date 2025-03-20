from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.schema import Document

from typing import Any, Dict

from src.graph.state import GraphState

# Función para el nodo webSearch que realizará búsqueda en internet sobre la pregunta dada por el usuario
# si hay documentos aún después de filtrarlos se concatenará el resultado obtenido de la búsqueda en la web
# en otro caso se declara como el único elemento de los documentos

web_search_tool = TavilySearchResults(max_results=3)

def web_search(state: GraphState) -> Dict[str, Any]:
    print("---WEB SEARCH---")
    question = state["question"]
    documents = state["documents"]

    tavily_results = web_search_tool.invoke({"query": question})
    joined_tavily_result = "\n".join(
        [tavily_result["content"] for tavily_result in tavily_results]
    )

    web_results = Document(page_content=joined_tavily_result)
    if documents is not None:
        documents.append(web_results)
    else:
        documents = [web_results]
    return {"documents": documents, "question": question}