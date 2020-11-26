`timescale 1ns/1ps
`define CONFIG_LEN 21
`default_nettype none

/* CONFIG SHIFT REGISTER ORDER
 *shift_i -> Comb.LUT Muxes -> CLB Muxes -> Flop -> LUT0 -> LUT1 -> shift_o 
 */

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
  reg[`CONFIG_LEN-1:0] shift_reg;
  reg shift_reg_out; // Connects to first submodule (flop)
  wire flop_to_lut0, lut0_to_lut1;

  always @(posedge shift_clk) begin
    if (shift_en) begin
      shift_reg_out = shift_reg[`CONFIG_LEN-1];
      shift_reg = ((shift_reg << 1) | shift_i);       
    end
  end

  // LUTs

  wire q;
  wire lut0_a, lut0_b, lut0_c, l0_f;
  lut3 lut0(
    .shift_clk(shift_clk),
    .shift_en(shift_en),
    .shift_i(flop_to_lut0),
    .shift_o(lut0_to_lut1),

    .a(lut0_a),
    .b(lut0_b),
    .c(lut0_c),
    .y(l0_f));

  // logic to generate lut0_a/b/c
  mux2 lut0_a_mux(
    .sel(shift_reg[0]),
    .a(a),
    .b(b),
    .mux_out(lut0_a)); 

  mux2 lut0_b_mux(
    .sel(shift_reg[1]),
    .a(b),
    .b(c),
    .mux_out(lut0_b)); 

  mux3 lut0_c_mux(
    .sel(shift_reg[3:2]),
    .a(c),
    .b(d),
    .c(q),
    .mux_out(lut0_c));
  //

  wire lut1_a, lut1_b, lut1_c, l1_g;
  lut3 lut1(
    .shift_clk(shift_clk),
    .shift_en(shift_en),
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

  mux3 lut1_c_mux(
    .sel(shift_reg[7:6]),
    .a(c),
    .b(d),
    .c(q),
    .mux_out(lut1_c));
  
  wire dynamic_out, f, g;
  // Output muxes: F and G muxes share select line
  mux2 dynamic_b_mux(
    .sel(b),
    .a(l0_f),
    .b(l1_g),
    .mux_out(dynamic_out)); 

  mux2 f_mux(
    .sel(shift_reg[8]),
    .a(l0_f),
    .b(dynamic_out),
    .mux_out(f));
 
  mux2 g_mux(
    .sel(shift_reg[8]),
    .a(l1_g),
    .b(dynamic_out),
    .mux_out(g)); 
  //


  wire clk_s1_out, flop_clk, flop_set, flop_rst;
  flop flop(
    .shift_clk(shift_clk),
    .shift_en(shift_en),
    .shift_i(shift_reg_out),
    .shift_o(flop_to_lut0),

    .flop_clk(flop_clk),
    .set(flop_set),
    .rst(flop_rst),
 
    .d(f),
    .q(q));

  // logic to generate flop_clk/set/rst
  mux3 clk_mux_s1(
    .sel(shift_reg[10:9]),
    .a(g),
    .b(c),
    .c(k),
    .mux_out(clk_s1_out));  
 
  mux3 clk_mux_s2(
    .sel(shift_reg[12:11]),
    .a(!clk_s1_out),
    .b(clk_s1_out),
    .c(0),
    .mux_out(flop_clk));  

  mux3 set_mux(
    .sel(shift_reg[14:13]),
    .a(a),
    .b(f),
    .c(0),
    .mux_out(flop_set));

  mux3 rst_mux(
    .sel(shift_reg[16:15]),
    .a(d),
    .b(g),
    .c(0),
    .mux_out(flop_rst));

  // logic to generate x/y 
  mux3 x_mux(
    .sel(shift_reg[18:17]),
    .a(f),
    .b(g),
    .c(q),
    .mux_out(x));

  mux3 y_mux(
    .sel(shift_reg[20:19]),
    .a(q),
    .b(g),
    .c(f),
    .mux_out(y));

endmodule
