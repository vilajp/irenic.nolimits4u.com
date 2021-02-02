from woocommerce import API
import os

wcapi = API(
    url="http://irenic.nolimits4u.com",
    consumer_key="ck_ef3e0827be1490d3c846afd0ad3da4e8c704440d",
    consumer_secret="cs_3db60cc6e72d0b353c2b4421694701bfe307e9e3",
    version="wc/v3",
    timeout=10,
)

r = wcapi.get("products/categories", params={"per_page": 100}).json()
for i in r:
    print(i["id"], i["name"])
