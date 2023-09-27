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
  
## FOR ENGLISH


# Project Name: Raspberry OCR Application
Rasp.py:
  -This project is written for Raspberry Pi and includes an application that captures photos with a USB camera when required, performs optical character recognition (OCR) using Google 
  Cloud Vision service to extract text from images, and sends the output data to an API. This allows you to identify, extract, and process text from images.
Cloud_ocr.py:
  -This project includes an application that performs text extraction from images using Google Cloud Vision service.
  Sample images will be uploaded shortly.
Features:
  Text Extraction from Images: Thanks to the Google Cloud Vision API, you can automatically detect and obtain text data from the images you upload.
  Text Processing: You can optionally edit, analyze, or convert the obtained text data into different formats.
# Getting Started:
  These steps include what is needed to run the project in your local development environment.

# Requirements: You need the following requirements to run the project:

  - Google Cloud account and project creation
  - Python 3.7.0
  - To install the required libraries: pip install google-cloud-vision, pip install time , pip install opencv-python, pip install opencv-python, pip install os
  - Google Cloud API Setup:

  - Go to the Google Cloud Console and create a new project.
  - On the project page, enable the Cloud Vision API.
  - Create your service account key and download it in JSON format.
# Project Setup:

  - Add your service account key to the file in the project's root directory.
# Running the Project:

  - Open a terminal and navigate to the project's root directory.
  - To run the application: python cloud_ocr.py




