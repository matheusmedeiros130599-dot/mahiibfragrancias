import os
import urllib.request

base_url = "https://mahibbfragancias.shop/"
images = [
    "images/banner.webp",
    "images/asad-lattafa.jpg",
    "images/attar-al-wesal.jpg",
    "images/sabah-al-ward.jpg",
    "images/fakhar-rose.jpg",
    "images/yara-lattafa.jpg",
    "images/fakhar-black.jpg",
    "images/club-de-nuit-intense.jpg",
    "images/royal-amber.jpg",
    "images/bareeq-al-dhahab.jpg",
    "images/shagaf-al-ward.jpg",
    "images/reviews/review-1.jpg",
    "images/reviews/review-2.jpg",
    "images/reviews/review-3.jpg",
    "images/reviews/review-4.jpg",
    "images/reviews/review-5.jpg",
    "images/reviews/review-6.jpg",
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

for img_path in images:
    url = base_url + img_path
    local_path = os.path.join(os.path.dirname(__file__), img_path)
    
    # Certifica-se de que a pasta existe
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    
    print(f"Baixando {url} para {local_path}...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            with open(local_path, 'wb') as out_file:
                out_file.write(response.read())
        print("Sucesso.")
    except Exception as e:
        print(f"Erro ao baixar {img_path}: {e}")
