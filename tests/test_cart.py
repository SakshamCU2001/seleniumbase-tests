from page_objects.cart_page import CartPage
from selenium.webdriver.common.keys import Keys
class CartTest(CartPage):
    def setUp(self):
        super().setUp()
        self.open("https://practice.automationbro.com/shop/")
    def test_add_to_cart(self):
        #add item to cart
        self.click(self.converse_add_to_cart_btn)
        # self.click(".tg-icon tg-icon-shopping-cart")
        #assert that prduct is added
        self.assert_text('1',self.cart_count_text)
        self.open_page()

        text=self.get_text(self.subtotal_text)
        print(text)#150$
        #change cart quantity
        self.set_value(self.product_quantity_input,'2')
        self.send_keys(self.product_quantity_input,Keys.RETURN)
        self.click(self.update_cart_btn)
        # self.assert_element_visible(self.loading_overlay)
        # self.assert_element_not_visible(self.loading_overlay)
        self.wait_for_text_visible("$300.00",self.subtotal_text)


        updated_text=self.get_text(self.subtotal_text)
        print(updated_text)
        self.assert_not_equal(text,updated_text)

