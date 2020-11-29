`timescale 1ns/1ps

// neg or pos edge D flip-flop or latch with async set/reset
module flop(
  input  shift_clk,
  input  shift_i,
  output shift_o,

  input  flop_clk,
  input  set,
  input  rst,

  input  d,
  output q);

  reg disable_ff;
  wire prim_p, prim_q;
  wire sec_p;

  /* TODO: Fix reset during configuration! */
  latch primary_latch(
      .latch_level(flop_clk),
      .set(set),
      .rst(rst),
      .d(d),
      .q_latch(prim_q),
      .p_latch(prim_p)
  );

  latch secondary_latch(
      .latch_level(flop_clk),
      .set(set),
      .rst(rst),
      .d(prim_p),
      .q_latch(q),
      .p_latch(sec_p)
  );

  assign shift_o = shift_i;
endmodule
