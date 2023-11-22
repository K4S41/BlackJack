import tkinter as tk
from sys import exit
from configparser import ConfigParser
#import own moduls
from language import dict_en_cz
import g_table
#config file loading
config = ConfigParser()
config.read("config.ini")
#to define default variables from config.ini
num_pack10 = int(config["Settings"]["packages"])
starting_budget20 = int(config["Settings"]["budget"])
b_strategy30 = bool(config["Settings"]["strategy"])
lang40 = int(config["Settings"]["language"])


#update config.ini data
def config_update():
  global num_pack10, starting_budget20, b_strategy30, lang40
  config = ConfigParser()
  config.read("config.ini")
  num_pack10 = int(config["Settings"]["packages"])
  starting_budget20 = int(config["Settings"]["budget"])
  b_strategy30 = int(config["Settings"]["strategy"])
  lang40 = int(config["Settings"]["language"])


#create settings menu panel
def create_settings_menu(amenu_bg_color="#ddddee"):
  global dict_en_cz

  #create button for set state save and for window leave
  def save_and_close_settings():
    config["Settings"] = {
        "packages": num_pack10_var.get(),
        "budget": starting_budget20_var.get(),
        "strategy": b_strategy30_var.get(),
        "language": lang40_var.get()
    }

    with open("config.ini", "w") as setup:
      config.write(setup)
    settings_panel.destroy()
    config_update()
    create_main_menu(amenu_bg_color="#ddddee")


  settings_panel = tk.Tk()
  # to get widget into screen center
  screen_width = settings_panel.winfo_screenwidth()
  screen_height = settings_panel.winfo_screenheight()
  panel_width = 250
  panel_height = 300
  settings_panel.geometry(
      f"{panel_width}x{panel_height}+{int((screen_width - panel_width) / 2)}+{int((screen_height - panel_height) / 2)}"
  )
  # main menu widget configuration
  settings_panel.title(dict_en_cz["settings"][lang40])
  settings_panel.resizable(False, False)
  settings_panel.configure(background=amenu_bg_color)
  settings_panel.protocol("WM_DELETE_WINDOW", lambda: settings_panel.destroy())
  # definition of variables used to configure buttons and labels (background color and font)
  bgcolor = amenu_bg_color
  label_font = ("Arial", 10, "bold")
  button_font = ("Arial", 10)

  # defining variables and for monitoring the state of numeric values ​​and checkboxes and setting a one-time default value
  num_pack10_var = tk.IntVar(value=num_pack10)
  starting_budget20_var = tk.IntVar(value=starting_budget20)
  b_strategy30_var = tk.IntVar(value=b_strategy30)
  lang40_var = tk.IntVar(value=lang40)

  # choose number of packages mixed into drawing deck (4 options)
  label10 = tk.Label(settings_panel,
                     text=(dict_en_cz["number_of_packages"][lang40]),
                     font=label_font,
                     bg=bgcolor)
  option11 = tk.Radiobutton(settings_panel,
                            text="2",
                            font=button_font,
                            variable=num_pack10_var,
                            bg=amenu_bg_color,
                            value=2,
                            command=lambda: num_pack10_var.get())
  option12 = tk.Radiobutton(settings_panel,
                            text="4",
                            font=button_font,
                            variable=num_pack10_var,
                            bg=amenu_bg_color,
                            value=4,
                            command=lambda: num_pack10_var.get())
  option13 = tk.Radiobutton(settings_panel,
                            text="6",
                            font=button_font,
                            variable=num_pack10_var,
                            bg=amenu_bg_color,
                            value=6,
                            command=lambda: num_pack10_var.get())
  option14 = tk.Radiobutton(settings_panel,
                            text="8",
                            font=button_font,
                            variable=num_pack10_var,
                            bg=amenu_bg_color,
                            value=8,
                            command=lambda: num_pack10_var.get())
  #label and buttons placing
  label10.grid(row=2, column=2, columnspan=8, sticky="w", pady=5, padx=10)
  option11.grid(row=4, column=2, sticky="w")
  option12.grid(row=4, column=4, sticky="w")
  option13.grid(row=4, column=6, sticky="w")
  option14.grid(row=4, column=8, sticky="w")

  # starting budget setting (4 options)
  label20 = tk.Label(settings_panel,
                     text=dict_en_cz["budget"][lang40],
                     font=label_font,
                     bg=bgcolor)
  option21 = tk.Radiobutton(settings_panel,
                            text="$1 ",
                            font=button_font,
                            variable=starting_budget20_var,
                            bg=amenu_bg_color,
                            value=1,
                            command=lambda: starting_budget20_var.get())
  option22 = tk.Radiobutton(settings_panel,
                            text="$5 ",
                            font=button_font,
                            variable=starting_budget20_var,
                            bg=amenu_bg_color,
                            value=5,
                            command=lambda: starting_budget20_var.get())
  option23 = tk.Radiobutton(settings_panel,
                            text="$10",
                            font=button_font,
                            variable=starting_budget20_var,
                            bg=amenu_bg_color,
                            value=10,
                            command=lambda: starting_budget20_var.get())
  option24 = tk.Radiobutton(settings_panel,
                            text="$20",
                            font=button_font,
                            variable=starting_budget20_var,
                            bg=amenu_bg_color,
                            value=20,
                            command=lambda: starting_budget20_var.get())
  #label and buttons placing
  label20.grid(row=6, column=2, columnspan=8, sticky="w", pady=5, padx=10)
  option21.grid(row=8, column=2, sticky="w")
  option22.grid(row=8, column=4, sticky="w")
  option23.grid(row=8, column=6, sticky="w")
  option24.grid(row=8, column=8, sticky="w")

  # basic strategy panel turn on/off
  label30 = tk.Label(settings_panel,
                     text=dict_en_cz["strategy"][lang40],
                     font=label_font,
                     bg=bgcolor)
  checkbox31 = tk.Checkbutton(settings_panel,
                              text=dict_en_cz["on_off"][lang40],
                              font=button_font,
                              bg=amenu_bg_color,
                              variable=b_strategy30_var,
                              command=lambda: b_strategy30_var.get())
  #checkbox placing
  label30.grid(row=10, column=2, columnspan=8, sticky="w", pady=5, padx=10)
  checkbox31.grid(row=12, column=2, columnspan=8, sticky="w")

  #program language switch
  label40 = tk.Label(settings_panel,
                     text=dict_en_cz["language"][lang40],
                     font=label_font,
                     bg=bgcolor)
  #choose English
  option41 = tk.Radiobutton(settings_panel,
                            text="EN",
                            font=button_font,
                            bg=amenu_bg_color,
                            value=0,
                            variable=lang40_var,
                            command=lambda: lang40_var.get())
  #choose Czech
  option42 = tk.Radiobutton(settings_panel,
                            text="CZ",
                            font=button_font,
                            bg=amenu_bg_color,
                            value=1,
                            variable=lang40_var,
                            command=lambda: lang40_var.get())
  #label and buttons placing
  label40.grid(row=14, column=2, columnspan=8, sticky="w", pady=5, padx=10)
  option41.grid(row=16, column=2, sticky="w")
  option42.grid(row=16, column=4, sticky="w")

  #save and back to the main menu button
  button50 = tk.Button(settings_panel,
                       text=dict_en_cz["save_and_back"][lang40],
                       font=label_font,
                       bg="#ccccff",
                       command=lambda: save_and_close_settings())
  #button placing
  button50.grid(row=18, column=2, columnspan=8, sticky="w", pady=30, padx=10)
  settings_panel.mainloop()


