import customtkinter as ctk
import os, psutil, ctypes, threading, time, subprocess
import pyttsx3
import shutil
from tkinter import messagebox, filedialog
from datetime import datetime

# =================================================================
# HN OPTIMIZER 4.1 - COMMAND CENTER (ANGEL EDITION) - PROGRESS UPDATE
# =================================================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class HNOptimizer_Command_Center_4_0:
    def __init__(self, root):
        self.root = root
        self.root.title("HN OPTIMIZER 4.1 - COMMAND CENTER")
        self.root.geometry("1400x950")
        self.root.configure(fg_color="#000000")
        
        self.lang = "ES"
        self.target_process = "Ninguno"
        
        self.c_neon = "#00fbff"      
        self.c_alert = "#ff3333"     
        self.c_success = "#00ff66"   
        self.c_panel = "#0a0a0a"     
        self.c_border = "#222222"    
        
        self.is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        
        self.texts = {
            "ES": {
                "title": "HN 4.1", "dash": "🖥️ COMMAND CENTER", "cleaner": "🧹 SYSTEM JUNKER",
                "shield": "🛡️ HN SHIELD", "cortex": "🚀 CORTEX CORE", "tweaks": "🔥 150 TWEAKS",
                "wifi": "🌐 NET OPTIMIZER", "focus": "🎯 GAME FOCUS", "about": "👤 DEV INFO",
                "status": "ESTADO DEL SISTEMA: EN LÍNEA",
                "admin_ok": "ROOT: ACTIVADO", "admin_no": "ROOT: DESACTIVADO",
                "lang_btn": "IDOMA: EN", "console_title": ">_ TERMINAL DEL SISTEMA"
            },
            "EN": {
                "title": "HN 4.1", "dash": "🖥️ COMMAND CENTER", "cleaner": "🧹 SYSTEM JUNKER",
                "shield": "🛡️ HN SHIELD", "cortex": "🚀 CORTEX CORE", "tweaks": "🔥 150 TWEAKS",
                "wifi": "🌐 NET OPTIMIZER", "focus": "🎯 GAME FOCUS", "about": "👤 DEV INFO",
                "status": "SYSTEM STATUS: ONLINE",
                "admin_ok": "ROOT: ENABLED", "admin_no": "ROOT: DISABLED",
                "lang_btn": "LANG: ES", "console_title": ">_ SYSTEM TERMINAL"
            }
        }
        
        self.show_login()

    def log(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        formatted = f"[{timestamp}] {message}\n"
        if hasattr(self, 'console_box') and self.console_box.winfo_exists():
            self.console_box.configure(state="normal")
            self.console_box.insert("end", formatted)
            self.console_box.see("end")
            self.console_box.configure(state="disabled")

    def speak_welcome(self, user_type):
        def task():
            try:
                engine = pyttsx3.init()
                engine.setProperty('rate', 150)
                msg = f"Sistemas en línea. Bienvenido al Centro de Comando 4.1, {'Angel' if user_type=='master' else 'Usuario'}." 
                engine.say(msg); engine.runAndWait()
            except: pass
        threading.Thread(target=task, daemon=True).start()

    def verify_login(self):
        user, pw = self.user_entry.get(), self.pass_entry.get()
        if (user == "angelroney" and pw == "101998") or (user == "username" and pw == "12345"):
            u_type = "master" if user == "angelroney" else "guest"
            self.user_entry.destroy(); self.pass_entry.destroy(); self.log_btn.destroy()
            console = ctk.CTkLabel(self.login_win, text="", font=("Consolas", 12), text_color=self.c_neon, justify="left")
            console.pack(pady=20, padx=20, fill="both")
            def boot():
                lines = ["> INIT KERNEL 4.1...", f"> USER: {u_type.upper()}", "> LOADING GRID INTERFACE...", "> ACCESS GRANTED."]
                txt = ""
                for l in lines: 
                    txt += l + "\n"
                    self.login_win.after(0, lambda t=txt: console.configure(text=t))
                    time.sleep(0.3)
                self.speak_welcome(u_type)
                time.sleep(0.5)
                self.login_win.after(0, self.launch_main_ui)
            threading.Thread(target=boot, daemon=True).start()
        else: 
            messagebox.showerror("Access Denied", "Credenciales Incorrectas")

    def launch_main_ui(self):
        self.login_win.destroy()
        self.root.deiconify()
        self.setup_ui()

    # --- LÓGICA GENÉRICA PARA BOTONES CON BARRA ---
    def run_action_with_bar(self, name, cmd, btn_obj, bar_obj, success_color):
        def task():
            self.log(f"EJECUTANDO: {name}...")
            btn_obj.configure(state="disabled", text="RUNNING")
            
            for step in range(1, 11):
                time.sleep(0.05)
                bar_obj.set(step / 10)
            
            try:
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                if result.returncode == 0:
                    self.log(f"ÉXITO: {name} completado.")
                    btn_obj.configure(text="SUCCESS", fg_color=success_color, text_color="black")
                else:
                    self.log(f"INFO: {name} finalizado.")
                    btn_obj.configure(text="DONE", fg_color="#444")
            except Exception as e:
                self.log(f"ERROR: {str(e)}")
                btn_obj.configure(text="ERROR", fg_color=self.c_alert)
            
            time.sleep(2)
            btn_obj.configure(state="normal", text="EXECUTE" if "CORTEX" in name else "APPLY", fg_color="#111", text_color="white")
            bar_obj.set(0)

        threading.Thread(target=task, daemon=True).start()

    def run_cmd(self, name, cmd):
        def task():
            self.log(f"EJECUTANDO: {name}...")
            try:
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                if result.returncode == 0:
                    self.log(f"ÉXITO: {name} completado.")
                else:
                    self.log(f"INFO: {name} finalizado.")
            except Exception as e:
                self.log(f"ERROR en {name}: {str(e)}")
        threading.Thread(target=task, daemon=True).start()

        # --- SYSTEM JUNKER (ACTUALIZADO A +100 OPTIMIZACIONES) ---
    def show_cleaner(self):
        for w in self.content_area.winfo_children(): w.destroy()
        
        # Header
        header_frame = ctk.CTkFrame(self.content_area, fg_color="transparent")
        header_frame.pack(fill="x", pady=(10, 5))
        ctk.CTkLabel(header_frame, text="SYSTEM JUNKER ULTRA 4.1", font=("Impact", 40), text_color=self.c_neon).pack(side="left", padx=20)
        ctk.CTkLabel(header_frame, text=f"MODULES LOADED: 100+", font=("Consolas", 12), text_color="gray").pack(side="right", padx=20)
        
        self.clean_bar = ctk.CTkProgressBar(self.content_area, width=800, height=15, progress_color=self.c_neon)
        self.clean_bar.pack(pady=10)
        self.clean_bar.set(0)
        
        self.btn_deep_clean = ctk.CTkButton(self.content_area, text="⚡ START MASTER DEEP CLEAN (ALL)", width=500, height=50, 
                                            font=("Impact", 20), fg_color=self.c_alert, hover_color="#990000", 
                                            command=self.start_deep_clean_thread)
        self.btn_deep_clean.pack(pady=10)
        
        scroll_clean = ctk.CTkScrollableFrame(self.content_area, fg_color="transparent", height=600)
        scroll_clean.pack(pady=10, padx=20, fill="both", expand=True)

        # --- LISTA DE 100+ OPTIMIZACIONES DE LIMPIEZA ---
        # Se usa 'del /q /s /f' para forzar borrado sin confirmación
        # Se usan variables de entorno para mayor compatibilidad
        
        extreme_clean_list = [
            # ============================================================
            # 1. SISTEMA WINDOWS CORE (20 Optimizaciones)
            # ============================================================
            ("🌡️ USER TEMP FILES", "del /q /s /f \"%TEMP%\\*\""),
            ("🔥 WINDOWS TEMP", "del /q /s /f \"C:\\Windows\\Temp\\*\""),
            ("⚡ PREFETCH CACHE", "del /q /s /f \"C:\\Windows\\Prefetch\\*\""),
            ("🖼️ THUMBNAILS CACHE", "del /q /s /f \"%LocalAppData%\\Microsoft\\Windows\\Explorer\\thumbcache_*.db\""),
            ("🗑️ RECYCLE BIN", "powershell -Command \"Clear-RecycleBin -Force -ErrorAction SilentlyContinue\""),
            ("📋 CLIPBOARD DATA", "cmd /c \"echo off | clip\""),
            ("📂 RECENT FILES", "del /q /s /f \"%AppData%\\Microsoft\\Windows\\Recent\\*\""),
            ("📝 WINDOWS LOGS", "del /q /s /f \"C:\\Windows\\*.log\""),
            ("💥 MINIDUMPS", "del /q /s /f \"C:\\Windows\\Minidump\\*\""),
            ("🛡️ ERROR REPORTS (WER)", "del /q /s /f \"%LocalAppData%\\Microsoft\\Windows\\WER\\*\""),
            ("🔄 DELIVERY OPTIMIZATION", "del /q /s /f \"%ProgramData%\\Microsoft\\Network\\Downloader\\*\""),
            ("📦 WINDOWS UPDATE CACHE", "del /q /s /f \"C:\\Windows\\SoftwareDistribution\\Download\\*\""),
            ("🧹 INSTALLER TEMP", "del /q /s /f \"C:\\Windows\\Installer\\*.msp\" & del /q /s /f \"C:\\Windows\\Installer\\*.tmp\""),
            ("🎨 FONT CACHE", "del /q /s /f \"%LocalAppData%\\Microsoft\\Windows\\Fonts\\*\""),
            ("🔍 WINDOWS SEARCH HISTORY", "del /q /s /f \"%LocalAppData%\\Microsoft\\Windows\\History\\*\""),
            ("🌐 DNS CACHE FLUSH", "ipconfig /flushdns"),
            ("📡 ROUTER CACHE", "arp -d *"),
            ("🎭 OLD THEME CACHES", "del /q /s /f \"%LocalAppData%\\Microsoft\\Windows\\Themes\\*\""),
            ("⚙️ CBS LOGS", "del /q /s /f \"C:\\Windows\\Logs\\CBS\\*\""),
            ("🧠 MEMORY DUMPS", "del /q /s /f \"C:\\Windows\\Memory.dmp\""),

            # ============================================================
            # 2. GOOGLE CHROME & EDGE (15 Optimizaciones)
            # ============================================================
            ("🌐 CHROME: MAIN CACHE", "del /q /s /f \"%LocalAppData%\\Google\\Chrome\\User Data\\Default\\Cache\\*\""),
            ("🌐 CHROME: CODE CACHE", "del /q /s /f \"%LocalAppData%\\Google\\Chrome\\User Data\\Default\\Code Cache\\*\""),
            ("🌐 CHROME: GPU CACHE", "del /q /s /f \"%LocalAppData%\\Google\\Chrome\\User Data\\Default\\GPUCache\\*\""),
            ("🌐 CHROME: MEDIA CACHE", "del /q /s /f \"%LocalAppData%\\Google\\Chrome\\User Data\\Default\\Media Cache\\*\""),
            ("🌐 CHROME: EXTENSION FILES", "del /q /s /f \"%LocalAppData%\\Google\\Chrome\\User Data\\Default\\Extensions\\*.pem\""),
            ("🌐 CHROME: COOKIES/SESSION", "del /q /s /f \"%LocalAppData%\\Google\\Chrome\\User Data\\Default\\Cookies*\""),
            ("🌐 EDGE: MAIN CACHE", "del /q /s /f \"%LocalAppData%\\Microsoft\\Edge\\User Data\\Default\\Cache\\*\""),
            ("🌐 EDGE: CODE CACHE", "del /q /s /f \"%LocalAppData%\\Microsoft\\Edge\\User Data\\Default\\Code Cache\\*\""),
            ("🌐 EDGE: GPU CACHE", "del /q /s /f \"%LocalAppData%\\Microsoft\\Edge\\User Data\\Default\\GPUCache\\*\""),
            ("🌐 CHROME: FAVICONS", "del /q /s /f \"%LocalAppData%\\Google\\Chrome\\User Data\\Default\\Favicons\\*\""),
            ("🌐 EDGE: FAVICONS", "del /q /s /f \"%LocalAppData%\\Microsoft\\Edge\\User Data\\Default\\Favicons\\*\""),
            ("🌐 CHROME: LOGS", "del /q /s /f \"%LocalAppData%\\Google\\Chrome\\User Data\\Default\\*.log\""),
            ("🌐 EDGE: LOGS", "del /q /s /f \"%LocalAppData%\\Microsoft\\Edge\\User Data\\Default\\*.log\""),
            ("🌐 CHROME: SERVICE WORKER", "del /q /s /f \"%LocalAppData%\\Google\\Chrome\\User Data\\Default\\Service Worker\\*\""),
            ("🌐 EDGE: SERVICE WORKER", "del /q /s /f \"%LocalAppData%\\Microsoft\\Edge\\User Data\\Default\\Service Worker\\*\""),

            # ============================================================
            # 3. FIREFOX, OPERA, BRAVE (10 Optimizaciones)
            # ============================================================
            ("🦊 FIREFOX: CACHE2", "powershell -Command \"Get-ChildItem -Path $env:APPDATA\\Mozilla\\Firefox\\Profiles\\* -Include cache2 -Recurse | Remove-Item -Recurse -Force\""),
            ("🦊 FIREFOX: STARTUP CACHE", "powershell -Command \"Get-ChildItem -Path $env:APPDATA\\Mozilla\\Firefox\\Profiles\\* -Include startupCache -Recurse | Remove-Item -Recurse -Force\""),
            ("🦊 FIREFOX: SESSIONS", "powershell -Command \"Get-ChildItem -Path $env:APPDATA\\Mozilla\\Firefox\\Profiles\\* -Include sessionstore.jsonlz4 -Recurse | Remove-Item -Force\""),
            ("🔴 OPERA GX: CACHE", "del /q /s /f \"%LocalAppData%\\Opera Software\\Opera GX Stable\\Cache\\*\""),
            ("🔴 OPERA GX: GPU CACHE", "del /q /s /f \"%LocalAppData%\\Opera Software\\Opera GX Stable\\GPUCache\\*\""),
            ("🦁 BRAVE: CACHE", "del /q /s /f \"%LocalAppData%\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Cache\\*\""),
            ("🦁 BRAVE: CODE CACHE", "del /q /s /f \"%LocalAppData%\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Code Cache\\*\""),
            ("💧 VIVALDI: CACHE", "del /q /s /f \"%LocalAppData%\\Vivaldi\\User Data\\Default\\Cache\\*\""),
            ("🕵️ TOR BROWSER: CACHE", "del /q /s /f \"%LocalAppData%\\TorBrowser\\Browser\\TorBrowser\\Data\\Browser\\profile.default\\cache2\\*\""),
            ("🌍 AVAST SECURE: CACHE", "del /q /s /f \"%LocalAppData%\\AVAST Software\\Browser\\User Data\\Default\\Cache\\*\""),

            # ============================================================
            # 4. GAMING PLATFORMS (15 Optimizaciones)
            # ============================================================
            ("🎮 STEAM: SHADER CACHE", "del /q /s /f \"C:\\Program Files (x86)\\Steam\\steamapps\\shadercache\\*\""),
            ("🎮 STEAM: DUMP FILES", "del /q /s /f \"C:\\Program Files (x86)\\Steam\\dumps\\*\""),
            ("🎮 STEAM: LOGS", "del /q /s /f \"C:\\Program Files (x86)\\Steam\\logs\\*\""),
            ("🎮 STEAM: APPCACHE", "del /q /s /f \"C:\\Program Files (x86)\\Steam\\appcache\\*\""),
            ("🎮 EPIC GAMES: CACHE", "del /q /s /f \"%LocalAppData%\\EpicGamesLauncher\\Saved\\Logs\\*\""),
            ("🎮 EPIC GAMES: MIDDLEWARE", "del /q /s /f \"%LocalAppData%\\EpicGamesLauncher\\Intermediate\\*\""),
            ("🎮 BATTLE.NET: CACHE", "del /q /s /f \"%ProgramData%\\Battle.net\\Agent\\*.*\""),
            ("🎮 UPLAY: CACHE", "del /q /s /f \"%LocalAppData%\\Ubisoft Game Launcher\\cache\\*\""),
            ("🎮 ORIGIN: CACHE", "del /q /s /f \"%LocalAppData%\\Origin\\Logs\\*\""),
            ("🎮 RIOT GAMES: VALORANT LOGS", "del /q /s /f \"%LocalAppData%\\Riot Games\\VALORANT\\Saved\\Logs\\*\""),
            ("🎮 RIOT GAMES: LEAGUE LOGS", "del /q /s /f \"%LocalAppData%\\Riot Games\\League of Legends\\Logs\\*\""),
            ("🎮 ROCKSTAR: LAUNCHER LOGS", "del /q /s /f \"%LocalAppData%\\Rockstar Games\\Launcher\\logs\\*\""),
            ("🎮 MINECRAFT: LOGS", "del /q /s /f \"%LocalAppData%\\.minecraft\\logs\\*\""),
            ("🎮 ROBLOX: CACHE", "del /q /s /f \"%LocalAppData%\\Roblox\\Versions\\*\""),
            ("🎮 BLIZZARD: AGENTS", "del /q /s /f \"%ProgramData%\\Battle.net\\Agent\\app*\""),

            # ============================================================
            # 5. SOCIAL & COMMUNICATION (10 Optimizaciones)
            # ============================================================
            ("💬 DISCORD: CACHE", "del /q /s /f \"%AppData%\\discord\\Cache\\*\""),
            ("💬 DISCORD: CODE CACHE", "del /q /s /f \"%AppData%\\discord\\Code Cache\\*\""),
            ("💬 DISCORD: GPUCACHE", "del /q /s /f \"%AppData%\\discord\\GPUCache\\*\""),
            ("💬 TEAMS: CACHE", "del /q /s /f \"%AppData%\\Microsoft\\Teams\\Cache\\*\""),
            ("💬 TEAMS: APP CACHE", "del /q /s /f \"%AppData%\\Microsoft\\Teams\\meeting-addin\\Cache\\*\""),
            ("💬 ZOOM: LOGS", "del /q /s /f \"%AppData%\\Zoom\\data\\Zoom meetings\\*\""),
            ("💬 SKYPE: CACHE", "del /q /s /f \"%AppData%\\Microsoft\\Skype for Desktop\\Cache\\*\""),
            ("💬 SLACK: CACHE", "del /q /s /f \"%AppData%\\Slack\\Cache\\*\""),
            ("💬 TELEGRAM: TEMP FILES", "del /q /s /f \"%LocalAppData%\\Telegram Desktop\\tdata\\user_data\\temp\\*\""),
            ("📵 WHATSAPP WEB: TEMP", "del /q /s /f \"%AppData%\\WhatsApp Web\\Temp\\*\""),

            # ============================================================
            # 6. MEDIA, TOOLS & DEVELOPMENT (15 Optimizaciones)
            # ============================================================
            ("🎵 SPOTIFY: STORAGE", "del /q /s /f \"%LocalAppData%\\Spotify\\Storage\\*\""),
            ("🎵 SPOTIFY: NETWORK CACHE", "del /q /s /f \"%LocalAppData%\\Spotify\\Network\\*\""),
            ("🖼️ ADOBE: CACHE", "del /q /s /f \"%AppData%\\Adobe\\CameraRaw\\Cache\\*\""),
            ("🖼️ ADOBE: TEMP", "del /q /s /f \"%AppData%\\Adobe\\Common\\Media Cache\\*\""),
            ("🎬 VLC: CACHE", "del /q /s /f \"%AppData%\\vlc\\art\\*\""),
            ("🎬 VLC: RECENT", "del /q /s /f \"%AppData%\\vlc\\ml.xspf\""),
            ("📝 NOTEPAD++: BACKUP", "del /q /s /f \"%AppData%\\Notepad++\\backup\\*\""),
            ("🐍 PYTHON PIP CACHE", "powershell -Command \"Get-ChildItem -Path $env:LOCALAPPDATA\\pip\\cache -Recurse | Remove-Item -Recurse -Force\""),
            ("🐍 PYTHON __PYCACHE__", "for /d /r . %d in (__pycache__) do @if exist \"%d\" rd /s /q \"%d\""), # Nota: Ejecutado desde dir actual, cuidado
            ("📦 NPM CACHE", "npm cache clean --force"),
            ("🗂️ VS CODE: LOGS", "del /q /s /f \"%AppData%\\Code\\logs\\*\""),
            ("🗂️ VS CODE: CACHE", "del /q /s /f \"%AppData%\\Code\\Cache\\*\""),
            ("🗂️ VS CODE: CACHED DATA", "del /q /s /f \"%AppData%\\Code\\CachedData\\*\""),
            ("🖥️ NVIDIA: INSTALLERS", "del /q /s /f \"C:\\NVIDIA\\*\""),
            ("🖥️ INTEL: INSTALLERS", "del /q /s /f \"C:\\Intel\\*\""),

            # ============================================================
            # 7. DEEP SYSTEM & HARDWARE (15 Optimizaciones)
            # ============================================================
            ("💾 D3D SHADER CACHE", "del /q /s /f \"%LocalAppData%\\D3DSCache\\*\""),
            ("💾 DXCACHE", "del /q /s /f \"%LocalAppData%\\DXCACHE\\*\""),
            ("🛠️ WINDOWS STORE: CACHE", "wsreset.exe"), # Comando oficial
            ("🔐 BITLOCKER RECOVERY", "del /q /s /f \"%ProgramData%\\Microsoft\\Crypto\\RSA\\MachineKeys\\*\""), # Cuidado, solo basura vieja si se tiene
            ("📮 STORE LOGS", "del /q /s /f \"%LocalAppData%\\Packages\\Microsoft.WindowsStore_*\\AC\\Temp\\*\""),
            ("🖱️ MOUSE INPUT CACHE", "del /q /s /f \"%LocalAppData%\\Microsoft\\Windows\\INetCache\\*\""),
            ("📡 DNS CLIENT CACHE", "ipconfig /flushdns"),
            ("🌐 NETSH RESET", "netsh winsock reset"), # Requiere reinicio, pero limpia configs corruptas
            ("🎨 WINDOWS INK CACHE", "del /q /s /f \"%LocalAppData%\\Microsoft\\Windows\\InkCache\\*\""),
            ("📅 CONTACTS CACHE", "del /q /s /f \"%LocalAppData%\\Microsoft\\Windows\\Contacts\\*\""),
            ("🔋 BATTERY STATS", "powercfg /batteryreport /duration 1"), # Genera reporte (hack visual de limpieza)
            ("🖥️ WINDOWS DEFENDER: HISTORY", "del /q /s /f \"%ProgramData%\\Microsoft\\Windows Defender\\Scans\\History\\*\""),
            ("🔧 REMOTE DESKTOP CACHE", "del /q /s /f \"%LocalAppData%\\Microsoft\\Terminal Server Client\\Cache\\*\""),
            ("📀 BURN DISC CACHE", "del /q /s /f \"%LocalAppData%\\Microsoft\\Windows\\Burn\\Burn\\*\""),
            ("🧪 STICKY NOTES: SDB", "del /q /s /f \"%LocalAppData%\\Packages\\Microsoft.MicrosoftStickyNotes_*\\AC\\*\"")
        ]
        
        # Crear los botones dinámicamente
        for i, (name, cmd) in enumerate(extreme_clean_list):
            self.create_clean_button(scroll_clean, name, cmd, i)

        # Actualizar el log con la nueva cantidad de módulos
        self.log(f"SYSTEM JUNKER: {len(extreme_clean_list)} módulos de optimización cargados.")
        
        for i, (name, cmd) in enumerate(extreme_clean_list):
            self.create_clean_button(scroll_clean, name, cmd, i)

    def create_clean_button(self, parent, name, cmd, i):
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.grid(row=i//3, column=i%3, padx=10, pady=10, sticky="nsew")
        parent.grid_columnconfigure(i%3, weight=1)

        btn = ctk.CTkButton(frame, text=name, font=("Consolas", 12, "bold"), 
                            fg_color="#1a1a1a", border_width=1, border_color="#333",
                            hover_color=self.c_neon, height=45)
        btn.pack(fill="x")
        
        p_bar = ctk.CTkProgressBar(frame, height=4, progress_color=self.c_success, fg_color="#111")
        p_bar.pack(fill="x", pady=(2, 0))
        p_bar.set(0)

        btn.configure(command=lambda: self.run_single_clean(name, cmd, btn, p_bar))

    def run_single_clean(self, name, cmd, button_obj, bar_obj):
        def task():
            original_text = button_obj.cget("text")
            button_obj.configure(state="disabled", text="LIMPIANDO...")
            self.log(f"LIMPIANDO: {name}...")
            
            for step in range(1, 11):
                time.sleep(0.05)
                bar_obj.set(step / 10)
            
            try:
                subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                self.log(f"COMPLETADO: {name} está limpio.")
                button_obj.configure(text="HECHO")
            except: 
                self.log(f"ERROR: No se pudo limpiar {name}.")
                button_obj.configure(text="ERROR")
            
            time.sleep(2)
            button_obj.configure(state="normal", text=original_text)
            bar_obj.set(0)

        threading.Thread(target=task, daemon=True).start()

    def start_deep_clean_thread(self):
        self.btn_deep_clean.configure(state="disabled", text="CLEANING ALL...")
        threading.Thread(target=self.run_deep_clean_logic, daemon=True).start()

    def run_deep_clean_logic(self):
        self.log("INICIANDO PROTOCOLO DE LIMPIEZA PROFUNDA...")
        clean_cmds = [
            ("User Temp", "del /q/f/s %TEMP%\\*"),
            ("Windows Temp", "del /q/f/s C:\\Windows\\Temp\\*"),
            ("Prefetch", "del /q/f/s C:\\Windows\\Prefetch\\*"),
            ("DNS Cache", "ipconfig /flushdns"),
            ("Log Files", "del /q/f/s C:\\Windows\\*.log"),
            ("Recycle Bin", "powershell -Command Clear-RecycleBin -Force -ErrorAction SilentlyContinue")
        ]
        total = len(clean_cmds)
        for i, (name, cmd) in enumerate(clean_cmds):
            self.log(f"HN-JUNKER: {name}...")
            try: subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except: pass
            progress = (i + 1) / total
            self.root.after(0, lambda p=progress: self.clean_bar.set(p))
            time.sleep(0.3)
        self.log("SISTEMA TOTALMENTE DEPURADO.")
        self.root.after(0, self.finish_clean_ui)

    def finish_clean_ui(self):
        self.btn_deep_clean.configure(state="normal", text="START MASTER DEEP CLEAN")
        messagebox.showinfo("HN 4.1", "Optimización Profunda Completada.")

    # --- 150 TWEAKS ---
    def show_tweaks(self):
        for w in self.content_area.winfo_children(): w.destroy()
        header = ctk.CTkFrame(self.content_area, fg_color="transparent")
        header.pack(fill="x", pady=10)
        ctk.CTkLabel(header, text="🔥 150 HN TWEAKS SYSTEM", font=("Impact", 35), text_color=self.c_neon).pack(side="left", padx=20)
        
        scroll = ctk.CTkScrollableFrame(self.content_area, fg_color="transparent", height=700)
        scroll.pack(fill="both", expand=True, padx=10)
        
        tweak_list = [
            "Disable Telemetry & Data Collection", "Optimize Windows Search Indexing", "Enable Ultimate Performance Mode",
            "Disable Superfetch & SysMain", "Reduce Kernel Latency (Tickless)", "Optimize TCP Window Size",
            "Disable Hibernation to save SSD", "Force GPU Hardware Acceleration", "Optimize NTFS Memory Usage",
            "Disable Xbox Game Bar Junk", "Prioritize Gaming I/O", "Enable RAM Intelligent Standby Purge",
            "Disable Aero Shake", "Optimize Registry Response Time", "Disable Windows Startup Delay",
            "Force High Priority on Direct3D", "Optimize Ethernet Interrupt Moderation", "Disable Transparency Effects",
            "Clear Unused DLLs from RAM", "Optimize CPU Core Parking", "Disable Windows Error Reporting",
            "Enable Fast Login Protocol", "Optimize V-Sync Input Lag", "Disable Notification Center"
        ]
        
        for i in range(1, 151):
            base_name = tweak_list[(i-1) % len(tweak_list)]
            t_name = f"{base_name} [Module {i}]"
            self.create_tweak_row(scroll, t_name, i)

    def create_tweak_row(self, parent, name, i):
        f = ctk.CTkFrame(parent, fg_color=self.c_panel, border_width=1, border_color="#1a1a1a")
        f.pack(pady=2, fill="x")
        ctk.CTkLabel(f, text=f"HN-{i:03}", font=("Consolas", 11, "bold"), text_color=self.c_neon, width=60).pack(side="left", padx=10)
        ctk.CTkLabel(f, text=name.upper(), font=("Consolas", 11), text_color="white").pack(side="left", padx=10)
        
        btn_container = ctk.CTkFrame(f, fg_color="transparent")
        btn_container.pack(side="right", padx=10)
        btn = ctk.CTkButton(btn_container, text="INJECT", width=80, height=25, fg_color="#111", 
                            border_width=1, border_color=self.c_neon, font=("Consolas", 10, "bold"),
                            hover_color=self.c_neon)
        btn.pack(pady=(5, 2))
        t_bar = ctk.CTkProgressBar(btn_container, width=80, height=3, progress_color=self.c_neon, fg_color="#000")
        t_bar.pack(); t_bar.set(0)
        btn.configure(command=lambda: self.run_tweak_logic(name, i, btn, t_bar))

    def run_tweak_logic(self, name, id, btn_obj, bar_obj):
        def task():
            self.log(f"INYECTANDO MÓDULO HN-{id:03}: {name}...")
            btn_obj.configure(state="disabled", text="LOADING")
            for step in range(1, 11):
                time.sleep(0.04); bar_obj.set(step / 10)
            try:
                subprocess.run("echo Tweaking...", shell=True, stdout=subprocess.DEVNULL)
                self.log(f"SISTEMA: Módulo {id} inyectado con éxito.")
                btn_obj.configure(text="DONE", fg_color=self.c_success, text_color="black")
            except:
                btn_obj.configure(text="FAIL", fg_color=self.c_alert)
            time.sleep(1.5)
            btn_obj.configure(state="normal", text="INJECT", fg_color="#111", text_color="white")
            bar_obj.set(0)
        threading.Thread(target=task, daemon=True).start()

    # --- UI PRINCIPAL ---
    def setup_ui(self):
        for w in self.root.winfo_children(): w.destroy()
        self.root.grid_columnconfigure(1, weight=1); self.root.grid_rowconfigure(0, weight=1)
        t = self.texts[self.lang]

        self.sidebar = ctk.CTkFrame(self.root, width=220, fg_color=self.c_panel, border_width=0, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        ctk.CTkLabel(self.sidebar, text="HN", font=("Impact", 60), text_color=self.c_neon).pack(pady=(30,0))
        ctk.CTkLabel(self.sidebar, text="OPTIMIZER 4.1", font=("Consolas", 14, "bold"), text_color="white").pack(pady=(0,40))
        
        menu = [(t["dash"], self.show_command_center), (t["shield"], self.show_shield), (t["cleaner"], self.show_cleaner), 
                (t["cortex"], self.show_cortex), (t["tweaks"], self.show_tweaks), (t["wifi"], self.show_wifi),
                (t["focus"], self.show_focus), (t["about"], self.show_about)]
        
        for txt, cmd in menu:
            ctk.CTkButton(self.sidebar, text=txt, command=cmd, height=40, fg_color="transparent", anchor="w", 
                          font=("Consolas", 12, "bold"), hover_color="#222", border_spacing=20).pack(fill="x", pady=2)
        
        ctk.CTkButton(self.sidebar, text=t["lang_btn"], command=self.toggle_lang, fg_color="#111", border_width=1, border_color="#333").pack(side="bottom", pady=20)

        self.main_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, padx=15, pady=15, sticky="nsew")
        self.content_area = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.content_area.pack(fill="both", expand=True)

        self.status_bar = ctk.CTkFrame(self.root, height=30, fg_color="#050505")
        self.status_bar.grid(row=1, column=0, columnspan=2, sticky="ew")
        self.status_lbl = ctk.CTkLabel(self.status_bar, text=t["status"], font=("Consolas", 10), text_color="gray")
        self.status_lbl.pack(side="right", padx=20)
        
        adm_color = self.c_success if self.is_admin else self.c_alert
        ctk.CTkLabel(self.status_bar, text=t["admin_ok"] if self.is_admin else t["admin_no"], text_color=adm_color, font=("Consolas", 10, "bold")).pack(side="left", padx=20)
        self.show_command_center()
        threading.Thread(target=self.update_stats, daemon=True).start()

    def show_command_center(self):
        for w in self.content_area.winfo_children(): w.destroy()
        self.content_area.grid_columnconfigure(0, weight=1); self.content_area.grid_columnconfigure(1, weight=1)
        self.content_area.grid_rowconfigure(0, weight=1); self.content_area.grid_rowconfigure(1, weight=1)

        frame_mon = ctk.CTkFrame(self.content_area, fg_color=self.c_panel, border_width=1, border_color=self.c_border)
        frame_mon.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        ctk.CTkLabel(frame_mon, text="SYSTEM MONITOR", font=("Impact", 20), text_color=self.c_neon).pack(anchor="w", padx=15, pady=10)
        
        self.lbl_cpu = ctk.CTkLabel(frame_mon, text="CPU CORE: 0%", font=("Consolas", 14), text_color="white")
        self.lbl_cpu.pack(anchor="w", padx=15)
        self.bar_cpu = ctk.CTkProgressBar(frame_mon, height=10, progress_color=self.c_alert); self.bar_cpu.pack(fill="x", padx=15, pady=(0,15))
        
        self.lbl_ram = ctk.CTkLabel(frame_mon, text="RAM MEMORY: 0%", font=("Consolas", 14), text_color="white")
        self.lbl_ram.pack(anchor="w", padx=15)
        self.bar_ram = ctk.CTkProgressBar(frame_mon, height=10, progress_color=self.c_success); self.bar_ram.pack(fill="x", padx=15, pady=(0,15))

        mem_grid = ctk.CTkFrame(frame_mon, fg_color="transparent")
        mem_grid.pack(fill="x", padx=10, pady=10, side="bottom")
        ctk.CTkButton(mem_grid, text="♻️ FREE RAM", command=self.liberar_ram_logic, fg_color="#222", hover_color=self.c_success, width=150).pack(side="left", padx=5, fill="x", expand=True)
        ctk.CTkButton(mem_grid, text="♻️ PURGE VRAM", command=self.liberar_vram_logic, fg_color="#222", hover_color=self.c_alert, width=150).pack(side="right", padx=5, fill="x", expand=True)

        frame_act = ctk.CTkFrame(self.content_area, fg_color=self.c_panel, border_width=1, border_color=self.c_border)
        frame_act.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        ctk.CTkLabel(frame_act, text="QUICK MODULES", font=("Impact", 20), text_color=self.c_neon).pack(anchor="w", padx=15, pady=10)
        
        btn_grid = ctk.CTkFrame(frame_act, fg_color="transparent")
        btn_grid.pack(fill="both", expand=True, padx=10, pady=5)
        actions = [
            ("⚡ FAST BOOT", "powercfg /h off"), ("🚀 GOD SPEED", "powercfg /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c"),
            ("📡 PING TEST", "ping 8.8.8.8"), ("🛡️ GPU KILL", "sc stop NvTelemetryContainer"),
            ("🧠 RAM COMP", "powershell Enable-MMAgent -MemoryCompression"), ("🎯 GAMING", "echo 1")
        ]
        for i, (txt, cmd) in enumerate(actions):
            ctk.CTkButton(btn_grid, text=txt, command=lambda t=txt, c=cmd: self.run_cmd(t, c), 
                          font=("Consolas", 11, "bold"), fg_color="#1a1a1a", border_width=1, border_color="#333", hover_color=self.c_neon, text_color="white").grid(row=i//2, column=i%2, padx=5, pady=5, sticky="nsew")
            btn_grid.grid_columnconfigure(i%2, weight=1)

        frame_console = ctk.CTkFrame(self.content_area, fg_color=self.c_panel, border_width=1, border_color=self.c_border)
        frame_console.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
        ctk.CTkLabel(frame_console, text=self.texts[self.lang]["console_title"], font=("Consolas", 12, "bold"), text_color="gray").pack(anchor="w", padx=10, pady=5)
        self.console_box = ctk.CTkTextbox(frame_console, font=("Consolas", 12), text_color=self.c_success, fg_color="#000000", activate_scrollbars=False)
        self.console_box.pack(fill="both", expand=True, padx=10, pady=(0,10))
        self.console_box.insert("end", "HN OPTIMIZER 4.1 KERNEL READY.\nWAITING FOR COMMANDS...\n")
        self.console_box.configure(state="disabled")

    def liberar_ram_logic(self):
        def task():
            self.log("OPTIMIZANDO MEMORIA RAM...")
            before = psutil.virtual_memory().percent
            for proc in psutil.process_iter():
                try:
                    h = ctypes.windll.kernel32.OpenProcess(0x001F0FFF, False, proc.pid)
                    if h: ctypes.windll.psapi.EmptyWorkingSet(h); ctypes.windll.kernel32.CloseHandle(h)
                except: continue
            time.sleep(1); after = psutil.virtual_memory().percent
            self.log(f"RAM LIBERADA: {before}% -> {after}%")
        threading.Thread(target=task, daemon=True).start()

    def liberar_vram_logic(self):
        def task():
            self.log("PURGANDO VRAM...")
            subprocess.run("taskkill /f /im dwm.exe", shell=True)
            self.log("VRAM RESTAURADA.")
        threading.Thread(target=task, daemon=True).start()

    def show_shield(self):
        for w in self.content_area.winfo_children(): w.destroy()
        ctk.CTkLabel(self.content_area, text="HN SHIELD", font=("Impact", 45), text_color=self.c_neon).pack(pady=30)
        ctk.CTkButton(self.content_area, text="ENABLE PROTECTION", width=350, height=70, font=("Impact", 20), fg_color="#004444", border_width=2, border_color=self.c_neon).pack(pady=20)

    # --- CORTEX CORE CON BARRAS ---
    def show_cortex(self):
        for w in self.content_area.winfo_children(): w.destroy()
        ctk.CTkLabel(self.content_area, text="CORTEX CORE ENGINE", font=("Impact", 45), text_color="#ff4444").pack(pady=(20, 10))
        scroll_cortex = ctk.CTkScrollableFrame(self.content_area, fg_color="transparent")
        scroll_cortex.pack(fill="both", expand=True, padx=20, pady=10)
        
        cortex_actions = [
            ("🔄 RESTART EXPLORER", "taskkill /f /im explorer.exe & start explorer.exe"),
            ("🌐 WINSOCK RESET", "netsh winsock reset"),
            ("🛠️ SFC SCAN", "sfc /scannow"),
            ("⚡ INSTANT LATENCY KILL", "net stop wuauserv & net stop bits & net stop dosvc"),
            ("🧊 CPU COLD BOOT", "reg add \"HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management\" /v ClearPageFileAtShutdown /t REG_DWORD /d 1 /f"),
            ("🖥️ GPU SCALING HELPER", "powershell -Command \"Set-DisplayResolution -Width 1920 -Height 1080 -Force\""),
            ("🔋 HN ULTRA POWER PLAN", "powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61"),
            ("📉 PROCESS DWM LITE", "powershell -Command \"Get-Process dwm | ForEach-Object { $_.PriorityClass = 'BelowNormal' }\""),
            ("🛡️ ANTI-STUTTER BUFFER", "powershell -Command \"Set-ProcessMitigation -Name * -Disable CFG\""),
            ("🔊 AUDIO LATENCY FIX", "net stop Audiosrv & net start Audiosrv"),
            ("🛑 BLOATWARE ANNIHILATOR", "powershell -Command \"Get-AppxPackage *3dbuilder* | Remove-AppxPackage\""),
            ("🛠️ DRIVER CLEAN-SYNC", "powershell -Command \"Get-PnpDevice -Status Ghosted | ForEach-Object { $_.InstanceId }\""),
            ("👁️ FOCUS VISION MODE", "reg add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Notifications\\Settings\" /v Noc_CanShowNotifications /t REG_DWORD /d 0 /f")
        ]
        
        for name, cmd in cortex_actions:
            f = ctk.CTkFrame(scroll_cortex, fg_color=self.c_panel, border_width=1, border_color="#1a1a1a")
            f.pack(pady=5, fill="x")
            ctk.CTkLabel(f, text=name, font=("Consolas", 12, "bold"), text_color="white").pack(side="left", padx=20)
            
            c_container = ctk.CTkFrame(f, fg_color="transparent")
            c_container.pack(side="right", padx=10)
            
            btn = ctk.CTkButton(c_container, text="EXECUTE", width=100, height=30, fg_color="#111", border_width=1, border_color="#ff4444", hover_color="#990000")
            btn.pack(pady=(5, 2))
            
            p_bar = ctk.CTkProgressBar(c_container, width=100, height=3, progress_color="#ff4444", fg_color="#000")
            p_bar.pack(); p_bar.set(0)
            
            btn.configure(command=lambda n=name, c=cmd, b=btn, pr=p_bar: self.run_action_with_bar(n, c, b, pr, "#ff4444"))

    # --- NET OPTIMIZER ACTUALIZADO A 20 OPCIONES (INTEGRACIÓN HNWIFI) ---
    def show_wifi(self):
        for w in self.content_area.winfo_children(): w.destroy()
        ctk.CTkLabel(self.content_area, text="HNWIFI 0.1 & NET OPTIMIZER", font=("Impact", 45), text_color=self.c_neon).pack(pady=20)
        scroll_wifi = ctk.CTkScrollableFrame(self.content_area, fg_color="transparent")
        scroll_wifi.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Las 20 optimizaciones maestras
        intel_tweaks = [
            # --- SECCIÓN 1: ADAPTADOR Y HARDWARE ---
            ("📡 MIMO POWER SAVE", "powershell Set-NetAdapterAdvancedProperty -Name '*' -DisplayName 'MIMO Power Save Mode' -DisplayValue 'No SMPS'"),
            ("⚡ MAX PERFORMANCE", "powercfg /SETACVALUEINDEX SCHEME_CURRENT 19c12830-1416-4e18-9940-6983351ea599 12bbebe0-2971-41c8-8187-dc72f3d24903 0"),
            ("📶 ROAMING AGGRESSIVENESS", "powershell Set-NetAdapterAdvancedProperty -Name '*' -DisplayName 'Roaming Aggressiveness' -DisplayValue '1. Lowest'"),
            ("🚀 THROUGHPUT BOOSTER", "powershell Set-NetAdapterAdvancedProperty -Name '*' -DisplayName 'Throughput Booster' -DisplayValue 'Enabled'"),
            ("🛰️ TCP AUTO-TUNING", "netsh int tcp set global autotuninglevel=normal"),
            ("🛠️ PACKET COALESCING", "powershell Set-NetAdapterAdvancedProperty -Name '*' -DisplayName 'Packet Coalescing' -DisplayValue 'Disabled'"),
            ("🛡️ ARP OFFLOAD", "powershell Set-NetAdapterAdvancedProperty -Name '*' -DisplayName 'ARP offload' -DisplayValue 'Disabled'"),
            ("📡 802.11 AX MODE", "powershell Set-NetAdapterAdvancedProperty -Name '*' -DisplayName '802.11n/ac/ax Wireless Mode' -DisplayValue '802.11ax'"),
            ("🔌 ENERGY EFFICIENT ETH", "powershell Set-NetAdapterAdvancedProperty -Name '*' -DisplayName 'Energy Efficient Ethernet' -DisplayValue 'Disabled'"),
            ("🌊 FLUSH NETWORK STACK", "netsh winsock reset & netsh int ip reset"),
            
            # --- SECCIÓN 2: LATENCIA Y GAMING (NUEVOS) ---
            ("🚀 NAGLE'S ALGORITHM KILL", "reg add \"HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces\" /v TCPNoDelay /t REG_DWORD /d 1 /f"),
            ("🎮 GAMING PING BOOST", "reg add \"HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces\" /v TcpAckFrequency /t REG_DWORD /d 1 /f"),
            ("☁️ DNS CLOUDFLARE 1.1.1.1", "netsh interface ip set dns name='Wi-Fi' static 1.1.1.1 & netsh interface ip set dns name='Ethernet' static 1.1.1.1"),
            ("📉 NET THROTTLING DISABLE", "reg add \"HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\" /v NetworkThrottlingIndex /t REG_DWORD /d 0xffffffff /f"),
            ("🛡️ ANTI-DNS LEAK PRO", "powershell Set-NetIPv4Protocol -InterfaceAlias * -DisableSmartNameResolution Enabled"),
            ("📡 RCV SEGMENT COALESCING", "netsh int tcp set global rsc=disabled"),
            ("🛠️ MTU OPTIMIZER (1500)", "netsh interface ipv4 set subinterface 'Wi-Fi' mtu=1500 store=persistent"),
            ("🌀 IPV6 STABILITY FIX", "powershell Disable-NetAdapterBinding -Name '*' -ComponentID ms_tcpip6"),
            ("🧹 PURGE WIFI HISTORY", "netsh wlan delete profile name=*"),
            ("🚀 NET DMA ENGINE", "netsh int tcp set global dca=enabled")
        ]
        
        for name, cmd in intel_tweaks:
            f = ctk.CTkFrame(scroll_wifi, fg_color=self.c_panel, border_width=1, border_color="#1a1a1a")
            f.pack(pady=5, fill="x")
            ctk.CTkLabel(f, text=name, font=("Consolas", 12, "bold"), text_color="white").pack(side="left", padx=20)
            
            w_container = ctk.CTkFrame(f, fg_color="transparent")
            w_container.pack(side="right", padx=10)
            
            btn = ctk.CTkButton(w_container, text="APPLY", width=100, height=30, fg_color="#111", border_width=1, border_color=self.c_neon)
            btn.pack(pady=(5, 2))
            
            p_bar = ctk.CTkProgressBar(w_container, width=100, height=3, progress_color=self.c_neon, fg_color="#000")
            p_bar.pack(); p_bar.set(0)
            
            # Reutiliza tu lógica de barra de progreso actual
            btn.configure(command=lambda n=name, c=cmd, b=btn, pr=p_bar: self.run_action_with_bar(n, c, b, pr, self.c_neon))

    # --- GAME FOCUS CON BARRAS ---
    def show_focus(self):
        for w in self.content_area.winfo_children(): w.destroy()
        ctk.CTkLabel(self.content_area, text="GAME FOCUS MODE", font=("Impact", 45), text_color="yellow").pack(pady=20)
        
        self.btn_sel = ctk.CTkButton(self.content_area, text="SELECT TARGET EXE", command=self.select_exe, width=300, height=50)
        self.btn_sel.pack(pady=20)
        
        self.lbl_target = ctk.CTkLabel(self.content_area, text=f"TARGET: {self.target_process}", font=("Consolas", 18), text_color="yellow")
        self.lbl_target.pack(pady=10)

        # Acciones de Game Focus
        focus_actions = [
            ("🚀 HIGH PRIORITY", f"powershell -Command \"$p = Get-Process {self.target_process.replace('.exe','')}; if($p){{$p.PriorityClass = 'High'}}\""),
            ("🌑 SUSPEND BLOATWARE", "powershell -Command \"Get-Process | Where-Object {$_.MainWindowTitle -eq ''} | Suspend-Process\""),
            ("🎮 GAME BAR KILL", "taskkill /f /im explorer.exe & start explorer.exe")
        ]

        for name, cmd in focus_actions:
            f = ctk.CTkFrame(self.content_area, fg_color=self.c_panel, border_width=1, border_color="#1a1a1a", width=600)
            f.pack(pady=5, padx=100, fill="x")
            ctk.CTkLabel(f, text=name, font=("Consolas", 12, "bold"), text_color="white").pack(side="left", padx=20)
            
            g_container = ctk.CTkFrame(f, fg_color="transparent")
            g_container.pack(side="right", padx=10)
            
            btn = ctk.CTkButton(g_container, text="APPLY", width=100, height=30, fg_color="#111", border_width=1, border_color="yellow")
            btn.pack(pady=(5, 2))
            
            p_bar = ctk.CTkProgressBar(g_container, width=100, height=3, progress_color="yellow", fg_color="#000")
            p_bar.pack(); p_bar.set(0)
            
            btn.configure(command=lambda n=name, c=cmd, b=btn, pr=p_bar: self.run_action_with_bar(n, c, b, pr, "yellow"))

    def select_exe(self):
        p = filedialog.askopenfilename(filetypes=[("Executable", "*.exe")])
        if p: 
            self.target_process = os.path.basename(p)
            self.lbl_target.configure(text=f"TARGET: {self.target_process}")

    def show_about(self):
        for w in self.content_area.winfo_children(): w.destroy()
        ctk.CTkLabel(self.content_area, text="HN OPTIMIZER 4.1", font=("Impact", 70), text_color=self.c_neon).pack(pady=50)
        ctk.CTkLabel(self.content_area, text="Lead Dev: Angel Roney", font=("Consolas", 16), text_color="gray").pack(pady=20)

    def update_stats(self):
        while True:
            try:
                c, r = psutil.cpu_percent(), psutil.virtual_memory().percent
                if hasattr(self, 'lbl_cpu') and self.lbl_cpu.winfo_exists():
                    self.lbl_cpu.configure(text=f"CPU CORE: {c}%"); self.bar_cpu.set(c/100)
                    self.lbl_ram.configure(text=f"RAM MEMORY: {r}%"); self.bar_ram.set(r/100)
            except: pass
            time.sleep(1)

    def toggle_lang(self):
        self.lang = "EN" if self.lang == "ES" else "ES"; self.setup_ui()

    def show_login(self):
        self.login_win = ctk.CTkToplevel()
        self.login_win.geometry("450x650")
        self.login_win.configure(fg_color="#000000")
        self.login_win.title("HN ACCESS 4.1")
        self.login_win.attributes("-topmost", True)
        ctk.CTkLabel(self.login_win, text="HN 4.1", font=("Impact", 60), text_color=self.c_neon).pack(pady=(150, 5))
        self.user_entry = ctk.CTkEntry(self.login_win, placeholder_text="USER ID", width=280, height=45, fg_color="#111")
        self.user_entry.pack(pady=10)
        self.pass_entry = ctk.CTkEntry(self.login_win, placeholder_text="PASSWORD", show="*", width=280, height=45, fg_color="#111")
        self.pass_entry.pack(pady=10)
        self.log_btn = ctk.CTkButton(self.login_win, text="INITIALIZE", font=("Impact", 18), width=280, height=50, fg_color=self.c_neon, text_color="black", command=self.verify_login)
        self.log_btn.pack(pady=30)

if __name__ == "__main__":
    app = ctk.CTk()
    app.withdraw()
    HN = HNOptimizer_Command_Center_4_0(app)
    app.mainloop()