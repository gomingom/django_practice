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

        # self.assertIn("To-Do", self.browser.title)
        # header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        # self.assertIn("To-Do", header_text)
        # 엔터키를 치면 페이지가 갱신되고 작업 목록에
        # "1. 공작깃털 사기" 아이템이 추가된다
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        inputbox.send_keys("공작깃털 사기")
        inputbox.send_keys(Keys.ENTER)
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, "/lists/.+")
        self.check_for_row_in_list_table("1: 공작깃털 사기")

        # 추가 아이템을 입력할 수 있는 여분의 텍스트 상자가 존재한다
        # 다시 "공작깃털을 이용해서 그물 만들기"라고 입력한다
        # inputbox = self.browser.find_elemnt(By.ID, "id_new_item")
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        inputbox.send_keys("공작깃털을 이용해서 그물 만들기")
        inputbox.send_keys(Keys.ENTER)

        # 페이지가 다시 갱신되고, 두 개 아이템이 목록에 보인다
        self.check_for_row_in_list_table("2: 공작깃털을 이용해서 그물 만들기")
        self.check_for_row_in_list_table("1: 공작깃털 사기")

        # 새로운 사용자인 프란시스가 사이트에 접속한다.

        ## 새로운 브라우저 세션을 이용해서 에디슨의 정보가
        ## 쿠키를 통해 유입되는 것을 방지한다.
        self.browser.quit()
        self.browser = webdriver.Chrome()

        # 프란시스가 홈페이지에 접속한다.
        # 에디스의 리스트는 보이지 않는다
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element(By.TAG_NAME, "body").text
        self.assertNotIn("공작깃털 사기", page_text)
        self.assertNotIn("그물 만들기", page_text)

        # 프란시스가 새로운 작업 아이템을 입력하기 시작했다
        # 그는 에디스보다 재미가 없다
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        inputbox.send_keys("우유 사기")
        inputbox.send_keys(Keys.ENTER)

        # 프란시스가 전용 URL을 취득한다
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, "/lists/.+")
        self.assertNotEqual(francis_list_url, edith_list_url)

        # 에디스가 입력한 흔적이 없다는 것을 다시 확인 한다
        page_text = self.browser.find_element(By.TAG_NAME, "body").text
        self.assertNotIn("공작깃털 사기", page_text)
        self.assertIn("우유 사기", page_text)
