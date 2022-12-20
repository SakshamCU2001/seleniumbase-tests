
from page_objects.home_page import HomePage
class HomeTest(HomePage):
    def setUp(self):
        super().setUp()
        print("Running Before each case")
        #login 
        self.open("https://practice.automationbro.com/my-account/")
        self.add_text("#username","testuser420")
        self.add_text("#password","testuser123@")
        self.click("button[name=login]")
        self.assert_text("Log out",".woocommerce-MyAccount-content a[href*=logout]")
        #open home page
        
        self.open_page()

    def tearDown(self):
        print("Running After each case")
        self.open("https://practice.automationbro.com/my-account/")
        self.click(".woocommerce-MyAccount-content a[href*=logout]")
        self.assert_element_visible("button[name=login]")
        super().tearDown()


    def test_home_page(self):
        #open home page
        
        # assert page title
        self.assert_title("Practice E-Commerce Site – Automation Bro")
        # # assert logo
        self.assert_element(HomePage.logo_icon)
        #click on the get started button and assert the url
        self.click(HomePage.get_started_btn) 
        get_demo_url=self.get_current_url()
        self.assert_equal(get_demo_url,"https://practice.automationbro.com/#get-started")

        #get the text of the header and assert the value
        self.assert_text("Think different. Make different.",HomePage.heading_text) 

        self.scroll_to_bottom()
        self.assert_text("Copyright © 2020 Automation Bro",HomePage.copyright_text)

    def test_menu_links(self):
        expected_Links=['Home','About','Shop','Blog','Contact','My account','Home','About','Blog','Contact','Support Form']
        menu_links_el=self.find_elements(HomePage.menu_links)
        

        for idx,link_el in enumerate(menu_links_el):
            # print(idx,link_el.text)
            self.assertEqual(expected_Links[idx],link_el.text)
