import json
import requests
from concurrent.futures import ThreadPoolExecutor

from tenacity import retry, wait_exponential, stop_after_attempt
store_hash = "rmz2xgu42d"
token = "jpts4mh09fxfef5ysqcgyyuqnegorgb"
class BCServer:
    def __init__(self):
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "X-Auth-Token": token
        }
        self.base_url = f"https://api.bigcommerce.com/stores/{store_hash}"
        self.session = requests.Session()

    def create_customer(self,user):
        data=[{
            "email":user.get("email"),
            "first_name":user.get("username"),
            "last_name":user.get("username"),
            "addresses":[
                {
                    "first_name": "Ronald",
                    "city": "San Francisco",
                    "country_code": "US",
                    "last_name": "Swimmer",
                    "address1": "Addr 1",
                }
            ],
            "authentication": {
                "force_password_reset": True,
                "new_password": user.get("password")
            },
        }
        ]
        url = self.base_url + "/v3/customers"
        resp = self.session.get(url, headers=self.headers,data=json.dumps(data))
        if resp.status_code !=200:
            return False
        return resp.json()


    def create_order(self,user):
        data=[{
            "customer_id":user.get('user_id'),
            "billing_address": {
                "first_name": "Jane",
                "last_name": "Doe",
                "street_1": "123 Main Street",
                "city": "Austin",
                "state": "Texas",
                "zip": "78751",
                "country": "United States",
                "country_iso2": "US",
                "email": "janedoe@example.com"
            },
            "products":
                {
                    "name": "BigCommerce Poster",
                    "quantity": 1,
                    "price_inc_tax": 10.9
                },
        }]

        url = self.base_url + "/v2/orders"
        resp = self.session.get(url, headers=self.headers, data=json.dumps(data))
        if resp.status_code != 200:
            return False
        return resp.json()


