import os
import sys
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from playwright.sync_api import sync_playwright
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from tests.pages.login_page import LoginPage

scenarios('../features/login.feature')

@given("login ekranındayım")
def go_to_login(page):
    login_page = LoginPage(page)
    login_page.navigate()

@when("kullanıcı adı ve şifre doğru girilir")
def valid_login(page):
    login_page = LoginPage(page)
    login_page.login("furkan", "1234")

@then("ana sayfa mesajını görürüm")
def see_home(page):
    assert page.locator("h2").inner_text() == "Merhaba, başarılı giriş yaptınız!"

@when(parsers.parse('kullanıcı adı "{username}" ve yanlış şifre girilir'))
def invalid_login(page, username):
    login_page = LoginPage(page)
    login_page.login(username, "yanlis_sifre")  # Bilerek yanlış şifre

@then("giriş başarısız uyarısı görürüm")
def fail_message_shown(page):
    login_page = LoginPage(page)
    assert "Kullanıcı adı veya şifre yanlış!" in login_page.get_error_message()