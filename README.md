# YouTube Video Summary Generator

Bu Python scripti, verilen bir YouTube videosunun altyazılarını alır ve Groq API kullanarak kısa ve açıklayıcı bir özet oluşturur.

## Özellikler
- YouTube videosunun altyazılarını otomatik olarak alır.
- Groq API ile metin analizini gerçekleştirir ve özet oluşturur.

## Gereksinimler
Bu scriptin çalışması için aşağıdaki kütüphanelerin yüklü olması gerekmektedir:

```sh
pip install groq youtube-transcript-api
```

Ayrıca [Groq API](https://console.groq.com/keys) oluşturmanız gerekmektedir.

## Kullanım
1. Scripti çalıştırın:
   ```sh
   python main.py
   ```
2. Video linkini girin.
3. Script, altyazıları alıp Groq API'ye göndererek özet döndürecektir.

## Yapılandırma
- `API_KEY` değişkenini kendi Groq API anahtarınızla değiştirin.

## Örnek Çalıştırma
```sh
Video linki: https://www.youtube.com/watch?v=abcd1234
Özet: Bu video XYZ konusunu ele alıyor ve temel noktaları şunlardır...
```

