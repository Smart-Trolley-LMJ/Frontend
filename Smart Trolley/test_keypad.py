class Success:
    def __init__(self, change_user_id_func):
        self.change_user_id_func = change_user_id_func
        self.update_cart_user_id("Lorenzo")

    def update_cart_user_id(self, new_user_id):
        self.change_user_id_func(new_user_id)


class Cart:
    def __init__(self, user_id):
        self.user_id = user_id
        # Instantiate the Success class and pass the change_user_id method
        self.success = Success(self.change_user_id)

    def change_user_id(self, new_user_id):
        self.user_id = new_user_id


# Example usage:
if __name__ == "__main__":
    cart = Cart(user_id="user123")

    print("Original User ID in Cart:", cart.user_id)
    cart.success.update_cart_user_id(new_user_id="new_user456")
    print("Updated User ID in Cart:", cart.user_id)
