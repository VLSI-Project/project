`timescale 1ns/1ps

// Latch with async set/reset
// Q is the node marked "FF OUT" in the diagram
// P is the node marked "LATCH OUT" in the diagram
module latch(
  input  latch_level,
  input  set,
  input  rst,

  input  d,
  output q_latch,
  output p_latch
   );

   assign #0.1 q_latch = (latch_level ? d : p_latch);
   assign #0.1 p_latch = ((q_latch | set) & !rst);

endmodule
