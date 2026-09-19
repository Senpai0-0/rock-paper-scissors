import random

# 1. Seçenekleri tanımlıyoruz
secenekler = ["tas", "kagit", "makas"]

# 2. Hangi seçim hangisini yener? (anahtar, değeri yener)
kim_kimi_yener = {
    "tas": "makas",     # taş, makası yener
    "makas": "kagit",   # makas, kağıdı yener
    "kagit": "tas"      # kağıt, taşı yener
}


def bilgisayar_secimi():
    """Bilgisayar rastgele bir seçim yapar."""
    return random.choice(secenekler)


def kazanani_belirle(oyuncu, bilgisayar):
    """İki seçimi karşılaştırıp sonucu döndürür."""
    if oyuncu == bilgisayar:
        return "Berabere!"
    elif kim_kimi_yener[oyuncu] == bilgisayar:
        return "Kazandın!"
    else:
        return "Bilgisayar kazandı!"


def oyunu_oyna():
    print("=== TAŞ KAĞIT MAKAS ===")
    print("Seçenekler: tas, kagit, makas (çıkmak için 'q')\n")

    while True:
        oyuncu = input("Seçimin: ").lower().strip()

        if oyuncu == "q":
            print("Oyun bitti, görüşürüz!")
            break

        # Geçersiz girdi kontrolü
        if oyuncu not in secenekler:
            print("Geçersiz seçim! Lütfen tas, kagit veya makas yaz.\n")
            continue

        bilgisayar = bilgisayar_secimi()
        sonuc = kazanani_belirle(oyuncu, bilgisayar)

        print(f"Sen: {oyuncu} | Bilgisayar: {bilgisayar}")
        print(f"Sonuç: {sonuc}\n")


# Programı başlat
if __name__ == "__main__":
    oyunu_oyna()