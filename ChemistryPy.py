''' The program is designed to solve non-graphic problems in a first year general chemistry book.
There are three environments. In the laboratory environment, anything can be created or 'deconstructed'
and each step of the process should be recorded and displayed to verify the process and to aid a student
learning general chemistry.
The industrial and nature environments only describes industrial and natural processes.
There is no experimentation in these environments and the level of detail in explanations varies.
The main part of the program is the laboratory process in which a process is selected, all the appropriate field
values are entered, calculations are made, results are presented, and a record of the process is stored. Later,
that record can be retrieved and used to recreate the process for verification and learning.
The ideal is that every important aspect of each process should be described and explained.
Especially, each step in the process, the equipment and energy used, the side effects and by-products.
'''
import sys
from tkinter import *  # get widget classes
from tkinter.ttk import Combobox, Entry, Label
#import ttk
import logging
logging.basicConfig(
    filename = 'app.log',            # Name of the log file (omit to use stderr)
    filemode = 'w',                  # File mode (use 'a' to append)
    level    = logging.WARNING,      # Logging level (DEBUG, INFO, WARNING, ERROR, or CRITICAL)
)
import tkinter as tk
#import numpy as np
#import matplotlib as mpl
#import matplotlib.pyplot as plt
#from scipy import *
#from scipy import constants
from sqlite3 import *
#from sqlite3 import Error
#import SQL_tables_to_dict_str as sq
import pdb
from tkinter import messagebox as mb #*  # get standard dialogs
#from MessageBoxes import *
#from tkinter import messagebox as mb
from tkinter import font
# from ElementsDict import *
from Elements import *
from Compounds import *
from Processes import *
# C:\PythonProjects\ChemistryGUI\chemistryapp\Compounds.py
# C:\PythonProjects\ChemistryGUI\chemistryapp\ChemistryPy.py
# import SQL_tables_to_dict_str
#from eci_dicts_lists import *
# from CompoundsDict import *
# from ionDict import *
# from eciDict import *
#from ConVarFunEtc import *
from collections import defaultdict
#import defaultdict

root = Tk()
root.geometry("1800x900")
root.config(padx=20, pady=5)
titlefont = ('Ariel', 18, 'bold')
boldfont = ('Ariel', 14, 'bold')
labelfont = ('Ariel', 14)  # , 'bold')
buttonfont = ('Ariel', 12)  # , 'bold')
entryfont = ('Ariel', 12)  # , 'bold')
font1 = font.Font(name='TkCaptionFont', exists=True)
font1.config(family='courier new', size=20)

# Use the following structure to create frames and a canvas and scrollbar
# in order to attach the scrollbar to the canvas
#Create a Main Frame
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand = 1)
#Create a Canvas
main_canvas = Canvas(main_frame)
main_canvas.pack(side=LEFT, fill=BOTH, expand = 1)
# Add a Scrollbar to the Canvas
sb = Scrollbar(main_frame, orient=VERTICAL,command=main_canvas.yview)
sb.pack(side=RIGHT)
# Configure the Canvas
main_canvas.configure(yscrollcommand=sb.set)
main_canvas.bind('<Configure>', lambda e: main_canvas.configure(scrollregion=main_canvas.bbox("all")))
# Create another Frame inside the Canvas
inside_frame = Frame(main_canvas)
inside_frame = Frame(main_canvas,width=1000,height=100)
inside_frame.grid(row=0,column=0, columnspan=16, sticky="w") # pack(side=LEFT)

S_1_frame = Frame(inside_frame, highlightbackground="blue", highlightthickness=2)
S_1_frame.grid(row=7,column=0, columnspan=4, sticky="nw")
S_1_frame.config(padx=20, pady=10)
S_4_frame = Frame(inside_frame, highlightbackground="green", highlightthickness=2)
S_4_frame.grid(row=7,column=4, columnspan=4, sticky="nw")
S_4_frame.config(padx=20, pady=10)
S_2_frame = Frame(inside_frame, highlightbackground="red", highlightthickness=2)
S_2_frame.grid(row=9,column=0, columnspan=4, sticky="nw")
S_2_frame.config(padx=20, pady=10)
S_5_frame = Frame(inside_frame, highlightbackground="blue", highlightthickness=2)
S_5_frame.grid(row=9,column=4, columnspan=4, sticky="nw")
S_5_frame.config(padx=20, pady=10)
S_3_frame = Frame(inside_frame, highlightbackground="green", highlightthickness=2)
S_3_frame.grid(row=10,column=0, columnspan=4, sticky="nw")
S_3_frame.config(padx=20, pady=10)
S_6_frame = Frame(inside_frame, highlightbackground="red", highlightthickness=2)
S_6_frame.grid(row=10,column=4, columnspan=4, sticky="nw")
S_6_frame.config(padx=20, pady=10)

# Add the new froma to a Window in the Canvas
main_canvas.create_window((0,0), window = inside_frame, anchor = "nw")

''' Create additional windows for instructions and Calculations and Conversions'''
winInstructions = Toplevel()
e_Instructions = Text(winInstructions, height=20, width=50)
e_Instructions.grid(row=0, column=0) #, columnspan=6, sticky=W)
e_Instructions.config(font=entryfont)
e_Instructions.insert(END, "Program instructions will be provided in this window. \n")
e_Instructions.insert(END, "Move this window so it is always visible, or minimize it are resize it as needed. \n")
e_Instructions.insert(END, "Process instructions will be provided in this window. \n")

def clear_explanation_text():
    numlines = int(t_Explanations.index('end - 1 line').split('.')[0])
    print("882 numlines is ", numlines)
        # if numlines == 24:
        # log.delete(1.0, 2.0)
    t_Explanations.delete(0.0, 4.0) #numlines - 2)
    # t_Explanations.delete(0, None)
    # t_Explanations.insert(0, "")
    # e_Temp_Qty_1.delete(0, tk.END)
    # e_Temp_Qty_1.insert(0, 0)

winExplanations = Toplevel()
t_Explanations = Text(winInstructions, height=20, width=50)
t_Explanations.grid(row=0, column=0) #, columnspan=6, sticky=W)
t_Explanations.config(font=entryfont)
btn_clear_explanations = Button(winInstructions, text='Clear Explanation Text', command=clear_explanation_text)
btn_clear_explanations.grid(row=0, column=6, sticky="nw")
btn_clear_explanations.config(font=labelfont)
t_Explanations.insert(END, "Program instructions will be provided in this window. \n")
t_Explanations.insert(END, "Move this window so it is always visible, or minimize it are resize it as needed. \n")
t_Explanations.insert(END, "Process instructions will be provided in this window. \n")


def Calculate():
    #print("Calculate is not yet functional. \n")
    e_Calculate.insert(END, "Calculate is not yet functional. \n")

''' The following create the window winCalculate. 
    This window is used to perform unit conversions and other calculations. '''
winCalculate = Toplevel()
#from scipy import constants
#constants.value(u'elementary charge')
#print(constants.value(u'elementary charge'))
''' Entry and CB variables follow. '''
unit_values = "kilogram gram kilometer meter day hour minute second mile yard foot inch K F C ampere volt ohm candela mole pound ounce"
kl_unit_values = "liter(l) kilogram"
molarity_units = "molarity molality"
other_units = "electronegativity density specific_gravity"
cb_process_values = "equals conversion addition subtraction multiplication division power s_root"
heat_units =   "α ρ ∝ c q cal kcal J kJ J/g °C T_init T_final ΔT electronegativity"
e_1_qty = 0.0 #DoubleVar(0)
e_2_qty =  0.0 #DoubleVar(0)
e_2a_qty =  0.0 #DoubleVar(0)
e_3_qty =  0.0 #DoubleVar(0)
e_3a_qty =  0.0 #DoubleVar(0)
e_4_qty = 0.0 #DoubleVar(0)
eci_1_units = StringVar()
eci_1a_units = StringVar()
eci_2_units = StringVar()
eci_2a_units = StringVar()
eci_3_units = StringVar()
eci_3a_units = StringVar()
eci_4_units = StringVar()
eci_4a_units = StringVar()
eci_1_process = StringVar()
eci_2_process = StringVar()
eci_3_process = StringVar()

''' End of Entry and CB variable definitions. '''
# Imponts u as 1.602176634e-19
lbl_Title = Label(winCalculate, text="Calculations and Conversions")
lbl_Title.grid(row=0, column=0, columnspan=6) # sticky=W
lbl_Title.config(font=titlefont)
lbl_blank = Label(winCalculate, text="")
lbl_blank.grid(row=1, column=0)
lbl_blank.config(font=labelfont)
btn_calculate = Button(winCalculate, text="Calculate", command=Calculate)
btn_calculate.grid(row=1, column=3)
btn_calculate.config(font=buttonfont)
#btn_continue.bind("<<ComboboxSelected>>", Continue)
lbl_eci_1N = Label(winCalculate, text="Number", width=8)
lbl_eci_1N.grid(row=2, column=0)
lbl_eci_1N.config(font=labelfont)
#lbl_eci_1_units = Label(winCalculate, text="Exponent", width=10)
#lbl_eci_1_units.grid(row=2, column=1, sticky=W)
#lbl_eci_1_units.config(font=labelfont)
lbl_eci_1U = Label(winCalculate, text="Units", width=10)
lbl_eci_1U.grid(row=2, column=1) # sticky=W
lbl_eci_1U.config(font=labelfont)
lbl_eci_1P = Label(winCalculate, text="Process", width=10)
lbl_eci_1P.grid(row=2, column=2) # sticky=W
lbl_eci_1P.config(font=labelfont)
lbl_eci_2N = Label(winCalculate, text="Number", width=10)
lbl_eci_2N.grid(row=2, column=3) # sticky=W
lbl_eci_2N.config(font=labelfont)
lbl_eci_2U = Label(winCalculate, text="Units", width=10)
lbl_eci_2U.grid(row=2, column=4) # sticky=W
lbl_eci_2U.config(font=labelfont)
lbl_eci_2P = Label(winCalculate, text="Process", width=10)
lbl_eci_2P.grid(row=2, column=5) # sticky=W
lbl_eci_2P.config(font=labelfont)
lbl_eci_3N = Label(winCalculate, text="Number", width=10)
lbl_eci_3N.grid(row=2, column=6)
lbl_eci_3N.config(font=labelfont)
lbl_eci_3U = Label(winCalculate, text="Units", width=10)
lbl_eci_3U.grid(row=2, column=7) # sticky=W
lbl_eci_3U.config(font=labelfont)
lbl_eci_3P = Label(winCalculate, text="Process", width=10)
lbl_eci_3P.grid(row=2, column=8) # sticky=W
lbl_eci_3P.config(font=labelfont)
lbl_eci_4N = Label(winCalculate, text="Number", width=10)
lbl_eci_4N.grid(row=2, column=9) # sticky=W
lbl_eci_4N.config(font=labelfont)
lbl_eci_4U = Label(winCalculate, text="Units", width=10)
lbl_eci_4U.grid(row=2, column=10) # sticky=W
lbl_eci_4U.config(font=labelfont)
e_1_number = Entry(winCalculate, text="", textvariable=e_1_qty, width=8)
e_1_number.grid(row=3, column=0)
e_1_number.config(font=entryfont)
#e_1_exp = StringVar()
#e_1_exponent = Entry(winCalculate, text="", textvariable=e_1_exp, width=8)
#e_1_exponent.grid(row=3, column=1)
#e_1_exponent.config(font=entryfont)

cb_eci_1_units: Combobox = Combobox(winCalculate, values=unit_values, textvariable=eci_1_units, width=10)
cb_eci_1_units.grid(row=3, column=1)
cb_eci_1_units.config(font=entryfont)
cb_1_process: Combobox = Combobox(winCalculate, values=cb_process_values, textvariable=eci_1_process, width=10)
cb_1_process.grid(row=3, column=2)
cb_1_process.config(font=entryfont)
e_2_number = Entry(winCalculate, text="", textvariable=e_2_qty, width=8)
e_2_number.grid(row=3, column=3)
e_2_number.config(font=entryfont)
cb_eci_2_units: Combobox = Combobox(winCalculate, values=unit_values, textvariable=eci_2_units, width=10)
cb_eci_2_units.grid(row=3, column=4)
cb_eci_2_units.config(font=entryfont)
cb_eci_2_process: Combobox = Combobox(winCalculate, values=cb_process_values, textvariable=eci_2_process, width=10)
cb_eci_2_process.grid(row=3, column=5)
cb_eci_2_process.config(font=entryfont)
e_3_number = Entry(winCalculate, text="", textvariable=e_3_qty, width=8)
e_3_number.grid(row=3, column=6)
e_3_number.config(font=entryfont)
unit_values = "kilogram gram kilometer meter day hour minute second mile yard foot inch K F C ampere volt ohm candela mole pound ounce"
cb_eci_3_units: Combobox = Combobox(winCalculate, values=unit_values, textvariable=eci_3_units, width=10)
cb_eci_3_units.grid(row=3, column=7)
cb_eci_3_units.config(font=entryfont)
cb_eci_3_process: Combobox = Combobox(winCalculate, values=cb_process_values, textvariable=eci_3_process, width=10)
cb_eci_3_process.grid(row=3, column=8)
cb_eci_3_process.config(font=entryfont)
e_4_number = Entry(winCalculate, text="", textvariable=e_4_qty, width=8)
e_4_number.grid(row=3, column=9)
e_4_number.config(font=entryfont)
cb_eci_4_units: Combobox = Combobox(winCalculate, values=unit_values, textvariable=eci_4_units, width=10)
cb_eci_4_units.grid(row=3, column=10)
cb_eci_4_units.config(font=entryfont)
e_2a_number = Entry(winCalculate, text="", textvariable=e_2a_qty, width=8)
e_2a_number.grid(row=4, column=3)
e_2a_number.config(font=entryfont)
cb_eci_1a_units: Combobox = Combobox(winCalculate, values=unit_values, textvariable=eci_1a_units, width=10)
cb_eci_1a_units.grid(row=4, column=1)
cb_eci_1a_units.config(font=entryfont)
cb_eci_2a_units: Combobox = Combobox(winCalculate, values=unit_values, textvariable=eci_2a_units, width=10)
cb_eci_2a_units.grid(row=4, column=4)
cb_eci_2a_units.config(font=entryfont)
e_3a_number = Entry(winCalculate, text="", textvariable=e_3a_qty, width=8)
e_3a_number.grid(row=4, column=6)
e_3a_number.config(font=entryfont)
cb_eci_3a_units: Combobox = Combobox(winCalculate, values=unit_values, textvariable=eci_3a_units, width=10)
cb_eci_3a_units.grid(row=4, column=7)
cb_eci_3a_units.config(font=entryfont)
cb_eci_4a_units: Combobox = Combobox(winCalculate, values=unit_values, textvariable=eci_4a_units, width=10)
cb_eci_4a_units.grid(row=4, column=10)
cb_eci_4a_units.config(font=entryfont)
#cb_eci_1_units.bind("<<ComboboxSelected>>", eci_units_selected)
lbl_blank = Label(winCalculate, text="")
lbl_blank.grid(row=5, column=0)
lbl_blank.config(font=labelfont)
e_Calculate = Text(winCalculate, height=10, width=80)
e_Calculate.grid(row=6, column=0, columnspan=6)
e_Calculate.config(font=entryfont)
''' End of winCalculate form GUI creation. '''


''' Add variables from ConVarFunEtc until I can find and fix the error. '''
'''Not all the elements and their attributes have been added to the database. H\u2082 works for H2 subscript'''
''' The following are not lists, but have list in the title because the string lists the items.'''
element_symbol_string = 'H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br ' \
                        'Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er ' \
                        'Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Bi Po At Rn Fr Ra Ac Th Pa U Np Am Cm Bk Cf Es Fm Md No Lr ' \
                        'RF Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og'
element_name_string = 'Hydrogen Helium Lithium Beryllium Boron Carbon Nitrogen Oxygen Fluorine Neon Sodium Magnesium Aluminum ' \
                      'Silicon Phosphorus Sulfur Chlorine Argon Potassium Calcium Scandium Lead Vanadium Chromium Manganese Iron ' \
                      'Cobalt Nickel Copper Zinc Gallium Germanium Arsenic Selenium Bromine Krypton Rubidium Strontium Yttrium ' \
                      'Zirconium Niobium Molybdenum Technetium Ruthenium Rhodium Palladium Silver Cadmium Indium Tin Antimony ' \
                      'Tellurium Iodine Xenon Cesium Barium Lanthanium Cerium Praseodymium Neodynium Promethium Samarium Europium ' \
                      'Gadolinium Terbium Dysprosium Holmium Erbium Thulium Ytterbium Lutetium Hafnium Tantalum Tungsten Rhenium ' \
                      'Osmium Iridium Platinum Gold Mercury Thallium Bismuth Polonium Astatine Radon Francium Radium Actinium ' \
                      'Thorium Plutonium Uranium Neptunium Americium Curium Berkelium Californium Einsteinium Fermium Mendelevium ' \
                      'Nobelium Lawrencium Ruthorfordium Dudmium Seaborgium Bohrium Hassium Meitnerium Darmstadtium Roentgenium ' \
                      'Copernicium Nihonium Flerovium Moscovium Livermorium Tennessine Oganesson'

''' This list of elements and names will help retrieve names from symbols. '''
# element = zip(elements_symbols_list, elements_name_list)
element_names_Dict = {'Hydrogen': 'H', 'Helium': 'He', 'Lithium': 'Li', 'Beryllium': 'Be', 'Boron': 'B', 'Carbon': 'C', 'Nitrogen': 'N',
                      'Oxygen': 'O', 'Fluorine': 'F', 'Neon': 'Ne', 'Sodium': 'Na', 'Magnesium': 'Mg', 'Aluminum': 'Al', 'Silicon': 'Si',
                      'Phosphorus': 'P', 'Sulfur': 'S', 'Chlorine': 'Cl', 'Argon': 'Ar', 'Potassium': 'K', 'Calcium': 'Ca', 'Scandium': 'Sc',
                      'Titanium': 'Ti', 'Vanadium': 'V', 'Chromium': 'Cr', 'Manganese': 'Mn', 'Iron': 'Fe', 'Cobalt': 'Co', 'Nickel': 'Ni',
                      'Copper': 'Cu', 'Zinc': 'Zn', 'Gallium': 'Ga', 'Germanium': 'Ge', 'Arsenic': 'As', 'Selenium': 'Se', 'Bromine': 'Br',
                      'Krypton': 'Kr', 'Rubidium': 'Rb', 'Strontium': 'Sr', 'Yttrium': 'Y', 'Zirconium': 'Zr', 'Niobium': 'Nb',
                      'Molybdenum': 'Mo', 'Technetium': 'Tc', 'Ruthenium': 'Ru', 'Rhodium': 'Rh', 'Palladium': 'Pd', 'Silver': 'Ag',
                      'Cadmium': 'Cd', 'Indium': 'In', 'Tin': 'Sn', 'Antimony': 'Sb', 'Tellurium': 'Te', 'Iodine': 'I', 'Xenon': 'Xe',
                      'Cesium': 'Cs', 'Barium': 'Ba', 'Lanthanium': 'La', 'Cerium': 'Ce', 'Praseodymium': 'Pr', 'Neodynium': 'Nd',
                      'Promethium': 'Pm', 'Samarium': 'Sm', 'Europium': 'Eu', 'Gadolinium': 'Gd', 'Terbium': 'Tb', 'Dysprosium': 'Dy',
                      'Holmium': 'Ho', 'Erbium': 'Er', 'Thulium': 'Tm', 'Ytterbium': 'Yb', 'Lutetium': 'Lu', 'Hafnium': 'Hf', 'Tantalum': 'Ta',
                      'Tungsten': 'W', 'Rhenium': 'Re', 'Osmium': 'Os', 'Iridium': 'Ir', 'Platinum': 'Pt', 'Gold': 'Au', 'Mercury': 'Hg',
                      'Thallium': 'Tl', 'Lead': 'Ti', 'Bismuth': 'Bi', 'Polonium': 'Po', 'Astatine': 'At', 'Radon': 'Rn', 'Francium': 'Fr',
                      'Radium': 'Ra', 'Actinium': 'Ac', 'Thorium': 'Th', 'Protactinium': 'Pa', 'Uranium': 'U', 'Neptunium': 'Np',
                      'Plutonium': 'Pa', 'Americium': 'Am', 'Curium': 'Cm', 'Berkelium': 'Bk', 'Californium': 'Cf', 'Einsteinium': 'Es',
                      'Fermium': 'Fm', 'Mendelevium': 'Md', 'Nobelium': 'No', 'Lawrencium': 'Lr', 'Ruthorfordium': 'RF', 'Dudmium': 'Db',
                      'Seaborgium': 'Sg', 'Bohrium': 'Bh', 'Hassium': 'Hs', 'Meitnerium': 'Mt', 'Darmstadtium': 'Ds', 'Roentgenium': 'Rg',
                      'Copernicium': 'Cn', 'Nihonium': 'Nh', 'Flerovium': 'Fl', 'Moscovium': 'Mc', 'Livermorium': 'Lv', 'Tennessine': 'Ts',
                      'Oganesson': 'Og'}
''' Tried to change symbols to use subscripts, but the Compound Dictionary would not accept 
a subscripted formula as a valid key'''
compound_formula_string =  "Al4C3 AlCl3 Ar2He2Kr2Ne2Xe2Rn2 BCl3 Ca(H2PO4)2 CaI Ca(OH)2 Ca3P2 CdS CsF C6H8O7 CH3CO2H C2H3OOH" \
                           " CO CO2 HBr HC2H3O2 HCl HClO4 HCN H2CO3 HF HI HNO2 HNO3 H3PO4 H2S H2SO3 H2SO4 IF7 KBr KOH LiCl" \
                           " Mg3N2 NaCl NaHCO33 Na2O NaOH NH3 N2H4 NO NO2 N2O4 N2O N2O5 PF5 SO2 SO3 CH4 C2H6 C3H8 C4H10 C4H10_M" \
                           " C5H12 C6H14 C7H16 C8H18 C9H20 C10H22 C14H30 C18H38"

compound_name_string = "aluminum_carbide aluminum_chloride air boron_trichloride calcium_dihydrogen_phosphate calcium_iodide" \
                       " calcium_hydroxide calcium_phosphide cadmium_sulfide cesium_fluoride citric_acid acetic_acid acetic_acid" \
                       " carbon_monoxide carbon_dioxide hydrobromic_acid acetic_acid hydrochloric_acid perchloric_acid" \
                       " hydrogen_cyanide carbonic_acid hydrofluoric_acid hydroiodic_acid nitrous_acid nitric_acid" \
                       " phosphoric_acid hydrosulfuric_acid sulfurous_acid sulfuric_acid iodine_heptafluoride potassium_bromide" \
                       " potassium_hydroxide lithium_chloride magnesium_nitride sodium_chloride bicarbonate_of_soda sodium_oxide" \
                       " sodium_hydroxide ammonia hydrazine nitric_oxide nitorgen_dioxide dinitrogen_tetroxide nitrous_oxide" \
                       " dinitrogen_pentoxide phosphorus_pentafluoride sulfur_dioxide sulfur_trioxide methane ethane propane" \
                       " butane 2-methylpropane pentane hexane heptane octane nonane decane tetradecane octadecane"
''' This list of compounds and names will help retrieve names from formulas. Doesn't work. Why? '''
compounds_formula_dict = {'Al4C3': 'aluminum_carbide', 'AlCl3': 'aluminum_chloride', 'Ar2He2Kr2Ne2Xe2Rn2': 'air',
                        'BCl3': 'boron_trichloride', 'Ca(H2PO4)2': 'calcium_dihydrogen_phosphate', 'CaI': 'calcium_iodide',
                        'Ca(OH)2': 'calcium_hydroxide', 'Ca3P2': 'calcium_phosphide', 'CdS': 'cadmium_sulfide',
                        'CsF': 'cesium_fluoride', 'C6H8O7': 'citric_acid', 'CH3CO2H': 'acetic_acid', 'C2H3OOH': 'acetic_acid',
                        'CO': 'carbon_monoxide', 'CO2': 'carbon_dioxide', 'HBr': 'hydrobromic_acid', 'HC2H3O2': 'acetic_acid',
                        'HCl': 'hydrochloric_acid', 'HClO4': 'perchloric_acid', 'HCN': 'hydrogen_cyanide',
                        'H2CO3': 'carbonic_acid', 'HF': 'hydrofluoric_acid', 'HI': 'hydroiodic_acid', 'HNO2': 'nitrous_acid',
                        'HNO3': 'nitric_acid', 'H3PO4': 'phosphoric_acid', 'H2S': 'hydrosulfuric_acid', 'H2SO3': 'sulfurous_acid',
                        'H2SO4': 'sulfuric_acid', 'IF7': 'iodine_heptafluoride', 'KBr': 'potassium_bromide',
                        'KOH': 'potassium_hydroxide', 'LiCl': 'lithium_chloride', 'Mg3N2': 'magnesium_nitride',
                        'NaCl': 'sodium_chloride', 'NaHCO33': 'bicarbonate_of_soda', 'Na2O': 'sodium_oxide',
                        'NaOH': 'sodium_hydroxide', 'NH3': 'ammonia', 'N2H4': 'hydrazine', 'NO': 'nitric_oxide',
                        'NO2': 'nitorgen_dioxide', 'N2O4': 'dinitrogen_tetroxide', 'N2O': 'nitrous_oxide',
                        'N2O5': 'dinitrogen_pentoxide', 'PF5': 'phosphorus_pentafluoride', 'SO2': 'sulfur_dioxide',
                        'SO3': 'sulfur_trioxide', 'CH4': 'methane', 'C2H6': 'ethane', 'C3H8': 'propane', 'C4H10': 'butane',
                        'C4H10_M': '2-methylpropane', 'C5H12': 'pentane', 'C6H14': 'hexane', 'C7H16': 'heptane',
                        'C8H18': 'octane', 'C9H20': 'nonane', 'C10H22': 'decane', 'C14H30': 'tetradecane', 'C18H38': 'octadecane'}

compound_names_dict =  {'aluminum_carbide': 'Al4C3', 'aluminum_chloride': 'AlCl3', 'air': 'Ar2He2Kr2Ne2Xe2Rn2',
                        'boron_trichloride': 'BCl3', 'calcium_dihydrogen_phosphate': 'Ca(H2PO4)2', 'calcium_iodide': 'CaI',
                        'calcium_hydroxide': 'Ca(OH)2', 'calcium_phosphide': 'Ca3P2', 'cadmium_sulfide': 'CdS',
                        'cesium_fluoride': 'CsF', 'citric_acid': 'C6H8O7', 'acetic_acid': 'HC2H3O2', 'carbon_monoxide': 'CO',
                        'carbon_dioxide': 'CO2', 'hydrobromic_acid': 'HBr', 'hydrochloric_acid': 'HCl', 'perchloric_acid': 'HClO4',
                        'hydrogen_cyanide': 'HCN', 'carbonic_acid': 'H2CO3', 'hydrofluoric_acid': 'HF',
                        'hydroiodic_acid': 'HI', 'nitrous_acid': 'HNO2', 'nitric_acid': 'HNO3', 'phosphoric_acid': 'H3PO4',
                        'hydrosulfuric_acid': 'H2S', 'sulfurous_acid': 'H2SO3', 'sulfuric_acid': 'H2SO4',
                        'iodine_heptafluoride': 'IF7', 'potassium_bromide': 'KBr', 'potassium_hydroxide': 'KOH',
                        'lithium_chloride': 'LiCl', 'magnesium_nitride': 'Mg3N2', 'sodium_chloride': 'NaCl',
                        'bicarbonate_of_soda': 'NaHCO33', 'sodium_oxide': 'Na2O', 'sodium_hydroxide': 'NaOH',
                        'ammonia': 'NH3', 'hydrazine': 'N2H4', 'nitric_oxide': 'NO', 'nitorgen_dioxide': 'NO2',
                        'dinitrogen_tetroxide': 'N2O4', 'nitrous_oxide': 'N2O', 'dinitrogen_pentoxide': 'N2O5',
                        'phosphorus_pentafluoride': 'PF5', 'sulfur_dioxide': 'SO2', 'sulfur_trioxide': 'SO3', 'methane': 'CH4',
                        'ethane': 'C2H6', 'propane': 'C3H8', 'butane': 'C4H10', '2-methylpropane': 'C4H10_M', 'pentane': 'C5H12',
                        'hexane': 'C6H14', 'heptane': 'C7H16', 'octane': 'C8H18', 'nonane': 'C9H20', 'decane': 'C10H22',
                        'tetradecane': 'C14H30', 'octadecane': 'C18H38'}

Al4C3 = dict(formula= 'Al4C3', elements= 'AlC',name= 'aluminum_carbide',mass= 63.015)
AlCl3 = dict(formula= 'AlCl3', elements= 'AlCl',name= 'aluminum_chloride',mass= 133.341)
Ar2He2Kr2Ne2Xe2Rn2 = dict(formula= 'Ar2He2Kr2Ne2Xe2Rn2', elements=  'ArHeKrNeXeRn', name= 'air',mass= 28.9647)
BCl3 = dict(formula= 'BCl3', elements= 'BCl',name= 'boron_trichloride',mass= 117.16)
CH4 = dict(formula= 'CH4', elements= 'CH', name= 'methane', mass= 16.043, melting=-182.5, boiling=-161.5)
C2H6 = dict(formula= 'C2H6', elements= 'CH', name= 'ethane', mass= 30.07,melting=-183.2, boiling=-88.6)
C3H8 = dict(formula= 'C3H8', elements= 'CH', name= 'propane', mass= 44.097,melting=-187.7, boiling=-42.1)
C4H10 = dict(formula= 'C4H10', elements= 'CH', name= 'butane', mass= 58.12,melting=-138.3, boiling=-0.5)
C4H10_M = dict(formula= 'C4H10_M', elements= 'CH', name= '2-methylpropane', mass= 58.124,melting='', boiling='')
C5H12 = dict(formula= 'C5H12', elements= 'CH', name= 'pentane', mass= 72.15,melting=-129.7, boiling=36.1)
C6H14 = dict(formula= 'C6H14', elements= 'CH', name= 'hexane', mass= 86.18,melting=-95.3, boiling=68.7)
C7H16 = dict(formula= 'C7H16', elements= 'CH', name= 'heptane', mass= 100.21,melting=-90.6, boiling=98.4)
C8H18 = dict(formula= 'C8H18', elements= 'CH', name= 'octane', mass= 114.23,melting=-56.8, boiling=125.7)
C9H20 = dict(formula= 'C9H20', elements= 'CH', name= 'nonane', mass= 128.26,melting=-53.6, boiling=150.8)
C10H22 = dict(formula= 'C10H22', elements= 'CH', name= 'decane', mass= 142.28,melting=-29.7, boiling=174.0)
C14H30 = dict(formula= 'C14H30', elements= 'CH', name= 'tetradecane', mass= 198.39,melting=5.9, boiling=253.5)
C18H38 = dict(formula= 'C18H38', elements= 'CH', name= 'octadecane', mass= 254.49432,melting=28.2, boiling=316.1)
CaH2PO4 = dict(formula= 'Ca(H2PO4)2', elements= 'CaHOP',name= 'calcium_dihydrogen_phosphate', mass= 234.05)
CaI = dict(formula= 'CaI', elements= 'CaI',name= 'calcium_iodide', mass= 166.98247)
CaOH2 = dict(formula= 'Ca(OH)2', elements= 'CaHO', name= 'calcium_hydroxide', mass= 74.092)
Ca3P2 = dict(formula= 'Ca3P2', elements= 'CaP', name= 'calcium_phosphide', mass= 182.182)
CdS = dict(formula= 'CdS', elements= 'CdS', name= 'cadmium_sulfide', mass= 144.474)
CsF = dict(formula= 'CsF', elements= 'CsF', name= 'cesium_fluoride', mass= 151.903452)
C6H8O7 = dict(formula= 'C6H8O7', elements= 'CHO', name= 'citric_acid', mass= 192.123)
CH3CO2H = dict(formula= 'CH3CO2H', elements= 'CHO', name= 'acetic_acid', mass= 60.052)
C2H4COH = dict(formula= 'C2H4COH', elements= 'CHO', name= 'acetic_acid', mass= 0)
CO = dict(formula= 'CO', elements= 'CO', name= 'carbon_monoxide', mass= 28.01)
CO2 = dict(formula= 'CO2', elements= 'CO', name= 'carbon_dioxide', mass= 44.009)
HBr = dict(formula= 'HBr', elements= 'BrH', name= 'hydrobromic_acid', mass= 80.912)
HC2H3O2 = dict(formula= 'HC2H3O2', elements= 'CHO', name= 'acetic_acid', mass= 60.052)
HCl = dict(formula= 'HCl', elements= 'ClH', name= 'hydrochloric_acid', mass= 38.474)
HClO4 = dict(formula= 'HClO4', elements= 'ClHO', name= 'perchloric_acid', mass= 100.454)
HCN = dict(formula= 'HCN', elements= 'CHN', name= 'hydrogen_cyanide', mass= 27.026)
H2CO3 = dict(formula= 'H2CO3', elements= 'CHO', name= 'carbonic_acid', mass= 62.024)
HF = dict(formula= 'HF', elements= 'FH', name= 'hydrofluoric_acid', mass= 20.006)
HI = dict(formula= 'HI', elements= 'HI', name= 'hydroiodic_acid', mass= 127.91247)
HNO2 = dict(formula= 'HNO2', elements= 'HNO', name= 'nitrous_acid', mass= 47.013)
HNO3 = dict(formula= 'HNO3', elements= 'HNO', name= 'nitric_acid', mass= 63.012)
H3PO4 = dict(formula= 'H3PO4', elements= 'HOS', name= 'phosphoric_acid', mass= 97.9938)
H2S = dict(formula= 'H2S_aq', elements= 'HS', name= 'hydrosulfuric_acid', mass= 34.1)
H2SO3 = dict(formula= 'H2SO3', elements= 'HOS', name= 'sulfurous_acid', mass= 82.07)
H2SO4 = dict(formula= 'H2SO4', elements= 'HOS', name= 'sulfuric_acid', mass= 98.079)
IF7 = dict(formula= 'IF7', elements= 'FI', name= 'iodine_heptafluoride', mass= 259.9)
KBr = dict(formula= 'KBr', elements= 'BrK', name= 'potassium_bromide', mass= 119.002)
KOH = dict(formula= 'KOH', elements= 'HKO', name= 'potassium_hydroxide', mass= 56.1056 )
LiCl = dict(formula= 'LiCl', elements= 'ClLi', name= 'lithium_chloride', mass= 42.394)
Mg3N2 = dict(formula= 'Mg3N2', elements= 'MgN', name= 'magnesium_nitride', mass= 100.9494)
NaCl = dict(formula= 'NaCl', elements= 'ClNa', name= 'sodium_chloride', mass= 58.44)
NaHCO3 = dict(formula= 'NaHCO33', elements= 'CHNaO)', name= 'bicarbonate_of_soda', mass= 84.007)
Na2O = dict(formula= 'Na2O', elements= 'NaO', name= 'sodium_oxide', mass= 61.9789)
NaOH = dict(formula= 'NaOH', elements= 'HNaO', name= 'sodium_hydroxide', mass= 39.997)
NH3 = dict(formula= 'NH3', elements= 'HN', name= 'ammonia', mass= 17.031)
N2H4 = dict(formula= 'N2H4', elements= 'HN', name= 'hydrazine', mass= 32.0452)
NO = dict(formula= 'NO', elements= 'NO', name= 'nitric_oxide', mass= 30.01)
NO2 = dict(formula= 'NO2', elements= 'NO', name= 'nitorgen_dioxide', mass= 46.0055)
N2O4 = dict(formula= 'N2O4', elements= 'NO', name= 'dinitrogen_tetroxide', mass= 92.011)
N2O = dict(formula= 'N2O', elements= 'NO', name= 'nitrous_oxide', mass= 44.013)
N2O5 = dict(formula= 'N2O5', elements= 'NO', name= 'dinitrogen_pentoxide', mass= 108.01)
PF5 = dict(formula= 'PF5', elements= 'FP', name= 'phosphorus_pentafluoride', mass= 125.966)
SO2 = dict(formula= 'SO2', elements= 'OS', name= 'sulfur_dioxide', mass= 64.066)
SO3 = dict(formula= 'SO3', elements= 'OS', name= 'sulfur_trioxide', mass= 80.06)