#show information about program author
def show_the_author():
  global language
  panel = tk.Toplevel()
  panel_width = 350
  panel_height = 110
  label_font = ("Arial", 10, "bold")
  bgcolor = "#ddddee"
  # to get widget into screen center
  screen_width = panel.winfo_screenwidth()
  screen_height = panel.winfo_screenheight()
  panel.geometry(
      f"{panel_width}x{panel_height}+{int((screen_width-panel_width)/2)}+{int((screen_height-panel_height)/2)}"
  )
  #author widget configuration
  panel.configure(bg=bgcolor)
  panel.title(dict_en_cz["author"][lang40])
  #panel.iconbitmap("./cards/AS.ico") - doesn´t run
  panel.resizable(False, False)
  panel.protocol("WM_DELETE_WINDOW", lambda: panel.destroy())
  panel.grab_set()

  #author widget contact data
  author_info_list = [[dict_en_cz["created_by"][lang40], "Petr Kašička"],
                      ["Mail: ", "K4S4@email.cz"],
                      ["LinkedIn: ", "www.linkedin.com/in/p-kasicka"]]
  ilist = author_info_list
  #label creating
  label00 = tk.Label(panel, text=ilist[0][0], font=label_font, bg=bgcolor)
  label01 = tk.Label(panel, text=ilist[0][1], font=label_font, bg=bgcolor)
  label10 = tk.Label(panel, text=ilist[1][0], font=label_font, bg=bgcolor)
  label11 = tk.Label(panel, text=ilist[1][1], font=label_font, bg=bgcolor)
  label20 = tk.Label(panel, text=ilist[2][0], font=label_font, bg=bgcolor)
  label21 = tk.Label(panel, text=ilist[2][1], font=label_font, bg=bgcolor)
  #label placing - "w" = "west"
  label00.grid(row=2, column=2, sticky="w")
  label01.grid(row=2, column=4, sticky="w")
  label10.grid(row=4, column=2, sticky="w")
  label11.grid(row=4, column=4, sticky="w")
  label20.grid(row=6, column=2, sticky="w")
  label21.grid(row=6, column=4, sticky="w")
  #create close button 
  exit_button = tk.Button(panel,
                          text=dict_en_cz["close"][lang40],
                          width=11,
                          font=("Arial", 10, "bold"),
                          border=3,
                          bg="#ccccff",
                          command=panel.destroy)
  exit_button.place(x=120, y=70)


