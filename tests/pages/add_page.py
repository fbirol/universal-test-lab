from playwright.sync_api import Page


class AddPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto("http://127.0.0.1:5000/add")

    def add_new_record(self, name, email):
        self.page.fill('input[name="name"]', name)
        self.page.fill('input[name="email"]', email)
        self.page.click('button[type="submit"]')

    def get_error_message(self):
        return self.page.locator("p").inner_text()
