from typing import List, TypedDict

# Utilizaremos un Graph state para esta aplicación por tanto necesitamos un objeto compartido que contenga el estado
# del grafo.

class GraphState(TypedDict):
    """
    Represents the state of our graph.
    
    Attributes:
        question: question
        generation: LLM generation
        web_search: wheter to add search
        documents: list of documents
    """

    question: str
    generation: str
    web_search: bool
    documents: List[str]