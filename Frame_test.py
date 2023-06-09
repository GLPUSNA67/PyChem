import sys
from tkinter import *  # get widget classes
from tkinter.ttk import Combobox, Entry, Label
import tkinter as tk
import pdb
from tkinter import messagebox as mb #*  # get standard dialogs
from tkinter import font

root = Tk()
root.geometry("1800x800")
titlefont = ('Ariel', 14, 'bold')
labelfont = ('Ariel', 14)  # , 'bold')
buttonfont = ('Ariel', 12)  # , 'bold')
entryfont = ('Ariel', 12)  # , 'bold')

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
title_frame = Frame(main_canvas, bg= "White", width=2000, height=1)
title_frame.grid(row=0,column=0, columnspan=16, sticky=W) # pack(side=LEFT)
# centerLeftframe = Frame(inside_frame , height=5, bg="PINK")
# centerLeftframe.pack( side = LEFT,fill=BOTH, expand = 1)
S_1_frame = Frame(main_canvas, width=800, height=200)
S_1_frame.grid(row=4,column=0, sticky="nw") # pack(side=LEFT) , sticky=W
S_4_frame = Frame(main_canvas, width=800, height=200)
S_4_frame.grid(row=4,column=1, sticky="nw") # pack(side=LEFT), sticky=W
# S_2_frame = Frame(inside_frame, width=800, height=200)
# S_2_frame.grid(row=5,column=0, sticky=W) # pack(side=LEFT) , sticky=W
# S_5_frame = Frame(inside_frame, width=800, height=200)
# S_5_frame.grid(row=5,column=1) # pack(side=LEFT), sticky=W
# Add the new froma to a Window in the Canvas
main_canvas.create_window((0,0), window = inside_frame, anchor = "nw")
# main_frame.columnconfigure(0, weight=1)
# main_frame.columnconfigure(1, weight=1)
# main_frame.columnconfigure(2, weight=1)
# main_frame.columnconfigure(3, weight=1)
# main_frame.columnconfigure(4, weight=1)
# main_frame.columnconfigure(5, weight=1)
# main_frame.columnconfigure(6, weight=1)
# main_frame.columnconfigure(7, weight=1)
# main_frame.columnconfigure(8, weight=1)
# main_frame.columnconfigure(9, weight=1)
# main_frame.columnconfigure(10, weight=1)
# main_frame.columnconfigure(11, weight=1)
# main_frame.columnconfigure(12, weight=1)
# main_frame.columnconfigure(13, weight=1)
# main_frame.columnconfigure(14, weight=1)
# main_frame.columnconfigure(15, weight=1)
# main_frame.columnconfigure(16, weight=1)
# main_frame.columnconfigure(17, weight=1)
# main_frame.columnconfigure(18, weight=1)
# main_frame.columnconfigure(19, weight=1)
# main_frame.columnconfigure(20, weight=1)
# main_frame.rowconfigure(0, weight=1)
# main_frame.rowconfigure(1, weight=1)
# main_frame.rowconfigure(2, weight=1)
# main_frame.rowconfigure(3, weight=1)
# main_frame.rowconfigure(4, weight=1)
# main_frame.rowconfigure(5, weight=1)
# main_frame.rowconfigure(6, weight=1)
# main_frame.rowconfigure(7, weight=1)
# main_frame.rowconfigure(8, weight=1)
# main_frame.rowconfigure(9, weight=1)
# main_frame.rowconfigure(10, weight=1)
# main_frame.rowconfigure(11, weight=1)
# main_frame.rowconfigure(12, weight=1)
# main_frame.rowconfigure(13, weight=1)
# main_frame.rowconfigure(14, weight=1)
# main_frame.rowconfigure(15, weight=1)
# main_frame.rowconfigure(16, weight=1)
# main_frame.rowconfigure(17, weight=1)
# main_frame.rowconfigure(18, weight=1)
# main_frame.rowconfigure(19, weight=1)
# main_frame.rowconfigure(20, weight=1)

# set variables
element_symbol_string = 'H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti\
        V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In\
        Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os\
        Ir Pt Au Hg Tl Bi Po At Rn Fr Ra Ac Th Pa U Np Am Cm Bk Cf Es Fm Md No Lr ' \
        'RF Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og'

