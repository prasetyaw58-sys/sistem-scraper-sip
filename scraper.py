import requests
from bs4 import BeautifulSoup

def run_scraper():
    target_url = "https://jdih.jabarprov.go.id/"
    headers = {"User-Agent": "Mozilla/5.0"}
    print(f"Memeriksa pembaruan dari: {target_url}")

    try:
        response = requests.get(target_url, headers=headers, timeout=15)
        if response.status_code == 200:
            print("Koneksi berhasil! Siap mengekstrak data regulasi.")
        else:
            print(f"Gagal. Status: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_scraper()
