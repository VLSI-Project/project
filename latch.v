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

   assign q_latch = (latch_level ? !d : !p_latch);
   assign p_latch = !((q_latch | set) & !rst);

endmodule
