# ElectricSuppliesInfosAPI
Get and provide information about the prices, information and other about Portugal Electric Supplies Stores products.

# How to use

1. Run the main.py to start the server
2. Go to the host link indicated in the console and change the URL to get the information about the products.

# Catalogs

Replace the `<id>` with the product reference what you want to search.<br>
Example: http://localhost:5000/efapel/37550%20kbr <br>
Note: Use the URL identity to use spaces if needed. In the example above '%20' is a space.

- /legrand/`<id>`
- /efapel/`<id>`

# About

## Used libraries

- Selenium
  - To download and scrap the products information from the websites.
- Flask
  - To create the RestfulAPI.