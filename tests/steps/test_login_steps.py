import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from pytest_bdd import scenarios, given, when, then, parsers
from tests.pages.login_page import LoginPage

scenarios("../features/login.feature")


@given("login ekranındayım")
def go_to_login(page):
    login_page = LoginPage(page)
    login_page.navigate()


@when("kullanıcı adı ve şifre doğru girilir")
def valid_login(page):
    login_page = LoginPage(page)
    login_page.login("furkan", "1234")


@when(parsers.parse('kullanıcı adı "{username}" ve yanlış şifre girilir'))
def invalid_login(page, username):
    login_page = LoginPage(page)
    login_page.login(username, "yanlis_sifre")


@then(parsers.parse('sayfa başlığı "{title}" olan bir ekranı görürüm'))
def page_header_is(page, title):
    actual = page.locator("h2").inner_text()
    assert actual == title, f'Beklenen başlık "{title}", görünen "{actual}"'


@then(parsers.parse('uyarı mesajı "{warning}" gösterilir'))
def warning_message(page, warning):
    login_page = LoginPage(page)
    actual = login_page.get_error_message()
    assert warning in actual, f'Beklenen uyarı "{warning}", görünen "{actual}"'
