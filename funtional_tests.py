from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8020')

        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish Test')

        # A user is invited to enter a do-do item straight away

        # A user types "buy peacock feathers into a text box (Edith's hobby is tying  fly-fishing luers)

        # When she hits enter, the page updates, and now the page lists "1: Buy peacock feathers" as an item in a to-do list

        # There is still a text box inviting her to add another item.  She enters "Use peacokc feathers to make a fly"

        # The page updates again, and now shows both items on her list

        # A user wonders wheather the site will remember her list.  Then she sees that the site has generated a unique URL

        # The user visits that URL - to-do list is still there

if __name__ == '__main__':
    unittest.main(warnings='ignore')