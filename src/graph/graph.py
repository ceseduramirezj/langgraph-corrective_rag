from langgraph.graph import END, StateGraph

from src.graph.nodes import generate, grade_documents, retrieve, web_search
from src.consts import RETRIEVE, GRADE_DOCUMENTS, GENERATE, WEBSEARCH
from src.graph.state import GraphState

def decide_to_generate(state):
    print("---ASSESS GRADED DOCUMENTS---")

    if state["web_search"]:
        print(
            "---DECISION: NOT ALL DOCUMENTS ARE NOT RELEVANT TO QUESTION, INCLUDE WEBSEARCH---"
        )
        return WEBSEARCH
    
    else:
        print("---DECISION: GENERATE---")
        return GENERATE
    
workflow = StateGraph(GraphState)

workflow.add_node(RETRIEVE, retrieve)
workflow.add_node(GRADE_DOCUMENTS, grade_documents)
workflow.add_node(GENERATE, generate)
workflow.add_node(WEBSEARCH, web_search)

workflow.set_entry_point(RETRIEVE)
workflow.add_edge(RETRIEVE, GRADE_DOCUMENTS)

# Diccionario agregado que mapea el resultado de la función del enlace condicional al nodo correspondiente
# En este caso mapea al mismo que da la función pero en otros casos puede ser útil
workflow.add_conditional_edges(
    GRADE_DOCUMENTS,
    decide_to_generate,
    {
        WEBSEARCH: WEBSEARCH,
        GENERATE: GENERATE,
    },
)

workflow.add_edge(WEBSEARCH, GENERATE)
workflow.add_edge(GENERATE, END)

app = workflow.compile()

#app.get_graph().draw_mermaid_png(output_file_path="graph.png")