#create main menu widget
def create_main_menu(atitle="Menu", amenu_bg_color="#ddddee"):
  global language

  # router function - will choose which window will be started
  def panel_switch(anew_window):
    main_panel.destroy()
    if anew_window == "ng":
      #function that lets you create a game window, deck of cards, players, user interface
      g_table.create_game_window()
    elif anew_window == "settings":
      create_settings_menu()

  main_panel = tk.Tk()
  # to get widget into screen center
  screen_width = main_panel.winfo_screenwidth()
  screen_height = main_panel.winfo_screenheight()
  panel_width = 250
  panel_height = 300
  main_panel.geometry(
      f"{panel_width}x{panel_height}+{int((screen_width-panel_width)/2)}+{int((screen_height-panel_height)/2)}"
  )
  #main menu window configuration
  main_panel.title(atitle)
  #main_panel.iconbitmap("./cards/AS.ico") - doesn´t work
  main_panel.resizable(False, False)
  main_panel.configure(background=amenu_bg_color)
  main_panel.protocol("WM_DELETE_WINDOW", lambda: main_panel.destroy())
  # create main menu buttons
  # "new game" button
  button1 = tk.Button(main_panel,
                      bg="#ccccff",
                      text=dict_en_cz["new_game"][lang40],
                      width=11,
                      height=1,
                      font=("Arial", 10, "bold"),
                      border=3,
                      command=lambda: panel_switch("ng"))
  # "setting" button
  button2 = tk.Button(main_panel,
                      bg="#ccccff",
                      text=dict_en_cz["settings"][lang40],
                      width=11,
                      height=1,
                      font=("Arial", 10, "bold"),
                      border=3,
                      command=lambda: panel_switch("settings"))
  # "show info about author" button
  button3 = tk.Button(main_panel,
                      bg="#ccccff",
                      text=dict_en_cz["author"][lang40],
                      width=11,
                      height=1,
                      font=("Arial", 10, "bold"),
                      border=3,
                      command=lambda: show_the_author())
  # "shut down the program" button
  button4 = tk.Button(main_panel,
                      bg="#ccccff",
                      text=dict_en_cz["quit"][lang40],
                      width=11,
                      height=1,
                      font=("Arial", 10, "bold"),
                      border=3,
                      command=lambda: exit())
  # buttons placing
  button1.place(x=75, y=30)
  button2.place(x=75, y=80)
  button3.place(x=75, y=130)
  button4.place(x=75, y=180)

  main_panel.mainloop()
