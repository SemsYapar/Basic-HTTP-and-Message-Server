# Basic-HTTP-and-Message-Server
Basic HTTP and Message Server(TÜRKÇE)


Server'ı kendi local ip nize göre düzenleyin ve çalıştırın http istekleri için 80, Server aracılığıyla Client ile mesajlaşmak içinse 8888 portunu giriniz

Kullanım:

http server ı seçtiyseniz kulandığınız tarayıcı dan local ağınıza bağlandığınızda (örnek: http://192.168.1.33) kodun içindeki HTTPServer class ından belirlediğiniz status codları, header ve bodyleri görebilirsiniz ön tanımlı olarak girerseniz ekranınıza "Hİ Man Whats Up" yazıcaktır

mesajlaşma hizmeti bir echo server gibi çalışıyor önce serverdan 8888 portunu istiyoruz ardından Client ile Server a bağlanıyoruz(Client ve Server in ön tanımlı ip ayarları bilgisiyarınızın local ip sine göre belirlenmeli) tebrikler.. artık cmd üzerinden Server ile mesajlaşabilirsiniz eğer Client i başka bir bilgisiyardan çalıştırıcaksanız iki bilgisiyaran da aynı ağ üzerinde olmasına dikkat edin yoksa bağlanamassınız

Yapamadıklarım:
Server ımda iki hizmetide yani http ve mesajlaşma hizmetini aynı anda nasıl çalıştıracağımı bilmiyorum o yüzden başta ya 80 portu ile http serverına bağlanıyorsunuz yada 8888 portu ile Client den mesaj alabiliyorsunuz. Bu konuda yapabileceğim bir şey varsa nütfen belirtmeyi unutmayın.

SON: kodumda bolca saçma tanımlamalar ve gereksiz detaylar bulursunuz, bulucaksınız yeni öğreniyorum bunu paylaşma nedenim hocalarımdan fikir alıp daha iyi adımlar atabilmek server ımı geliştirmek kodu basitleştirmek bu yüzden nütfen güzel yorumlarınızı benden esirgemeyin sağolun var olun teşekkürler iyi forumlar..
