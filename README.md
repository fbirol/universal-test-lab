# 🚀 Universal Test Lab

Universal Test Lab, modern yazılım projeleri için uçtan uca test otomasyonu, CI/CD entegrasyonu ve dinamik test veri yönetimi sağlar.  
Backend ve UI test otomasyonunu, kapsamlı raporlama ve statik kod analiz araçlarıyla birleştirerek kurum ölçeğinde QA süreçlerini hızlandırır ve şeffaf hale getirir.

---

## 🎯 Amaç & Kapsam

- **API ve Web UI testlerinin** tek çatı altında, sürdürülebilir şekilde otomasyonu  
- **CI/CD pipeline ile otomatik test, kalite ve coverage raporlama**  
- **Dinamik & gerçekçi test datası üretimi** (Faker/factory)
- **Kurumsal kod hijyeni:** Black, isort, flake8 ile kod ve import standardizasyonu  
- **BDD (Behaviour Driven Development) ile canlı, anlaşılır ve tekrar edilebilir senaryolar**
- **Gelişmiş Allure raporları ile anlık coverage ve durum takibi**

---

## ✨ Özellikler

- ✅ **Playwright destekli Web UI ve API Otomasyonu**
- ✅ **pytest-bdd ile senaryo tabanlı testler**
- ✅ **Faker ile data-collision’a dayanıklı random test dataları**
- ✅ **Allure ile detaylı test raporlama**
- ✅ **Black, isort, flake8 lint ve code quality enforcement**
- ✅ **CI pipeline badge'leri ve otomatik GitHub Pages'den dashboard yayını**
- ✅ **Kolay genişletilebilir dosya yapısı: API, UI, fixture, steps, factories, pages**

---

## 🚦 Hızlı Başlangıç

### 1. Sanal ortamı başlat  
```bash
.\venv\Scripts\activate
```

### 2. Backend (Flask) app’i çalıştır  
```bash
cd app
python main.py
```

### 3. Test otomasyonuna geç  
```bash
cd ..
pytest --alluredir=allure-results
```

### 4. Allure ile raporu aç  
```bash
allure serve allure-results
```

---

## 🧹 Kod Standardizasyonu Komutları

Her push/pull öncesi kodunu temizle:

```bash
black .
isort .
flake8 .
```

---

## 🧑‍💻 Kullanım & Senaryo Örnekleri

- `tests/steps/`: BDD step definitions, dinamik faker verisiyle
- `tests/pages/`: Playwright page object’leri
- `tests/factories.py`: Test veri üretimi
- `tests/conftest.py`: fixture ve context yönetimi

Örnek:  
`pytest --alluredir=allure-results` ile tüm testler,  
`allure serve allure-results` ile detaylı coverage raporu!

---

    
# QA Reports and Dashboards

- [Dashboard](https://fbirol.github.io/universal-test-lab/index.html)  
- [Allure Functional Test Report](https://fbirol.github.io/universal-test-lab/allure-report/index.html)  
- [Locust Performance Test Report](https://fbirol.github.io/universal-test-lab/locust-report.html)
[![codecov](https://codecov.io/gh/fbirol/universal-test-lab/branch/main/graph/badge.svg)](https://codecov.io/gh/fbirol/universal-test-lab)

## 🛠️ TODO

- [ ] Gelişmiş Load & Performance Testleri (Locust, k6 entegrasyonu)
- [ ] Mock ve stub destekli servis bağımlılıkları izolasyonu
- [ ] Versiyonlanmış test dataları ve reusable scenario templates
- [ ] Projenin Github Actions üzerinden auto-deploy, tag badge (passing, coverage) ekleme
- [ ] Manuel run / pipeline run share link entegrasyonu

---

## ☕ Seni Yormadıysak Bir Kahveni Alırız…

Projeye katkı, öneri veya kahve desteğiyle gelişimine ortak olabilirsin!

[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-%23FFDD00.svg?&style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/fbirol)

---

**Universal Test Lab:**  
Daha sürdürülebilir, daha profesyonel ve en temiz test otomasyonu için!