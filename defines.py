# unidirectional
CLB_PIP_A = [
    (19,-7,"X","x_top"),
    (19,-12,"LONG","long_row"),
    (19,-20,"ROW0","gen_row_right[0]"),
    (19,-25,"ROW1","gen_row_right[1]"),
    (19,-30,"ROW2","gen_row_right[2]"),
    (19,-36,"ROW3","gen_row_right[3]")
]
# unidirectional
CLB_PIP_B = [
    (-7,14,"X","x_top"),
    (-12,14,"GLOBAL","global_"),
    (-17,14,"LONG1","long_col[1]"),
    (-22,14,"LONG0","long_col[0]"),
    (-27,14,"Y","y_left"),
    (-32,14,"COL4","gen_col_bot[4]"),
    (-40,14,"COL3","gen_col_bot[3]"),
    (-45,14,"COL2","gen_col_bot[2]"),
    (-50,14,"COL1","gen_col_bot[1]"),
    (-55,14,"COL0","gen_col_bot[0]")
]
# unidirectional
CLB_PIP_C = [
    (-7,22,"X","x_bot"),
    (-17,22,"LONG1","long_col[1]"),
    (-22,22,"LONG0","long_col[0]"),
    (-32,22,"COL4","gen_col_bot[4]"),
    (-40,22,"COL3","gen_col_bot[3]"),
    (-45,22,"COL2","gen_col_bot[2]"),
    (-50,22,"COL1","gen_col_bot[1]"),
    (-55,22,"COL0","gen_col_bot[0]")
]
# unidirectional
CLB_PIP_D = [
    (11,51,"X","clb_x"),
    (11,58,"ROW3","gen_row_right[3]"),
    (11,64,"ROW2","gen_row_right[2]"),
    (11,69,"ROW1","gen_row_right[1]"),
    (11,74,"ROW0","gen_row_right[0]"),
    (11,82,"LONG","long_row")
]
# unidirectional
CLB_PIP_K = [
    (-12,30,"GLOBAL","global_"),
    (-17,30,"LONG1","long_col[1]")
]
# unidirectional
CLB_PIP_X = [
    (43,3,"COL1","gen_col_bot[1]"),
    (53,3,"COL3","gen_col_bot[3]"),
    (71,3,"LONG0","long_col[0]")
]
# unidirectional
CLB_PIP_Y = [
    (37,35,"COL0","gen_col_bot[0]"),
    (48,35,"COL2","gen_col_bot[2]"),
    (61,35,"COL4","gen_col_bot[4]"),
    (76,35,"LONG1","long_col[1]")
]
# bidirectional
SWITCH_PIP = [
    (1,25,"COL0_LONG","long_row","gen_col_bot[0]"),
    (17,25,"COL3_LONG","long_row","gen_col_bot[3]"),
    (25,-1,"COL4HI_COL4LO","gen_col_bot[4]","gen_col_top[4]"),
    (25,7,"COL4HI_ROW2","gen_row_right[2]","gen_col_top[4]"),
    (25,12,"COL4HI_ROW1","gen_row_right[1]","gen_col_top[4]"),
    (30,7,"COL4LO_ROW2","gen_row_right[2]","gen_col_bot[4]"),
    (30,12,"COL4LO_ROW1","gen_row_right[1]","gen_col_bot[4]"),
    (35,7,"ROW2_LONG0","gen_row_right[2]","long_col[0]"),
    (35,17,"ROW0_LONG0","gen_row_right[0]","long_col[0]"),
    (40,1,"ROW3_LONG1","gen_row_right[3]","long_col[1]"),
    (40,12,"ROW1_LONG1","gen_row_right[1]","long_col[1]")
]
LEFT_IOB = [
    (13,123,"P11"),
    (13,170,"P12"),
    (13,217,"P13"),
    (13,264,"P14"),
    (13,311,"P15"),
    (13,358,"P16"),
    (13,405,"P17"),
    (13,499,"P19"),
    (13,546,"P20"),
    (13,593,"P21"),
    (13,640,"P22"),
    (13,687,"P23"),
    (13,734,"P24")
]
TOP_IOB = [
    (86,16,"P9"),
    (123,16,"P8"),
    (185,16,"P7"),
    (216,16,"P6"),
    (279,16,"P5"),
    (310,16,"P4"),
    (372,16,"P3"),
    (404,16,"P2"),
    (466,16,"P68"),
    (497,16,"P67"),
    (560,16,"P66"),
    (591,16,"P65"),
    (653,16,"P64"),
    (684,16,"P63"),
    (747,16,"P62"),
    (778,16,"P61")
]
RIGHT_IOB = [
    (859,123,"P59"),
    (859,170,"P58"),
    (859,217,"P57"),
    (859,264,"P56"),
    (859,311,"P55"),
    (859,358,"P54"),
    (859,405,"P53"),
    (859,499,"P51"),
    (859,546,"P50"),
    (859,593,"P49"),
    (859,640,"P48"),
    (859,687,"P47"),
    (859,734,"P46")
]
BOT_IOB = [
    (86,864,"P27"),
    (122,864,"P28"),
    (185,864,"P29"),
    (216,864,"P30"),
    (279,864,"P31"),
    (310,864,"P32"),
    (372,864,"P33"),
    (403,864,"P34"),
    (466,864,"P36"),
    (497,864,"P37"),
    (559,864,"P38"),
    (591,864,"P39"),
    (653,864,"P40"),
    (684,864,"P41"),
    (747,864,"P42"),
    (778,864,"P43")
]
# unidirectional
IOB_LEFT_TOP_PIP = [
    (20,14,"TS_LONG2","long_col[2]","iob_ts_top"),
    (25,14,"TS_COL0","gen_col_top[0]","iob_ts_top"),
    (35,14,"TS_COL2","gen_col_top[2]","iob_ts_top"),
    (48,14,"TS_LONG0","long_col[0]","iob_ts_top"),
    (30,19,"IN_COL1","iob_in_top","gen_col_top[1]"),
    (41,19,"IN_COL3","iob_in_top","gen_col_top[3]"),
    (54,19,"IN_LONG1","iob_in_top","long_col[1]"),
    (82,43,"IN_ROW1","iob_in_top","gen_row_right[1]"),
    (82,56,"IN_LONG","iob_in_top","long_row"),
    (20,24,"OUT_LONG2","long_col[2]","iob_out_top"),
    (25,24,"OUT_COL0","gen_col_top[0]","iob_out_top"),
    (35,24,"OUT_COL2","gen_col_top[2]","iob_out_top"),
    (48,24,"OUT_LONG0","long_col[0]","iob_out_top"),
    (77,37,"OUT_ROW2","gen_row_right[2]","iob_out_top"),
    (77,48,"OUT_ROW0","gen_row_right[0]","iob_out_top")
]
# unidirectional
IOB_LEFT_BOT_PIP = [
    (20,14,"TS_LONG2","long_col[2]","iob_ts_mid"),
    (25,14,"TS_COL0","gen_col_bot[0]","iob_ts_mid"),
    (35,14,"TS_COL2","gen_col_bot[2]","iob_ts_mid"),
    (48,14,"TS_LONG0","long_col[0]","iob_ts_mid"),
    (20,19,"IN_LONG2","iob_in_mid","long_col[2]"),
    (25,19,"IN_COL0","iob_in_mid","gen_col_bot[0]"),
    (35,19,"IN_COL2","iob_in_mid","gen_col_bot[2]"),
    (48,19,"IN_LONG0","iob_in_mid","long_col[0]"),
    (64,1,"IN_ROW0","iob_in_mid","gen_row_right[0]"),
    (30,25,"OUT_COL1","gen_col_bot[1]","iob_out_mid"),
    (41,25,"OUT_COL3","gen_col_bot[3]","iob_out_mid"),
    (54,25,"OUT_LONG1","long_col[1]","iob_out_mid"),
    (72,9,"OUT_LONG","long_row","iob_out_mid"),
    (72,-4,"OUT_ROW1","gen_row_right[1]","iob_out_mid"),
    (72,-15,"OUT_ROW3","gen_row_right[3]","iob_out_mid")
]
# unidirectional
CLB_LEFT_PIP_B = [
    (-7,14,"X","x_top"),
    (-12,14,"IOB","iob_in_bot"),
    (-35,14,"GLOBAL","global_"),
    (-40,14,"LONG1","long_col[1]"),
    (-46,14,"LONG0","long_col[0]"),
    (-53,14,"COL3","gen_col_bot[3]"),
    (-59,14,"COL2","gen_col_bot[2]"),
    (-64,14,"COL1","gen_col_bot[1]"),
    (-69,14,"COL0","gen_col_bot[0]"),
    (-74,14,"LONG2","long_col[2]")
]
# unidirectional
CLB_LEFT_PIP_C = [
    (-7,22,"X","x_bot"),
    (-40,22,"LONG1","long_col[1]"),
    (-46,22,"LONG0","long_col[0]"),
    (-53,22,"COL3","gen_col_bot[3]"),
    (-59,22,"COL2","gen_col_bot[2]"),
    (-64,22,"COL1","gen_col_bot[1]"),
    (-69,22,"COL0","gen_col_bot[0]"),
    (-74,22,"LONG2","long_col[2]")
]
# unidirectional
CLB_LEFT_PIP_K = [
    (-35,30,"GLOBAL","global_"),
    (-40,30,"LONG1","long_col[1]")
]
# bidirectional
SWITCH_LEFT_PIP = [
    (-4,25,"LONG2_LONG","long_row","long_col[2]"),
    (1,25,"COL0_LONG","long_row","gen_col_bot[0]"),
    (17,25,"COL3_LONG","long_row","gen_col_bot[3]"),
    (24,25,"LONG0_LONG","long_row","long_col[0]"),
    (30,25,"LONG1_LONG","long_row","long_col[1]"),
    (24,1,"LONG0_ROW3","gen_row_right[3]","long_col[0]"),
    (30,7,"LONG1_ROW2","gen_row_right[2]","long_col[1]")
]
# unidirectional
IOB_TOP_LEFT_PIP = [
    (19,24,"TS_LONG2","long_row[1]","iob_ts_mid"),
    (19,30,"TS_ROW3","gen_row_right[3]","iob_ts_mid"),
    (19,40,"TS_ROW1","gen_row_right[1]","iob_ts_mid"),
    (19,53,"TS_LONG","long_row[0]","iob_ts_mid"),
    (14,30,"IN_ROW3","iob_in_mid","gen_row_right[3]"),
    (14,40,"IN_ROW1","iob_in_mid","gen_row_right[1]"),
    (14,53,"IN_LONG","iob_in_mid","long_row[0]"),
    (-1,74,"IN_LONG1","iob_in_mid","long_col[1]"),
    (-17,74,"IN_COL4","iob_in_mid","gen_col_bot[4]"),
    (-25,74,"IN_COL3","iob_in_mid","gen_col_bot[3]"),
    (-35,74,"IN_COL1","iob_in_mid","gen_col_bot[1]"),
    (9,24,"OUT_LONG2","long_row[1]","iob_out_mid"),
    (9,35,"OUT_ROW2","gen_row_right[2]","iob_out_mid"),
    (9,45,"OUT_ROW0","gen_row_right[0]","iob_out_mid"),
    (-7,69,"OUT_LONG0","long_col[0]","iob_out_mid"),
    (-30,69,"OUT_COL2","gen_col_bot[2]","iob_out_mid"),
    (-41,69,"OUT_COL0","gen_col_bot[0]","iob_out_mid")
]
# unidirectional
IOB_TOP_RIGHT_PIP = [
    (14,24,"TS_LONG2","long_row[1]","iob_ts_right"),
    (14,30,"TS_ROW3","gen_row_right[3]","iob_ts_right"),
    (14,40,"TS_ROW1","gen_row_right[1]","iob_ts_right"),
    (14,53,"TS_LONG","long_row[0]","iob_ts_right"),
    (9,24,"IN_LONG2","iob_in_right","long_row[1]"),
    (9,35,"IN_ROW2","iob_in_right","gen_row_right[2]"),
    (9,45,"IN_ROW0","iob_in_right","gen_row_right[0]"),
    (22,58,"IN_COL0","iob_in_left","gen_col_bot[0]"),
    (33,58,"IN_COL2","iob_in_left","gen_col_bot[2]"),
    (56,58,"IN_LONG0","iob_in_left","long_col[0]"),
    (4,30,"OUT_ROW3","gen_row_right[3]","iob_out_right"),
    (4,40,"OUT_ROW1","gen_row_right[1]","iob_out_right"),
    (4,53,"OUT_LONG","long_row[0]","iob_out_right"),
    (14,64,"OUT_X","clb_x","iob_out_right"),
    (27,64,"OUT_COL1","gen_col_bot[1]","iob_out_left"),
    (38,64,"OUT_COL3","gen_col_bot[3]","iob_out_left"),
    (46,64,"OUT_COL4","gen_col_bot[4]","iob_out_left"),
    (61,64,"OUT_LONG1","long_col[1]","iob_out_left")
]
# unidirectional
CLB_TOP_PIP_A = [
    (12,-17,"IOB","iob_in_mid"),
    (12,-28,"LONG","long_row[0]"),
    (12,-36,"ROW0","gen_row_right[0]"),
    (12,-41,"ROW1","gen_row_right[1]"),
    (12,-46,"ROW2","gen_row_right[2]"),
    (12,-51,"ROW3","gen_row_right[3]"),
    (12,-57,"LONG2","long_row[1]")
]
# bidirectional
SWITCH_TOP_PIP = [
    (1,24,"COL0_LONG","long_row[0]","gen_col_bot[0]"),
    (16,24,"COL3_LONG","long_row[0]","gen_col_bot[3]"),
    (24,6,"ROW2_COL4","gen_row_right[2]","gen_col_bot[4]"),
    (24,11,"ROW1_COL4","gen_row_right[1]","gen_col_bot[4]"),
    (34,24,"LONG0_LONG","long_row[0]","long_col[0]"),
    (34,16,"LONG0_ROW0","gen_row_right[0]","long_col[0]"),
    (34,6,"LONG0_ROW2","gen_row_right[2]","long_col[0]"),
    (34,-5,"LONG0_LONG2","long_row[1]","long_col[0]"),
    (40,24,"LONG1_LONG","long_row[0]","long_col[1]"),
    (40,11,"LONG1_ROW1","gen_row_right[1]","long_col[1]"),
    (40,1,"LONG1_ROW3","gen_row_right[3]","long_col[1]")
]
# unidirectional
IOB_RIGHT_TOP_PIP = [
    (-7,14,"TS_LONG2","long_col[2]","iob_ts_top"),
    (-12,14,"TS_COL3","gen_col_top[3]","iob_ts_top"),
    (-22,14,"TS_COL1","gen_col_top[1]","iob_ts_top"),
    (-35,14,"TS_LONG1","long_col[1]","iob_ts_top"),
    (-7,19,"IN_LONG2","iob_in_top","long_col[2]"),
    (-17,19,"IN_COL2","iob_in_top","gen_col_top[2]"),
    (-28,19,"IN_COL0","iob_in_top","gen_col_top[0]"),
    (-41,19,"IN_LONG0","iob_in_top","long_col[0]"),
    (-62,38,"IN_ROW2","iob_in_top","gen_row_left[2]"),
    (-62,48,"IN_ROW0","iob_in_top","gen_row_left[0]"),
    (-12,25,"OUT_COL3","gen_col_top[3]","iob_out_top"),
    (-22,25,"OUT_COL1","gen_col_top[1]","iob_out_top"),
    (-35,25,"OUT_LONG1","long_col[1]","iob_out_top"),
    (-56,32,"OUT_ROW3","gen_row_left[3]","iob_out_top"),
    (-56,43,"OUT_ROW1","gen_row_left[1]","iob_out_top"),
    (-56,56,"OUT_LONG","long_row","iob_out_top")
]
# unidirectional
IOB_RIGHT_BOT_PIP = [
    (-7,14,"TS_LONG2","long_col[2]","iob_ts_mid"),
    (-12,14,"TS_COL3","gen_col_bot[3]","iob_ts_mid"),
    (-22,14,"TS_COL1","gen_col_bot[1]","iob_ts_mid"),
    (-35,14,"TS_LONG1","long_col[1]","iob_ts_mid"),
    (-12,19,"IN_COL3","iob_in_mid","gen_col_bot[3]"),
    (-22,19,"IN_COL1","iob_in_mid","gen_col_bot[1]"),
    (-35,19,"IN_LONG1","iob_in_mid","long_col[1]"),
    (-46,9,"IN_LONG","iob_in_mid","long_row"),
    (-46,-4,"IN_ROW1","iob_in_mid","gen_row_left[1]"),
    (-46,-15,"IN_ROW3","iob_in_mid","gen_row_left[3]"),
    (-7,25,"OUT_LONG2","long_col[2]","iob_out_mid"),
    (-17,25,"OUT_COL2","gen_col_bot[2]","iob_out_mid"),
    (-28,25,"OUT_COL0","gen_col_bot[0]","iob_out_mid"),
    (-41,25,"OUT_LONG0","long_col[0]","iob_out_mid"),
    (-51,1,"OUT_ROW0","gen_row_left[0]","iob_out_mid"),
    (-51,-9,"OUT_ROW2","gen_row_left[2]","iob_out_mid")
]
# unidirectional
CLB_RIGHT_PIP_X = [
    (40,14,"OUTLO","iob_out_bot"),
    (45,14,"OUTHI","iob_out_mid"),
    (60,14,"LONG1","long_col[1]"),
    (73,14,"COL1","gen_col_bot[1]"),
    (84,14,"COL3","gen_col_bot[3]")
]
# unidirectional
CLB_RIGHT_PIP_Y = [
    (40,35,"OUTLO","iob_out_bot"),
    (45,35,"OUTHI","iob_out_mid"),
    (55,35,"LONG0","long_col[0]"),
    (68,35,"COL0","gen_col_bot[0]"),
    (79,35,"COL2","gen_col_bot[2]"),
    (89,35,"LONG2","long_col[2]")
]
# bidirectional
SWITCH_RIGHT_PIP = [
    (22,25,"LONG_LONG2","long_row","long_col[2]"),
    (17,25,"LONG_COL3","long_row","gen_col_bot[3]"),
    (1,25,"LONG_COL0","long_row","gen_col_bot[0]"),
    (-7,25,"LONG_LONG1","long_row","long_col[1]"),
    (-12,25,"LONG0_LONG","long_row","long_col[0]"),
    (-12,17,"LONG0_ROW0","gen_row_left[0]","long_col[0]"),
    (-12,7,"LONG0_ROW2","gen_row_left[2]","long_col[0]"),
    (-7,12,"LONG1_ROW1","gen_row_left[1]","long_col[1]"),
    (-7,1,"LONG1_ROW3","gen_row_left[3]","long_col[1]")
]
# unidirectional
IOB_BOT_LEFT_PIP = [
    (19,-14,"TS_LONG2","long_row[1]","iob_ts_mid"),
    (19,-19,"TS_ROW0","gen_row_right[0]","iob_ts_mid"),
    (19,-30,"TS_ROW2","gen_row_right[2]","iob_ts_mid"),
    (19,-43,"TS_LONG","long_row[0]","iob_ts_mid"),
    (14,-19,"IN_ROW0","iob_in_mid","gen_row_right[0]"),
    (14,-30,"IN_ROW2","iob_in_mid","gen_row_right[2]"),
    (14,-43,"IN_LONG","iob_in_mid","long_row[0]"),
    (-1,-64,"IN_LONG1","iob_in_mid","long_col[1]"),
    (-17,-64,"IN_COL4","iob_in_mid","gen_col_top[4]"),
    (-25,-64,"IN_COL3","iob_in_mid","gen_col_top[3]"),
    (-35,-64,"IN_COL1","iob_in_mid","gen_col_top[1]"),
    (9,-14,"OUT_LONG2","long_row[1]","iob_out_mid"),
    (9,-24,"OUT_ROW1","gen_row_right[1]","iob_out_mid"),
    (9,-35,"OUT_ROW3","gen_row_right[3]","iob_out_mid"),
    (-7,-58,"OUT_LONG0","long_col[0]","iob_out_mid"),
    (-30,-58,"OUT_COL2","gen_col_top[2]","iob_out_mid"),
    (-40,-58,"OUT_COL0","gen_col_top[0]","iob_out_mid")
]
# unidirectional
IOB_BOT_RIGHT_PIP = [
    (15,-14,"TS_LONG2","long_row[1]","iob_ts_right"),
    (15,-19,"TS_ROW0","gen_row_right[0]","iob_ts_right"),
    (15,-30,"TS_ROW2","gen_row_right[2]","iob_ts_right"),
    (15,-43,"TS_LONG","long_row[0]","iob_ts_right"),
    (9,-14,"IN_LONG2","iob_in_right","long_row[1]"),
    (9,-24,"IN_ROW1","iob_in_right","gen_row_right[1]"),
    (9,-35,"IN_ROW3","iob_in_right","gen_row_right[3]"),
    (22,-48,"IN_COL0","iob_in_left","gen_col_top[0]"),
    (33,-48,"IN_COL2","iob_in_left","gen_col_top[2]"),
    (56,-48,"IN_LONG0","iob_in_left","long_col[0]"),
    (4,-19,"OUT_ROW0","gen_row_right[0]","iob_out_right"),
    (4,-30,"OUT_ROW2","gen_row_right[2]","iob_out_right"),
    (4,-43,"OUT_LONG","long_row[0]","iob_out_right"),
    (15,-53,"OUT_X","x_top","iob_out_right"),
    (28,-53,"OUT_COL1","gen_col_top[1]","iob_out_left"),
    (38,-53,"OUT_COL3","gen_col_top[3]","iob_out_left"),
    (46,-53,"OUT_COL4","gen_col_top[4]","iob_out_left"),
    (62,-53,"OUT_LONG1","long_col[1]","iob_out_left")
]
# unidirectional
CLB_BOT_PIP_D = [
    (12,51,"IOB","iob_in_mid"),
    (12,66,"LONG","long_row[0]"),
    (12,74,"ROW3","gen_row_right[3]"),
    (12,79,"ROW2","gen_row_right[2]"),
    (12,84,"ROW1","gen_row_right[1]"),
    (12,90,"ROW0","gen_row_right[0]"),
    (12,95,"LONG2","long_row[1]")
]
# bidirectional
SWITCH_BOT_PIP = [
    (1,-7,"LONG_COL0","long_row[0]","gen_col_top[0]"),
    (16,-7,"LONG_COL3","long_row[0]","gen_col_top[3]"),
    (34,-7,"LONG0_LONG","long_row[0]","long_col[0]"),
    (34,1,"LONG0_ROW3","gen_row_right[3]","long_col[0]"),
    (34,12,"LONG0_ROW1","gen_row_right[1]","long_col[0]"),
    (34,22,"LONG0_LONG2","long_row[1]","long_col[0]"),
    (40,-7,"LONG1_LONG","long_row[0]","long_col[1]"),
    (40,6,"LONG1_ROW2","gen_row_right[2]","long_col[1]"),
    (40,17,"LONG1_ROW0","gen_row_right[0]","long_col[1]"),
    (40,30,"LONG1_ALT","alt","long_col[1]"),
    (24,6,"COL4_ROW2","gen_row_right[2]","gen_col_top[4]"),
    (24,12,"COL4_ROW1","gen_row_right[1]","gen_col_top[4]")
]
# unidirectional
IOB_P9_PIP = [
    (20,24,"TS_LONG2_ROW","long_row[1]","iob_ts_mid"),
    (20,30,"TS_ROW3","gen_row_right[3]","iob_ts_mid"),
    (20,40,"TS_ROW1","gen_row_right[1]","iob_ts_mid"),
    (20,53,"TS_LONG","long_row[0]","iob_ts_mid"),
    (14,30,"IN_ROW3","iob_in_mid","gen_row_right[3]"),
    (14,40,"IN_ROW1","iob_in_mid","gen_row_right[1]"),
    (14,53,"IN_LONG","iob_in_mid","long_row[0]"),
    (-19,79,"IN_LONG1","iob_in_mid","long_col[1]"),
    (-32,79,"IN_COL3","iob_in_mid","gen_col_bot[3]"),
    (-43,79,"IN_COL1","iob_in_mid","gen_col_bot[1]"),
    (-53,79,"IN_LONG2_COL","iob_in_mid","long_col[2]"),
    (9,19,"OUT_GLOBAL","global_","iob_out_mid"),
    (9,24,"OUT_LONG2_ROW","long_row[1]","iob_out_mid"),
    (9,35,"OUT_ROW2","gen_row_right[2]","iob_out_mid"),
    (9,45,"OUT_ROW0","gen_row_right[0]","iob_out_mid"),
    (-25,58,"OUT_LONG0","long_col[0]","iob_out_mid"),
    (-38,58,"OUT_COL2","gen_col_bot[2]","iob_out_mid"),
    (-48,58,"OUT_COL0","gen_col_bot[0]","iob_out_mid"),
    (-53,58,"OUT_LONG2_COL","long_col[2]","iob_out_mid")
]
# bidirectional
TOP_LEFT_CORNER_PIP = [
    (33,40,"LONG2_COL_LONG2_ROW","long_row[1]","long_col[2]"),
    (33,46,"LONG2_COL_ROW3","gen_row_right[3]","long_col[2]"),
    (38,40,"LONG2_ROW_COL0","long_row[1]","gen_col_bot[0]"),
    (38,46,"COL0_ROW3","gen_row_right[3]","gen_col_bot[0]"),
    (43,51,"COL1_ROW2","gen_row_right[2]","gen_col_bot[1]"),
    (48,56,"COL2_ROW1","gen_row_right[1]","gen_col_bot[2]"),
    (53,61,"COL3_ROW0","gen_row_right[0]","gen_col_bot[3]"),
    (53,69,"COL3_LONG","long_row[0]","gen_col_bot[3]"),
    (61,69,"LONG0_LONG","long_row[0]","long_col[0]"),
    (66,69,"LONG1_LONG","long_row[0]","long_col[1]"),
    (67,56,"LONG1_ROW1","gen_row_right[1]","long_col[1]"),
    (61,41,"LONG0_LONG2_ROW","long_row[1]","long_col[0]")
]
# unidirectional
GLOBALIN_PIP = [
    (48,90,"COL2","gen_col_bot[2]"),
    (61,90,"LONG0","long_col[0]"),
    (90,56,"ROW1","gen_row_right[1]"),
    (90,69,"LONG","long_row[0]"),
    (90,95,"P9","iob_in_mid"),
    (90,142,"P11","iob_in_bot")
]
# unidirectional
IOB_P61_PIP = [
    (14,24,"TS_LONG2_ROW","long_row[1]","iob_ts_right"),
    (14,30,"TS_ROW3","gen_row_left[3]","iob_ts_right"),
    (14,40,"TS_ROW1","gen_row_left[1]","iob_ts_right"),
    (14,53,"TS_LONG","long_row[0]","iob_ts_right"),
    (9,24,"IN_LONG2_ROW","iob_in_right","long_row[1]"),
    (9,35,"IN_ROW2","iob_in_right","gen_row_left[2]"),
    (9,45,"IN_ROW0","iob_in_right","gen_row_left[0]"),
    (45,64,"IN_LONG1","iob_in_right","long_col[1]"),
    (59,64,"IN_COL1","iob_in_left","gen_col_bot[1]"),
    (69,64,"IN_COL3","iob_in_left","gen_col_bot[3]"),
    (74,64,"IN_LONG2_COL","iob_in_left","long_col[2]"),
    (4,30,"OUT_ROW3","gen_row_left[3]","iob_out_right"),
    (4,40,"OUT_ROW1","gen_row_left[1]","iob_out_right"),
    (4,53,"OUT_LONG","long_row[0]","iob_out_right"),
    (14,69,"OUT_X","clb_x","iob_out_right"),
    (40,69,"OUT_LONG0","long_col[0]","iob_out_left"),
    (53,69,"OUT_COL0","gen_col_bot[0]","iob_out_left"),
    (64,69,"OUT_COL2","gen_col_bot[2]","iob_out_left"),
    (74,69,"OUT_LONG2_COL","long_col[2]","iob_out_left")
]
# bidirectional
TOP_RIGHT_CORNER_PIP = [
    (808,35,"IOCLK_TOP_GLOBAL","global_","ioclk_top"),
    (808,46,"IOCLK_TOP_ROW3","gen_row_left[3]","ioclk_top"),
    (808,51,"IOCLK_TOP_ROW2","gen_row_left[2]","ioclk_top"),
    (808,56,"IOCLK_TOP_ROW1","gen_row_left[1]","ioclk_top"),
    (808,61,"IOCLK_TOP_ROW0","gen_row_left[0]","ioclk_top"),
    (808,69,"IOCLK_TOP_LONG","long_row[0]","ioclk_top"),
    (813,74,"IOCLK_RIGHT_GLOBAL","ioclk_right","global_"),
    (824,74,"IOCLK_RIGHT_LONG1","ioclk_right","long_col[1]"),
    (831,74,"IOCLK_RIGHT_COL0","ioclk_right","gen_col_bot[0]"),
    (837,74,"IOCLK_RIGHT_COL1","ioclk_right","gen_col_bot[1]"),
    (842,74,"IOCLK_RIGHT_COL2","ioclk_right","gen_col_bot[2]"),
    (847,74,"IOCLK_RIGHT_COL3","ioclk_right","gen_col_bot[3]"),
    (818,69,"LONG_LONG0","long_row[0]","long_col[0]"),
    (824,69,"LONG_LONG1","long_row[0]","long_col[1]"),
    (831,61,"ROW0_COL0","gen_row_left[0]","gen_col_bot[0]"),
    (837,56,"ROW1_COL1","gen_row_left[1]","gen_col_bot[1]"),
    (842,51,"ROW2_COL2","gen_row_left[2]","gen_col_bot[2]"),
    (847,46,"ROW3_COL3","gen_row_left[3]","gen_col_bot[3]"),
    (847,40,"COL3_LONG2_ROW","long_row[1]","gen_col_bot[3]"),
    (852,40,"LONG2_ROW_LONG2_COL","long_row[1]","long_col[2]"),
    (852,46,"ROW3_LONG2_COL","gen_row_left[3]","long_col[2]")
]
# unidirectional
IOB_P43_PIP = [
    (14,-14,"TS_LONG2_ROW","long_row[1]","iob_ts_right"),
    (14,-19,"TS_ROW0","gen_row_left[0]","iob_ts_right"),
    (14,-30,"TS_ROW2","gen_row_left[2]","iob_ts_right"),
    (14,-43,"TS_LONG","long_row[0]","iob_ts_right"),
    (9,-14,"IN_LONG2_ROW","iob_in_right","long_row[1]"),
    (9,-24,"IN_ROW1","iob_in_right","gen_row_left[1]"),
    (9,-35,"IN_ROW3","iob_in_right","gen_row_left[3]"),
    (40,-53,"IN_LONG0","iob_in_right","long_col[0]"),
    (53,-53,"IN_COL0","iob_in_left","gen_col_top[0]"),
    (64,-53,"IN_COL2","iob_in_left","gen_col_top[2]"),
    (74,-53,"IN_LONG2_COL","iob_in_left","long_col[2]"),
    (4,-6,"OUT_ALT","alt","iob_out_right"),
    (4,-19,"OUT_ROW0","gen_row_left[0]","iob_out_right"),
    (4,-30,"OUT_ROW2","gen_row_left[2]","iob_out_right"),
    (4,-43,"OUT_LONG","long_row[0]","iob_out_right"),
    (14,-58,"OUT_X","x_top","iob_out_right"),
    (46,-58,"OUT_LONG1","long_col[1]","iob_out_left"),
    (59,-58,"OUT_COL1","gen_col_top[1]","iob_out_left"),
    (69,-58,"OUT_COL3","gen_col_top[3]","iob_out_left"),
    (74,-58,"OUT_LONG2_COL","long_col[2]","iob_out_left")
]
# bidirectional
BOT_RIGHT_CORNER_PIP = [
    (818,821,"LONG_LONG0","long_row[0]","long_col[0]"),
    (824,821,"LONG_LONG1","long_row[0]","long_col[1]"),
    (831,829,"ROW3_COL0","gen_row_left[3]","gen_col_top[0]"),
    (837,834,"ROW2_COL1","gen_row_left[2]","gen_col_top[1]"),
    (842,840,"ROW1_COL2","gen_row_left[1]","gen_col_top[2]"),
    (847,845,"ROW0_COL3","gen_row_left[0]","gen_col_top[3]"),
    (847,850,"COL3_LONG2_ROW","long_row[1]","gen_col_top[3]"),
    (852,850,"LONG2_ROW_LONG2_COL","long_row[1]","long_col[2]"),
    (852,845,"ROW0_LONG2_COL","gen_row_left[0]","long_col[2]")
]
# unidirectional
ALTIN_PIP = [
    (808,848,"INTOSC","intosc"),
    (797,834,"ROW2","gen_row_left[2]"),
    (797,821,"LONG","long_row[0]"),
    (797,811,"P43","iob_in_left"),
    (813,816,"P46","iob_in_top"),
    (824,816,"LONG1","long_col[1]"),
    (837,816,"COL1","gen_col_top[1]")
]
# unidirectional
IOB_P27_PIP = [
    (20,-14,"TS_LONG2_ROW","long_row[1]","iob_ts_mid"),
    (20,-19,"TS_ROW0","gen_row_right[0]","iob_ts_mid"),
    (20,-30,"TS_ROW2","gen_row_right[2]","iob_ts_mid"),
    (20,-43,"TS_LONG","long_row[0]","iob_ts_mid"),
    (14,-19,"IN_ROW0","iob_in_mid","gen_row_right[0]"),
    (14,-30,"IN_ROW2","iob_in_mid","gen_row_right[2]"),
    (14,-43,"IN_LONG","iob_in_mid","long_row[0]"),
    (-19,-64,"IN_LONG1","iob_in_mid","long_col[1]"),
    (-32,-64,"IN_COL3","iob_in_mid","gen_col_top[3]"),
    (-43,-64,"IN_COL1","iob_in_mid","gen_col_top[1]"),
    (-53,-64,"IN_LONG2_COL","iob_in_mid","long_col[2]"),
    (9,-14,"OUT_LONG2_ROW","long_row[1]","iob_out_mid"),
    (9,-24,"OUT_ROW1","gen_row_right[1]","iob_out_mid"),
    (9,-35,"OUT_ROW3","gen_row_right[3]","iob_out_mid"),
    (-25,-58,"OUT_LONG0","long_col[0]","iob_out_mid"),
    (-38,-58,"OUT_COL2","gen_col_top[2]","iob_out_mid"),
    (-48,-58,"OUT_COL0","gen_col_top[0]","iob_out_mid"),
    (-53,-58,"OUT_LONG2_COL","long_col[2]","iob_out_mid")
]
# bidirectional
BOT_LEFT_CORNER_PIP = [
    (72,795,"IOCLK_LEFT_GLOBAL","ioclk_left","global_"),
    (61,795,"IOCLK_LEFT_LONG0","ioclk_left","long_col[0]"),
    (54,795,"IOCLK_LEFT_COL3","ioclk_left","gen_col_top[3]"),
    (48,795,"IOCLK_LEFT_COL2","ioclk_left","gen_col_top[2]"),
    (43,795,"IOCLK_LEFT_COL1","ioclk_left","gen_col_top[1]"),
    (38,795,"IOCLK_LEFT_COL0","ioclk_left","gen_col_top[0]"),
    (77,816,"IOCLK_BOT_GLOBAL","global_","ioclk_bot"),
    (77,821,"IOCLK_BOT_LONG","long_row[0]","ioclk_bot"),
    (77,829,"IOCLK_BOT_ROW3","gen_row_right[3]","ioclk_bot"),
    (77,834,"IOCLK_BOT_ROW2","gen_row_right[2]","ioclk_bot"),
    (77,840,"IOCLK_BOT_ROW1","gen_row_right[1]","ioclk_bot"),
    (77,845,"IOCLK_BOT_ROW0","gen_row_right[0]","ioclk_bot"),
    (54,821,"LONG_COL3","long_row[0]","gen_col_top[3]"),
    (61,821,"LONG_LONG0","long_row[0]","long_col[0]"),
    (67,821,"LONG_LONG1","long_row[0]","long_col[1]"),
    (67,834,"LONG1_ROW2","gen_row_right[2]","long_col[1]"),
    (62,850,"LONG0_LONG2_ROW","long_row[1]","long_col[0]"),
    (54,829,"ROW3_COL3","gen_row_right[3]","gen_col_top[3]"),
    (48,834,"ROW2_COL2","gen_row_right[2]","gen_col_top[2]"),
    (43,840,"ROW1_COL1","gen_row_right[1]","gen_col_top[1]"),
    (38,845,"ROW0_COL0","gen_row_right[0]","gen_col_top[0]"),
    (33,845,"ROW0_LONG2_COL","gen_row_right[0]","long_col[2]"),
    (33,850,"LONG2_ROW_LONG2_COL","long_row[1]","long_col[2]"),
    (38,850,"COL0_LONG2_ROW","long_row[1]","gen_col_top[0]")
]
SWITCH_CONNS = [
    "1_3",
    "1_5",
    "1_6",
    "1_7",
    "1_8",
    "2_3",
    "2_4",
    "2_5",
    "2_6",
    "2_8",
    "3_1",
    "3_2",
    "3_5",
    "3_7",
    "3_8",
    "4_2",
    "4_5",
    "4_6",
    "4_7",
    "4_8",
    "5_1",
    "5_2",
    "5_3",
    "5_4",
    "5_7",
    "6_1",
    "6_2",
    "6_4",
    "6_7",
    "6_8",
    "7_1",
    "7_3",
    "7_4",
    "7_5",
    "7_6",
    "8_1",
    "8_2",
    "8_3",
    "8_4",
    "8_6"
]
