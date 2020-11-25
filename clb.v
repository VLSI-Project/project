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

  // connections for shift register
  reg[9:0] shift_reg;

  wire lut0_a, lut0_b, lut0_c, l0_f, l1_g;
  lut3 lut0(
    .shift_clk(shift_clk),
    .shift_en(shift_en),
    .shift_i(),
    .shift_o(),

    .a(lut0_a),
    .b(lut0_b),
    .c(lut0_c),
    .y(l0_f));

  // logic to generate lut0_a/b/c
  mux2 lut0_a_mux(
    .sel(),
    .a(a),
    .b(b),
    .mux_out(lut0_a)); 

  mux2 lut0_b_mux(
    .sel(),
    .a(b),
    .b(c),
    .mux_out(lut0_b)); 

  mux3 lut0_c_mux(
    .sel(),
    .a(c),
    .b(d),
    .c(q),
    .mux_out(lut0_c));
  //

  wire lut1_a, lut1_b, lut1_c, l1_g;
  lut3 lut1(
    .shift_clk(shift_clk),
    .shift_en(shift_en),
    .shift_i(),
    .shift_o(),

    .a(lut1_a),
    .b(lut1_b),
    .c(lut1_c),
    .y(l1_g));  

  // logic to generate lut1_a/b/c
  // Input Muxes
  mux2 lut1_a_mux(
    .sel(),
    .a(a),
    .b(b),
    .mux_out(lut1_a)); 

  mux2 lut1_b_mux(
    .sel(),
    .a(b),
    .b(c),
    .mux_out(lut1_b)); 

  mux3 lut1_c_mux(
    .sel(),
    .a(c),
    .b(d),
    .c(q),
    .mux_out(lut1_c));
  
  wire dynamic_out, f, g;
  // Output muxes
  mux2 dynamic_b_mux(
    .sel(b),
    .a(l0_f),
    .b(l1_g),
    .mux_out(dynamic_out)); 

  mux2 f_mux(
    .sel(),
    .a(l0_f),
    .b(dynamic_out),
    .mux_out(f));
 
  mux2 lut1_a_mux(
    .sel(),
    .a(l1_g),
    .b(dynamic_out),
    .mux_out(g)); 
  //


  wire clk_s1_out, flop_clk, flop_set, flop_rst, q;
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
  mux3 clk_mux_s1(
    .sel(shift_reg[1:0]),
    .a(g),
    .b(c),
    .c(k),
    .mux_out(clk_s1_out));  
 
  mux3 clk_mux_s2(
    .sel(shift_reg[1:0]),
    .a(!clk_s1_out),
    .b(clk_s1_out),
    .c(0),
    .mux_out(flop_clk));  

  mux3 set_mux(
    .sel(shift_reg[1:0]),
    .a(a),
    .b(f),
    .c(0),
    .mux_out(flop_set));

  mux3 rst_mux(
    .sel(shift_reg[1:0]),
    .a(d),
    .b(g),
    .c(0),
    .mux_out(flop_rst));

  // logic to generate x/y 
  mux3 x_mux(
    .sel(shift_reg[1:0]),
    .a(f),
    .b(g),
    .c(q),
    .mux_out(x));

  mux3 y_mux(
    .sel(shift_reg[1:0]),
    .a(q),
    .b(g),
    .c(f),
    .mux_out(y));

endmodule
