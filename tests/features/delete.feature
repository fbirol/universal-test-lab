Feature: Kayıt silme

    Scenario: Kullanıcı dinamik bir kaydı ekler ve siler
        Given login ekranındayım
        When kullanıcı adı ve şifre doğru girilir
        When bir kayıt eklerim
        Then listede kayıt bulunur
        When kaydı silerim
        Then listede kayıt bulunmaz