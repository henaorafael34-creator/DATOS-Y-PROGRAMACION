# DDYA parcial práctico tercio 2

Explicaciones (En cuanto el funcionamiento principal de cada punto, no incluye resiliencia a erores)

El grafo se representa por medio de una lista de adyacencia, la cual es un diccionario que expresa las listas de vecinos con llaves que son cada elemento en el grafo.

BFS se implementó por medio de una cola de atención, se van atendiendo los nuevos nodos encontrados por cada proceso, siempre siguiendo la lógica FIFO, donde el frente es el inicio de la lista que es la cola.

DFS se aplica a través de un recorrido recursivo, el cual va cambiando el recorrido y los visitados, para finalmente darnos el orden adecuado por profundidad.

La mayoría de funciones se sintetizaron dentro de una sola clase, RedSocial.

La búsqueda de una nueva ruta, se provee requiriendo un origen y un objetivo, se navega por medio de BFS el grafo, en el proceso no es necesario registrar recorrido, entonces la diferencia es que se almacenan los padres de cada nodo visitado, de esta manera se almacena un recorrido desde el objetivo a el origen en la lista de padres, así solo obtenemos la ruta de interés, como se recorre desde el objetivo, al final aplicamos reverse, y el output es el recorrido más corto.

El agregar un nuevo usuario, se hace insertando el nombre del nuevo nodo, para después por medio de una función esencial de unión bidireccional, se entrelacen los nodos ya existentes seleccionados, con el usuario nuevo insertado.

Muestra de grafo:

<img width="663" height="521" alt="image" src="https://github.com/user-attachments/assets/755987b5-0779-462b-beb5-97f2a39366af" />

BFS desde Ana:

<img width="741" height="182" alt="image" src="https://github.com/user-attachments/assets/ceff8b75-7093-405d-b513-f0bd4ec31bb2" />

DFS desde Ana:

<img width="752" height="85" alt="image" src="https://github.com/user-attachments/assets/6bbe7ae1-b3a2-4e75-8509-ab31bf301913" />

Desde usuario seleccionado:

<img width="749" height="314" alt="image" src="https://github.com/user-attachments/assets/5ece27d2-2358-491b-85ec-bc162b21c412" />

Búsqueda de ruta mínima desde origen insertado a objetivo seleccionado:

<img width="743" height="410" alt="image" src="https://github.com/user-attachments/assets/52958e3f-af3c-4b8d-b268-6ad86c53c8c0" />

Agregación de nuevo usuario:

<img width="870" height="145" alt="image" src="https://github.com/user-attachments/assets/9d2cc7a6-133b-4cb2-923e-fbe99972519e" />

Solicitud preferencial de tutor:

Buscador de usuario específico.

<img width="451" height="179" alt="image" src="https://github.com/user-attachments/assets/9e593953-d107-4c24-938c-08af523c4de8" />









