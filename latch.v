`timescale 1ns/1ps

// Latch with async set/reset
module latch(
  input  latch_level,
  input  set,
  input  rst,

  input  d,
  output q_latch,
  output p_latch
   );

   assign #1 q_latch = (latch_level ? p_latch : d);
   assign #1 p_latch = ((q_latch | set) & !rst);

endmodule
