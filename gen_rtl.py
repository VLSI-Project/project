#!/usr/bin/env python3

from defines import *

IOB_NAMES = {
    (0,0): ("P9","P8"),
    (1,0): ("P7","P6"),
    (2,0): ("P5","P4"),
    (3,0): ("P3","P2"),
    (4,0): ("P68","P67"),
    (5,0): ("P66","P65"),
    (6,0): ("P64","P63"),
    (7,0): ("P62","P61"),

    (8,1): ("P59","P58"),
    (8,2): ("P57","P56"),
    (8,3): ("P55","P54"),
    (8,4): ("P53",""),
    (8,5): ("P51","P50"),
    (8,6): ("P49","P48"),
    (8,7): ("P47","P46"),

    (0,8): ("P27","P28"),
    (1,8): ("P29","P30"),
    (2,8): ("P31","P32"),
    (3,8): ("P33","P34"),
    (4,8): ("P36","P37"),
    (5,8): ("P38","P39"),
    (6,8): ("P40","P41"),
    (7,8): ("P42","P43"),

    (0,1): ("P11","P12"),
    (0,2): ("P13","P14"),
    (0,3): ("P15","P16"),
    (0,4): ("P17",""),
    (0,5): ("P19","P20"),
    (0,6): ("P21","P22"),
    (0,7): ("P23","P24"),
}

class GenRTL:
    def __init__(self):
        self.numCLBs = 0
        self.numSwitches = 0
        self.numIOBs = 0
        self.numPIPs = 0
    def w(self, lines: str):
        self.outfile.write(lines)
    def begin(self, moduleName: str):
        self.outfile = open("rtl/"+moduleName+".v", "w")
        self.shiftIn = "shift_i"
        self.shiftIndex = 0
        self.w("""`timescale 1ns/1ps

module {}(
  input shift_clk,
  input shift_en,
  input shift_i,
  output shift_o""".format(moduleName))
    def port(self, port: str):
        self.w(",\n  " + port)
    def endPorts(self):
        self.w(");\n\n")
    def end(self):
        self.w("""  assign shift_o = {};

endmodule
""".format(self.shiftIn))
        self.outfile.close()
    def clb(self, name: str):
        shiftOut = "shift"+str(self.shiftIndex)
        self.w("""  // {}
  wire {};
  tri clb_a, clb_b, clb_c, clb_k;
  clb clb(
    .shift_clk(shift_clk),
    .shift_en(shift_en),
    .shift_i({}),
    .shift_o({}),
    .a(clb_a),
    .b(clb_b),
    .c(clb_c),
    .d(clb_d),
    .k(clb_k),
    .x(clb_x),
    .y(clb_y));

""".format(name, shiftOut, self.shiftIn, shiftOut))
        self.shiftIndex += 1
        self.shiftIn = shiftOut
        self.numCLBs += 1
    def switch(self, name: str, index: int, sides: str = "NESW"):
        index *= 2
        north = 1 if ("N" in sides) else 0
        east = 1 if ("E" in sides) else 0
        south = 1 if ("S" in sides) else 0
        west = 1 if ("W" in sides) else 0
        shiftOut = "shift"+str(self.shiftIndex)
        self.w("""  // {}
  wire {};
  switch #({},{},{},{}) switch{}(
    .shift_clk(shift_clk),
    .shift_en(shift_en),
    .shift_i({}),
    .shift_o({}),
    .pin1({}),
    .pin2({}),
    .pin3({}),
    .pin4({}),
    .pin5({}),
    .pin6({}),
    .pin7({}),
    .pin8({}));

""".format(name, shiftOut,
           north, east, south, west,
           self.shiftIndex, self.shiftIn, shiftOut,
           "gen_col_top[{}]".format(index) if north else "",
           "gen_col_top[{}]".format(index+1) if north else "",
           "gen_row_right[{}]".format(index+1) if east else "",
           "gen_row_right[{}]".format(index) if east else "",
           "gen_col_bot[{}]".format(index+1) if south else "",
           "gen_col_bot[{}]".format(index) if south else "",
           "gen_row_left[{}]".format(index) if west else "",
           "gen_row_left[{}]".format(index+1) if west else ""))
        self.shiftIndex += 1
        self.shiftIn = shiftOut
        self.numSwitches += 1
    def pip(self, name: str, a: str, b: str, uni: bool = False):
        shiftOut = "shift"+str(self.shiftIndex)
        self.w("""  // {}
  wire {};
  pip{} pip{}(
    .shift_clk(shift_clk),
    .shift_en(shift_en),
    .shift_i({}),
    .shift_o({}),
    .a({}),
    .b({}));

""".format(name, shiftOut, "_uni" if uni else "", self.shiftIndex, self.shiftIn, shiftOut, a, b))
        self.shiftIndex += 1
        self.shiftIn = shiftOut
        self.numPIPs += 1
    def iob(self, name: str, place: str, ioclk: str):
        shiftOut = "shift"+str(self.shiftIndex)
        self.w("""  // {}
  wire {};
  iob iob_{}(
    .shift_clk(shift_clk),
    .shift_en(shift_en),
    .shift_i({}),
    .shift_o({}),
    .io_clk({}),
    .ts(iob_ts_{}),
    .in(iob_in_{}),
    .out(iob_out_{}),
    .pin(iob_pin_{}));

""".format(name, shiftOut, place, self.shiftIn, shiftOut, ioclk, place, place, place, place))
        self.shiftIndex += 1
        self.shiftIn = shiftOut
        self.numIOBs += 1

