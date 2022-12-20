from seleniumbase import BaseCase

class ContactTest(BaseCase):
    def test_contact_page(self):
        #open page
        self.open("https://practice.automationbro.com/contact")
        #taking screenshot before filling the form
        self.scroll_to("#evf-form-277")
        self.save_screenshot("empty_form","custom screenshot")
        #fill in all the fileds
        self.send_keys('.contact-name input','Tester')
        self.send_keys('.contact-email input','Tester@gmail.com')
        self.send_keys('.contact-phone input','123456789')
        self.send_keys('.contact-message textarea','This is a text message')
        #taking screenshot after filling the form
        self.scroll_to("#evf-form-277")
        self.save_screenshot("filled_screenshot","custom screenshot")


        #click the submit button 
        self.click("#evf-submit-277")

        #verify submit message
        self.assert_text("Thanks for contacting us! We will be in touch with you shortly","div[role=alert]")

         