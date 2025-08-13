import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from pytest_bdd import scenarios, given, when, then, parsers
from faker import Faker
import pytest

from tests.pages.login_page import LoginPage
from tests.pages.list_page import ListPage
from tests.pages.add_page import AddPage

fake = Faker()

scenarios('../features/list.feature')


@given("login ekranındayım")
def go_to_login(page):
    login_page = LoginPage(page)
    login_page.navigate()

@when("kullanıcı adı ve şifre doğru girilir")
def valid_login(page):
    login_page = LoginPage(page)
    login_page.login("furkan", "1234")

@when("dinamik bir kullanıcı eklerim")
def dinamik_kullanici_ekle(page, context):
    name = fake.name()
    email = fake.email()
    context["list_name"] = name
    context["list_email"] = email
    page.click('a[href="/add"]')
    add_page = AddPage(page)
    add_page.add_new_record(name, email)

@then(parsers.parse('sayfa başlığı "{title}" olan bir ekranı görürüm'))
def page_header_is(page, title):
    actual = page.locator("h2").inner_text()
    assert actual == title, f'Beklenen başlık "{title}", görünen "{actual}"'

@then("listede o kullanıcı görünür")
def listede_kullanici_var_mi(page, context):
    name = context["list_name"]
    email = context["list_email"]
    list_page = ListPage(page)
    rows = ''.join(list_page.get_table_rows())
    assert name in rows, f"Kayıt '{name}' tablo satırlarında yok!"
    assert email in rows, f"E-posta '{email}' tablo satırlarında yok!"