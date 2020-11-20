`timescale 1ns/1ps

// programmable row/column switch for general purpose interconnect
module intercon_crossbar(
  input  shift_clk,
  input  shift_en,
  input  shift_i,
  output shift_o,

  inout  pin1,
  inout  pin2,
  inout  pin3,
  inout  pin4,
  inout  pin5,
  inout  pin6,
  inout  pin7,
  inout  pin8);

  // Valid connections (20 total):
  // 1 <-> {3,5,6,7,8}
  // 2 <-> {3,4,5,6,8}
  // 3 <-> {5,7,8}
  // 4 <-> {5,6,7,8}
  // 5 <-> 7
  // 6 <-> {7,8}

endmodule
