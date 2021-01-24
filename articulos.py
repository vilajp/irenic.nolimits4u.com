from woocommerce import API
import os
import shutil

wcapi = API(
    url="http://irenic.nolimits4u.com",
    consumer_key="ck_ef3e0827be1490d3c846afd0ad3da4e8c704440d",
    consumer_secret="cs_3db60cc6e72d0b353c2b4421694701bfe307e9e3",
    version="wc/v3",
    timeout = 10,
    )

'''


def renombrar(arch_renombrados=0):
    resguardo = open("resguardo.txt", "a+")
    for archivo in os.listdir("."):
        print("Analizando " + archivo)
        cant = 0
        for i in range(len(archivo)):
            if archivo[i] in " 0123456789-" and archivo[-3:].lower() == "mp3":
                cant += 1
                continue
            else:
                if cant > 0:
                    print("Encontrado " + archivo + " renombrando " + archivo[cant:len(archivo)])
                    resguardo.write(archivo + "%" + archivo[cant:len(archivo)] + "\r")
                    os.rename(archivo, archivo[cant:len(archivo)])
                    arch_renombrados += 1
                    break
                else:
                    break
    resguardo.close()
    return arch_renombrados'''
    
'''dict_keys(['id', 'name', 'slug', 'permalink', 'date_created', 'date_created_gmt'
, 'date_modified', 'date_modified_gmt', 'type', 'status', 'featured', 
'catalog_visibility', 'description', 'short_description', 'sku', 'price', 
'regular_price', 'sale_price', 'date_on_sale_from', 'date_on_sale_from_gmt', 
'date_on_sale_to', 'date_on_sale_to_gmt', 'on_sale', 'purchasable', 'total_sales',
 'virtual', 'downloadable', 'downloads', 'download_limit', 'download_expiry', 
 'external_url', 'button_text', 'tax_status', 'tax_class', 'manage_stock', 
 'stock_quantity', 'backorders', 'backorders_allowed', 'backordered', 
 'sold_individually', 'weight', 'dimensions', 'shipping_required', 
 'shipping_taxable', 'shipping_class', 'shipping_class_id', 'reviews_allowed', 
 'average_rating', 'rating_count', 'upsell_ids', 'cross_sell_ids', 'parent_id', 
 'purchase_note', 'categories', 'tags', 'images', 'attributes', 
 'default_attributes', 'variations', 'grouped_products', 'menu_order', 
 'price_html', 'related_ids', 'meta_data', 'stock_status', '_links'])

{'id': 385, 'name': 'cepillo', 'slug': 'cepillo', 
'permalink': 'http://irenic.nolimits4u.com/producto/cepillo/', 
'date_created': '2021-01-23T00:30:43', 'date_created_gmt': '2021-01-23T00:30:43', 
ate_modified': '2021-01-23T00:30:43', 'date_modified_gmt': '2021-01-23T00:30:43',
 'type': 'simple', 'status': 'publish', 'featured': False, 
 'catalog_visibility': 'visible', 'description': '', 'short_description': '', 
 'sku': '', 'price': '', 'regular_price': '', 'sale_price': '', 
 'date_on_sale_from': None, 'date_on_sale_from_gmt': None, 'date_on_sale_to': None,
 'date_on_sale_to_gmt': None, 'on_sale': False, 'purchasable': False, 
 'total_sales': 0, 'virtual': False, 'downloadable': False, 'downloads': [], 
 'download_limit': -1, 'download_expiry': -1, 'external_url': '', 
 'button_text': '', 'tax_status': 'taxable', 'tax_class': '', 'manage_stock': False,
  'stock_quantity': None, 'backorders': 'no', 'backorders_allowed': False, 
  'backordered': False, 'sold_individually': False, 'weight': '', 
  'dimensions': {'length': '', 'width': '', 'height': ''}, 
  'shipping_required': True, 'shipping_taxable': True, 'shipping_class': '', 
  'shipping_class_id': 0, 'reviews_allowed': True, 'average_rating': '0.00', 
  'rating_count': 0, 'upsell_ids': [], 'cross_sell_ids': [], 'parent_id': 0, 
  'purchase_note': '', 'categories': [{'id': 15, 'name': 'Sin categorizar', 
  'slug': 'sin-categorizar'}], 'tags': [], 'images': [], 'attributes': [], 
  'default_attributes': [], 'variations': [], 'grouped_products': [], 
  'menu_order': 0, 'price_html': '', 'related_ids': [383, 382, 384], 
  'meta_data': [], 'stock_status': 'instock', 
  '_links': {'self': [{'href': 'http://irenic.nolimits4u.com/wp-json/wc/v3/products/385'}], 
  'collection': [{'href': 'http://irenic.nolimits4u.com/wp-json/wc/v3/products'}]}}'''

