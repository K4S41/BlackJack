import tkinter as tk
import random
from time import sleep
from sys import exit
from PIL import Image, ImageTk
from language import dict_en_cz
from configparser import ConfigParser
#config.ini data loading
config = ConfigParser()
config.read("config.ini")
#definition of default variables from config.ini
num_pack10 = int(config["Settings"]["packages"])
starting_budget20 = int(config["Settings"]["budget"])
b_strategy30 = bool(config["Settings"]["strategy"])
lang40 = int(config["Settings"]["language"])

#main window creating
#===============================================================================
class CGameTable:
  #--------------------------------------------------------------------------------
  def __init__(self, amenu_bg_color="#228822",abutt_bg_color="#ccccff",abutton_state=True):
    self.bg_color=amenu_bg_color
    #game interface crating - board
    self.button_state = abutton_state
    config.read("config.ini")
    lang40 = int(config["Settings"]["language"])
    self.table = tk.Tk()
    self.table.title("BlackJackGame")
    self.table.configure(background=self.bg_color)
    self.table.resizable(False, False)
    self.table.protocol("WM_DELETE_WINDOW", lambda: self.table.destroy())
    #game window size
    self.table_width = 800
    self.table_height = 600
    screen_width = self.table.winfo_screenwidth()
    screen_height = self.table.winfo_screenheight()
    #get game window into screen center
    self.table.geometry(
        f"{self.table_width}x{self.table_height}+{int((screen_width - self.table_width)/2)}+{int((screen_height - self.table_height)/2)}")
    
    #create dealer
    self.dealer = CPlayer()
    
    #create player1
    self.player1=CPlayer()

    #create player2 (player1 split hand)
    self.player2=CPlayer()

    #create drawing deck
    self.drawing_deck = CDeck(anum_decks=num_pack10)

    #create discard deck
    self.discard_deck = CDeck(anum_decks=0)

    #returns the active player's hand
    self.activ = self.player1.hand

    #create game menu panel

    self.table_game_menu = tk.Canvas(self.table,
                                     width=self.table_width,
                                     height=self.table_height / 8,
                                     bg="#ddddff")
    #bottom menu border 
    self.table_game_menu.create_line(0,
                                     2,
                                     self.table_width,
                                     2,
                                     fill="#000000",
                                     width=2)  
    self.table_game_menu.place(x=0,
                               y=self.table_height - self.table_height / 8)

    #create game buttons
    #button "deal cards"
    self.deal_button = tk.Button(self.table,
                                 text="Deal",
                                 font=("Arial", 10, "bold"),
                                 width=8,
                                 border=2,
                                 state=tk.NORMAL,
                                 bg=abutt_bg_color,
                                 command=lambda: self.deal_cards())
    # button "draw a new card"
    self.hit_button = tk.Button(self.table,
                                text="Hit",
                                font=("Arial", 10, "bold"),
                                width=8,
                                border=2,
                                state=tk.DISABLED,
                                bg=abutt_bg_color,
                                command=lambda: self.hit())
    # button "stand"
    self.stand_button = tk.Button(self.table,
                                  text="Stand",
                                  font=("Arial", 10, "bold"),
                                  width=8,
                                  border=2,
                                  bg=abutt_bg_color,
                                  state=tk.DISABLED,
                                  command= lambda: print(
                                    self.dealer.player_id,
                                    self.player1.player_id,
                                    self.player2.player_id))
    # button "double your bet"
    self.double_button = tk.Button(self.table,
                                   text="Double",
                                   font=("Arial", 10, "bold"),
                                   width=8,
                                   border=2,
                                   state=tk.DISABLED,
                                   bg=abutt_bg_color,
                                   command=lambda: self.double_down())
    # button "split your cards"
    self.split_button = tk.Button(self.table,
                                  text="Split",
                                  font=("Arial", 10, "bold"),
                                  width=8,
                                  border=2,
                                  state=tk.DISABLED,
                                  bg=abutt_bg_color,
                                  command=lambda: self.split())
    # button "use insurance"
    self.insurance_button = tk.Button(self.table,
                                      text="Insurance",
                                      font=("Arial", 10, "bold"),
                                      width=8,
                                      border=2,
                                      state=tk.DISABLED,
                                      bg=abutt_bg_color,)

    #create (object) popup windows with button function label
    CWidgetInfo(self.deal_button, "deal_button_note")
    CWidgetInfo(self.hit_button, "hit_button_note")
    CWidgetInfo(self.stand_button, "stand_button_note")
    CWidgetInfo(self.double_button, "double_button_note")
    CWidgetInfo(self.split_button, "split_button_note")
    CWidgetInfo(self.insurance_button, "insurance_button_note")
    #game buttons placing
    self.deal_button.place(
        x=(self.table_width / 7 - self.hit_button.winfo_reqwidth()) / 2,
        y=(self.table_height - self.table_height / 8) +
        (self.table_height / 8 - self.hit_button.winfo_reqheight()) / 2)
    self.hit_button.place(
        x=self.table_width / 7 +
        (self.table_width / 7 - self.hit_button.winfo_reqwidth()) / 2,
        y=(self.table_height - self.table_height / 8) +
        (self.table_height / 8 - self.hit_button.winfo_reqheight()) / 2)
    self.stand_button.place(
        x=self.table_width / 7 * 2 +
        (self.table_width / 7 - self.hit_button.winfo_reqwidth()) / 2,
        y=(self.table_height - self.table_height / 8) +
        (self.table_height / 8 - self.hit_button.winfo_reqheight()) / 2)
    self.double_button.place(
        x=self.table_width / 7 * 3 +
        (self.table_width / 7 - self.hit_button.winfo_reqwidth()) / 2,
        y=(self.table_height - self.table_height / 8) +
        (self.table_height / 8 - self.hit_button.winfo_reqheight()) / 2)
    self.split_button.place(
        x=self.table_width / 7 * 4 +
        (self.table_width / 7 - self.hit_button.winfo_reqwidth()) / 2,
        y=(self.table_height - self.table_height / 8) +
        (self.table_height / 8 - self.hit_button.winfo_reqheight()) / 2)
    self.insurance_button.place(
        x=self.table_width / 7 * 5 +
        (self.table_width / 7 - self.hit_button.winfo_reqwidth()) / 2,
        y=(self.table_height - self.table_height / 8) +
        (self.table_height / 8 - self.hit_button.winfo_reqheight()) / 2)

    #create display with info about your budget balance
    self.display_budget = tk.Label(
        self.table,
        text=
        f"{dict_en_cz['your'][lang40]} {dict_en_cz['budget'][lang40].lower()}${starting_budget20}",
        font=("Arial", 12, "bold"),
        bg=self.bg_color,
        foreground="#dddd00")
    self.display_budget.pack()
    #assign key ESC as 'escape' function
    self.table.bind(
        '<Escape>',
        lambda e, bg_color="#ddddee": CEscWin(bg_color))
  #--------------------------------------------------------------------------------
  #function to switch buttons, whether they are active or not 0 - off, 1 - on
  def button_states(self,ab_deal=1,ab_hit=0,ab_stand=0,ab_double=0,ab_split=0,ab_insurance=0):
    if ab_deal==1:self.deal_button.config(state=tk.NORMAL)
    else:self.deal_button.config(state=tk.DISABLED)
    if ab_hit==1:self.hit_button.config(state=tk.NORMAL)
    else:self.hit_button.config(state=tk.DISABLED)
    if ab_stand==1:self.stand_button.config(state=tk.NORMAL)
    else:self.stand_button.config(state=tk.DISABLED)
    if ab_double==1:self.double_button.config(state=tk.NORMAL)
    else:self.double_button.config(state=tk.DISABLED)
    if ab_split==1:self.split_button.config(state=tk.NORMAL)
    else:self.split_button.config(state=tk.DISABLED)
    if ab_insurance==1:self.insurance_button.config(state=tk.NORMAL)
    else:self.insurance_button.config(state=tk.DISABLED)

  #--------------------------------------------------------------------------------
  def deal_cards(self):
    #define variables for button_states arguments
    self.b_split = 0
    self.b_double = 0
    self.b_insurance = 0 
    #deal cards to dealer
    self.drawing_deck.move_card(self.dealer.hand, ay=50)
    #deal cards to player
    self.drawing_deck.move_card(self.player1.hand)
    self.drawing_deck.table_cleaner(self.player1.hand)
    self.drawing_deck.move_card(self.player1.hand)
    #determines whether the player won immediately
    if self.player1.hand.calculate_hand_value(self.player1.hand)==21:
      print("You have win!")
    #have player cards the same rank. if yes, it is possible to split this cards
    if self.player1.hand.cards[0].rank == self.player1.hand.cards[1].rank: 
      self.b_split = 1
    # if the sum of the cards dealt is 9, 10 or 11, it is possible to double down
    if 8<(self.player1.hand.cards[0].value + self.player1.hand.cards[1].value)<12:
      self.b_double = 1
    # button state setup - only split could change value
    if self.dealer.hand.cards[0].rank == "ace":
      self.b_insurance = 1
    self.button_states(0, 1, 1, self.b_double, self.b_split, self.b_insurance)

  #--------------------------------------------------------------------------------
  #this function will check if game state is not: immediatly lose or win 
  def lose_check(self):
    
    #auto-lose condition
    if self.activ.calculate_hand_value(self.activ)>21:
      print("Player1 have lose!")
       
    
  #--------------------------------------------------------------------------------
  #player draw new card
  def hit(self):
    self.drawing_deck.move_card(self.activ)

    self.lose_check()

  
  #--------------------------------------------------------------------------------
  # take just one more card and double your bet
  def double_down(self):
    self.drawing_deck.move_card(self.activ)

    self.lose_check()


  #--------------------------------------------------------------------------------
  # devide player hand into the two new decks
  def split(self):
    #hide card images after split
    self.split_cover=tk.Canvas(self.table,width=240,height=185,bg="#228822",bd=0,highlightthickness=0)
    self.split_cover.place(x=280,y=280)
    self.player1.hand.move_card(self.player2.hand)
    self.player1.hand.move_card(self.player1.hand)
    #player1 dealing a second card
    self.split_cover=tk.Canvas(self.table,width=240,height=185,bg="#228822",bd=0,highlightthickness=0)
    self.split_cover.place(x=80,y=280)
    self.drawing_deck.move_card(self.player1.hand)
    #player2 dealing a second (to second hand of player1)
    self.split_cover=tk.Canvas(self.table,width=240,height=185,bg="#228822",bd=0,highlightthickness=0)
    self.split_cover.place(x=480,y=280)
    self.drawing_deck.move_card(self.player2.hand)

    self.lose_check()