compound_formula_string = "Al4C3 AlCl3 Ar2He2Kr2Ne2Xe2Rn2 BCl3 Ca(H2PO4)2 CaI Ca(OH)2 Ca3P2 CdS CsF C6H8O7 CH3CO2H C2H3OOH" \
                           " CO CO2 HBr HC2H3O2 HCl HClO4 HCN H2CO3 HF HI HNO2 HNO3 H3PO4 H2S H2SO3 H2SO4 IF7 KBr KOH LiCl" \
                           " Mg3N2 NaCl NaHCO33 Na2O NaOH NH3 N2H4 NO NO2 N2O4 N2O N2O5 PF5 SO2 SO3 CH4 C2H6 C3H8 C4H10 C4H10_M" \
                           " C5H12 C6H14 C7H16 C8H18 C9H20 C10H22 C14H30 C18H38"

major_process_list = "Calculate Synthesis Decompostion Combustion Single_Replacement Double_Replacement Neutralization Precipitation Balance_Equation Set_default_T_and_P Parse_Reactants Parse_Products Acid_Base Oxidation_Reduction Oxidation_Rate Metathesis Refinement"
minor_process_list = "Set_STP_Variables Pressure Volume, moles Temperature pvnrt "
environment = "Laboratory Industry Nature"
process_list = "major minor"
eci_cb_values = ""
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
energy_amount = DoubleVar()
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
unit_values = "grams liters(g)"

def create_record():
    pass

def update_record():
    pass

def retrieve_record():
    pass

def next_record(): #
    pass


def previous_record():
    pass

def major_process_selected():
    pass

def minor_process_selected():
    pass

def get_record():
    pass

def select_eci_1_type():
    pass

def select_eci_2_type():
    pass
def select_eci_3_type():
    pass
def select_eci_4_type():
    pass
def select_eci_5_type():
    pass
def select_eci_6_type():
    pass
def eci_units_selected():
    pass
def setEci_1():
    pass
def setEci_2():
    pass
def setEci_3():
    pass
def setEci_4():
    pass
def setEci_5():
    pass


def Continue():
    pass

def eci_1_qty_adjusted():
    pass

compound_formula_string = "Al4C3 AlCl3 Ar2He2Kr2Ne2Xe2Rn2 BCl3 Ca(H2PO4)2 CaI Ca(OH)2 Ca3P2 CdS CsF C6H8O7 CH3CO2H C2H3OOH" \
                           " CO CO2 HBr HC2H3O2 HCl HClO4 HCN H2CO3 HF HI HNO2 HNO3 H3PO4 H2S H2SO3 H2SO4 IF7 KBr KOH LiCl" \
                           " Mg3N2 NaCl NaHCO33 Na2O NaOH NH3 N2H4 NO NO2 N2O4 N2O N2O5 PF5 SO2 SO3 CH4 C2H6 C3H8 C4H10 C4H10_M" \
                           " C5H12 C6H14 C7H16 C8H18 C9H20 C10H22 C14H30 C18H38"

major_process_list = "Calculate Synthesis Decompostion Combustion Single_Replacement Double_Replacement Neutralization Precipitation Balance_Equation Set_default_T_and_P Parse_Reactants Parse_Products Acid_Base Oxidation_Reduction Oxidation_Rate Metathesis Refinement"
minor_process_list = "Set_STP_Variables Pressure Volume, moles Temperature pvnrt "
environment = "Laboratory Industry Nature"
lbl_Title = Label(title_frame, text="Chemistry") # inside_frame
lbl_Title.grid(row=0, column=3)
lbl_Title.config(font=titlefont)

lbl_blank = Label(title_frame, text="")
lbl_blank.grid(row=1, column=0)
lbl_blank.config(font=labelfont)

lbl_blank = Label(title_frame, text="")
lbl_blank.grid(row=1, column=0)
lbl_blank.config(font=labelfont)

lbl_record_create = Label(title_frame, text="Create record:")
lbl_record_create.grid(row=2, column=0)
lbl_record_create.config(font=labelfont)
e_recordname = Entry(title_frame, text="")
e_recordname.grid(row=2, column=1, columnspan=2)
e_recordname.config(font=labelfont)
btn_create_record = Button(title_frame, text='Create Record', command=create_record)
btn_create_record.grid(row=2, column=3)
btn_create_record.config(font=buttonfont)
btn_create_record.bind("<<ComboboxSelected>>", create_record())
btn_update_record = Button(title_frame, text='Update Record', command=update_record)
btn_update_record.grid(row=2, column=4)
btn_update_record.config(font=buttonfont)
btn_update_record.bind("<<ComboboxSelected>>", update_record)
btn_Continue = Button(title_frame, text='* Continue *', command=Continue)
btn_Continue.grid(row=2, column=5)
btn_Continue.config(font=titlefont)

