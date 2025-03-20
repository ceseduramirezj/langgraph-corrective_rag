from typing import Any, Dict

from src.graph.chains.generation import generation_chain
from src.graph.state import GraphState

# Función para el nodo de generación RAG

def generate(state: GraphState) -> Dict[str, Any]:
    print("---GENERATE---")
    question = state["question"]
    documents = state["documents"]

    generation = generation_chain.invoke({"context": documents, "question": question})
    return {"documents": documents, "question": question, "generation": generation}