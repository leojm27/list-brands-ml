# list-brands-ml

El programa se creo para listar marcas de motos, y su precio promedio de todas las motos publicadas en MercadoLibre (para cada marca).
Para ello se utilizó la API pública de mercadolibre.

## API MercadoLibre

El proyecto realiza peticiones al siguiente endpoint para obtener información de publicaciones de Motos, utilizando el id de categoría (MLA1763)
- [ https://api.mercadolibre.com/sites/MLA/search?category=MLA1763 ] 

Una vez que se obtiene la información de las motos publicadas, se realiza un procesamiento de los datos, obteniendo asi un Listado de Productos(motos), y un listado de Marcas.
El proyecto devuelve por consola un Listado de las Marcas de motos obtenidas de nuestras peticiones a la API, y para cada Marca se calcula el precio Promedio.

# Librerias
- [ https://docs.python-requests.org/en/master/ ] 
- Requests nos permite enviar peticiones HTTP. 

# Instalación
## Instalar dependencias
python -m pip install requests

# Ejecutar proyecto
python main.py
