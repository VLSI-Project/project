`timescale 1ns/1ps

// programmable input/output buffer (connects to external pin)
module iob(
  input  shift_clk,
  input  shift_en,
  input  shift_i,
  output shift_o,

  input  io_clk,
  input  in,
  input  out_en,
  output out,

  inout  pin);

  // logic

endmodule
