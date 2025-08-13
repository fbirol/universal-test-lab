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

scenarios('../features/delete.feature')


@given("login ekranındayım")
def go_to_login(page):
    login_page = LoginPage(page)
    login_page.navigate()

@when("kullanıcı adı ve şifre doğru girilir")
def valid_login(page):
    login_page = LoginPage(page)
    login_page.login("furkan", "1234")

@when("bir kayıt eklerim", target_fixture="eklenen_kayit")
def bir_kayit_eklerim(page, context):
    name = fake.name()
    email = fake.email()
    context["delete_name"] = name
    context["delete_email"] = email
    page.click('a[href="/add"]')
    add_page = AddPage(page)
    add_page.add_new_record(name, email)
    return name

@then('listede kayıt bulunur')
def kayit_var_mi(page, context):
    name = context["delete_name"]
    list_page = ListPage(page)
    rows = ''.join(list_page.get_table_rows())
    assert name in rows

@when('kaydı silerim')
def kaydi_sil(page, context):
    name = context["delete_name"]
    list_page = ListPage(page)
    list_page.delete_record(name)

@then('listede kayıt bulunmaz')
def kayit_yok(page, context):
    name = context["delete_name"]
    list_page = ListPage(page)
    rows = ''.join(list_page.get_table_rows())
    assert name not in rows