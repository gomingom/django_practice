import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class NewVisitorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get("http://localhost:8000/lists")

        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), '작업 아이템 입력',)

        inputbox.send_keys('공작깃털 사기')

        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertTrue(
            any(row.text == '1: 공작깃털 사기' for row in rows), "신규 작업이 테이블에 표시되지 않는다.")
        self.fail("Finish the test!")


if __name__ == "__main__":
    unittest.main(warnings="ignore")


browser = webdriver.Chrome()
browser.get("http://127.0.0.1:8000")

assert "Congratulations" in browser.title
