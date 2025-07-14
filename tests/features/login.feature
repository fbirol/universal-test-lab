Feature: Login Screen

    Scenario: Kullanıcı doğru bilgiyle giriş yaparsa ana sayfaya ulaşır
        Given login ekranındayım
        When kullanıcı adı ve şifre doğru girilir
        Then sayfa başlığı "Kayıt Listesi" olan bir ekranı görürüm

    Scenario: Kullanıcı hatalı şifreyle giriş denediğinde uyarı alır
        Given login ekranındayım
        When kullanıcı adı "furkan" ve yanlış şifre girilir
        Then uyarı mesajı "Kullanıcı adı veya şifre yanlış!" gösterilir