#.get(endpoint, **kwargs)
#.post(endpoint, data, **kwargs)
#.put(endpoint, data), **kwargs
#.delete(endpoint, **kwargs)

'''data = {
    "create": [
        {
            "name": "Woo Single #1",
            "type": "simple",
            "regular_price": "21.99",
            "virtual": True,
            "downloadable": True,
            "downloads": [
                {
                    "name": "Woo Single",
                    "file": "http://demo.woothemes.com/woocommerce/wp-content/uploads/sites/56/2013/06/cd_4_angle.jpg"
                }
            ],
            "categories": [
                {
                    "id": 11
                },
                {
                    "id": 13
                }
            ],
            "images": [
                {
                    "src": "http://demo.woothemes.com/woocommerce/wp-content/uploads/sites/56/2013/06/cd_4_angle.jpg"
                }
            ]
        },
        {
            "name": "New Premium Quality",
            "type": "simple",
            "regular_price": "21.99",
            "description": "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo.",
            "short_description": "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.",
            "categories": [
                {
                    "id": 9
                },
                {
                    "id": 14
                }
            ],
            "images": [
                {
                    "src": "http://demo.woothemes.com/woocommerce/wp-content/uploads/sites/56/2013/06/T_2_front.jpg"
                },
                {
                    "src": "http://demo.woothemes.com/woocommerce/wp-content/uploads/sites/56/2013/06/T_2_back.jpg"
                }
            ]
        }
    ],
    "update": [
        {
            "id": 799,
            "default_attributes": [
                {
                    "id": 6,
                    "name": "Color,
                    "option": "Green"
                },
                {
                    "id": 0,
                    "name": "Size",
                    "option": "M"
                }
            ]
        }
    ],
    "delete": [
        794
    ]
}
'''

data = {
    # "create": [
    #     {
    #         "name": "Brand"
    #     },
    #     {
    #         "name": "Publisher"
    #     }
    # ],
    # "update": [
    #     {
    #         "id": 389,
    #         "name": "Cepillos Meraki",
    #         'regular_price':"255.99",
    #         "images": [
    #             {
    #                 "src": "http://irenic.nolimits4u.com/wp-content/uploads/2021/01/irenic-cepillos-meraki.jpg"
    #             }
    #         ],
    #     }
    # ],
    # "delete": [
    #     392,
    #     393,
    #     394,
    #     395,
    #     396,
    #     397,
    #     398,
    # ]
}

#print(wcapi.post("products/attributes/batch", data).json())

'''data = {
    "order_by": "name"
}

print(wcapi.put("products/attributes/1", data).json())'''
def actualizo(accion, datos):
	data = {
			accion:[
			datos
			]
		}
	return data
 
for archivo in os.listdir("./fotos/articulos"):
	if archivo[-3:]=="jpg":
		
		print("Actualizando...",archivo)
		datos = {}
		nombre_producto = capitalize("".join(archivo.split("irenic - "))[0:-4])

		datos["name"] = nombre_producto
		nombre_archivo = "-".join(nombre_producto.split())

		datos["images"] = [
	                {
	                    "src": f"http://irenic.nolimits4u.com/wp-content/uploads/2021/01/irenic-{nombre_archivo}.jpg"
	                }
	                ]

		data = actualizo("create", datos)


		while True:
			salir = False
			try:
				print(wcapi.post("products/batch", data).json())
				shutil.move(archivo, "./fotos/articulos/copiados")			
				break
			except KeyboardInterrupt:
				print("Programa interrumpido por Operador")
				salir = True
				break
			else:
				print("No pude conectarme, reintentando...")
		if salir:
			break
	else:
		print("No hay archivos de fotos para seguir")
r = wcapi.get("products", params={"per_page": 100}).json()
for i in r:
	print(i["id"],i["name"], i["price"])
	

