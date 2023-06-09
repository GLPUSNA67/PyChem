dbr = {}
''' Define the record dictionary 
'''
r1 = dict(name= 'Record 1', id= 1, compound= 'None', process= 'None', major_process= 'None', minor_process= 'None', environment= 'None',
          equipment = "", energy_type = "", energy_amount = "", catalyst = "", side_effects = "", by_products = "",
          variables = "", variable_values = "", explanation = "", eci_name = "",
          eci_1_type = "", eci_1_formula= "", eci_1_name = "", eci_1_units = "grams", eci_1_qty = "", eci_1_M_qty = "", eci_1_valence = "",
          eci_1_temp_display_units = "C", eci_1_temp_calc_units = "K", eci_1_temp_display_qty = "", eci_1_temp_calc_qty = "",
          eci_1_press_display_units = "atm", eci_1_press_calc_units = "atm", eci_1_press_display_qty = "", eci_1_press_calc_qty = "",
          eci_2_type = "", eci_2_formula= "", eci_2_name = "", eci_2_units = "grams", eci_2_qty = "", eci_2_M_qty = "", eci_2_valence = "",
          eci_2_temp_display_units = "C", eci_2_temp_calc_units = "K", eci_2_temp_display_qty = "", eci_2_temp_calc_qty = "",
          eci_2_press_display_units = "atm", eci_2_press_calc_units = "atm", eci_2_press_display_qty = "", eci_2_press_calc_qty = "",
          eci_3_type = "", eci_3_formula= "", eci_3_name = "", eci_3_units = "grams", eci_3_qty = "", eci_3_M_qty = "", eci_3_valence = "",
          eci_3_temp_display_units = "C", eci_3_temp_calc_units = "K", eci_3_temp_display_qty = "", eci_3_temp_calc_qty = "",
          eci_3_press_display_units = "atm", eci_3_press_calc_units = "atm", eci_3_press_display_qty = "", eci_3_press_calc_qty = "",
          eci_4_type = "", eci_4_formula= "", eci_4_name = "", eci_4_units = "grams", eci_4_qty = "", eci_4_M_qty = "", eci_4_valence = "",
          eci_4_temp_display_units = "C", eci_4_temp_calc_units = "K", eci_4_temp_display_qty = "", eci_4_temp_calc_qty = "",
          eci_4_press_display_units = "atm", eci_4_press_calc_units = "atm", eci_4_press_display_qty = "", eci_4_press_calc_qty = "",
          eci_5_type = "", eci_5_formula= "", eci_5_name = "", eci_5_units = "grams", eci_5_qty = "", eci_5_M_qty = "", eci_5_valence = "",
          eci_5_temp_display_units = "atm", eci_5_temp_calc_units = "K", eci_5_temp_display_qty = "", eci_5_temp_calc_qty = "",
          eci_5_press_display_units = "C", eci_5_press_calc_units = "atm", eci_5_press_display_qty = "", eci_5_press_calc_qty = "",
          eci_6_type = "", eci_6_formula= "atm", eci_6_name = "", eci_6_units = "grams", eci_6_qty = "", eci_6_M_qty = "", eci_6_valence = "",
          eci_6_temp_display_units = "C", eci_6_temp_calc_units = "K", eci_6_temp_display_qty = "", eci_6_temp_calc_qty = "",
          eci_6_press_display_units = "atm", eci_6_press_calc_units = "atm", eci_6_press_display_qty = "", eci_6_press_calc_qty = "",)

