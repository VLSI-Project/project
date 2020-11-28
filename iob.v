`timescale 1ns/1ps

// programmable input/output buffer (connects to external pin)
module iob(
  input  shift_clk,
  input  shift_i,
  output shift_o,

  input  io_clk,

  input  ts,
  output in,
  input  out,

  inout  pin);

  reg pin_r;
  always @(posedge io_clk)
    pin_r <= pin;

  reg [2:0] data;
  assign shift_o = data[2];
  always @(posedge shift_clk)
    data <= {data[1:0],shift_i};

  assign in = data[0] ? pin_r : pin;
  assign pin = data[1] ? (ts ? out : 1'bz) : (data[2] ? out : 1'bz);

endmodule