#===============================================================================
#create widget for geme quiting
class CEscWin:
  #--------------------------------------------------------------------------------
  def __init__(self, bg_color="#ddddee", abutt_bg_color="#ccccff"):
    self.esc_window = tk.Toplevel()
    self.esc_window.configure(bg=bg_color)
    self.esc_window.title(dict_en_cz["quit"][lang40])
    screen_width = self.esc_window.winfo_screenwidth()
    screen_height = self.esc_window.winfo_screenheight()
    self.esc_window_width = 250
    self.esc_window_height = 100
    self.esc_window.geometry(
        f"{self.esc_window_width}x{self.esc_window_height}+{int((screen_width-self.esc_window_width)/2)}+{int((screen_height-self.esc_window_height)/2)}"
    )
    self.esc_window.resizable(False, False)
    
    self.esc_window.protocol("WM_DELETE_WINDOW",
                             lambda: self.esc_window.destroy())
    #it is impossible to make any action before solving this widget
    self.esc_window.grab_set()
    #label for 'Escape window'
    self.label = tk.Label(self.esc_window,
                          text=dict_en_cz["want_quit"][lang40],
                          bg=bg_color,
                          font=("Arial", 12, "bold"))
    self.label.place(x=40, y=10)
    #to define 'Escape' buttons and their position
    #button "quit"
    self.button_quit = tk.Button(self.esc_window,
                                 text=dict_en_cz["quit"][lang40],
                                 bg=abutt_bg_color,
                                 width=5,
                                 font=("Arial", 10, "bold"),
                                 borderwidth=3,
                                 command=lambda: exit())
    #button "close"
    self.button_close = tk.Button(self.esc_window,
                                  text=dict_en_cz["close"][lang40],
                                  bg=abutt_bg_color,
                                  width=5,
                                  font=("Arial", 10, "bold"),
                                  borderwidth=3,
                                  command=lambda: self.esc_window.destroy())
    #"close" and "quit" button placement
    self.button_quit.place(x=40, y=50)
    self.button_close.place(x=160, y=50)

