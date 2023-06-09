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

#Create a Canvas
main_canvas = Canvas(main_frame, bg = "RED")
main_canvas.pack(side=LEFT, fill=BOTH, expand = 1)
# Add a Scrollbar to the Canvas
sb = Scrollbar(main_frame, orient=VERTICAL,command=main_canvas.yview)
sb.pack(side=RIGHT)
# Configure the Canvas
main_canvas.configure(yscrollcommand=sb.set)
main_canvas.bind('<Configure>', lambda e: main_canvas.configure(scrollregion=main_canvas.bbox("all")))
# Create another Frame inside the Canvas
inside_frame = Frame(main_frame)
top_frame = Frame(main_canvas, bg= "GREEN")
top_frame.pack(side=TOP)
lbl_Title = Label(top_frame, text="Chemistry") # inside_frame
lbl_Title.grid(row=0, column=3)
lbl_Title.config(font=titlefont)

# second_level_frame = Frame(top_frame, bg= "RED")
# second_level_frame.pack(side=LEFT)
# third_level_frame = Frame(second_level_frame)
# third_level_frame.pack(side=TOP)

# title_frame = Frame(top_frame, bg= "RED", width=2000, height=100)
# title_frame.pack(side=TOP) #grid(row=0,column=0, co5umnspan=16) # 
# # S_1_frame = Frame(second_level_frame, bg= "GREEN", width=500, height=100)
# second_level_frame = Frame(title_frame, bg= "BLUE", width=2000, height=100)
# second_level_frame.pack(side=TOP) #grid(row=0,column=0, co5umnspan=16) # 
# S_1_frame.pack(side=LEFT) #grid(row=3,column=0) # pack(side=LEFT) , sticky=W
# S_4_frame = Frame(second_level_frame, bg= "BLUE", width=500, height=100)
# S_4_frame.pack(side=LEFT) #grid(row=3,column=1) # pack(side=LEFT), sticky=W
# S_2_frame = Frame(third_level_frame, bg= "GREEN", width=500, height=100)
# S_2_frame.pack(side=LEFT) #grid(row=3,column=0) # pack(side=LEFT) , sticky=W
# S_5_frame = Frame(third_level_frame, bg= "BLUE", width=500, height=100)
# S_5_frame.pack(side=LEFT) #grid(row=3,column=1) # pack(side=LEFT), sticky=W

# btn_create_record = Button(inside_frame, text='Get Record', command=get_record)
# btn_create_record.grid(row=3, column=2)
# btn_create_record.config(font=buttonfont)
# btn_create_record.bind("<<ComboboxSelected>>", retrieve_record)
# btn_create_record = Button(inside_frame, text='Previous Record', command=get_record)
# btn_create_record.grid(row=3, column=3)
# btn_create_record.config(font=buttonfont)
# btn_create_record.bind("<<ComboboxSelected>>", previous_record)
# btn_create_record = Button(inside_frame, text='Next Record', command=get_record)
# btn_create_record.grid(row=3, column=4)
# btn_create_record.config(font=buttonfont)
# btn_create_record.bind("<<ComboboxSelected>>", next_record)
# btn_show_instructions = Button(inside_frame, text='Show Instructions', command=get_record)
# btn_show_instructions.grid(row=2, column=6)
# btn_show_instructions.config(font=labelfont)
# #btn_show_instructions.bind("<<ComboboxSelected>>", show_hide_instructions)

# lbl_LU_Compound = Label(inside_frame, text="   Look up compound:")
# lbl_LU_Compound.grid(row=6, column=0)
# lbl_LU_Compound.config(font=labelfont)
# cb_LU_Compound = Combobox(inside_frame, values=compound_formula_string, width=12)
# cb_LU_Compound.grid(row=6, column=1)
# cb_LU_Compound.config(font=entryfont)

# # Create a search for and retrieve a compount
# lbl_LU_Process = Label(inside_frame, text="   Look up process:")
# lbl_LU_Process.grid(row=6, column=2)
# lbl_LU_Process.config(font=labelfont)
# cb_LU_Process = Combobox(inside_frame, values=major_process_list, width=12)
# cb_LU_Process.grid(row=6, column=3)
# cb_LU_Process.config(font=entryfont)
# # Create a search for and retrieve a process
# lbl_LU_Environment = Label(inside_frame, text="   Look up environment:", width=22)
# lbl_LU_Environment.grid(row=6, column=4)
# lbl_LU_Environment.config(font=labelfont)
# cb_LU_Environment = Combobox(inside_frame, values=environment, width=12)
# cb_LU_Environment.grid(row=6, column=5)
# cb_LU_Environment.config(font=entryfont)

# lbl_Select_M_Process = Label(inside_frame, text="   Select major process", width=20)
# lbl_Select_M_Process.grid(row=7, column=0)
# lbl_Select_M_Process.config(font=labelfont)
# cb_Select_M_Process: Combobox = Combobox(inside_frame, values=major_process_list, textvariable=major_process_selected, width=12)
# cb_Select_M_Process.grid(row=7, column=1)
# cb_Select_M_Process.config(font=entryfont)
# lbl_Select_m_Process = Label(inside_frame, text="   Select minor process", width=20)
# lbl_Select_m_Process.grid(row=7, column=2)
# lbl_Select_m_Process.config(font=labelfont)
# cb_Select_m_Process: Combobox = Combobox(inside_frame, values=minor_process_list, textvariable=minor_process_selected, width=12)
# cb_Select_m_Process.grid(row=7, column=3)
# cb_Select_m_Process.config(font=entryfont)
# cb_Select_m_Process.bind("<<ComboboxSelected>>", minor_process_selected)
# lbl_Select_Environment = Label(inside_frame, text="   Select environment:", width=22)
# lbl_Select_Environment.grid(row=7, column=4)
# lbl_Select_Environment.config(font=titlefont)
# cb_Select_Environment: Combobox = Combobox(inside_frame, values=environment, width=12)
# cb_Select_Environment.grid(row=7, column=5)
# cb_Select_Environment.config(font=entryfont)

main_canvas.create_window((0,0), window = main_frame, anchor = "nw")

if __name__ == '__main__':
    root.mainloop()
