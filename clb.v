`timescale 1ns/1ps
`include "defs.v"
`default_nettype none

/* CONFIG SHIFT REGISTER ORDER
 *shift_i -> Comb.LUT Muxes -> CLB Muxes -> Flop -> LUT0 -> LUT1 -> shift_o 
 */

// configurable logic block
module clb(
  input  shift_clk,
  input  shift_i,
  output shift_o,

  input  a,
  input  b,
  input  c,
  input  d,
  input  k,
  output x,
  output y);

  // CLB signals
  wire flop_to_lut0, lut0_to_lut1;
  wire d_comb;
  wire q;

  // connections for shift register
  reg[`CLB_CONFIG_LEN-1:0] shift_reg;
  reg shift_reg_out; // Connects to first submodule (flop)
  reg init;

  initial begin
    shift_reg = `CLB_CONFIG_LEN'bZ;
  end

  always @(posedge shift_clk) begin
    shift_reg_out = shift_reg[`CLB_CONFIG_LEN-1];
    shift_reg = ((shift_reg << 1) | shift_i);       
  end


  // Mux for D and Q 
  mux2 dq_mux(
    .sel(shift_reg[0]),
    .a(d),
    .b(q),
    .mux_out(d_comb)); 


  // LUTs
  wire lut0_a, lut0_b, lut0_c, l0_f;
  lut3 lut0(
    .shift_clk(shift_clk),
    .shift_i(flop_to_lut0),
    .shift_o(lut0_to_lut1),

    .a(lut0_a),
    .b(lut0_b),
    .c(lut0_c),
    .y(l0_f));

  // logic to generate lut0_a/b/c
  mux2 lut0_a_mux(
    .sel(shift_reg[1]),
    .a(a),
    .b(b),
    .mux_out(lut0_a)); 

  mux2 lut0_b_mux(
    .sel(shift_reg[2]),
    .a(b),
    .b(c),
    .mux_out(lut0_b)); 

  mux2 lut0_c_mux(
    .sel(shift_reg[3]),
    .a(c),
    .b(d_comb),
    .mux_out(lut0_c));
  //

  wire lut1_a, lut1_b, lut1_c, l1_g;
  lut3 lut1(
    .shift_clk(shift_clk),
    .shift_i(lut0_to_lut1),
    .shift_o(shift_o),

    .a(lut1_a),
    .b(lut1_b),
    .c(lut1_c),
    .y(l1_g));  

  // logic to generate lut1_a/b/c
  // Input Muxes
  mux2 lut1_a_mux(
    .sel(shift_reg[4]),
    .a(a),
    .b(b),
    .mux_out(lut1_a)); 

  mux2 lut1_b_mux(
    .sel(shift_reg[5]),
    .a(b),
    .b(c),
    .mux_out(lut1_b)); 

  mux2 lut1_c_mux(
    .sel(shift_reg[6]),
    .a(c),
    .b(d_comb),
    .mux_out(lut1_c));
  
  wire dynamic_out, f, g;
  // Output muxes: F and G muxes share select line
  mux2 dynamic_b_mux(
    .sel(b),
    .a(l0_f),
    .b(l1_g),
    .mux_out(dynamic_out)); 

  mux2 f_mux(
    .sel(shift_reg[7]),
    .a(l0_f),
    .b(dynamic_out),
    .mux_out(f));
 
  mux2 g_mux(
    .sel(shift_reg[7]),
    .a(l1_g),
    .b(dynamic_out),
    .mux_out(g)); 
  //


  wire clk_s1_out, flop_clk, flop_set, flop_rst;
  flop flop(
    .shift_clk(shift_clk),
    .shift_i(shift_reg_out),
    .shift_o(flop_to_lut0),

    .flop_clk(flop_clk),
    .set(flop_set),
    .rst(flop_rst),
 
    .d(f),
    .q(q));

  // logic to generate flop_clk/set/rst
  mux3 clk_mux_s1(
    .sel(shift_reg[9:8]),
    .a(g),
    .b(c),
    .c(k),
    .mux_out(clk_s1_out));  
 
  mux3 clk_mux_s2(
    .sel(shift_reg[11:10]),
    .a(!clk_s1_out),
    .b(clk_s1_out),
    .c(1'b0),
    .mux_out(flop_clk));  

  mux3 set_mux(
    .sel(shift_reg[13:12]),
    .a(a),
    .b(f),
    .c(1'b0),
    .mux_out(flop_set));

  mux3 rst_mux(
    .sel(shift_reg[15:14]),
    .a(d),
    .b(g),
    .c(1'b0),
    .mux_out(flop_rst));

  // logic to generate x/y 
  mux3 x_mux(
    .sel(shift_reg[17:16]),
    .a(f),
    .b(g),
    .c(q),
    .mux_out(x));

  mux3 y_mux(
    .sel(shift_reg[19:18]),
    .a(q),
    .b(g),
    .c(f),
    .mux_out(y));

endmodule
