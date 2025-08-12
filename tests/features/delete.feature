Feature: Kayıt silme

    Scenario: Kullanıcı listeden bir kaydı siler
        Given login ekranındayım
        When kullanıcı adı ve şifre doğru girilir
        Then listede "Ali Veli" kaydı bulunur
        When "Ali Veli" kaydını silerim
        Then listede "Ali Veli" kaydı bulunmaz