dbr['R1'] = r1
H = dict(id= 1, symbol= 'H', name= 'Hydrogen', atomic_number= 1, mass= 1.008, period= 1, row= 1, column= 1, _group= '1A 7A', protons= 1, neutrons= 0, electrons= 1, _1s= 1, _2s= 0, _2p= 0, _3s= 0, _3p= 0, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-72', density= '0.00008988', electronegativity= '2.1', melt= '14.01', boil= '-252.76', e_fusion= 'ef', e_vapor= 'ev', t_crit= '-240.17', p_crit= '12.77', valence= '1 -1', a_radius= '53')
He = dict(id= 2, symbol= 'He', name= 'Helium', atomic_number= 2, mass= 4.002602, period= 1, row= 1, column= 18, _group= '8A', protons= 2, neutrons= 2, electrons= 2, _1s= 2, _2s= 0, _2p= 0, _3s= 0, _3p= 0, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '20', density= '0.0001785', electronegativity= '0.0', melt= 'NULL', boil= '-268.94', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '-267.9550', p_crit= '2.261', valence= '0', a_radius= '31')
Li = dict(id= 3, symbol= 'Li', name= 'Lithium', atomic_number= 3, mass= 6.941, period= 2, row= 2, column= 1, _group= '1A', protons= 3, neutrons= 3, electrons= 3, _1s= 2, _2s= 1, _2p= 0, _3s= 0, _3p= 0, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-60', density= '0.535', electronegativity= '1.0', melt= '180.50', boil= '1342', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '2950', p_crit= '67', valence= '1', a_radius= '167')
Be = dict(id= 4, symbol= 'Be', name= 'Beryllium', atomic_number= 4, mass= 9.012182, period= 2, row= 2, column= 2, _group= '2A', protons= 4, neutrons= 4, electrons= 4, _1s= 2, _2s= 2, _2p= 0, _3s= 0, _3p= 0, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '240', density= '1.848', electronegativity= '1.5', melt= '1287', boil= '2468', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '4932', p_crit= 'NULL', valence= '2', a_radius= '112')
B = dict(id= 5, symbol= 'B', name= 'Boron', atomic_number= 5, mass= 10.8111, period= 2, row= 2, column= 13, _group= '3A', protons= 5, neutrons= 5, electrons= 5, _1s= 2, _2s= 2, _2p= 1, _3s= 0, _3p= 0, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-23', density= '2.460', electronegativity= '2.0', melt= '2077', boil= '4000', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'NULL', p_crit= 'NULL', valence= '3', a_radius= '87')
C = dict(id= 6, symbol= 'C', name= 'Carbon', atomic_number= 6, mass= 12.0107, period= 2, row= 2, column= 14, _group= '4A', protons= 6, neutrons= 6, electrons= 6, _1s= 2, _2s= 2, _2p= 2, _3s= 0, _3p= 0, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-123', density= '2.260', electronegativity= '2.5', melt= '4489', boil= '3825', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'NULL', p_crit= 'NULL', valence= '4 3 2 1 0 -1 -2 -3 -4', a_radius= '67')
N = dict(id= 7, symbol= 'N', name= 'Nitrogen', atomic_number= 7, mass= 14.0087, period= 2, row= 2, column= 15, _group= '5A', protons= 7, neutrons= 7, electrons= 7, _1s= 2, _2s= 2, _2p= 3, _3s= 0, _3p= 0, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '0', density= '0.001251', electronegativity= '3.0', melt= '-210.0', boil= '-195.795', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '-146.89', p_crit= '33.54', valence= '5 4 3 2 1 -1 -2 -3', a_radius= '56')
O = dict(id= 8, symbol= 'O', name= 'Oxygen', atomic_number= 8, mass= 15.9994, period= 2, row= 2, column= 16, _group= '6A', protons= 8, neutrons= 8, electrons= 8, _1s= 2, _2s= 2, _2p= 4, _3s= 0, _3p= 0, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-141', density= '0.001429', electronegativity= '3.5', melt= '-218.79', boil= '-182.962', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '-118.38', p_crit= '50.14', valence= '-1 -2', a_radius= '48')
F = dict(id= 9, symbol= 'F', name= 'Fluorine', atomic_number= 9, mass= 18.9984032, period= 2, row= 2, column= 17, _group= '7A', protons= 9, neutrons= 9, electrons= 9, _1s= 2, _2s= 2, _2p= 5, _3s= 0, _3p= 1, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-322', density= '0.001696', electronegativity= '4.0', melt= '-219.67', boil= '-188.11', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '-128.74', p_crit= '5.1724', valence= '-1', a_radius= '42')
Ne = dict(id= 10, symbol= 'Ne', name= 'Neon', atomic_number= 10, mass= 20.1797, period= 2, row= 2, column= 18, _group= '8A', protons= 10, neutrons= 10, electrons= 10, _1s= 2, _2s= 2, _2p= 6, _3s= 0, _3p= 0, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '30', density= '0.000900', electronegativity= '0.0', melt= '-248.59', boil= '-246.046', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '-228.6580', p_crit= '26.86', valence= '0', a_radius= '38')
Na = dict(id= 11, symbol= 'Na', name= 'Sodium', atomic_number= 11, mass= 22.989770, period= 3, row= 3, column= 1, _group= '1A', protons= 11, neutrons= 11, electrons= 11, _1s= 2, _2s= 2, _2p= 6, _3s= 1, _3p= 0, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-53', density= '0.968', electronegativity= '0.9', melt= '97.794', boil= '882.940', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '2300', p_crit= '35', valence= '1', a_radius= '190')
Mg = dict(id= 12, symbol= 'Mg', name= 'Magnesium', atomic_number= 12, mass= 24.3050, period= 3, row= 3, column= 2, _group= '2A', protons= 12, neutrons= 12, electrons= 12, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 0, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '230', density= '1.738', electronegativity= '1.2', melt= '650', boil= '1090', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'NULL', p_crit= 'NULL', valence= '2', a_radius= '145')
Al = dict(id= 13, symbol= 'Al', name= 'Aluminum', atomic_number= 13, mass= 26.981538, period= 3, row= 3, column= 13, _group= '3A', protons= 13, neutrons= 13, electrons= 13, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 1, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-44', density= '2.7', electronegativity= '1.5', melt= '660.323', boil= '2519', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '6427', p_crit= 'NULL', valence= '3', a_radius= '118')
Si = dict(id= 14, symbol= 'Si', name= 'Silicon', atomic_number= 14, mass= '28.0855', period= 3, row= 3, column= 14, _group= '4A', protons= 14, neutrons= 14, electrons= 14, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 2, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-120', density= '2.330', electronegativity= '1.8', melt= '1414', boil= '3265', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'NULL', p_crit= 'NULL', valence= '4', a_radius= '111')
P = dict(id= 15, symbol= 'P', name= 'Phosphorus', atomic_number= 15, mass= '30.973761', period= 3, row= 3, column= 15, _group= '5A, 7A', protons= 15, neutrons= 15, electrons= 15, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 3, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-74', density= '1.823', electronegativity= '2.1', melt= '44.15 579.2', boil= '280.5 431', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '721', p_crit= 'NULL', valence= '5 3 -3', a_radius= '98')
S = dict(id= 16, symbol= 'S', name= 'Sulfur', atomic_number= 16, mass= '32.065', period= 3, row= 3, column= 16, _group= '6A', protons= 16, neutrons= 16, electrons= 16, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 4, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-201', density= '1.960', electronegativity= '2.5', melt= '95.2 115.21', boil= '4461', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '1041', p_crit= 'NULL', valence= '6 4 -2', a_radius= '88')
Cl = dict(id= 17, symbol= 'Cl', name= 'Chlorine', atomic_number= 17, mass= '35.453', period= 3, row= 3, column= 17, _group= '7A', protons= 17, neutrons= 17, electrons= 17, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 5, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-348', density= '0.003214', electronegativity= '3.0', melt= '-101.5', boil= '-34.03', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '143.9', p_crit= '78.1', valence= '7 5 3 1 -1', a_radius= '79')
Ar = dict(id= 18, symbol= 'Ar', name= 'Argon', atomic_number= 18, mass= '39.948', period= 3, row= 3, column= 18, _group= '8A', protons= 18, neutrons= 18, electrons= 18, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '35', density= '0.001784', electronegativity= '0.0', melt= '-189.34', boil= '-185.854', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '-122.463', p_crit= '4.863', valence= '0', a_radius= '71')
K = dict(id= 19, symbol= 'K', name= 'Potassium', atomic_number= 19, mass= '39.0983', period= 4, row= 4, column= 1, _group= '1A', protons= 19, neutrons= 19, electrons= 19, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 1, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-48', density= '0.856', electronegativity= '0.8', melt= '63.5', boil= '759', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '1950', p_crit= '16', valence= '1', a_radius= '243')
Ca = dict(id= 20, symbol= 'Ca', name= 'Calcium', atomic_number= 20, mass= '40.078', period= 4, row= 4, column= 2, _group= '2A', protons= 20, neutrons= 20, electrons= 20, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '150', density= '1.550', electronegativity= '1.0', melt= '842', boil= '1484', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'NULL', p_crit= 'NULL', valence= '2', a_radius= '194')
Sc = dict(id= 21, symbol= 'Sc', name= 'Scandium', atomic_number= 21, mass= '44.955910', period= 4, row= 4, column= 3, _group= '3B', protons= 21, neutrons= 21, electrons= 21, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 1, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '2.985', electronegativity= '1.3', melt= '1541', boil= '2836', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'NULL', p_crit= 'NULL', valence= 'NULL', a_radius= '184')
Ti = dict(id= 22, symbol= 'Ti', name= 'Titanium', atomic_number= 22, mass= '47.867', period= 4, row= 4, column= 4, _group= '4B', protons= 22, neutrons= 22, electrons= 22, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 2, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '4.507', electronegativity= '1.5', melt= '1670', boil= '3287', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'NULL', p_crit= 'NULL', valence= 'NULL', a_radius= '176')
V = dict(id= 23, symbol= 'V', name= 'Vanadium', atomic_number= 23, mass= '50.9415', period= 4, row= 4, column= 5, _group= '5B', protons= 23, neutrons= 23, electrons= 23, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 3, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '6.110', electronegativity= '1.6', melt= '1910', boil= '3407', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'NULL', p_crit= 'NULL', valence= 'NULL', a_radius= '171')
Cr = dict(id= 24, symbol= 'Cr', name= 'Chromium', atomic_number= 24, mass= '51.9961', period= 4, row= 4, column= 6, _group= '6B', protons= 24, neutrons= 24, electrons= 24, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 1, _3d= 5, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '7.140', electronegativity= '1.6', melt= '1907', boil= '2671', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'NULL', p_crit= 'NULL', valence= 'NULL', a_radius= '166')
Mn = dict(id= 25, symbol= 'Mn', name= 'Manganese', atomic_number= 25, mass= '54.938049', period= 4, row= 4, column= 7, _group= '7B', protons= 25, neutrons= 25, electrons= 25, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 5, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '7.470', electronegativity= '1.5', melt= '1246', boil= '2061', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '4052', p_crit= 'NULL', valence= 'NULL', a_radius= '161')
Fe = dict(id= 26, symbol= 'Fe', name= 'Iron', atomic_number= 26, mass= '55.845', period= 4, row= 4, column= 8, _group= '8B', protons= 26, neutrons= 26, electrons= 26, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 6, _4p= 2, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '7.874', electronegativity= '1.8', melt= '1538', boil= '2861', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '9067', p_crit= 'NULL', valence= 'NULL', a_radius= '156')
Co = dict(id= 27, symbol= 'Co', name= 'Cobalt', atomic_number= 27, mass= '58.9932', period= 4, row= 4, column= 9, _group= '8B', protons= 27, neutrons= 27, electrons= 27, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 7, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '8.9', electronegativity= '1.9', melt= '1495', boil= '2927', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'NULL', p_crit= 'NULL', valence= 'NULL', a_radius= '152')
Ni = dict(id= 28, symbol= 'Ni', name= 'Nickel', atomic_number= 28, mass= '58.6934', period= 4, row= 4, column= 10, _group= '8B', protons= 28, neutrons= 28, electrons= 28, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 8, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '8.908', electronegativity= '1.9', melt= '1455', boil= '2913', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'NULL', p_crit= 'NULL', valence= 'NULL', a_radius= '149')
Cu = dict(id= 29, symbol= 'Cu', name= 'Copper', atomic_number= 29, mass= '63.546', period= 4, row= 4, column= 11, _group= '1B', protons= 29, neutrons= 29, electrons= 29, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 1, _3d= 10, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '8.920', electronegativity= '1.9', melt= '1084.62', boil= '2560', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'NULL', p_crit= 'NULL', valence= 'NULL', a_radius= '145')
Zn = dict(id= 30, symbol= 'Zn', name= 'Zinc', atomic_number= 30, mass= '65.409', period= 4, row= 4, column= 12, _group= '2B', protons= 30, neutrons= 30, electrons= 30, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '7.140', electronegativity= '1.6', melt= '419.527', boil= '907', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'NULL', p_crit= 'NULL', valence= '2', a_radius= '142')
Ga = dict(id= 31, symbol= 'Ga', name= 'Gallium', atomic_number= 31, mass= '69.723', period= 4, row= 4, column= 13, _group= '3A', protons= 31, neutrons= 31, electrons= 31, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 1, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-40', density= '5.904', electronegativity= '1.6', melt= '29.7646', boil= '2229', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'NULL', p_crit= 'NULL', valence= '3', a_radius= '136')
Ge = dict(id= 32, symbol= 'Ge', name= 'Germanium', atomic_number= 32, mass= '72.64', period= 4, row= 4, column= 14, _group= '4A', protons= 32, neutrons= 32, electrons= 32, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 2, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-116', density= '5.323', electronegativity= '1.8', melt= '938.25', boil= '2833', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '4', a_radius= '125')
As = dict(id= 33, symbol= 'As', name= 'Arsenic', atomic_number= 33, mass= '74.92160', period= 4, row= 4, column= 15, _group= '5A', protons= 33, neutrons= 33, electrons= 33, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 3, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-77', density= '5.727', electronegativity= '2.0', melt= '817', boil= '616', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '5 3 -3', a_radius= '114')
Se = dict(id= 34, symbol= 'Se', name= 'Selenium', atomic_number= 34, mass= '778.96', period= 4, row= 4, column= 16, _group= '6A', protons= 34, neutrons= 34, electrons= 34, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 4, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-195', density= '4.819', electronegativity= '2.4', melt= '220.8', boil= '685', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '6 4 -2', a_radius= '103')
Br = dict(id= 35, symbol= 'Br', name= 'Bromine', atomic_number= 35, mass= '79.904', period= 4, row= 4, column= 17, _group= '7A', protons= 35, neutrons= 35, electrons= 35, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 5, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-324', density= '3.120', electronegativity= '2.8', melt= '-7.2', boil= '58.8', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '7 5 3 1 -1', a_radius= '94')
Kr = dict(id= 36, symbol= 'Kr', name= 'Krypton', atomic_number= 36, mass= '83.798', period= 4, row= 4, column= 18, _group= '8A', protons= 36, neutrons= 36, electrons= 36, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '40', density= '0.00375', electronegativity= '0', melt= '-157.37', boil= '-153.415', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '4 2', a_radius= '88')
Rb = dict(id= 37, symbol= 'Rb', name= 'Rubidium', atomic_number= 37, mass= '85.4678', period= 5, row= 5, column= 1, _group= '1A', protons= 37, neutrons= 37, electrons= 37, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 0, _5s= 1, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-46', density= '1.532', electronegativity= '0.8', melt= '39.30', boil= '688', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '1', a_radius= '265')
Sr = dict(id= 38, symbol= 'Sr', name= 'Strontium', atomic_number= 38, mass= '87.62', period= 5, row= 5, column= 2, _group= '2A', protons= 38, neutrons= 38, electrons= 38, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 0, _5s= 2, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '160', density= '2.630', electronegativity= '1.0', melt= '777', boil= '1377', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '2', a_radius= '219')
Y = dict(id= 39, symbol= 'Y', name= 'Yttrium', atomic_number= 39, mass= '88.90585', period= 5, row= 5, column= 3, _group= '3B', protons= 39, neutrons= 39, electrons= 30, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 1, _5s= 2, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '4.472', electronegativity= '1.2', melt= '1522', boil= '3345', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= 'NULL', a_radius= '212')
Zr = dict(id= 40, symbol= 'Zr', name= 'Zirconium', atomic_number= 40, mass= '91.224', period= 5, row= 5, column= 4, _group= '4B', protons= 40, neutrons= 40, electrons= 40, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 2, _5s= 2, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '6.511', electronegativity= '1.4', melt= '1854', boil= '4406', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= 'NULL', a_radius= '206')
Nb = dict(id= 41, symbol= 'Nb', name= 'Niobium', atomic_number= 41, mass= '92.90638', period= 5, row= 5, column= 5, _group= '5B', protons= 41, neutrons= 41, electrons= 41, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 4, _5s= 1, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '8.570', electronegativity= '1.6', melt= '2477', boil= '4741', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= 'NULL', a_radius= '198')
Mo = dict(id= 42, symbol= 'Mo', name= 'Molybdenum', atomic_number= 42, mass= '95.94', period= 5, row= 5, column= 6, _group= '6B', protons= 42, neutrons= 42, electrons= 42, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 5, _5s= 1, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '10.280', electronegativity= '1.8', melt= '2622', boil= '4639', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= 'NULL', a_radius= '190')
Tc = dict(id= 43, symbol= 'Tc', name= 'Technetium', atomic_number= 43, mass= '98', period= 5, row= 5, column= 7, _group= '7B', protons= 43, neutrons= 43, electrons= 43, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 6, _5s= 1, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '11.5', electronegativity= '1.9', melt= '2157', boil= '4262', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= 'NULL', a_radius= '183')
Ru = dict(id= 44, symbol= 'Ru', name= 'Ruthenium', atomic_number= 44, mass= '101.07', period= 5, row= 5, column= 8, _group= '8B', protons= 44, neutrons= 44, electrons= 44, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 7, _5s= 1, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '12.370', electronegativity= '2.2', melt= '2333', boil= '4147', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= 'NULL', a_radius= '178')
Rh = dict(id= 45, symbol= 'Rh', name= 'Rhodium', atomic_number= 45, mass= '102.90550', period= 5, row= 5, column= 9, _group= '8B', protons= 45, neutrons= 45, electrons= 45, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 8, _5s= 1, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '12.450', electronegativity= '2.2', melt= '1963', boil= '3695', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= 'NULL', a_radius= '173')
Pd = dict(id= 46, symbol= 'Pd', name= 'Palladium', atomic_number= 46, mass= '106.42', period= 5, row= 5, column= 10, _group= '8B', protons= 46, neutrons= 46, electrons= 46, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '12.023', electronegativity= '2.2', melt= '1554.8', boil= '2963', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= 'NULL', a_radius= '169')
Ag = dict(id= 47, symbol= 'Ag', name= 'Silver', atomic_number= 47, mass= '107.8682', period= 5, row= 5, column= 11, _group= '1B', protons= 47, neutrons= 47, electrons= 47, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 1, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '10.490', electronegativity= '1.9', melt= '961.78', boil= '2162', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '6137', p_crit= 'Press Crit', valence= 'NULL', a_radius= '165')
Cd = dict(id= 48, symbol= 'Cd', name= 'Cadmium', atomic_number= 48, mass= '112.411', period= 5, row= 5, column= 12, _group= '2B', protons= 48, neutrons= 48, electrons= 48, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '8.650', electronegativity= '1.7', melt= '321.069', boil= '767', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '2', a_radius= '161')
La = dict(id= 57, symbol= 'La', name= 'Lanthanium', atomic_number= 57, mass= '138.90547', period= 6, row= 6, column= 3, _group= '19', protons= 57, neutrons= 82, electrons= 57, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _5d= 1, _6p= 0, _7s= 0, affinity= '40', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Ce = dict(id= 58, symbol= 'Ce', name= 'Cerium', atomic_number= 58, mass= '140.166', period= 6, row= 6, column= 3, _group= '19', protons= 58, neutrons= 82, electrons= 58, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 1, _5d= 1, _6p= 0, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Pr = dict(id= 59, symbol= 'Pr', name= 'Praseodymium', atomic_number= 59, mass= '140.907', period= 6, row= 6, column= 3, _group= '19', protons= 59, neutrons= 82, electrons= 59, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 3, _5d= 0, _6p= 0, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Nd = dict(id= 60, symbol= 'Nd', name= 'Neodynium', atomic_number= 60, mass= '144.242', period= 6, row= 6, column= 3, _group= '19', protons= 60, neutrons= 84, electrons= 60, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 4, _5d= 0, _6p= 0, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '1010.0', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Pm = dict(id= 61, symbol= 'Pm', name= 'Promethium', atomic_number= 61, mass= '145', period= 6, row= 6, column= 3, _group= '19', protons= 61, neutrons= 84, electrons= 61, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 5, _5d= 0, _6p= 0, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Sm = dict(id= 62, symbol= 'Sm', name= 'Samarium', atomic_number= 62, mass= '150.36', period= 6, row= 6, column= 3, _group= '19', protons= 62, neutrons= 88, electrons= 62, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 6, _5d= 0, _6p= 0, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Eu = dict(id= 63, symbol= 'Eu', name= 'Europium', atomic_number= 63, mass= '151.964', period= 6, row= 6, column= 3, _group= '19', protons= 63, neutrons= 89, electrons= 63, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 7, _5d= 0, _6p= 0, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '822.0', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Gd = dict(id= 64, symbol= 'Gd', name= 'Gadolinium', atomic_number= 64, mass= '157.25', period= 6, row= 6, column= 3, _group= '19', protons= 64, neutrons= 93, electrons= 64, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 7, _5d= 1, _6p= 0, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Tb = dict(id= 65, symbol= 'Tb', name= 'Terbium', atomic_number= 65, mass= '158.92535', period= 6, row= 6, column= 3, _group= '19', protons= 65, neutrons= 94, electrons= 65, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 9, _5d= 0, _6p= 0, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Dy = dict(id= 66, symbol= 'Dy', name= 'Dysprosium', atomic_number= 66, mass= '162.500', period= 6, row= 6, column= 3, _group= '19', protons= 66, neutrons= 97, electrons= 66, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 10, _5d= 0, _6p= 0, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Ho = dict(id= 67, symbol= 'Ho', name= 'Holmium', atomic_number= 67, mass= '164.93033', period= 6, row= 6, column= 3, _group= '19', protons= 67, neutrons= 98, electrons= 67, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 11, _5d= 0, _6p= 0, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Er = dict(id= 68, symbol= 'Er', name= 'Erbium', atomic_number= 68, mass= '167.259', period= 6, row= 6, column= 3, _group= '19', protons= 68, neutrons= 99, electrons= 68, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 12, _5d= 0, _6p= 0, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Tm = dict(id= 69, symbol= 'Tm', name= 'Thulium', atomic_number= 69, mass= '168.93422', period= 6, row= 6, column= 3, _group= '19', protons= 69, neutrons= 100, electrons= 69, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 13, _5d= 0, _6p= 0, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Yb = dict(id= 70, symbol= 'Yb', name= 'Ytterbium', atomic_number= 70, mass= '173.054', period= 6, row= 6, column= 3, _group= '19', protons= 70, neutrons= 103, electrons= 70, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 0, _6p= 0, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Lu = dict(id= 71, symbol= 'Lu', name= 'Lutetium', atomic_number= 71, mass= '174.9668', period= 6, row= 6, column= 3, _group= '19', protons= 71, neutrons= 104, electrons= 71, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 1, _6p= 0, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Hf = dict(id= 72, symbol= 'Hf', name= 'Hafnium', atomic_number= 72, mass= '178.49', period= 6, row= 6, column= 4, _group= '4B', protons= 72, neutrons= 106, electrons= 72, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 2, _6p= 0, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Ta = dict(id= 73, symbol= 'Ta', name= 'Tantalum', atomic_number= 73, mass= '180.94788', period= 6, row= 6, column= 5, _group= '5B', protons= 73, neutrons= 108, electrons= 73, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 3, _6p= 0, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
W = dict(id= 74, symbol= 'W', name= 'Tungsten', atomic_number= 74, mass= '183.84', period= 6, row= 6, column= 6, _group= '6B', protons= 74, neutrons= 110, electrons= 74, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 4, _6p= 0, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Re = dict(id= 75, symbol= 'Re', name= 'Rhenium', atomic_number= 75, mass= '186.207', period= 6, row= 6, column= 7, _group= '7B', protons= 75, neutrons= 111, electrons= 75, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 5, _6p= 0, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Os = dict(id= 76, symbol= 'Os', name= 'Osmium', atomic_number= 76, mass= '190.23', period= 6, row= 6, column= 8, _group= '8B', protons= 76, neutrons= 114, electrons= 76, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 6, _6p= 0, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Ir = dict(id= 77, symbol= 'Ir', name= 'Iridium', atomic_number= 77, mass= '192.217', period= 6, row= 6, column= 8, _group= '8B', protons= 77, neutrons= 114, electrons= 77, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 7, _6p= 0, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Pt = dict(id= 78, symbol= 'Pt', name= 'Platinum', atomic_number= 78, mass= '195.084.', period= 6, row= 6, column= 10, _group= '8B', protons= 78, neutrons= 117, electrons= 78, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 1, _4f1 = 14, _5d= 9, _6p= 0, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Au = dict(id= 79, symbol= 'Au', name= 'Gold', atomic_number= 79, mass= '196.966569', period= 6, row= 6, column= 11, _group= '1B', protons= 79, neutrons= 118, electrons= 79, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 1, _4f1 = 14, _5d= 10, _6p= 0, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Hg = dict(id= 80, symbol= 'Hg', name= 'Mercury', atomic_number= 80, mass= '200.592', period= 6, row= 6, column= 12, _group= '2B', protons= 80, neutrons= 121, electrons= 80, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 0, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Tl = dict(id= 81, symbol= 'Tl', name= 'Thallium', atomic_number= 81, mass= '200.592', period= 6, row= 6, column= 12, _group= '2B', protons= 81, neutrons= 123, electrons= 81, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 1, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Pb = dict(id= 82, symbol= 'Ti', name= 'Lead', atomic_number= 82, mass= '200.592', period= 6, row= 6, column= 12, _group= '2B', protons= 82, neutrons= 125, electrons= 82, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 2, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Bi = dict(id= 83, symbol= 'Bi', name= 'Bismuth', atomic_number= 83, mass= '208.98040', period= 6, row= 6, column= 12, _group= '2B', protons= 83, neutrons= 126, electrons= 83, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 3, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Po = dict(id= 84, symbol= 'Po', name= 'Polonium', atomic_number= 84, mass= '209', period= 6, row= 6, column= 12, _group= '2B', protons= 84, neutrons= 125, electrons= 84, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 4, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
At = dict(id= 85, symbol= 'At', name= 'Astatine', atomic_number= 85, mass= '210', period= 6, row= 6, column= 12, _group= '2B', protons= 85, neutrons= 125, electrons= 85, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 5, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Rn = dict(id= 86, symbol= 'Rn', name= 'Radon', atomic_number= 86, mass= '222', period= 6, row= 6, column= 12, _group= '2B', protons= 86, neutrons= 136, electrons= 86, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Fr = dict(id= 87, symbol= 'Fr', name= 'Francium', atomic_number= 87, mass= '223', period= 7, row= 7, column= 1, _group= '1A', protons= 87, neutrons= 136, electrons= 87, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 1, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Ra = dict(id= 88, symbol= 'Ra', name= 'Radium', atomic_number= 88, mass= '226', period= 7, row= 7, column= 2, _group= '2A', protons= 88, neutrons= 138, electrons= 88, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 2, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Ac = dict(id= 89, symbol= 'Ac', name= 'Actinium', atomic_number= 89, mass= '227', period= 7, row= 7, column= 4, _group= '20', protons= 89, neutrons= 139, electrons= 89, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Th = dict(id= 90, symbol= 'Th', name= 'Thorium', atomic_number= 90, mass= '232.0377', period= 7, row= 7, column= 5, _group= '20', protons= 90, neutrons= 142, electrons= 90, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Pa = dict(id= 91, symbol= 'Pa', name= 'Protactinium', atomic_number= 91, mass= '231.03588', period= 7, row= 7, column= 6, _group= '20', protons= 91, neutrons= 140, electrons= 91, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
U = dict(id= 92, symbol= 'U', name= 'Uranium', atomic_number= 92, mass= '238.0289', period= 7, row= 7, column= 7, _group= '20', protons= 92, neutrons= 146, electrons= 92, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Np = dict(id= 93, symbol= 'Np', name= 'Neptunium', atomic_number= 93, mass= '237', period= 7, row= 7, column= 8, _group= '20', protons= 93, neutrons= 144, electrons= 93, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Pu = dict(id= 94, symbol= 'Pa', name= 'Plutonium', atomic_number= 91, mass= '244', period= 7, row= 7, column= 9, _group= '20', protons= 94, neutrons= 145, electrons= 94, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Am = dict(id= 95, symbol= 'Am', name= 'Americium', atomic_number= 91, mass= '243', period= 7, row= 7, column= 10, _group= '20', protons= 95, neutrons= 148, electrons= 95, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Cm = dict(id= 96, symbol= 'Cm', name= 'Curium', atomic_number= 91, mass= '247', period= 7, row= 7, column= 11, _group= '20', protons= 96, neutrons= 151, electrons= 96, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Bk = dict(id= 97, symbol= 'Bk', name= 'Berkelium', atomic_number= 97, mass= '247', period= 7, row= 7, column= 12, _group= '20', protons= 97, neutrons= 150, electrons= 97, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Cf = dict(id= 98, symbol= 'Cf', name= 'Californium', atomic_number= 98, mass= '251', period= 7, row= 7, column= 13, _group= '20', protons= 98, neutrons= 153, electrons= 98, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Es = dict(id= 99, symbol= 'Es', name= 'Einsteinium', atomic_number= 99, mass= '252', period= 7, row= 7, column= 14, _group= '20', protons= 99, neutrons= 153, electrons= 99, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Fm = dict(id= 100, symbol= 'Fm', name= 'Fermium', atomic_number= 101, mass= '257', period= 7, row= 7, column= 15, _group= '20', protons= 100, neutrons= 157, electrons= 100, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Md = dict(id= 101, symbol= 'Md', name= 'Mendelevium', atomic_number= 101, mass= '258', period= 7, row= 7, column= 16, _group= '20', protons= 101, neutrons= 157, electrons= 101, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
No = dict(id= 102, symbol= 'No', name= 'Nobelium', atomic_number= 102, mass= '259', period= 7, row= 7, column= 17, _group= '20', protons= 102, neutrons= 157, electrons= 102, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Lr = dict(id= 103, symbol= 'Lr', name= 'Lawrencium', atomic_number= 103, mass= '262', period= 7, row= 7, column= 18, _group= '20', protons= 103, neutrons= 159, electrons= 103, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Rf = dict(id= 104, symbol= 'Rf', name= 'Ruthorfordium', atomic_number= 104, mass= '267', period= 7, row= 7, column= 4, _group= '21', protons= 104, neutrons= 159, electrons= 104, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Db = dict(id= 105, symbol= 'Db', name= 'Dudmium', atomic_number= 105, mass= '268', period= 7, row= 7, column= 5, _group= '21', protons= 105, neutrons= 159, electrons= 105, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Sg = dict(id= 106, symbol= 'Sg', name= 'Seaborgium', atomic_number= 106, mass= '271', period= 7, row= 7, column= 6, _group= '21', protons= 106, neutrons= 159, electrons= 106, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Bh = dict(id= 107, symbol= 'Bh', name= 'Bohrium', atomic_number= 107, mass= '272', period= 7, row= 7, column= 7, _group= '21', protons= 107, neutrons= 159, electrons= 107, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Hs = dict(id= 108, symbol= 'Hs', name= 'Hassium', atomic_number= 108, mass= '270', period= 7, row= 7, column= 8, _group= '21', protons= 108, neutrons= 159, electrons= 108, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Mt = dict(id= 109, symbol= 'Mt', name= 'Meitnerium', atomic_number= 109, mass= '276', period= 7, row= 7, column= 9, _group= '21', protons= 109, neutrons= 159, electrons= 109, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Ds = dict(id= 110, symbol= 'Ds', name= 'Darmstadtium', atomic_number= 110, mass= '281', period= 7, row= 7, column= 10, _group= '21', protons= 110, neutrons= 159, electrons= 110, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Rg = dict(id= 111, symbol= 'Rg', name= 'Roentgenium', atomic_number= 111, mass= '280', period= 7, row= 7, column= 11, _group= '21', protons= 111, neutrons= 159, electrons= 111, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Cn = dict(id= 112, symbol= 'Cn', name= 'Copernicium', atomic_number= 112, mass= '285', period= 7, row= 7, column= 13, _group= '21', protons= 112, neutrons= 159, electrons= 112, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Nh = dict(id= 113, symbol= 'Nh', name= 'Nihonium', atomic_number= 113, mass= '284', period= 7, row= 7, column= 13, _group= '21', protons= 113, neutrons= 159, electrons= 113, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Fl = dict(id= 114, symbol= 'Fl', name= 'Flerovium', atomic_number= 114, mass= '289', period= 7, row= 7, column= 14, _group= '21', protons= 114, neutrons= 159, electrons= 114, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Mc = dict(id= 115, symbol= 'Mc', name= 'Moscovium', atomic_number= 115, mass= '288', period= 7, row= 7, column= 15, _group= '21', protons= 115, neutrons= 159, electrons= 115, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Lv = dict(id= 116, symbol= 'Lv', name= 'Livermorium', atomic_number= 116, mass= '293', period= 7, row= 7, column= 16, _group= '21', protons= 116, neutrons= 159, electrons= 116, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Ts = dict(id= 117, symbol= 'Ts', name= 'Tennessine', atomic_number= 117, mass= '294', period= 7, row= 7, column= 17, _group= '21', protons= 117, neutrons= 159, electrons= 117, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')
Og = dict(id= 118, symbol= 'Og', name= 'Oganesson', atomic_number= 118, mass= '294', period= 7, row= 7, column= 18, _group= '21', protons= 118, neutrons= 159, electrons= 118, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 6, _6s= 2, _4f1 = 14, _5d= 10, _6p= 6, _7s= 0, affinity= '', density= '', electronegativity= '0', melt= '', boil= '', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '', a_radius= '')

db = {}
db['H'] = H
db['He'] = He
db['Li'] = Li
db['Be'] = Be
db['B'] = B
db['C'] = C
db['N'] = N
db['O'] = O
db['F'] = F
db['Ne'] = Ne
db['Na'] = Na
db['Mg'] = Mg
db['Al'] = Al
db['Si'] = Si
db['P'] = P
db['S'] = S
db['Cl'] = Cl
db['Ar'] = Ar
db['K'] = K
db['Ca'] = Ca
db['Sc'] = Sc
db['Ti'] = Ti
db['V'] = V
db['Cr'] = Cr
db['Mn'] = Mn
db['Fe'] = Fe
db['Co'] = Co
db['Ni'] = Ni
db['Cu'] = Cu
db['Zn'] = Zn
db['Ga'] = Ga
db['Ge'] = Ge
db['As'] = As
db['Se'] = Se
db['Br'] = Br
db['Kr'] = Kr
db['Rb'] = Rb
db['Sr'] = Sr
db['Y'] = Y
db['Zr'] = Zr
db['Nb'] = Nb
db['Mo'] = Mo
db['Tc'] = Tc
db['Ru'] = Ru
db['Rh'] = Rh
db['Pd'] = Pd
db['Ag'] = Ag
db['Cd'] = Cd
db['La'] = La
db['Ce'] = Ce
db['Pr'] = Pr
db['Nd'] = Nd
db['Pm'] = Pm
db['Sm'] = Sm
db['Eu'] = Eu
db['Gd'] = Gd
db['Tb'] = Tb
db['Dy'] = Dy
db['Ho'] = Ho
db['Er'] = Er
db['Tm'] = Tm
db['Yb'] = Yb
db['Lu'] = Lu
db['Hf'] = Hf
db['Ta'] = Ta
db['W'] = W
db['Re'] = Re
db['Os'] = Os
db['Ir'] = Ir
db['Pt'] = Pt
db['Au'] = Au
db['Hg'] = Hg
db['Tl'] = Tl
db['Pb'] = Pb
db['Bi'] = Bi
db['Po'] = Po
db['At'] = At
db['Rn'] = Rn
db['Fr'] = Fr
db['Ra'] = Ra
db['Ac'] = Ac
db['Th'] = Th
db['Pa'] = Pa
db['U'] = U
db['Np'] = Np
db['Pu'] = Pu
db['Am'] = Am
db['Cm'] = Cm
db['Bk'] = Bk
db['Cf'] = Cf
db['Es'] = Es
db['Fm'] = Fm
db['Md'] = Md
db['No'] = No
db['Lr'] = Lr
db['Rf'] = Rf
db['Db'] = Db
db['Sg'] = Sg
db['Bh'] = Bh
db['Hs'] = Hs
db['Mt'] = Mt
db['Ds'] = Ds
db['Rg'] = Rg
db['Cn'] = Cn
db['Nh'] = Nh
db['Fl'] = Fl
db['Mc'] = Mc
db['Lv'] = Lv
db['Ts'] = Ts
db['Og'] = Og

# create_element_dict()
#     print(" 891 eci_1_d['type']= ", eci_1_d['type'])
    # print(" 892 eci_1_d['type']= ", cb_Select_CB1.get())
    #     cb_1_type = cb_Select_CB1.get()  # use cb_1_type as a local variable to improve readability
    # eci_d['eci_1']['type'] = cb_Select_CB1.get()
    # eci_d['eci_1']
    # dbr['R1']['eci_1_type'] = eci_1_d['type']
    # print("934 eci_d['eci_1']['type']) = ", eci_d['eci_1'])
        # print("cb_1_type is ", cb_1_type)
    ''' Both of the assignments below work. '''
    # print("eci_d['eci_1']['type'] is ", eci_d['eci_1']['type'])
    # print("eci_db['eci_1']['eci_type'] is ", cb_1_type)
    #eci_d['eci_1']['eci_type'] = cb_1_type
    '''
    Use the appropriate symbol and name lists to fill in the comboboxes.
    '''
    # cb_1_type = cb_Select_CB1.get()
    # cb_2_type = cb_Select_CB2.get()
    # cb_3_type = cb_Select_CB3.get()
    # cb_4_type = cb_Select_CB4.get()
    # cb_5_type = cb_Select_CB5.get()
    # cb_6_type = cb_Select_CB6.get()
        # dbr['R1']['eci_1_formula'] = cb_eci_1.get()
    # print("dbr['R1']['eci_1_formula'] is ", dbr['R1']['eci_1_formula'])
    # dbr['R1']['eci_1_name'] = cb_eci_1_N.get()
    # print("dbr['R1']['eci_1_name'] is ", dbr['R1']['eci_1_name'])
    ''' The following works to set units to grams.'''
    # cb_eci_1_units.set('grams')
    #cb_eci_1_units.set(eci_1_units)
    # dbr['R1']['eci_1_units'] = 'grams'
    # ''' Initial value of qty is the selected element atomic mass in grams. '''
    # dbr['R1']['eci_1_qty'] = db[eci_1.get()]['mass']
    # print("1488 dbr['R1']['eci_1_qty'] is ", dbr['R1']['eci_1_qty'])
    ''' Get the atomic mass of the selected element. then set e_eci_1_qty equal to it. '''
            # eci_1_M_qty = getdouble(e_eci_1_M_qty.get())

    ''' ********** eci_1 gives user a PVAR. Use eci_1.get() to get the actual value of eci_1 '''
    #print('eci_1 is ', eci_1.get())
    # eci_1_mass = db[eci_1.get()]['mass']    #db[eci_1]['mass']
    #print('eci_1_M_qty is ', eci_1_M_qty)
    # print('1496 eci_1_mass is ', eci_1_mass) #eci_1.get['mass'])
    # eci_1_qty = eci_1_mass  #db[eci_1.get()]['eci_1_mass']
    ''' ************************************************************ '''
    ''' The following works to inset the (atomic mass) into the quantity entry widget! '''
    ''' But, it only works if an element symbol is selected; not if the name is selected. '''
    # e_eci_1_qty.delete(0, tk.END)
    # e_eci_1_qty.insert(0, eci_1_qty)   #eci_1_mass)
    # e_eci_1_M_qty.delete(0, tk.END)
    # e_eci_1_M_qty.insert(0, 1.0)
        # cb_eci_1_units.set('grams')
    # eci_1_d['units'] = cb_eci_1_units.get()
    

    #cb_eci_1_units.set(eci_1_units)
    # dbr['R1']['eci_1_units'] = 'grams'
    # ''' Initial value of qty is the selected element atomic mass in grams. '''
    # dbr['R1']['eci_1_qty'] = db[eci_1.get()]['mass']
    # print("1443 dbr['R1']['eci_1_qty'] is ", dbr['R1']['eci_1_qty'])
    ''' Get the atomic mass of the selected element. then set e_eci_1_qty equal to it. '''
    # eci_1_M_qty = eci_d[eci]['M_qty']  #getdouble(e_eci_1_M_qty.get())

    ''' ********** eci_1 gives user a PVAR. Use eci_1.get() to get the actual value of eci_1 '''
    ''' Get the atomic mass of the selected element. then set e_eci_3_qty equal to it. '''
    # #eci_2_M_qty = getdouble(e_eci_2_M_qty.get())
    # eci_2_mass = db[eci_2.get()]['mass']    #db[eci_1]['mass']
    # #print('eci_2_M_qty is ', eci_2_M_qty)
    # print('1520 eci_2_mass is ', eci_2_mass) #eci_1.get['mass'])
    # eci_2_qty = eci_2_mass  #db[eci_1.get()]['eci_1_mass']
    # ''' ************************************************************ '''
    # ''' The following works to inset the (atomic mass) into the quantity entry widget! '''
    # ''' But, it only works if an element symbol is selected; not if the name is selected. '''
    # e_eci_2_qty.delete(0, tk.END)
    # e_eci_2_qty.insert(0, eci_2_qty)
    # e_eci_2_M_qty.delete(0, tk.END)
    # e_eci_2_M_qty.insert(0, 1.0)
        # cb_1_type = cb_Select_CB1.get()
    # cb_2_type = cb_Select_CB2.get()
    # cb_3_type = cb_Select_CB3.get()
    # cb_4_type = cb_Select_CB4.get()
    # cb_5_type = cb_Select_CB5.get()
    # cb_6_type = cb_Select_CB6.get()
    # eci_1 = cb_eci_1.get()
    # print("1647 eci_1 is ", eci)
    # eci_2 = cb_eci_2.get()
    # eci_3 = cb_eci_3.get()
    # eci_4 = cb_eci_4.get()
    # eci_5 = cb_eci_5.get()
    # eci_6 = cb_eci_6.get()
    # eci_1_name = cb_eci_1_N.get()
    # eci_2_name = cb_eci_2_N.get()
    # eci_3_name = cb_eci_3_N.get()
    # eci_4_name = cb_eci_4_N.get()
    # eci_5_name = cb_eci_5_N.get()
    # eci_6_name = cb_eci_6_N.get()
    # print("1693 eci_1_name is ", eci_1_name)
    # print("1694 eci_type is ", eci_type)
    #eci_1_d['eci'] = cb_eci_1.get()
    #eci_1_d['name'] = db[eci_1]['name'] #cb_eci_1_N.get()
    #eci_d['eci_1']['eci'] = eci_1
    #eci_d['eci_1']['name'] = db[eci_1]['name'] #eci_1_name
    #print("eci_db['eci_1']['eci'] is ", eci_db['eci_1']['eci'])
    #print("eci_db['eci_1']['name'] is ", eci_db['eci_1']['name'])
    #print("eci_1_d['eci'] is ", eci_1_d['eci'])
    #print("eci_1_d['name'] is ", eci_1_d['name'])
# # # e_eci_1_qty = Entry(inside_frame, text="", textvariable=eci_1_qty, width=10)
# # # e_eci_1_qty.grid(row=12, column=0)
# # # e_eci_1_qty.config(font=entryfont)
# # # e_eci_1_qty.bind('<Return>', eci_1_qty_adjusted)

# # cb_Select_CB1.bind("<<ComboboxSelected>>", callback1)
# # cb_Process = Combobox(root, values=process_list, width=20)
# # cb_Process.grid(row=9, column=3) # , columnspan=2
# # cb_Process.config(font=entryfont)

# lbl_eci_5 = Label(S_5_frame, text="Select Element, Compound or Ion for ComboBox 5")
# lbl_eci_5.grid(row=0, column=5, columnspan=3, sticky="w") #, sticky=W)
# lbl_eci_5.config(font=labelfont)
# cb_Select_CB5 = Combobox(S_5_frame, values=eci_cb_values, width=10)
# cb_Select_CB5.grid(row=0, column=8, sticky="w")
# cb_Select_CB5.config(font=entryfont)
# cb_Select_CB5.bind("<<ComboboxSelected>>", select_eci_5_type)
# lbl_eci_2_qty = Label(S_2_frame, text="ECI 2 Qty", width=10)
# lbl_eci_2_qty.grid(row=1, column=0, sticky="w")
# lbl_eci_2_qty.config(font=labelfont)
# lbl_eci_2_units = Label(S_2_frame, text="Units 2", width=10)
# lbl_eci_2_units.grid(row=1, column=1, sticky="w") #, sticky=W)
# lbl_eci_2_units.config(font=labelfont)
# lbl_eci_2 = Label(S_2_frame, text="ECI 2", width=10)
# lbl_eci_2.grid(row=1, column=2, sticky="w") #, sticky=W)
# lbl_eci_2.config(font=labelfont)
# lbl_eci_2_valence = Label(S_2_frame, text="Valence 2", width=10)
# lbl_eci_2_valence.grid(row=1, column=3, sticky="w") #, sticky=W)
# lbl_eci_2_valence.config(font=labelfont)
# lbl_eci_5_qty = Label(S_5_frame, text="ECI 5 Qty", width=8)
# lbl_eci_5_qty.grid(row=1, column=0, sticky="w")
# lbl_eci_5_qty.config(font=labelfont)
# lbl_eci_5_units = Label(S_5_frame, text="Units 5", width=10)
# lbl_eci_5_units.grid(row=1, column=1, sticky="w") #, sticky=W)
# lbl_eci_5_units.config(font=labelfont)
# lbl_eci_5 = Label(S_5_frame, text="ECI 5", width=10)
# lbl_eci_5.grid(row=1, column=2, sticky="w") #, sticky=W)
# lbl_eci_5.config(font=labelfont)
# lbl_eci_5_valence = Label(S_5_frame, text="Valence 5", width=10)
# lbl_eci_5_valence.grid(row=1, column=3, sticky="w") #, sticky=W)
# lbl_eci_5_valence.config(font=labelfont)
# lbl_eci_5_Molar_Mass_Label = Label(S_5_frame, text="Molar Mass Qty", width=12)
# lbl_eci_5_Molar_Mass_Label.grid(row=1, column=4, sticky="w") #, sticky=W)
# lbl_eci_5_Molar_Mass_Label.config(font=labelfont)
# lbl_eci_5_Alpha_Label = Label(S_5_frame, text="Alpha", width=10)
# lbl_eci_5_Alpha_Label.grid(row=1, column=7, sticky="w") #, sticky=W)
# lbl_eci_5_Alpha_Label.config(font=labelfont)

# e_eci_2_qty = Entry(S_2_frame, text="", textvariable=eci_2_qty, width=8)
# e_eci_2_qty.grid(row=2, column=0, sticky="w")
# e_eci_2_qty.config(font=entryfont)
# e_eci_2_qty.bind('<Return>', eci_2_qty_adjusted)
# # #e_eci_1_qty.bind('<FocusOut>', lambda event: set_eci_db_eci_1_qty(e_eci_1_qty.get()))
# cb_eci_2_units: Combobox = Combobox(S_2_frame, values=unit_values, textvariable=eci_2_units, width=10)
# cb_eci_2_units.grid(row=2, column=1, sticky="w")
# cb_eci_2_units.config(font=entryfont)
# cb_eci_2_units.bind("<<ComboboxSelected>>", eci_2_units_selected)
# cb_eci_2: Combobox = Combobox(S_2_frame, textvariable=eci_2, width=12)
# cb_eci_2.grid(row=2, column=2, sticky="w")
# cb_eci_2.config(font=labelfont)
# cb_eci_2['values'] = element_symbol_string
# cb_eci_2.bind("<<ComboboxSelected>>", setEci_2) # setSelectedItemName
# lbl_blank = Label(inside_frame, text="")
# lbl_blank.grid(row=24, column=0)
# lbl_blank.config(font=labelfont)
# lbl_eci_3 = Label(S_3_frame, text="Select Element, Compound or Ion for ComboBox 3")
# lbl_eci_3.grid(row=0, column=0, columnspan=3, sticky="w") #, sticky=W)
# lbl_eci_3.config(font=labelfont)
# cb_Select_CB3: Combobox = Combobox(S_3_frame, values=eci_cb_values, width=10)
# cb_Select_CB3.grid(row=0, column=3, sticky="w") #, sticky=W)
# cb_Select_CB3.config(font=entryfont)
# cb_Select_CB3.bind("<<ComboboxSelected>>", select_eci_2_type)
# lbl_eci_3 = Label(inside_frame, text="   Select Element, Compound or Ion for ComboBox 3")
# lbl_eci_3.grid(row=26, column=0, columnspan=3) #, sticky=W)
# lbl_eci_3.config(font=labelfont)
# cb_Select_CB3: Combobox = Combobox(inside_frame, values=eci_cb_values, width=10)
# cb_Select_CB3.grid(row=26, column=3) #, sticky=W)
# cb_Select_CB3.config(font=entryfont)
# cb_Select_CB3.bind("<<ComboboxSelected>>", select_eci_3_type)
# lbl_eci_6 = Label(inside_frame, text="Select Element, Compound or Ion for ComboBox 6 ")
# lbl_eci_6.grid(row=26, column=4, columnspan=2) #, sticky=W)
# lbl_eci_6.config(font=labelfont)
# cb_Select_CB6: Combobox = Combobox(inside_frame, values=eci_cb_values, width=10)
# cb_Select_CB6.grid(row=26, column=6) #, sticky=W)
# cb_Select_CB6.config(font=entryfont)
# cb_Select_CB6.bind("<<ComboboxSelected>>", select_eci_6_type)

# lbl_eci_3_qty = Label(inside_frame, text="ECI Qty 3", width=8)
# lbl_eci_3_qty.grid(row=27, column=0)
# lbl_eci_3_qty.config(font=labelfont)
# lbl_eci_3_units = Label(inside_frame, text="Units 3", width=6)
# lbl_eci_3_units.grid(row=27, column=1) #, sticky=W)
# lbl_eci_3_units.config(font=labelfont)
# lbl_eci_3 = Label(inside_frame, text="ECI 3")
# lbl_eci_3.grid(row=27, column=2) #, sticky=W)
# lbl_eci_3.config(font=labelfont)
# lbl_eci_3_valence = Label(inside_frame, text="Valence 3", width=10)
# lbl_eci_3_valence.grid(row=27, column=3) #, sticky=W)
# lbl_eci_3_valence.config(font=labelfont)
# lbl_eci_6_qty = Label(inside_frame, text="ECI Qty 6", width=8)
# lbl_eci_6_qty.grid(row=27, column=4)
# lbl_eci_6_qty.config(font=labelfont)
# lbl_eci_6_units = Label(inside_frame, text="Units 6", width=8)
# lbl_eci_6_units.grid(row=27, column=5) #, sticky=W)
# lbl_eci_6_units.config(font=labelfont)
# lbl_eci_6 = Label(inside_frame, text="ECI 6", width=10)
# lbl_eci_6.grid(row=27, column=6) #, sticky=W)
# lbl_eci_6.config(font=labelfont)
# lbl_eci_6_valence = Label(inside_frame, text="Valence 6", width=10)
# lbl_eci_6_valence.grid(row=27, column=7) #, sticky=W)
# lbl_eci_6_valence.config(font=labelfont)

# e_eci_3_qty = Entry(inside_frame, text="", textvariable=eci_3_qty, width=8)
# e_eci_3_qty.grid(row=28, column=0)
# e_eci_3_qty.config(font=entryfont)
# e_eci_3_qty.bind('<Return>', eci_3_qty_adjusted)
# # cb_Elements1.bind("<<ComboboxSelected>>", callback_E1)
# cb_eci_3_units: Combobox = Combobox(inside_frame, values=unit_values, textvariable=eci_3_units, width=8)
# cb_eci_3_units.grid(row=28, column=1) #, sticky=W)
# cb_eci_3_units.config(font=entryfont)
# cb_eci_3_units.bind("<<ComboboxSelected>>", eci_units_selected)
# cb_eci_3: Combobox = Combobox(inside_frame, textvariable=eci_3, width=12)
# cb_eci_3.grid(row=28, column=2) #, sticky=W)
# cb_eci_3.config(font=entryfont)
# cb_eci_3['values'] = element_symbol_string
# cb_eci_3.bind("<<ComboboxSelected>>", setEci_3)
# cb_eci_3_valence: Combobox = Combobox(inside_frame, textvariable=eci_3_valence, width=8)
# cb_eci_3_valence.grid(row=28, column=3)
# cb_eci_3_valence.config(font=entryfont)
# cb_eci_3_valence['values'] = valences
# e_eci_6_qty = Entry(inside_frame, text="", textvariable=eci_6_qty, width=8)
# e_eci_6_qty.grid(row=28, column=4)
# e_eci_6_qty.config(font=entryfont)
# cb_eci_6_units: Combobox = Combobox(inside_frame, values=unit_values, textvariable=eci_6_units, width=8)
# cb_eci_6_units.grid(row=28, column=5)
# cb_eci_6_units.config(font=entryfont)
# cb_eci_6_units.bind("<<ComboboxSelected>>", eci_units_selected)
# cb_eci_6: Combobox = Combobox(inside_frame, values=compound_formula_string, textvariable=eci_6, width=12)
# cb_eci_6.grid(row=28, column=6)
# cb_eci_6.config(font=entryfont)
# cb_eci_6.bind("<<ComboboxSelected>>", setEci_6)
# cb_eci_6_valence: Combobox = Combobox(inside_frame, textvariable=eci_6_valence, width=5)
# cb_eci_6_valence.grid(row=28, column=7)
# cb_eci_6_valence.config(font=entryfont)
# cb_eci_6_valence['values'] = valences

# e_eci_3_M_qty = Entry(inside_frame, text=" ", width=8)
# e_eci_3_M_qty.grid(row=29, column=0)
# e_eci_3_M_qty.config(font=entryfont, textvariable=eci_3_M_qty)
# e_eci_3_M_qty.bind('<Return>', eci_3_M_qty_adjusted)
# lbl_eci_3_units_M = Label(inside_frame, text="Moles", width=8)
# lbl_eci_3_units_M.grid(row=29, column=1)
# lbl_eci_3_units_M.config(font=labelfont)
# cb_eci_3_N: Combobox = Combobox(inside_frame, values=elements_name_list, textvariable=eci_3_name, width=12)
# cb_eci_3_N.grid(row=29, column=2)
# cb_eci_3_N.config(font=entryfont)
# cb_eci_3_N.bind("<<ComboboxSelected>>", setSelectedItemFormula)
# e_eci_6_M_qty = Entry(inside_frame, text="CompoundQty 6", textvariable=eci_6_M_qty, width=8)
# e_eci_6_M_qty.grid(row=29, column=4)
# e_eci_6_M_qty.config(font=entryfont)
# lbl_eci_6_units_M = Label(inside_frame, text="Moles", width=8)
# lbl_eci_6_units_M.grid(row=29, column=5)
# lbl_eci_6_units_M.config(font=labelfont)
# cb_eci_6_N: Combobox = Combobox(inside_frame, values=compound_name_string, textvariable=eci_6_name, width=12)
# cb_eci_6_N.grid(row=29, column=6)
# cb_eci_6_N.config(font=entryfont)
# cb_eci_6_N.bind("<<ComboboxSelected>>", setSelectedItemFormula)

# lbl_Temp_Units_3 = Label(inside_frame, text="Temp Units", width=10)
# lbl_Temp_Units_3.grid(row=30, column=0)
# lbl_Temp_Units_3.config(font=labelfont)
# lbl_Temp_Qty_3 = Label(inside_frame, text="Temp Qty", width=10)
# lbl_Temp_Qty_3.grid(row=30, column=1)
# lbl_Temp_Qty_3.config(font=labelfont)
# lbl_Press_Units_3 = Label(inside_frame, text="Press Units", width=10)
# lbl_Press_Units_3.grid(row=30, column=2)
# lbl_Press_Units_3.config(font=labelfont)
# lbl_Press_Qty_3 = Label(inside_frame, text="Press Qty", width=10)
# lbl_Press_Qty_3.grid(row=30, column=3)
# lbl_Press_Qty_3.config(font=labelfont)
# lbl_Temp_Units_6 = Label(inside_frame, text="Temp Units", width=10)
# lbl_Temp_Units_6.grid(row=30, column=4)
# lbl_Temp_Units_6.config(font=labelfont)
# lbl_Temp_Qty_6 = Label(inside_frame, text="Temp Qty", width=10)
# lbl_Temp_Qty_6.grid(row=30, column=5)
# lbl_Temp_Qty_6.config(font=labelfont)
# lbl_Press_Units_6 = Label(inside_frame, text="Press Units", width=10)
# lbl_Press_Units_6.grid(row=30, column=6)
# lbl_Press_Units_6.config(font=labelfont)
# lbl_Press_Qty_6 = Label(inside_frame, text="Press Qty", width=10)
# lbl_Press_Qty_6.grid(row=30, column=7)
# lbl_Press_Qty_6.config(font=labelfont)

# cb_3_Temp_Units: Combobox = Combobox(inside_frame, values=temp_units, textvariable=eci_3_temp_units, width=10)
# cb_3_Temp_Units.grid(row=31, column=0)
# cb_3_Temp_Units.config(font=entryfont)
# cb_3_Temp_Units.bind("<<ComboboxSelected>>", eci_units_selected)
# e_Temp_Qty_3 = Entry(inside_frame, text="", textvariable=eci_temp_3_qty, width=8)
# e_Temp_Qty_3.grid(row=31, column=1)
# e_Temp_Qty_3.config(font=entryfont)
# cb_3_Press_Units: Combobox = Combobox(inside_frame, values=press_units, textvariable=eci_3_press_units, width=10)
# cb_3_Press_Units.grid(row=31, column=2)
# cb_3_Press_Units.config(font=entryfont)
# cb_3_Press_Units.bind("<<ComboboxSelected>>", eci_units_selected)
# e_Press_Qty_3 = Entry(inside_frame, text="", textvariable=eci_press_3_qty, width=8)
# e_Press_Qty_3.grid(row=31, column=3)
# e_Press_Qty_3.config(font=entryfont)
# cb_6_Temp_Units: Combobox = Combobox(inside_frame, values=temp_units, textvariable=eci_6_temp_units, width=10)
# cb_6_Temp_Units.grid(row=31, column=4)
# cb_6_Temp_Units.config(font=entryfont)
# cb_6_Temp_Units.bind("<<ComboboxSelected>>", eci_units_selected)
# e_Temp_Qty_6 = Entry(inside_frame, text="", textvariable=eci_temp_6_qty, width=8)
# e_Temp_Qty_6.grid(row=31, column=5)
# e_Temp_Qty_6.config(font=entryfont)
# cb_6_Press_Units: Combobox = Combobox(inside_frame, values=press_units, textvariable=eci_6_press_units, width=10)
# cb_6_Press_Units.grid(row=31, column=6)
# cb_6_Press_Units.config(font=entryfont)
# cb_6_Press_Units.bind("<<ComboboxSelected>>", eci_units_selected)
# e_Press_Qty_6 = Entry(inside_frame, text="", textvariable=eci_press_6_qty, width=8)
# e_Press_Qty_6.grid(row=31, column=7)
# e_Press_Qty_6.config(font=entryfont)
    # current_dict = eci_2
    # eci_2_d['type'] = cb_Select_CB2.get()
    # cb_2_type = eci_1_d['type']
    # print("727 cb_1_type = ", cb_2_type)
    # current_item_info['s_type'] = cb_2_type #     s_type, s_id, s_id_formula, substance
    # print("9727 eci_2_d['type'] = ", eci_2_d['type'])
    # if cb_2_type == 'elements':
    #     cb_eci_2['values'] = element_symbol_string
    #     cb_eci_2_N['values'] = element_name_string
    # elif cb_2_type == 'compounds':
    #     cb_eci_2['values'] = compound_formula_string
    #     cb_eci_2_N['values'] = compound_name_string
    # elif cb_2_type == 'ions':
    #     cb_eci_2['values'] = ion_symbols_list
    #     cb_eci_2_N['values'] = ion_names_list
    # else:
        # print("Error is select_eci_2_type")
            # current_dict = eci_3
    # eci_3_d['type'] = cb_Select_CB3.get()
    # cb_3_type = eci_3_d['type']
    # # dbr['R1']['eci_3_type'] = cb_Select_CB3.get()
    # print("dbr['R1']['eci_3_type'] = ", cb_Select_CB3.get())
    # print("cb_3_type is ", cb_3_type)
    # # eci_d['eci_3']['eci_type'] = cb_Select_CB3.get()
    # if cb_3_type == 'elements':
    #     cb_eci_3['values'] = element_symbol_string
    #     cb_eci_3_N['values'] = element_name_string
    # elif cb_3_type == 'compounds':
    #     cb_eci_3['values'] = compound_formula_string
    #     cb_eci_3_N['values'] = compound_name_string
    # elif cb_3_type == 'ions':
    #     cb_eci_3['values'] = ion_symbols_list
    #     cb_eci_3_N['values'] = ion_names_list
    # else:
    #     print("Error is select_eci_3_type")

    '''
    When an entry is made, check the value and assign it to an r dictionary field.
    '''
    '''eci_1_d = dict(eci = 'eci_1', eci_type = "", name ="", column = "", electronegativity = "", _group = "",
                 display_qty = "", qty = "", M_qty = "" , mass = "", Oxidation_State ="", display_units = "", units = "", valence = "",
                 display_temp_units= "", display_temp_qty="", display_press_units= "", display_press_qty= "",
                 temp_units= "", temp_qty="", press_units= "", press_qty= "")
    '''
    #print("In check_entry_changes")
    ''' The following don't seem necessary. '''
    #eci_1_type = cb_Select_CB1.get()
    #eci_1 = cb_eci_1.get()
    #eci_1_qty = e_eci_1_qty.get()
    #eci_1_units = cb_eci_1_units.get()
    #dbr['R1']['eci_1_formula'] = cb_eci_1.get()
    #r1['eci_1_formula']['eci'] = eci_1
    #r1['eci_1']['eci'] = eci_1
    #r1['eci_1_type']['type'] = eci_1_type
    #if eci_1_units == "":
    #   cb_eci_1_units.set('grams')
    #    r1['eci_1']['display_units'] = cb_eci_1_units.get()
    #    r1['eci_1']['display_temp_units'] = cb_1_Temp_Units.get()
    #    r1['eci_1']['display_temp_qty'] = e_Temp_Qty_1.get()
    #    r1['eci_1']['display_press_units'] = cb_1_Press_Units.get()
    #    r1['eci_1']['display_press_qty'] = e_Press_Qty_1.get()
    #if eci_1_type == 'elements':
    #    eci_1_mass = getdouble(db[eci_1]['mass'])   # Get element mass from the dictionary of element dictionaries
    #    r1['eci_1']['mass'] = getdouble(db[eci_1]['mass'])   #set the eci_frame mass field to the element mass
    #    ''' Need to move the following to a separate function because qty may be input or calculated
    #        or qualify it as an imput or a calculated value. Won't it normally be a calculated value? '''
    #    r1['eci_1']['display_qty'] = e_eci_1_qty.get()

    #    #eci_1_M_qty = getdouble(db[eci_1]['mass'])  # don't use float due to precision errors
    #    eci_1_M_qty = getdouble(e_eci_1_M_qty.get())
    #    m_mass = eci_1_M_qty * getdouble(db[eci_1]['mass'])
    #    e_eci_1_qty.insert(0, m_mass)   #eci_1_mass)
    #    print("m_mass is ", m_mass)
    #    print("m_mass is ",  getdouble(eci_1_M_qty) * getdouble(db[eci_1]['mass'])) #getdouble(e_eci_1_M_qty.get()) eci_1_M_qty


    #elif eci_1_type == 'compounds':
    #    pass
    #    ''' Compounds and ions don't currently have a mass property '''
    #    #eci_1_mass = getdouble(c_db[eci_1]['mass'])
    #    #e_eci_1_qty.insert(0, eci_1_mass)
    #elif eci_1_type == 'ions':
    #    pass
    #    ''' Compounds and ions don't currently have a mass property '''
        #eci_1_mass = getdouble(i_db[eci_1]['mass'])
        #e_eci_1_qty.insert(0, eci_1_mass)

    #print("e_eci_1_qty.get() is ", e_eci_1_qty.get())
    #print("eci_db['eci_1']['qty'] is ", eci_d['eci_1']['qty'])
    #print("e_eci_1_M_qty.get() is ", e_eci_1_M_qty.get())
    #print("eci_1_qty is ", e_eci_1_qty.get())  # eci_1_qty is  PY_VAR54
    #print("eci_db['eci_1']['qty'] is ", eci_1_qty)


    #The following works.
    '''
    total_mass = getdouble(e_eci_1_qty.get()) * eci_1_mass  # float(db[eci_1]['mass'])
    print("total_mass is ", total_mass)
    eci_d['eci_1']['qty'] = total_mass
    print("eci_db['eci_1']['qty'] ", eci_d['eci_1']['qty'])
    r1 = dict(name= 'Record 1', id= 1, compound= 'None', process= 'None', major_process= 'None', minor_process= 'None', environment= 'None',
          equipment = "", energy_type = "", energy_amount = "", catalyst = "", side_effects = "", by_products = "",
          variables = "", variable_values = "", explanation = "",
          eci_1_type = "", eci_1_formula= "", eci_1_name = "", eci_1_units = "", eci_1_qty = "", eci_1_M_qty = "", eci_1_valence = "",
          eci_1_temp_display_units = "", eci_1_temp_calc_units = "", eci_1_temp_display_qty = "", eci_1_temp_calc_qty = "",
          eci_1_press_display_units = "", eci_1_press_calc_units = "", eci_1_press_display_qty = "", eci_1_press_calc_qty = "",
          eci_2_type = "", eci_3_type = "", eci_4_type = "", eci_5_type = "", eci_6_type = "")
'''
    #e_Explanation.insert(tk.END, "setClassItem process entered\n")
def setClassItem(eventObject): # This function appears to be redundant.
    print("1334 In setClassItem function")

    ''' If eci_1 or eci_2 are elements, set their quantity and name variables. '''
    # print("setClassItem process entered")
    '''eci_1 = cb_eci_1.get()
    # print('eci_1 is', eci_1)
    # *** The following works!
    if cb_1_type == 'elements':
        eci_temp_1_qty = db[eci_1]['mass']
        eci_1_name = db[eci_1]['name']
        e_Explanation.insert(END, "db[eci_1]['mass'] is ", eci_temp_1_qty, '\n')
        print("db[eci_1]['mass'] is ", eci_temp_1_qty)
        print("db[eci_1]['name'] is ", eci_1_name)
    elif cb_1_type == 'compounds':
        eci_1 = cb_eci_1.get()
        eci_1_name = c_db[eci_1]['name']
        print('eci_1 = ', eci_1)
        print("In setClassItem at elif compounds")
        '''
'''
    ''' If gas units are selected, the user needs to fill in temperature and pressure
    units and amounts. This procedure sets default values.
    The user can reset the displayed units and quantities, but they will be converted into
    the units and quantities actually used to calculate quantities used by the program.  '''
    #### print("1764 In process eci_units_selected")
    #print("cb_eci_1_units.get() is ", cb_eci_1_units.get())
    # eci_1 = cb_eci_1.get()
    # dbr['R1']['eci_1_formula'] = eci_1
    # print("1812 dbr['R1']['eci_1_formula'] is ", dbr['R1']['eci_1_formula'])
    # eci_1_units = cb_eci_1_units.get()
    # eci_2_units = cb_eci_2_units.get()
    # eci_3_units = cb_eci_3_units.get()
    # eci_4_units = cb_eci_4_units.get()
    # eci_5_units = cb_eci_5_units.get()
    # dbr['R1']['eci_1_display_units'] = cb_eci_1_units.get()
    # dbr['R1']['eci_1_calc_units'] = cb_eci_1_units.get()
    # print("1820 dbr['R1']['eci_1_display_units'] ", dbr['R1']['eci_1_display_units']) #dbr['R1']['eci_1_display_units'])
    # print("1821 dbr['R1']['eci_1_calc_units'] ", dbr['R1']['eci_1_calc_units'])
    #r1['eci_2']['display_units'] = cb_eci_2_units.get()
    #r1['eci_3']['display_units'] = cb_eci_3_units.get()
    #r1['eci_4']['display_units'] = cb_eci_4_units.get()
    #r1['eci_5']['display_units'] = cb_eci_5_units.get()
    #r1['eci_6']['display_units'] = cb_eci_6_units.get()
    #eci_d['eci_1']['display_units'] = cb_eci_1_units.get()
    #ci_d['eci_2']['display_units'] = cb_eci_2_units.get()
    #eci_d['eci_3']['display_units'] = cb_eci_3_units.get()
    #eci_d['eci_4']['display_units'] = cb_eci_4_units.get()
    #eci_d['eci_5']['display_units'] = cb_eci_5_units.get()
    #eci_d['eci_6']['display_units'] = cb_eci_6_units.get()
    # if eci_1_units == 'liters(l)' or eci_1_units == 'ml(l)' or eci_1_units == 'liters(g)' or eci_1_units == 'ml(g)':    #liters(l) liters(g) ml(l) ml(g
    #     # dbr['R1']['eci_1_display_units'] = eci_1_units
    #     # dbr['R1']['eci_1_calc_units'] = eci_1_units
    #     print("1833 eci_1_units are ", eci_1_units) # == 'liters(g)')
    #     print("1834 dbr['R1']['eci_1_display_units'] ", dbr['R1']['eci_1_display_units'])
    #     if cb_1_Temp_Units.get() == "":
    #         eci_1_temp_units = cb_1_Temp_Units.set('C')
    #         e_Temp_Qty_1.delete(0, tk.END)
    #         e_Temp_Qty_1.insert(0, 0)
    #     elif cb_1_Temp_Units.get() == 'C':
    #         e_Temp_Qty_1.delete(0, tk.END)
    #         e_Temp_Qty_1.insert(0, 0)
    #     elif cb_1_Temp_Units.get() == 'K':
    #         e_Temp_Qty_1.delete(0, tk.END)
    #         e_Temp_Qty_1.insert(0, 273.15)
    #     elif cb_1_Temp_Units.get() == 'F':
    #         e_Temp_Qty_1.delete(0, tk.END)
    #         e_Temp_Qty_1.insert(0, -32)

        # initialize at 0 degrees C -- stp
        #print('1797 e_Press_Qty_1.get() is ', e_Press_Qty_1.get())
        # if cb_1_Press_Units.get() == "":
        #     eci_1_press_units = cb_1_Press_Units.set('atm')
        #     e_Press_Qty_1.delete(0, tk.END)
        #     e_Press_Qty_1.insert(0, 1.0) # initialize at 1 atm -- stp
        #     e_eci_1_qty.delete(0, tk.END)
        #     e_eci_1_qty.insert(0, 22.4)   #eci_1_mass)
        #     e_eci_1_M_qty.delete(0, tk.END)
        #     e_eci_1_M_qty.insert(0, 1.0)
        # elif cb_1_Press_Units.get() == "atm":
        #     #eci_1_press_units = cb_1_Press_Units.set('atm')
        #     e_Press_Qty_1.delete(0, tk.END)
        #     e_Press_Qty_1.insert(0, 1.0) # initialize at 1 atm -- stp
        #     e_eci_1_qty.delete(0, tk.END)
        #     e_eci_1_qty.insert(0, 22.4)   #eci_1_mass)
        #     e_eci_1_M_qty.delete(0, tk.END)
        #     e_eci_1_M_qty.insert(0, 1.0)

'''
    # elif not eci_1_units == 'liters(g)' and not eci_1_units == 'ml(g)':
    #     print('cb_eci_1_units are ', eci_1_units)
    if eci_2_units == 'liters(l)' or eci_2_units == 'ml(l)' or eci_2_units == 'liters(g)' or eci_2_units == 'ml(g)':
        if cb_2_Temp_Units.get() == "":
            eci_2_temp_units = cb_2_Temp_Units.set('C')
        if cb_2_Press_Units.get() == "":
            eci_2_press_units = cb_2_Press_Units.set('ATM')
    if eci_3_units == 'liters(l)' or eci_3_units == 'ml(l)' or eci_3_units == 'liters(g)' or eci_3_units == 'ml(g)':
        if cb_3_Temp_Units.get() == "":
            eci_3_temp_units = cb_3_Temp_Units.set('C')
        if cb_3_Press_Units.get() == "":
            eci_3_press_units = cb_3_Press_Units.set('ATM')
    if eci_4_units == 'liters(l)' or eci_4_units == 'ml(l)' or eci_4_units == 'liters(g)' or eci_4_units == 'ml(g)':
        if cb_4_Temp_Units.get() == "":
            eci_4_temp_units = cb_4_Temp_Units.set('C')
        if cb_4_Press_Units.get() == "":
            eci_4_press_units = cb_4_Press_Units.set('ATM')
    if eci_5_units == 'liters(l)' or eci_5_units == 'ml(l)' or eci_5_units == 'liters(g)' or eci_5_units == 'ml(g)':
        if cb_5_Temp_Units.get() == "":
            eci_5_temp_units = cb_5_Temp_Units.set('C')
        if cb_4_Press_Units.get() == "":
            eci_5_press_units = cb_5_Press_Units.set('ATM')
    if eci_6_units == 'liters(l)' or eci_6_units == 'ml(l)' or eci_6_units == 'liters(g)' or eci_6_units == 'ml(g)':
        if cb_6_Temp_Units.get() == "":
            eci_6_temp_units = cb_6_Temp_Units.set('C')
        if cb_6_Press_Units.get() == "":
            eci_6_press_units = cb_6_Press_Units.set('ATM')
    eci_d['eci_1']['display_temp_units'] = cb_1_Temp_Units.get()
    eci_d['eci_2']['display_temp_units'] = cb_2_Temp_Units.get()
    eci_d['eci_3']['display_temp_units'] = cb_3_Temp_Units.get()
    eci_d['eci_4']['display_temp_units'] = cb_4_Temp_Units.get()
    eci_d['eci_5']['display_temp_units'] = cb_5_Temp_Units.get()
    eci_d['eci_6']['display_temp_units'] = cb_6_Temp_Units.get()
    eci_d['eci_1']['display_press_units'] = cb_1_Press_Units.get()
    eci_d['eci_2']['display_press_units'] = cb_2_Press_Units.get()
    eci_d['eci_3']['display_press_units'] = cb_3_Press_Units.get()
    eci_d['eci_4']['display_press_units'] = cb_4_Press_Units.get()
    eci_d['eci_5']['display_press_units'] = cb_5_Press_Units.get()
    eci_d['eci_6']['display_press_units'] = cb_6_Press_Units.get()
    #print("eci_db['eci_1']['display_temp_units'] are ", eci_db['eci_1']['display_temp_units'])
    #print("eci_db['eci_1']['display_press_units'] are ", eci_db['eci_1']['display_press_units'])
'''

# def calc_temp(eci):
#     """ Use eci to get temp qty and units, convert to degrees K and return"""
#     temp_qty = float(eci_d[eci]['temp_display_qty'])
#     temp_units = eci_d[eci]['temp_display_units']
#     T = calc_temp(eci) # temp_qty, temp_units
#     return T
        # refresh_s_1_display()
        # e_eci_1_M_qty.delete(0, tk.END)
                # substance = eci_d[eci]['formula']
        # eci_d[eci]['mass'] = db[eci_1.get()]['mass']
        # print("2133 eci_d[eci]['qty'] = ", eci_d[eci]['qty'])

            print("2036 eci_1_qty is ", eci_1_qty)
                # value is <KeyPress event send_event=True state=Mod1 keysym=Return keycode=13 char='\r' x=48 y=28>

                
def eci_3_qty_adjusted(value):
    print('eci_3_qty_adjusted event procedure called.', value)
    print('e_eci_3_qty is ', e_eci_3_qty.get())
    current_eci_3_units = dbr['R1']['eci_3_units']
    print('current_eci_3_units is ', current_eci_3_units)
    if dbr['R1']['eci_3_units'] == 'grams':
        ''' I can't just adjust the eci_1_qty, I need to determine what it should be based on units.
        Since units are in grams, I need to retrieve the element atomic mass and use it for calculations.'''
        print("dbr['R1']['eci_3_units'] == ", dbr['R1']['eci_3_units'])
        dbr['R1']['eci_3_qty'] = db[eci_3.get()]['mass']
        new_mole_qty = eci_3_qty.get()/dbr['R1']['eci_3_qty']
        e_eci_3_M_qty.delete(0, tk.END)
        e_eci_3_M_qty.insert(0, new_mole_qty)

def eci_3_M_qty_adjusted(value):
    current_eci_3_units = dbr['R1']['eci_3_units']
    print('current_eci_3_units is ', current_eci_3_units)
    if dbr['R1']['eci_3_units'] == 'grams':
        print("dbr['R1']['eci_3_units'] == ", dbr['R1']['eci_3_units'])
        ''' Reset the record quantity to the element atomic mass before doing calculations. '''
        dbr['R1']['eci_3_qty'] = db[eci_3.get()]['mass']
        ''' current_eci_3_qty may be mass in grams or some other quantity of the current units.'''
        current_eci_3_qty = dbr['R1']['eci_3_qty']
        print('current_eci_3_qty is ', current_eci_3_qty)
        new_eci_3_qty = eci_3_M_qty.get() * current_eci_3_qty
        e_eci_3_qty.delete(0, tk.END)
        e_eci_3_qty.insert(0, new_eci_3_qty)

def Fill_Product_Comboboxes():