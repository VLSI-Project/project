`timescale 1ns/1ps

// programmable row/column switch for all interconnect
module intercon_switch(
  input       shift_clk,
  input       shift_en,
  input       shift_i,
  output      shift_o,

  // general purpose interconnect
  inout [3:0] gen_row_left,
  inout [3:0] gen_row_right,
  inout [4:0] gen_col_above,
  inout [4:0] gen_col_below,

  // long line interconnect
  inout       long_row,
  inout [1:0] long_col,

  // global interconnect
  inout       global_col);

  intercon_crossbar crossbar0(
    .shift_clk(shift_clk),
    .shift_en(shift_en),
    .shift_i(),
    .shift_o(),

    .pin1(gen_col_above[0]),
    .pin2(gen_col_above[1]),
    .pin3(gen_row_right[3]),
    .pin4(gen_row_right[2]),
    .pin5(gen_col_below[1]),
    .pin6(gen_col_below[0]),
    .pin7(gen_row_left[2]),
    .pin8(gen_row_left[3]));

  intercon_crossbar crossbar1(
    .shift_clk(shift_clk),
    .shift_en(shift_en),
    .shift_i(),
    .shift_o(),

    .pin1(gen_col_above[2]),
    .pin2(gen_col_above[3]),
    .pin3(gen_row_right[1]),
    .pin4(gen_row_right[0]),
    .pin5(gen_col_below[3]),
    .pin6(gen_col_below[2]),
    .pin7(gen_row_left[0]),
    .pin8(gen_row_left[1]));

  // logic for other connections

endmodule
