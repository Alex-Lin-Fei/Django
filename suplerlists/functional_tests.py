"""
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from selenium import webdriver


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    browser = webdriver.Firefox()

    # She has heard about a cool new online to-do app. She goes
    # to check out its homepage
    browser.get('http://localhost:8000')

    # She notices the page title and header mention to-do lists
    assert 'To-Do' in browser.title, "Browser title was " + browser.title

    # She is invited to enter a to-do item straight away

    # She types "Buy peacock feathers" into a text box (Edith`s hobby
    # is tying fly-fishing lures

    # when she hits enter, the page updates, and now the page lists
    # "1: Buy peacock feathers" as an item in a to-do list

    # There is still a text box inviting her to add another item. She
    # enters "Use peacock feathers to make a fly" (Edith is very methodical)

    # The page updates again, and now shows both items on her list

    # Edith wonders whether the site will remember her list. The she sees
    # that the site has generated a unique URL for her -- there is some
    # explanatory text to that effect.

    # She visits that URL - her to-do list is still there.

    # Satisfied, she goes back to sleep

    browser.quit()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest, time


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        # self.fail('Finish the test!')
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        # She types "Buy peacock feathers" into a text box (Edith`s hobby
        # is tying fly-fishing lures
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