c_db = {}
c_db['Al4C3'] = Al4C3
c_db['AlCl3'] = AlCl3
c_db['Ar2He2Kr2Ne2Xe2Rn2'] = Ar2He2Kr2Ne2Xe2Rn2
c_db['BCl3'] = BCl3
c_db['CH4'] = CH4
c_db['C2H6'] = C2H6
c_db['C3H8'] = C3H8
c_db['C4H10'] = C4H10
c_db['C4H10_M'] = C4H10_M
c_db['C5H12'] = C5H12
c_db['C6H14'] = C6H14
c_db['C7H16'] = C7H16
c_db['C8H18'] = C8H18
c_db['C9H20'] = C9H20
c_db['C10H22'] = C10H22
c_db['C14H30'] = C14H30
c_db['C18H38'] = C18H38
c_db['CaH2PO4'] = CaH2PO4
c_db['CaI'] = CaI
c_db['CaOH2'] = CaOH2
c_db['Ca3P2'] = Ca3P2
c_db['CdS'] = CdS
c_db['C6H8O7'] = C6H8O7
c_db['CH3CO2H'] = CH3CO2H
c_db['C2H4COH'] = C2H4COH
c_db['CO'] = CO
c_db['CO2'] = CO2
c_db['HBr'] = HBr
c_db['HC2H3O2'] = HC2H3O2
c_db['HCl'] = HCl
c_db['HCl'] = HCl
c_db['HClO4'] = HClO4
c_db['H2CO3'] = H2CO3
c_db['HF'] = HF
c_db['HI'] = HI
c_db['HNO2'] = HNO2
c_db['HNO3'] = HNO3
c_db['H3PO4'] = H3PO4
c_db['H2S'] = H2S
c_db['H2SO3'] = H2SO3
c_db['H2SO4'] = H2SO4
c_db['IF7'] = IF7
c_db['KBr'] = KBr
c_db['KOH'] = KOH
c_db['LiCl'] = LiCl
c_db['Mg3N2'] = Mg3N2
c_db['NaCl'] = NaCl
c_db['NaHCO3'] = NaHCO3
c_db['Na2O'] = Na2O
c_db['NaOH'] = NaOH
c_db['NH3'] = NH3
c_db['N2H4'] = N2H4
c_db['NO'] = NO
c_db['NO2'] = NO2
c_db['N2O4'] = N2O4
c_db['N2O'] = N2O
c_db['N2O5'] = N2O5
c_db['PF5'] = PF5
c_db['SO2'] = SO2
c_db['SO3'] = SO3

ionic_compounds_symbols_string = "No list yet"
ionic_compounds_names_string = "No list yet"
''' An initial list of ions and names to fill the combo boxes until a proper list can be made. '''
ion_symbols_string = "C2H3O2 ClO2 ClO3 ClO4 CN CO32 CuS FeCl2 FeCl3 H2PO4 HCO3 Hg2O HgO H3O HPO42 HSO4 OH NH4 NO3 NO2 MnO4 O22 SO42 SO32 PO43"
ion_names_string = "acetate chlorite chlorate perchlorate cyanide carbonate copper_(II)_sulfide " \
                 "iron_(II)_chloride iron_(III)_chloride dihydrogen_phosphate hydrogen_carbonate " \
                 "mercury_(I)_oxide mercury_(II)_oxide hydronium hydrogen_phosphate hydrogen_sulfate " \
                 "hydroxide ammonium nitrate nitrite permanganate peroxide sulfate sulfite phosphate "

ion_names_dict = {'acetate': 'C2H3O2', 'chlorite': 'ClO2', 'chlorate': 'ClO3', 'perchlorate': 'ClO4',
                  'cyanide': 'CN', 'carbonate': 'CO32', 'copper_(II)_sulfide': 'CuS', 'iron_(II)_chloride': 'FeCl2',
                  'iron_(III)_chloride': 'FeCl3', 'dihydrogen_phosphate': 'H2PO4', 'hydrogen_carbonate': 'HCO3',
                  'mercury_(I)_oxide': 'Hg2O', 'mercury_(II)_oxide': 'HgO', 'hydronium': 'H3O',
                  'hydrogen_phosphate': 'HPO42', 'hydrogen_sulfate': 'HSO4', 'hydroxide': 'OH',
                  'ammonium': 'NH4', 'nitrate': 'NO3', 'nitrite': 'NO2',
                  'permanganate': 'MnO4', 'peroxide': 'H2O22', 'sulfate': 'SO42',
                  'sulfite': 'SO32', 'phosphate': 'PO43'}

# diatomic_formula_string = 'H2 N2 F2 O2 I2 Cl2 Br2'
polyatomic_formula_string = 'H2 N2 F2 O2 I2 Cl2 S8 Se8 P4 Br2'
# diatomic_name_string = 'Hydrogen Nitrogen Fluorine Oxygen Iodine Chlorine Bromine'
polyatomic_name_string = 'Hydrogen Nitrogen Fluorine Oxygen Iodine Chlorine Sulfur Selenium Phosphorous Bromine'
''' Other variables used by Chemistry and other programs '''
''' combobox lists go here. Other variables go elsewhere. '''
unit_values = "Moles grams kilograms ounces pounds liters(l) liters(g) ml(l) ml(g)"
eci_cb_values = "elements compounds ions polyatomic" # ionic_compounds acids bases polyatomic
environment = "Laboratory Industry Nature"
temp_units = "K F C"
press_units = "ATM torr psi mmHg"
current_item_info = dict(s_type = "", s_id = "", s_id_formula = "", substance = "") 
current_dict = ""
major_process_list = "Calculate Synthesis Decompostion Combustion Single_Replacement Double_Replacement Neutralization Precipitation Balance_Equation Set_default_T_and_P Parse_Reactants Parse_Products Acid_Base Oxidation_top_frameuction Oxidation_Rate Metathesis Refinement"
minor_process_list = "Set_STP_Variables Pressure Volume, moles Temperature pvnrt "
equipment = "refinery blah1 blah2"
energy_type = "heat electricity"
catalyst = "blah1 blah2 blah3 blah4"
side_effects = "air_polution water_polution land_polution"
by_products = "CO CO2 NO NO2"
variables = "Av Bv Cv Kv"  # Variable names cannot conflict with element symbols like B C H K etc
''' Variables to hold the selected items of combo boxes. '''
major_process_selected = ""
minor_process_selected = ""
equipment_selected = ""
energy_type_selected = ""
catalyst_selected = ""
side_effect_selected = ""
by_product_selected = ""
variable_selected = ""
variable_value = DoubleVar()
Init_default_T_and_P = FALSE
Av = DoubleVar()
Bv = DoubleVar()
Cv = DoubleVar()
Kv = DoubleVar()

''' Miscellaneous variables to use until proper variables are created. '''
valences = "7 6 5 4 3 2 1 0 -1 -2 -3 -4"


''' This list of elements and names will help retrieve names from symbols. '''
# element = zip(elements_symbols_list, elements_name_list)

''' Tried to change symbols to use subscripts, but the Compound Dictionary would not accept
a subscripted formula as a valid key'''

current_eci = ""
variable_value = "" #DoubleVar()
Init_default_T_and_P = FALSE
Av = "" #DoubleVar()
Bv = "" #DoubleVar()
Cv = "" #DoubleVar()
Kv = "" #DoubleVar()

#for i in range(40):
#    Button(inside_frame, text = f'Button {i}').grid(row=i, column=0)
''' Add lists here '''

''' Old definition of eci_1_d delete items as moved 

'''
''' Define the eci_d dictionary structure. Use this structure to pass eci frames so code can be generic.'''


# eci_d = dict(eci_1 = "eci_1_d", eci_2 = "eci_2_d",eci_3 = "eci_3_d",eci_4 = "eci_4_d",eci_5 = "eci_5_d",eci_6 = "eci_6_d")
# print("424 eci_d is ", eci_d)
# print("425 eci_d is ", eci_d['eci_1'])


eci_1_d = dict(id = 'eci_1', formula= "", name= "", dict= "eci_1_d", type = "", 
               units = "grams", qty = 0.0,
               calc_qty = 0.0, M_qty = 1, valence = 0, moles_molarity = "moles", molarity_molality_units = "liters(l)",
               temp_display_units = "C", temp_calc_units = "K", temp_display_qty = 0, temp_calc_qty = 273.15,
               press_display_units = "atm", press_calc_units = "atm", press_display_qty = 1, press_calc_qty = 1,
               column = 0, electronegativity = 0, _group = "", mass = 0, Oxidation_State = 0, activity = 99,
               kl_qty = 0, kl_units = "", mm_qty = 0, mm_units = "", molarity_qty = 0, molality_qty = 0, cation_qty = 0,
               cation = "", cation_charge = 0, anion_qty = 0, anion = "", anion_charge = 0, specific_gravity = 0, heat_display_qty = 0,
               heat_display_units = "", other_display_qty = 0, other_display_units = "", melt = "", boil = "", elements_list = [], ions_list = [],
               Energy_of_first_ionization = 0, other = "")

# print("437 eci_d is ", eci_1_d['type'])
# print("438 eci_d is ", eci_d['eci_1']['type'])
eci_2_d = dict(id = 'eci_2', formula= "", name= "", dict= "eci_2_d", type = "", units = "grams", qty = 0.0,
               calc_qty = 0.0, M_qty = 1, valence = 0, moles_molarity = "moles", molarity_molality_units = "liters(l)",
               temp_display_units = "C", temp_calc_units = "K", temp_display_qty = 0, temp_calc_qty = 273.15,
               press_display_units = "atm", press_calc_units = "atm", press_display_qty = 1, press_calc_qty = 1,
               column = 0, electronegativity = 0, _group = "", mass = 0, Oxidation_State = 0, activity = 99,
               kl_qty = 0, kl_units = "", mm_qty = 0, mm_units = "", molarity_qty = 0, molality_qty = 0, cation_qty = 0,
               cation = "", cation_charge = 0, anion_qty = 0, anion = "", anion_charge = 0, specific_gravity = 0, heat_display_qty = 0,
               heat_display_units = "", other_display_qty = 0, other_display_units = "", melt = "", boil = "", elements_list = [], ions_list = [],
               Energy_of_first_ionization = 0, other = "")
eci_3_d = dict(id = 'eci_3', formula= "", name= "", dict= "eci_3_d", type = "", units = "grams", qty = 0.0,
               calc_qty = 0.0, M_qty = 1, valence = 0, moles_molarity = "moles", molarity_molality_units = "liters(l)",
               temp_display_units = "C", temp_calc_units = "K", temp_display_qty = 0, temp_calc_qty = 273.15,
               press_display_units = "atm", press_calc_units = "atm", press_display_qty = 1, press_calc_qty = 1,
               column = 0, electronegativity = 0, _group = "", mass = 0, Oxidation_State = 0, activity = 99,
               kl_qty = 0, kl_units = "", mm_qty = 0, mm_units = "", molarity_qty = 0, molality_qty = 0, cation_qty = 0,
               cation = "", cation_charge = 0, anion_qty = 0, anion = "", anion_charge = 0, specific_gravity = 0, heat_display_qty = 0,
               heat_display_units = "", other_display_qty = 0, other_display_units = "", melt = "", boil = "", elements_list = [], ions_list = [],
               Energy_of_first_ionization = 0, other = "")
eci_4_d = dict(id = 'eci_4', formula= "", name= "", dict= "eci_4_d", type = "", units = "grams", qty = 0.0,
               calc_qty = 0.0, M_qty = 1, valence = 0, moles_molarity = "moles", molarity_molality_units = "liters(l)",
               temp_display_units = "C", temp_calc_units = "K", temp_display_qty = 0, temp_calc_qty = 273.15,
               press_display_units = "atm", press_calc_units = "atm", press_display_qty = 1, press_calc_qty = 1,
               column = 0, electronegativity = 0, _group = "", mass = 0, Oxidation_State = 0, activity = 99,
               kl_qty = 0, kl_units = "", mm_qty = 0, mm_units = "", molarity_qty = 0, molality_qty = 0, cation_qty = 0,
               cation = "", cation_charge = 0, anion_qty = 0, anion = "", anion_charge = 0, specific_gravity = 0, heat_display_qty = 0,
               heat_display_units = "", other_display_qty = 0, other_display_units = "", melt = "", boil = "", elements_list = [], ions_list = [],
               Energy_of_first_ionization = 0, other = "")
eci_5_d = dict(id = 'eci_5', formula= "", name= "", dict= "eci_5_d", type = "", units = "grams", qty = 0.0,
               calc_qty = 0.0, M_qty = 1, valence = 0, moles_molarity = "moles", molarity_molality_units = "liters(l)",
               temp_display_units = "C", temp_calc_units = "K", temp_display_qty = 0, temp_calc_qty = 273.15,
               press_display_units = "atm", press_calc_units = "atm", press_display_qty = 1, press_calc_qty = 1,
               column = 0, electronegativity = 0, _group = "", mass = 0, Oxidation_State = 0, activity = 99,
               kl_qty = 0, kl_units = "", mm_qty = 0, mm_units = "", molarity_qty = 0, molality_qty = 0, cation_qty = 0,
               cation = "", cation_charge = 0, anion_qty = 0, anion = "", anion_charge = 0, specific_gravity = 0, heat_display_qty = 0,
               heat_display_units = "", other_display_qty = 0, other_display_units = "", melt = "", boil = "", elements_list = [], ions_list = [],
               Energy_of_first_ionization = 0, other = "")
eci_6_d = dict(id = 'eci_6', formula= "", name= "", dict= "eci_6_d", type = "", units = "grams", qty = 0.0,
               calc_qty = 0.0, M_qty = 1, valence = 0, moles_molarity = "moles", molarity_molality_units = "liters(l)",
               temp_display_units = "C", temp_calc_units = "K", temp_display_qty = 0, temp_calc_qty = 273.15,
               press_display_units = "atm", press_calc_units = "atm", press_display_qty = 1, press_calc_qty = 1,
               column = 0, electronegativity = 0, _group = "", mass = 0, Oxidation_State = 0, activity = 99,
               kl_qty = 0, kl_units = "", mm_qty = 0, mm_units = "", molarity_qty = 0, molality_qty = 0, cation_qty = 0,
               cation = "", cation_charge = 0, anion_qty = 0, anion = "", anion_charge = 0, specific_gravity = 0, heat_display_qty = 0,
               heat_display_units = "", other_display_qty = 0, other_display_units = "", melt = "", boil = "", elements_list = [], ions_list = [],
               Energy_of_first_ionization = 0, other = "")
eci_d = {}
eci_d['eci_1'] = eci_1_d
eci_d['eci_2'] = eci_2_d
eci_d['eci_3'] = eci_3_d
eci_d['eci_4'] = eci_4_d
eci_d['eci_5'] = eci_5_d
eci_d['eci_6'] = eci_6_d
# dbr['R1'] = r1



elements_symbols_list = "Ac Ag Al Am Ar As At Au B Ba Be Bi Bk Br C Ca Cd Ce Cf Cl Cm Co Cr Cs Cu Dy Er Es Eu " \
                        "F Fe Fm Fr Ga Gd Ge H He Hf Hg Ho I In Ir K Kr La Li Lu Md Mn Mo N Na Nb Nd Ne Ni Np O Os " \
                        "P Pa Pb Pd Pm Po Pr Pt Pu Ra Rb Re Rh Rn  Ru S Sb Sc Se Si Sm Sn Sr Ta Tb Tc Te Th Ti Tl Tm" \
                        "U V W Xe Y Yb Zn Zr "
''' An element name list is used to fill the element name combo box to help the user who knows
the name of an element, but not the symbols. '''
elements_name_list = "Actinium Silver Aluminum Americium Argon Arsenic Astatine Gold Boron Barium Beryllium " \
                     "Bismuth Berkelium Bromine Carbon Calcium Cadmium Cerium Californium Chlorine Curium Cobalt Chromium " \
                     "Cesium Copper Dysprosium Erbium Einsteinium Europium Fluorine Iron Fermium Francium Gallium Gadolinium " \
                     "Germanium Hydrogen Helium Hafnium Mercury Holmium Iodine Indium Iridium Potassium Krypton " \
                     "Lanthanum Lithium Lutetium Mendelevium Manganese Molybdenum Nitrogen Na Niobium Neodymium Neon Nickel " \
                     "Neptunium Oxygen Osmium Phosphorus Protactinium Lead Palladium Promethium Polonium Praseodymium " \
                     "Platnum Plutonium Radium Rubidium Rhenium Rhodium Radon Rutherfordium Sulfur Antimony Scandium Selenium Silicon " \
                     "Samarium Tin Strontium Tantalum Terbium Technetium Tellurium Thorium Titanium " \
                     "Thallium Thulium Uranium Vanadium Tungsten Xenon Yttrium Ytterbium Zinc Zirconium "


compound_name_string = "aluminum_carbide aluminum_chloride air boron_trichloride methane ethane propane butane 2-methylpropane" \
                      " pentane hexane heptane octane nonane decane tetradecane octadecane calcium_dihydrogen_phosphate" \
                      " calcium_iodide calcium_hydroxide calcium_phosphide cadmium_sulfide cesium_fluoride citric_acid" \
                      " acetic_acid acetic_acid carbon_monoxide carbon_dioxide hydrogen_bromide " \
                      " acetic_acid hydrogen_chloride hydrochloric_acid perchloric_acid hydrogen_cyanide" \
                      " carbonic_acid hydrogen_fluoride hydrofluoric_acid hydrogen_iodide nitrous_acid" \
                      " nitric_acid phosphoric_acid hydrogen_suflide sulfurous_acid sulfuric_acid" \
                      " iodine_heptafluoride potassium_bromide potassium_hydroxide lithium_chloride magnesium_nitride" \
                      " sodium_chloride bicarbonate_of_soda sodium_oxide sodium_hydroxide sodium_sulfate ammonia hydrazine nitric_oxide" \
                      " nitorgen_dioxide dinitrogen_tetroxide nitrous_oxide dinitrogen_pentoxide phosphorus_pentafluoride" \
                      " sulfur_dioxide sulfur_trioxide"
''' This list of compounds and names will help retrieve names from formulas. Doesn't work. Why? '''
compound_names_dict = {'aluminum_carbide': 'Al4C3', 'aluminum_chloride': 'AlCl3', 'air': 'Ar2He2Kr2Ne2Xe2Rn2',
                        'boron_trichloride': 'BCl3', 'methane': 'CH4', 'ethane': 'C2H6', 'propane': 'C3H8',
                        'butane': 'C4H10', '2-methylpropane': 'C4H10_M', 'pentane': 'C5H12', 'hexane': 'C6H14',
                        'heptane': 'C7H16', 'octane': 'C8H18', 'nonane': 'C9H20', 'decane': 'C10H22',
                        'tetradecane': 'C14H30', 'octadecane': 'C18H38', 'calcium_dihydrogen_phosphate': 'CaH2PO4',
                        'calcium_iodide': 'CaI', 'calcium_hydroxide': 'CaOH2', 'calcium_phosphide': 'Ca3P2',
                        'cadmium_sulfide': 'CdS', 'cesium_fluoride': 'CsF', 'citric_acid': 'C6H8O7',
                        'acetic_acid': 'HC2H3O2', 'carbon_monoxide': 'CO', 'carbon_dioxide': 'CO2',
                        'hydrogen_bromide': 'HBr',
                        'hydrochloric_acid': 'HCl', 'perchloric_acid': 'HClO4', 'hydrogen_cyanide': 'HCN',
                        'carbonic_acid': 'H2CO3', 'hydrofluoric_acid': 'HF',
                        'hydroiodic_acid': 'HI', 'nitrous_acid': 'HNO2',
                        'nitric_acid': 'HNO3', 'phosphoric_acid': 'H3PO4',
                        'hydrosulfuric_acid': 'H2S', 'sulfurous_acid': 'H2SO3', 'sulfuric_acid': 'H2SO4',
                        'iodine_heptafluoride': 'IF7', 'potassium_bromide': 'KBr', 'potassium_hydroxide': 'KOH',
                        'lithium_chloride': 'LiCl', 'magnesium_nitride': 'Mg3N2', 'sodium_chloride': 'NaCl',
                        'bicarbonate_of_soda': 'NaHCO3', 'sodium_oxide': 'Na2O', 'sodium_hydroxide': 'NaOH',
                        'sodium_sulfate': 'Na2SO4', 'ammonia': 'NH3', 'hydrazine': 'N2H4', 'nitric_oxide': 'NO',
                        'nitorgen_dioxide': 'NO2', 'dinitrogen_tetroxide': 'N2O4', 'nitrous_oxide': 'N2O',
                        'dinitrogen_pentoxide': 'N2O5', 'phosphorus_pentafluoride': 'PF5', 'sulfur_dioxide': 'SO2',
                        'sulfur_trioxide': 'SO3'}
ion_names_dict = {'acetate': 'C2H3O2', 'chlorite': 'ClO2', 'chlorate': 'ClO3', 'perchlorate': 'ClO4',
                  'cyanide': 'CN', 'carbonate': 'CO32', 'copper_(II)_sulfide': 'CuS', 'iron_(II)_chloride': 'FeCl2',
                  'iron_(III)_chloride': 'FeCl3', 'dihydrogen_phosphate': 'H2PO4', 'hydrogen_carbonate': 'HCO3',
                  'mercury_(I)_oxide': 'Hg2O', 'mercury_(II)_oxide': 'HgO', 'hydronium': 'H3O',
                  'hydrogen_phosphate': 'HPO42', 'hydrogen_sulfate': 'HSO4', 'hydroxide': 'OH',
                  'ammonium': 'NH4', 'nitrate': 'NO3', 'nitrite': 'NO2',
                  'permanganate': 'MnO4', 'peroxide': 'H2O22', 'sulfate': 'SO42',
                  'sulfite': 'SO32', 'phosphate': 'PO43'}
ion_symbols_list = "C2H3O2 ClO2 ClO3 ClO4 CN CO32 CuS FeCl2 FeCl3 H2PO4 HCO3 Hg2O HgO H3O HPO42 HSO4 OH NH4 NO3 NO2 MnO4 O22 SO42 SO32 PO43"
ion_names_list = "acetate chlorite chlorate perchlorate cyanide carbonate copper_(II)_sulfide " \
                 "iron_(II)_chloride iron_(III)_chloride dihydrogen_phosphate hydrogen_carbonate " \
                 "mercury_(I)_oxide mercury_(II)_oxide hydronium hydrogen_phosphate hydrogen_sulfate " \
                 "hydroxide ammonium nitrate nitrite permanganate peroxide sulfate sulfite phosphate "

acids_symbol_string = "No list yet"
acids_names_string = "No list yet"
bases_symbol_string = "No list yet"
bases_symbol_string = "No list yet"
bases_names_string = "No list yet"

unit_values = "Moles grams kilograms ounces pounds liters(l) liters(g) ml(l) ml(g)"
environment = "Laboratory Industry Nature"
temp_units = "K F C"
press_units = "atm torr psi mmHg"
equipment = "refinery blah1 blah2"
energy_type = "heat electricity"
catalyst = "blah1 blah2 blah3 blah4"
side_effects = "air_polution water_polution land_polution"
by_products = "CO CO2 NO NO2"
variables = "Av Bv Cv Kv"  # Variable names cannot conflict with element symbols like B C H K etc

def define_variables():
    pass

record_name = ""  # This is a placeholder for a record name to store the process in the database.
''' The following are lists of variables to fill various combo boxes until proper lists are made. '''

''' Variables to hold the selected items of combo boxes. '''
#process_selected = ""
equipment_selected = ""
energy_type_selected = ""
catalyst_selected = ""
side_effect_selected = ""
by_product_selected = ""
variable_selected = ""
variable_value = DoubleVar()
Init_default_T_and_P = FALSE
Av = DoubleVar()
Bv = DoubleVar()
Cv = DoubleVar()
Kv = DoubleVar()
''' Miscellaneous variables to use until proper variables are created. '''
valences = "7 6 5 4 3 2 1 0 -1 -2 -3 -4"
default_temp_units = StringVar()
default_temp_qty = DoubleVar()
default_press_units = StringVar()
default_press_qty = DoubleVar()
eci_1 = StringVar()
eci_2 = StringVar()
eci_3 = StringVar()
eci_4 = StringVar()
eci_5 = StringVar()
eci_6 = StringVar()
eci_1_col = IntVar()
eci_2_col = IntVar()
eci_3_col = IntVar()
eci_4_col = IntVar()
eci_5_col = IntVar()
eci_6_col = IntVar()
eci_1_electronegativity = DoubleVar()
eci_2_electronegativity = DoubleVar()
eci_3_electronegativity = DoubleVar()
eci_4_electronegativity = DoubleVar()
eci_5_electronegativity = DoubleVar()
eci_6_electronegativity = DoubleVar()
eci_1_group = StringVar()
eci_2_group = StringVar()
eci_3_group = StringVar()
eci_4_group = StringVar()
eci_5_group = StringVar()
eci_6_group = StringVar()
eci_1_M_qty = DoubleVar()
eci_2_M_qty = DoubleVar()
eci_3_M_qty = DoubleVar()
eci_4_M_qty = DoubleVar()
eci_5_M_qty = DoubleVar()
eci_6_M_qty = DoubleVar()
eci_1_mass = DoubleVar()
eci_2_mass = DoubleVar()
eci_3_mass = DoubleVar()
eci_4_mass = DoubleVar()
eci_5_mass = DoubleVar()
eci_6_mass = DoubleVar()
eci_1_name = StringVar()
eci_2_name = StringVar()
eci_3_name = StringVar()
eci_4_name = StringVar()
eci_5_name = StringVar()
eci_6_name = StringVar()
eci_1_Oxidation_State = StringVar()
eci_2_Oxidation_State = StringVar()
eci_3_Oxidation_State = StringVar()
eci_4_Oxidation_State = StringVar()
eci_5_Oxidation_State = StringVar()
eci_6_Oxidation_State = StringVar()
eci_1_qty = DoubleVar()
eci_2_qty = DoubleVar()
eci_3_qty = DoubleVar()
eci_4_qty = DoubleVar()
eci_5_qty = DoubleVar()
eci_6_qty = DoubleVar()
eci_1_type = StringVar()
eci_2_type = StringVar()
eci_3_type = StringVar()
eci_4_type = StringVar()
eci_5_type = StringVar()
eci_6_type = StringVar()
eci_1_units = StringVar()
eci_2_units = StringVar()
eci_3_units = StringVar()
eci_4_units = StringVar()
eci_5_units = StringVar()
eci_6_units = StringVar()
eci_1_valence = StringVar()
eci_2_valence = StringVar()
eci_3_valence = StringVar()
eci_4_valence = StringVar()
eci_5_valence = StringVar()
eci_6_valence = StringVar()
eci_kl_1_qty = DoubleVar()
eci_kl_2_qty = DoubleVar()
eci_kl_3_qty = DoubleVar()
eci_kl_4_qty = DoubleVar()
eci_kl_5_qty = DoubleVar()
eci_kl_6_qty = DoubleVar()
eci_1_kl_units = StringVar()
eci_2_kl_units = StringVar()
eci_3_kl_units = StringVar()
eci_4_kl_units = StringVar()
eci_5_kl_units = StringVar()
eci_6_kl_units = StringVar()
eci_1_mm_units = StringVar()
eci_2_mm_units = StringVar()
eci_3_mm_units = StringVar()
eci_4_mm_units = StringVar()
eci_5_mm_units = StringVar()
eci_6_mm_units = StringVar()
eci_1_temp_units = StringVar()
eci_2_temp_units = StringVar()
eci_3_temp_units = StringVar()
eci_4_temp_units = StringVar()
eci_5_temp_units = StringVar()
eci_6_temp_units = StringVar()
eci_temp_1_qty = DoubleVar()
eci_temp_2_qty = DoubleVar()
eci_temp_3_qty = DoubleVar()
eci_temp_4_qty = DoubleVar()
eci_temp_5_qty = DoubleVar()
eci_temp_6_qty = DoubleVar()
eci_1_press_units = StringVar()
eci_2_press_units = StringVar()
eci_3_press_units = StringVar()
eci_4_press_units = StringVar()
eci_5_press_units = StringVar()
eci_6_press_units = StringVar()
eci_press_1_qty = DoubleVar()
eci_press_2_qty = DoubleVar()
eci_press_3_qty = DoubleVar()
eci_press_4_qty = DoubleVar()
eci_press_5_qty = DoubleVar()
eci_press_6_qty = DoubleVar()
eci_heat_1_qty = DoubleVar()
eci_heat_2_qty = DoubleVar()
eci_heat_3_qty = DoubleVar()
eci_heat_4_qty = DoubleVar()
eci_heat_5_qty = DoubleVar()
eci_heat_6_qty = DoubleVar()
energy_amount = DoubleVar()
eci_1_heat_units = StringVar()
eci_2_heat_units = StringVar()
eci_3_heat_units = StringVar()
eci_4_heat_units = StringVar()
eci_5_heat_units = StringVar()
eci_6_heat_units = StringVar()
eci_heat_1_qty = DoubleVar()
eci_heat_2_qty = DoubleVar()
eci_heat_3_qty = DoubleVar()
eci_heat_4_qty = DoubleVar()
eci_heat_5_qty = DoubleVar()
eci_heat_6_qty = DoubleVar()
other_1_qty = StringVar()
other_2_qty = StringVar()
other_3_qty = StringVar()
other_4_qty = StringVar()
other_5_qty = StringVar()
other_6_qty = StringVar()
other_1_units = StringVar()
other_2_units = StringVar()
other_3_units = StringVar()
other_4_units = StringVar()
other_5_units = StringVar()
other_6_units = StringVar()
alpha_4 = StringVar()
molar_mass = DoubleVar()
ion_4_charge = IntVar()
total_mass = DoubleVar()
cb_1_type = ""  # elements compounds ions
cb_2_type = ""
cb_3_type = ""
cb_4_type = ""
cb_5_type = ""
cb_6_type = ""

''' Add functions here'''

def select_eci_1_type(eventObject):
    '''
    Use these comboboxes to load the correct symbols/formulae and names
    in the associated comboboxes
    '''
    current_dict = eci_1
    print("Enter select_eci_1_type.")
    t_Explanations.insert(END, "Entered substance 1 type. \n")
    eci_1_d['type'] = cb_Select_CB1.get()
    cb_1_type = eci_1_d['type']
    # f"Hello, {name}. You are {age}."
    t_Explanations.insert(END, f"User selected substance type {cb_1_type} \n")
    print("933 cb_1_type = ", cb_1_type)
    current_item_info['s_type'] = cb_1_type #     s_type, s_id, s_id_formula, substance
    print("935 eci_1_d['type'] = ", eci_1_d['type'])
    if cb_1_type == 'elements':
        cb_eci_1['values'] = element_symbol_string #elements_symbols_list # element_symbol_string
        cb_eci_1_N['values'] = element_name_string #elements_name_list   # element_name_string
    elif cb_1_type == 'compounds':  #ionic-compounds
        cb_eci_1['values'] = compound_formula_string
        cb_eci_1_N['values'] = compound_name_string
    elif cb_1_type == 'ions':
        print("835 substance type ions not yet implemented.")
        cb_eci_1['values'] = ion_symbols_string
        cb_eci_1_N['values'] = ion_names_string
    elif cb_1_type == 'polyatomic':
        print("835 substance type polyatomic not yet implemented.")
        cb_eci_1['values'] = polyatomic_formula_string
        cb_eci_1_N['values'] = polyatomic_name_string
    else:
        print("Error is select_eci_1_type")


def select_eci_2_type(eventObject):
    print("847 Enteinside_frame select_eci_2_type.")
    current_dict = eci_2
    print("Entered select_eci_2_type.")
    eci_2_d['type'] = cb_Select_CB2.get()
    cb_2_type = eci_2_d['type']
    print("933 cb_2_type = ", cb_2_type)
    current_item_info['s_type'] = cb_2_type #     s_type, s_id, s_id_formula, substance
    print("935 eci_2_d['type'] = ", eci_2_d['type'])
    if cb_2_type == 'elements':
        cb_eci_2['values'] = element_symbol_string #elements_symbols_list # element_symbol_string
        cb_eci_2_N['values'] = element_name_string #elements_name_list   # element_name_string
    elif cb_2_type == 'compounds':  #ionic-compounds
        cb_eci_2['values'] = compound_formula_string
        cb_eci_2_N['values'] = compound_name_string
    elif cb_2_type == 'ions':
        cb_eci_2['values'] = ion_symbols_string
        cb_eci_2_N['values'] = ion_names_string
    elif cb_2_type == 'polyatomic':
        cb_eci_2['values'] = polyatomic_formula_string
        cb_eci_2_N['values'] = polyatomic_name_string
    else:
        print("Error is select_eci_2_type")

def select_eci_3_type(eventObject):
    print("Entered select_eci_3_type.")
    current_dict = eci_3
    eci_3_d['type'] = cb_Select_CB3.get()
    cb_3_type = eci_3_d['type']
    print("933 cb_3_type = ", cb_3_type)
    current_item_info['s_type'] = cb_3_type #     s_type, s_id, s_id_formula, substance
    print("935 eci_3_d['type'] = ", eci_3_d['type'])
    if cb_3_type == 'elements':
        cb_eci_3['values'] = element_symbol_string #elements_symbols_list # element_symbol_string
        cb_eci_3_N['values'] = element_name_string #elements_name_list   # element_name_string
    elif cb_3_type == 'compounds':  #ionic-compounds
        cb_eci_3['values'] = compound_formula_string
        cb_eci_3_N['values'] = compound_name_string
    elif cb_3_type == 'ions':
        cb_eci_3['values'] = ion_symbols_string
        cb_eci_3_N['values'] = ion_names_string
    elif cb_3_type == 'polyatomic':
        cb_eci_3['values'] = polyatomic_formula_string
        cb_eci_3_N['values'] = polyatomic_name_string
    else:
        print("Error is select_eci_3_type")

def select_eci_4_type(eventObject):
    print("Entered select_eci_4_type.")
    current_dict = eci_4
    eci_4_d['type'] = cb_Select_CB4.get()
    cb_4_type = eci_4_d['type']
    print("933 cb_type = ", cb_4_type)
    current_item_info['s_type'] = cb_4_type #     s_type, s_id, s_id_formula, substance
    print("935 eci_4_d['type'] = ", eci_4_d['type'])
    if cb_4_type == 'elements':
        cb_eci_4['values'] = element_symbol_string #elements_symbols_list # element_symbol_string
        cb_eci_4_N['values'] = element_name_string #elements_name_list   # element_name_string
    elif cb_4_type == 'compounds':  #ionic-compounds
        cb_eci_4['values'] = compound_formula_string
        cb_eci_4_N['values'] = compound_name_string
    elif cb_4_type == 'ions':
        cb_eci_4['values'] = ion_symbols_string
        cb_eci_4_N['values'] = ion_names_string
    elif cb_4_type == 'polyatomic':
        cb_eci_4['values'] = polyatomic_formula_string
        cb_eci_4_N['values'] = polyatomic_name_string
    else:
        print("Error is select_eci_4_type")


def select_eci_5_type(eventObject):
    print("Entered select_eci_5_type.")
    current_dict = eci_5
    eci_5_d['type'] = cb_Select_CB5.get()
    cb_5_type = eci_5_d['type']
    print("933 cb_type = ", cb_5_type)
    current_item_info['s_type'] = cb_5_type #     s_type, s_id, s_id_formula, substance
    print("935 eci_5_d['type'] = ", eci_5_d['type'])
    if cb_5_type == 'elements':
        cb_eci_5['values'] = element_symbol_string #elements_symbols_list # element_symbol_string
        cb_eci_5_N['values'] = element_name_string #elements_name_list   # element_name_string
    elif cb_5_type == 'compounds':  #ionic-compounds
        cb_eci_5['values'] = compound_formula_string
        cb_eci_5_N['values'] = compound_name_string
    elif cb_5_type == 'ions':
        cb_eci_5['values'] = ion_symbols_string
        cb_eci_5_N['values'] = ion_names_string
    elif cb_5_type == 'polyatomic':
        cb_eci_5['values'] = polyatomic_formula_string
        cb_eci_5_N['values'] = polyatomic_name_string
    else:
        print("Error is select_eci_5_type")


