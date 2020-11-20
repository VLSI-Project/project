`timescale 1ns/1ps

// programmable input/output connections for a clb
module intercon_clb(
  input       shift_clk,
  input       shift_en,
  input       shift_i,
  output      shift_o,

  // general purpose interconnect
  inout [3:0] gen_row_top,
  inout [3:0] gen_row_bot,
  inout [4:0] gen_col_left,
  inout [4:0] gen_col_right,

  // long line interconnect
  inout       long_row_top,
  inout       long_row_bot,
  inout [1:0] long_col_left,
  inout [1:0] long_col_right,

  // global interconnect
  inout       global_col_left,

  // direct interconnect
  input       direct_x_top,
  input       direct_x_bot,
  input       direct_y_left,
  output      x,
  output      y);

  wire a, b, c, d, k;
  clb clb(
    .shift_clk(shift_clk),
    .shift_en(shift_en),
    .shift_i(),
    .shift_o(),

    .a(a),
    .b(b),
    .c(c),
    .d(d),
    .k(k),
    .x(x),
    .y(y));

  // logic to connect clb inputs/outputs to interconnect

endmodule
