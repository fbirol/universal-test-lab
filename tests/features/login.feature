Feature: Login Screen

    Scenario: Kullanıcı doğru bilgiyle giriş yaparsa ana sayfaya ulaşır
        Given login ekranındayım
        When kullanıcı adı ve şifre doğru girilir
        Then ana sayfa mesajını görürüm

    Scenario: Kullanıcı hatalı şifreyle giriş denediğinde uyarı alır
        Given login ekranındayım
        When kullanıcı adı "furkan" ve yanlış şifre girilir
        Then giriş başarısız uyarısı görürüm