lbl_record_ops = Label(title_frame, text="Get record:")
lbl_record_ops.grid(row=3, column=0)
lbl_record_ops.config(font=labelfont)
cb_RecordName: Combobox = Combobox(title_frame, values="", width=12)
cb_RecordName.grid(row=3, column=1)
cb_RecordName.config(font=entryfont)
cb_RecordName.bind("<<ComboboxSelected>>", retrieve_record)
# e_recordname = Entry(root, text="")   #, width=30)
# e_recordname.grid(row=3, column=3)
# e_recordname.config(font=labelfont)
btn_create_record = Button(title_frame, text='Get Record', command=get_record)
btn_create_record.grid(row=3, column=2)
btn_create_record.config(font=buttonfont)
btn_create_record.bind("<<ComboboxSelected>>", retrieve_record)
btn_create_record = Button(title_frame, text='Previous Record', command=get_record)
btn_create_record.grid(row=3, column=3)
btn_create_record.config(font=buttonfont)
btn_create_record.bind("<<ComboboxSelected>>", previous_record)
btn_create_record = Button(title_frame, text='Next Record', command=get_record)
btn_create_record.grid(row=3, column=4)
btn_create_record.config(font=buttonfont)
btn_create_record.bind("<<ComboboxSelected>>", next_record)
btn_show_instructions = Button(title_frame, text='Show Instructions', command=get_record)
btn_show_instructions.grid(row=2, column=6)
btn_show_instructions.config(font=labelfont)
#btn_show_instructions.bind("<<ComboboxSelected>>", show_hide_instructions)

lbl_LU_Compound = Label(title_frame, text="   Look up compound:")
lbl_LU_Compound.grid(row=4, column=0)
lbl_LU_Compound.config(font=labelfont)
cb_LU_Compound = Combobox(title_frame, values=compound_formula_string, width=12)
cb_LU_Compound.grid(row=4, column=1)
cb_LU_Compound.config(font=entryfont)
cb_LU_Environment = Combobox(title_frame, values=environment, width=12)

# Create a search for and retrieve a compount
lbl_LU_Process = Label(title_frame, text="   Look up process:")
lbl_LU_Process.grid(row=4, column=2)
lbl_LU_Process.config(font=labelfont)
cb_LU_Process = Combobox(title_frame, values=major_process_list, width=12)
cb_LU_Process.grid(row=4, column=3)
cb_LU_Process.config(font=entryfont)
# Create a search for and retrieve a process
lbl_LU_Environment = Label(title_frame, text="   Look up environment:", width=22)
lbl_LU_Environment.grid(row=4, column=4)
lbl_LU_Environment.config(font=labelfont)
cb_LU_Environment = Combobox(title_frame, values=environment, width=12)
cb_LU_Environment.grid(row=4, column=5)
cb_LU_Environment.config(font=entryfont)

lbl_Select_M_Process = Label(title_frame, text="   Select major process", width=20)
lbl_Select_M_Process.grid(row=5, column=0)
lbl_Select_M_Process.config(font=labelfont)
cb_Select_M_Process: Combobox = Combobox(title_frame, values=major_process_list, textvariable=major_process_selected, width=12)
cb_Select_M_Process.grid(row=5, column=1)
cb_Select_M_Process.config(font=entryfont)
lbl_Select_m_Process = Label(title_frame, text="   Select minor process", width=20)
lbl_Select_m_Process.grid(row=5, column=2)
lbl_Select_m_Process.config(font=labelfont)
cb_Select_m_Process: Combobox = Combobox(title_frame, values=minor_process_list, textvariable=minor_process_selected, width=12)
cb_Select_m_Process.grid(row=5, column=3)
cb_Select_m_Process.config(font=entryfont)
cb_Select_m_Process.bind("<<ComboboxSelected>>", minor_process_selected)
lbl_Select_Environment = Label(title_frame, text="   Select environment:", width=22)
lbl_Select_Environment.grid(row=5, column=4)
lbl_Select_Environment.config(font=titlefont)
cb_Select_Environment: Combobox = Combobox(title_frame, values=environment, width=12)
cb_Select_Environment.grid(row=5, column=5)
cb_Select_Environment.config(font=entryfont)

