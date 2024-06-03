import json
def read_json_file(file_path):
    import json
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"{file_path} bulunamadı.")
        return None
    except json.JSONDecodeError:
        print(f"{file_path} geçerli bir JSON dosyası değil.")
        return None
    
def write_json_file(file_path, data):
    import json
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)
def json_dogrula():
    json_file_path = './config.json'
    json_data = read_json_file(json_file_path)

    if json_data and isinstance(json_data, list) and json_data:
        # JSON dosyası boş değil ve bir liste içeriyorsa devam et
        ajson_school = json_data[0].get("school")
        ajson_class = json_data[0].get("class")

        if ajson_school == "none" or ajson_school is None:

            # Okul adı "none" veya boşsa, kullanıcıdan yeni değerleri al
            newschool = input(str("Okul Adı: "))
            newclass = input(str("Sınıf Numarası: "))
            ajson_school = newschool
            ajson_class = newclass
            new_data = {'school': newschool, 'class': newclass}
            write_json_file(json_file_path, [new_data])  # yeni veriyi listeye eklemeyi unutmayın
            return new_data
        else:
            return json_data[0]

    else:
        print("JSON verileri alınamadı veya geçersiz.")
        return None
    
deger = json_dogrula()