`timescale 1ns/1ps

module pip_uni(
  input  shift_clk,
  input  shift_en,
  input  shift_i,
  output shift_o,

  input  a,
  output b);

  reg data;
  assign shift_o = data;
  always @(posedge shift_clk)
    data <= shift_i;

  assign b = (data && !shift_en) ? a : 1'bz;

endmodule
