from flask import jsonify


class ProductInfo:
    """
    Represents the information about a product.

    It has the information about a product.
    """
    def __init__(self, name, price):
        """
        Initializes the product attributes.

        Args:
            name: Name of the product.
            price: Price of the product.
        """
        self.name = name
        self.price = price

    def print_info(self):
        """
        Prints the information about this product in the console.

        Shows the attributes of the product.
        """
        print(f"{self.name}\n{self.price}")

    def to_json(self):
        """
        Creates a JSON with the information of the products.

        Create and returns a JSON with the attributes of the products.

        Returns:
            JSON object with the information of the product.
        """
        product_info = {
            "name": self.name,
            "price": self.price
        }

        return jsonify(product_info)
