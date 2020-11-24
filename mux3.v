`timescale 1ns/1ps

// 3-input MUX
module mux3(
  input[1:0] sel,
  input a,
  input b,
  input c,
  output reg mux_out   
);

  always @(*) begin
    case (sel)
      2'b00: mux_out = a;
      2'b01: mux_out = b;
      2'b10: mux_out = c;
      default: mux_out = 1'bZ;  
    endcase
  end

endmodule
