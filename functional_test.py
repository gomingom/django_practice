import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get("http://localhost:8000/users")

        self.assertIn("To-Do", self.browser.title)
        self.fail("Finish the test!")


if __name__ == "__main__":
    unittest.main(warnings="ignore")


browser = webdriver.Chrome()
browser.get("http://127.0.0.1:8000")

assert "Congratulations" in browser.title
