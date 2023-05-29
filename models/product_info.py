from flask import jsonify


class ProductInfo:
    """
    Represents the information about a product.

    It has the information about a product.
    """
    def __init__(self, reference, name, price):
        """
        Initializes the product attributes.

        Args:
            name: Name of the product.
            price: Price of the product.
        """
        self.reference = reference
        self.name = name
        self.price = price

    def print_info(self):
        """
        Prints the information about this product in the console.

        Shows the attributes of the product.
        """
        print("-------------------------")
        print(f"Reference: {self.reference}\nName: {self.name}\nPrice: {self.price}")
        print("-------------------------")

    def to_json(self):
        """
        Creates a JSON with the information of the products.

        Create and returns a JSON with the attributes of the products.

        Returns:
            JSON object with the information of the product.
        """
        product_info = {
            "reference": self.reference,
            "name": self.name,
            "price": self.price
        }

        return jsonify(product_info)
