from tkinter import messagebox
import subprocess
from getpass import getpass
import os
import sys
from PIL import Image
# Uygulamanın ana dizini
project_root = os.path.dirname(os.path.abspath(__file__))

# customtkinter kütüphanesinin bulunduğu klasörü sys.path'e ekle
customtkinter_path = os.path.join(project_root, "lib")
sys.path.append(customtkinter_path)
import customtkinter
from customtkinter import filedialog

customtkinter.set_appearance_mode("Dark")


class App(customtkinter.CTk):
    def __init__(app,app_version,latest_ver):
        super().__init__()
        your_version_number = app_version
        

        def start_exe(file,pw):
            try:
                password = pw
                command = f"echo '{password}' | sudo -S wine {file}"
                process = subprocess.Popen(["gnome-terminal", "--", "bash", "-c", command])
                print(process.stdout)
            except subprocess.CalledProcessError as e:
                print(f"Hata oluştu: {e}")

        def update_command():
            file_path = filedialog.askopenfilename(title="Dosya Seç", filetypes=[("Tüm Dosyalar", "*.*")])
            print(f"Seçilen Dosya: {file_path}")
            if file_path:
                file_extension = file_path.split('.')[-1]
                print(f"Dosya Uzantısı: {file_extension}")
                if file_path:
                    file_extension = file_path.split('.')[-1]
                    print(f"Dosya Uzantısı: {file_extension}")

                    
                    app.home_frame_label.configure(text=f"{file_path}")


        def start_command():
            selected_file = app.home_frame_label.cget("text")
            input_value = app.home_frame_input_entry.get()
            start_log = start_exe(selected_file,input_value)
            print(start_log)
            print(f"Başlat butonuna basıldı. Seçilen Dosya: {selected_file}, Giriş Değeri: {input_value}")
        
        def start_fatih():

            command = "echo '1' | sudo -S wine /home/*/Belgeler/parduspenta/pentafatih/fatih.exe"
            process = subprocess.Popen(["gnome-terminal", "--", "bash", "-c", command])

        def download_fatih():
            command = "echo '1' | sudo -S bash -c 'cd /home/*/Belgeler/parduspenta/ && wget https://penta.skyfetch.dev/docs/plugins/fatih/fatih.sh && chmod +x fatih.sh && ./fatih.sh'"
            process = subprocess.Popen(["gnome-terminal", "--", "bash", "-c", command])
            print(process.stdout)

        def download_gpic():
            command = "echo '1' | sudo -S apt-get -y install gpicview"
            process = subprocess.Popen(["gnome-terminal", "--", "bash", "-c", command])
            print(process.stdout)

        def open_gpic():
            command = "echo '1' | sudo -S gpicview"
            process = subprocess.Popen(["gnome-terminal", "--", "bash", "-c", command])
            print(process.stdout)


        def start_update():
            
            full_command = f"echo '1' | sudo -S cd /home/*/Belgeler/"
            site_url = "https://penta.skyfetch.dev/docs/guncelle.sh"
            folder_path = "/home/*/Belgeler/"
            file_name = "guncelle.sh"
            file_path = f"{folder_path}/{file_name}"

            terminal_command = f"gnome-terminal -- bash -c 'if [ -e {file_path} ]; then echo \"1\" | sudo -S rm {file_path}; fi; exec bash'"
            subprocess.run(terminal_command, check=True, text=True, shell=True)

            terminal_command = f"gnome-terminal -- echo '1' | sudo -S bash -c 'cd {folder_path} && sudo wget {site_url}; exec bash'"
            subprocess.run(terminal_command, check=True, text=True, shell=True)

            execute_command = f"echo '1' | sudo -S chmod +x {file_path} && gnome-terminal -- bash -c 'cd {folder_path} && sudo ./{file_name}; exec bash'"
            result = subprocess.run(execute_command, check=True, text=True, shell=True)
            print(result.stdout)





        app.title("Pardus Penta Tools")
        app.geometry("700x450")

        app.grid_rowconfigure(0, weight=1)
        app.grid_columnconfigure(1, weight=1)

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")

        app.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "pardus.png")), size=(26, 26))
        app.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        app.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        
        app.program_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "program.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "program_white.png")), size=(20, 20))
        app.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))
        if app_version < latest_ver:
            app.version_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "version_old.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "version_old.png")), size=(20, 20))
        else:
            app.version_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "version_ok.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "version_ok.png")), size=(20, 20))
        #Other Image
        app.fatih_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path,"fatih.png")), size=(128,128))
        app.gpicview_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path,"gpicview.png")), size=(64,64))

        if app_version < latest_ver:
            version_message = "(Güncelleyiniz)"
        else:
           version_message = " "


        # create navigation frame
        app.navigation_frame = customtkinter.CTkFrame(app, corner_radius=0)
        app.navigation_frame.grid(row=0, column=0, sticky="nsew")
        app.navigation_frame.grid_rowconfigure(6, weight=1)

        app.navigation_frame_label = customtkinter.CTkLabel(app.navigation_frame, text=" Pardus Penta Tools", image=app.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        app.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        app.home_button = customtkinter.CTkButton(app.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Anasayfa",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=app.home_image, anchor="w", command=app.home_button_event)
        app.home_button.grid(row=1, column=0, sticky="ew")

        app.frame_2_button = customtkinter.CTkButton(app.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Uygulamalar",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=app.program_image, anchor="w", command=app.frame_2_button_event)
        app.frame_2_button.grid(row=2, column=0, sticky="ew")

        app.frame_3_button = customtkinter.CTkButton(app.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="İletişim",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=app.add_user_image, anchor="w", command=app.frame_3_button_event)
        app.frame_3_button.grid(row=3, column=0, sticky="ew")
        app.frame_5_button = customtkinter.CTkButton(app.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Güncelle",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=app.version_image, anchor="w", command=app.frame_4_button_event)
        app.frame_5_button.grid(row=4, column=0, sticky="ew")


        app.appearance_mode_menu = customtkinter.CTkOptionMenu(app.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=app.change_appearance_mode_event)
        app.appearance_mode_menu.grid(row=7, column=0, padx=20, pady=20, sticky="s")
        #version

        app.frame_ver = customtkinter.CTkButton(app.navigation_frame, corner_radius=0, height=40, border_spacing=10, text=f"Version {your_version_number}     {version_message}",fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                       image=app.version_image,anchor="w",command=app.frame_4_button_event)
        app.frame_ver.grid(row=8, column=0,padx=30,  sticky="s")
        app.frame_by = customtkinter.CTkLabel(app.navigation_frame, text="Coded By Halil Baki",
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        app.frame_by.grid(row=9, column=0,padx=0,  sticky="s")

        

        app.home_frame = customtkinter.CTkFrame(app, corner_radius=0, fg_color="transparent")
        app.home_frame.grid_columnconfigure(0, weight=1)
        
       
        # Dosya Seçme Butonu
        app.home_frame_button_1 = customtkinter.CTkButton(app.home_frame, text="Dosya Seç", command=update_command)
        app.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        # Dosya adını gösteren etiketi oluştur
        app.home_frame_label = customtkinter.CTkLabel(app.home_frame, text="Seçilen Dosya: ")
        app.home_frame_label.grid(row=0, column=0, padx=20, pady=10)
        
        # Giriş kutusunu oluştur
        app.home_frame_label2 = customtkinter.CTkLabel(app.home_frame, text="Kullanıcı Şifresi(Default 1): ")
        app.home_frame_label2.grid(row=2, column=0, padx=20, pady=10)
        app.home_frame_input_entry = customtkinter.CTkEntry(app.home_frame)
        app.home_frame_input_entry.grid(row=3,column=0,padx=20,pady=10)

        # Başlangıç değerini ekleyin
        app.home_frame_input_entry.insert(0, "1")
        # "Başlat" butonunu oluştur
        app.home_frame_button_start = customtkinter.CTkButton(app.home_frame, text="Başlat", command=start_command)
        app.home_frame_button_start.grid(row=4,column=0,padx=20,pady=10)




        # application Sayfası

        app.app_frame = customtkinter.CTkFrame(app, corner_radius=0, fg_color="transparent")
        
        app.image_label = customtkinter.CTkLabel(app.app_frame,text="", image=app.fatih_icon_image)
        app.app_frame_button = customtkinter.CTkLabel(app.app_frame, text = "Fatih Kalem")
        app.app_frame_button.grid(row=1,column=0,padx=10,pady=0)
        app.image_label.grid(row=0, column=0, padx=10, pady=2)
        app.fatih_button = customtkinter.CTkButton(app.app_frame,text="Kur", command=download_fatih)
        app.fatih_button.grid(row=2,column=0,padx=10,pady=0)
        app.fatih_button2 = customtkinter.CTkButton(app.app_frame,text="Aç", command=start_fatih)
        app.fatih_button2.grid(row=3,column=0,padx=10,pady=5)
        app.app_frame_label2 = customtkinter.CTkLabel(app.app_frame,text="",image=app.gpicview_icon_image)
        app.app_frame_label2.grid(row=0,column=1,padx=30,pady=10)
        app.app_frame_button2 = customtkinter.CTkLabel(app.app_frame, text = "Resim Görüntüleyici")
        app.app_frame_button2.grid(row=1,column=1,padx=30,pady=0)
        app.fatih_button21 = customtkinter.CTkButton(app.app_frame,text="Kur", command=download_gpic)
        app.fatih_button21.grid(row=2,column=1,padx=30,pady=0)
        app.fatih_button22 = customtkinter.CTkButton(app.app_frame,text="Aç", command=open_gpic)
        app.fatih_button22.grid(row=3,column=1,padx=30,pady=5)

        # İletişim Sayfası
        app.iletisim_frame = customtkinter.CTkFrame(app, corner_radius=0, fg_color="transparent")
        app.iletisim_frame_web = customtkinter.CTkLabel(app.iletisim_frame, text="Web Sitesi: https://penta.skyfetch.dev/ ")
        app.iletisim_frame_web.grid(row=0, column=0, padx=20, pady=10)
        app.iletisim_frame_mail = customtkinter.CTkLabel(app.iletisim_frame, text="Mail Adresi: info@penta.skyfetch.dev ")
        app.iletisim_frame_mail.grid(row=1, column=0, padx=19, pady=10)
        #version Sayfası
      

        app.version_frame = customtkinter.CTkFrame(app, corner_radius=0, fg_color="transparent")
        app.version_frame.grid_columnconfigure(0, weight=1)
        app.version_frame_label = customtkinter.CTkLabel(app.version_frame, text="Version: "+app_version+" | Latest Version: "+latest_ver)
        app.version_frame_label.grid(row=1,column=0,padx=20,pady=10)
        app.version_frame_label2 = customtkinter.CTkLabel(app.version_frame, text="Yüklü Sürüm: "+app_version+" | Yeni Sürüm: "+latest_ver)
        app.version_frame_label2.grid(row=2,column=0,padx=20,pady=10)
        
        #Versiyon Güncelleme
        app.version_frame_button = customtkinter.CTkButton(app.version_frame, text="Güncelle",command=start_update)
        app.version_frame_button.grid(row=4,column=0,padx=20,pady=10)
        # select default frame
        app.select_frame_by_name("home")
        app.appearance_mode_menu.set("Dark")
      


    def select_frame_by_name(app, name):
        # set button color for selected button
        app.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        app.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        app.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")
        app.version_frame.configure(fg_color=("gray75", "gray25") if name == "frame_4" else "transparent")

        # show selected frame
        if name == "home":
            app.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            app.home_frame.grid_forget()
        if name == "frame_2":
            app.app_frame.grid(row=0, column=1, sticky="nsew")
        else:
            app.app_frame.grid_forget()
        if name == "frame_3":
            app.iletisim_frame.grid(row=0, column=1, sticky="nsew")
        else:
            app.iletisim_frame.grid_forget()
        if name == "frame_4":
            app.version_frame.grid(row=0, column=1, sticky="nsew")
        else:
            app.version_frame.grid_forget()

    def home_button_event(app):
        app.select_frame_by_name("home")

    def frame_2_button_event(app):
        app.select_frame_by_name("frame_2")

    def frame_3_button_event(app):
        app.select_frame_by_name("frame_3")
    def frame_4_button_event(app):
        app.select_frame_by_name("frame_4")

    def change_appearance_mode_event(app, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)
    


if __name__ == "__main__":
    app = App()
    app.mainloop()