if __name__ == "__main__":
    gen = GenRTL()
    top = open("rtl/top.v", "w")
    top.write("""`timescale 1ns/1ps

module top(
  input shift_clk,
  input shift_en,
  input shift_i,
  output shift_o,

  inout tri [15:0] iob_pin_top,
  inout tri [15:0] iob_pin_right,
  inout tri [15:0] iob_pin_bot,
  inout tri [15:0] iob_pin_left);

  wire [81:0] shift;
  tri  [3:0]  gen_row [0:71];
  tri  [4:0]  gen_col [0:71];
  tri  [1:0]  long_row [0:8];
  tri  [2:0]  long_col [0:8];
  tri  [63:0] clb_d;
  wire [63:0] clb_x;
  wire [63:0] clb_y;
  tri         global_;
  tri         alt;
  tri         ioclk_top;
  tri         ioclk_bot;
  tri         ioclk_left;
  tri         ioclk_right;
  wire [7:0]  top_iob_in;
  wire [7:0]  top_iob_out;
  wire [7:0]  bot_iob_in;
  wire [7:0]  bot_iob_out;
  wire [7:0]  left_iob_in;
  wire [7:0]  right_iob_out;
  wire        right_iob_in;
  wire [7:0]  bot_iob_in_mid;

  assign shift[0] = shift_i;
  assign shift_o = shift[81];

""")
    for y in range(9):
        for x in range(9):
            tileName = "tile_"+chr(0x41+y)+chr(0x41+x)
            idx = (y * 9) + x
            gen.begin(tileName)
            top.write("""  {} {}(
    .shift_clk(shift_clk),
    .shift_en(shift_en),
    .shift_i(shift[{}]),
    .shift_o(shift[{}]),
    .global_(global_)""".format(tileName, tileName, idx, idx+1))
            if x > 0:
                gen.port("inout tri [3:0] gen_row_left")
                top.write(",\n    .gen_row_left(gen_row[{}])".format((y*8)+x-1))
            if x < 8:
                gen.port("inout tri [3:0] gen_row_right")
                top.write(",\n    .gen_row_right(gen_row[{}])".format((y*8)+x))
            ################
            if y > 0:
                if x == 0 or x == 8:
                    gen.port("inout tri [3:0] gen_col_top")
                    top.write(",\n    .gen_col_top(gen_col[{}][3:0])".format(((y-1)*9)+x))
                else:
                    gen.port("inout tri [4:0] gen_col_top")
                    top.write(",\n    .gen_col_top(gen_col[{}])".format(((y-1)*9)+x))
            if y < 8:
                if x == 0 or x == 8:
                    gen.port("inout tri [3:0] gen_col_bot")
                    top.write(",\n    .gen_col_bot(gen_col[{}][3:0])".format((y*9)+x))
                else:
                    gen.port("inout tri [4:0] gen_col_bot")
                    top.write(",\n    .gen_col_bot(gen_col[{}])".format((y*9)+x))
            ################
            if y == 0 or y == 8:
                gen.port("inout tri [1:0] long_row");
                top.write(",\n    .long_row(long_row[{}])".format(y))
            else:
                gen.port("inout tri long_row")
                top.write(",\n    .long_row(long_row[{}][0])".format(y))
            ################
            if x == 0 or x == 8:
                gen.port("inout tri [2:0] long_col");
                top.write(",\n    .long_col(long_col[{}])".format(x))
            else:
                gen.port("inout tri [1:0] long_col");
                top.write(",\n    .long_col(long_col[{}][1:0])".format(x))
            ################
            if x == 0 and y == 0:
                gen.port("output tri global_")
            else:
                gen.port("input global_")
            ################
            if x < 8 and y > 0:
                gen.port("input x_top")
                top.write(",\n    .x_top(clb_x[{}])".format(((y-1)*8)+x))
            if x < 8 and y < 8:
                gen.port("input x_bot")
                if y == 7:
                    top.write(",\n    .x_bot(bot_iob_in_mid[{}])".format(x))
                else:
                    top.write(",\n    .x_bot(clb_x[{}])".format(((y+1)*8)+x))
            if x > 0 and y < 8:
                gen.port("input x_left")
                top.write(",\n    .x_left(clb_x[{}])".format((y*8)+x-1))
                gen.port("input y_left")
                top.write(",\n    .y_left(clb_y[{}])".format((y*8)+x-1))
            if y > 0 and x < 8:
                gen.port("output tri d_top")
                top.write(",\n    .d_top(clb_d[{}])".format(((y-1)*8)+x))
            ################
            if y == 8:
                if x == 8:
                    gen.port("output tri alt")
                else:
                    gen.port("input alt")
                top.write(",\n    .alt(alt)")
            ################
            if x < 8 and y < 8:
                gen.port("input clb_d")
                top.write(",\n    .clb_d(clb_d[{}])".format((y*8)+x))
                gen.port("output clb_x")
                top.write(",\n    .clb_x(clb_x[{}])".format((y*8)+x))
                gen.port("output clb_y")
                top.write(",\n    .clb_y(clb_y[{}])".format((y*8)+x))
            ################
            if x == 0:
                if y == 0:
                    gen.port("input ioclk_top")
                    top.write(",\n    .ioclk_top(ioclk_top)")
                    gen.port("output iob_in_right")
                    top.write(",\n    .iob_in_right(top_iob_in[0])")
                    gen.port("input iob_out_right")
                    top.write(",\n    .iob_out_right(top_iob_out[0])")
                    gen.port("input iob_in_bot")
                    top.write(",\n    .iob_in_bot(left_iob_in[0])")
                    gen.port("inout tri iob_pin_mid")
                    top.write(",\n    .iob_pin_mid(iob_pin_top[0])")
                    gen.port("inout tri iob_pin_right")
                    top.write(",\n    .iob_pin_right(iob_pin_top[1])")
                elif y == 8:
                    gen.port("output tri ioclk_left")
                    top.write(",\n    .ioclk_left(ioclk_left)")
                    gen.port("output tri ioclk_bot")
                    top.write(",\n    .ioclk_bot(ioclk_bot)")
                    gen.port("output iob_in_mid")
                    top.write(",\n    .iob_in_mid(left_iob_in[7])")
                    gen.port("output iob_in_right")
                    top.write(",\n    .iob_in_right(bot_iob_in[0])")
                    gen.port("input iob_out_right")
                    top.write(",\n    .iob_out_right(bot_iob_out[0])")
                    gen.port("inout tri iob_pin_mid")
                    top.write(",\n    .iob_pin_mid(iob_pin_bot[0])")
                    gen.port("inout tri iob_pin_right")
                    top.write(",\n    .iob_pin_right(iob_pin_bot[1])")
                else:
                    gen.port("input ioclk_left")
                    top.write(",\n    .ioclk_left(ioclk_left)")
                    gen.port("output iob_in_top")
                    top.write(",\n    .iob_in_top(left_iob_in[{}])".format(y-1))
                    gen.port("input iob_in_bot")
                    top.write(",\n    .iob_in_bot(left_iob_in[{}])".format(y))
                    gen.port("inout tri iob_pin_top")
                    top.write(",\n    .iob_pin_top(iob_pin_left[{}])".format(y*2))
                    if y != 4:
                        gen.port("inout tri iob_pin_mid")
                        top.write(",\n    .iob_pin_mid(iob_pin_left[{}])".format((y*2)+1))
            elif x == 8:
                if y == 0:
                    gen.port("output tri ioclk_top")
                    top.write(",\n    .ioclk_top(ioclk_top)")
                    gen.port("output tri ioclk_right")
                    top.write(",\n    .ioclk_right(ioclk_right)")
                    gen.port("input iob_in_left")
                    top.write(",\n    .iob_in_left(top_iob_in[7])")
                    gen.port("output iob_out_left")
                    top.write(",\n    .iob_out_left(top_iob_out[7])")
                    gen.port("output iob_out_bot")
                    top.write(",\n    .iob_out_bot(right_iob_out[0])")
                elif y == 8:
                    gen.port("input iob_in_top")
                    top.write(",\n    .iob_in_top(right_iob_in)")
                    gen.port("input iob_in_left")
                    top.write(",\n    .iob_in_left(bot_iob_in[7])")
                    gen.port("output iob_out_left")
                    top.write(",\n    .iob_out_left(bot_iob_out[7])")
                else:
                    gen.port("input ioclk_right")
                    top.write(",\n    .ioclk_right(ioclk_right)")
                    gen.port("input iob_out_top")
                    top.write(",\n    .iob_out_top(right_iob_out[{}])".format(y-1))
                    gen.port("output iob_out_bot")
                    top.write(",\n    .iob_out_bot(right_iob_out[{}])".format(y))
                    if y == 7:
                        gen.port("output iob_in_mid")
                        top.write(",\n    .iob_in_mid(right_iob_in)")
                    gen.port("inout tri iob_pin_top")
                    top.write(",\n    .iob_pin_top(iob_pin_right[{}])".format(y*2))
                    if y != 4:
                        gen.port("inout tri iob_pin_mid")
                        top.write(",\n    .iob_pin_mid(iob_pin_right[{}])".format((y*2)+1))
            else:
                if y == 0:
                    gen.port("input ioclk_top")
                    top.write(",\n    .ioclk_top(ioclk_top)")
                    gen.port("output iob_in_right")
                    top.write(",\n    .iob_in_right(top_iob_in[{}])".format(x))
                    gen.port("input iob_out_right")
                    top.write(",\n    .iob_out_right(top_iob_out[{}])".format(x))
                    gen.port("input iob_in_left")
                    top.write(",\n    .iob_in_left(top_iob_in[{}])".format(x-1))
                    gen.port("output iob_out_left")
                    top.write(",\n    .iob_out_left(top_iob_out[{}])".format(x-1))
                    gen.port("inout tri iob_pin_mid")
                    top.write(",\n    .iob_pin_mid(iob_pin_top[{}])".format(x*2))
                    gen.port("inout tri iob_pin_right")
                    top.write(",\n    .iob_pin_right(iob_pin_top[{}])".format((x*2)+1))
                elif y == 8:
                    gen.port("input ioclk_bot")
                    top.write(",\n    .ioclk_bot(ioclk_bot)")
                    gen.port("input iob_in_left")
                    top.write(",\n    .iob_in_left(bot_iob_in[{}])".format(x-1))
                    gen.port("output iob_out_left")
                    top.write(",\n    .iob_out_left(bot_iob_out[{}])".format(x-1))
                    gen.port("output iob_in_mid")
                    top.write(",\n    .iob_in_mid(bot_iob_in_mid[{}])".format(x))
                    gen.port("output iob_in_right")
                    top.write(",\n    .iob_in_right(bot_iob_in[{}])".format(x))
                    gen.port("input iob_out_right")
                    top.write(",\n    .iob_out_right(bot_iob_out[{}])".format(x))
                    gen.port("inout tri iob_pin_mid")
                    top.write(",\n    .iob_pin_mid(iob_pin_bot[{}])".format(x*2))
                    gen.port("inout tri iob_pin_right")
                    top.write(",\n    .iob_pin_right(iob_pin_bot[{}])".format((x*2)+1))
            gen.endPorts()
            top.write(");\n\n")

            if x < 8 and y < 8:
                gen.clb("CLB_"+chr(0x41+y)+chr(0x41+x))

            if not ((x == 0 or x == 8) and (y == 0 or y == 8)):
                sides = ""
                if y > 0:
                    sides += "N"
                if x < 8:
                    sides += "E"
                if y < 8:
                    sides += "S"
                if x > 0:
                    sides += "W"
                switchName = chr(0x41+y) + chr(0x41+x)
                if x == 0:
                    switchName = "LEFT" + str(y-1)
                if x == 8:
                    switchName = "RIGHT" + str(y-1)
                if y == 0:
                    switchName = "TOP" + str(x-1)
                if y == 8:
                    switchName = "BOT" + str(x-1)
                gen.switch("SW_"+switchName+"_0", 0, sides)
                gen.switch("SW_"+switchName+"_1", 1, sides)

            if y == 0 and x < 8:
                iobNames = IOB_NAMES[(x,y)]
                gen.iob("IOB_"+iobNames[0], "mid", "ioclk_top")
                gen.iob("IOB_"+iobNames[1], "right", "ioclk_top")
                pipName = "PIP_IOB_"+iobNames[0]+"_"
                if x > 0:
                    for pip in IOB_TOP_LEFT_PIP:
                        gen.pip(pipName+pip[2], pip[3], pip[4], True)
                else:
                    for pip in IOB_P9_PIP:
                        gen.pip(pipName+pip[2], pip[3], pip[4], True)
                pipNameRight = "PIP_IOB_"+iobNames[1]+"_"
                if x > 0:
                    pipNameLeft = "PIP_IOB_"+IOB_NAMES[(x-1,y)][1]+"_"
                if x < 7:
                    for pip in IOB_TOP_RIGHT_PIP:
                        if ("iob" in pip[3] and "_left" in pip[3]) or ("iob" in pip[4] and "_left" in pip[4]):
                            if x == 0:
                                continue
                            gen.pip(pipNameLeft+pip[2], pip[3], pip[4], True)
                        else:
                            gen.pip(pipNameRight+pip[2], pip[3], pip[4], True)
                else:
                    for pip in IOB_TOP_RIGHT_PIP:
                        if ("iob" in pip[3] and "_right" in pip[3]) or ("iob" in pip[4] and "_right" in pip[4]):
                            continue
                        gen.pip(pipNameLeft+pip[2], pip[3], pip[4], True)
                    for pip in IOB_P61_PIP:
                        if ("iob" in pip[3] and "_left" in pip[3]) or ("iob" in pip[4] and "_left" in pip[4]):
                            continue
                        gen.pip(pipNameRight+pip[2], pip[3], pip[4], True)

            if x == 8 and y > 0 and y < 8:
                iobNames = IOB_NAMES[(x,y)]
                if y != 4:
                    gen.iob("IOB_"+iobNames[1], "mid", "ioclk_right")
                gen.iob("IOB_"+iobNames[0], "top", "ioclk_right")
                pipName = "PIP_IOB_"+iobNames[0]+"_"
                for pip in IOB_RIGHT_TOP_PIP:
                    gen.pip(pipName+pip[2], pip[3], pip[4], True)
                pipName = "PIP_IOB_"+iobNames[1]+"_"
                if y != 4:
                    for pip in IOB_RIGHT_BOT_PIP:
                        gen.pip(pipName+pip[2], pip[3], pip[4], True)
            if y == 8 and x < 8:
                iobNames = IOB_NAMES[(x,y)]
                gen.iob("IOB_"+iobNames[0], "mid", "ioclk_bot")
                gen.iob("IOB_"+iobNames[1], "right", "ioclk_bot")
                pipName = "PIP_IOB_"+iobNames[0]+"_"
                if x > 0:
                    for pip in IOB_BOT_LEFT_PIP:
                        gen.pip(pipName+pip[2], pip[3], pip[4], True)
                pipNameRight = "PIP_IOB_"+iobNames[1]+"_"
                if x > 0:
                    pipNameLeft = "PIP_IOB_"+IOB_NAMES[(x-1,y)][1]+"_"
                if x < 7:
                    for pip in IOB_BOT_RIGHT_PIP:
                        if ("iob" in pip[3] and "_left" in pip[3]) or ("iob" in pip[4] and "_left" in pip[4]):
                            if x == 0:
                                continue
                            gen.pip(pipNameLeft+pip[2], pip[3], pip[4], True)
                        else:
                            gen.pip(pipNameRight+pip[2], pip[3], pip[4], True)
                else:
                    for pip in IOB_BOT_RIGHT_PIP:
                        if ("iob" in pip[3] and "_right" in pip[3]) or ("iob" in pip[4] and "_right" in pip[4]):
                            continue
                        gen.pip(pipNameLeft+pip[2], pip[3], pip[4], True)
                    for pip in IOB_P43_PIP:
                        if ("iob" in pip[3] and "_left" in pip[3]) or ("iob" in pip[4] and "_left" in pip[4]):
                            continue
                        gen.pip(pipNameRight+pip[2], pip[3], pip[4], True)
            if x == 0 and y > 0 and y < 8:
                iobNames = IOB_NAMES[(x,y)]
                if y != 4:
                    gen.iob("IOB_"+iobNames[1], "mid", "ioclk_left")
                gen.iob("IOB_"+iobNames[0], "top", "ioclk_left")
                pipName = "PIP_IOB_"+iobNames[0]+"_"
                for pip in IOB_LEFT_TOP_PIP:
                    gen.pip(pipName+pip[2], pip[3], pip[4], True)
                pipName = "PIP_IOB_"+iobNames[1]+"_"
                if y != 4:
                    for pip in IOB_LEFT_BOT_PIP:
                        gen.pip(pipName+pip[2], pip[3], pip[4], True)

            if x < 8 and y < 8:
                pipName = "PIP_"+chr(0x41+y)+chr(0x41+x)+"_"
                if y > 0:
                    for pip in CLB_PIP_A:
                        gen.pip(pipName+"A_"+pip[2], pip[3], "clb_a", True)
                else:
                    for pip in CLB_TOP_PIP_A:
                        gen.pip(pipName+"A_"+pip[2], pip[3], "clb_a", True)
                if x > 0:
                    for pip in CLB_PIP_B:
                        b = pip[3]
                        if y == 0 and pip[2] == "X":
                            b = "iob_in_mid"
                        gen.pip(pipName+"B_"+pip[2], b, "clb_b", True)
                    for pip in CLB_PIP_C:
                        gen.pip(pipName+"C_"+pip[2], pip[3], "clb_c", True)
                    for pip in CLB_PIP_K:
                        gen.pip(pipName+"K_"+pip[2], pip[3], "clb_k", True)
                else:
                    for pip in CLB_LEFT_PIP_B:
                        b = pip[3]
                        if y == 0 and pip[2] == "X":
                            b = "iob_in_mid"
                        if y == 7 and pip[2] == "IOB":
                            b = "iob_in_mid"
                        gen.pip(pipName+"B_"+pip[2], b, "clb_b", True)
                    for pip in CLB_LEFT_PIP_C:
                        gen.pip(pipName+"C_"+pip[2], pip[3], "clb_c", True)
                    for pip in CLB_LEFT_PIP_K:
                        gen.pip(pipName+"K_"+pip[2], pip[3], "clb_k", True)

            if x < 8 and y > 0:
                pipName = "PIP_"+chr(0x41+y-1)+chr(0x41+x)+"_"
                if y < 8:
                    for pip in CLB_PIP_D:
                        gen.pip(pipName+"D_"+pip[2], pip[3], "d_top", True)
                else:
                    for pip in CLB_BOT_PIP_D:
                        gen.pip(pipName+"D_"+pip[2], pip[3], "d_top", True)

            if x > 0 and y < 8:
                pipName = "PIP_"+chr(0x41+y)+chr(0x41+x-1)+"_"
                if x < 8:
                    for pip in CLB_PIP_X:
                        gen.pip(pipName+"X_"+pip[2], "x_left", pip[3], True)
                    for pip in CLB_PIP_Y:
                        gen.pip(pipName+"Y_"+pip[2], "y_left", pip[3], True)
                else:
                    for pip in CLB_RIGHT_PIP_X:
                        if y == 4 and pip[2] == "OUTHI":
                            continue
                        gen.pip(pipName+"X_"+pip[2], "x_left", pip[3], True)
                    for pip in CLB_RIGHT_PIP_Y:
                        if y == 4 and pip[2] == "OUTHI":
                            continue
                        gen.pip(pipName+"Y_"+pip[2], "y_left", pip[3], True)

            if x > 0 and x < 8 and y > 0 and y < 8:
                pipName = "PIP_SW_"+chr(0x41+y)+chr(0x41+x)+"_"
                for pip in SWITCH_PIP:
                    gen.pip(pipName+pip[2], pip[3], pip[4])
            if x == 0 and y > 0 and y < 8:
                pipName = "PIP_SW_LEFT"+str(y-1)+"_"
                for pip in SWITCH_LEFT_PIP:
                    gen.pip(pipName+pip[2], pip[3], pip[4])
            if y == 0 and x > 0 and x < 8:
                pipName = "PIP_SW_TOP"+str(x-1)+"_"
                for pip in SWITCH_TOP_PIP:
                    gen.pip(pipName+pip[2], pip[3], pip[4])
            if x == 8 and y > 0 and y < 8:
                pipName = "PIP_SW_RIGHT"+str(y-1)+"_"
                for pip in SWITCH_RIGHT_PIP:
                    gen.pip(pipName+pip[2], pip[3], pip[4])
            if y == 8 and x > 0 and x < 8:
                pipName = "PIP_SW_BOT"+str(x-1)+"_"
                for pip in SWITCH_BOT_PIP:
                    gen.pip(pipName+pip[2], pip[3], pip[4])

            if x == 0 and y == 0:
                pipName = "PIP_TOP_LEFT_"
                for pip in TOP_LEFT_CORNER_PIP:
                    gen.pip(pipName+pip[2], pip[3], pip[4])
                pipName = "PIP_GLOBALIN_"
                for pip in GLOBALIN_PIP:
                    gen.pip(pipName+pip[2], pip[3], "global_", True)
            if x == 8 and y == 0:
                pipName = "PIP_TOP_RIGHT_"
                for pip in TOP_RIGHT_CORNER_PIP:
                    gen.pip(pipName+pip[2], pip[3], pip[4])
                pipName = "PIP_IOB_P61_"
                for pip in IOB_P61_PIP:
                    if ("iob" in pip[3] and "_right" in pip[3]) or ("iob" in pip[4] and "_right" in pip[4]):
                        continue
                    gen.pip(pipName+pip[2], pip[3], pip[4], True)
            if x == 8 and y == 8:
                pipName = "PIP_BOT_RIGHT_"
                for pip in BOT_RIGHT_CORNER_PIP:
                    gen.pip(pipName+pip[2], pip[3], pip[4])
                pipName = "PIP_IOB_P43_"
                for pip in IOB_P43_PIP:
                    if ("iob" in pip[3] and "_right" in pip[3]) or ("iob" in pip[4] and "_right" in pip[4]):
                        continue
                    gen.pip(pipName+pip[2], pip[3], pip[4], True)
                pipName = "PIP_ALTIN_"
                for pip in ALTIN_PIP:
                    gen.pip(pipName+pip[2], pip[3], "alt", True)
            if x == 0 and y == 8:
                pipName = "PIP_IOB_P27_"
                for pip in IOB_P27_PIP:
                    gen.pip(pipName+pip[2], pip[3], pip[4], True)
                pipName = "PIP_BOT_LEFT_"
                for pip in BOT_LEFT_CORNER_PIP:
                    gen.pip(pipName+pip[2], pip[3], pip[4])

            gen.end()
    top.write("endmodule\n")
    top.close()

    print("CLBs: "+str(gen.numCLBs))
    print("Switches: "+str(gen.numSwitches))
    print("IOBs: "+str(gen.numIOBs))
    print("PIPs: "+str(gen.numPIPs))