def select_eci_6_type(eventObject):
    print("Entered select_eci_6_type.")
    current_dict = eci_6
    eci_6_d['type'] = cb_Select_CB6.get()
    cb_6_type = eci_6_d['type']
    print("933 cb_type = ", cb_6_type)
    current_item_info['s_type'] = cb_6_type #     s_type, s_id, s_id_formula, substance
    print("935 eci_6_d['type'] = ", eci_6_d['type'])
    if cb_6_type == 'elements':
        cb_eci_6['values'] = element_symbol_string #elements_symbols_list # element_symbol_string
        cb_eci_6_N['values'] = element_name_string #elements_name_list   # element_name_string
    elif cb_6_type == 'compounds':  #ionic-compounds
        cb_eci_6['values'] = compound_formula_string
        cb_eci_6_N['values'] = compound_name_string
    elif cb_6_type == 'ions':
        cb_eci_6['values'] = ion_symbols_string
        cb_eci_6_N['values'] = ion_names_string
    elif cb_6_type == 'polyatomic':
        cb_eci_6['values'] = polyatomic_formula_string
        cb_eci_6_N['values'] = polyatomic_name_string
    else:
        print("Error is select_eci_6_type")


''' Start defining process and chemistry related functions '''



def minor_process_selected(eventObject):
    """ print("process_selected") """
    # if process_selected == Calculate:
    # Change the following message to a window with instructions.
    #showinfo(title=None, message="To calculate eci variables, enter an element type and symbol and a mole quantity.")
    #tkMessageBox.showinfo(message='Hello')
    #"Set_STP_Variables Pressure Volume, moles Temperature pvnrt"
    print('1068 minor_process_selected function entered.', eventObject)
    if minor_process_selected == Set_STP_Variables():
        print("In Continue function at major_process_selected == 'Set_STP_Variables'")
        ''' Continue the Set_STP_Variables process '''
    elif minor_process_selected == 'pvnrt':
        pvnrt()
    else: print('minor_process_selected fell thru to else clause.')

def Set_STP_Variables():
    """
    Set the initial units and values of temperature and pressure to standard temperature and pressure
    (0°C) and  (1 atm)
    """
    print('1075 Set_STP_Variables function entered.')
    ''' The following code works to set initial STP variables for all 6 frames. '''
    eci_1_temp_units = cb_1_Temp_Units.set('C')
    eci_1_d['temp_display_units'] = "C"
    e_Temp_Qty_1.delete(0, tk.END)
    e_Temp_Qty_1.insert(0, 0)
    eci_1_d['temp_display_qty'] = 0
    eci_1_press_units = cb_1_Press_Units.set('atm')
    eci_1_d['press_display_units'] = "atm"
    e_Press_Qty_1.delete(0, tk.END)
    e_Press_Qty_1.insert(0, 1.0)
    eci_1_d['temp_display_qty'] = 0.0
    eci_1_d['press_display_qty'] = 1.0

    eci_2_temp_units = cb_2_Temp_Units.set('C')
    eci_2_d['temp_display_units'] = "C"
    e_Temp_Qty_2.delete(0, tk.END)
    e_Temp_Qty_2.insert(0, 0)
    eci_2_d['temp_display_qty'] = 0
    eci_2_press_units = cb_2_Press_Units.set('atm')
    eci_2_d['press_display_units'] = "atm"
    e_Press_Qty_2.delete(0, tk.END)
    e_Press_Qty_2.insert(0, 1.0)
    eci_2_d['press_display_qty'] = 1.0

    eci_3_temp_units = cb_3_Temp_Units.set('C')
    eci_3_d['temp_display_units'] = "C"
    e_Temp_Qty_3.delete(0, tk.END)
    e_Temp_Qty_3.insert(0, 0)
    eci_3_d['temp_display_qty'] = 0
    eci_3_press_units = cb_3_Press_Units.set('atm')
    eci_3_d['press_display_units'] = "atm"
    e_Press_Qty_3.delete(0, tk.END)
    e_Press_Qty_3.insert(0, 1.0)
    eci_3_d['press_display_qty'] = 1.0

    eci_4_temp_units = cb_4_Temp_Units.set('C')
    eci_4_d['temp_display_units'] = "C"
    e_Temp_Qty_4.delete(0, tk.END)
    e_Temp_Qty_4.insert(0, 0)
    eci_4_d['temp_display_qty'] = 0
    eci_4_press_units = cb_4_Press_Units.set('atm')
    eci_4_d['press_display_units'] = "atm"
    e_Press_Qty_4.delete(0, tk.END)
    e_Press_Qty_4.insert(0, 1.0)
    eci_4_d['press_display_qty'] = 1.0

    eci_5_temp_units = cb_5_Temp_Units.set('C')
    eci_5_d['temp_display_units'] = "C"
    e_Temp_Qty_5.delete(0, tk.END)
    e_Temp_Qty_5.insert(0, 0)
    eci_5_d['temp_display_qty'] = 0
    eci_5_press_units = cb_1_Press_Units.set('atm')
    eci_5_d['press_display_units'] = "atm"
    e_Press_Qty_5.delete(0, tk.END)
    e_Press_Qty_5.insert(0, 1.0)
    eci_1_d['press_display_qty'] = 1.0

    eci_6_temp_units = cb_6_Temp_Units.set('C')
    eci_6_d['temp_display_units'] = "C"
    e_Temp_Qty_6.delete(0, tk.END)
    e_Temp_Qty_6.insert(0, 0)
    eci_6_d['temp_display_qty'] = 0
    eci_6_press_units = cb_6_Press_Units.set('atm')
    eci_6_d['press_display_units'] = "atm"
    e_Press_Qty_6.delete(0, tk.END)
    e_Press_Qty_6.insert(0, 1.0)
    eci_6_d['press_display_qty'] = 1.0

    
def major_process_selected():
    print("1193 In Continue function at major_process_selected")
    Continue()

def Continue():
    '''A button/function to continue whatever process was selected. '''
    print("1198 In Continue function")
    major_process_selected = cb_Select_M_Process.get() #cb_Select_Process.get()
    minor_process_selected = cb_Select_m_Process.get()
    #print("Process selected is ", process_selected)
    # check_entry_changes(
    #
    if major_process_selected == 'Acid_Base':
        print("In Continue function at major_process_selected == 'Acid_Base'")
        ''' Continue the Acid_Base process '''
        Acid_Base()
    elif major_process_selected == 'Balance_Equation':
        print("In Continue function at major_process_selected == 'Balance_Equation'")
        Balance_Equation()
    elif major_process_selected == 'Calculate':
        print("In Continue function at major_process_selected == 'Calculate'")

        ''' Continue the Calculate process '''
        check_entry_changes()
        #calculate()
    elif major_process_selected == 'Decompose':
        print("In Continue function at major_process_selected == 'Decompose'")
        """ Continue the Decompose process """
        Decompose()
    elif major_process_selected == 'Set_default_T_and_P':
        print("In Continue function at major_process_selected == 'Set_default_T_and_P'")
        """ Continue the Initialize_default_T_and_P process """
        #if Init_default_T_and_P == FALSE:
        #    pdb.set_trace()
        #    Initialize_default_T_and_P()
        #    Init_default_T_and_P == TRUE
        set_t_and_p_inst = "Set the default temperature and pressure settings you want to use" \
                           "for the current process. Select Set_default_T_and_P from the Process " \
                           "combobox, then select/set the temperature and pressure units and quantities" \
                           "in the first eci frame. Then press the Continue button. After you have set these" \
                           "defaults, select the next process. "
        e_Explanation.insert(END, set_t_and_p_inst)
        Set_default_T_and_P()
    elif major_process_selected == 'Oxidation_Reduction':
        print("In Continue function at major_process_selected == 'Oxidation_Reduction'")
        """ Continue the Oxidation_Reduction process """
        Oxidation_Reduction()
    elif major_process_selected == 'Metathesis':
        print("In Continue function at major_process_selected == 'Metathesis'")
        """ Continue the Metathesis process """
        Metathesis()
    elif major_process_selected == 'Oxidation_Rate':
        print("In Continue function at major_process_selected == 'Oxidation_Rate'")
        """ Continue the Oxidation_Rate process """
        Oxidation_Rate()
    elif major_process_selected == 'Parse_Reactants':
        print("In Continue function at major_process_selected == 'Parse_Reactants'")
        ''' There is a general procedure used to prove parse works,
        and a procedure tied to the eci_1 combobox. '''
        Parse_Reactants()
    elif major_process_selected == 'Parse_Products':
        print("In Continue function at major_process_selected == 'Parse_Products'")
        ''' There is a general procedure used to prove parse works,
        and a procedure tied to the eci_1 combobox. '''
        Parse_Products()
    elif major_process_selected == 'Precipitation':
        print("In Continue function at major_process_selected == 'Precipitation'")
        """ Continue the Precipitation process """
        Precipitation()
    elif major_process_selected == 'Reduction':
        print("In Continue function at major_process_selected == 'Reduction'")
        """ Continue the Reduction process """
        Reduction()
    elif major_process_selected == 'Refine':
        print("In Continue function at major_process_selected == 'Refine'")
        """ Continue the Refine process """
        Refine()
    elif major_process_selected == 'Synthesis':
        print("In Continue function at major_process_selected == 'Synthesis'")
        """ Continue the Synthesis process """
        Synthesis()

    elif minor_process_selected == "Set_STP_Variables":
        print("In Continue function at major_process_selected == 'Set_STP_Variables'")
        Set_STP_Variables()
    elif minor_process_selected == 'pvnrt':
        pvnrt()
    elif minor_process_selected == 'vol_from_prt':
        vol_from_prt()
    else:
        print("No process has been selected in Continue selection of process")
    # CountElements()
    # AlphabetizeElements()
    # eci_1 = cb_eci_1.get()
    # print("Process selected is " , process_selected)
    # print('eci_1 = ', eci_1)
    # print("Pressed Continue button")

#def Set_default_T_and_P():
#    print("1287 In Set_default_T_and_P function")

def Balance_Equation():
    print("1290 In Set_default_T_and_P function")
    be = ""
    print("Started Balance_Equation")
    e_Explanation.insert(END, "Started Balance_Equation")
    e_Explanation.insert(END, '\n')
    e_Explanation.insert(END, "Step 1: ")
    if cb_eci_1.get() != "":
        be = cb_eci_1.get()
        print("cb_eci_1 is ", be)
        #e_Explanation.insert(END, cb_eci_1.get())
    if cb_eci_2.get() != "":
        be = be + " + " + cb_eci_2.get()
        print("cb_eci_2 is ", be)
        #e_Explanation.insert(END, be)
    if cb_eci_3.get() != "":
        be = be + " + " + cb_eci_3.get()
        print("cb_eci_3 is ", be)
        #e_Explanation.insert(END, be)
    if cb_eci_4.get() != "":
        be = be + " --> " + cb_eci_4.get()
        print("cb_eci_4 is ", be)
        #e_Explanation.insert(END, be)
    if cb_eci_5.get() != "":
        be = be + " + " + cb_eci_5.get()
        print("cb_eci_5 is ", be)
        #e_Explanation.insert(END, be)
    if cb_eci_6.get() != "":
        be = be + " + " + cb_eci_6.get()
        print("cb_eci_6 is ", be)
    e_Explanation.insert(END, be)

def calculate():
    print("1322 In calculate function")
    ''' A step toward performing general chemistry related calculations.
    There will be many calculations done by the program.
    They will be separated into separate functions as they are developed.'''
    #Message.config(font, titlefont)
    #showinfo.__setattr__(font, 'Helvetica 12') # Doesn't work
    #mb.Dialog.show(title=None, message="To calculate eci variable, senter an element type and symbol and a mole quantity.")
    #showinfo(title=None, message="To calculate eci variables, enter an element type and symbol and a mole quantity.")
    #check_entry_changes()
    #calculate_eci_variables()



def setElementInitialVariables(eci, cb_type):
    """ When an element is selected, set the formula, name, units to grams, moles to 1, and valence if numeric (not a list of numbers)"""
    print("1228 eci_d[eci]['name'] = ", eci_d[eci]['name'])
    s_formula = eci_d[eci]['formula']
    print('1485 Entered setElementInitialVariables. cb_type is ', eci, cb_type, )
    t_Explanations.insert(END, f"Set initial element variables for {s_formula} \n")
    if cb_type == "elements":
        # print("1487 Entered if cb_type ==", cb_type)
        print("1484 eci_d[eci]['type'] is ", eci_d[eci]['type'])
        print("1489 eci_d[eci]['formula'] = ", eci_d[eci]['formula'])
        current_item_info = dict(s_type = "", s_id = "", s_id_formula = "", substance = "") 
        current_item_info["s_id"] = eci_d[eci]['id'] #     s_type, s_id, s_id_formula, substance
        current_item_info["s_id_formula"] = eci_d[eci]['formula'] #     s_type, s_id, s_id_formula, substance
        current_item_info["s_id_formula"] = eci_d[eci]['name'] #     s_type, s_id, s_id_formula, substance
        print("1238 set dict variables, db[eci]['mass'] is ")
        eci_d[eci]['mass'] = db[s_formula]['mass']
        eci_d[eci]['qty'] = db[s_formula]['mass']
        print("1241 after set dict variables")
        # eci_mass = db[eci]['mass']  
        # eci_d[eci]['mass'] = db[eci]['mass'] #db[eci_1]['mass']
        # eci_d[eci]['valence'] = db[eci]['valence']
        # eci_d[eci]['units'] = "grams"
        # eci_d[eci]['qty'] = db[eci]['mass'] #db[eci_1]['mass']
        # eci_d[eci]['M_qty'] = 1

        
        # cb_1_Temp_Units.values = "C"
        # e_Temp_Qty_1.delete(0, tk.END)
        # e_Temp_Qty_1.insert(0, eci_1_qty)

        # e_eci_1_qty.insert(0, eci_1_qty) 
        # refresh_display(eci)
        # print('1451 eci_mass is ', eci_mass) #eci_1.get['mass'])
        # eci_1_qty = eci_1_mass  #db[eci_1.get()]['eci_1_mass']
        ''' ************************************************************ '''
        ''' The following works to inset the (atomic mass) into the quantity entry widget! '''
        ''' But, it only works if an element symbol is selected; not if the name is selected. '''
        
        # refresh_s_1_display()
  #eci_1_mass)
        # dbr['R1']['eci_1_qty'] = e_eci_1_qty.get()
        # print("dbr['R1']['eci_1_qty'] is ", dbr['R1']['eci_1_qty'])
    else: print('1533 else clause cb_type != "elements":')


def setSelectedItemInitialVariables(eci, cb_type):
        """
        Use this function to set all the variables associated with a selected item.
        For example, set the atomic number or molecular mass, and display the appropriate values.
        such as e_eci_1_qty = eci_1_mass -- find and replace with the appropriate db value
        """
        print("1275 Entered setSelectedItemVariables ", eci, cb_type)
        print("1276 eci_d[eci]['formula'] is ", eci_d[eci]['formula'])
        print("1277 eci_d[eci]['name'] is ", eci_d[eci]['name'])
        t_Explanations.insert(END, f"Set initial variables for {eci_d[eci]['formula']} \n")
        ''' I added an additional criteria to check so all statements don't run extra times. '''
        ''' If the type is elements and the formula is different, process it; otherwise pass.'''
        print("1279 if cb_type ", eci, eci_d[eci]['formula'])
        if cb_type == 'elements': # and eci_1_d['formula'] != cb_eci_1.get():
            print("1290 if cb_type == 'elements'", cb_type)
            eci_d[eci]['units'] = 'grams'
            eci_d[eci]['M_qty'] = 1
            eci_d[eci]['M_units'] = "moles"
            setElementInitialVariables(eci, cb_type)
            # print("1279 After setElementInitialVariables")
            # print('e_eci_1_qty is ', e_eci_1_qty.get())
            refresh_display(eci)
        elif cb_type == 'compounds': # and eci_1_d['formula'] != cb_eci_1.get():
            print("1299 if cb_type == 'compounds'", cb_type)
            eci_d[eci]['units'] = 'grams'
            eci_d[eci]['M_qty'] = 1
            eci_d[eci]['M_units'] = "moles"
            ec_f = eci_d[eci]['formula']
            print("1304 eci_d[ec_f]['mass'] is ", eci_d[eci]['units'])
            print("1305 ec_f is ", ec_f)
            # print("1305 ec_f is ", ec_f)
            current_item_info = dict(s_type = "", s_id = "", s_id_formula = "", substance = "") 
            current_item_info["s_id"] = eci_d[eci]['id'] #     s_type, s_id, s_id_formula, substance
            current_item_info["s_id_formula"] = eci_d[eci]['formula'] #     s_type, s_id, s_id_formula, substance
            current_item_info["s_id_formula"] = eci_d[eci]['name'] #     s_type, s_id, s_id_formula, substance
            print("1309 eci_d[ec_f]['mass'] is ", eci_d[eci]['units'])
            eci_d[eci]['mass'] = c_db[ec_f]['mass']
            print("1311 eci_d[ec_f]['mass'] is ", eci_d[eci]['units'])
            eci_d[eci]['qty'] = c_db[ec_f]['mass']
            print("1308 eci_d[eci]['mass'] is ", eci_d[eci]['mass'])
            refresh_display(eci)
        elif cb_type == 'ions': # and eci_1_d['formula'] != cb_eci_1.get():
            print("1482 if cb_type == 'ions'", cb_type)
            eci_d[eci]['units'] = 'grams'
            eci_d[eci]['M_qty'] = 1
            eci_d[eci]['M_units'] = "moles"
            ec_f = eci_d[eci]['formula']
            print("1304 eci_d[ec_f]['mass'] is ", eci_d[eci]['units'])
            print("1305 ec_f is ", ec_f)
            # print("1305 ec_f is ", ec_f)
            current_item_info = dict(s_type = "", s_id = "", s_id_formula = "", substance = "") 
            current_item_info["s_id"] = eci_d[eci]['id'] #     s_type, s_id, s_id_formula, substance
            current_item_info["s_id_formula"] = eci_d[eci]['formula'] #     s_type, s_id, s_id_formula, substance
            current_item_info["s_id_formula"] = eci_d[eci]['name'] #     s_type, s_id, s_id_formula, substance
            print("1309 eci_d[ec_f]['mass'] is ", eci_d[eci]['units'])
            eci_d[eci]['mass'] = i_db[ec_f]['mass']
            print("1311 eci_d[ec_f]['mass'] is ", eci_d[eci]['units'])
            eci_d[eci]['qty'] = i_db[ec_f]['mass']
            print("1308 eci_d[eci]['mass'] is ", eci_d[eci]['mass'])
            refresh_display(eci)
        elif cb_type == 'polyatomic': # and eci_1_d['formula'] != cb_eci_1.get():
            print("1482 if cb_type == 'ions'", cb_type)
            eci_d[eci]['units'] = 'grams'
            eci_d[eci]['M_qty'] = 1
            eci_d[eci]['M_units'] = "moles"
            ec_f = eci_d[eci]['formula']
            print("1304 eci_d[ec_f]['mass'] is ", eci_d[eci]['units'])
            print("1305 ec_f is ", ec_f)
            # print("1305 ec_f is ", ec_f)
            current_item_info = dict(s_type = "", s_id = "", s_id_formula = "", substance = "") 
            current_item_info["s_id"] = eci_d[eci]['id'] #     s_type, s_id, s_id_formula, substance
            current_item_info["s_id_formula"] = eci_d[eci]['formula'] #     s_type, s_id, s_id_formula, substance
            current_item_info["s_id_formula"] = eci_d[eci]['name'] #     s_type, s_id, s_id_formula, substance
            print("1309 eci_d[ec_f]['mass'] is ", eci_d[eci]['units'])
            eci_d[eci]['mass'] = p_db[ec_f]['mass']
            print("1311 eci_d[ec_f]['mass'] is ", eci_d[eci]['units'])
            eci_d[eci]['qty'] = p_db[ec_f]['mass']
            print("1308 eci_d[eci]['mass'] is ", eci_d[eci]['mass'])
            refresh_display(eci)
            # print("1241 after set dict variables")
                # setElementInitialVariables(eci, cb_type)

        if cb_2_type == 'elements' and eci_2_d['formula'] != cb_eci_2.get():
            print("1532 if cb_type == 'elements'", cb_type)
            eci_d[eci]['units'] = 'grams'
            eci_d[eci]['M_qty'] = 1
            eci_d[eci]['M_units'] = "moles"
            setElementInitialVariables(eci, cb_type)
            # print("1279 After setElementInitialVariables")
            # print('e_eci_1_qty is ', e_eci_1_qty.get())
            refresh_display(eci)

        if cb_3_type == 'elements':
            print("1542 if cb_type == 'elements'", cb_type)
            eci_d[eci]['units'] = 'grams'
            eci_d[eci]['M_qty'] = 1
            eci_d[eci]['M_units'] = "moles"
            setElementInitialVariables(eci, cb_type)
            # print("1279 After setElementInitialVariables")
            # print('e_eci_1_qty is ', e_eci_1_qty.get())
            refresh_display(eci)

            ''' 
            Use the following print statements as needed later. They are currently used above while developing
            the program.
            '''
            #print("dbr['R1']['eci_1_type'] = ", dbr['R1']['eci_1_type'])
            #print("dbr['R1']['eci_1_formula'] is ", dbr['R1']['eci_1_formula'])
            #print("dbr['R1']['eci_1_name'] is ", dbr['R1']['eci_1_name'])
            ''' Shouldn't need the following anymore. Delete when confirmed.'''
            #print("eci_db['eci_1']['name'] is ", eci_db['eci_1']['name'])
            #print("eci_1_d['eci'] is ", eci_1_d['eci'])
            #print("eci_1_d['name'] is ", eci_1_d['name'])
            #dbr['R1']['mass'] = db[eci_1]['mass']
            #dbr['R1']['valence'] = db[eci_1]['valence']
            #eci_d['eci_1']['mass'] = db[eci_1]['mass']
            #eci_d['eci_1']['valence'] = db[eci_1]['valence']
            #e_eci_1_M_qty.delete(0, END)
            #e_eci_1_M_qty.insert(0, 1)

def setEci_1(event):
    #event is <VirtualEvent event x=0 y=0>
    print('1658 Entered setEci_1') 
    eci_d['eci_1']['formula'] = cb_eci_1.get()
    print("1661 eci_1 is ", 'eci_i', eci_d['eci_1']['formula'])
    setSelectedItemName('eci_1')
    
def setEci_2(event):
    print('1658 Entered setEci_2') 
    eci_d['eci_2']['formula'] = cb_eci_2.get()
    print("1661 eci_2 is ", 'eci_i', eci_d['eci_2']['formula'])
    setSelectedItemName('eci_2')

def setEci_3(event):
    print('1587 Entered setEci_3') 
    eci_d['eci_3']['formula'] = cb_eci_3.get()
    print("1661 eci_3 is ", 'eci_i', eci_d['eci_3']['formula'])
    setSelectedItemName('eci_3')

def setEci_4(event):
    print('1658 Entered setEci_4') 
    eci_d['eci_4']['formula'] = cb_eci_4.get()
    print("1661 eci_4 is ", 'eci_i', eci_d['eci_4']['formula'])
    setSelectedItemName('eci_4')

def setEci_5(event):
    print('1502 Entered setEci_5') 
    eci_d['eci_5']['formula'] = cb_eci_5.get()
    print("1504 eci_5 is ", 'eci_i', eci_d['eci_5']['formula'])
    setSelectedItemName('eci_5')

def setEci_6(event):
    print('1508 Entered setEci_6') 
    eci_d['eci_6']['formula'] = cb_eci_6.get()
    print("1510 eci_6 is ", 'eci_i', eci_d['eci_6']['formula'])
    setSelectedItemName('eci_6')

def setSelectedItemName(eci):
    print('1514 Entered setSelectedItemName ', eci) 
    eci_type = eci_d[eci]['type']
    ec_f = eci_d[eci]['formula']
    print("1517 eci_type is ", eci_type, ec_f)

    if eci_type == 'elements':
        print("1363 in if eci_type == ", eci_type)  # eci_d[eci]['type']
        print("1364 eci_1_name == db[eci_1]['name'] is ", db[ec_f]['name'])
        eci_d[eci]['name'] = db[ec_f]['name']
        eci_name = eci_d[eci]['name']
        # cb_eci_1_N.set(eci_name)
        print("1701 eci_name is ", eci_name, eci_d[eci]['name'])
        # print("1703 eci_1_d['name'] is ", eci_d[eci]['name')
        try:
            if eci_name == eci_d[eci]['name']: #eci_1_d['name']: #db[eci_1]['name']:
                print("1706 eci_name == eci_d[eci]['name'] is ", eci_name, eci_d[eci]['name'])
                setSelectedItemInitialVariables(eci, eci_type)
        except KeyError:
            print("1551 not a valid key")
            # cb_eci_1_N.set("not a valid key")
    elif eci_type == 'compounds':
        try:
            eci_d[eci]['name'] = c_db[ec_f]['name']
            eci_name = eci_d[eci]['name']
            # ec_f = eci_d[eci]['formula']
            print("1381 eci_type is ", eci_type, ec_f)
            print("1698 eci_1_name == c_db[eci_1]['name'] is ", c_db[ec_f]['name'])
            print("1611 ec_f is ", eci_type, ec_f)
            # if not eci_1_name == c_db[ec_f]['name']:
            if eci_name == eci_d[eci]['name']:
                # cb_eci_1_N.set(c_db[ec_f]['name'])
                # eci_d['ec_f'] = cb_eci_1.get()
                # eci_d[eci]['name'] = c_db[ec_f]['name']
                print("1388 eci_name == eci_d[eci]['name'] is ", eci_name, eci_d[eci]['name'])
                setSelectedItemInitialVariables(eci, eci_type)
        except KeyError:
            print("1551 not a valid key")
            # cb_eci_1_N.set("not a valid key")
    elif eci_type == 'ions':
        # print("1554 Type ions has not yet been implemented.")
        eci_d[eci]['name'] = i_db[ec_f]['name']
        eci_name = eci_d[eci]['name']
        # ec_f = eci_d[eci]['formula']
        print("1381 eci_type is ", eci_type, ec_f)
        print("1698 eci_1_name == c_db[eci_1]['name'] is ", i_db[ec_f]['name'])
        print("1611 ec_f is ", eci_type, ec_f)
        # if not eci_1_name == c_db[ec_f]['name']:
        if eci_name == eci_d[eci]['name']:
            # cb_eci_1_N.set(c_db[ec_f]['name'])
            # eci_d['ec_f'] = cb_eci_1.get()
            # eci_d[eci]['name'] = c_db[ec_f]['name']
            print("1388 eci_name == eci_d[eci]['name'] is ", eci_name, eci_d[eci]['name'])
            setSelectedItemInitialVariables(eci, eci_type)
    # except KeyError:
            print("1551 not a valid key")
    elif eci_type == 'polyatomic':
        print("1563 Type polyatomic has not yet been implemented.")
        eci_d[eci]['name'] = p_db[ec_f]['name']
        eci_name = eci_d[eci]['name']
        # ec_f = eci_d[eci]['formula']
        print("1381 eci_type is ", eci_type, ec_f)
        print("1698 eci_1_name == c_db[eci_1]['name'] is ", p_db[ec_f]['name'])
        print("1611 ec_f is ", eci_type, ec_f)
        # if not eci_1_name == c_db[ec_f]['name']:
        if eci_name == eci_d[eci]['name']:
            # cb_eci_1_N.set(c_db[ec_f]['name'])
            # eci_d['ec_f'] = cb_eci_1.get()
            # eci_d[eci]['name'] = c_db[ec_f]['name']
            print("1388 eci_name == eci_d[eci]['name'] is ", eci_name, eci_d[eci]['name'])
            setSelectedItemInitialVariables(eci, eci_type)
    # except KeyError:
            print("1551 not a valid key")

    if cb_2_type == 'elements':
        eci_2_d['name'] = eci_2
        try:
            if not eci_2_name == eci_2_d['name']: #db[eci_2]['name']:
                cb_eci_2_N.set(db[eci_2]['name'])
                setSelectedItemInitialVariables('cb_2_type', 'elements')
                #eci_2_d['eci'] = cb_eci_2.get()
                #eci_2_d['name'] = eci_2_name
        except KeyError:
            cb_eci_2_N.set("not a valid key")
    elif cb_2_type == 'compounds':
        try:
            if not eci_2_name == c_db[eci_2]['name']:
                cb_eci_2_N.set(c_db[eci_2]['name'])
                #eci_2_d['eci'] = cb_eci_2.get()
                #eci_2_d['name'] = eci_2_name
        except KeyError:
            cb_eci_2_N.set("not a valid key")
    elif cb_2_type == 'ions':
        try:
            if not eci_2_name == i_db[eci_2]['name']:
                cb_eci_2_N.set(i_db[eci_2]['name'])
                eci_2_d['eci'] = cb_eci_2.get()
                eci_2_d['name'] = eci_2_name
        except KeyError:
            cb_eci_2_N.set("not a valid key")
    if cb_3_type == 'elements':
        try:
            if not eci_3_name == db[eci_3]['name']:
                cb_eci_3_N.set(db[eci_3]['name'])
                setSelectedItemInitialVariables('cb_3_type', 'elements')
                #eci_3_d['eci'] = cb_eci_3.get()
                #eci_3_d['name'] = eci_3_name
        except KeyError:
            cb_eci_3_N.set("not a valid key")
    elif cb_3_type == 'compounds':
        try:
            if not eci_3_name == c_db[eci_3]['name']:
                cb_eci_3_N.set(c_db[eci_3]['name'])
                eci_3_d['eci'] = cb_eci_3.get()
                eci_3_d['name'] = eci_3_name
        except KeyError:
            cb_eci_3_N.set("not a valid key")
    elif cb_3_type == 'ions':
        try:
            if not eci_3_name == i_db[eci_3]['name']:
                cb_eci_3_N.set(i_db[eci_3]['name'])
                eci_3_d['eci'] = cb_eci_3.get()
                eci_3_d['name'] = eci_3_name
        except KeyError:
            cb_eci_3_N.set("not a valid key")
    if cb_4_type == 'elements':
        try:
            if not eci_4_name == db[eci_4]['name']:
                cb_eci_4_N.set(db[eci_4]['name'])
                eci_4_d['eci'] = cb_eci_4.get()
                eci_4_d['name'] = eci_4_name
        except KeyError:
            cb_eci_4_N.set("not a valid key")
    elif cb_4_type == 'compounds':
        try:
            if not eci_4_name == c_db[eci_4]['name']:
                cb_eci_4_N.set(c_db[eci_4]['name'])
                eci_4_d['eci'] = cb_eci_4.get()
                eci_4_d['name'] = eci_4_name
        except KeyError:
            cb_eci_4_N.set("not a valid key")
    elif cb_4_type == 'ions':
        try:
            if not eci_4_name == i_db[eci_4]['name']:
                cb_eci_4_N.set(i_db[eci_4]['name'])
                eci_4_d['eci'] = cb_eci_4.get()
                eci_4_d['name'] = eci_4_name
        except KeyError:
            cb_eci_4_N.set("not a valid key")
    if cb_5_type == 'elements':
        try:
            if not eci_5_name == db[eci_5]['name']:
                cb_eci_5_N.set(db[eci_5]['name'])
                eci_5_d['eci'] = cb_eci_5.get()
                eci_5_d['name'] = eci_5_name
        except KeyError:
            cb_eci_5_N.set("not a valid key")
    elif cb_5_type == 'compounds':
        try:
            if not eci_5_name == c_db[eci_5]['name']:
                cb_eci_5_N.set(c_db[eci_5]['name'])
                eci_5_d['eci'] = cb_eci_5.get()
                eci_5_d['name'] = eci_5_name
        except KeyError:
            cb_eci_5_N.set("not a valid key")
    elif cb_5_type == 'ions':
        try:
            if not eci_5_name == i_db[eci_5]['name']:
                cb_eci_5_N.set(i_db[eci_5]['name'])
                eci_5_d['eci'] = cb_eci_5.get()
                eci_5_d['name'] = eci_5_name
        except KeyError:
            cb_eci_5_N.set("not a valid key")
    if cb_6_type == 'elements':
        try:
            if not eci_6_name == db[eci_6]['name']:
                cb_eci_6_N.set(db[eci_6]['name'])
                eci_6_d['eci'] = cb_eci_6.get()
                eci_6_d['name'] = eci_6_name
        except KeyError:
            cb_eci_6_N.set("not a valid key")
    elif cb_6_type == 'compounds':
        try:
            if not eci_6_name == c_db[eci_6]['name']:
                cb_eci_6_N.set(c_db[eci_6]['name'])
                eci_6_d['eci'] = cb_eci_6.get()
                eci_6_d['name'] = eci_6_name
        except KeyError:
            cb_eci_6_N.set("not a valid key")
    elif cb_6_type == 'ions':
        try:
            if not eci_6_name == i_db[eci_6]['name']:
                cb_eci_6_N.set(i_db[eci_6]['name'])
                eci_6_d['eci'] = cb_eci_6.get()
                eci_6_d['name'] = eci_6_name
        except KeyError:
            cb_eci_6_N.set("not a valid key")
    else:
        pass  # print('In else clause of setSelectedItemName.')

def set_S_1_Formula(ComboboxSelected):
    print('1827 Entered setSelectedItemFormula ')
    eci = 'eci_1'
    formula = eci_d[eci_1]['formula'] #= cb_eci_1.get()
    cb_type = eci_d[eci_1]['type'] #= cb_eci_1.get()
    setSelectedItemNameAux(eci, cb_type)

def setSelectedItemNameAux(eci, cb_type):
    print('1699 Entered setSelectedItemFormula ')

