#Library
# -*- coding: utf-8 -*-

import importlib
import subprocess
import time


#basic def
#Kontrol listesi
library_list = ["numpy","tkinter","requests","json"]

def check_lib(library_list):
    nalibrary = []

    for library in library_list:
            try:
                importlib.import_module(library)
                print(f"{library} Kütüphanesi \033[92m Mevcut \033[0m")
            except ImportError:
                print(f"\033[91m{library} \033[0m\033[94mKütüphanesi yüklü değil. \033[0m")
                nalibrary.append(library)

    return nalibrary

def lib_download(lists):
    indirilemeyenler = []
    for lib in lists:
        try:
            plib = "python3-"+lib
            subprocess.check_call(["apt-get", "install", plib])
            print(f"{lib} kütüphanesi başarıyla indirildi.")
        except subprocess.CalledProcessError:
            print(f"\033[91m {lib} \033[0m kütüphanesi indirilemedi.")
            indirilemeyenler.append(lib)
        return indirilemeyenler

#gui
    
def start_gui(app_ver,latest_ver):
    import os
    from PIL import Image
    import subprocess
    from getpass import getpass
    import box
    app_version = app_ver
    app = box.App(app_version=app_version,latest_ver=latest_ver)
    app.mainloop()



    


#versiyon kontrol
    
def check_ver(ver,school,schoolclass):
    import requests
    import uuid
    mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(5, -1, -1)])


    api_url = "https://pentascans.com.tr/api/ver.php?data=pardusexe&ver="+str(ver)+"&okul="+str(school)+"&sinif="+str(schoolclass)+"&machine="+str(mac_address)
    
    try:
        # API'ye GET isteği yap
        response = requests.get(api_url)

        # Yanıtın durum kodunu kontrol et
        if response.status_code == 200:
            # JSON formatındaki yanıtı al
            data = response.json()
            
            # API'den alınan en son sürümü kontrol et
            if "message" in data:
                latest_ver = data["latest"]
                message = data["message"]

                
                if message == "guncel":
                    return {"latest": latest_ver, "myver": ver,"message": "guncel"}
                else:
                    return {"latest": latest_ver, "myver": ver,"message": "eski"}
            else:
                print("API yanıtında 'latest' anahtarı bulunamadı.")
                return {"latest": ver, "myver": ver,"message": "API yanıtında 'latest' anahtarı bulunamadı."}

        else:
            print(f"Hata: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Hata: {e}")



#json işlemleri
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
    json_file_path = '../Belgeler/parduspenta/config.json'
    json_data = read_json_file(json_file_path)

    if json_data and isinstance(json_data, list) and json_data:
        # JSON dosyası boş değil ve bir liste içeriyorsa devam et
        ajson_school = json_data[0].get("school")
        ajson_class = json_data[0].get("class")

        if ajson_school == "none" or ajson_school is None:
            none_data = {'school':"bulunamadi","class": "bulunamadı"}
            return none_data


        else:
            return json_data[0]

    else:
        print("JSON verileri alınamadı veya geçersiz.")
        none_data = {'school':"bulunamadi","class": "bulunamadı"}
        return none_data




# Başlatıcı
def start():
    
    libs = check_lib(library_list)


    if libs:
        print("Eksik Kütüphane")
        print(libs)
        download_l = lib_download(libs)
        if download_l:
            print("indirme başarısız!")
            print(download_l)
            return
        else:
            print("indirme başarılı")
    else:
         print("\033[92mKütüphaneler Eksiksiz \033[0m")
#kontrol tamamlandı
    time.sleep(2)
    json_school = json_dogrula()


    json_school_name = json_school["school"]
    json_school_class = json_school["class"]
    app_ver = "1.5"
    checked = check_ver(app_ver,json_school_name,json_school_class)
    if checked:
        latest_ver = checked.get("latest")
        my_ver = checked.get("myver")
        check_msg = checked.get("message")

        if check_msg == "guncel":
            print(f"\033[92mVersiyon uyumlu.\033[0m \033[94m Güncelleme gerekmiyor.\033[0m \033[95m Güncel Version: \033[0m\033[92m{latest_ver} \033[0m ")
        elif check_msg == "eski":
            print(f"\033[91mYeni versiyon mevcut:  \033[0m \033[92m {latest_ver}\033[0m  \033[91m  Güncelleme yapmalısınız.\033[0m")
        else:
            print("versiyonda bir hata oluştu!")
            print(check_msg)
    else:
        latest_ver = app_ver
        print("versiyon kontrolu başarısız")

    start_gui(app_ver,latest_ver)








start()
