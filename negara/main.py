from countries import restcountries

def get_user_input():
    country_code = input("Masukkan kode negara (contoh: usa): ")
    return country_code

def main():
    rest_countries_api = restcountries()

    # Mendapatkan input dari pengguna
    country_code = get_user_input()

    # Memanggil fungsi untuk mendapatkan informasi negara berdasarkan kode negara
    country_info = rest_countries_api.get_country_info(country_code)
    
    if "error" in country_info:
        print(country_info["error"])
    else:
        print(f"Informasi Negara untuk {country_code.upper()}:")
        print(country_info)

if __name__ == "__main__":
    main()