def setSelectedItemFormula(ComboboxSelected):
    print('1837 Entered setSelectedItemFormula ', ComboboxSelected)
    eci_1_N = cb_eci_1_N.get()
    eci_2_N = cb_eci_2_N.get()
    eci_3_N = cb_eci_3_N.get()
    eci_4_N = cb_eci_4_N.get()
    eci_5_N = cb_eci_5_N.get()
    eci_6_N = cb_eci_6_N.get()
    cb_1_type = cb_Select_CB1.get()
    cb_2_type = cb_Select_CB2.get()
    cb_3_type = cb_Select_CB3.get()
    cb_4_type = cb_Select_CB4.get()
    cb_5_type = cb_Select_CB5.get()
    cb_6_type = cb_Select_CB6.get()
    ''' If the name in the name combobox is not the name associated with the selected element, update the name.'''
    if cb_1_type == 'elements':
        if not eci_1 == element_names_Dict[cb_eci_1_N.get()]:
            cb_eci_1.set(element_names_Dict[cb_eci_1_N.get()])
    elif cb_1_type == 'compounds':
        if not eci_1 == compound_names_dict[cb_eci_1_N.get()]:
            cb_eci_1.set(compound_names_dict[cb_eci_1_N.get()])
        else:
            print('eci_1 is already correct and doesn\'t need to be reset')
    elif cb_1_type == 'ions':
        if not eci_1 == ion_names_dict[cb_eci_1_N.get()]:
            cb_eci_1.set(ion_names_dict[cb_eci_1_N.get()])
    if cb_2_type == 'elements':
        if not eci_2 == element_names_Dict[cb_eci_2_N.get()]:
            cb_eci_2.set(element_names_Dict[cb_eci_2_N.get()])
    elif cb_2_type == 'compounds':
        if not eci_2 == compound_names_dict[cb_eci_2_N.get()]:
            cb_eci_2.set(compound_names_dict[cb_eci_2_N.get()])
    elif cb_2_type == 'ions':
        if not eci_2 == ion_names_dict[cb_eci_2_N.get()]:
            cb_eci_2.set(ion_names_dict[cb_eci_2_N.get()])
    if cb_3_type == 'elements':
        if not eci_3 == element_names_Dict[cb_eci_3_N.get()]:
            cb_eci_3.set(element_names_Dict[cb_eci_3_N.get()])
    elif cb_3_type == 'compounds':
        if not eci_3 == compound_names_dict[cb_eci_3_N.get()]:
            cb_eci_3.set(compound_names_dict[cb_eci_3_N.get()])
    elif cb_3_type == 'ions':
        if not eci_3 == ion_names_dict[cb_eci_3_N.get()]:
            cb_eci_3.set(ion_names_dict[cb_eci_3_N.get()])
    if cb_4_type == 'elements':
        if not eci_4 == element_names_Dict[cb_eci_4_N.get()]:
            cb_eci_4.set(element_names_Dict[cb_eci_4_N.get()])
    elif cb_4_type == 'compounds':
        if not eci_4 == compound_names_dict[cb_eci_4_N.get()]:
            cb_eci_4.set(compound_names_dict[cb_eci_4_N.get()])
    elif cb_4_type == 'ions':
        if not eci_4 == ion_names_dict[cb_eci_4_N.get()]:
            cb_eci_4.set(ion_names_dict[cb_eci_4_N.get()])
    if cb_5_type == 'elements':
        if not eci_5 == element_names_Dict[cb_eci_5_N.get()]:
            cb_eci_5.set(element_names_Dict[cb_eci_5_N.get()])
    elif cb_5_type == 'compounds':
        if not eci_5 == compound_names_dict[cb_eci_5_N.get()]:
            cb_eci_5.set(compound_names_dict[cb_eci_5_N.get()])
    elif cb_5_type == 'ions':
        if not eci_5 == ion_names_dict[cb_eci_5_N.get()]:
            cb_eci_5.set(ion_names_dict[cb_eci_5_N.get()])
    if cb_6_type == 'elements':
        if not eci_6 == element_names_Dict[cb_eci_6_N.get()]:
            cb_eci_6.set(element_names_Dict[cb_eci_6_N.get()])
    elif cb_6_type == 'compounds':
        if not eci_6 == compound_names_dict[cb_eci_6_N.get()]:
            cb_eci_6.set(compound_names_dict[cb_eci_6_N.get()])
    elif cb_6_type == 'ions':
        if not eci_6 == ion_names_dict[cb_eci_6_N.get()]:
            cb_eci_6.set(ion_names_dict[cb_eci_6_N.get()])

def eci_1_units_selected(*arg):
    print('1772 Entered eci_1_units_selected ')
    eci = "eci_1"
    units = cb_eci_1_units.get()
    eci_units_selected(eci, units)
def eci_2_units_selected(*arg):
    print('1772 Entered eci_2_units_selected ')
    eci = "eci_2"
    units = cb_eci_2_units.get()
    eci_units_selected(eci, units)
def eci_3_units_selected(*arg):
    print('1772 Entered eci_3_units_selected ')
    eci = "eci_3"
    units = cb_eci_3_units.get()
    eci_units_selected(eci, units)

def eci_4_units_selected(*arg):
    print('1772 Entered eci_4_units_selected ')
    eci = "eci_4"
    units = cb_eci_4_units.get()
    eci_units_selected(eci, units)
def eci_5_units_selected(*arg):
    print('1772 Entered eci_5_units_selected ')
    eci = "eci_5"
    units = cb_eci_5_units.get()
    eci_units_selected(eci, units)
def eci_6_units_selected(*arg):
    print('1772 Entered eci_6_units_selected ')
    eci = "eci_6"
    units = cb_eci_6_units.get()
    eci_units_selected(eci, units)

def eci_units_selected(eci, units):
    print('1760 Entered eci_units_selected ', eci, units)
    eci_d[eci]['units'] =  units
    print("1893 units are ", units)
    if units == 'grams' :
        print("1764 units are ", units)
        mole_change(eci, units)
    elif units =='liters(g)':
        print("1767 units are ", units)
        gas_volume_changes(eci, units)
    # elif units == "P_units":
    #     print("1769 units are ", units)
    # elif units == 'liters(g)':
    #     print("1895 units are ", units)
    #     print("1896 call the gas law calculation function")
        # mole_mass_change(eci, units)
    else:
        print("1900 units not yet processes.")

def eci_1_Temp_units_selected(event):
    # print('1772 Entered eci_4_units_selected ')
    print("1779 Entered eci_1_Temp_units_selected", event)
    eci = "eci_1"
    t_units = cb_1_Temp_Units.get()
    eci_d[eci]["temp_display_units"] = t_units
    # print('1772 Entered eci_4_units_selected ')
    print("1789 Entered eci_1_Temp_units_selected", event)
    p_units = cb_1_Press_Units.get()
    eci_d[eci]["press_display_units"] = p_units
    print("1782 units are ", p_units, eci_d[eci]["press_display_units"])
    eci_Temp_Press_units_selected(eci)
def eci_2_Temp_units_selected(event):
    eci = "eci_2"
    t_units = cb_2_Temp_Units.get()
    eci_d[eci]["temp_display_units"] = t_units
    p_units = cb_2_Press_Units.get()
    eci_d[eci]["press_display_units"] = p_units
    print("1782 units are ", p_units, eci_d[eci]["press_display_units"])
    eci_Temp_Press_units_selected(eci)
def eci_3_Temp_units_selected(event):
    eci = "eci_3"
    t_units = cb_3_Temp_Units.get()
    eci_d[eci]["temp_display_units"] = t_units
    p_units = cb_3_Press_Units.get()
    eci_d[eci]["press_display_units"] = p_units
    print("1782 units are ", p_units, eci_d[eci]["press_display_units"])
    eci_Temp_Press_units_selected(eci)
def eci_4_Temp_units_selected(event):
    eci = "eci_4"
    t_units = cb_4_Temp_Units.get()
    eci_d[eci]["temp_display_units"] = t_units
    p_units = cb_4_Press_Units.get()
    eci_d[eci]["press_display_units"] = p_units
    print("1782 units are ", p_units, eci_d[eci]["press_display_units"])
    eci_Temp_Press_units_selected(eci)
def eci_5_Temp_units_selected(event):
    eci = "eci_5"
    t_units = cb_5_Temp_Units.get()
    eci_d[eci]["temp_display_units"] = t_units
    p_units = cb_5_Press_Units.get()
    eci_d[eci]["press_display_units"] = p_units
    print("1782 units are ", p_units, eci_d[eci]["press_display_units"])
    eci_Temp_Press_units_selected(eci)
def eci_6_Temp_units_selected(event):
    eci = "eci_6"
    t_units = cb_6_Temp_Units.get()
    eci_d[eci]["temp_display_units"] = t_units
    p_units = cb_6_Press_Units.get()
    eci_d[eci]["press_display_units"] = p_units
    print("1782 units are ", p_units, eci_d[eci]["press_display_units"])
    eci_Temp_Press_units_selected(eci)

def eci_1_Press_units_selected():
    pass
def eci_Temp_Press_units_selected(eci):
     print('1787 Entered eci_units_selected ',(eci))
    #  eci = 'eci_1'
    #  eci_d[eci]['temp_display_qty'] = e_Temp_Qty_1.get()
     print("1870 units changed to liters(g), calculate a new volume.")
     R = 0.082057 # R value for t)hese units
     n = float(eci_d[eci]['M_qty'])   #n is mole_qty
     T = calc_temp(eci)           #float(eci_d[eci]['temp_display_qty'])
     print("1874 n, T, P and V are ", T, type(T))
     P = calc_press(eci)
     V = (n * R * T) / P
     print("1874 n, T, P and V are ", n, T, P, V)
     eci_d[eci]['qty'] = V
     refresh_display(eci)

def calculate_eci_variables():
    print('1871 In process calculate_eci_variables')
    '''
    A step toward calculating variables associated with an eci.
    This one simply gets an element symbol, retrieves the atomic mass,
    and the mole quantity, calculates the quantity in grams, and
    inserts that quantity into the eci quantity entry box.
    '''
    '''msg_Calculate_eci_variables = Label(text=showinfo(title=None, message=None, **options), enter an element type and symbol and a mole quantity.")
    msg_Calculate_eci_variables.config(font=labelfont)
    msg_Calculate_eci_variables.grid(row=8, column=0)
    '''
    ''' What will standard calculation units be? Set them in the eci frame dictionary.
    If a temp or press units or quantity changes, change the value in the eci frame dictionary.
    If there is a mole quantity, assume it is correct and change the regular quantity.
    Implement controlled changes in mole and regular quantities. For example,if a mole quantity
    changes, calculate the regular quantity. If that quantity already exists in the quantity box,
    do not change it. Otherwise change it. Likewise, if the mole quantity is the same, do not change it.
    After each change, the values in the dicionary need to be set. Check the logic, it may be better
    to verify changes in the dictionary values and then change the mole and regular quantities
    rather than delegating the change control to the widgets. Widgets changes update the directory
    and the directory updates the widgets.
    '''
    ''' The following process currently only works for eci_1'''
    #check_entry_changes()
    #print('In process calculate_eci_variables after check_entry_changes')
    #eci_1 = cb_eci_1.get()
    #print('eci_1 is ', eci_1)
    #eci_1_M_qty = e_eci_1_M_qty.get()
    ''' e_eci_1_qty.insert(0, eci_1_M_qty) WORKS!!! '''
    #print('eci_1_M_qty is ', eci_1_M_qty)
    #eci_1_units = cb_eci_1_units.get()
    #print('eci_1_units are ', eci_1_units)

    if eci_1_units == 'liters(l)' or eci_1_units == 'liters(g)' or eci_1_units == 'ml(l)' or eci_1_units == 'ml(g)':
            #and not eci_1_M_qty == 0.0:
        pvnrt(eci, item)

    #else:
    #if eci_1_units == 'grams' and not eci_1_M_qty == "":
    ''' eci_1_mass = DoubleVar() '''
    #eci_1_mass = getdouble(db[eci_1]['mass'])
    #eci_1_mass = db[eci_1]['mass'].get()  #eci_1('mass')   #
    eci_1_M_qty = getdouble(e_eci_1_M_qty.get())
    #print('eci_1_mass = ', getdouble(db[eci_1]['mass']))   #eci_1('mass'))    #eci_1_mass)
    print('eci_1_M_qty = ', getdouble(e_eci_1_M_qty.get()))
    #m_mass = eci_1_M_qty * 26    #getdouble(db[eci_1]['mass'])  #26   #eci_1_mass getdouble(db[eci_1]['mass'])
    #e_eci_1_qty.delete(0, END)
    #e_eci_1_qty.insert(0, m_mass)
    #e_Explanation.insert(END, m_mass)
    #print('m_mass is ', m_mass)

    #if not eci_1_M_qty == "":  ''' Have not yet incorporated temp and press into calculate

    #    eci_1_temp_units = cb_1_Temp_Units.get()
    #    print('eci_1_temp_units are ', eci_1_temp_units)
    #    eci_1_press_units_units = cb_1_Press_Units.get()
    #    print('eci_1_press_units_units are ', eci_1_press_units_units)
        #eci_1_temp_units = cb_1_Temp_Units.get()
        #e_Temp_Qty_1.delete(0, END)
        #e_Temp_Qty_1.insert(0, 288)
        #eci_1_press_units = "ATM"
        #e_Press_Qty_1.delete(0, END)
        #e_Press_Qty_1.insert(0, 0.967)
        # vol_from_prt()    ''' Not yet ready to incorporate gas calculations into calculate process
#pdb.set_trace()
def eci_units_changed(eci, units):
    pass

def qty_mole_change(eci, units): #pvnrt_1
    """ If the quantity is changed, change the mass. The quantity units are passed 
    so the function can determine if the changed quantity is mass or volume,
    and call the correct function"""
    print('2108 qty_mole_change event procedure called.', eci, units)
    t_Explanations.insert(END, "1908 Enter qty_mole_change. \n")
    units = eci_d[eci]['units']  #cb_eci_1_units.get() # current_eci_1_
    # eci_d[eci]['units'] = cb_eci_1_units.get()
    units = eci_d[eci]['units']  #cb_eci_1_units.get() # current_eci_1_
    print("2111 eci_d[eci]['units'] ", units, eci_d[eci]['units'])
    if units == 'grams': #eci_d['eci_1']['units']
        print("2113 eci_d[eci]['units'] == ", eci_d[eci]['units'])
        new_mole_qty = float(eci_d[eci]['qty'])/ eci_d[eci]['mass']
        print("2135 new_mole_qty = ", new_mole_qty)
        eci_d[eci]['M_qty'] = new_mole_qty
        refresh_display(eci)
        print('e_eci_1_M_qty ', new_mole_qty)
    elif units == 'liters(g)': #eci_d['eci_1']['units']
        print("1854 eci_d[eci]['units'] == ", eci_d[eci]['units'])
    if units == "liters(g)":
        print("1970 units changed to liters(g), calculate a new volume.")
        R = 0.082057 # R value for these units
        T = float(calc_temp(eci))           #float(eci_d[eci]['temp_display_qty'])
        P = float(calc_press(eci))
        print("1974 n, T, P and V are ", T, P)
        V = float(eci_d[eci]['qty'])
        n = (P*V)/(R*T)                #float(eci_d[eci]['M_qty'])   #n is mole_qty
        print("2161 n, T, P and V are ", n, T, P, V)
        eci_d[eci]['M_qty'] = n
        refresh_display(eci)


        # new_mole_qty = gas_volume_changes(eci, units)      #float(eci_d[eci]['qty'])/ eci_d[eci]['mass']
        # print("1854 new_mole_qty = ", new_mole_qty)
        # eci_d[eci]['M_qty'] = new_mole_qty
        # refresh_display(eci)
        # print('e_eci_1_M_qty ', new_mole_qty)

def mole_change(eci, units): 
    """ 
    I can't just adjust a value or units, I need to retrieve all the other units and values
    in order to determine what changes to make. For example, to implement PV = nRT,
    the program needs to retrieve all the values and units associated with a change.
    These changes will need to be cascaded due to other programatic changes.
    For example, if the process is 'Synthesis', and the compound changes the number of moles
    of an elemeent, that changes needs to be made. And it needs to progress from moles to
    whatever the correct units are for that element -- e.g. liters of gas. """
    print('2131 mole_change event procedure called.', eci, units)
    t_Explanations.insert(END, "1950 Enter mole_change.", units, "\n")
    # eci_d[eci]['units'] = cb_eci_1_units.get()
    # print("2103 eci_d[eci]['units'] ", eci_d[eci]['units'])
    # dbr['R1']['eci_1_units'] = current_eci_1_units
    current_eci_2_units = cb_eci_2_units.get()
    # dbr['R1']['eci_2_units'] = current_eci_2_units
    current_eci_3_units = cb_eci_3_units.get()
    # dbr['R1']['eci_3_units'] = current_eci_3_units
    print('1968 current_eci_units are ', units)
    if units == 'grams': # eci_d[eci]['units']
        # if item == "M_qty":
        mass = float(eci_d[eci]['mass'])
        print("2162 mass is ", mass)
        new_eci_qty = float(eci_d[eci]['M_qty']) * mass
        print("2164 new_eci_qty = ", new_eci_qty)
        print("2165 eci_d[eci]['M_qty']", eci_d[eci]['M_qty'])
        eci_d[eci]['qty'] = new_eci_qty
        print("2167 new_eci_qty is ", new_eci_qty, eci_d[eci]['qty'])
        t_Explanations.insert(END, "1968 New mass quantity is .", new_eci_qty, "\n")
        refresh_display(eci)
            # refresh_s_1_display()
            # e_eci_1_qty.delete(0, tk.END)
            # e_eci_1_qty.insert(0, new_eci_qty)
        # elif item == "T_qty":
        #     print("1997 T_qty is ", eci_d[eci]['temp_display_qty'], ". Item is ", item)
        # elif item == "T_units":
        #     ''' Units are changed via a combobox selection. '''
        #     print("2000 T_units is ", eci_d[eci]['temp_display_units'], ". Item is ", item)
        # elif item == "P_qty":
        #     print("2002 P_qty is ", eci_d[eci]['press_display_qty'], ". Item is ", item)
        # elif item == "P_units":
        #     ''' Units are changed via a combobox selection. '''
        #     print("2005 P_units is ", eci_d[eci]['press_display_units'], ". Item is ", item)
        # #else: print("Element is ", dbr['R1']['eci_1_formula'], ". Item is ", item)
    elif eci_d[eci]['units'] == 'liters(g)':
        mole_qty = float(eci_d[eci]['M_qty'])
        print("2162 mole_qty is ", mole_qty)
        gas_volume_changes(eci, units)
        t_Explanations.insert(END, "1988 New volume quantity is .", new_eci_qty, "\n")
        refresh_display(eci)
        # gas_volume_changes(eci, units)
        # print("2025 eci_d[eci]['units'] = 'liters(g) = ", eci_d[eci]['units'])
        # print("1995 goto pvnrt(eci, item)") # pvnrt(eci, item)
        
# 2910 gas_volume_change values  0 s_1_units s_1_dict liters(g)
# functions.js:2745 3148 entered calc_temp_qty, temp_display_units s_1_units s_1_dict C
# functions.js:2752 3145 temp_units are  C
# functions.js:4780 4886 convert_C_to_K  273.15
# functions.js:2757 3151 C to K  0 273.15
# functions.js:2779 3216 entered calc_press_qty, press_display_units s_1_units s_1_dict atm
# #pdb.set_trace()
def gas_volume_changes(eci, units):
    """ The eci is the dictionary to check. The item is what changed and
    triggered the function to be called."""
    print("1916 gas_volume_changes(eci, units)", eci, units)
    t_Explanations.insert(END, "2005 gas_volume_changes", units, "\n")
    eci_d[eci]['units'] = units
    if units == "liters(g)":
        print("2058 units changed to liters(g), calculate a new volume.")
        R = 0.082057 # R value for these units
        n = float(eci_d[eci]['M_qty'])
        T = calc_temp(eci)
        P = calc_press(eci)
        V = (n * R * T) / P
        print("2067 n, T, P and V are ", n, T, P, V)
        eci_d[eci]['qty'] = V
        refresh_display(eci)

def calc_temp(eci):
    """ convert K to K and return it."""
    print("2080 Entering calc_temp")
    qty = float(eci_d[eci]['temp_display_qty'])
    units = eci_d[eci]['temp_display_units']
    print("2083 qty and units are ", qty, units, type(qty), type(units))
    if units == 'K':
        return qty
    elif units == 'C':
        return qty + 273.15
    elif units == 'F':
        # T = (5/9) * float(e_Temp_Qty_1.get()) + 32 + 273.15
        return (5/9 * qty) + 273.15
def calc_press(eci):
    """ Use eci to get temp qty and units, convert to degrees K and return"""
    qty = float(eci_d[eci]['press_display_qty'])
    units = eci_d[eci]['press_display_units']
    if units == 'atm':
        return qty
    elif units == 'torr':
        return qty * 760
    elif units == 'psi':
        return  14.7 * qty
    elif units == 'mmhg':
        return qty * 760
    elif units == 'Pa':
        return qty / 101325 #* 9.8692e-6
    elif units == 'kPa':
        return qty / 101.325

def pvnrt(eci, item):
    print('1986 In process pvnrt ', eci, item)
    ''' Calculate volume given pressure, R constant, and temperature. pv = nRt'''
    R = 0.082057 # R value for these units
    if eci == eci_1.get():
        print('In pvnrt if eci == eci_1:')
        V = float(eci_1_qty.get())
        n = float(eci_1_M_qty.get())
        if eci_1_temp_units.get() == 'C':
            T = 273.15 + float(e_Temp_Qty_1.get())  #C_to_K(float(e_Temp_Qty_1.get())) got TypeError: unsupported operand type(s) for *: 'float' and 'NoneType'
            eci_d[eci]['temp_calc_qty'] = T
        elif eci_1_temp_units.get() == 'K':
            T = float(e_Temp_Qty_1.get())
            eci_d[eci]['temp_calc_qty'] = T
        elif eci_1_temp_units.get() == 'F':
            T = (5/9) * float(e_Temp_Qty_1.get()) + 32 + 273.15
            eci_d[eci]['temp_calc_qty'] = T
        if eci_1_press_units.get() == 'atm':
            P = float(e_Press_Qty_1.get())
            eci_d[eci]['temp_press_qty'] = P
        elif eci_1_press_units.get() == 'torr' or eci_1_press_units.get() == 'mmHg':
            P = float(e_Temp_Qty_1.get()) * 760
            eci_d[eci]['temp_press_qty'] = P
        print('2008 n = ', n,'T = ', T,'P = ', P, 'V = ',V)
        if item == 'M_qty':
            print("2010 in if item == 'M_qty':")
            n = float(eci_1_M_qty.get())    # getdouble
            try:
                V = n*R*T/P
                eci_d[eci]['qty'] = V
                e_eci_1_qty.delete(0, 'end')
                e_eci_1_qty.insert(0, V)
                print(n, T, P, V)
            except: print('Error in vol = n*R*T/P item == M_qty')
        elif item == 'qty':
            print("2019 in if item == 'qty':")
            V = float(eci_1_qty.get())
            try:
                n = (P*V)/(R*T)
                e_eci_1_M_qty.delete(0, tk.END)
                e_eci_1_M_qty.insert(0, n)
                print('2025 n is ', n, ' V is  ', V)
            except: print('Error in vol = n*R*T/P item == qty')
    elif eci == eci_2.get():
        V = float(eci_2_qty.get())
        n = float(eci_2_M_qty.get())
        if eci_2_temp_units.get() == 'C':
            T = 273.15 + float(e_Temp_Qty_2.get())  #C_to_K(float(e_Temp_Qty_1.get())) got TypeError: unsupported operand type(s) for *: 'float' and 'NoneType'
            # dbr['R1']['eci_2_temp_calc_qty'] = T
        elif eci_2_temp_units.get() == 'K':
            T = float(e_Temp_Qty_2.get())
            # dbr['R1']['eci_2_temp_calc_qty'] = T
        elif eci_2_temp_units.get() == 'F':
            T = (5/9) * float(e_Temp_Qty_2.get()) + 32 + 273.15
            # dbr['R1']['eci_2_temp_calc_qty'] = T
        if eci_2_press_units.get() == 'atm':
            P = float(e_Press_Qty_2.get())
            dbr['R1']['eci_2_press_display_qty'] = P
        elif eci_2_press_units.get() == 'torr' or eci_2_press_units.get() == 'mmHg':
            P = float(e_Temp_Qty_2.get()) * 760
            dbr['R1']['eci_2_press_display_qty'] = P
        print('2045 n = ', n,'T = ', T,'P = ', P, 'V = ',V)
        if item == 'M_qty':
            print("2047 in if item == 'M_qty':")
            n = float(eci_2_M_qty.get())    # getdouble
            try:
                V = n*R*T/P
                e_eci_2_qty.delete(0, 'end')
                e_eci_2_qty.insert(0, V)
                print(n, T, P, V)
            except: print('Error in vol = n*R*T/P item == M_qty')
        elif item == 'qty':
            print("2056 in if item == 'qty':")
            V = float(eci_2_qty.get())
            try:
                n = (P*V)/(R*T)
                e_eci_2_M_qty.delete(0, tk.END)
                e_eci_2_M_qty.insert(0, n)
                print('2026 n is ', n, ' V is  ', V)
            except: print('Error in vol = n*R*T/P item == qty')
    elif eci == eci_3.get():
        V = float(eci_3_qty.get())
        n = float(eci_3_M_qty.get())

    #temp = 0.0


def eci_1_qty_adjusted(value): # e_eci_lk_1_qty_adjusted
    print('2030 eci_1_qty_adjusted event procedure called.')
    t_Explanations.insert(END, "Adjust substance 1 quantity. \n")
    eci = 'eci_1'
    eci_1_qty = e_eci_1_qty.get()
    eci_d[eci]['qty'] = eci_1_qty
    units = cb_eci_1_units.get() # current_eci_1_
    eci_d[eci]['units'] = cb_eci_1_units.get()
    qty_mole_change(eci, units) 
def eci_2_qty_adjusted(value): # e_eci_lk_1_qty_adjusted
    print('2030 eci_2_qty_adjusted event procedure called.')
    t_Explanations.insert(END, "Adjust substance 2 quantity. \n")
    eci = 'eci_2'
    eci_2_qty = e_eci_2_qty.get()
    eci_d[eci]['qty'] = eci_2_qty
    units = cb_eci_2_units.get() # current_eci_1_
    eci_d[eci]['units'] = cb_eci_2_units.get()
    qty_mole_change(eci, units) 
def eci_3_qty_adjusted(value): # e_eci_lk_1_qty_adjusted
    print('2030 eci_3_qty_adjusted event procedure called.')
    t_Explanations.insert(END, "Adjust substance 3 quantity. \n")
    eci = 'eci_3'
    eci_3_qty = e_eci_3_qty.get()
    eci_d[eci]['qty'] = eci_3_qty
    units = cb_eci_3_units.get() # current_eci_1_
    eci_d[eci]['units'] = cb_eci_3_units.get()
    qty_mole_change(eci, units) 
def eci_4_qty_adjusted(value): # e_eci_lk_1_qty_adjusted
    print('2030 eci_4_qty_adjusted event procedure called.')
    t_Explanations.insert(END, "Adjust substance 4 quantity. \n")
    eci = 'eci_4'
    eci_4_qty = e_eci_4_qty.get()
    eci_d[eci]['qty'] = eci_4_qty
    units = cb_eci_4_units.get() # current_eci_1_
    eci_d[eci]['units'] = cb_eci_4_units.get()
    qty_mole_change(eci, units) 
def eci_5_qty_adjusted(value): # e_eci_lk_1_qty_adjusted
    print('2030 eci_5_qty_adjusted event procedure called.')
    t_Explanations.insert(END, "Adjust substance 5 quantity. \n")
    eci = 'eci_5'
    eci_5_qty = e_eci_5_qty.get()
    eci_d[eci]['qty'] = eci_5_qty
    units = cb_eci_1_units.get() # current_eci_1_
    eci_d[eci]['units'] = cb_eci_5_units.get()
    qty_mole_change(eci, units) 
def eci_6_qty_adjusted(value): # e_eci_lk_1_qty_adjusted
    print('2030 eci_6_qty_adjusted event procedure called.')
    t_Explanations.insert(END, "Adjust substance 6 quantity. \n")
    eci = 'eci_6'
    eci_6_qty = e_eci_6_qty.get()
    eci_d[eci]['qty'] = eci_6_qty
    units = cb_eci_6_units.get() # current_eci_1_
    eci_d[eci]['units'] = cb_eci_6_units.get()
    qty_mole_change(eci, units) 

def eci_1_M_qty_adjusted(value):
    print('2277 eci_1_M_qty_adjusted procedure called.') # value is
    t_Explanations.insert(END, "Adjust substance 1 mole quantity. \n")
    eci = 'eci_1'
    units = cb_eci_1_units.get()
    eci_d[eci]['M_qty'] = e_eci_1_M_qty.get()
    mole_change(eci, units) 
def eci_2_M_qty_adjusted(value):
    print('2277 eci_2_M_qty_adjusted procedure called.') # value is
    t_Explanations.insert(END, "Adjust substance 2 mole quantity. \n")
    eci = 'eci_2'
    units = cb_eci_2_units.get()
    eci_d[eci]['M_qty'] = e_eci_2_M_qty.get()
    mole_change(eci, units) 
def eci_3_M_qty_adjusted(value):
    print('2277 eci_13M_qty_adjusted procedure called.') # value is
    t_Explanations.insert(END, "Adjust substance 3 mole quantity. \n")
    eci = 'eci_3'
    units = cb_eci_3_units.get()
    eci_d[eci]['M_qty'] = e_eci_3_M_qty.get()
    mole_change(eci, units) 
def eci_4_M_qty_adjusted(value):
    print('2277 eci_4_M_qty_adjusted procedure called.') # value is
    t_Explanations.insert(END, "Adjust substance 4 mole quantity. \n")
    eci = 'eci_4'
    units = cb_eci_4_units.get()
    eci_d[eci]['M_qty'] = e_eci_4_M_qty.get()
    mole_change(eci, units) 
def eci_5_M_qty_adjusted(value):
    print('2277 eci_5_M_qty_adjusted procedure called.') # value is
    t_Explanations.insert(END, "Adjust substance 5 mole quantity. \n")
    eci = 'eci_5'
    units = cb_eci_5_units.get()
    eci_d[eci]['M_qty'] = e_eci_5_M_qty.get()
    mole_change(eci, units) 
def eci_6_M_qty_adjusted(value):
    print('2277 eci_6_M_qty_adjusted procedure called.') # value is
    t_Explanations.insert(END, "Adjust substance 6 mole quantity. \n")
    eci = 'eci_6'
    units = cb_eci_6_units.get()
    eci_d[eci]['M_qty'] = e_eci_6_M_qty.get()
    mole_change(eci, units) 


def e_eci_kl_1_qty_adjusted(value): # eci_kl_1_units_selected
    print('2315 e_eci_lk_1_qty_adjusted event procedure called.')
    eci = 'eci_1'
    e_eci_kl_1_qty = e_eci_kl_1_qty.get()
    eci_d[eci]['kl_qty'] = e_eci_kl_1_qty
    kl_1_units = cb_kl_1_units.get() # current_eci_1_
    eci_d[eci]['units'] = cb_eci_1_units.get()
    print("2036 eci_1_qty is ", eci_1_qty)
    # qty_mole_change(eci, 'qty', kl_1_units) 


def e_eci_kl_2_qty_adjusted(value):
    print('2315 e_eci_lk_2_qty_adjusted event procedure called.')
    eci = 'eci_2'
    e_eci_kl_2_qty = e_eci_kl_2_qty.get()
    eci_d[eci]['kl_qty'] = e_eci_kl_2_qty
    kl_2_units = cb_kl_2_units.get() # current_eci_1_
    eci_d[eci]['units'] = cb_eci_2_units.get()
    print("2036 eci_2_qty is ", eci_2_qty)

def e_eci_kl_3_qty_adjusted(value):
    print('2315 e_eci_lk_3_qty_adjusted event procedure called.')
    eci = 'eci_3'
    e_eci_kl_3_qty = e_eci_kl_3_qty.get()
    eci_d[eci]['kl_qty'] = e_eci_kl_3_qty
    kl_3_units = cb_kl_3_units.get() # current_eci_1_
    eci_d[eci]['units'] = cb_eci_3_units.get()
    print("2036 eci_3_qty is ", eci_3_qty)

def e_eci_kl_4_qty_adjusted(value):
    print('2315 e_eci_lk_4_qty_adjusted event procedure called.')
    eci = 'eci_4'
    e_eci_kl_4_qty = e_eci_kl_4_qty.get()
    eci_d[eci]['kl_qty'] = e_eci_kl_4_qty
    kl_4_units = cb_kl_4_units.get() # current_eci_1_
    eci_d[eci]['units'] = cb_eci_4_units.get()
    print("2036 eci_4_qty is ", eci_4_qty)

def e_eci_kl_5_qty_adjusted(value):
    print('2315 e_eci_lk_5_qty_adjusted event procedure called.')
    eci = 'eci_5'
    e_eci_kl_5_qty = e_eci_kl_5_qty.get()
    eci_d[eci]['kl_qty'] = e_eci_kl_5_qty
    kl_5_units = cb_kl_5_units.get() 
    eci_d[eci]['units'] = cb_eci_5_units.get()
    print("2036 eci_5_qty is ", eci_5_qty)

def e_eci_kl_6_qty_adjusted(value):
    print('2315 e_eci_lk_6_qty_adjusted event procedure called.')
    eci = 'eci_6'
    e_eci_kl_6_qty = e_eci_kl_6_qty.get()
    eci_d[eci]['kl_qty'] = e_eci_kl_6_qty
    kl_6_units = cb_kl_6_units.get() 
    eci_d[eci]['units'] = cb_eci_6_units.get()
    print("2036 eci_6_qty is ", eci_6_qty)

def cb_kl_1_units_selected(value): # eci_kl_1_units_selected
    print('2228 cb_kl_1_units_selected event procedure called.')
def cb_kl_2_units_selected(value): # eci_kl_1_units_selected
    print('2228 cb_kl_2_units_selected event procedure called.')
def cb_kl_3_units_selected(value): # eci_kl_1_units_selected
    print('2228 cb_kl_3_units_selected event procedure called.')
def cb_kl_4_units_selected(value): # eci_kl_1_units_selected
    print('2228 cb_kl_4_units_selected event procedure called.')
def cb_kl_5_units_selected(value): # eci_kl_1_units_selected
    print('2228 cb_kl_5_units_selected event procedure called.')
def cb_kl_6_units_selected(value): # eci_kl_1_units_selected
    print('2228 cb_kl_6_units_selected event procedure called.')


def e_eci_MM_1_qty_adjusted(value): # eci_kl_1_units_selected
    print('2228 e_eci_MM_1_qty_adjusted event procedure called.')
def e_eci_MM_2_qty_adjusted(value): # eci_kl_1_units_selected
    print('2228 e_eci_MM_2_qty_adjusted event procedure called.')
def e_eci_MM_3_qty_adjusted(value): # eci_kl_1_units_selected
    print('2228 e_eci_MM_3_qty_adjusted event procedure called.')
def e_eci_MM_4_qty_adjusted(value): # eci_kl_1_units_selected
    print('2228 e_eci_MM_4_qty_adjusted event procedure called.')
def e_eci_MM_5_qty_adjusted(value): # eci_kl_1_units_selected
    print('2228 e_eci_MM_5_qty_adjusted event procedure called.')
def e_eci_MM_6_qty_adjusted(value): # eci_kl_1_units_selected
    print('2228 e_eci_MM_6_qty_adjusted event procedure called.')

def eci_1_Temp_qty_adjusted(value):
    print('2080 eci_1_Temp_qty_adjusted event procedure called.')
    eci = 'eci_1'
    units = cb_eci_1_units.get()
    t_units = cb_1_Temp_Units.get()
    qty = e_Temp_Qty_1.get()
    eci_d[eci]['temp_display_units'] = t_units
    eci_d[eci]['temp_display_qty'] = qty
    print("2295 ",eci, t_units, qty)

    # cb_1_Temp_Units.get()
    """ The eci is the dictionary to check. The item is what changed and
    triggered the function to be called."""
    # print("1916 gas_volume_changes(eci, units)", eci, units)
    # t_Explanations.insert(END, "2005 gas_volume_changes", units, "\n")
    # eci_d[eci]['units'] = units
    if units == "liters(g)":
        gas_volume_changes(eci, units)
        refresh_display(eci)
        # print("2312 units changed to liters(g), calculate a new volume.")
        # R = 0.082057 # R value for these units
        # n = float(eci_d[eci]['M_qty'])   #n is mole_qty
        # T = calc_temp(eci)           #float(eci_d[eci]['temp_display_qty'])
        # P = calc_press(eci)
        # V = (n * R * T) / P
        # print("2161 n, T, P and V are ", n, T, P, V)
        # eci_d[eci]['qty'] = V
        
def eci_2_Temp_qty_adjusted(value):
    print('2080 eci_2_Temp_qty_adjusted event procedure called.')
    # mole_change(dbr['R1']['eci_1_formula'], 'T_qty')
def eci_3_Temp_qty_adjusted(value):
    print('2080 eci_3_Temp_qty_adjusted event procedure called.')
    # mole_change(dbr['R1']['eci_1_formula'], 'T_qty')
def eci_4_Temp_qty_adjusted(value):
    print('2080 eci_4_Temp_qty_adjusted event procedure called.')
    # mole_change(dbr['R1']['eci_1_formula'], 'T_qty')
def eci_5_Temp_qty_adjusted(value):
    print('2080 eci_5_Temp_qty_adjusted event procedure called.')
    # mole_change(dbr['R1']['eci_1_formula'], 'T_qty')
