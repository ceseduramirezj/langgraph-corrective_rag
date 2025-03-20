# Arquitectura RAG Correctivo

Este repositorio contiene el código de un RAG Correctivo con LangGraph. Un RAG correctivo es una versión más completa de un RAG común ya que se controla el flujo en función de si los documentos extraidos del vector store son relevantes a la petición de usuario, en caso de que no se puede pedir ayuda a fuentes externas (la web en este caso).

## Funcionamiento

Esta arquitectura consiste en los siguientes pasos:

1. Usuario envía pregunta al flujo
2. El flujo inicia con el nodo 'retrieve' que obtiene los documentos, almacenados en el vector store, relacionados con la pregunta.
3. Se comprueba la relevancia de cada documento obtenido en el nodo 'grade_documents', concatenando una etiqueta de si o no a los relevantes o no para la pregunta.
4. Se filtran los documentos y nos quedamos con solo los relevantes.
5. Si hay documentos no relevantes, se complementan los documentos agregando uno más obtenido del internet gracias a Tavily (se busca con la pregunta del usuario).
6. Con todos los documentos se enriquece el prompt final a partir de un contexto compuesto de todos los documentos. Con esto el LLM responde al usuario con toda la información que necesita.

## Diagrama

A continuación mostramos un diagrama del Flujo:

![Grafo del Flujo](/assets/graph.png)

## Variables de entorno

Se han utilizado servicios externos como Tavily, LangSmith, OpenAI, Azure, etc. Por ello, hay que incluir las siguientes variables de entorno:

- AZURE_OPENAI_API_KEY
- AZURE_OPENAI_ENDPOINT
- OPENAI_API_VERSION
- AZURE_DEPLOYMENT_NAME
- OPENAI_API_KEY
- LANGSMITH_API_KEY
- LANGSMITH_PROJECT
- TAVILY_API_KEY

## Testing

Es muy importante el testing al trabajar con LLM, ya que son entidades estadísticas y hay que comprobar el buen funcionamiento por ello utilizamos pytest.