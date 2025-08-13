Feature: Listeleme ekranı

    Scenario: Giriş sonrası dinamik kayıt ile kayıt listesi görüntülenir
        Given login ekranındayım
        When kullanıcı adı ve şifre doğru girilir
        When dinamik bir kullanıcı eklerim
        Then sayfa başlığı "Kayıt Listesi" olan bir ekranı görürüm
        And listede o kullanıcı görünür