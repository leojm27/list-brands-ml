from services.ProductService import ProductService
from controllers.BrandController import BrandController

productService = ProductService()
brandController = BrandController()

if __name__ == '__main__':
    print("Realizando peticiones a la API de MercadoLibre...")
    list_brands = brandController.get_list_brands()
    brandController.show_brand_average(list_brands)
