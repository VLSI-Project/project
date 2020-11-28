`timescale 1ns/1ps

module pip(
  input  shift_clk,
  input  shift_i,
  output shift_o,

  inout  a,
  inout  b);

  reg [1:0] data;
  assign shift_o = data[1];
  always @(posedge shift_clk)
    data <= {data[0],shift_i};

  assign a = data[0] ? b : 1'bz;
  assign b = data[1] ? a : 1'bz;

endmodule
