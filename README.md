# Chatbot Att. cliente con documentos PDF

Para las soluciones a coste 0 he optado por usar Mistral-7B, Phi-4-mini y Phi-3-instruct, los cuales han sido elegido porque son capaces de realizar las tareas encomendadas y los puedo usar en mi cpu, aunque la limitación de no tener GPU los hacen lentos, pero con una pequeña GPU se podrían implentar sin problemas.

### Conclusiones:

A todos los modelos se le han pasado las mismas preguntas de control una por documento:

a) servicios training2works

b) cuales son los pasos del flujo de trabajo

c) cual es el plan de accion para la clinica beiman

- Chatgpt 3.5-turbo-125: Es el que da mejor respuesta y en el menor tiempo posible (instantáneo) pero su coste es su mayor inconveniente, ya que procesar muchos documentos como contexto puede que lo haga poco rentable.

- Modelos opensource: 

    * Mistral 7B: Es lento en contestar pero da respuestas adecuadas aunque no son correctas al 100%.

    * Phi-4-mini: Queda descartado por ser demasiado lento como para poder trabajar con él, más de 20 min en dar respuesta a cada pregunta. No es nada útil.

    * Phi-3-instruct: Es un poco más rápido que mistral pero las respuestas son un poco precisas.

Para implementar este proyecto la solución elegida sería Mistral-7B al que habría que realizarle un finne-tunning para agilizar el modelo y obtener mejores respuestas. (No se ha podido realizar el finnetuned por falta de tiempo para el proyecto)