def eci_6_Temp_qty_adjusted(value):
    print('2080 eci_6_Temp_qty_adjusted event procedure called.')
    # mole_change(dbr['R1']['eci_1_formula'], 'T_qty')

def cb_MM_1_units_selected(value):
    pass
def cb_MM_2_units_selected(value):
    pass
def cb_MM_3_units_selected(value):
    pass
def cb_MM_4_units_selected(value):
    pass
def cb_MM_5_units_selected(value):
    pass
def cb_MM_6_units_selected(value):
    pass
def eci_1_Temp_units_adjusted(value):
    print('2084 eci_1_Temp_units_adjusted event procedure called.')
def eci_2_Temp_units_adjusted(value):
    print('2084 eci_2_Temp_units_adjusted event procedure called.')
def eci_3_Temp_units_adjusted(value):
    print('2084 eci_3_Temp_units_adjusted event procedure called.')
def eci_4_Temp_units_adjusted(value):
    print('2084 eci_4_Temp_units_adjusted event procedure called.')
def eci_5_Temp_units_adjusted(value):
    print('2084 eci_5_Temp_units_adjusted event procedure called.')
def eci_6_Temp_units_adjusted(value):
    print('2084 eci_6_Temp_units_adjusted event procedure called.')
    # mole_change(dbr['R1']['eci_1_formula'], 'T_units')

def eci_1_Press_qty_adjusted(value):
    print('2089 eci_1_Press_qty_adjusted event procedure called.')
def eci_2_Press_qty_adjusted(value):
    print('2089 eci_2_Press_qty_adjusted event procedure called.')
def eci_3_Press_qty_adjusted(value):
    print('2089 eci_3_Press_qty_adjusted event procedure called.')
def eci_4_Press_qty_adjusted(value):
    print('2089 eci_4_Press_qty_adjusted event procedure called.')
def eci_5_Press_qty_adjusted(value):
    print('2089 eci_5_Press_qty_adjusted event procedure called.')
def eci_6_Press_qty_adjusted(value):
    print('2089 eci_6_Press_qty_adjusted event procedure called.')

def eci_1_Press_units_adjusted(value):
    print('2092 eci_1_Press_units_adjusted event procedure called.')
def eci_2_Press_units_adjusted(value):
    print('2092 eci_2_Press_units_adjusted event procedure called.')
def eci_3_Press_units_adjusted(value):
    print('2092 eci_3_Press_units_adjusted event procedure called.')
def eci_4_Press_units_adjusted(value):
    print('2092 eci_4_Press_units_adjusted event procedure called.')
def eci_5_Press_units_adjusted(value):
    print('2092 eci_5_Press_units_adjusted event procedure called.')
def eci_6_Press_units_adjusted(value):
    print('2092 eci_6_Press_units_adjusted event procedure called.')


# def eci_2_qty_adjusted(value):
#     print('2030 eci_2_qty_adjusted event procedure called.')
#     eci = 'eci_2'
#     eci_2_qty = e_eci_2_qty.get()
#     eci_d[eci]['qty'] = eci_2_qty
#     units = cb_eci_2_units.get() # current_eci_1_
#     eci_d[eci]['units'] = cb_eci_2_units.get()
#     print("2036 eci_2_qty is ", eci_2_qty)
#     qty_mole_change(eci, units) 

# def eci_2_M_qty_adjusted(value):
#     print('2275 eci_2_M_qty_adjusted procedure called.') # value is
#     units = cb_eci_2_units.get()
#     eci_2_sub = eci_d['eci_2']['formula']
#     eci_d['eci_2']['M_qty'] = e_eci_2_M_qty.get()
#     print("2272 units and mass are ", units, eci_2_sub, eci_d['eci_2']['M_qty'])
#     mole_change('eci_2', units) 








# def xeci_2_qty_adjusted(value):
#     print('2001 eci_2_qty_adjusted event procedure called.', value)
#     print('e_eci_2_qty is ', e_eci_2_qty.get())
#     current_eci_2_units = dbr['R1']['eci_2_units']
#     print('current_eci_2_units is ', current_eci_2_units)
#     if dbr['R1']['eci_2_units'] == 'grams':
#         ''' I can't just adjust the eci_1_qty, I need to determine what it should be based on units.
#         Since units are in grams, I need to retrieve the element atomic mass and use it for calculations.'''
#         print("1750 dbr['R1']['eci_2_units'] == ", dbr['R1']['eci_2_units'])
#         dbr['R1']['eci_2_qty'] = db[eci_2.get()]['mass']
#         new_mole_qty = eci_2_qty.get()/dbr['R1']['eci_2_qty']
#         e_eci_2_M_qty.delete(0, tk.END)
#         e_eci_2_M_qty.insert(0, new_mole_qty)

# def xeci_2_M_qty_adjusted(value):
#     print('eci_2_M_qty_adjusted event procedure called.', value)
#     print('eci_2_M_qty is ', eci_2_M_qty.get())
#     current_eci_2_units = dbr['R1']['eci_2_units']
#     print('current_eci_2_units is ', current_eci_2_units)
#     if dbr['R1']['eci_2_units'] == 'grams':
#         print("1750 dbr['R1']['eci_2_units'] == ", dbr['R1']['eci_2_units'])
#         ''' Reset the record quantity to the element atomic mass before doing calculations. '''
#         dbr['R1']['eci_2_qty'] = db[eci_2.get()]['mass']
#         ''' current_eci_2_qty may be mass in grams or some other quantity of the current units.'''
#         current_eci_2_qty = dbr['R1']['eci_2_qty']
#         print('current_eci_2_qty is ', current_eci_2_qty)
#         new_eci_2_qty = eci_2_M_qty.get() * current_eci_2_qty
#         e_eci_2_qty.delete(0, tk.END)
#         e_eci_2_qty.insert(0, new_eci_2_qty)

def Fill_Product_Comboboxes():
    print('2473 Entered Fill_Product_Comboboxes')
    cb_4_type = "compounds"
    cb_Select_CB4.set(cb_4_type)
    cnd_set = set(compounds_names_dict.values())
    '''{'C5H12', 'HNO3', 'KOH', 'N2O5', 'Al4C3','SO3', 'Na2SO4', 'C6H8O7',
     'NH3', 'C9H20', 'HBr', 'HCl', 'HNO2', 'KBr', 'LiCl', 'C3H8', 'C6H14', 
     'HF', 'C8H18', 'CO', 'HC2H3O2', 'H2SO3', 'C18H38', 'CaI', 'CO2', 'H3PO4', 
     'CaH2PO4', 'N2H4', 'N2O', 'C7H16', 'CaOH2', 'AlCl3', 'C4H10', 'NO', 'H2SO4', 
     'Ca3P2', 'C2H6', 'HCN', 'Mg3N2', 'NaCl', 'NaOH', 'HI', 'CdS', 'NaHCO3', 
     'CH4', 'BCl3', 'C4H10_M', 'C10H22', 'Na2O', 'CsF', 'HClO4', 'H2S', 'NO2', 
     'N2O4', 'H2CO3', 'Ar2He2Kr2Ne2Xe2Rn2', 'C14H30', 'PF5', 'SO2', 'IF7'}'''
    # iterate throught cnd_set items dictionary above
    # if the alpha_list == the compound dictionary elements string
    # AlCl3 = dict(formula= 'AlCl3', elements= 'AlCl',name= 'aluminum_chloride')
    # Thus, if the set item is AlCl3, and the alpha_list is AlCl
    # When the loop gets to AlCl3, alpha_list = AlCl will equal AlCl3(elements) = AlCl
    # if the above conditions are satisfied, create two new strings:
    # one to set the values of cb_4 formula values and one to set the cd_4 names values.
    #for c in cnd_set:
    #    print(c, c.elements)
    print(cnd_set)
    print("cb_4_type is ", cb_Select_CB4.get())
    print('Exited Fill_Product_Comboboxes')

def Oxidation_Reduction():
    """This function has been entered after elements have been selected and the Continue button pressed."""
    e_Explanation.insert(END, "Oxidation_Reduction process entered\n")
    print('2086 Entering Oxidation_Reduction() ')
    Oxidation_Rate()
    cb_1_type = cb_Select_CB1.get()  # Get the selected type of: element, compound, or ion
    print('eci_1_type = ', cb_1_type)
    eci_1 = cb_eci_1.get()
    print('eci_1 = ', eci_1)
    if cb_1_type == 'elements':
        '''  *** The following works! '''

        # eci_db['eci_1']['name']
        eci_d['eci_1']['name'] = db[eci_1]['name']
        # eci_db[eci_1]['name'] = db[eci_1]['name']
        print("eci_db['eci_1']['name'] is ", eci_d['eci_1']['name'])
        eci_1_name = db[eci_1]['name']
        print("eci_1_name is ", eci_1_name)   #db[eci_1]['name']
        print("db[eci_1]['name'] is ", db[eci_1]['name'])
        eci_1_col = db[eci_1]['column']
        eci_1_mass = db[eci_1]['mass']
        eci_1_valence = db[eci_1]['valence']
        eci_d['eci_1']['column'] = db[eci_1]['column']
        eci_d['eci_1']['mass'] = db[eci_1]['mass']
        eci_d['eci_1']['valence'] = db[eci_1]['valence']
        print("eci_db['eci_1']['column'] is ", eci_d['eci_1']['column'])
        print("eci_db['eci_1']['mass'] is ", eci_d['eci_1']['mass'])
        print("eci_db['eci_1']['valence'] is ", eci_d['eci_1']['valence'])
        # print("db[eci_1]['name'] is ", eci_1_name)
        # print("db[eci_1]['column'] is ", eci_1_col)
        # print("db[eci_1]['mass'] is ", eci_1_mass)
        # print("db[eci_1]['valence'] is ", eci_1_valence)
        # print(eci_1_valence)   # Prints out the variable #str(eci_1).affinity
    elif cb_1_type == 'compounds':
        # eci_1 = cb_eci_1.get()
        # print('eci_1 = ', eci_1)
        e_Explanation.insert(END, "Oxidation_Reduction process entered\n")
        print("Oxidation_Reduction eci_1 can't process compounds yet")
    elif cb_1_type == 'ions':
        # eci_1 = cb_eci_1.get()
        # print('eci_1 = ', eci_1)
        e_Explanation.insert(END, "Error in Oxidation_Reduction eci_1 can't process compounds yet")
    else:
        print("Oxidation_Reduction process eci_1 else clause")
    cb_2_type = cb_Select_CB2.get()  # Get the selected type of: element, compound, or ion
    print('eci_2_type = ', cb_2_type)
    if cb_2_type == 'elements':
        eci_2 = cb_eci_2.get()
        print('eci_2 = ', eci_2)
        '''  *** The following works! '''
        eci_2_name = db[eci_2]['name']
        eci_2_col = db[eci_2]['column']
        eci_2_mass = db[eci_2]['mass']
        eci_2_valence = db[eci_2]['valence']
        print("db[eci_2]['name'] is ", eci_2_name)
        print("db[eci_2]['column'] is ", eci_2_col)
        print("db[eci_2]['mass'] is ", eci_2_mass)
        print("db[eci_2]['valence'] is ", eci_2_valence)
        # print(eci_1_valence)   # Prints out the variable #str(eci_1).affinity
    elif cb_2_type == 'compounds':
        # eci_2 = cb_eci_2.get()
        # print('eci_2 = ', eci_2)
        print("Error in Oxidation_Reduction eci_2 can't process compounds yet")
    elif cb_2_type == 'ions':
        # eci_2 = cb_eci_2.get()
        # print('eci_2 = ', eci_2)
        print("Error in Oxidation_Reduction eci_2 can't process ions yet")
    else:
        print("Error in Oxidation_Reduction process eci_2 else clause")
    cb_3_type = cb_Select_CB3.get()  # Get the selected type of: element, compound, or ion
    print('eci_3_type = ', cb_3_type)
    eci_3 = cb_eci_3.get()
    print('eci_3 = ', eci_3)
    if cb_3_type == 'elements':
        # eci_3 = cb_eci_3.get()
        # print('eci_3 = ', eci_3)
        '''  *** The following works! '''
        eci_3_name = db[eci_3]['name']
        eci_3_col = db[eci_3]['column']
        eci_3_mass = db[eci_3]['mass']
        eci_3_valence = db[eci_3]['valence']
        print("db[eci_3]['name'] is ", eci_3_name)
        print("db[eci_3]['column'] is ", eci_3_col)
        print("db[eci_3]['mass'] is ", eci_3_mass)
        print("db[eci_3]['valence'] is ", eci_3_valence)
        # print(eci_1_valence)   # Prints out the variable #str(eci_1).affinity
    elif cb_3_type == 'compounds':
        # eci_3 = cb_eci_3.get()
        # print('eci_3 = ', eci_3)
        print("Error in Oxidation_Reduction eci_3 can't process compounds yet")
    elif cb_3_type == 'ions':
        # eci_3 = cb_eci_3.get()
        # print('eci_3 = ', eci_3)
        print("Error in Oxidation_Reduction eci_3 can't process ions yet")
    elif cb_3_type == "":
        pass
    else:
        e_Explanation.insert(END, "Error in Oxidation_Reduction process eci_3 else clause\n")

    # if cb_eci_1.get() == 'elements':
    #    eci_1 = cb_eci_1.get()
    #    print('eci_1 = ', eci_1)
    #    print('eci_1_type = ', cb_eci_1.get())


def Precipitation():
    print('2189 Entered Precipitation')
    """ print("Pressed update_record button") """
    e_Explanation.insert(END, "Precipitation process entered\n")
    # print("Precipitation process entered")


def Oxidation_Rate():   #Based on eci type, call appropriate Oxidation_Rate function
    print('2196 Entering Oxidation_Rate() ')

    cb_1_type = cb_Select_CB1.get()
    cb_2_type = cb_Select_CB2.get()
    cb_3_type = cb_Select_CB3.get()
    if cb_1_type == 'elements' and cb_2_type == 'elements' and cb_3_type == 'elements' or cb_3_type == "":
        Oxidation_Rate_Elements()
    elif cb_1_type == 'compounds' or cb_2_type == 'compounds' and cb_3_type == 'compounds':
        Oxidation_Rate_Compounds()
    elif cb_1_type == 'ions' or cb_2_type == 'ions' and cb_3_type == 'ions':
        Oxidation_Rate_Ions()
    else:
        e_Explanation.insert(END, "Oxidation_Rate process fell through to else clause\n")


''' Oxidation_Rate_Compounds and Oxidation_Rate_Ions are placeholders for future use as needed. '''


def Oxidation_Rate_Compounds():
    e_Explanation.insert(END, "Entered Oxidation_Rate_Compounds process\n")


def Oxidation_Rate_Ions():
    e_Explanation.insert(END, "Entered Oxidation_Rate_Ions process\n")

def set_eci_d_balance_variables():
    ''' The following demonstrate the direct assignments of frame values
    from the element dictionary. '''
    print('In set_eci_d_balance_variables()')

    eci_d['eci_1']['eci'] = cb_eci_1.get()
    eci_d['eci_2']['eci'] = cb_eci_2.get()
    eci_d['eci_3']['eci'] = cb_eci_3.get()
    print("eci_d['eci_1']['eci'] is ", eci_d['eci_1']['eci'])
    print("eci_d['eci_2']['eci'] is ", eci_d['eci_2']['eci'])
    print("eci_d['eci_3']['eci'] is ", eci_d['eci_3']['eci'])
    eci_d['eci_1']['eci_type'] = cb_Select_CB1.get()
    eci_d['eci_2']['eci_type'] = cb_Select_CB2.get()
    eci_d['eci_3']['eci_type'] = cb_Select_CB3.get()
    print("eci_d['eci_1']['eci_type'] is ", eci_d['eci_1']['eci_type'])
    print("eci_d['eci_2']['eci_type'] is ", eci_d['eci_2']['eci_type'])
    print("eci_d['eci_3']['eci_type'] is ", eci_d['eci_3']['eci_type'])

def Oxidation_Rate_Elements():
    ''' This function has been entered after elements have been selected and the Continue button pressed. Each item is an element. Compounds and ions use a different function.
    It is necessary to get the valence and electronegativity values because the valence of some
    elements is determined by the relative electronegativity of the other elements.'''
    cb_eci_1_units.set('grams')
    cb_eci_2_units.set('grams')
    cb_eci_4_units.set('grams')

    e_Explanation.insert(END, "Oxidation_Rate_Elements process entered\n")
    print(' Entering Oxidation_Rate_Elements() ')

    ''' The following has already been done in the Oxidation_Rate() function
    cb_1_type = cb_Select_CB1.get()
    cb_2_type = cb_Select_CB2.get()
    cb_3_type = cb_Select_CB3.get()
    '''
    eci_1 = cb_eci_1.get()
    eci_2 = cb_eci_2.get()
    eci_3 = cb_eci_3.get()
    ''' Set the values in the eci frame dictionary. '''
    # eci_1_temp_units = cb_1_Temp_Units.get() # Move to after balance process
    set_eci_d_balance_variables()

    ''' if eci_db['eci_1']['eci_type'] == 'elements': is no longer needed
    because all non-elements have been moved to another function. '''
    ''' These lines get values of the element from the element dictionary. '''
    eci_1_name = db[eci_1]['name']
    eci_1_mass = db[eci_1]['mass']
    eci_1_group = db[eci_1]['_group']
    eci_1_valence = db[eci_1]['valence']
    eci_1_electronegativity = db[eci_1]['electronegativity']
    eci_1_qty = eci_1_mass
    print('e_eci_1_qty is at line 1638', eci_1_qty)
    print("db[eci_1]['name'] is ", eci_1_name)
    print("db[eci_1]['mass'] is ", eci_1_mass)
    print("db[eci_1]['_group'] is ", eci_1_group)
    print("db[eci_1]['valence'] is ", eci_1_valence)
    print("db[eci_1]['electronegativity'] is ", eci_1_electronegativity)
    ''' if eci_db['eci_2']['eci_type'] == 'elements':  in no longer needed. '''
    eci_2_name = db[eci_2]['name']
    eci_2_mass = db[eci_2]['mass']
    eci_2_group = db[eci_2]['_group']
    eci_2_valence = db[eci_2]['valence']
    eci_2_electronegativity = db[eci_2]['electronegativity']
    print("db[eci_2]['name'] is ", eci_2_name)
    print("db[eci_2]['_group'] is ", eci_2_group)
    print("db[eci_2]['valence'] is ", eci_2_valence)
    print("db[eci_2]['electronegativity'] is ", eci_2_electronegativity)
    if eci_d['eci_3']['eci_type'] == 'elements':
        eci_3_name = db[eci_3]['name']
        eci_3_group = db[eci_3]['_group']
        eci_3_valence = db[eci_3]['valence']
        eci_3_electronegativity = db[eci_3]['electronegativity']
        print("db[eci_3]['name'] is ", eci_3_name)
        print("db[eci_3]['_group'] is ", eci_3_group)
        print("db[eci_3]['valence'] is ", eci_3_valence)
        print("db[eci_3]['electronegativity'] is ", eci_3_electronegativity)
        print("In Oxidation_Rate_Elements. Function does not yet work for 3 elements.")
    if eci_1_valence.isnumeric():
        ''' This process only works for metals that have single valence values. '''
        ''' Set the dictionary values. Valence may have multiple values. In these cases, it has only one value.
        Oxidation_State only has one value that is set for this case. '''
        eci_1_Oxidation_State = eci_1_valence
        db[eci_1]['valence'] = eci_1_valence
        db[eci_1]['Oxidation_State'] = eci_1_valence
        print("eci_1_Oxidation_State is ", eci_1_Oxidation_State)
        print("db[eci_1]['valence'] is numeric ", eci_1_valence)
        ''' eci_db['eci_2']['eci_type'] == 'elements': '''
        if eci_2_valence.isnumeric():
            eci_2_Oxidation_State = eci_2_valence
            db[eci_2]['valence'] = eci_2_valence
            db[eci_2]['Oxidation_State'] = eci_2_Oxidation_State
            print("db[eci_2]['valence'] is numeric ", eci_2_valence)
            print("eci_1_Oxidation_State is ", eci_1_Oxidation_State)
            ''' Now we can solve for the valences'''
        elif not eci_2_valence.isnumeric():
            print("In elif not eci_2_valence.isnumeric")
            if eci_2_group == "7A":
                print("db[eci_2]['_group'] is ", eci_2_group)
                if eci_1_electronegativity < eci_2_electronegativity:
                    eci_2_valence = -1
                    eci_2_Oxidation_State = eci_2_valence
                    db[eci_2]['Oxidation_State'] = eci_2_Oxidation_State
                    print("eci_2_Oxidation_State is ", eci_2_Oxidation_State)
                    ''' The following can be moved to synthesis. '''
                    eci_1_M_qty = 1
                    e_eci_1_qty = eci_1_mass # e_eci_1_qty = eci_1_mass
                    print('e_eci_1_qty is at line 1693', e_eci_1_qty)
                    #e_eci_1_qty.delete(0)
                    #e_eci_1_qty.insert(0, eci_1_mass)
                    #print('e_eci_1_qty is at line 1696', e_eci_1_qty)
                    e_eci_1_M_qty.delete(0)
                    e_eci_1_M_qty.insert(0, eci_1_M_qty)
                    eci_2_M_qty = eci_1_valence  # This is correct. Cross assign valences to quantities
                    e_eci_2_M_qty.delete(0, END)
                    e_eci_2_M_qty.insert(0, eci_2_M_qty)
                    ''' Set the type and value of the compound.'''
                    ''' These functions will be moved to other processes when they are defined.
                    Oxidation_Rate_Elements will only store the oxidation states in the frame directories. '''
                    cb_4_type = "compound"
                    eci_4_type = "compound"
                    ''' Set a temporary variable to hold the formula variable
                    because the formula assumes quantity is 1, so it doen't need to be shown'''
                    eci_1a = eci_1
                    eci_2a = eci_2
                    if eci_2_valence == -1:
                        eci_1a = eci_1
                    elif not eci_2_valence == -1:
                        eci_1a = eci_1 + str(eci_2_valence)
                    if eci_1_valence == '1':
                        eci_2a = eci_2
                        print('eci_2a is ', eci_2a)
                    elif not eci_1_valence == '1':
                        eci_2a = eci_2 + str(eci_1_valence)
                    eci_4 = eci_1a + eci_2a
                    ''' Need to set cb_eci_4 selected item to eci_4'''
                    cb_eci_4.set(eci_4)
                    e_eci_4_M_qty.delete(0, END)
                    e_eci_4_M_qty.insert(0, 1)
                    print("eci_4 is ", eci_4)
                    print("e_eci_1_M_qty is ", e_eci_1_M_qty.get())
                    print("e_eci_2_M_qty is ", e_eci_2_M_qty.get())
                elif eci_1_electronegativity > eci_2_electronegativity:
                    print(
                        "In Oxidation_Rate_Elements eci_2 group 7A -- eci_1_electronegativity > eci_2_electronegativity")
            elif eci_2_group == "6A":  # Will need to exclude Oxygen for some compounds
                print("In Oxidation_Rate_Elements eci_2_group == 6A.")
                db[eci_2]['_group'] = eci_2_group
                print("db[eci_2]['_group'] is ", eci_2_group)
                if eci_1_electronegativity < eci_2_electronegativity:
                    eci_2_valence = -2
                    eci_1_M_qty = -eci_2_valence
                    eci_2_M_qty = eci_1_valence
                    eci_2_Oxidation_State = eci_2_valence
                    print("eci_2_Oxidation_State is ", eci_2_Oxidation_State)
                    if eci_2_valence == -2 and eci_1_valence == "1":
                        print("if eci_2_valence == -2 and eci_1_valence == 1:")
                        print("eci_1 is", eci_1, "eci_2_valence is", eci_2_valence, "eci_2 is", eci_2)
                        eci_4 = eci_1 + str(abs(eci_2_valence)) + eci_2
                        e_eci_1_M_qty.delete(0)
                        e_eci_1_M_qty.insert(0, eci_1_M_qty)
                        eci_2_M_qty = eci_1_valence  # This is correct. Cross assign valences to quantities
                        e_eci_2_M_qty.delete(0, END)
                        e_eci_2_M_qty.insert(0, eci_2_M_qty)
                    elif -int(eci_2_valence) == int(eci_1_valence):
                        print("-eci_2_valence is", -eci_2_valence)
                        eci_4 = eci_1 + eci_2
                        e_eci_1_M_qty.delete(0)
                        e_eci_1_M_qty.insert(0, 1)
                        e_eci_2_M_qty.delete(0, END)
                        e_eci_2_M_qty.insert(0, 1)
                    elif not -int(eci_2_valence) == int(eci_1_valence):
                        eci_4 = eci_1 + str(-eci_2_valence) + eci_2 + str(eci_1_valence)
                        print("-int(eci_2_valence) is", -int(eci_2_valence))
                        print("int(eci_1_valence) is", int(eci_1_valence))
                        # eci_4 = eci_1 + eci_2 + eci_1_valence
                        e_eci_1_M_qty.delete(0)
                        e_eci_1_M_qty.insert(0, eci_1_M_qty)
                        eci_2_M_qty = eci_1_valence  # This is correct. Cross assign valences to quantities
                        e_eci_2_M_qty.delete(0, END)
                        e_eci_2_M_qty.insert(0, eci_2_M_qty)
                    cb_eci_4.set(eci_4)
                    e_eci_4_M_qty.delete(0, END)
                    e_eci_4_M_qty.insert(0, 1)
                    print("eci_4 is ", eci_4)
                    eci_1_massa = float(eci_1_M_qty) * float(eci_1_mass)
                    print("eci_1_massa is ", eci_1_massa)
                    e_eci_1_qty.delete(0)
                    e_eci_1_qty.insert(0, eci_1_massa)
                    print('e_eci_1_qty is at line 1772', e_eci_1_qty)
                    e_eci_2_qty.delete(0)
                    e_eci_2_qty.insert(0, float(eci_2_M_qty) * float(eci_2_mass))
                    # eci_1_M_qty = 1

            elif not eci_2_group == "6A" and not eci_2_group == "7A":
                print("In Oxidation_Rate_Elements not eci_2_group == 6A or 7A.")
            elif eci_1_electronegativity > eci_1_electronegativity:
                pass
    elif not eci_1_valence.isnumeric():  # if eci_1_valence is a string of valence values
        print("In Oxidation_Rate_Elements not eci_1_valence.isnumeri.")
    else:
        e_Explanation.insert(END, "In Oxidation_Rate process else clause\n")

def Acid_Base():
    e_Explanation.insert(END, "Acid_Base process entered\n")

def Combustion():
    e_Explanation.insert(END, "Combustion process entered\n")

def Decomposition():
    e_Explanation.insert(END, "Decomposition process entered\n")

def Neutralization():
    e_Explanation.insert(END, "Neutralization process entered\n")


def Decompostion():
    e_Explanation.insert(END, "Decompostion process entered\n")

def Precipitation():
    e_Explanation.insert(END, "Precipitation process entered\n")

def Refinement():
    e_Explanation.insert(END, "Refinement process entered\n")

def Single_Replacement():
    e_Explanation.insert(END, "Single_Replacement process entered\n")

def Double_Replacement():
    e_Explanation.insert(END, "Double_Replacement process entered\n")

def Metathesis():
    e_Explanation.insert(END, "Metathesis process entered\n")


def Oxidization():
    e_Explanation.insert(END, "Oxidization process entered\n")

def Synthesis():
    '''
    Option 1. The user will select a product and the program will determine the reactants
    and the by-products.
    Option 2. The user will start by entering compounds and or elements in the left side of the
    GUI. Since there are so many possibilities, the user will need to specify the reactants and
    the primary product. Any other products will be considered by-products.
    Start by counting the number of reactants, alphabetize them, look up all the products
    that have any combination of those reactant elements, and fill the product combobox
    with that list. Since the program will not know which items will be products and which
    will be by-products, the list must contain all the compounds that have any of the reactants.
    All products that do not have those elements can be eliminated from the products comboboxes --
    even catalysts can be eliminated because they will be specified in a separate combobox.
    When a primary product has been selected, start the synthesis process by calculating the
    oxidation status, then

    '''
    e_Explanation.insert(END, "Synthesis process entered\n")
    print("2479 Synthesis process entered")
    CountElements()
    AlphabetizeElements()
    Fill_Product_Comboboxes()
    Oxidation_Rate()

    ''' Consider starting with a compound formula or name.'''

    cb_1_type = cb_Select_CB1.get()  # Get the selected type of: element, compound, or ion
    cb_2_type = cb_Select_CB2.get()
    cb_3_type = cb_Select_CB3.get()

    print("cb_1_type is", cb_1_type, "cb_2_type is", cb_2_type)

    # e_Explanation.insert(tk.END, "cb_1_type = cb_Select_CB1.get() step\n")

    eci_1 = cb_eci_1.get()
    eci_2 = cb_eci_2.get()
    # if cb_1_type == 'elements':
    #    eci_1_valence = db[eci_1]['valence']
    #    eci_2_valence = db[eci_2]['valence']
    #    print("eci_1 is", eci_1, "eci_2 is", eci_2)
    # eci_3 = cb_eci_3.get()
    # and eci_1 != ''
    # eci_1_valence = db[eci_1]['valence']
    # eci_3_group = db[eci_3]['_group']
    '''
    Cut out code that determines oxidation rate for elements.
    '''
    if cb_1_type == 'compounds':
        eci_1 = cb_eci_1.get()
        print('eci_1 is ', eci_1)
        eci_1_name = c_db[eci_1]['name']
        # eci_1_name = c_db[eci_1]['name']
        print('eci_1 is ', eci_1)
        # e_Explanation.insert(tk.END, "In Synthesis, compounds.\n")

def set_eci_db_eci_1_qty(qty):
    set_eci_db_eci_1_qty = qty
    print('2517 set_eci_db_eci_1_qty is ', set_eci_db_eci_1_qty)


''' function may not be needed
def eci_1_qty_changed(eventObject):    #callback
    eci_1_qty = e_eci_1_qty.get()   #e_eci_1_qty
    print('eci_1_qty is ', eci_1_qty)'''


def callback_set_temp_units(eventObject):
    pass
    ''' Whenever a temperature units combo box is selected, update the eci_db variable. '''
    '''
    eci_1_temp_units = cb_1_Temp_Units.get()
    eci_2_temp_units = cb_2_Temp_Units.get()
    eci_3_temp_units = cb_3_Temp_Units.get()
    eci_4_temp_units = cb_4_Temp_Units.get()
    eci_5_temp_units = cb_5_Temp_Units.get()
    eci_6_temp_units = cb_6_Temp_Units.get()
    eci_d['eci_1']['display_temp_units'] = cb_1_Temp_Units.get()
    eci_d['eci_2']['display_temp_units'] = cb_2_Temp_Units.get()
    eci_d['eci_3']['display_temp_units'] = cb_3_Temp_Units.get()
    eci_d['eci_4']['display_temp_units'] = cb_4_Temp_Units.get()
    eci_d['eci_5']['display_temp_units'] = cb_5_Temp_Units.get()
    eci_d['eci_6']['display_temp_units'] = cb_6_Temp_Units.get()
    '''

def callback_set_press_units(eventObject):
    ''' Whenever a temperature units combo box is selected, update the eci_db variable. '''
    '''
    eci_1_press_units = cb_1_Press_Units.get()
    eci_2_press_units = cb_2_Press_Units.get()
    eci_3_press_units = cb_3_Press_Units.get()
    eci_4_press_units = cb_4_Press_Units.get()
    eci_5_press_units = cb_5_Press_Units.get()
    eci_6_press_units = cb_6_Press_Units.get()
    eci_d['eci_1']['display_press_units'] = cb_1_Press_Units.get()
    eci_d['eci_2']['display_press_units'] = cb_2_Press_Units.get()
    eci_d['eci_3']['display_press_units'] = cb_3_Press_Units.get()
    eci_d['eci_4']['display_press_units'] = cb_4_Press_Units.get()
    eci_d['eci_5']['display_press_units'] = cb_5_Press_Units.get()
    eci_d['eci_6']['display_press_units'] = cb_6_Press_Units.get()
    '''


def Reset_Product_Boxes():
    e_eci_1_M_qty.delete(0, END)
    e_eci_1_M_qty.insert(0, 0.0)
    cb_eci_2.set("")
    cb_eci_2_N.set("")
    e_eci_2_M_qty.delete(0, END)
    e_eci_2_M_qty.insert(0, 0.0)
    cb_eci_3.set("")
    cb_eci_3_N.set("")
    e_eci_3_M_qty.delete(0, END)
    e_eci_3_M_qty.insert(0, 0.0)
    e_eci_4_M_qty.delete(0, END)
    e_eci_4_M_qty.insert(0, 0.0)
    cb_eci_5.set("")
    cb_eci_5_N.set("")
    e_eci_5_M_qty.delete(0, END)
    e_eci_5_M_qty.insert(0, 0.0)
    cb_eci_6.set("")
    cb_eci_6_N.set("")
    e_eci_6_M_qty.delete(0, END)
    e_eci_6_M_qty.insert(0, 0.0)

def Parse_Reactants():  # 'He2SO4'
    ''' I need to parse for number, uppercase, and lowercase. Leading number always applies to an element or formula,
    later numbers are assumed to apply to the preceeding element.
    '''
    e_Explanation.insert(END, "Parse_Reactants process entered\n")
    if cb_Select_CB1.get() == 'compounds':
        eci_1 = cb_eci_1.get()
        compound = cb_eci_1.get()
        print('Parse_Reactants compound is ', compound)

    elif not cb_Select_CB1.get() == 'compounds':
        print('In Parse_Reactants, but compound type is not a set')
        e_Explanation.insert(END, "Parse_Compounds process entered, but compound type is not a set\n")

    else: print("Parse_Reactants process entered", cb_eci_1.get())


    #print('Parse_Reactants compound is ', compound)
    ''' Start with a normal compound which does not start with an integer.'''
    # For example: compound = 'Na2SO4'
    if cb_Select_CB1.get() == '':
        e_Explanation.insert(END, "Parse_Reactants process entered, but compound is empty string. \n")
    elif compound[0].isdigit():
        ''' If the leading character is a number, apply it to the whole formula. '''
        compound_formula_qty = compound[0]
        ''' Reset the compound to the string after the intial digit. '''
        compound = compound[1:]
        print('Parse_Reactants compound first character is integer ', compound[0])
        ''' The first character is not a number. '''
    elif not compound[0].isdigit():
        print('Pass to Parse_Compound') #Parse_Compound_ECI_1
        parsed_compound = Parse_Compound(compound)

        Display_Parsed_Reactant(parsed_compound)
        # Parse_Compound_ECI_1()
    else:
        print('In else clause of Parse_Compounds')
    # print(' If the leading character is a number, '
    #      'need to add it to the result of Parse_Compounds_1(compound).')

def Parse_Products(): # 'He2SO4'
    ''' I need to parse for number, uppercase, and lowercase. Leading number always applies to an element or formula,
    later numbers are assumed to apply to the preceeding element.
    '''
    e_Explanation.insert(END, "2828 Parse_Products process entered\n")
    if cb_Select_CB4.get() == 'compounds':
        eci_4 = cb_eci_4.get()
        compound = cb_eci_4.get()
        print('Parse_Products compound is ', compound)

    elif not cb_Select_CB4.get() == 'compounds':
        print('In Parse_Products, but compound type is not set')
        e_Explanation.insert(END, "Parse_Products process entered, but compound type is not set\n")

    else: print("2838 Parse_Products process entered", cb_eci_4.get())

    ''' Start with a normal compound which does not start with an integer.'''
    if compound == "":
        e_Explanation.insert(END, "Parse_Products process entered, but compound is empty string. \n")
    elif compound[0].isdigit():
        ''' If the leading character is a number, apply it to the whole formula. '''
        compound_formula_qty = compound[0]
        ''' Reset the compound to the string after the intial digit. '''
        compound = compound[1:]
        print('Parse_Products compound first character is integer ', compound[0])
        ''' The first character is not a number. '''
    elif not compound[0].isdigit():
        print('Pass to Parse_Products') #Parse_Compound_ECI_1
        parsed_compound = Parse_Compound(compound)
        Display_Parsed_Product(parsed_compound)
        # Parse_Compound_ECI_1()
    else:
        print('In else clause of Parse_Compounds')
    # print(' If the leading character is a number, '
    #      'need to add it to the result of Parse_Compounds_1(compound).')

