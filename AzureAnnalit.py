from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
import openai    # version0.28
from openai import ChatCompletion


#* Configuración de Azure Cognitive Search (Azure AI Search setup)
search_endpoint = "https://demodefinitiva.search.windows.net"; 
# AÑADIR KEY SEARCH
search_index_name = "implantacion-web-index"; 

#* Crea el cliente de Azure Cognitive Search
credential = AzureKeyCredential(search_key)
client = SearchClient(endpoint=search_endpoint, index_name=search_index_name, credential=credential)

#* Crea el cliente de OpenAI
#AÑADIR KEY API OPENAI
openai.api_type = "azure"
openai.api_base = "https://demodefinitiva.openai.azure.com/"
openai.api_version = "2023-07-01-preview"

#* Bucle principal
while True:
    # Solicita la entrada del usuario
    user = input("Usuario: ")

    # Si el usuario escribe 'salir', termina el bucle
    if user.lower() == 'salir':
        print("Hasta luego!")
        break

    else:
        # Realiza una búsqueda por vectores en Azure Cognitive Search
        results = client.search(
            search_text=user,
            query_type="semantic",
            query_answer="extractive|count-1",
            semantic_configuration_name="default",
            top=1,
        )

        results = list(results) # Convierte el resultado en una lista para poder usarlo para generar el contexto.

        # Si se encontraron resultados, usa el modelo de chat GPT para generar una respuesta
        if results:
            # Usa el primer resultado como contexto para el modelo de chat GPT
            context = results[0]['content']

            # Genera una respuesta usando el modelo de chat GPT
            response = openai.ChatCompletion.create(
                            engine="gpt-35-turbo", # engine = "deployment_name".
                            messages=[
                                {"role": "system", "content": "Estás chateando con un asistente de IA que puede responder preguntas basadas en el siguiente texto:"},
                                {"role": "user", "content": context},
                                {"role": "user", "content": user},
                                    ]
                        )
            
        print(response['choices'][0]['message']['content'] + "\n")


#print(response) --> ver todo el contenido de la respuesta.