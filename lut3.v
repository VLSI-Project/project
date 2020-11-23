`timescale 1ns / 1ps

module lut3(

   input shift_clk, 
   input shift_en, 
   input shift_i, 
   output shift_o, 
   
   input a, 
   input b, 
   input c, 
   output reg y); 
   
   //assign the output based on the select lines 
   always @(posedge shift_clk) begin 
   
   if (shift_en) begin //if shift is enabled, assign the output 
   case(a & b & c)
   
   3'b000: y = shift_i; 
   3'b001: y = shift_i;
   3'b010: y = shift_i;
   3'b011: y = shift_i;
   3'b100: y = shift_i;
   3'b101: y = shift_i;
   3'b110: y = shift_i;
   3'b111: y = shift_i;
   
   default: y = 0; 
   endcase 
   
   end 
   else begin 
   
      y = 0; 
   end 
   
   
   end 
   
   
endmodule 
