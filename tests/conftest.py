import os, sys
import pytest
from playwright.sync_api import sync_playwright
import subprocess
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import app, db, Record

# DB dosyasının yolunu sabit tut
DB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "app", "instance", "universal_test_lab.db"))

@pytest.fixture(scope="session", autouse=True)
def setup_test_db():
    # TEST BAŞLANGICINDA SADECE BİR KEZ sil-seed-yap
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    from app.main import app, db, Record
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

@pytest.fixture()
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # her test için memory’de yeni DB!
    with app.app_context():
        db.drop_all()
        db.create_all()
        db.session.add(Record(name="Ali Veli", email="ali@example.com"))
        db.session.add(Record(name="Fatma Yılmaz", email="fatma@example.com"))
        db.session.commit()
        with app.test_client() as client:
            yield client