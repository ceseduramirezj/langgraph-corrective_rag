from src.graph import workflow

if __name__ == '__main__':
    print('Hello, Corrective RAG!')
    print(workflow.invoke(input={"question": "what is agent memory?"}))