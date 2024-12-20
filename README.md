# Diyabet Tahmin Arayüzü

Bu proje, diyabet riski tahmini yapmak için geliştirilmiş bir Python uygulamasıdır. Makine öğrenimi modelini kullanarak, kullanıcılardan alınan sağlık verileriyle diyabet riski tahmini yapılır. Kullanıcılar, çeşitli sağlık parametrelerini girerek bu tahmini alabilirler. --> https://huggingface.co/spaces/elfgk/diyabettahmin

## Özellikler

- **Hamilelik sayısı (Pregnancies)**
- **Glikoz seviyesi (Glucose)**
- **İnsülin seviyesi (Insulin)**
- **Vücut Kitle Endeksi (BMI)**
- **Diyabet Soy Ağacı Fonksiyonu (Diabetes Pedigree Function)**
- **Yaş (Age)**

Model, bu girdileri kullanarak diyabetin olup olmadığını tahmin eder.

## Kullanım

### 1. Gerekli Kütüphaneler

Bu projeyi çalıştırmak için aşağıdaki Python kütüphanelerine ihtiyaç vardır:

- `gradio`: Arayüz için
- `joblib`: Model dosyasını yüklemek için
- `scikit-learn`: Makine öğrenimi işlemleri için

Gerekli kütüphaneleri yüklemek için şu komutu kullanabilirsiniz:

```bash
pip install gradio joblib scikit-learn
