import tkinter
import customtkinter

# customtkinter.set_appearance_mode("System")
# customtkinter.set_default_color_theme("blue") 

# class LeftFrame(customtkinter.CTkFrame):
#     def __init__(self, *args, header_name="LeftFrame", **kwargs):
#         super().__init__(*args, **kwargs)

#         self.header_name = header_name

#         self.header = customtkinter.CTkLabel(self, text=self.header_name)
#         self.header.grid(row=0, column=0, padx=10, pady=10)

#         self.radio_button_var = customtkinter.StringVar(value="")



class PathFinder(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Make the window
        self.title("Shortest Path Finder")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (2x2)
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0, 1), weight=1)

        # Create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=2, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(3, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Tucil 2 Stima", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=10, pady=(10,20))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_1_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=10, pady=20)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Apperance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=3, column=0, padx=10, pady=(10,0))
        self.appearance_mode_optionMenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark"],
                                                                      command=self.change_appearance_mode_event)
        self.appearance_mode_optionMenu.grid(row=4, column=0, padx=10, pady=(10,10))

        # Set default values
        self.appearance_mode_optionMenu.set("Dark")
        
    
    def sidebar_button_1_event(self):
        print("Sidebar Button Click")

    def change_appearance_mode_event(self, new_apperance_mode: str):
        customtkinter.set_appearance_mode(new_apperance_mode)





if __name__ == "__main__":
    app = PathFinder()
    app.mainloop()