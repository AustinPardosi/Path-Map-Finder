from tkinter import filedialog, Canvas
from PIL import ImageTk, Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from tkintermapview import TkinterMapView
import matplotlib.pyplot as plt
import customtkinter
import tkinter
import tkinter as tk
import os
import networkx as nx
import parse_into_graph as p
import algorithm as a
from algorithm import UCS, aStar

customtkinter.set_default_color_theme("blue") 

# Digunakan untuk membuka path gambar untuk logo pada button
PATH = os.path.dirname(os.path.realpath(__file__))

class PathFinder(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Make the window
        self.title("Path Map Finder")
        self.geometry(f"{1100}x{580}")

        # Configure grid layout (1x2)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Configure image
        self.add_folder_image = self.load_image("\\..\\img\\add_folder.png", 30)
        self.execute_image = self.load_image("\\..\\img\\execute.png", 30)

        # Create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, corner_radius=10, width=200)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew", padx=(20,0), pady=20)
        self.sidebar_frame.grid_rowconfigure(15, weight=1) #frame maksimal
        self.sidebar_frame.grid_rowconfigure(12, weight=20)

        # Create Main Label
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Path Map Finder", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=10, pady=(20,20))

        # Create Insert File Button
        self.file_is_selected = False;
        self.Map_label = customtkinter.CTkLabel(self.sidebar_frame, text="Select Map: ", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.Map_label.grid(row=1, column=0, padx=25, pady=(20,0), sticky="w")
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, height=40, width=130, image=self.add_folder_image, text="Insert File", command=self.select_map)
        self.sidebar_button_1.grid(row=2, column=0, padx=10, pady=(10,5))
        self.file_info = customtkinter.CTkLabel(self.sidebar_frame, text="")
        self.file_info.grid(row=3, column=0, padx=0, pady=0, sticky="n")

        # Create combobox 
        self.Node_label = customtkinter.CTkLabel(self.sidebar_frame, text="Nodes Search: ", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.Node_label.grid(row=4, column=0, padx=25, pady=(30,0), sticky="w")
        self.combobox_1 = customtkinter.CTkComboBox(values=[""], master= self.sidebar_frame)
        self.combobox_1.grid(row=5, column=0, padx=0, pady=10)
        self.combobox_2 = customtkinter.CTkComboBox(values=[""], master= self.sidebar_frame,)
        self.combobox_2.grid(row=6, column=0, padx=0, pady=10)

        # Create Radiobutton
        self.radio_var = tkinter.IntVar(value=0)
        self.label_radio_group = customtkinter.CTkLabel(self.sidebar_frame, text="Algorithm:", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_radio_group.grid(row=7, column=0, padx=30, pady=(40,0), sticky="w")
        self.radio_button_1 = customtkinter.CTkRadioButton(self.sidebar_frame, variable=self.radio_var, value=0, text="A*")
        self.radio_button_1.grid(row=8, column=0, padx=40, pady=10, sticky="nw")
        self.radio_button_2 = customtkinter.CTkRadioButton(self.sidebar_frame, variable=self.radio_var, value=1, text="UCS")
        self.radio_button_2.grid(row=9, column=0, padx=40, pady=10, sticky="nw")

        # Create Button
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, height=40, width=130, text="Execute", image=self.execute_image, command=self.execute)
        self.sidebar_button_2.grid(row=10, column=0, padx=10, pady=(40,5))
        self.error_info = customtkinter.CTkLabel(self.sidebar_frame, text="")
        self.error_info.grid(row=11, column=0, padx=0, pady=0, sticky="n")

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Theme Mode:", anchor="w",font=customtkinter.CTkFont(size=15, weight="bold"))
        self.appearance_mode_label.grid(row=13, column=0, padx=0, pady=(10,0), sticky="s")
        self.appearance_mode_optionMenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionMenu.grid(row=14, column=0, padx=10, pady=(10,10))

        # Create main frame with visualization
        self.main_frame = customtkinter.CTkFrame(self, corner_radius=10)
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        # create tabview
        self.tabview = customtkinter.CTkTabview(self.main_frame, width=1230, height=700)
        self.tabview.grid(row=0, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("Graph")
        self.tabview.add("Map")
        self.tabview.tab("Graph").grid_columnconfigure(2, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Graph").grid_rowconfigure(20, weight=10)  # configure grid of individual tabs
        self.tabview.tab("Map").grid_columnconfigure(3, weight=1)

        # Create Answer label
        self.algorithm_label = customtkinter.CTkLabel(self.tabview.tab("Graph"), text="")
        self.algorithm_label.grid(row=0, column=0, padx=50, pady=(20,20))

        # Create a frame to hold the graph
        self.graph_frame = customtkinter.CTkFrame(self.tabview.tab("Graph"), corner_radius=10)
        self.graph_frame.grid(row=1, column=0, padx=50, pady=(20,20))

        # Create a place to put the graph
        self.place = customtkinter.CTkFrame(self.graph_frame, corner_radius=10)
        self.place.pack(expand=True, fill=tk.BOTH, anchor=tk.CENTER)

        # Create Graph Info Label
        self.result_label = customtkinter.CTkLabel(self.tabview.tab("Graph"), text="", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.result_label.grid(row=0, column=2)
        self.graph_path_label = customtkinter.CTkLabel(self.tabview.tab("Graph"), text="", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.graph_path_label.grid(row=1, column=2, sticky="nw")
        self.cost_label = customtkinter.CTkLabel(self.tabview.tab("Graph"), text="", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.cost_label.grid(row=2, column=2, sticky="nw")

        # Set default values
        self.appearance_mode_optionMenu.set("Dark")
        self.combobox_1.set("Start")
        self.combobox_2.set("Goal")

    def change_appearance_mode_event(self, new_apperance_mode: str):
        customtkinter.set_appearance_mode(new_apperance_mode)

     # Fungsi untuk mengambil gambar logo
    def load_image(self, path, image_size):
        return ImageTk.PhotoImage(Image.open(PATH + path).resize((image_size, image_size)))
        
    def select_map(self):
        self.file_is_selected = False;
        self.mapName = filedialog.askopenfilename(title="Select a map", filetypes=(("txt files", "*.txt"), ("All Files", "*.*")))
        self.file_name = os.path.basename(self.mapName)
        self.file_ext = os.path.splitext(self.mapName)[1] # Mengambil ekstensi file
        self.combobox_1.configure(values=[""])
        self.combobox_2.configure(values=[""])
        if (self.file_ext==".txt"):
            self.file_is_selected = True;
            self.file_info.configure(text=self.file_name, text_color="green")
            self.mtr, self.nodes, self.listnodes = p.parse_into_adjacency_mtr(self.mapName)
            self.node_coords = [self.nodes[label] for label in self.listnodes]
            array = []
            for node in self.listnodes:
                array.append(node)
            self.combobox_1.configure(values=array)
            self.combobox_2.configure(values=array)
        else:
            self.file_info.configure(text="Wrong Input File!", text_color="red",  font=customtkinter.CTkFont(size=15, weight="bold"))

    def execute(self):
        selected_value = self.radio_var.get()
        value1 = self.combobox_1.get()
        value2 = self.combobox_2.get()
        if (self.file_is_selected==False) :
            self.error_info.configure(text="Insert File!", text_color="red", font=customtkinter.CTkFont(size=15, weight="bold"))
        else :
            self.error_info.configure(text="")
            if (value1 == "Start" or value2 == "Goal"):
                self.error_info.configure(text="Select Nodes Search!", text_color="red", font=customtkinter.CTkFont(size=15, weight="bold"))
            else:
                if (selected_value == 0) :
                    self.algorithm_label.configure(text="A* Algorithm Result", text_color="white",  font=customtkinter.CTkFont(size=30, weight="bold"))
                    self.visualizeGraph()
                    self.path, self.cost = aStar.astar(value1, value2, self.graph, self.nodes, True)
                    self.visualizeInfo()
                    print("Run A*")
                elif (selected_value == 1) :
                    self.algorithm_label.configure(text="UCS Algorithm Result", text_color="white",  font=customtkinter.CTkFont(size=30, weight="bold"))
                    self.visualizeGraph()
                    self.path, self.cost = UCS.ucs(value1, value2, self.graph)
                    self.visualizeInfo()

    def visualizeGraph(self):
        self.graph = p.parse_adjacency_matrix(self.mtr)
        if hasattr(self, "fig"):
            self.ax.clear() 
        else:
            self.fig = plt.figure(figsize=(5, 5))
            self.ax = self.fig.add_subplot(111)
        pos = {label: coord for label, coord in zip(self.listnodes, self.node_coords)}
        nx.draw(self.graph, pos, with_labels=True, ax=self.ax)
        if hasattr(self, "canvas"):
            self.canvas.draw_idle()
        else:
            canvas = FigureCanvasTkAgg(self.fig, master=self.place)
            canvas.draw()
            canvas.get_tk_widget().pack(expand=True)
            self.canvas = canvas

    def visualizeInfo(self):
        self.result_label.configure(text="Result", text_color="white",  font=customtkinter.CTkFont(size=30, weight="bold"))
        self.graph_path_label.configure(text="Path = " + ' - '.join(self.path))
        self.cost_label.configure(text="Distance = " + str(self.cost))


if __name__ == "__main__":
    app = PathFinder()
    app.mainloop()