lbl_blank = Label(title_frame, text="")
lbl_blank.grid(row=6, column=0)
# lbl_blank = Label(title_frame, text="")
# lbl_blank.grid(row=9, column=0)

# *****
# lbl_spacing = Label(S_1_frame, text="", width=100) 
# # 0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
# lbl_spacing.grid(row=0, column=0, columnspan=10, sticky=W)
# lbl_spacing.config(font=labelfont)
lbl_eci_1 = Label(S_1_frame, text="Select Element, Compound or Ion for ComboBox 1")
lbl_eci_1.grid(row=0, column=0, columnspan=4, sticky=tk.N+tk.W) #, sticky=W)
lbl_eci_1.config(font=labelfont)
cb_Select_CB1: Combobox = Combobox(S_1_frame, values=eci_cb_values, width=10)
cb_Select_CB1.grid(row=0, column=5, sticky=tk.N+tk.W) #, sticky=W)
cb_Select_CB1.config(font=entryfont)
cb_Select_CB1.bind("<<ComboboxSelected>>", select_eci_1_type)
# cb_Process = Combobox(S_1_frame, values=process_list, width=20)
# cb_Process.grid(row=0, column=3, sticky=W) # , columnspan=2
# cb_Process.config(font=entryfont)

# lbl_spacing = Label(S_1_frame, text="   Select Element, Compound or Ion for ComboBox 1", width=60)
# lbl_spacing.grid(row=1, column=0, columnspan=6, sticky=W)
# lbl_spacing.config(font=labelfont)
lbl_eci_4 = Label(S_4_frame, text="Select Element, Compound or Ion for ComboBox 4")
lbl_eci_4.grid(row=0, column=8, columnspan=4, sticky=tk.N+tk.W) #, sticky=W)
lbl_eci_4.config(font=labelfont)

cb_Select_CB4 = Combobox(S_4_frame, values=eci_cb_values, width=10)
cb_Select_CB4.grid(row=0, column=12, columnspan=1, sticky=tk.N+tk.W)
cb_Select_CB4.config(font=entryfont)
cb_Select_CB4.bind("<<ComboboxSelected>>", select_eci_4_type)

lbl_eci_1_qty = Label(S_1_frame, text="ECI 1 Qty", width=10)
lbl_eci_1_qty.grid(row=2, column=0, columnspan=1, sticky=W)
lbl_eci_1_qty.config(font=labelfont)
lbl_eci_1_units = Label(S_1_frame, text="Units 1", width=10)
lbl_eci_1_units.grid(row=2, column=1, columnspan=1, sticky=W) #, sticky=W)
lbl_eci_1_units.config(font=labelfont)
lbl_eci_1 = Label(S_1_frame, text="ECI 1", width=10)
lbl_eci_1.grid(row=2, column=2, columnspan=2, sticky=W) #, sticky=W)
lbl_eci_1.config(font=labelfont)
lbl_eci_1_valence = Label(S_1_frame, text="Valence 1", width=10)
lbl_eci_1_valence.grid(row=2, column=5, columnspan=1, sticky=W) #, sticky=W)
lbl_eci_1_valence.config(font=labelfont)
lbl_eci_4_qty = Label(S_4_frame, text="ECI 4 Qty", width=10)
lbl_eci_4_qty.grid(row=2, column=8, columnspan=1)
lbl_eci_4_qty.config(font=labelfont)
lbl_eci_4_units = Label(S_4_frame, text="Units 4", width=10)
lbl_eci_4_units.grid(row=2, column=9, columnspan=1) #, sticky=W)
lbl_eci_4_units.config(font=labelfont)
lbl_eci_4 = Label(S_4_frame, text="ECI 4", width=10)
lbl_eci_4.grid(row=2, column=10, columnspan=1) #, sticky=W)
lbl_eci_4.config(font=labelfont)
lbl_eci_4_valence = Label(S_4_frame, text="Valence 4", width=10)
lbl_eci_4_valence.grid(row=2, column=11, columnspan=1) #, sticky=W)
lbl_eci_4_valence.config(font=labelfont)
lbl_eci_4_Molar_Mass_Label = Label(S_4_frame, text="Molar Mass", width=10)
lbl_eci_4_Molar_Mass_Label.grid(row=2, column=12, columnspan=1, sticky=W) #, sticky=W)
lbl_eci_4_Molar_Mass_Label.config(font=labelfont)

