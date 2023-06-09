import sys
from tkinter import *  # get widget classes
from tkinter.ttk import Combobox, Entry, Label

root = Tk()
root.geometry("1500x250")
titlefont = ('Ariel', 14, 'bold')
labelfont = ('Ariel', 14)  # , 'bold')
buttonfont = ('Ariel', 12)  # , 'bold')
entryfont = ('Ariel', 12) 
  
# w = Label(root, text ='GeeksForGeeks', bg="PINK", font = "50") 
# w.pack(fill=BOTH, expand = 1)


frame = Frame(root)
frame.pack(fill=BOTH, expand = 1)
# title_frame = Frame(frame)
# title_frame.pack(fill=BOTH, expand = 1)

centerframe = Frame(root , height=5)
centerframe.pack( side = BOTTOM)
    
top_frame = Frame(frame , height=5)
top_frame.pack( side = TOP,fill=BOTH, expand = 1)
centerLeftframe = Frame(frame , height=5, bg="PINK")
centerLeftframe.pack( side = LEFT,fill=BOTH, expand = 1)

centerCenterframe = Frame(frame , height=5, bg="RED")
centerCenterframe.pack( side = LEFT, fill=BOTH, expand = 1)

centerRightframe = Frame(frame , height=5)
centerRightframe.pack( side = LEFT, fill=BOTH, expand = 1)

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM ,fill=BOTH, expand = 1)

def get_record():
    pass

def retrieve_record():
    pass

def previous_record():
    pass

def next_record():
    pass

def major_process_selected():
    pass

def minor_process_selected():
    pass
major_process_list = ""
minor_process_list = ""
environment = ""

lbl_Title = Label(top_frame, text="Chemistry") # inside_frame
lbl_Title.grid(row=0, column=3)
lbl_Title.config(font=titlefont)
btn_show_instructions = Button(top_frame, text='Show Instructions', command=get_record)
btn_show_instructions.grid(row=0, column=8)
btn_show_instructions.config(font=labelfont)

lbl_blank = Label(top_frame, text="")
lbl_blank.grid(row=1, column=0)
lbl_blank.config(font=labelfont)

btn_create_record = Button(top_frame, text='Get Record', command=get_record)
btn_create_record.grid(row=3, column=2)
btn_create_record.config(font=buttonfont)
btn_create_record.bind("<<ComboboxSelected>>", retrieve_record)
btn_create_record = Button(top_frame, text='Previous Record', command=get_record)
btn_create_record.grid(row=3, column=3)
btn_create_record.config(font=buttonfont)
btn_create_record.bind("<<ComboboxSelected>>", previous_record)
btn_create_record = Button(top_frame, text='Next Record', command=get_record)
btn_create_record.grid(row=3, column=4)
btn_create_record.config(font=buttonfont)
btn_create_record.bind("<<ComboboxSelected>>", next_record)
btn_show_instructions = Button(top_frame, text='Show Instructions', command=get_record)
btn_show_instructions.grid(row=0, column=6)
btn_show_instructions.config(font=labelfont)
#btn_show_instructions.bind("<<ComboboxSelected>>", show_hide_instructions)

lbl_LU_Compound = Label(top_frame, text="   Look up compound:")
lbl_LU_Compound.grid(row=6, column=0)
lbl_LU_Compound.config(font=labelfont)
cb_LU_Compound = Combobox(top_frame, values=previous_record, width=12)
cb_LU_Compound.grid(row=6, column=1)
cb_LU_Compound.config(font=entryfont)

# Create a search for and retrieve a compount
lbl_LU_Process = Label(top_frame, text="   Look up process:")
lbl_LU_Process.grid(row=6, column=2)
lbl_LU_Process.config(font=labelfont)
cb_LU_Process = Combobox(top_frame, values=major_process_list, width=12)
cb_LU_Process.grid(row=6, column=3)
cb_LU_Process.config(font=entryfont)
# Create a search for and retrieve a process
lbl_LU_Environment = Label(top_frame, text="   Look up environment:", width=22)
lbl_LU_Environment.grid(row=6, column=4)
lbl_LU_Environment.config(font=labelfont)
cb_LU_Environment = Combobox(top_frame, values=environment, width=12)
cb_LU_Environment.grid(row=6, column=5)
cb_LU_Environment.config(font=entryfont)

