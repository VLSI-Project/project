`timescale 1ns / 1ps

module lut3(

   input shift_clk, 
   input shift_en, 
   input [8:0] bitstream, //passed in a bitstream, each bit will be an output 
   output reg shift_o, 
   
   input a, 
   input b, 
   input c, 
   output reg y); 
   
   integer i; 
   //assign the output based on the select lines 
   always @(posedge shift_clk) begin 
   
   if (shift_en) begin //if shift is enabled, go through bitstream
   
   
   for (i = 0; i < 8; i = i + 1) begin  //go through the bitstream and assign each bit, to shift_o
   
   shift_o = bitstream[i]; 
   
   case(a & b & c)   //implement a 8:1 mux to get the output 
   
   3'b000: y = shift_o; 
   3'b001: y = shift_o;
   3'b010: y = shift_o;
   3'b011: y = shift_o;
   3'b100: y = shift_o;
   3'b101: y = shift_o;
   3'b110: y = shift_o;
   3'b111: y = shift_o;
   
   default: y = 0; 
   endcase 
   
   end //end for loop
   end //end for if clause 
   else begin 
   
      y = 0; 
   end //else 
   
   
   end //always block
   
   
endmodule 
