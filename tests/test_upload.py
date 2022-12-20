from seleniumbase import BaseCase
from pathlib import Path
    

class UploadTest(BaseCase):

    def test_hidden_upload(self):
        self.open('https://practice.automationbro.com/cart/')

     #get file path

     
        file_path= Path(__file__).resolve().parent.parent/'Data/logo-social.png'
        #adding js code to remove the class which was hiding the input bar
        remove_hidden_class="document.getElementById('upfile_1').classList.remove('file_input_hidden')"
        self.add_js_code(remove_hidden_class)
        self.choose_file("#upfile_1",file_path)

     #click button

        self.click('#upload_1')

     #assert text

        self.assert_text("uploaded successfully","#wfu_messageblock_header_1_label_1")
