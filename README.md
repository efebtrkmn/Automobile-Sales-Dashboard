# Automobile-Sales-Dashboard
IBM Data Analyst/Data Visualization Final Project

Bu proje, Python ve Dash kütüphaneleri kullanılarak geliştirilmiş etkileşimli bir veri görselleştirme panosudur. **IBM Data Analyst/Data Visualization Final Project** programı kapsamında bitirme projesi olarak geliştirilmiştir.

Kullanıcılar, otomobil satış verilerini yıllık bazda veya ekonomik durgunluk (resesyon) dönemlerine göre filtreleyerek analiz edebilirler.

## 🚀 Özellikler

Proje iki ana analiz modu sunar:

### 1. Yıllık İstatistikler (Yearly Statistics)
* 📅 **Yıllık Satış Trendi:** Yıllara göre toplam otomobil satışlarının değişimi.
* 📊 **Aylık Satışlar:** Seçilen yıla ait aylık satış performansı.
* 🚙 **Araç Tipine Göre Satış:** Hangi araç türünün (SUV, Sedan vb.) ne kadar sattığı.
* 📢 **Reklam Harcamaları:** Araç türlerine göre reklam bütçesi dağılımı.

### 2. Resesyon Dönemi İstatistikleri (Recession Period Statistics)
* 📉 **Satış Dalgalanmaları:** Ekonomik durgunluk dönemlerindeki satış hareketleri.
* 💰 **Fiyat ve Satış İlişkisi:** Araç fiyatları ile satış hacmi arasındaki korelasyon (Scatter Plot).
* 🏗️ **İşsizlik Etkisi:** İşsizlik oranlarının araç satışlarına etkisi.
* ❄️ **Mevsimsellik:** Mevsimlerin satışlar üzerindeki etkisinin analizi (Bubble Plot).

## 🛠️ Kullanılan Teknolojiler

* **Dil:** Python 3.8
* **Arayüz:** [Dash](https://dash.plotly.com/) (Web Framework)
* **Görselleştirme:** [Plotly Express](https://plotly.com/python/plotly-express/)
* **Veri İşleme:** Pandas

## 📊 Ekran Görüntüleri

![Dashboard Genel Görünüm](screenshots/dashboard-yearly.png)

## ⚙️ Kurulum ve Çalıştırma

Bu projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin:

1.  **Repoyu klonlayın:**
    ```bash
    git clone [https://github.com/efebtrkmn/Automobile-Sales-Dashboard.git](https://github.com/efebtrkmn/Automobile-Sales-Dashboard.git)
    cd Automobile-Sales-Dashboard
    ```

2.  **Gerekli kütüphaneleri yükleyin:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Eğer requirements.txt dosyanız yoksa manuel olarak: `pip install dash pandas plotly`)*

3.  **Uygulamayı başlatın:**
    ```bash
    python Automobile-Project.py
    ```

4.  **Tarayıcıda görüntüleyin:**
    Terminalde çıkan linke tıklayın veya tarayıcınıza şunu yazın:
    `http://127.0.0.1:8050/`

## 📝 Lisans ve Teşekkür

Bu proje eğitim amaçlı geliştirilmiştir. Veri seti ve proje şablonu IBM Skills Network tarafından sağlanmıştır.
