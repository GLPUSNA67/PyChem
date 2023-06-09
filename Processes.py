
def create_record():
    ''' print("Pressed create_record button") '''


def get_record():
    ''' print("Pressed get_record button") '''


def retrieve_record():
    ''' print("Pressed retrieve_record button") '''


def previous_record():
    ''' print("Pressed previous_record button") '''


def next_record():
    ''' print("Pressed next_record button") '''


def update_record():
    ''' print("Pressed update_record button") '''

def check_entry_changes():
    print('1126 check_entry_changes function entered.')
# def print_R1():
#     """ Print the record of the first eci to verify record."""
#     print("dbr['R1']['eci_name'] is ", dbr['R1']['eci_1_name'])
#     print("dbr['R1']['eci_1_type'] is ", dbr['R1']['eci_1_type'])
#     print("dbr['R1']['eci_1_formula'] is ", dbr['R1']['eci_1_formula'])
#     print("dbr['R1']['eci_1_name'] is ", dbr['R1']['eci_1_name'])
#     print("dbr['R1']['eci_1_units'] is ", dbr['R1']['eci_1_units'])
#     print("dbr['R1']['eci_1_qty'] is ", dbr['R1']['eci_1_qty'])
#     print("dbr['R1']['eci_1_M_qty'] is ", dbr['R1']['eci_1_M_qty'])
#     print("dbr['R1']['eci_1_temp_display_units'] is ", dbr['R1']['eci_1_temp_display_units'])
#     print("dbr['R1']['eci_1_temp_calc_units'] is ", dbr['R1']['eci_1_temp_calc_units'])
#     print("dbr['R1']['eci_1_temp_display_qty'] is ", dbr['R1']['eci_1_temp_display_qty'])
#     print("dbr['R1']['eci_1_temp_calc_qty'] is ", dbr['R1']['eci_1_temp_calc_qty'])
#     print("dbr['R1']['eci_1_press_display_units'] is ", dbr['R1']['eci_1_press_display_units'])
#     print("dbr['R1']['eci_1_press_calc_units'] is ", dbr['R1']['eci_1_press_calc_units'])
#     print("dbr['R1']['eci_1_press_display_qty'] is ", dbr['R1']['eci_1_press_display_qty'])
#     print("dbr['R1']['eci_1_press_calc_qty'] is ", dbr['R1']['eci_1_press_calc_qty'])
#     print("end of dbr['R1']['eci_1_formula'] print function.")def calc_temp(eci):
    """ convert K to K and return it."""
    qty = float(eci_d[eci]['temp_display_qty'])
    units = eci_d[eci]['temp_display_units']
    if units == 'K':
        return qty
    elif units == 'C':
        return qty + 273.15
    elif units == 'F':
        return  (5/9 * qty) + 459.67

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