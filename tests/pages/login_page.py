from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto("http://127.0.0.1:5000/login")  # or use custom port

    def login(self, username, password):
        self.page.fill('input[name="username"]', username)
        self.page.fill('input[name="password"]', password)
        self.page.click('button[type="submit"]')

    def get_error_message(self):
        return self.page.locator("p").inner_text()
