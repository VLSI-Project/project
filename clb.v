`timescale 1ns/1ps

// configurable logic block
module clb(
  input  shift_clk,
  input  shift_en,
  input  shift_i,
  output shift_o,

  input  a,
  input  b,
  input  c,
  input  d,
  input  k,
  output x,
  output y);

  wire lut0_a, lut0_b, lut0_c, f;
  lut3 lut0(
    .shift_clk(shift_clk),
    .shift_en(shift_en),
    .shift_i(),
    .shift_o(),

    .a(lut0_a),
    .b(lut0_b),
    .c(lut0_c),
    .y(f));

  // logic to generate lut0_a/b/c

  wire lut1_a, lut1_b, lut1_c, g;
  lut3 lut0(
    .shift_clk(shift_clk),
    .shift_en(shift_en),
    .shift_i(),
    .shift_o(),

    .a(lut1_a),
    .b(lut1_b),
    .c(lut1_c),
    .y(g));  

  // logic to generate lut1_a/b/c

  wire flop_clk, flop_set, flop_rst, q;
  flop flop(
    .shift_clk(shift_clk),
    .shift_en(shift_en),
    .shift_i(),
    .shift_o(),

    .flop_clk(flop_clk),
    .set(flop_set),
    .rst(flop_rst),
 
    .d(f),
    .q(q));

  // logic to generate flop_clk/set/rst

  // logic to generate x/y

  // connections for shift register

endmodule
