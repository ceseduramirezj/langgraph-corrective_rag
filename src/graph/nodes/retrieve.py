from typing import Any, Dict

from src.graph.state import GraphState
from src.ingestion import retriever

# Función del nodo recoger para obtener los documentos relevantes a una pregunta (aún no se hace filtrado)

def retrieve(state: GraphState) -> Dict[str, Any]:
    print("---RETRIEVE---")
    question = state["question"]

    documents = retriever.invoke(question)
    return {"documents": documents, "question": question}