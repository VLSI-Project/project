`timescale 1ns/1ps

// neg or pos edge D flip-flop or latch with async set/reset
module flop(
  input  shift_clk,
  input  shift_en,

  input  flop_clk,
  input  set,
  input  rst,

  input  d,
  output latch_q,
  output ff_q);

  latch primary_latch(
      .latch_level(!flop_clk & !shift_en),
      .set(set),
      .rst(rst | shift_en),
      .d(d),
      .q_latch(),
      .p_latch(latch_q)
  );

  latch secondary_latch(
      .latch_level(flop_clk & !shift_en),
      .set(set),
      .rst(rst | shift_en),
      .d(latch_q),
      .q_latch(ff_q),
      .p_latch()
  );

endmodule
