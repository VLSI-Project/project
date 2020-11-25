`timescale 1ns/1ps

// 2-input MUX
module mux2(
  input sel,
  input a,
  input b,
  output reg mux_out   
);

  always @(*) begin
    case (sel)
      1'b0: mux_out = a;
      1'b1: mux_out = b;
    endcase
  end

endmodule