def Parse_Compound(compound):
    ''' Got a compound from eci_1. Parse it. '''
    print('2862 In Parse_Compound(compound): compound = ', compound)
    len_compound = len(compound)
    current_compound = []
    # print('len_compound is ', len_compound)
    while len(compound) >= 3:
        # print('len(compound) is ', len_compound)
        if compound[0].isupper() and compound[1].islower() and compound[2].isdigit():  # and compound[3].isupper():
            print(
                'In compound[0].isupper() and compound[1].islower() and compound[2].isdigit()')  # Re,removed  and compound[3].isupper()
            current_element_multiplier = 1
            current_element = compound[:2]
            current_element_multiplier = int(compound[2:3])
            current_compound.append(current_element)
            current_compound.append(current_element_multiplier)
            compound = compound[3:]
            print('elif compound[0].isupper() and compound[1].isdigit() and compound[2].isupper(): compound = ',
                  compound)
            print('2879 current_element is ', current_element, ' current_element_multiplier is ', current_element_multiplier)
            print('2880 current_compound is ', current_compound)
        elif compound[0].isupper() and compound[1].islower() and compound[2].isdigit():  # and compound[3].isdigit()
            print('In compound[0].isupper() and compound[1].islower() and compound[2].isdigit()')
            print("Don't know if there are any of these.")
        elif compound[0].isupper() and compound[1].isupper():
            print('In compound[0].isupper() and compound[1].isupper()')
            current_element_multiplier = 1
            current_element = compound[0]
            current_compound.append(current_element)
            current_compound.append(current_element_multiplier)
            compound = compound[1:]
            print('In elif compound[1].isupper() and len(compound) > 1: compound = ', compound)
            print('2892 current_element is ', current_element, ' current_element_multiplier is ', current_element_multiplier)
            print('2893 current_compound is ', current_compound)
        elif compound[0].isupper() and compound[1].islower() and compound[2].isupper():
            print('In compound[0].isupper() and compound[1].islower() and compound[2].isupper()')
            current_element_multiplier = 1
            current_element = compound[:2]
            current_element_multiplier = 1
            current_compound.append(current_element)
            current_compound.append(current_element_multiplier)
            compound = compound[2:]
            len_compound = len(compound)
            print('elif compound[0].isupper() and compound[1].islower() and compound[2].isupper(): compound = ',
                  compound)
            print('2905 current_element is ', current_element, ' current_element_multiplier is ', current_element_multiplier)
            print('2906 current_compound, and length are ', current_compound, len_compound)
        elif compound[0].isupper() and compound[1].isdigit() and compound[2].isupper():
            print('In compound[0].isupper() and compound[1].isdigit() and compound[2].isupper()')
            current_element_multiplier = 1
            current_element = compound[:1]
            current_element_multiplier = int(compound[1:2])
            current_compound.append(current_element)
            current_compound.append(current_element_multiplier)
            compound = compound[2:]
            print('elif compound[0].isupper() and compound[1].isdigit() and compound[2].isupper(): compound = ',
                  compound)
            print('2917 current_element is ', current_element, ' current_element_multiplier is ', current_element_multiplier)
            print('2918 current_compound is ', current_compound)
        elif compound[0].isupper() and compound[1].isdigit() and compound[2].isdigit():
            print('In compound[0].isupper() and compound[1].isdigit() and compound[2].isdigit()')
            current_element_multiplier = 1
            current_element = compound[:1]
            current_element_multiplier = int(compound[1:3])
            current_compound.append(current_element)
            current_compound.append(current_element_multiplier)
            if len(compound) > 2:
                compound = compound[3:]
            else:
                compound = ""
            print('elif compound[0].isupper() and compound[1].isdigit() and compound[2].isupper(): compound = ',
                  compound)
            print('2932 current_element is ', current_element, ' current_element_multiplier is ', current_element_multiplier)
            print('2933 current_compound is ', current_compound)

    if len(compound) < 3:
        print('if len(compound) < 3:')
        while len(compound) > 0:
            if compound[0] == '_':
                compound = ""
                print("In if compound[0] == '_':")
            elif len(compound) == 1:
                if compound[0].isupper():
                    print('In compound[0].isupper()')
                    current_element_multiplier = 1
                    current_element = compound[0]
                    current_compound.append(current_element)
                    current_compound.append(current_element_multiplier)
                    print('In if compound[0].isupper():: compound = ', compound)
                    print('2949 current_element is ', current_element, ' current_element_multiplier is ',
                          current_element_multiplier)
                    print('2951 current_compound is ', current_compound)
                    compound = ""
            elif len(compound) == 2:
                if compound[0].isupper() and compound[1].isupper():
                    print('In compound[0].isupper() and compound[1].isupper()')
                    current_element_multiplier = 1
                    current_element = compound[0]
                    current_compound.append(current_element)
                    current_compound.append(current_element_multiplier)
                    compound = compound[1:]
                    print('In elif compound[1].isupper() and len(compound) > 1: compound = ', compound)
                    print('2962 current_element is ', current_element, ' current_element_multiplier is ',
                          current_element_multiplier)
                    print('2964 current_compound is ', current_compound)
                elif compound[0].isupper() and compound[1].islower():
                    print('In compound[0].isupper() and compound[1].islower()')
                    current_element_multiplier = 1
                    current_element = compound[0:1]
                    current_compound.append(current_element)
                    current_compound.append(current_element_multiplier)
                    compound = ""
                    print('In if compound[0].isupper() and compound[1].islower():: compound = ', compound)
                    print('2973 current_element is ', current_element, ' current_element_multiplier is ', current_element_multiplier)
                    print('2974 current_compound is ', current_compound)
                elif compound[0].isupper() and compound[1].isdigit():
                    print('In compound[0].isupper() and compound[1].isdigit()')
                    current_element_multiplier = 1
                    current_element = compound[0]
                    current_element_multiplier = int(compound[1])
                    current_compound.append(current_element)
                    current_compound.append(current_element_multiplier)
                    compound = ""
                    print('In if compound[0].isupper() and compound[1].islower():: compound = ', compound)
                    print('2984 current_element is ', current_element, ' current_element_multiplier is ', current_element_multiplier)
                    print('2985 current_compound is ', current_compound)
        print('2986 compound =  ', compound)
        compound = ""
        return current_compound
        #Display_Parsed_Reactant(current_compound)


def Display_Parsed_Reactant(parsed_compound):
    print('Entering Display_Parsed_Compound')
    print("2994 parsed_compound is ", parsed_compound)
    ''' Need to reset all possible product boxes to empty strings'''
    Reset_Product_Boxes()
    ''' Set the current reactant moles to 1.'''
    e_eci_1_M_qty.delete(0, END)
    e_eci_1_M_qty.insert(0, 1)
    ''' Set the product type to elements.'''
    cb_Select_CB4.set('elements')
    ''' Set the product element formulas, and moles. And names? '''
    element_1 = parsed_compound[0]
    print('element_1 is ', element_1)
    cb_eci_4.set("")
    cb_eci_4_N.set("")
    cb_eci_4.set(element_1)
    moles_1 = parsed_compound[1]
    print('moles_1 is ', moles_1)
    e_eci_4_M_qty.delete(0, END)
    e_eci_4_M_qty.insert(0, moles_1)

    cb_Select_CB5.set('elements')
    element_2 = parsed_compound[2]
    print('element_2 is ', element_2)
    cb_eci_5.set("")
    cb_eci_5_N.set("")
    cb_eci_5.set(element_2)
    moles_2 = parsed_compound[3]
    e_eci_5_M_qty.delete(0, END)
    e_eci_5_M_qty.insert(0, moles_2)

    try:
        if parsed_compound[4]:
            print('parsed_compound[4] is ', parsed_compound[4])
            cb_Select_CB6.set('elements')
            element_3 = parsed_compound[4]
            print('element_3 is ', element_3)
            cb_eci_6.set("")
            cb_eci_6_N.set("")
            cb_eci_6.set(element_3)
            moles_3 = parsed_compound[5]
            e_eci_6_M_qty.delete(0, END)
            e_eci_6_M_qty.insert(0, moles_3)
        if parsed_compound[6]:
            cb_Select_CB3.set('elements')
            element_4 = parsed_compound[6]
            print('element_4 is ', element_4)
            cb_eci_3.set("")
            cb_eci_3_N.set("")
            cb_eci_3.set(element_4)
            moles_4 = parsed_compound[7]
            e_eci_3_M_qty.delete(0, END)
            e_eci_3_M_qty.insert(0, moles_4)
    except:
        pass

def Display_Parsed_Product(parsed_compound):
    print('Entering Display_Parsed_Product')
    print("3048 parsed_compound is ", parsed_compound)
    ''' Need to reset all possible product boxes to empty strings'''
    Reset_Product_Boxes()
    e_eci_4_M_qty.delete(0, END)
    e_eci_4_M_qty.insert(0, 1)

    cb_Select_CB1.set('elements')
    element_1 = parsed_compound[0]
    print('element_1 is ', element_1)
    cb_eci_1.set("")
    cb_eci_1_N.set("")
    cb_eci_1.set(element_1)
    moles_4 = parsed_compound[1]
    print('moles_1 is ', moles_4)
    e_eci_1_M_qty.delete(0, END)
    e_eci_1_M_qty.insert(0, moles_4)

    cb_Select_CB2.set('elements')
    element_2 = parsed_compound[2]
    print('element_2 is ', element_2)
    cb_eci_2.set("")
    cb_eci_2_N.set("")
    cb_eci_2.set(element_2)
    moles_2 = parsed_compound[3]
    e_eci_2_M_qty.delete(0, END)
    e_eci_2_M_qty.insert(0, moles_2)

    try:
        if parsed_compound[4]:
            print('parsed_compound[4] is ', parsed_compound[4])
            cb_Select_CB3.set('elements')
            element_3 = parsed_compound[4]
            print('element_3 is ', element_3)
            cb_eci_3.set("")
            cb_eci_3_N.set("")
            cb_eci_3.set(element_3)
            moles_3 = parsed_compound[5]
            e_eci_3_M_qty.delete(0, END)
            e_eci_3_M_qty.insert(0, moles_3)
        if parsed_compound[6]:
            cb_Select_CB6.set('elements')
            element_4 = parsed_compound[6]
            print('element_4 is ', element_4)
            cb_eci_6.set("")
            cb_eci_6_N.set("")
            cb_eci_6.set(element_4)
            moles_4 = parsed_compound[7]
            e_eci_6_M_qty.delete(0, END)
            e_eci_6_M_qty.insert(0, moles_4)
    except:
        pass

''' Use decimal instead of float in order to eliminate floating point errors. '''
def Parse_Compound_Logic():
    ''' Identify the logical steps in parsing compounds'''
    print('In Parse_Compound_Logic')
    ''' Get len(compound'''
    ''' If len(compound < 3'''
    ''' If len(compound >= 3 -- there is only one four item pattern, so include it with 3 item pattern. '''
    ''' Patterns that allow the first element to be identified and separated are:'''
    ''' Upper, upper -- compound[0].isupper() and compound[1].isupper()'''
    ''' Upper, lower, upper -- compound[0].isupper() and compound[1].islower() and compound[2].isupper() '''
    ''' Upper, digit, upper -- compound[0].isupper() and compound[1].isdigit() and compound[2].isupper() '''
    ''' Upper, lower, digit -- compound[0].isupper() and compound[1].islower() and compound[2].isdigit() '''
    ''' Patterns that allow the subsequent element or digits to be identified and separated are:'''
    ''' same as above'''
    ''' Upper, upper -- compound[0].isupper() and compound[1].isupper()'''
    ''' Upper, lower, upper -- compound[0].isupper() and compound[1].islower() and compound[2].isupper() '''
    ''' Upper, digit, upper -- compound[0].isupper() and compound[1].isdigit() and compound[2].isupper() '''

    ''' *** Not valid *** Upper, lower, digit -- compound[0].isupper() and compound[1].islower() and compound[2].isdigit() '''
    ''' new patterns'''
    ''' Upper, digit, digit -- compound[0].isupper() and compound[1].isdigit() and compound[2].isdigit() '''
    ''' Upper, lower, digit, digit -- compound[0].isupper() and compound[1].islower() and compound[2].isdigit()  and compound[3].isdigit()'''
    ''' digit, upper -- compound[0].isdigit() and compound[1].isupper() '''
    ''' digit, digit, upper -- compound[0].isdigit() and compound[1].isdigit() and compound[2].isupper() '''
    ''' final patterns'''
    ''' If len(compound < 3'''
    ''' All the above where length is 2, 1, or 0. '''


def CountElements():  # The following does not work. Need valid test for value
    e_Explanation.insert(tk.END, "CountElements process entered\n")
    intElementCount = 0
    eci_1 = cb_eci_1.get()
    eci_2 = cb_eci_2.get()
    eci_3 = cb_eci_3.get()
    if eci_1 == "":  # cb_eci_1
        intElementCount = 0
    else:
        intElementCount = 1
    if eci_2 == "":
        pass
    else:
        intElementCount = intElementCount + 1
    if eci_3 == "":
        pass
    else:
        intElementCount = intElementCount + 1
    print('element count is', intElementCount)
    # rtb_Explanation.Text = rtb_Explanation.Text & intElementCount

def AlphabetizeElements():  # TypeError: '<' not supported between instances of 'StringVar' and 'StringVar'
    e_Explanation.insert(END, "AlphabetizeElements process entered\n")
    strAlphaElements = ""
    eci_1 = cb_eci_1.get()
    eci_2 = cb_eci_2.get()
    eci_3 = cb_eci_3.get()

    if eci_1 < eci_2 and eci_1 < eci_3:
        if eci_2 < eci_3:
            strAlphaElements = eci_1 + eci_2 + eci_3
        elif eci_3 < eci_2:
            strAlphaElements = eci_1 + eci_3 + eci_2
    elif eci_2 < eci_1 and eci_2 < eci_3:
        if eci_1 < eci_3:
            strAlphaElements = eci_2 + eci_1 + eci_3
        elif eci_3 < eci_1:
            strAlphaElements = eci_2 + eci_3 + eci_1
    elif eci_3 < eci_1 and eci_3 < eci_2:
        if eci_1 < eci_2:
            strAlphaElements = eci_3 + eci_1 + eci_2
        elif eci_2 < eci_1:
            strAlphaElements = eci_3 + eci_2 + eci_1
    else:
        e_Explanation.insert(END, 'Error:Fell to else clause in AlphabetizeElements\n')
    # e_Explanation.insert(tk.END, 'strAlphaElements is %', strAlphaElements) #How do I insert arguments?
    print('strAlphaElements is ', strAlphaElements)

def reset_s_x(eci):
  print("3336 Entering reset_s_x, eci is ", eci)
  eci_d[eci]['qty'] = 0
  eci_d[eci]["units"] = "grams"
  eci_d[eci]["M_qty"] = 1
  eci_d[eci]["valence"] = 0
  eci_d[eci]["kl_qty"] = 0
  eci_d[eci]["kl_units"] = ""
#   print("3343 eci_d[eci]['kl_units']", eci_d[eci]["kl_units"])
  eci_d[eci]["temp_display_qty"] = 0
  eci_d[eci]["mm_qty"] = 0
  eci_d[eci]["mm_units"] = ""
  eci_d[eci]["temp_calc_qty"] = 273.15
  eci_d[eci]["temp_display_units"] = "C"
#   print("3349 eci_d[eci]['temp_display_units']", eci_d[eci]["temp_display_units"])
  eci_d[eci]["press_display_qty"] = 1
  eci_d[eci]["press_display_units"] = "atm"
  eci_d[eci]["mm_units"] = ""
  eci_d[eci]["heat_calc_qty"] = 0
  eci_d[eci]["heat_display_units"] = ""
  eci_d[eci]["other_display_qty"] = 0
  eci_d[eci]["other_display_units"] = ""

#   print("3296 ",eci, eci_d[eci]["kl_units"])

def refresh_display(eci):
    # print("3293 refresh_display", eci)
    if eci == "eci_1":
        refresh_s_1_display(eci)
    elif eci == "eci_2":
        refresh_s_2_display(eci)
    elif eci == "eci_3":
        refresh_s_3_display(eci)
    elif eci == "eci_4":
        refresh_s_4_display(eci)
    elif eci == "eci_5":
        refresh_s_5_display(eci)
    elif eci == "eci_6":
        refresh_s_6_display(eci)
    else:
        print("Error in refresh_display function.")

def refresh_s_1_display(eci):
   print("3376 refresh_s_1_display")
   cb_eci_1_N.set(eci_d[eci]['name'])
   cb_eci_1_units.set(eci_d[eci]['units'])
   e_eci_1_qty.delete(0, tk.END)
   e_eci_1_qty.insert(0, eci_d[eci]['qty'])
   e_eci_1_M_qty.delete(0, tk.END)
   e_eci_1_M_qty.insert(0, eci_d[eci]['M_qty'])
   cb_eci_1_valence.set(eci_d[eci]['valence'])
   e_eci_kl_1_qty.delete(0, tk.END)
   e_eci_kl_1_qty.insert(0, eci_d[eci]['kl_qty'])
   cb_kl_1_units.set(eci_d[eci]["kl_units"])
   e_eci_MM_1_qty.delete(0, tk.END)
   e_eci_MM_1_qty.insert(0, eci_d[eci]['mm_qty'])
   cb_MM_1_units.set(eci_d[eci]["mm_units"])
   e_Temp_Qty_1.delete(0, tk.END)
   e_Temp_Qty_1.insert(0, eci_d[eci]["temp_display_qty"])
   cb_1_Temp_Units.set(eci_d[eci]["temp_display_units"])
   e_Press_Qty_1.delete(0, tk.END)
   e_Press_Qty_1.insert(0, eci_d[eci]["press_display_qty"])
   cb_1_Press_Units.set(eci_d[eci]["press_display_units"])
   e_Heat_Qty_1.delete(0, tk.END)
   e_Heat_Qty_1.insert(0, eci_d[eci]["heat_display_qty"])
   cb_1_Heat_Units.set(eci_d[eci]["heat_display_units"])
def refresh_s_2_display(eci):
   print("3376 refresh_s_2_display")
   cb_eci_2_N.set(eci_d[eci]['name'])
   cb_eci_2_units.set(eci_d[eci]['units'])
   e_eci_2_qty.delete(0, tk.END)
   e_eci_2_qty.insert(0, eci_d[eci]['qty'])
   e_eci_2_M_qty.delete(0, tk.END)
   e_eci_2_M_qty.insert(0, eci_d[eci]['M_qty'])
   cb_eci_2_valence.set(eci_d[eci]['valence'])
   e_eci_kl_2_qty.delete(0, tk.END)
   e_eci_kl_2_qty.insert(0, eci_d[eci]['kl_qty'])
   cb_kl_2_units.set(eci_d[eci]["kl_units"])
   e_eci_MM_2_qty.delete(0, tk.END)
   e_eci_MM_2_qty.insert(0, eci_d[eci]['mm_qty'])
   cb_MM_2_units.set(eci_d[eci]["mm_units"])
   e_Temp_Qty_2.delete(0, tk.END)
   e_Temp_Qty_2.insert(0, eci_d[eci]["temp_display_qty"])
   cb_2_Temp_Units.set(eci_d[eci]["temp_display_units"])
   e_Press_Qty_2.delete(0, tk.END)
   e_Press_Qty_2.insert(0, eci_d[eci]["press_display_qty"])
   cb_2_Press_Units.set(eci_d[eci]["press_display_units"])
   e_Heat_Qty_2.delete(0, tk.END)
   e_Heat_Qty_2.insert(0, eci_d[eci]["heat_display_qty"])
   cb_2_Heat_Units.set(eci_d[eci]["heat_display_units"])
def refresh_s_3_display(eci):
   print("3376 refresh_s_1_display")
   cb_eci_3_N.set(eci_d[eci]['name'])
   cb_eci_3_units.set(eci_d[eci]['units'])
   e_eci_3_qty.delete(0, tk.END)
   e_eci_3_qty.insert(0, eci_d[eci]['qty'])
   e_eci_3_M_qty.delete(0, tk.END)
   e_eci_3_M_qty.insert(0, eci_d[eci]['M_qty'])
   cb_eci_3_valence.set(eci_d[eci]['valence'])
   e_eci_kl_3_qty.delete(0, tk.END)
   e_eci_kl_3_qty.insert(0, eci_d[eci]['kl_qty'])
   cb_kl_3_units.set(eci_d[eci]["kl_units"])
   e_eci_MM_3_qty.delete(0, tk.END)
   e_eci_MM_3_qty.insert(0, eci_d[eci]['mm_qty'])
   cb_MM_3_units.set(eci_d[eci]["mm_units"])
   e_Temp_Qty_3.delete(0, tk.END)
   e_Temp_Qty_3.insert(0, eci_d[eci]["temp_display_qty"])
   cb_3_Temp_Units.set(eci_d[eci]["temp_display_units"])
   e_Press_Qty_3.delete(0, tk.END)
   e_Press_Qty_3.insert(0, eci_d[eci]["press_display_qty"])
   cb_3_Press_Units.set(eci_d[eci]["press_display_units"])
   e_Heat_Qty_3.delete(0, tk.END)
   e_Heat_Qty_3.insert(0, eci_d[eci]["heat_display_qty"])
   cb_3_Heat_Units.set(eci_d[eci]["heat_display_units"])
def refresh_s_4_display(eci):
   print("3376 refresh_s_1_display")
   cb_eci_4_N.set(eci_d[eci]['name'])
   cb_eci_4_units.set(eci_d[eci]['units'])
   e_eci_4_qty.delete(0, tk.END)
   e_eci_4_qty.insert(0, eci_d[eci]['qty'])
   e_eci_4_M_qty.delete(0, tk.END)
   e_eci_4_M_qty.insert(0, eci_d[eci]['M_qty'])
   cb_eci_4_valence.set(eci_d[eci]['valence'])
   e_eci_kl_4_qty.delete(0, tk.END)
   e_eci_kl_4_qty.insert(0, eci_d[eci]['kl_qty'])
   cb_kl_4_units.set(eci_d[eci]["kl_units"])
   e_eci_MM_4_qty.delete(0, tk.END)
   e_eci_MM_4_qty.insert(0, eci_d[eci]['mm_qty'])
   cb_MM_4_units.set(eci_d[eci]["mm_units"])
   e_Temp_Qty_4.delete(0, tk.END)
   e_Temp_Qty_4.insert(0, eci_d[eci]["temp_display_qty"])
   cb_4_Temp_Units.set(eci_d[eci]["temp_display_units"])
   e_Press_Qty_4.delete(0, tk.END)
   e_Press_Qty_4.insert(0, eci_d[eci]["press_display_qty"])
   cb_4_Press_Units.set(eci_d[eci]["press_display_units"])
   e_Heat_Qty_4.delete(0, tk.END)
   e_Heat_Qty_4.insert(0, eci_d[eci]["heat_display_qty"])
   cb_4_Heat_Units.set(eci_d[eci]["heat_display_units"])
def refresh_s_5_display(eci):
   print("3376 refresh_s_1_display")
   cb_eci_5_N.set(eci_d[eci]['name'])
   cb_eci_5_units.set(eci_d[eci]['units'])
   e_eci_5_qty.delete(0, tk.END)
   e_eci_5_qty.insert(0, eci_d[eci]['qty'])
   e_eci_5_M_qty.delete(0, tk.END)
   e_eci_5_M_qty.insert(0, eci_d[eci]['M_qty'])
   cb_eci_5_valence.set(eci_d[eci]['valence'])
   e_eci_kl_5_qty.delete(0, tk.END)
   e_eci_kl_5_qty.insert(0, eci_d[eci]['kl_qty'])
   cb_kl_5_units.set(eci_d[eci]["kl_units"])
   e_eci_MM_5_qty.delete(0, tk.END)
   e_eci_MM_5_qty.insert(0, eci_d[eci]['mm_qty'])
   cb_MM_5_units.set(eci_d[eci]["mm_units"])
   e_Temp_Qty_5.delete(0, tk.END)
   e_Temp_Qty_5.insert(0, eci_d[eci]["temp_display_qty"])
   cb_5_Temp_Units.set(eci_d[eci]["temp_display_units"])
   e_Press_Qty_5.delete(0, tk.END)
   e_Press_Qty_5.insert(0, eci_d[eci]["press_display_qty"])
   cb_5_Press_Units.set(eci_d[eci]["press_display_units"])
   e_Heat_Qty_5.delete(0, tk.END)
   e_Heat_Qty_5.insert(0, eci_d[eci]["heat_display_qty"])
   cb_5_Heat_Units.set(eci_d[eci]["heat_display_units"])
def refresh_s_6_display(eci):
   print("3376 refresh_s_1_display")
   cb_eci_6_N.set(eci_d[eci]['name'])
   cb_eci_6_units.set(eci_d[eci]['units'])
   e_eci_6_qty.delete(0, tk.END)
   e_eci_6_qty.insert(0, eci_d[eci]['qty'])
   e_eci_6_M_qty.delete(0, tk.END)
   e_eci_6_M_qty.insert(0, eci_d[eci]['M_qty'])
   cb_eci_6_valence.set(eci_d[eci]['valence'])
   e_eci_kl_6_qty.delete(0, tk.END)
   e_eci_kl_6_qty.insert(0, eci_d[eci]['kl_qty'])
   cb_kl_6_units.set(eci_d[eci]["kl_units"])
   e_eci_MM_6_qty.delete(0, tk.END)
   e_eci_MM_6_qty.insert(0, eci_d[eci]['mm_qty'])
   cb_MM_6_units.set(eci_d[eci]["mm_units"])
   e_Temp_Qty_6.delete(0, tk.END)
   e_Temp_Qty_6.delete(0, tk.END)
   e_Temp_Qty_6.insert(0, eci_d[eci]["temp_display_qty"])
   cb_6_Temp_Units.set(eci_d[eci]["temp_display_units"])
   e_Press_Qty_6.delete(0, tk.END)
   e_Press_Qty_6.insert(0, eci_d[eci]["press_display_qty"])
   cb_6_Press_Units.set(eci_d[eci]["press_display_units"])
   e_Heat_Qty_6.delete(0, tk.END)
   e_Heat_Qty_6.insert(0, eci_d[eci]["heat_display_qty"])
   cb_6_Heat_Units.set(eci_d[eci]["heat_display_units"])

def set_initial_form_values():
    eci_d = ["eci_1", "eci_2", "eci_3", "eci_4", "eci_5", "eci_6"]
    for eci in eci_d:
        reset_s_x(eci)
        refresh_display(eci)

'''Create the GUI '''
#root.title('Chemistry')

# lbl_spacing = Label(inside_frame, text="0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789")

# lbl_spacing.grid(row=0, column=0, columnspan=30)
# lbl_spacing.config(font=labelfont)
lbl_col_0 = Label(inside_frame, text="", width=5)
lbl_col_0.grid(row=0, column=0)
lbl_col_0.config(font=titlefont)
lbl_col_1 = Label(inside_frame, text="", width=5)
lbl_col_1.grid(row=0, column=1)
lbl_col_1.config(font=titlefont)
lbl_col_2 = Label(inside_frame, text="", width=5)
lbl_col_2.grid(row=0, column=2)
lbl_col_2.config(font=titlefont)
lbl_col_3 = Label(inside_frame, text="", width=5)
lbl_col_3.grid(row=0, column=3)
lbl_col_3.config(font=titlefont)
lbl_col_4 = Label(inside_frame, text="", width=5)
lbl_col_4.grid(row=0, column=4)
lbl_col_4.config(font=titlefont)
lbl_col_5 = Label(inside_frame, text="", width=5)
lbl_col_5.grid(row=0, column=5)
lbl_col_5.config(font=titlefont)
lbl_col_6 = Label(inside_frame, text="", width=5)
lbl_col_6.grid(row=0, column=6)
lbl_col_6.config(font=titlefont)
lbl_col_7 = Label(inside_frame, text="", width=5)
lbl_col_7.grid(row=0, column=7)
lbl_col_7.config(font=titlefont)
lbl_col_8 = Label(inside_frame, text="", width=5)
lbl_col_8.grid(row=0, column=8)
lbl_col_8.config(font=titlefont)
lbl_col_9 = Label(inside_frame, text="", width=5)
lbl_col_9.grid(row=0, column=9)
lbl_col_9.config(font=titlefont)
lbl_col_10 = Label(inside_frame, text="", width=5)
lbl_col_10.grid(row=0, column=10)
lbl_col_10.config(font=titlefont)
lbl_col_11 = Label(inside_frame, text="", width=5)
lbl_col_11.grid(row=0, column=11)
lbl_col_11.config(font=titlefont)
lbl_col_12 = Label(inside_frame, text="", width=5)
lbl_col_12.grid(row=0, column=12)
lbl_col_12.config(font=titlefont)
lbl_col_13 = Label(inside_frame, text="", width=5)
lbl_col_13.grid(row=0, column=13)
lbl_col_13.config(font=titlefont)
lbl_col_14 = Label(inside_frame, text="", width=5)
lbl_col_14.grid(row=0, column=14)
lbl_col_14.config(font=titlefont)
lbl_col_15 = Label(inside_frame, text="", width=5)
lbl_col_15.grid(row=0, column=15)
lbl_col_15.config(font=titlefont)
lbl_col_16 = Label(inside_frame, text="", width=5)
lbl_col_16.grid(row=0, column=16)
lbl_col_16.config(font=titlefont)
lbl_col_17 = Label(inside_frame, text="", width=5)
lbl_col_17.grid(row=0, column=17)
lbl_col_17.config(font=titlefont)
lbl_col_18 = Label(inside_frame, text="", width=5)
lbl_col_18.grid(row=0, column=18)
lbl_col_18.config(font=titlefont)
lbl_col_19 = Label(inside_frame, text="", width=5)
lbl_col_19.grid(row=0, column=19)
lbl_col_19.config(font=titlefont)
lbl_col_20 = Label(inside_frame, text="", width=5)
lbl_col_20.grid(row=0, column=20)
lbl_col_20.config(font=titlefont)

lbl_Title = Label(inside_frame, text="Pettus Chemistry Calculators") # inside_frame
lbl_Title.grid(row=0, column=2, sticky="w")
lbl_Title.config(font=boldfont)
btn_show_instructions = Button(inside_frame, text='Show Instructions', command=get_record)
btn_show_instructions.grid(row=0, column=6, sticky="nw")
btn_show_instructions.config(font=labelfont)

# btn_show_instructions.bind("<<ComboboxSelected>>", show_hide_instructions)
lbl_blank = Label(inside_frame, text="")
lbl_blank.grid(row=1, column=0)
lbl_blank.config(font=labelfont)

lbl_create_record = Label(inside_frame, text="Create record:       ")
lbl_create_record.grid(row=2, column=0, sticky="w")
lbl_create_record.config(font=labelfont)
e_recordname = Entry(inside_frame, text="") #, columnspan=2
e_recordname.grid(row=2, column=2, sticky="w")    #, sticky=W
e_recordname.config(font=labelfont)
btn_create_record = Button(inside_frame, text='Create Record', command=create_record)
btn_create_record.grid(row=2, column=3, sticky="w")
btn_create_record.config(font=buttonfont)
# btn_create_record.bind("<<ComboboxSelected>>", create_record())
btn_update_record = Button(inside_frame, text='Update Record', command=update_record)
btn_update_record.grid(row=2, column=4, sticky="w")
btn_update_record.config(font=buttonfont)
# btn_update_record.bind("<<ComboboxSelected>>", update_record)
btn_Continue = Button(inside_frame, text='* Continue *', command=Continue)
btn_Continue.grid(row=2, column=6)
btn_Continue.config(font=labelfont)

lbl_get_record = Label(inside_frame, text="Get record with ID:     ")
lbl_get_record.grid(row=3, column=0, columnspan=2, sticky="w")
lbl_get_record.config(font=labelfont)
# cb_Record_ID: Combobox = Combobox(inside_frame, values="") # , width=12
# cb_Record_ID.grid(row=3, column=3, columnspan=2)
# cb_Record_ID.config(font=entryfont)
# cb_Record_ID.bind("<<ComboboxSelected>>", retrieve_record)
# lbl_record_ID = Label(inside_frame, text="Record ID:     ")
# lbl_record_ID.grid(row=3, column=6, columnspan=2)
# lbl_record_ID.config(font=labelfont)
e_record_ID = Entry(inside_frame, text="")   #, width=30)
e_record_ID.grid(row=3, column=2, columnspan=2, sticky="w")
# e_record_ID.rowconfigure(0, weight=1)
e_record_ID.config(font=labelfont)
btn_get_record = Button(inside_frame, text='Get Record    ', command=get_record)
btn_get_record.grid(row=3, column=3,  sticky="w")
btn_get_record.config(font=buttonfont)
btn_get_record.bind("<<ComboboxSelected>>", retrieve_record)
btn_previous_record = Button(inside_frame, text='Previous Record', command=get_record)
btn_previous_record.grid(row=3, column=4, sticky="w")
btn_previous_record.config(font=buttonfont)
btn_previous_record.bind("<<ComboboxSelected>>", previous_record)
btn_next_record = Button(inside_frame, text='Next Record', command=get_record)
btn_next_record.grid(row=3, column=5, sticky="w")
btn_next_record.config(font=buttonfont)
btn_next_record.bind("<<ComboboxSelected>>", next_record)


lbl_LU_Compound = Label(inside_frame, text="Look up compound:")
lbl_LU_Compound.grid(row=4, column=0, columnspan=2, sticky="w")
lbl_LU_Compound.config(font=labelfont)
cb_LU_Compound = Combobox(inside_frame, values=compound_formula_string)
cb_LU_Compound.grid(row=4, column=2, columnspan=2, sticky="w")
cb_LU_Compound.config(font=entryfont)

# # Create a search for and retrieve a compount
lbl_LU_Process = Label(inside_frame, text="Look up process:")
lbl_LU_Process.grid(row=4, column=3, sticky="w")
lbl_LU_Process.config(font=labelfont)
cb_LU_Process = Combobox(inside_frame, values=major_process_list)
cb_LU_Process.grid(row=4, column=4, sticky="w")
cb_LU_Process.config(font=entryfont)
# Create a search for and retrieve a process
lbl_LU_Environment = Label(inside_frame, text="Look up environment:")
lbl_LU_Environment.grid(row=4, column=5, sticky="w")
lbl_LU_Environment.config(font=labelfont)
cb_LU_Environment = Combobox(inside_frame, values=environment)
cb_LU_Environment.grid(row=4, column=6, sticky="w")
cb_LU_Environment.config(font=entryfont)

lbl_Select_M_Process = Label(inside_frame, text="Select major process")
lbl_Select_M_Process.grid(row=5, column=0, sticky="w")
lbl_Select_M_Process.config(font=labelfont)
cb_Select_M_Process: Combobox = Combobox(inside_frame, values=major_process_list, textvariable=major_process_selected, width=12)
cb_Select_M_Process.grid(row=5, column=2, sticky="w")
cb_Select_M_Process.config(font=entryfont)
lbl_Select_m_Process = Label(inside_frame, text="Select minor process")
lbl_Select_m_Process.grid(row=5, column=3,  sticky="w")
lbl_Select_m_Process.config(font=labelfont)
cb_Select_m_Process: Combobox = Combobox(inside_frame, values=minor_process_list, textvariable=minor_process_selected, width=12)
cb_Select_m_Process.grid(row=5, column=4,  sticky="w")
cb_Select_m_Process.config(font=entryfont)
cb_Select_m_Process.bind("<<ComboboxSelected>>", minor_process_selected)
lbl_Select_Environment = Label(inside_frame, text="Select environment:")
lbl_Select_Environment.grid(row=5, column=5, columnspan=2, sticky="w")
lbl_Select_Environment.config(font=labelfont)
cb_Select_Environment: Combobox = Combobox(inside_frame, values=environment)
cb_Select_Environment.grid(row=5, column=6, sticky="w")
cb_Select_Environment.config(font=entryfont)

