import sys
import os
import re
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from pytest_bdd import scenarios, given, when, then, parsers
from tests.pages.login_page import LoginPage
from tests.pages.list_page import ListPage
from tests.pages.add_page import AddPage

scenarios('../features/add.feature')

@given("login ekranındayım")
def go_to_login(page):
    login_page = LoginPage(page)
    login_page.navigate()

@when("kullanıcı adı ve şifre doğru girilir")
def valid_login(page):
    login_page = LoginPage(page)
    login_page.login("furkan", "1234")

@when(parsers.parse('"{link}" bağlantısına tıklarım'))
def click_add_link(page, link):
    page.click('a[href="/add"]')

@when(parsers.re(r'isim olarak "(?P<name>.*)" ve e-posta olarak "(?P<email>.*)" girerim ve kaydederim'))
def add_record(page, name, email):
    from tests.pages.add_page import AddPage
    add_page = AddPage(page)
    add_page.add_new_record(name, email)

@then(parsers.parse('uyarı mesajı "{warning}" gösterilir'))
def warning_message(page, warning):
    locator = page.locator('p')
    try:
        locator.wait_for(state="visible", timeout=2000)
        text = locator.inner_text()
    except:
        text = ""
    assert warning in text, f'Beklenen uyarı "{warning}", görünen "{text}"'

@then("kayıt listesi ekranda görüntülenir")
def see_list(page):
    list_page = ListPage(page)
    assert list_page.is_on_list_page()

@then(parsers.parse('listede "{kayit}" kaydı bulunur'))
def kayit_var_mi(page, kayit):
    list_page = ListPage(page)
    rows = ''.join(list_page.get_table_rows())
    assert kayit in rows, f'Kayıt "{kayit}" tablo satırlarında yok!'