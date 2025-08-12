Feature: Kayıt ekleme

    Scenario: Kullanıcı yeni kayıt ekler ve kayıt listesinde görüntüler
        Given login ekranındayım
        When kullanıcı adı ve şifre doğru girilir
        And "Yeni Kayıt Ekle" bağlantısına tıklarım
        And isim olarak "Mehmet Tester" ve e-posta olarak "mehmet@test.com" girerim ve kaydederim
        Then kayıt listesi ekranda görüntülenir
        And listede "Mehmet Tester" kaydı bulunur

    Scenario: Kullanıcı eksik bilgiyle kayıt eklemeye çalışınca uyarı alır
        Given login ekranındayım
        When kullanıcı adı ve şifre doğru girilir
        And "Yeni Kayıt Ekle" bağlantısına tıklarım
        And isim olarak "" ve e-posta olarak "" girerim ve kaydederim
        Then uyarı mesajı "İsim ve e-posta zorunlu!" gösterilir