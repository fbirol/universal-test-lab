Feature: Listeleme ekranı

    Scenario: Giriş sonrası kayıt listesi görüntülenir
        Given login ekranındayım
        When kullanıcı adı ve şifre doğru girilir
        Then sayfa başlığı "Kayıt Listesi" olan bir ekranı görürüm
        And listede "Ali Veli" kaydı bulunur