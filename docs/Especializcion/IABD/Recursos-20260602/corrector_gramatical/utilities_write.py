#from mistralai import Mistral
from dotenv import load_dotenv  
from mistralai.client import Mistral
import os

# Cargar variables desde .env (busca en el directorio actual o padres)
load_dotenv() 

# Configuración del cliente de Mistral
api_key = os.getenv("MISTRAL_API_KEY", "eNlexCR0Hwvd2yPERjzHBV4EEJYrOKzV")
if api_key == "eNlexCR0Hwvd2yPERjzHBV4EEJYrOKzV":
    print("ADVERTENCIA: Usando API key por defecto. Define MISTRAL_API_KEY en el entorno.")
model = "mistral-large-latest"
client = Mistral(api_key=api_key)

prompt_template = {
    'corregir': """Eres un experto corrector de textos en español.
Tu tarea es corregir los errores gramaticales, ortográficos y de puntuación del siguiente texto.
Devuelve:
1. El texto corregido (en negrita los cambios con **texto**)
2. Una lista breve de los errores encontrados y corregidos

Si el texto no tiene errores, indícalo claramente.
Texto a corregir:""",

    'resumir': """Eres un experto en síntesis y comprensión lectora en español.
Tu tarea es resumir el siguiente texto de forma clara y concisa, conservando las ideas principales.
El resumen debe tener aproximadamente un 30% de la extensión del original.
Estructura tu respuesta así:
## Resumen
(tu resumen aquí)

## Ideas clave
(lista con los puntos más importantes)

Texto a resumir:""",

    'mejorar': """Eres un escritor profesional y estilista literario en español.
Tu tarea es mejorar el estilo del siguiente texto haciéndolo más fluido, elegante y atractivo,
manteniendo el significado original. Evita palabras repetidas, mejora la estructura de las frases
y usa vocabulario más rico.
Devuelve:
## Texto mejorado
(tu versión mejorada)

## Cambios realizados
(breve explicación de las mejoras aplicadas)

Texto a mejorar:""",

    'formalizar': """Eres un experto en comunicación formal y redacción profesional en español.
Tu tarea es convertir el siguiente texto informal o coloquial a un registro formal y profesional,
adecuado para un entorno de trabajo o comunicación oficial.
Devuelve:
## Versión formal
(el texto en registro formal)

## Notas
(cambios de registro más importantes)

Texto a formalizar:""",
}


def LLM_response(texto: str, modo: str) -> str:
    """
    Envía el texto a Mistral AI con el prompt correspondiente al modo elegido.
    
    Args:
        texto: El texto que el usuario quiere procesar
        modo: El tipo de procesamiento ('corregir', 'resumir', 'mejorar', 'formalizar')
    
    Returns:
        La respuesta generada por el modelo en formato Markdown
    """
    prompt_sistema = prompt_template.get(modo, prompt_template['corregir'])
    
    mensaje_usuario = f"{prompt_sistema}\n\n{texto}"
    
    try:
        # Realizar la llamada a la API de Mistral
        chat_response = client.chat.complete(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content":mensaje_usuario,
                },
            ]
        )
        
        # Extraer y devolver la respuesta
        return chat_response.choices[0].message.content
        
    except Exception as e:
        return f"Lo siento, ha ocurrido un error al generar la respuesta: {str(e)}. Por favor, inténtelo de nuevo."


 


# Comentar cuando ya tengamos la aplicación hecha para evitar redundancia
# if __name__=="__main__":
#     print(">>>>>>>>> Prueba con ingredientes válidos:")
#     test_ingredientes = "pollo, limón, ajo, romero, aceite de oliva"
#     receta = LLM_response(test_ingredientes)
#     print(receta)
    
#     print(">>>>>>>>> Prueba sin ingredientes:")
#     test_sin_ingredientes = "hola que tal"
#     receta2 = LLM_response(test_sin_ingredientes)
#     print(receta2)