#===============================================================================
#class which create info widget to game buttons
class CWidgetInfo:
  #--------------------------------------------------------------------------------
  #create new popup info widget
  def __init__(self, awidget, atext):
    self.widget = awidget
    self.text = atext
    self.tooltip = None
    #what happends when hover the cursor
    self.widget.bind("<Enter>", self.show_tooltip)
    #what happends when hover out
    self.widget.bind("<Leave>", self.hide_tooltip)
  #--------------------------------------------------------------------------------
  #show info widget
  def show_tooltip(self, aevent):
    #use right language from config.ini
    config.read("config.ini")
    lang40 = int(config["Settings"]["language"])

    #returt info widget position (x, y)
    x, y, _, _ = self.widget.bbox("insert")
    x = x + self.widget.winfo_rootx() + 25
    y = y + self.widget.winfo_rooty() + 30

    self.tooltip = tk.Toplevel(self.widget)
    #widget is just simple label without classic window border 
    self.tooltip.wm_overrideredirect(True)
    #determine info widget position
    self.tooltip.wm_geometry(f"+{x}+{y}")

    #define text in info widget
    label = tk.Label(self.tooltip,
                     text=dict_en_cz[self.text][lang40],
                     background="#ffffe0",
                     relief="solid",
                     borderwidth=1)
    label.pack(ipadx=1)
  #--------------------------------------------------------------------------------
  #info widget disappears
  def hide_tooltip(self, event):
    if self.tooltip:
      self.tooltip.destroy()


