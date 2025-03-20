from pprint import pprint

from src.graph.chains.retrieval_grader import GradeDocuments, retrieval_grader
from src.graph.chains.generation import generation_chain
from src.ingestion import retriever

# question referencia a la pregunta original del usuario
# en el segundo test se cambia manualmente la pregunta para que no sea relevante

def test_retrieval_grader_answer_yes() -> None:
    question = "agent memory"
    docs = retriever.invoke(question)
    doc_txt = docs[0].page_content

    res: GradeDocuments = retrieval_grader.invoke(
        {"question": question, "document": doc_txt}
    )

    assert res.tool_calls[-1]['args']['binary_score'] == "yes"

def test_retrieval_grader_answer_no() -> None:
    question = "agent memory"
    docs = retriever.invoke(question)
    doc_txt = docs[0].page_content

    res: GradeDocuments = retrieval_grader.invoke(
        {"question": "how to make pizza", "document": doc_txt}
    )

    assert res.tool_calls[-1]['args']['binary_score'] == "no"

# Verificar funcionamiento de chain

def test_generation_chain() -> None:
    question = "agent memory"
    docs = retriever.invoke(question)
    generation = generation_chain.invoke({"context": docs, "question": question})
    pprint(generation)