import customtkinter as ctk
import webbrowser

class GuessNumberUi(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Guess Number Game")

        #---------------Window Game Settings---------------
        width = 800
        height = 500
        self.geometry(f"{width}x{height}")
        self.update_idletasks()
        screen_width=self.winfo_screenwidth()
        screen_height=self.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.geometry(f"{width}x{height}+{x}+{y}")
        self.minsize(width, height)

        #---------------Frame Weight Settings---------------
        self.grid_columnconfigure(0, weight=0, minsize=250)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        #---------------Create Left Frame (Settings)---------------
        self.frame_settings = ctk.CTkFrame(self,width=250,height=500,corner_radius=3)
        self.frame_settings.grid(column=0, row=0,sticky="nsew",padx=(10,5),pady=10)
        self.frame_settings.grid_propagate(False)

        #---------------Title Left Frame (Settings)---------------
        settings_title = ctk.CTkLabel(self.frame_settings,text="Settings",font=("Arial",20,"bold"))
        settings_title.pack(padx=5,pady=5)
        line_settings1 = ctk.CTkFrame(self.frame_settings, height=4)
        line_settings1.pack(fill="x", padx=15)

        # ---------------Difficulty(Settings)---------------
        diff_title = ctk.CTkLabel(self.frame_settings, text="Difficulty", font=("Arial", 16))
        diff_title.pack(pady=10)
        segment_frame = ctk.CTkFrame(self.frame_settings,fg_color="transparent")
        segment_frame.pack(fill="x",pady=(0,17),padx=5)
        self.difficulty_var = ctk.StringVar(value="Easy")
        self.difficulty_segment = ctk.CTkSegmentedButton(segment_frame,
                                              values=["Easy", "Normal", "Hard"],
                                              variable=self.difficulty_var,
                                              corner_radius=8,
                                              height=33,
                                              )
        self.difficulty_segment.pack(fill="x",padx=17)
        line_settings2 = ctk.CTkFrame(self.frame_settings, height=2)
        line_settings2.pack(fill="x", padx=15)

        # ---------------Hint(Settings)---------------
        hint_title = ctk.CTkLabel(self.frame_settings, text="Hint", font=("Arial", 16))
        hint_title.pack(pady=10)
        hint_frame = ctk.CTkFrame(self.frame_settings, fg_color="transparent")
        hint_frame.pack(pady=(4, 15))
        self.hint_var = ctk.StringVar(value="on")
        radio_btn1 = ctk.CTkRadioButton(hint_frame, text="On",width=50,value="on",variable=self.hint_var)
        radio_btn1.grid(column=0, row=0,padx=15)
        radio_btn2 = ctk.CTkRadioButton(hint_frame, text="Off",width=50,value="off",variable=self.hint_var)
        radio_btn2.grid(column=1, row=0,padx=15)
        line_settings3 = ctk.CTkFrame(self.frame_settings, height=2)
        line_settings3.pack(fill="x", padx=15)

        # ---------------Window Theme(Settings)---------------
        theme_title = ctk.CTkLabel(self.frame_settings, text="Window Theme", font=("Arial", 16))
        theme_title.pack(pady=10)
        theme_frame = ctk.CTkFrame(self.frame_settings, fg_color="transparent")
        theme_frame.pack(pady=(4, 15))
        self.btn_dark = ctk.CTkButton(theme_frame, text="Dark",width=70)
        self.btn_dark.grid(column=0, row=0,padx=(0,10))
        self.btn_light = ctk.CTkButton(theme_frame, text="Light",width=70)
        self.btn_light.grid(column=1, row=0,padx=(10,0))

        # ---------------Right Frame (Game)---------------
        self.frame_game = ctk.CTkFrame(self,corner_radius=3)
        self.frame_game.grid(column=1, row=0,sticky="nsew",padx=(5,10),pady=10)
        game_title = ctk.CTkLabel(self.frame_game, text="Guess Number Game", font=("Arial", 20, "bold"))
        game_title.pack(pady=5)
        line_game = ctk.CTkFrame(self.frame_game, height=4)
        line_game.pack(fill="x", padx=15)

        # ---------------Guess title/input (Game)---------------
        title_guess = ctk.CTkLabel(self.frame_game,text="Guess The Number ?", font=("Arial", 18))
        title_guess.pack(pady=(35,5))
        info_range = ctk.CTkLabel(self.frame_game, text="Enter a Number Between 1 - 100", font=("Arial", 13))
        info_range.pack()
        self.guess_entry = ctk.CTkEntry(self.frame_game, width=75,justify="center")
        self.guess_entry.pack(pady=15)

        # ---------------Label Hint/Count (Game)---------------
        self.count_label = ctk.CTkLabel(self.frame_game, text="You Have 20 Chance To Guess", font=("Arial", 13))
        self.count_label.pack()
        self.hint_label = ctk.CTkLabel(self.frame_game, text="Guess It? Im Waiting...  ", font=("Arial", 13))
        self.hint_label.pack()

        # ---------------Guess Button/NewGame/Exit (Game)---------------
        self.frame_btn_game = ctk.CTkFrame(self.frame_game,fg_color="transparent")
        self.frame_btn_game.pack()
        self.guess_btn = ctk.CTkButton(self.frame_btn_game, text="Guess", width=100)
        self.guess_btn.grid(column=0, row=0, pady=8)
        self.newgame_btn = ctk.CTkButton(self.frame_btn_game, text="New Game",width=50)
        self.newgame_btn.grid(column=0, row=1, pady=8)
        self.exit_btn = ctk.CTkButton(self.frame_btn_game, text="Exit",width=50)
        self.exit_btn.grid(column=0, row=2, pady=8)

        # ---------------Tag Developer  (Game)---------------
        dev_info = ctk.CTkLabel(self.frame_game,text="Developed by MonkeyxDev",text_color=("black","white"),cursor="hand2",font=("Arial",16))
        dev_info.pack(side="bottom", pady=10)
        def on_enter(e):
            dev_info.configure(text_color="#1a0dab")

        def on_leave(e):
            dev_info.configure(text_color=("black","white"))

        def open_link(e=None):
            webbrowser.open("https://github.com/MonkeyxDev")
        dev_info.bind("<Enter>", on_enter)
        dev_info.bind("<Leave>", on_leave)
        dev_info.bind("<Button-1>", open_link)

        # ---------------Status Bar---------------
        self.my_status_title = ctk.CTkLabel(self.frame_settings, text="Details", font=("Arial", 24, "bold"), anchor="w", corner_radius=5, fg_color="#ABABAB", text_color="black")
        self.my_status_title.pack(fill="x", side="top", ipady=2)
        self.my_status = ctk.CTkLabel(self.frame_settings, width=150, height=150, font=("Arial", 16), text="Hints: On\nDifficulty: Easy", anchor="center", corner_radius=5, fg_color="#ABABAB", text_color="black")
        self.my_status.pack(fill="x", side="bottom", ipady=2)




class OkMessage(ctk.CTkToplevel):
    def __init__(self, master, title, message):
        super().__init__(master)
        self.title(title)
        self.resizable(False, False)
        width = 200
        height = 100
        self.geometry(f"{width}x{height}")
        self.update_idletasks()
        master_x = master.winfo_x()
        master_y = master.winfo_y()
        master_width = master.winfo_width()
        master_height = master.winfo_height()
        x = master_x +(master_width - width) // 2
        y = master_y + (master_height - height) // 2
        self.geometry(f"{width}x{height}+{x}+{y}")
        self.minsize(width, height)
        ctk.CTkLabel(self, text=message, font=("Arial", 15)).pack(pady=(20,0))
        ctk.CTkButton(self, text="OK", width=80, command=self.destroy).pack(pady=10)
        self.grab_set()