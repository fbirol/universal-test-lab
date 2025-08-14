import os
import subprocess
import sys
import time

import pytest
from playwright.sync_api import sync_playwright

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.main import Record, app, db
from tests.factories import fake_record

# DB dosyasının yolunu sabit tut
DB_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), "..", "app", "instance", "universal_test_lab.db"
    )
)


@pytest.fixture(scope="session", autouse=True)
def setup_test_db():
    # TEST BAŞLANGICINDA SADECE BİR KEZ sil-seed-yap
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    with app.app_context():
        db.create_all()
        db.session.add(Record(name="Ali Veli", email="ali@example.com"))
        db.session.add(Record(name="Fatma Yılmaz", email="fatma@example.com"))
        db.session.commit()


@pytest.fixture(scope="session", autouse=True)
def start_flask():
    # Test boyunca TEK sefer Flask sunucusu aç
    proc = subprocess.Popen(["python", "app/main.py"])
    time.sleep(2)  # Açılması için zaman ver
    yield
    proc.terminate()
    proc.wait()


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()


@pytest.fixture
def context():
    return {}


@pytest.fixture()
def client_and_records():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    added_records = []
    with app.app_context():
        db.create_all()
        for _ in range(2):
            rec = fake_record()
            record_obj = Record(**rec)
            db.session.add(record_obj)
            db.session.commit()
            added_records.append(record_obj)
        with app.test_client() as client:
            yield client, added_records