lbl_blank = Label(inside_frame, text="")
lbl_blank.grid(row=6, column=0)

lbl_eci_1 = Label(S_1_frame, text="Select Element, Compound or Ion for ComboBox 1")
lbl_eci_1.grid(row=0, column=0, columnspan=3, sticky="w")
lbl_eci_1.config(font=labelfont)
cb_Select_CB1: Combobox = Combobox(S_1_frame, values=eci_cb_values, width=10)
cb_Select_CB1.grid(row=0, column=4, sticky="w")
cb_Select_CB1.config(font=entryfont)
cb_Select_CB1.bind("<<ComboboxSelected>>", select_eci_1_type)
lbl_eci_4 = Label(S_4_frame, text="Select Element, Compound or Ion for ComboBox 4") # , bg="BLUE"
lbl_eci_4.grid(row=0, column=0, columnspan=3, sticky="nw") #, sticky=W)
lbl_eci_4.config(font=labelfont)
cb_Select_CB4 = Combobox(S_4_frame, values=eci_cb_values, width=10)
cb_Select_CB4.grid(row=0, column=4, sticky="nw")
cb_Select_CB4.config(font=entryfont)
cb_Select_CB4.bind("<<ComboboxSelected>>", select_eci_4_type)

# ***************
lbl_eci_1_qty = Label(S_1_frame, text="ECI 1 Qty", width=10)
lbl_eci_1_qty.grid(row=1, column=0, sticky="w")
lbl_eci_1_qty.config(font=labelfont)
lbl_eci_1_units = Label(S_1_frame, text="Units 1", width=10)
lbl_eci_1_units.grid(row=1, column=1, sticky="w") #, sticky=W)
lbl_eci_1_units.config(font=labelfont)
lbl_eci_1 = Label(S_1_frame, text="ECI 1", width=10)
lbl_eci_1.grid(row=1, column=2, sticky="w") #, sticky=W)
lbl_eci_1.config(font=labelfont)
lbl_eci_1_valence = Label(S_1_frame, text="Valence 1", width=10)
lbl_eci_1_valence.grid(row=1, column=3, sticky="w") #, sticky=W)
lbl_eci_1_valence.config(font=labelfont)
lbl_eci_4_qty = Label(S_4_frame, text="ECI 4 Qty", width=8)
lbl_eci_4_qty.grid(row=1, column=0, sticky="w")
lbl_eci_4_qty.config(font=labelfont)
lbl_eci_4_units = Label(S_4_frame, text="Units 4", width=10)
lbl_eci_4_units.grid(row=1, column=1, sticky="w") #, sticky=W)
lbl_eci_4_units.config(font=labelfont)
lbl_eci_4 = Label(S_4_frame, text="ECI 4", width=10)
lbl_eci_4.grid(row=1, column=2, sticky="w") #, sticky=W)
lbl_eci_4.config(font=labelfont)
lbl_eci_4_valence = Label(S_4_frame, text="Valence 4", width=10)
lbl_eci_4_valence.grid(row=1, column=3, sticky="w") #, sticky=W)
lbl_eci_4_valence.config(font=labelfont)
lbl_eci_4_Molar_Mass_Label = Label(S_4_frame, text="Molar Mass", width=12)
lbl_eci_4_Molar_Mass_Label.grid(row=1, column=4, sticky="w") #, sticky=W)
lbl_eci_4_Molar_Mass_Label.config(font=labelfont)
lbl_eci_4_Alpha_Label = Label(S_4_frame, text="Alpha", width=10)
lbl_eci_4_Alpha_Label.grid(row=1, column=5, sticky="w") #, sticky=W)
lbl_eci_4_Alpha_Label.config(font=labelfont)

e_eci_1_qty = Entry(S_1_frame, text="", textvariable=eci_1_qty, width=8)
e_eci_1_qty.grid(row=2, column=0, sticky="w")
e_eci_1_qty.config(font=entryfont)
e_eci_1_qty.bind('<Return>', eci_1_qty_adjusted)
cb_eci_1_units: Combobox = Combobox(S_1_frame, values=unit_values, textvariable=eci_1_units, width=10)
cb_eci_1_units.grid(row=2, column=1, sticky="w")
cb_eci_1_units.config(font=entryfont)
cb_eci_1_units.bind("<<ComboboxSelected>>", eci_1_units_selected)
cb_eci_1: Combobox = Combobox(S_1_frame, textvariable=eci_1, width=12)
cb_eci_1.grid(row=2, column=2, sticky="w")
cb_eci_1.config(font=labelfont)
cb_eci_1['values'] = element_symbol_string
cb_eci_1.bind("<<ComboboxSelected>>", setEci_1) # setSelectedItemName

cb_eci_1_valence: Combobox = Combobox(S_1_frame, textvariable=eci_1_valence, width=8)
cb_eci_1_valence.grid(row=2, column=3, sticky="w")
cb_eci_1_valence.config(font=entryfont)
cb_eci_1_valence['values'] = valences
e_eci_4_qty = Entry(S_4_frame, text="", textvariable=eci_4_qty, width=8)
e_eci_4_qty.grid(row=2, column=0, sticky="w")
e_eci_4_qty.config(font=entryfont)
e_eci_4_qty.bind('<Return>', eci_4_qty_adjusted)
cb_eci_4_units: Combobox = Combobox(S_4_frame, values=unit_values, textvariable=eci_4_units, width=10)
cb_eci_4_units.grid(row=2, column=1, sticky="w")
cb_eci_4_units.config(font=entryfont)
cb_eci_4_units.bind("<<ComboboxSelected>>", eci_units_selected)
cb_eci_4: Combobox = Combobox(S_4_frame, textvariable=eci_4, width=12)
cb_eci_4.grid(row=2, column=2, sticky="w")
cb_eci_4.config(font=entryfont)
cb_eci_4['values'] = compound_formula_string
cb_eci_4.bind("<<ComboboxSelected>>", setEci_4)
cb_eci_4_valence: Combobox = Combobox(S_4_frame, textvariable=eci_4_valence, width=5)
cb_eci_4_valence.grid(row=2, column=3, sticky="w")
cb_eci_4_valence.config(font=entryfont)
cb_eci_4_valence['values'] = valences
lbl_eci_4_Molar_Mass_Qty_label = Label(S_4_frame, text="MM Qty here", width=12)
lbl_eci_4_Molar_Mass_Qty_label.grid(row=2, column=4, sticky="w") #, sticky=W)
lbl_eci_4_Molar_Mass_Qty_label.config(font=labelfont)

e_eci_1_M_qty = Entry(S_1_frame, text="", textvariable=eci_1_M_qty, width=8)
e_eci_1_M_qty.grid(row=3, column=0, sticky="w")
e_eci_1_M_qty.config(font=entryfont)
e_eci_1_M_qty.bind('<Return>', eci_1_M_qty_adjusted)
#e_eci_1_M_qty.bind('<FocusOut>', (lambda event: check_entry_changes()))  # '''  does not work'''
lbl_eci_1_units_M = Label(S_1_frame, text="Moles", width=12)
lbl_eci_1_units_M.grid(row=3, column=1, sticky="w")
lbl_eci_1_units_M.config(font=labelfont)
# # cb_Elements1 = Combobox(root, values=elements, width=30)
cb_eci_1_N: Combobox = Combobox(S_1_frame, textvariable=eci_1_name, width=12)
cb_eci_1_N.grid(row=3, column=2, sticky="w")
cb_eci_1_N.config(font=entryfont)
cb_eci_1_N['values'] = compound_name_string
cb_eci_1_N.bind("<<ComboboxSelected>>", setSelectedItemFormula)

e_eci_4_M_qty = Entry(S_4_frame, text="", textvariable=eci_4_M_qty, width=8)
e_eci_4_M_qty.grid(row=3, column=0, sticky="w")
e_eci_4_M_qty.config(font=entryfont)
e_eci_4_M_qty.bind('<Return>', eci_4_M_qty_adjusted)
lbl_eci_4_units_M = Label(S_4_frame, text="Moles", width=10)
lbl_eci_4_units_M.grid(row=3, column=1, sticky="w")
lbl_eci_4_units_M.config(font=labelfont)
cb_eci_4_N: Combobox = Combobox(S_4_frame, values=compound_formula_string, textvariable=eci_4_name, width=12)
cb_eci_4_N.grid(row=3, column=2, sticky="w")
cb_eci_4_N.config(font=entryfont)
cb_eci_4_N.bind("<<ComboboxSelected>>", setSelectedItemFormula)

lbl_kl_Qty_1 = Label(S_1_frame, text="Liter 1 Qty", width=10)
lbl_kl_Qty_1.grid(row=4, column=0, sticky="w")
lbl_kl_Qty_1.config(font=labelfont)
lbl_kl_Units_1 = Label(S_1_frame, text="Liter 1 Units", width=10)
lbl_kl_Units_1.grid(row=4, column=1, sticky="w")
lbl_kl_Units_1.config(font=labelfont)
lbl_MM_Qty_1 = Label(S_1_frame, text="Molarity 1 Qty", width=12)
lbl_MM_Qty_1.grid(row=4, column=2, sticky="w") #, sticky=W)
lbl_MM_Qty_1.config(font=labelfont)
lbl_MM_Units_1 = Label(S_1_frame, text="Molarity 1 Units", width=12)
lbl_MM_Units_1.grid(row=4, column=3, sticky="w") #, sticky=W)
lbl_MM_Units_1.config(font=labelfont)
lbl_kl_Qty_4 = Label(S_4_frame, text="Liter 4 Qty", width=10)
lbl_kl_Qty_4.grid(row=4, column=0, sticky="w") #, sticky=W)
lbl_kl_Qty_4.config(font=labelfont)
lbl_kl_Units_4 = Label(S_4_frame, text="Liter 4 Units", width=12)
lbl_kl_Units_4.grid(row=4, column=1, sticky="w")
lbl_kl_Units_4.config(font=labelfont)
lbl_MM_Qty_4 = Label(S_4_frame, text="Molarity 4 Qty", width=12)
lbl_MM_Qty_4.grid(row=4, column=2, sticky="w") #, sticky=W)
lbl_MM_Qty_4.config(font=labelfont)
lbl_MM_Units_4 = Label(S_4_frame, text="Molarity 4 Units", width=12)
lbl_MM_Units_4.grid(row=4, column=3, sticky="w") #, sticky=W)
lbl_MM_Units_4.config(font=labelfont)

e_eci_kl_1_qty = Entry(S_1_frame, text="", textvariable=eci_kl_1_qty, width=8)
e_eci_kl_1_qty.grid(row=5, column=0, sticky="w")
e_eci_kl_1_qty.config(font=entryfont)
e_eci_kl_1_qty.bind('<Return>', e_eci_kl_1_qty_adjusted)
cb_kl_1_units: Combobox = Combobox(S_1_frame, values=kl_unit_values, textvariable=eci_1_kl_units, width=10)
cb_kl_1_units.grid(row=5, column=1, sticky="w")
cb_kl_1_units.config(font=entryfont)
cb_kl_1_units.bind("<<ComboboxSelected>>", cb_kl_1_units_selected)
e_eci_MM_1_qty = Entry(S_1_frame, text="", textvariable=eci_kl_1_qty, width=8)
e_eci_MM_1_qty.grid(row=5, column=2, sticky="w")
e_eci_MM_1_qty.config(font=entryfont)
e_eci_MM_1_qty.bind('<Return>', e_eci_MM_1_qty_adjusted)
cb_MM_1_units: Combobox = Combobox(S_1_frame, values=kl_unit_values, textvariable=eci_1_mm_units, width=10)
cb_MM_1_units.grid(row=5, column=3, sticky="w")
cb_MM_1_units.config(font=entryfont)
cb_MM_1_units.bind("<<ComboboxSelected>>", cb_MM_1_units_selected)
e_eci_kl_4_qty = Entry(S_4_frame, text="", textvariable=eci_kl_1_qty, width=8)
e_eci_kl_4_qty.grid(row=5, column=0, sticky="w")
e_eci_kl_4_qty.config(font=entryfont)
e_eci_kl_4_qty.bind('<Return>', e_eci_kl_4_qty_adjusted)
cb_kl_4_units: Combobox = Combobox(S_4_frame, values=kl_unit_values, textvariable=eci_4_kl_units, width=10)
cb_kl_4_units.grid(row=5, column=1, sticky="w")
cb_kl_4_units.config(font=entryfont)
cb_kl_4_units.bind("<<ComboboxSelected>>", cb_kl_4_units_selected)
e_eci_MM_4_qty = Entry(S_4_frame, text="", textvariable=eci_kl_4_qty, width=8)
e_eci_MM_4_qty.grid(row=5, column=2, sticky="w")
e_eci_MM_4_qty.config(font=entryfont)
e_eci_MM_4_qty.bind('<Return>', e_eci_MM_4_qty_adjusted)
cb_MM_4_units: Combobox = Combobox(S_4_frame, values=kl_unit_values, textvariable=eci_4_mm_units, width=10)
cb_MM_4_units.grid(row=5, column=3, sticky="w")
cb_MM_4_units.config(font=entryfont)
cb_MM_4_units.bind("<<ComboboxSelected>>", cb_MM_4_units_selected)

lbl_Temp_Qty_1 = Label(S_1_frame, text="Temp 1 Qty", width=10)
lbl_Temp_Qty_1.grid(row=6, column=0, sticky="w")
lbl_Temp_Qty_1.config(font=labelfont)
lbl_Temp_Units_1 = Label(S_1_frame, text="Temp 1 Units", width=12)
lbl_Temp_Units_1.grid(row=6, column=1, sticky="w")
lbl_Temp_Units_1.config(font=labelfont)
lbl_Press_Qty_1 = Label(S_1_frame, text="Press 1 Qty", width=10)
lbl_Press_Qty_1.grid(row=6, column=2, sticky="w") #, sticky=W)
lbl_Press_Qty_1.config(font=labelfont)
lbl_Press_Units_1 = Label(S_1_frame, text="Press 1 Units", width=12)
lbl_Press_Units_1.grid(row=6, column=3, sticky="w") #, sticky=W)
lbl_Press_Units_1.config(font=labelfont)
lbl_Temp_Qty_4 = Label(S_4_frame, text="Temp 4 Qty", width=10)
lbl_Temp_Qty_4.grid(row=6, column=0, sticky="w") #, sticky=W)
lbl_Temp_Qty_4.config(font=labelfont)
lbl_Temp_Units_4 = Label(S_4_frame, text="Temp 4 Units", width=10)
lbl_Temp_Units_4.grid(row=6, column=1, sticky="w")
lbl_Temp_Units_4.config(font=labelfont)
lbl_Press_Qty_4 = Label(S_4_frame, text="Press 4 Qty", width=10)
lbl_Press_Qty_4.grid(row=6, column=2, sticky="w") #, sticky=W)
lbl_Press_Qty_4.config(font=labelfont)
lbl_Press_Units_4 = Label(S_4_frame, text="Press 4 Units", width=12)
lbl_Press_Units_4.grid(row=6, column=3, sticky="w") #, sticky=W)
lbl_Press_Units_4.config(font=labelfont)

e_Temp_Qty_1 = Entry(S_1_frame, text="", textvariable=eci_temp_1_qty, width=8)
e_Temp_Qty_1.grid(row=7, column=0, sticky="w")
e_Temp_Qty_1.config(font=entryfont)
e_Temp_Qty_1.bind('<Return>', eci_1_Temp_qty_adjusted)
cb_1_Temp_Units: Combobox = Combobox(S_1_frame, values=temp_units, textvariable=eci_1_temp_units,
                                     width=10)  # eci_temp_1_units
cb_1_Temp_Units.grid(row=7, column=1, sticky="w")
cb_1_Temp_Units.config(font=entryfont)
cb_1_Temp_Units.bind("<<ComboboxSelected>>", eci_1_Temp_units_selected) #callback_set_temp_units)
e_Press_Qty_1 = Entry(S_1_frame, text="", textvariable=eci_press_1_qty, width=8)
e_Press_Qty_1.grid(row=7, column=2, sticky="w")
e_Press_Qty_1.config(font=entryfont)
cb_1_Press_Units: Combobox = Combobox(S_1_frame, values=press_units, textvariable=eci_1_press_units, width=10)
cb_1_Press_Units.grid(row=7, column=3, sticky="w")  # , padx=4)
cb_1_Press_Units.config(font=entryfont)
cb_1_Press_Units.bind("<<ComboboxSelected>>", eci_1_Press_units_selected)
e_Temp_Qty_4 = Entry(S_4_frame, text="", textvariable=eci_temp_4_qty, width=8)
e_Temp_Qty_4.grid(row=7, column=0, sticky="w") #, sticky=W)
e_Temp_Qty_4.config(font=entryfont)
cb_4_Temp_Units: Combobox = Combobox(S_4_frame, values=temp_units, textvariable=eci_4_temp_units, width=10)
cb_4_Temp_Units.grid(row=7, column=1, sticky="w")
cb_4_Temp_Units.config(font=entryfont)
cb_4_Temp_Units.bind("<<ComboboxSelected>>", eci_4_Temp_units_selected)
e_Press_Qty_4 = Entry(S_4_frame, text="", textvariable=eci_press_4_qty, width=8)
e_Press_Qty_4.grid(row=7, column=2, sticky="w")
e_Press_Qty_4.config(font=entryfont)
cb_4_Press_Units: Combobox = Combobox(S_4_frame, values=press_units, textvariable=eci_4_press_units, width=10)
cb_4_Press_Units.grid(row=7, column=3, sticky="w")
cb_4_Press_Units.config(font=entryfont)
cb_4_Press_Units.bind("<<ComboboxSelected>>", eci_units_selected)

lbl_Heat_Qty_1 = Label(S_1_frame, text="Heat 1 Qty", width=10)
lbl_Heat_Qty_1.grid(row=8, column=0, sticky="w")
lbl_Heat_Qty_1.config(font=labelfont)
lbl_Heat_Units_1 = Label(S_1_frame, text="Heat 1 Units", width=10)
lbl_Heat_Units_1.grid(row=8, column=1, sticky="w")
lbl_Heat_Units_1.config(font=labelfont)
lbl_Other_Qty_1 = Label(S_1_frame, text="Other 1 Qty", width=10)
lbl_Other_Qty_1.grid(row=8, column=2, sticky="w") #, sticky=W)
lbl_Other_Qty_1.config(font=labelfont)
lbl_Other_Units_1 = Label(S_1_frame, text="Other 1 Units", width=10)
lbl_Other_Units_1.grid(row=8, column=3, sticky="w") #, sticky=W)
lbl_Other_Units_1.config(font=labelfont)
lbl_Heat_Qty_4 = Label(S_4_frame, text="Heat 4 Qty", width=10)
lbl_Heat_Qty_4.grid(row=8, column=0, sticky="w")
lbl_Heat_Qty_4.config(font=labelfont)
lbl_Heat_Units_4 = Label(S_4_frame, text="Heat 4 Units", width=10)
lbl_Heat_Units_4.grid(row=8, column=1, sticky="w")
lbl_Heat_Units_4.config(font=labelfont)
lbl_Other_Qty_4 = Label(S_4_frame, text="Other 4 Qty", width=10)
lbl_Other_Qty_4.grid(row=8, column=2, sticky="w") #, sticky=W)
lbl_Other_Qty_4.config(font=labelfont)
lbl_Other_Units_4 = Label(S_4_frame, text="Other 4 Units", width=10)
lbl_Other_Units_4.grid(row=8, column=3, sticky="w") #, sticky=W)
lbl_Other_Units_4.config(font=labelfont)

e_Heat_Qty_1 = Entry(S_1_frame, text="", textvariable=eci_heat_1_qty, width=8)
e_Heat_Qty_1.grid(row=9, column=0, sticky="w")
e_Heat_Qty_1.config(font=entryfont)
e_Heat_Qty_1.bind('<Return>', eci_1_Temp_qty_adjusted)
cb_1_Heat_Units: Combobox = Combobox(S_1_frame, values=heat_units,
                                     textvariable=eci_1_heat_units, width=10)  
cb_1_Heat_Units.config(font=entryfont)
cb_1_Heat_Units.grid(row=9, column=1, sticky="w")
cb_1_Heat_Units.bind("<<ComboboxSelected>>", eci_units_selected) #callback_set_temp_units)
e_Other_Qty_1 = Entry(S_1_frame, text="", textvariable=other_1_qty, width=8)
e_Other_Qty_1.grid(row=9, column=2, sticky="w")
e_Other_Qty_1.config(font=entryfont)
cb_1_Other_Units: Combobox = Combobox(S_1_frame, values=other_units, textvariable=other_1_units , width=10)
cb_1_Other_Units.grid(row=9, column=3, sticky="w")  # , padx=4)
cb_1_Other_Units.config(font=entryfont)
cb_1_Other_Units.bind("<<ComboboxSelected>>", eci_units_selected) #callback_set_press_units)
e_Heat_Qty_4 = Entry(S_4_frame, text="", textvariable=eci_heat_4_qty, width=8)
e_Heat_Qty_4.grid(row=9, column=0, sticky="w")
e_Heat_Qty_4.config(font=entryfont)
e_Heat_Qty_4.bind('<Return>', eci_4_Temp_qty_adjusted)
cb_4_Heat_Units: Combobox = Combobox(S_4_frame, values=heat_units, textvariable=eci_4_heat_units,
                                     width=10) 
cb_4_Heat_Units.grid(row=9, column=1, sticky="w")
cb_4_Heat_Units.config(font=entryfont)
cb_4_Heat_Units.bind("<<ComboboxSelected>>", eci_units_selected) #callback_set_temp_units)
e_Other_Qty_4 = Entry(S_4_frame, text="", textvariable=other_4_qty, width=8)
e_Other_Qty_4.grid(row=9, column=2, sticky="w")
e_Other_Qty_4.config(font=entryfont)
cb_4_Other_Units: Combobox = Combobox(S_4_frame, values=other_units, textvariable=other_4_units, width=10)
cb_4_Other_Units.grid(row=9, column=3, sticky="w")  # , padx=4)
cb_4_Other_Units.config(font=entryfont)
cb_4_Other_Units.bind("<<ComboboxSelected>>", eci_units_selected)

# ###

lbl_blank = Label(inside_frame, text="")
lbl_blank.grid(row=10, column=0, columnspan=16, sticky="w")

lbl_eci_2 = Label(S_2_frame, text="Select Element, Compound or Ion for ComboBox 2")
lbl_eci_2.grid(row=0, column=0, columnspan=3, sticky="w") #, sticky=W)
lbl_eci_2.config(font=labelfont)
cb_Select_CB2: Combobox = Combobox(S_2_frame, values=eci_cb_values, width=10)
cb_Select_CB2.grid(row=0, column=4, sticky="w") #, sticky=W)
cb_Select_CB2.config(font=entryfont)
cb_Select_CB2.bind("<<ComboboxSelected>>", select_eci_2_type)
lbl_eci_5 = Label(S_5_frame, text="Select Element, Compound or Ion for ComboBox 5") # , bg="BLUE"
lbl_eci_5.grid(row=0, column=0, columnspan=3, sticky="nw") #, sticky=W)
lbl_eci_5.config(font=labelfont)
cb_Select_CB5 = Combobox(S_5_frame, values=eci_cb_values, width=10)
cb_Select_CB5.grid(row=0, column=4, sticky="nw")
cb_Select_CB5.config(font=entryfont)
cb_Select_CB5.bind("<<ComboboxSelected>>", select_eci_5_type)

lbl_eci_2_qty = Label(S_2_frame, text="ECI 2 Qty", width=10)
lbl_eci_2_qty.grid(row=1, column=0, sticky="w")
lbl_eci_2_qty.config(font=labelfont)
lbl_eci_2_units = Label(S_2_frame, text="Units 2", width=10)
lbl_eci_2_units.grid(row=1, column=1, sticky="w") #, sticky=W)
lbl_eci_2_units.config(font=labelfont)
lbl_eci_2 = Label(S_2_frame, text="ECI 2", width=10)
lbl_eci_2.grid(row=1, column=2, sticky="w") #, sticky=W)
lbl_eci_2.config(font=labelfont)
lbl_eci_2_valence = Label(S_2_frame, text="Valence 2", width=10)
lbl_eci_2_valence.grid(row=1, column=3, sticky="w") #, sticky=W)
lbl_eci_2_valence.config(font=labelfont)
lbl_eci_5_qty = Label(S_5_frame, text="ECI 5 Qty", width=8)
lbl_eci_5_qty.grid(row=1, column=0, sticky="nw")
lbl_eci_5_qty.config(font=labelfont)
lbl_eci_5_units = Label(S_5_frame, text="Units 5", width=10)
lbl_eci_5_units.grid(row=1, column=1, sticky="nw") #, sticky=W)
lbl_eci_5_units.config(font=labelfont)
lbl_eci_5 = Label(S_5_frame, text="ECI 5", width=10)
lbl_eci_5.grid(row=1, column=2, sticky="w") #, sticky=W)
lbl_eci_5.config(font=labelfont)
lbl_eci_5_valence = Label(S_5_frame, text="Valence 5", width=10)
lbl_eci_5_valence.grid(row=1, column=3, sticky="w") #, sticky=W)
lbl_eci_5_valence.config(font=labelfont)
lbl_eci_5_Molar_Mass_Label = Label(S_5_frame, text="Molar Mass", width=12)
lbl_eci_5_Molar_Mass_Label.grid(row=1, column=4, sticky="w") #, sticky=W)
lbl_eci_5_Molar_Mass_Label.config(font=labelfont)
lbl_eci_5_Alpha_Label = Label(S_5_frame, text="Alpha", width=10)
lbl_eci_5_Alpha_Label.grid(row=1, column=5, sticky="w") #, sticky=W)
lbl_eci_5_Alpha_Label.config(font=labelfont)
e_eci_2_qty = Entry(S_2_frame, text="", textvariable=eci_2_qty, width=8)
e_eci_2_qty.grid(row=2, column=0, sticky="w")
e_eci_2_qty.config(font=entryfont)
e_eci_2_qty.bind('<Return>', eci_2_qty_adjusted)
cb_eci_2_units: Combobox = Combobox(S_2_frame, values=unit_values, textvariable=eci_2_units, width=10)
cb_eci_2_units.grid(row=2, column=1, sticky="w")
cb_eci_2_units.config(font=entryfont)
cb_eci_2_units.bind("<<ComboboxSelected>>", eci_2_units_selected)
cb_eci_2: Combobox = Combobox(S_2_frame, textvariable=eci_2, width=12)
cb_eci_2.grid(row=2, column=2, sticky="w")
cb_eci_2.config(font=labelfont)
cb_eci_2['values'] = element_symbol_string
cb_eci_2.bind("<<ComboboxSelected>>", setEci_2) # setSelectedItemName

cb_eci_2_valence: Combobox = Combobox(S_2_frame, textvariable=eci_2_valence, width=8)
cb_eci_2_valence.grid(row=2, column=3, sticky="w")
cb_eci_2_valence.config(font=entryfont)
cb_eci_2_valence['values'] = valences
e_eci_5_qty = Entry(S_5_frame, text="", textvariable=eci_5_qty, width=8)
e_eci_5_qty.grid(row=2, column=0, sticky="w")
e_eci_5_qty.config(font=entryfont)
e_eci_5_qty.bind('<Return>', eci_5_qty_adjusted)
cb_eci_5_units: Combobox = Combobox(S_5_frame, values=unit_values, textvariable=eci_5_units, width=10)
cb_eci_5_units.grid(row=2, column=1, sticky="w")
cb_eci_5_units.config(font=entryfont)
cb_eci_5_units.bind("<<ComboboxSelected>>", eci_units_selected)
cb_eci_5: Combobox = Combobox(S_5_frame, textvariable=eci_5, width=12)
cb_eci_5.grid(row=2, column=2, sticky="w")
cb_eci_5.config(font=entryfont)
cb_eci_5['values'] = element_symbol_string
cb_eci_5.bind("<<ComboboxSelected>>", setEci_5)
cb_eci_5_valence: Combobox = Combobox(S_5_frame, textvariable=eci_5_valence, width=5)
cb_eci_5_valence.grid(row=2, column=3, sticky="w")
cb_eci_5_valence.config(font=entryfont)
cb_eci_5_valence['values'] = valences
lbl_eci_5_Molar_Mass_Qty_label = Label(S_5_frame, text="MM Qty here", width=12)
lbl_eci_5_Molar_Mass_Qty_label.grid(row=2, column=4, sticky="w") #, sticky=W)
lbl_eci_5_Molar_Mass_Qty_label.config(font=labelfont)

e_eci_2_M_qty = Entry(S_2_frame, text="", textvariable=eci_2_M_qty, width=8)
e_eci_2_M_qty.grid(row=3, column=0, sticky="w")
e_eci_2_M_qty.config(font=entryfont)
e_eci_2_M_qty.bind('<Return>', eci_2_M_qty_adjusted)
lbl_eci_2_units_M = Label(S_2_frame, text="Moles", width=12)
lbl_eci_2_units_M.grid(row=3, column=1, sticky="w")
lbl_eci_2_units_M.config(font=labelfont)
# # cb_Elements1 = Combobox(root, values=elements, width=30)
cb_eci_2_N: Combobox = Combobox(S_2_frame, textvariable=eci_2_name, width=12)
cb_eci_2_N.grid(row=3, column=2, sticky="w")
cb_eci_2_N.config(font=entryfont)
cb_eci_2_N['values'] = compound_name_string
cb_eci_2_N.bind("<<ComboboxSelected>>", setSelectedItemFormula)

e_eci_5_M_qty = Entry(S_5_frame, text="", textvariable=eci_5_M_qty, width=8)
e_eci_5_M_qty.grid(row=3, column=0, sticky="w")
e_eci_5_M_qty.config(font=entryfont)
e_eci_5_M_qty.bind('<Return>', eci_5_M_qty_adjusted)
lbl_eci_5_units_M = Label(S_5_frame, text="Moles", width=10)
lbl_eci_5_units_M.grid(row=3, column=1, sticky="w")
lbl_eci_5_units_M.config(font=labelfont)
cb_eci_5_N: Combobox = Combobox(S_5_frame, values=compound_formula_string, textvariable=eci_5_name, width=12)
cb_eci_5_N.grid(row=3, column=2, sticky="w")
cb_eci_5_N.config(font=entryfont)
cb_eci_5_N.bind("<<ComboboxSelected>>", setSelectedItemFormula)

lbl_kl_Qty_2 = Label(S_2_frame, text="Liter 2 Qty", width=10)
lbl_kl_Qty_2.grid(row=4, column=0, sticky="w")
lbl_kl_Qty_2.config(font=labelfont)
lbl_kl_Units_2 = Label(S_2_frame, text="Liter 2 Units", width=10)
lbl_kl_Units_2.grid(row=4, column=1, sticky="w")
lbl_kl_Units_2.config(font=labelfont)
lbl_MM_Qty_2 = Label(S_2_frame, text="Molarity 2 Qty", width=12)
lbl_MM_Qty_2.grid(row=4, column=2, sticky="w") #, sticky=W)
lbl_MM_Qty_2.config(font=labelfont)
lbl_MM_Units_2 = Label(S_2_frame, text="Molarity 2 Units", width=12)
lbl_MM_Units_2.grid(row=4, column=3, sticky="w") #, sticky=W)
lbl_MM_Units_2.config(font=labelfont)
lbl_kl_Qty_5 = Label(S_5_frame, text="Liter 5 Qty", width=10)
lbl_kl_Qty_5.grid(row=4, column=0, sticky="w") #, sticky=W)
lbl_kl_Qty_5.config(font=labelfont)
lbl_kl_Units_5 = Label(S_5_frame, text="Liter 5 Units", width=12)
lbl_kl_Units_5.grid(row=4, column=1, sticky="w")
lbl_kl_Units_5.config(font=labelfont)
lbl_MM_Qty_5 = Label(S_5_frame, text="Molarity 5 Qty", width=12)
lbl_MM_Qty_5.grid(row=4, column=2, sticky="w") #, sticky=W)
lbl_MM_Qty_5.config(font=labelfont)
lbl_MM_Units_5 = Label(S_5_frame, text="Molarity 5 Units", width=12)
lbl_MM_Units_5.grid(row=4, column=3, sticky="w") #, sticky=W)
lbl_MM_Units_5.config(font=labelfont)

e_eci_kl_2_qty = Entry(S_2_frame, text="", textvariable=eci_kl_2_qty, width=8)
e_eci_kl_2_qty.grid(row=5, column=0, sticky="w")
e_eci_kl_2_qty.config(font=entryfont)
e_eci_kl_2_qty.bind('<Return>', e_eci_kl_2_qty_adjusted)
cb_kl_2_units: Combobox = Combobox(S_2_frame, values=kl_unit_values, textvariable=eci_2_kl_units, width=10)
cb_kl_2_units.grid(row=5, column=1, sticky="w")
cb_kl_2_units.config(font=entryfont)
cb_kl_2_units.bind("<<ComboboxSelected>>", cb_kl_2_units_selected)
e_eci_MM_2_qty = Entry(S_2_frame, text="", textvariable=eci_kl_2_qty, width=8)
e_eci_MM_2_qty.grid(row=5, column=2, sticky="w")
e_eci_MM_2_qty.config(font=entryfont)
e_eci_MM_2_qty.bind('<Return>', e_eci_MM_2_qty_adjusted)
cb_MM_2_units: Combobox = Combobox(S_2_frame, values=kl_unit_values, textvariable=eci_2_mm_units, width=10)
cb_MM_2_units.grid(row=5, column=3, sticky="w")
cb_MM_2_units.config(font=entryfont)
cb_MM_2_units.bind("<<ComboboxSelected>>", cb_MM_2_units_selected)
e_eci_kl_5_qty = Entry(S_5_frame, text="", textvariable=eci_kl_1_qty, width=8)
e_eci_kl_5_qty.grid(row=5, column=0, sticky="w")
e_eci_kl_5_qty.config(font=entryfont)
e_eci_kl_5_qty.bind('<Return>', e_eci_kl_5_qty_adjusted)
cb_kl_5_units: Combobox = Combobox(S_5_frame, values=kl_unit_values, textvariable=eci_5_kl_units, width=10)
cb_kl_5_units.grid(row=5, column=1, sticky="w")
cb_kl_5_units.config(font=entryfont)
cb_kl_5_units.bind("<<ComboboxSelected>>", cb_kl_1_units_selected)
e_eci_MM_5_qty = Entry(S_5_frame, text="", textvariable=eci_kl_5_qty, width=8)
e_eci_MM_5_qty.grid(row=5, column=2, sticky="w")
e_eci_MM_5_qty.config(font=entryfont)
e_eci_MM_5_qty.bind('<Return>', e_eci_MM_5_qty_adjusted)
cb_MM_5_units: Combobox = Combobox(S_5_frame, values=kl_unit_values, textvariable=eci_5_mm_units, width=10)
cb_MM_5_units.grid(row=5, column=3, sticky="w")
cb_MM_5_units.config(font=entryfont)
cb_MM_5_units.bind("<<ComboboxSelected>>", cb_kl_5_units_selected)

