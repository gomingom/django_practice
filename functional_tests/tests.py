from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class NewVisitorTest(LiveServerTestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self) -> None:
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get(self.live_server_url)

        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("To-Do", header_text)
        # 엔터키를 치면 페이지가 갱신되고 작업 목록에
        # "1. 공작깃털 사기" 아이템이 추가된다
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        inputbox.send_keys("공작깃털 사기")
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table("1: 공작깃털 사기")

        # 추가 아이템을 입력할 수 있는 여분의 텍스트 상자가 존재한다
        # 다시 "공작깃털을 이용해서 그물 만들기"라고 입력한다
        # inputbox = self.browser.find_elemnt(By.ID, "id_new_item")
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        inputbox.send_keys("공작깃털을 이용해서 그물 만들기")
        inputbox.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table("2: 공작깃털을 이용해서 그물 만들기")
        self.check_for_row_in_list_table("1: 공작깃털 사기")
        self.fail("Finish the test!")
