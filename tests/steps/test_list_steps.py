import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from pytest_bdd import scenarios, given, when, then, parsers
from tests.pages.login_page import LoginPage
from tests.pages.list_page import ListPage

scenarios('../features/list.feature')

@given("login ekranındayım")
def go_to_login(page):
    login_page = LoginPage(page)
    login_page.navigate()

@when("kullanıcı adı ve şifre doğru girilir")
def valid_login(page):
    login_page = LoginPage(page)
    login_page.login("furkan", "1234")

@then(parsers.parse('sayfa başlığı "{title}" olan bir ekranı görürüm'))
def page_header_is(page, title):
    actual = page.locator("h2").inner_text()
    assert actual == title, f'Beklenen başlık "{title}", görünen "{actual}"'

@then(parsers.parse('listede "{kayit}" kaydı bulunur'))
def kayit_var_mi(page, kayit):
    list_page = ListPage(page)
    rows = ''.join(list_page.get_table_rows())  # satırları birleştir
    assert kayit in rows, f'Kayıt "{kayit}" tablo satırlarında yok!'