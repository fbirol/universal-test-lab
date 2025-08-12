from playwright.sync_api import Page

class ListPage:
    def __init__(self, page: Page):
        self.page = page

    def is_on_list_page(self):
        return self.page.url.endswith("/list")

    def get_table_rows(self):
        return self.page.locator("table tr").all_inner_texts()
    
    def delete_record(self, name):
        # Kaydın adını bul ve aynı satırdaki Sil butonuna tıkla
        rows = self.page.locator('table tr')
        for i in range(rows.count()):
            row_text = rows.nth(i).inner_text()
            if name in row_text:
                self.page.locator(f'table tr:nth-child({i+1}) button').click()
                break