#===============================================================================
#create card instantion
class Card:
  # card rank (str) to card value (int) convertor
  card_values = {
      '2': 2,
      '3': 3,
      '4': 4,
      '5': 5,
      '6': 6,
      '7': 7,
      '8': 8,
      '9': 9,
      '10': 10,
      'Jack': 10,
      'Queen': 10,
      'King': 10,
      'Ace': 11}
  #--------------------------------------------------------------------------------
  #create card with suit, rank and nominal value
  def __init__(self, asuit, arank):
    self.suit = asuit
    self.rank = arank
    self.value = self.card_values[arank]

#===============================================================================
#create deck instantion
class CDeck:
  #--------------------------------------------------------------------------------
  #create deck from N x 52-card packs 
  def __init__(self, anum_decks=1):
    #creating a dictionary its keys are individual 'suits' and values ​​are lists of card values
    self.card_photo={suit: [] for suit in ['Clubs', 'Diamonds', 'Hearts', 'Spades']}
    #create N x 52-card deck and save it into self.cards
    if anum_decks > 0:
      #create deck from all suit and rank combination, this operation will repeat 'anum_decks' times 
      self.cards = [
          Card(suit, rank) for _ in range(anum_decks)
          for suit in ['Clubs', 'Diamonds', 'Hearts', 'Spades'] for rank in [
              '2']]
      #, '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen','King', 'Ace'
      # shuffle created deck
      random.shuffle(self.cards)
    #create empty deck
    else:
      self.cards = []
    #create links to card pictures referring to suit and rank
    for suit in ['Clubs', 'Diamonds', 'Hearts', 'Spades']:
      for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']:
        # connect card object with image 'rank'.gif in folder 'suit'
        obverse_side_image = Image.open(f"./cards/{suit}/{rank}.gif")
        obverse_side_photo = ImageTk.PhotoImage(obverse_side_image)
        self.card_photo[suit].append(obverse_side_photo)
  #--------------------------------------------------------------------------------
  # move card from one deck to other
  def move_card(self, ato, afrom=None, ay=300,ashow_card=True):  
    #draw card from self.deck if is not changed default value of argument 'afrom'
    card_to_move = afrom.draw_card() if afrom else self.draw_card()
    # place card into target deck
    ato.cards.append(card_to_move)
    #condition, if it is shown card
    if ashow_card==True and card_to_move is not None:
      self.show_card(ato,ay)
  #--------------------------------------------------------------------------------    
  # shows card image on the table
  def show_card(self,ato,ay):
    
    #return exact card position in 'rank' list above
    rank_to_list_pos_convertor = {'2':0, '3':1, '4':2, '5':3, '6':4, '7':5, '8':6, '9':7,
                                  '10':8, 'Jack':9, 'Queen':10, 'King':11, 'Ace':12}
    
    #returns card image position multiplier in case of split in this function


    t_width = game.table_width
    # purpose of local variable 'lcs' is code shortening 
    lcs = len(ato.cards)

    # check if object player2 does exist and choose way of images showing
    if isinstance(game.player2,CPlayer)==True and len(game.player2.hand.cards)!=0:
      id_num=0
      if ato == game.player1.hand:id_num = 1
      elif ato == game.player2.hand:id_num = -1
      else: id_num = 0
      for i in range(len(ato.cards)):
        self.label = tk.Label(game.table, image=self.card_photo[ato.cards[i].suit]
                        [rank_to_list_pos_convertor[ato.cards[i].rank]])
        # method which place card image into the centre of game widget (window)
        # the width of the cards images is 104 pxl
        self.label.place(x=((t_width)-(250*(lcs-1)/(lcs)+104))/2+(250*i/lcs)-(t_width/4*id_num), y=ay)
      #displays cards values total above player and dealer hand image
      self.value_total = tk.Label(game.table, text=f"{self.calculate_hand_value(ato)}",
                            font=("Arial", 11),
                            fg="#000000",
                            bg=game.bg_color)
      self.value_total.place(x=((t_width)/2-10)-t_width/4*id_num, y=ay-25)    
    else:
      for i in range(len(ato.cards)):
        self.label = tk.Label(game.table, image=self.card_photo[ato.cards[i].suit]
                        [rank_to_list_pos_convertor[ato.cards[i].rank]])       
        # method which place card image into the centre of game widget (window)
        # the width of the cards images is 104 pxl
        self.label.place(x=(t_width-(250*(lcs-1)/(lcs)+104))/2+(250*i)/lcs, y=ay)

      #displays cards values total above player and dealer hand image
      self.value_total = tk.Label(game.table, text=f"{self.calculate_hand_value(ato)}",
                            font=("Arial", 11),
                            fg="#000000",
                            bg=game.bg_color)
      self.value_total.place(x=(t_width)/2-10, y=ay-25)
    
  #--------------------------------------------------------------------------------
  #return total value of hand (argument 'ahand')
  def calculate_hand_value(self,ahand):
    total_value = 0
    for card in ahand.cards:
        total_value += int(card.value)
    self.hand_value = total_value
    return total_value
  #--------------------------------------------------------------------------------
  #removes card from one deck amd return it for later using
  def draw_card(self):
    if len(self.cards) == 0:
      return None
    return self.cards.pop()
  #--------------------------------------------------------------------------------
  #removes old card images from the game table
  def table_cleaner(self,ato):
    for _ in range(len(ato.cards)):
      self.label.place_forget()
  #--------------------------------------------------------------------------------
  """  
  #load backend of card
  def place_reverse_side(self, ax=500,ay=300): 
    self.reverse_side_image = Image.open("./cards/red_back.gif")
    self.reverse_side_photo = ImageTk.PhotoImage(self.reverse_side_image)
    self.reverse_side = tk.Label(game.table, image=self.reverse_side_photo)
    #umístění obrázku rubová strany karty
    self.reverse_side.place(x=ax,y=ay)
  """

#===============================================================================
#class, which creates a new player with a few attributes
class CPlayer:
  #--------------------------------------------------------------------------------
  def __init__(self):
    self.budget = starting_budget20
    self.hand = CDeck(anum_decks=0)
    self.bet_amount = 1
    
#===============================================================================
#initiates main class and crates the game board
def create_game_window():
  global game
  game=CGameTable()
