import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from pytest_bdd import scenarios, given, when, then, parsers
from tests.pages.login_page import LoginPage
from tests.pages.list_page import ListPage

scenarios('../features/delete.feature')

@given("login ekranındayım")
def go_to_login(page):
    login_page = LoginPage(page)
    login_page.navigate()

@when("kullanıcı adı ve şifre doğru girilir")
def valid_login(page):
    login_page = LoginPage(page)
    login_page.login("furkan", "1234")

@then(parsers.parse('listede "{kayit}" kaydı bulunur'))
def kayit_var_mi(page, kayit):
    page.goto("http://127.0.0.1:5000/list")  # Refresh!
    list_page = ListPage(page)
    rows = ''.join(list_page.get_table_rows())
    print("DEBUG-list rows: ", rows)
    assert kayit in rows, f'Kayıt "{kayit}" tablo satırlarında yok!'

@when(parsers.parse('"{kayit}" kaydını silerim'))
def kaydi_sil(page, kayit):
    list_page = ListPage(page)
    list_page.delete_record(kayit)

@then(parsers.parse('listede "{kayit}" kaydı bulunmaz'))
def kayit_yok(page, kayit):
    list_page = ListPage(page)
    rows = ''.join(list_page.get_table_rows())
    assert kayit not in rows
