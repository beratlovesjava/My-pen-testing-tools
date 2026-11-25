import customtkinter
import webbrowser

sg = customtkinter.CTk()
sg.title("ShotGun Hash cracker")
sg.resizable(False, False)
sg.configure(fg_color="#000000")
sg.geometry("1000x500")

def github_link():
    webbrowser.open_new_tab("https://github.com/beratlovesjava/Shotgun-python-hashcracker")

shotgun_art = r"""
    ,______________________________________       
   |_________________,----------._ [____]  ""-,__  __....-----=====
                  (_(||||||||||||)___________/   ""                |
                     `----------'        [ ))"-,                   |
                                          ""    `,  _,--....___    |
                                                  `/           
"""

ascii_label = customtkinter.CTkLabel(
    sg,
    text=shotgun_art,
    font=("Courier", 12, "bold"),
    text_color="#00FF00",
    justify="left"
)
ascii_label.pack(pady=(40, 10))

label = customtkinter.CTkLabel(
    sg,
    text="Welcome to Shotgun hash cracker! (Press enter to continue)",
    font=("Courier", 14, "bold"),
    text_color="#00FF00",
)
label.pack(pady=(10, 20))

start = customtkinter.CTkButton(
    sg,
    text="Start",
    font=("Courier", 14, "bold"),
    text_color="#00FF00",
    fg_color="#000000",
    border_color="#00FF00",
    border_width=2,
    hover_color="#003300"
)
start.pack(pady=10)

github = customtkinter.CTkButton(
    sg,
    text="GitHub",
    font=("Courier", 14, "bold"),
    text_color="#00FF00",
    fg_color="#000000",
    border_color="#00FF00",
    border_width=2,
    hover_color="#003300",
    command=github_link
)
github.pack(pady=30)

sg.mainloop()
