import gradio as gr
import joblib


# Modeli yükle
try:
    with open("diyabettahminadaboost.joblib", "rb") as model_file:
      model = joblib.load("diyabettahminadaboost.joblib")
    print("Model başarıyla yüklendi.")  # Başarı mesajı
except FileNotFoundError:
    print("Model dosyası bulunamadı! Lütfen doğru dosya adını ve yolunu kontrol edin.")
    model = None  # Modeli None olarak ayarlayın
except Exception as e:
    print(f"Model yüklenirken bir hata oluştu: {e}")
    model = None  # Modeli None olarak ayarlayın

# Tahmin fonksiyonu
def predict_diabetes(Pregnancies, Glucose, Insulin, BMI, DiabetesPedigreeFunction, Age):
    if model is None:
        return "Model yüklenemedi, tahmin yapılamıyor."
    # Kullanıcıdan alınan verileri özellikler olarak
    features = [[Pregnancies, Glucose, Insulin, BMI, DiabetesPedigreeFunction, Age]]
    prediction = model.predict(features)  # Modelin tahmin yapması
    return f"Diyabet tahmini: {'Pozitif' if prediction[0] == 1 else 'Negatif'}"

# Arayüz
iface = gr.Interface(
    fn=predict_diabetes,
    inputs=[
        gr.Slider(label="Hamilelikler", minimum=0, maximum=20, step=1),
        gr.Slider(label="Glikoz", minimum=0, maximum=200, step=10),
        gr.Slider(label="Insulin", minimum=0, maximum=900, step=10),
        gr.Slider(label="BMI", minimum=0, maximum=70, step=1),
        gr.Slider(label="Diyabet Soy Ağacı ", minimum=0.0, maximum=2.5, step=0.1),
        gr.Slider(label="Yaş", minimum=0, maximum=100, step=1),
    ],
    outputs="text",
    live=True,
    title="Diyabet Tahmin Arayüzü",
    description="Verileri girerek diyabet durumu tahmini yapabilirsiniz."
)

iface.launch(share=True)
