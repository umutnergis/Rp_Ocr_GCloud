# Proje Adı: Raspberry OCR Uygulaması
Rasp.py:
  -Bu proje, Raspberry pi için yazılmış olup istenilen durum olduğunda usb kamera ile fotoğraf çekip Google Cloud Vision hizmetini kullanarak görüntülerden metin çıkarma (OCR) işlemi      gerçekleştiren ve çıktı bilgisini api'a gönderen bir uygulamayı içerir. Bu sayede görüntülerdeki metinleri tanımlayabilir, çıkarabilir ve işleyebilirsiniz.
Cloud_ocr.py:
  -Bu proje Google Cloud Vision hizmetini kullanarak görüntülerden metin çıkarma işlemi gerçekleştiren uygulamayı içerir.
Örnek görüntü kısa sürede yüklenecek.

## Özellikler

- Görüntülerden metin çıkarma: Google Cloud Vision API sayesinde, yüklediğiniz görüntülerdeki metinleri otomatik olarak algılayabilir ve metin verisini elde edebilirsiniz.
- Metin İşleme: Elde edilen metin verisini isteğe bağlı olarak düzenleyebilir, analiz edebilir veya farklı formatlara dönüştürebilirsiniz.

## Başlangıç

Bu adımlar, projeyi yerel geliştirme ortamınızda çalıştırmak için gerekenleri içerir.

1. **Gereksinimler**: Projenin çalıştırılması için aşağıdaki gereksinimlere ihtiyacınız vardır:
   - Google Cloud hesabı ve proje oluşturma
   - Python 3.7.0
   - Gerekli kütüphaneleri yüklemek için: `pip install google-cloud-vision`, `pip install time `, `pip install opencv-python`, `pip install opencv-python`,`pip install os`

2. **Google Cloud API Ayarları**:
   - Google Cloud Console'a gidin ve yeni bir proje oluşturun.
   - Proje sayfasında, Cloud Vision API'yi etkinleştirin.
   - Hesap anahtarınızı oluşturun ve JSON formatında indirin.

3. **Proje Ayarları**:
   - Projenin ana dizininde bulunan dosyaya hesap anahtarınızı ekleyin.

4. **Projeyi Çalıştırma**:
   - Terminali açın ve projenin ana dizinine gidin.
   - Uygulamayı çalıştırmak için: `python cloud_ocr.py`




