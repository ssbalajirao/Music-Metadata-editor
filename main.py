import customtkinter as ct

g_app = ct.CTk()

# g_app title and geometry
g_app.title("Music Tinker")
g_app.geometry("800x800")


g_button = ct.CTkButton(g_app, text = "Test button")

g_app.mainloop()