lbl_Temp_Qty_2 = Label(S_2_frame, text="Temp 2 Qty", width=10)
lbl_Temp_Qty_2.grid(row=6, column=0, sticky="w")
lbl_Temp_Qty_2.config(font=labelfont)
lbl_Temp_Units_2 = Label(S_2_frame, text="Temp 2 Units", width=12)
lbl_Temp_Units_2.grid(row=6, column=1, sticky="w")
lbl_Temp_Units_2.config(font=labelfont)
lbl_Press_Qty_2 = Label(S_2_frame, text="Press 2 Qty", width=10)
lbl_Press_Qty_2.grid(row=6, column=2, sticky="w") #, sticky=W)
lbl_Press_Qty_2.config(font=labelfont)
lbl_Press_Units_2 = Label(S_2_frame, text="Press 2 Units", width=12)
lbl_Press_Units_2.grid(row=6, column=3, sticky="w") #, sticky=W)
lbl_Press_Units_2.config(font=labelfont)
lbl_Temp_Qty_5 = Label(S_5_frame, text="Temp 5 Qty", width=10)
lbl_Temp_Qty_5.grid(row=6, column=0, sticky="w") #, sticky=W)
lbl_Temp_Qty_5.config(font=labelfont)
lbl_Temp_Units_5 = Label(S_5_frame, text="Temp 5 Units", width=10)
lbl_Temp_Units_5.grid(row=6, column=1, sticky="w")
lbl_Temp_Units_5.config(font=labelfont)
lbl_Press_Qty_5 = Label(S_5_frame, text="Press 5 Qty", width=10)
lbl_Press_Qty_5.grid(row=6, column=2, sticky="w") #, sticky=W)
lbl_Press_Qty_5.config(font=labelfont)
lbl_Press_Units_5 = Label(S_5_frame, text="Press 5 Units", width=12)
lbl_Press_Units_5.grid(row=6, column=3, sticky="w") #, sticky=W)
lbl_Press_Units_5.config(font=labelfont)

e_Temp_Qty_2 = Entry(S_2_frame, text="", textvariable=eci_temp_2_qty, width=8)
e_Temp_Qty_2.grid(row=7, column=0, sticky="w")
e_Temp_Qty_2.config(font=entryfont)
e_Temp_Qty_2.bind('<Return>', eci_2_Temp_qty_adjusted)
cb_2_Temp_Units: Combobox = Combobox(S_2_frame, values=temp_units, textvariable=eci_2_temp_units,
                                     width=10)  # eci_temp_1_units
cb_2_Temp_Units.grid(row=7, column=1, sticky="w")
cb_2_Temp_Units.config(font=entryfont)
cb_2_Temp_Units.bind("<<ComboboxSelected>>", eci_2_Temp_units_selected) #callback_set_temp_units)
e_Press_Qty_2 = Entry(S_2_frame, text="", textvariable=eci_press_2_qty, width=8)
e_Press_Qty_2.grid(row=7, column=2, sticky="w")
e_Press_Qty_2.config(font=entryfont)
cb_2_Press_Units: Combobox = Combobox(S_2_frame, values=press_units, textvariable=eci_2_press_units, width=10)
cb_2_Press_Units.grid(row=7, column=3, sticky="w")  # , padx=4)
cb_2_Press_Units.config(font=entryfont)
cb_2_Press_Units.bind("<<ComboboxSelected>>", eci_units_selected) #callback_set_press_units)
e_Temp_Qty_5 = Entry(S_5_frame, text="", textvariable=eci_temp_5_qty, width=8)
e_Temp_Qty_5.grid(row=7, column=0, sticky="w") #, sticky=W)
e_Temp_Qty_5.config(font=entryfont)
cb_5_Temp_Units: Combobox = Combobox(S_5_frame, values=temp_units, textvariable=eci_5_temp_units, width=10)
cb_5_Temp_Units.grid(row=7, column=1, sticky="w")
cb_5_Temp_Units.config(font=entryfont)
cb_5_Temp_Units.bind("<<ComboboxSelected>>", eci_5_Temp_units_selected)
e_Press_Qty_5 = Entry(S_5_frame, text="", textvariable=eci_press_5_qty, width=8)
e_Press_Qty_5.grid(row=7, column=2, sticky="w")
e_Press_Qty_5.config(font=entryfont)
cb_5_Press_Units: Combobox = Combobox(S_5_frame, values=press_units, textvariable=eci_5_press_units, width=10)
cb_5_Press_Units.grid(row=7, column=3, sticky="w")
cb_5_Press_Units.config(font=entryfont)
cb_5_Press_Units.bind("<<ComboboxSelected>>", eci_units_selected)

lbl_Heat_Qty_2 = Label(S_2_frame, text="Heat 2 Qty", width=10)
lbl_Heat_Qty_2.grid(row=8, column=0, sticky="w")
lbl_Heat_Qty_2.config(font=labelfont)
lbl_Heat_Units_2 = Label(S_2_frame, text="Heat 2 Units", width=10)
lbl_Heat_Units_2.grid(row=8, column=1, sticky="w")
lbl_Heat_Units_2.config(font=labelfont)
lbl_Other_Qty_2 = Label(S_2_frame, text="Other 2 Qty", width=10)
lbl_Other_Qty_2.grid(row=8, column=2, sticky="w") #, sticky=W)
lbl_Other_Qty_2.config(font=labelfont)
lbl_Other_Units_2 = Label(S_2_frame, text="Other 2 Units", width=10)
lbl_Other_Units_2.grid(row=8, column=3, sticky="w") #, sticky=W)
lbl_Other_Units_2.config(font=labelfont)
lbl_Heat_Qty_5 = Label(S_5_frame, text="Heat 5 Qty", width=10)
lbl_Heat_Qty_5.grid(row=8, column=0, sticky="w")
lbl_Heat_Qty_5.config(font=labelfont)
lbl_Heat_Units_5 = Label(S_5_frame, text="Heat 5 Units", width=10)
lbl_Heat_Units_5.grid(row=8, column=1, sticky="w")
lbl_Heat_Units_5.config(font=labelfont)
lbl_Other_Qty_5 = Label(S_5_frame, text="Other 5 Qty", width=10)
lbl_Other_Qty_5.grid(row=8, column=2, sticky="w") #, sticky=W)
lbl_Other_Qty_5.config(font=labelfont)
lbl_Other_Units_5 = Label(S_5_frame, text="Other 5 Units", width=10)
lbl_Other_Units_5.grid(row=8, column=3, sticky="w") #, sticky=W)
lbl_Other_Units_5.config(font=labelfont)

e_Heat_Qty_2 = Entry(S_2_frame, text="", textvariable=eci_heat_2_qty, width=8)
e_Heat_Qty_2.grid(row=9, column=0, sticky="w")
e_Heat_Qty_2.config(font=entryfont)
e_Heat_Qty_2.bind('<Return>', eci_2_Temp_qty_adjusted)
cb_2_Heat_Units: Combobox = Combobox(S_2_frame, values=heat_units, textvariable=eci_2_heat_units,
                                     width=10)  # eci_temp_1_units
cb_2_Heat_Units.grid(row=9, column=1, sticky="w")
cb_2_Heat_Units.config(font=entryfont)
cb_2_Heat_Units.bind("<<ComboboxSelected>>", eci_units_selected) #callback_set_temp_units)
e_Other_Qty_2 = Entry(S_2_frame, text="", textvariable=other_2_qty, width=8)
e_Other_Qty_2.grid(row=9, column=2, sticky="w")
e_Other_Qty_2.config(font=entryfont)
cb_2_Other_Units: Combobox = Combobox(S_2_frame, values=other_units, textvariable=other_2_units, width=10)
cb_2_Other_Units.grid(row=9, column=3, sticky="w")  # , padx=4)
cb_2_Other_Units.config(font=entryfont)
cb_2_Other_Units.bind("<<ComboboxSelected>>", eci_units_selected) #callback_set_press_units)
e_Heat_Qty_5 = Entry(S_5_frame, text="", textvariable=eci_heat_5_qty, width=8)
e_Heat_Qty_5.grid(row=9, column=0, sticky="w")
e_Heat_Qty_5.config(font=entryfont)
e_Heat_Qty_5.bind('<Return>', eci_5_Temp_qty_adjusted)
cb_5_Heat_Units: Combobox = Combobox(S_5_frame, values=heat_units, textvariable=eci_2_heat_units,
                                     width=10) 
cb_5_Heat_Units.grid(row=9, column=1, sticky="w")
cb_5_Heat_Units.config(font=entryfont)
cb_5_Heat_Units.bind("<<ComboboxSelected>>", eci_units_selected) #callback_set_temp_units)
e_Other_Qty_5 = Entry(S_5_frame, text="", textvariable=other_5_qty, width=8)
e_Other_Qty_5.grid(row=9, column=2, sticky="w")
e_Other_Qty_5.config(font=entryfont)
cb_5_Other_Units: Combobox = Combobox(S_5_frame, values=other_units, textvariable=other_5_units, width=10)
cb_5_Other_Units.grid(row=9, column=3, sticky="w")  # , padx=4)
cb_5_Other_Units.config(font=entryfont)
cb_5_Other_Units.bind("<<ComboboxSelected>>", eci_units_selected)

# lbl_blank = Label(inside_frame, text="")
# lbl_blank.grid(row=10, column=0)

lbl_eci_3 = Label(S_3_frame, text="Select Element, Compound or Ion for ComboBox 3")
lbl_eci_3.grid(row=0, column=0, columnspan=3, sticky="w")
lbl_eci_3.config(font=labelfont)
cb_Select_CB3: Combobox = Combobox(S_3_frame, values=eci_cb_values, width=10)
cb_Select_CB3.grid(row=0, column=4, sticky="w")
cb_Select_CB3.config(font=entryfont)
cb_Select_CB3.bind("<<ComboboxSelected>>", select_eci_3_type)
lbl_eci_6 = Label(S_6_frame, text="Select Element, Compound or Ion for ComboBox 6") # , bg="BLUE"
lbl_eci_6.grid(row=0, column=0, columnspan=3, sticky="nw") #, sticky=W)
lbl_eci_6.config(font=labelfont)
cb_Select_CB6 = Combobox(S_6_frame, values=eci_cb_values, width=10)
cb_Select_CB6.grid(row=0, column=4, sticky="nw")
cb_Select_CB6.config(font=entryfont)
cb_Select_CB6.bind("<<ComboboxSelected>>", select_eci_6_type)

lbl_eci_3_qty = Label(S_3_frame, text="ECI 3 Qty", width=10)
lbl_eci_3_qty.grid(row=1, column=0, sticky="w")
lbl_eci_3_qty.config(font=labelfont)
lbl_eci_3_units = Label(S_3_frame, text="Units 3", width=10)
lbl_eci_3_units.grid(row=1, column=1, sticky="w") #, sticky=W)
lbl_eci_3_units.config(font=labelfont)
lbl_eci_3 = Label(S_3_frame, text="ECI 3", width=10)
lbl_eci_3.grid(row=1, column=2, sticky="w") #, sticky=W)
lbl_eci_3.config(font=labelfont)
lbl_eci_3_valence = Label(S_3_frame, text="Valence 3", width=10)
lbl_eci_3_valence.grid(row=1, column=3, sticky="w") #, sticky=W)
lbl_eci_3_valence.config(font=labelfont)
lbl_eci_6_qty = Label(S_6_frame, text="ECI 6 Qty", width=8)
lbl_eci_6_qty.grid(row=1, column=0, sticky="w")
lbl_eci_6_qty.config(font=labelfont)
lbl_eci_6_units = Label(S_6_frame, text="Units 6", width=10)
lbl_eci_6_units.grid(row=1, column=1, sticky="w") #, sticky=W)
lbl_eci_6_units.config(font=labelfont)
lbl_eci_6 = Label(S_6_frame, text="ECI 6", width=10)
lbl_eci_6.grid(row=1, column=2, sticky="w") #, sticky=W)
lbl_eci_6.config(font=labelfont)
lbl_eci_6_valence = Label(S_6_frame, text="Valence 6", width=10)
lbl_eci_6_valence.grid(row=1, column=3, sticky="w") #, sticky=W)
lbl_eci_6_valence.config(font=labelfont)
lbl_eci_6_Molar_Mass_Label = Label(S_6_frame, text="Molar Mass", width=12)
lbl_eci_6_Molar_Mass_Label.grid(row=1, column=4, sticky="w") #, sticky=W)
lbl_eci_6_Molar_Mass_Label.config(font=labelfont)
lbl_eci_6_Alpha_Label = Label(S_6_frame, text="Alpha", width=10)
lbl_eci_6_Alpha_Label.grid(row=1, column=5, sticky="w") #, sticky=W)
lbl_eci_6_Alpha_Label.config(font=labelfont)

e_eci_3_qty = Entry(S_3_frame, text="", textvariable=eci_3_qty, width=8)
e_eci_3_qty.grid(row=2, column=0, sticky="w")
e_eci_3_qty.config(font=entryfont)
e_eci_3_qty.bind('<Return>', eci_3_qty_adjusted)
cb_eci_3_units: Combobox = Combobox(S_3_frame, values=unit_values, textvariable=eci_3_units, width=10)
cb_eci_3_units.grid(row=2, column=1, sticky="w")
cb_eci_3_units.config(font=entryfont)
cb_eci_3_units.bind("<<ComboboxSelected>>", eci_3_units_selected)
cb_eci_3: Combobox = Combobox(S_3_frame, textvariable=eci_3, width=12)
cb_eci_3.grid(row=2, column=2, sticky="w")
cb_eci_3.config(font=labelfont)
cb_eci_3['values'] = element_symbol_string
cb_eci_3.bind("<<ComboboxSelected>>", setEci_3) # setSelectedItemName

cb_eci_3_valence: Combobox = Combobox(S_3_frame, textvariable=eci_3_valence, width=8)
cb_eci_3_valence.grid(row=2, column=3, sticky="w")
cb_eci_3_valence.config(font=entryfont)
cb_eci_3_valence['values'] = valences
e_eci_6_qty = Entry(S_6_frame, text="", textvariable=eci_6_qty, width=8)
e_eci_6_qty.grid(row=2, column=0, sticky="w")
e_eci_6_qty.config(font=entryfont)
e_eci_6_qty.bind('<Return>', eci_6_qty_adjusted)
cb_eci_6_units: Combobox = Combobox(S_6_frame, values=unit_values, textvariable=eci_6_units, width=10)
cb_eci_6_units.grid(row=2, column=1, sticky="w")
cb_eci_6_units.config(font=entryfont)
cb_eci_6_units.bind("<<ComboboxSelected>>", eci_units_selected)
cb_eci_6: Combobox = Combobox(S_6_frame, textvariable=eci_6, width=12)
cb_eci_6.grid(row=2, column=2, sticky="w")
cb_eci_6.config(font=entryfont)
cb_eci_6['values'] = element_symbol_string
cb_eci_6.bind("<<ComboboxSelected>>", setEci_6)
cb_eci_6_valence: Combobox = Combobox(S_6_frame, textvariable=eci_6_valence, width=5)
cb_eci_6_valence.grid(row=2, column=3, sticky="w")
cb_eci_6_valence.config(font=entryfont)
cb_eci_6_valence['values'] = valences
lbl_eci_6_Molar_Mass_Qty_label = Label(S_6_frame, text="MM Qty here", width=12)
lbl_eci_6_Molar_Mass_Qty_label.grid(row=2, column=4, sticky="w") #, sticky=W)
lbl_eci_6_Molar_Mass_Qty_label.config(font=labelfont)

e_eci_3_M_qty = Entry(S_3_frame, text="", textvariable=eci_3_M_qty, width=8)
e_eci_3_M_qty.grid(row=3, column=0, sticky="w")
e_eci_3_M_qty.config(font=entryfont)
e_eci_3_M_qty.bind('<Return>', eci_3_M_qty_adjusted)
lbl_eci_3_units_M = Label(S_3_frame, text="Moles", width=12)
lbl_eci_3_units_M.grid(row=3, column=1, sticky="w")
lbl_eci_3_units_M.config(font=labelfont)
# # cb_Elements1 = Combobox(root, values=elements, width=30)
cb_eci_3_N: Combobox = Combobox(S_3_frame, textvariable=eci_3_name, width=12)
cb_eci_3_N.grid(row=3, column=2, sticky="w")
cb_eci_3_N.config(font=entryfont)
cb_eci_3_N['values'] = compound_name_string
cb_eci_3_N.bind("<<ComboboxSelected>>", setSelectedItemFormula)

e_eci_6_M_qty = Entry(S_6_frame, text="", textvariable=eci_6_M_qty, width=8)
e_eci_6_M_qty.grid(row=3, column=0, sticky="w")
e_eci_6_M_qty.config(font=entryfont)
e_eci_6_M_qty.bind('<Return>', eci_6_M_qty_adjusted)
lbl_eci_6_units_M = Label(S_6_frame, text="Moles", width=10)
lbl_eci_6_units_M.grid(row=3, column=1, sticky="w")
lbl_eci_6_units_M.config(font=labelfont)
cb_eci_6_N: Combobox = Combobox(S_6_frame, values=compound_formula_string, textvariable=eci_6_name, width=12)
cb_eci_6_N.grid(row=3, column=2, sticky="w")
cb_eci_6_N.config(font=entryfont)
cb_eci_6_N.bind("<<ComboboxSelected>>", setSelectedItemFormula)

lbl_kl_Qty_3 = Label(S_3_frame, text="Liter 3 Qty", width=10)
lbl_kl_Qty_3.grid(row=4, column=0, sticky="w")
lbl_kl_Qty_3.config(font=labelfont)
lbl_kl_Units_3 = Label(S_3_frame, text="Liter 3 Units", width=10)
lbl_kl_Units_3.grid(row=4, column=1, sticky="w")
lbl_kl_Units_3.config(font=labelfont)
lbl_MM_Qty_3 = Label(S_3_frame, text="Molarity 3 Qty", width=12)
lbl_MM_Qty_3.grid(row=4, column=2, sticky="w") #, sticky=W)
lbl_MM_Qty_3.config(font=labelfont)
lbl_MM_Units_3 = Label(S_3_frame, text="Molarity 3 Units", width=12)
lbl_MM_Units_3.grid(row=4, column=3, sticky="w") #, sticky=W)
lbl_MM_Units_3.config(font=labelfont)
lbl_kl_Qty_6 = Label(S_6_frame, text="Liter 6 Qty", width=10)
lbl_kl_Qty_6.grid(row=4, column=0, sticky="w") #, sticky=W)
lbl_kl_Qty_6.config(font=labelfont)
lbl_kl_Units_6 = Label(S_6_frame, text="Liter 6 Units", width=12)
lbl_kl_Units_6.grid(row=4, column=1, sticky="w")
lbl_kl_Units_6.config(font=labelfont)
lbl_MM_Qty_6 = Label(S_6_frame, text="Molarity 6 Qty", width=12)
lbl_MM_Qty_6.grid(row=4, column=2, sticky="w") #, sticky=W)
lbl_MM_Qty_6.config(font=labelfont)
lbl_MM_Units_6 = Label(S_6_frame, text="Molarity 6 Units", width=12)
lbl_MM_Units_6.grid(row=4, column=3, sticky="w") #, sticky=W)
lbl_MM_Units_6.config(font=labelfont)

e_eci_kl_3_qty = Entry(S_3_frame, text="", textvariable=eci_kl_3_qty, width=8)
e_eci_kl_3_qty.grid(row=5, column=0, sticky="w")
e_eci_kl_3_qty.config(font=entryfont)
e_eci_kl_3_qty.bind('<Return>', e_eci_kl_3_qty_adjusted)
cb_kl_3_units: Combobox = Combobox(S_3_frame, values=kl_unit_values, textvariable=eci_3_kl_units, width=10)
cb_kl_3_units.grid(row=5, column=1, sticky="w")
cb_kl_3_units.config(font=entryfont)
cb_kl_3_units.bind("<<ComboboxSelected>>", cb_kl_2_units_selected)
e_eci_MM_3_qty = Entry(S_3_frame, text="", textvariable=eci_kl_3_qty, width=8)
e_eci_MM_3_qty.grid(row=5, column=2, sticky="w")
e_eci_MM_3_qty.config(font=entryfont)
e_eci_MM_3_qty.bind('<Return>', e_eci_MM_3_qty_adjusted)
cb_MM_3_units: Combobox = Combobox(S_3_frame, values=kl_unit_values, textvariable=eci_3_mm_units, width=10)
cb_MM_3_units.grid(row=5, column=3, sticky="w")
cb_MM_3_units.config(font=entryfont)
cb_MM_3_units.bind("<<ComboboxSelected>>", cb_MM_3_units_selected)
e_eci_kl_6_qty = Entry(S_6_frame, text="", textvariable=eci_kl_6_qty, width=8)
e_eci_kl_6_qty.grid(row=5, column=0, sticky="w")
e_eci_kl_6_qty.config(font=entryfont)
e_eci_kl_6_qty.bind('<Return>', e_eci_kl_5_qty_adjusted)
cb_kl_6_units: Combobox = Combobox(S_6_frame, values=kl_unit_values, textvariable=eci_6_kl_units, width=10)
cb_kl_6_units.grid(row=5, column=1, sticky="w")
cb_kl_6_units.config(font=entryfont)
cb_kl_6_units.bind("<<ComboboxSelected>>", cb_kl_6_units_selected)
e_eci_MM_6_qty = Entry(S_6_frame, text="", textvariable=eci_kl_6_qty, width=8)
e_eci_MM_6_qty.grid(row=5, column=2, sticky="w")
e_eci_MM_6_qty.config(font=entryfont)
e_eci_MM_6_qty.bind('<Return>', e_eci_MM_5_qty_adjusted)
cb_MM_6_units: Combobox = Combobox(S_6_frame, values=kl_unit_values, textvariable=eci_6_mm_units, width=10)
cb_MM_6_units.grid(row=5, column=3, sticky="w")
cb_MM_6_units.config(font=entryfont)
cb_MM_6_units.bind("<<ComboboxSelected>>", cb_kl_6_units_selected)

lbl_Temp_Qty_3 = Label(S_3_frame, text="Temp 3 Qty", width=10)
lbl_Temp_Qty_3.grid(row=6, column=0, sticky="w")
lbl_Temp_Qty_3.config(font=labelfont)
lbl_Temp_Units_3 = Label(S_3_frame, text="Temp 3 Units", width=12)
lbl_Temp_Units_3.grid(row=6, column=1, sticky="w")
lbl_Temp_Units_3.config(font=labelfont)
lbl_Press_Qty_3 = Label(S_3_frame, text="Press 3 Qty", width=10)
lbl_Press_Qty_3.grid(row=6, column=2, sticky="w") #, sticky=W)
lbl_Press_Qty_3.config(font=labelfont)
lbl_Press_Units_3 = Label(S_3_frame, text="Press 3 Units", width=12)
lbl_Press_Units_3.grid(row=6, column=3, sticky="w") #, sticky=W)
lbl_Press_Units_3.config(font=labelfont)
lbl_Temp_Qty_6 = Label(S_6_frame, text="Temp 6 Qty", width=10)
lbl_Temp_Qty_6.grid(row=6, column=0, sticky="w") #, sticky=W)
lbl_Temp_Qty_6.config(font=labelfont)
lbl_Temp_Units_6 = Label(S_6_frame, text="Temp 6 Units", width=10)
lbl_Temp_Units_6.grid(row=6, column=1, sticky="w")
lbl_Temp_Units_6.config(font=labelfont)
lbl_Press_Qty_6 = Label(S_6_frame, text="Press 6 Qty", width=10)
lbl_Press_Qty_6.grid(row=6, column=2, sticky="w") #, sticky=W)
lbl_Press_Qty_6.config(font=labelfont)
lbl_Press_Units_6 = Label(S_6_frame, text="Press 6 Units", width=12)
lbl_Press_Units_6.grid(row=6, column=3, sticky="w") #, sticky=W)
lbl_Press_Units_6.config(font=labelfont)

e_Temp_Qty_3 = Entry(S_3_frame, text="", textvariable=eci_temp_3_qty, width=8)
e_Temp_Qty_3.grid(row=7, column=0, sticky="w")
e_Temp_Qty_3.config(font=entryfont)
e_Temp_Qty_3.bind('<Return>', eci_3_Temp_qty_adjusted)
cb_3_Temp_Units: Combobox = Combobox(S_3_frame, values=temp_units, textvariable=eci_3_temp_units,
                                     width=10)  # eci_temp_1_units
cb_3_Temp_Units.grid(row=7, column=1, sticky="w")
cb_3_Temp_Units.config(font=entryfont)
cb_3_Temp_Units.bind("<<ComboboxSelected>>", eci_3_Temp_units_selected) #callback_set_temp_units)
e_Press_Qty_3 = Entry(S_3_frame, text="", textvariable=eci_press_3_qty, width=8)
e_Press_Qty_3.grid(row=7, column=2, sticky="w")
e_Press_Qty_3.config(font=entryfont)
cb_3_Press_Units: Combobox = Combobox(S_3_frame, values=other_units, textvariable=eci_3_press_units, width=10)
cb_3_Press_Units.grid(row=7, column=3, sticky="w")  # , padx=4)
cb_3_Press_Units.config(font=entryfont)
cb_3_Press_Units.bind("<<ComboboxSelected>>", eci_units_selected) #callback_set_press_units)
e_Temp_Qty_6 = Entry(S_6_frame, text="", textvariable=eci_temp_6_qty, width=8)
e_Temp_Qty_6.grid(row=7, column=0, sticky="w") #, sticky=W)
e_Temp_Qty_6.config(font=entryfont)
cb_6_Temp_Units: Combobox = Combobox(S_6_frame, values=temp_units, textvariable=eci_6_temp_units, width=10)
cb_6_Temp_Units.grid(row=7, column=1, sticky="w")
cb_6_Temp_Units.config(font=entryfont)
cb_6_Temp_Units.bind("<<ComboboxSelected>>", eci_6_Temp_units_selected)
e_Press_Qty_6 = Entry(S_6_frame, text="", textvariable=eci_press_5_qty, width=8)
e_Press_Qty_6.grid(row=7, column=2, sticky="w")
e_Press_Qty_6.config(font=entryfont)
cb_6_Press_Units: Combobox = Combobox(S_6_frame, values=press_units, textvariable=eci_6_press_units, width=10)
cb_6_Press_Units.grid(row=7, column=3, sticky="w")
cb_6_Press_Units.config(font=entryfont)
cb_6_Press_Units.bind("<<ComboboxSelected>>", eci_units_selected)

lbl_Heat_Qty_3 = Label(S_3_frame, text="Heat 3 Qty", width=10)
lbl_Heat_Qty_3.grid(row=8, column=0, sticky="w")
lbl_Heat_Qty_3.config(font=labelfont)
lbl_Heat_Units_3 = Label(S_3_frame, text="Heat 3 Units", width=10)
lbl_Heat_Units_3.grid(row=8, column=1, sticky="w")
lbl_Heat_Units_3.config(font=labelfont)
lbl_Other_Qty_3 = Label(S_3_frame, text="Other 3 Qty", width=10)
lbl_Other_Qty_3.grid(row=8, column=2, sticky="w") #, sticky=W)
lbl_Other_Qty_3.config(font=labelfont)
lbl_Other_Units_3 = Label(S_3_frame, text="Other 3 Units", width=10)
lbl_Other_Units_3.grid(row=8, column=3, sticky="w") #, sticky=W)
lbl_Other_Units_3.config(font=labelfont)
lbl_Heat_Qty_6 = Label(S_6_frame, text="Heat 6 Qty", width=10)
lbl_Heat_Qty_6.grid(row=8, column=0, sticky="w")
lbl_Heat_Qty_6.config(font=labelfont)
lbl_Heat_Units_6 = Label(S_6_frame, text="Heat 6 Units", width=10)
lbl_Heat_Units_6.grid(row=8, column=1, sticky="w")
lbl_Heat_Units_6.config(font=labelfont)
lbl_Other_Qty_6 = Label(S_6_frame, text="Other 6 Qty", width=10)
lbl_Other_Qty_6.grid(row=8, column=2, sticky="w") #, sticky=W)
lbl_Other_Qty_6.config(font=labelfont)
lbl_Other_Units_6 = Label(S_6_frame, text="Other 6 Units", width=10)
lbl_Other_Units_6.grid(row=8, column=3, sticky="w") #, sticky=W)
lbl_Other_Units_6.config(font=labelfont)

e_Heat_Qty_3 = Entry(S_3_frame, text="", textvariable=eci_heat_3_qty, width=8)
e_Heat_Qty_3.grid(row=9, column=0, sticky="w")
e_Heat_Qty_3.config(font=entryfont)
e_Heat_Qty_3.bind('<Return>', eci_3_Temp_qty_adjusted)
cb_3_Heat_Units: Combobox = Combobox(S_3_frame, values=heat_units, textvariable=eci_3_heat_units,
                                     width=10)  # eci_temp_1_units
cb_3_Heat_Units.grid(row=9, column=1, sticky="w")
cb_3_Heat_Units.config(font=entryfont)
cb_3_Heat_Units.bind("<<ComboboxSelected>>", eci_units_selected) #callback_set_temp_units)
e_Other_Qty_3 = Entry(S_3_frame, text="", textvariable=other_3_qty, width=8)
e_Other_Qty_3.grid(row=9, column=2, sticky="w")
e_Other_Qty_3.config(font=entryfont)
cb_3_Other_Units: Combobox = Combobox(S_3_frame, values=other_units, textvariable=other_3_units, width=10)
cb_3_Other_Units.grid(row=9, column=3, sticky="w")  # , padx=4)
cb_3_Other_Units.config(font=entryfont)
cb_3_Other_Units.bind("<<ComboboxSelected>>", eci_units_selected) #callback_set_press_units)
e_Heat_Qty_6 = Entry(S_6_frame, text="", textvariable=eci_heat_6_qty, width=8)
e_Heat_Qty_6.grid(row=9, column=0, sticky="w")
e_Heat_Qty_6.config(font=entryfont)
e_Heat_Qty_6.bind('<Return>', eci_6_Temp_qty_adjusted)
cb_6_Heat_Units: Combobox = Combobox(S_6_frame, values=heat_units, textvariable=eci_6_heat_units,
                                     width=10) 
cb_6_Heat_Units.grid(row=9, column=1, sticky="w")
cb_6_Heat_Units.config(font=entryfont)
cb_6_Heat_Units.bind("<<ComboboxSelected>>", eci_units_selected) #callback_set_temp_units)
e_Other_Qty_6 = Entry(S_6_frame, text="", textvariable=other_6_qty, width=8)
e_Other_Qty_6.grid(row=9, column=2, sticky="w")
e_Other_Qty_6.config(font=entryfont)
cb_6_Other_Units: Combobox = Combobox(S_6_frame, values=press_units, textvariable=other_2_units, width=10)
cb_6_Other_Units.grid(row=9, column=3, sticky="w")  # , padx=4)
cb_6_Other_Units.config(font=entryfont)
cb_6_Other_Units.bind("<<ComboboxSelected>>", eci_units_selected)


# lbl_blank = Label(inside_frame, text="")
# lbl_blank.grid(row=32, column=0)
# lbl_blank.config(font=labelfont)

# lbl_Equipment = Label(inside_frame, text="Equipment", width=10)
# lbl_Equipment.grid(row=33, column=0)
# lbl_Equipment.config(font=labelfont)
# lbl_Energy_type = Label(inside_frame, text="Energy type", width=10)
# lbl_Energy_type.grid(row=33, column=1) #, sticky=W)
# lbl_Energy_type.config(font=labelfont)
# lbl_Energy_amount = Label(inside_frame, text="Energy amount", width=12)
# lbl_Energy_amount.grid(row=33, column=2) #, sticky=W)
# lbl_Energy_amount.config(font=labelfont)
# lbl_Catalyst = Label(inside_frame, text="Catalyst", width=10)
# lbl_Catalyst.grid(row=33, column=3) #, sticky=W)
# lbl_Catalyst.config(font=labelfont)
# lbl_Side_effects = Label(inside_frame, text="Side effects", width=12)
# lbl_Side_effects.grid(row=33, column=4)
# lbl_Side_effects.config(font=labelfont)
# lbl_By_products = Label(inside_frame, text="By-products", width=10)
# lbl_By_products.grid(row=33, column=5) #, sticky=W)
# lbl_By_products.config(font=labelfont)
# lbl_Variables = Label(inside_frame, text="Variables")
# lbl_Variables.grid(row=33, column=6) #, sticky=W)
# lbl_Variables.config(font=labelfont)
# lbl_Variables = Label(inside_frame, text="Values", width=10)
# lbl_Variables.grid(row=33, column=7) #, sticky=W)
# lbl_Variables.config(font=labelfont)

# cb_Equipment: Combobox = Combobox(inside_frame, values=equipment, textvariable=equipment_selected, width=12)
# cb_Equipment.grid(row=34, column=0)
# cb_Equipment.config(font=entryfont)
# cb_Energy_type: Combobox = Combobox(inside_frame, values=energy_type, textvariable=energy_type_selected, width=12)
# cb_Energy_type.grid(row=34, column=1) #, sticky=W)
# cb_Energy_type.config(font=entryfont)
# e_Energy_amount = Entry(inside_frame, text="", textvariable=energy_amount, width=12)
# e_Energy_amount.grid(row=34, column=2)
# e_Energy_amount.config(font=entryfont)
# cb_Catalyst: Combobox = Combobox(inside_frame, values=catalyst, textvariable=catalyst_selected, width=12)
# cb_Catalyst.grid(row=34, column=3) #, sticky=W)
# cb_Catalyst.config(font=entryfont)
# cb_Side_effects: Combobox = Combobox(inside_frame, values=side_effects, textvariable=side_effect_selected, width=12)
# cb_Side_effects.grid(row=34, column=4)
# cb_Side_effects.config(font=entryfont)
# cb_By_products: Combobox = Combobox(inside_frame, values=by_products, textvariable=by_product_selected, width=12)
# cb_By_products.grid(row=34, column=5) #, sticky=W)
# cb_By_products.config(font=entryfont)
# cb_Variables: Combobox = Combobox(inside_frame, values=variables, textvariable=variable_selected, width=12)
# cb_Variables.grid(row=34, column=6) #, sticky=W)
# cb_Variables.config(font=entryfont)
# e_Variable_Value = Entry(inside_frame, text="", textvariable=variable_value, width=8)
# e_Variable_Value.grid(row=34, column=7)
# e_Variable_Value.config(font=entryfont)

# lbl_Explanation = Label(inside_frame, text="Explanation", width=10)
# lbl_Explanation.grid(row=35, column=0)
# lbl_Explanation.config(font=labelfont)
# lbl_Explanation = Label(inside_frame, text="Super subscript ", width=12)
# lbl_Explanation.grid(row=35, column=1)
# lbl_Explanation.config(font=labelfont)
# lbl_LU_Process = Label(inside_frame, text='360\u2070 \u2070C H\u2082O')  # C2H3O2-
# lbl_LU_Process.grid(row=35, column=2)
# lbl_LU_Process.config(font=labelfont)
# '''
# unicode numbers. degrees: \u2070 subscript 2: \u2082 subscript 3: \u2083 subscript e: \u2091
# superscript 2:\u00B2 superscript 3:\u00B3 superscript 4: \u2074 superscript -: \u207B
# '''
# lbl_LU_Process = Label(inside_frame, text='X\u2074 + X\u00B2 = 0')
# lbl_LU_Process.grid(row=35, column=3)
# lbl_LU_Process.config(font=labelfont)
# lbl_LU_Process = Label(inside_frame, text='C\u2082H\u2083O\u2082\u207B C\u2082H\u2083O\u00B2\u207B')
# # lbl_LU_Process = Label(text='C\u00B2\u207A Fe\u00B3\u207A Cl\u207B e\u207B')
# lbl_LU_Process.grid(row=35, column=4)
# lbl_LU_Process.config(font=labelfont)
# lbl_LU_Process = Label(inside_frame,text='Cl\u2091 Fe\u00B3\u207A ')
# lbl_LU_Process.grid(row=35, column=5)
# lbl_LU_Process.config(font=labelfont)
# e_Explanation = Text(inside_frame, height=6, width=100)
# e_Explanation.grid(row=36, column=0, columnspan=6) #, sticky=W)
# e_Explanation.config(font=entryfont)
# e_Explanation.rowconfigure(99)
# lbl_blank = Label(inside_frame, text="")
# lbl_blank.grid(row=40, column=0, columnspan=2)
# lbl_blank.config(font=labelfont)
# lbl_blank = Label(inside_frame, text="")
# lbl_blank.grid(row=41, column=0, columnspan=2)
# lbl_blank.config(font=labelfont)
# lbl_blank = Label(inside_frame, text="")
# lbl_blank.grid(row=42, column=0, columnspan=2)
# lbl_blank.config(font=labelfont)

set_initial_form_values()

if __name__ == '__main__':
    root.mainloop()


