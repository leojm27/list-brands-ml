# README

Nombre del proyecto: list-brands-ml

El programa se creó para listar marcas de motos, y su precio promedio de todas las motos publicadas en MercadoLibre (para cada marca).
Para ello se utilizó la API pública de Mercado Libre.

## API MercadoLibre

Documentación
Principal
- [ https://developers.mercadolibre.com.ar/es_ar/api-docs-es ]

Obtención de Categoría e información de productos
- [ https://developers.mercadolibre.com.ar/es_ar/categorias-y-publicaciones ] 
- [ https://developers.mercadolibre.com.ar/es_ar/items-y-busquedas ]

El proyecto realiza peticiones al siguiente endpoint para obtener información de publicaciones de Motos, utilizando el Id de categoría (MLA1763)
- [ https://api.mercadolibre.com/sites/MLA/search?category=MLA1763 ] 
- Ejemplo del Json devuelto por la API, en archivo 'example_data_api.json'.

Una vez que se obtiene la información de las motos publicadas, se realiza un procesamiento de los datos, obteniendo asi un Listado de Productos(motos), y un listado de Marcas.
El proyecto devuelve por consola un Listado de las Marcas de motos obtenidas de nuestras peticiones a la API, y para cada Marca se calcula el precio Promedio.

## Modelos de Datos

| Product       | Tipo   |
|---------------|--------|
| id_product    | String |
| title         | String |
| price         | float  |
| condition     | String |
| brand         | String |


| Brand       | Tipo   |
|-------------|--------|
| brand_name  | String |
| total_price | float  |
| quantity    | int    |
| average     | float  |


## Librerías
- [ https://docs.python-requests.org/en/master/ ] 
- Requests nos permite enviar peticiones HTTP. 

## Instalación
### Instalar dependencias
python -m pip install requests

### Ejecutar el proyecto
python main.py
