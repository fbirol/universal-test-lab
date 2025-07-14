from playwright.sync_api import Page

class ListPage:
    def __init__(self, page: Page):
        self.page = page

    def is_on_list_page(self):
        return self.page.url.endswith("/list")

    def get_table_rows(self):
        return self.page.locator("table tr").all_inner_texts()