e_eci_1_qty = Entry(S_1_frame, text="", textvariable=eci_1_qty, width=8)
e_eci_1_qty.grid(row=3, column=0, columnspan=1, sticky=W)
e_eci_1_qty.config(font=entryfont)
e_eci_1_qty.bind('<Return>', eci_1_qty_adjusted)
cb_eci_1_units: Combobox = Combobox(S_1_frame, values=unit_values, textvariable=eci_1_units, width=10)
cb_eci_1_units.grid(row=3, column=1, columnspan=1, sticky=W) 
cb_eci_1_units.config(font=entryfont)
cb_eci_1_units.bind("<<ComboboxSelected>>", eci_units_selected)
cb_eci_1: Combobox = Combobox(inside_frame, textvariable=eci_1, width=12)
cb_eci_1.grid(row=3, column=2, sticky=W)
cb_eci_1.config(font=labelfont)
cb_eci_1['values'] = element_symbol_string
cb_eci_1.bind("<<ComboboxSelected>>", setEci_1) # setSelectedItemName

# lbl_eci_2_qty = Label(S_2_frame, text="ECI Qty 2", width=10)
# lbl_eci_2_qty.grid(row=2, column=0, columnspan=1, sticky=W)
# lbl_eci_2_qty.config(font=labelfont)
# lbl_eci_2_units = Label(S_2_frame, text="Units 2", width=10)
# lbl_eci_2_units.grid(row=2, column=1, columnspan=1, sticky=W) #, sticky=W)
# lbl_eci_2_units.config(font=labelfont)
# lbl_eci_2 = Label(S_2_frame, text="ECI 2", width=10)
# lbl_eci_2.grid(row=2, column=2, columnspan=2, sticky=W) #, sticky=W)
# lbl_eci_2.config(font=labelfont)
# lbl_eci_2_valence = Label(S_2_frame, text="Valence 2", width=10)
# lbl_eci_2_valence.grid(row=2, column=5, columnspan=1, sticky=W) #, sticky=W)
# lbl_eci_2_valence.config(font=labelfont)
# lbl_eci_5_qty = Label(S_2_frame, text="ECI Qty 5", width=10)
# lbl_eci_5_qty.grid(row=2, column=7, columnspan=1)
# lbl_eci_5_qty.config(font=labelfont)
# lbl_eci_5_units = Label(S_2_frame, text="Units 5", width=10)
# lbl_eci_5_units.grid(row=2, column=8, columnspan=1) #, sticky=W)
# lbl_eci_5_units.config(font=labelfont)
# lbl_eci_5 = Label(S_2_frame, text="ECI 5", width=10)
# lbl_eci_5.grid(row=2, column=9, columnspan=1) #, sticky=W)
# lbl_eci_5.config(font=labelfont)
# lbl_eci_5_valence = Label(S_2_frame, text="Valence 5", width=10)
# lbl_eci_5_valence.grid(row=2, column=10, columnspan=1) #, sticky=W)
# lbl_eci_5_valence.config(font=labelfont)
# lbl_eci_5_Molar_Mass_Label = Label(S_2_frame, text="Molar Mass", width=10)
# lbl_eci_5_Molar_Mass_Label.grid(row=2, column=11, columnspan=1, sticky=W) #, sticky=W)
# lbl_eci_5_Molar_Mass_Label.config(font=labelfont)

# e_eci_2_qty = Entry(S_2_frame, text="", textvariable=eci_1_qty, width=8)
# e_eci_2_qty.grid(row=3, column=0, columnspan=1, sticky=W)
# e_eci_2_qty.config(font=entryfont)
# e_eci_2_qty.bind('<Return>', eci_1_qty_adjusted)
# # #e_eci_1_qty = 666
# # #e_eci_1_qty = 36.0
# # ''' Can I generalize the following to: set_eci_db_eci_1_qty = e_eci_1_qty.get()'''
# # #e_eci_1_qty.bind('<FocusOut>', lambda event: set_eci_db_eci_1_qty(e_eci_1_qty.get()))
# cb_eci_2_units: Combobox = Combobox(S_2_frame, values=unit_values, textvariable=eci_1_units, width=10)
# cb_eci_2_units.grid(row=3, column=1, columnspan=1, sticky=W) 
# cb_eci_2_units.config(font=entryfont)
# cb_eci_2_units.bind("<<ComboboxSelected>>", eci_units_selected)

if __name__ == '__main__':
    root.mainloop()