lbl_Select_M_Process = Label(top_frame, text="   Select major process", width=20)
lbl_Select_M_Process.grid(row=7, column=0)
lbl_Select_M_Process.config(font=labelfont)
cb_Select_M_Process: Combobox = Combobox(top_frame, values=major_process_list, textvariable=major_process_selected, width=12)
cb_Select_M_Process.grid(row=7, column=1)
cb_Select_M_Process.config(font=entryfont)
lbl_Select_m_Process = Label(top_frame, text="   Select minor process", width=20)
lbl_Select_m_Process.grid(row=7, column=2)
lbl_Select_m_Process.config(font=labelfont)
cb_Select_m_Process: Combobox = Combobox(top_frame, values=minor_process_list, textvariable=minor_process_selected, width=12)
cb_Select_m_Process.grid(row=7, column=3)
cb_Select_m_Process.config(font=entryfont)
cb_Select_m_Process.bind("<<ComboboxSelected>>", minor_process_selected)
lbl_Select_Environment = Label(top_frame, text="   Select environment:", width=22)
lbl_Select_Environment.grid(row=7, column=4)
lbl_Select_Environment.config(font=titlefont)
cb_Select_Environment: Combobox = Combobox(top_frame, values=environment, width=12)
cb_Select_Environment.grid(row=7, column=5)
cb_Select_Environment.config(font=entryfont)
lbl_blank = Label(top_frame, text="")
lbl_blank.grid(row=7, column=0)
lbl_blank.config(font=labelfont)
# lbl_record_create = Label(top_frame, text="Create record:")
# lbl_record_create.grid(row=2, column=0)
# lbl_record_create.config(font=labelfont)
# e_recordname = Entry(top_frame, text="")
# e_recordname.grid(row=2, column=1, columnspan=2)
# e_recordname.config(font=labelfont)
# lbl_record_ops = Label(top_frame, text="Get record:")
# lbl_record_ops.grid(row=2, column=2)
# lbl_record_ops.config(font=labelfont)
# lbl_record_ops = Label(top_frame, text="Get record:")
# lbl_record_ops.grid(row=3, column=0)
# lbl_record_ops.config(font=labelfont)
# lbl_record_ops = Label(top_frame, text="Get record:")
# lbl_record_ops.grid(row=3, column=1)
# lbl_record_ops.config(font=labelfont)
# lbl_record_ops = Label(top_frame, text="Get record:")
# lbl_record_ops.grid(row=3, column=2)
# lbl_record_ops.config(font=labelfont)
# lbl_record_ops = Label(top_frame, text="Get record:")
# lbl_record_ops.grid(row=3, column=3)
# lbl_record_ops.config(font=labelfont)
# lbl_record_ops = Label(top_frame, text="Get record:")
# lbl_record_ops.grid(row=3, column=4)
# lbl_record_ops.config(font=labelfont)
# lbl_record_ops = Label(top_frame, text="Get record:")
# lbl_record_ops.grid(row=3, column=5)
# lbl_record_ops.config(font=labelfont)

lbl_s_1 = Label(centerLeftframe, text="Label 1")
lbl_s_1.grid(row=0, column=0)
lbl_s_1.config(font=labelfont)
lbl_s_2 = Label(centerLeftframe, text="Label 2")
lbl_s_2.grid(row=1, column=1)
lbl_s_2.config(font=labelfont)
lbl_s_1 = Label(centerCenterframe, text="Label 1")
lbl_s_1.grid(row=0, column=0)
lbl_s_1.config(font=labelfont)
lbl_s_2 = Label(centerCenterframe, text="Label 2")
lbl_s_2.grid(row=1, column=1)
lbl_s_2.config(font=labelfont)
# b1_button = Button(centerLeftframe, text ="Geeks1", bg="BLUE", fg ="red", width=5, height=5)
# b1_button.grid(row=1, column=0) #pack( side = LEFT)
# b1a_button = Button(centerLeftframe, text ="Geeks1a", bg="BLUE", fg ="red", width=5, height=5)
# b1a_button.grid(row=1, column=1) #pack( side = LEFT)
# b1b_button = Button(centerLeftframe, text ="Geeks1a", bg="BLUE", fg ="red", width=5, height=5)
# b1b_button.grid(row=1, column=2) #pack( side = LEFT)
# b1c_button = Button(centerLeftframe, text ="Geeks1", bg="BLUE", fg ="red", width=5, height=5)
# b1c_button.grid(row=2, column=0) #pack( side = LEFT)
# b1d_button = Button(centerLeftframe, text ="Geeks1a", bg="BLUE", fg ="red", width=5, height=5)
# b1d_button.grid(row=2, column=1) #pack( side = LEFT)
# b1e_button = Button(centerLeftframe, text ="Geeks1a", bg="BLUE", fg ="red", width=5, height=5)
# b1e_button.grid(row=2, column=2) #pack( side = LEFT)
  
# b2_button = Button(centerCenterframe, text ="Geeks2", fg ="brown", width=15)
# b2_button.pack( side = LEFT,fill=BOTH, expand = 1 )
  
# b3_button = Button(centerRightframe, text ="Geeks3", fg ="blue", width=15)
# b3_button.pack( side = LEFT,fill=BOTH, expand = 1 )
  
# b4_button = Button(bottomframe, text ="Geeks4", fg ="green", height=5)
# b4_button.pack(side = LEFT,fill=BOTH, expand = 1)
  
# b5_button = Button(bottomframe, text ="Geeks5", fg ="green", height=5)
# b5_button.pack(side = LEFT,fill=BOTH, expand = 1)
  
# b6_button = Button(bottomframe, text ="Geeks6", bg ="green", height=10)
# b6_button.pack(side = LEFT, fill=BOTH, expand = 1)
  
root.mainloop()