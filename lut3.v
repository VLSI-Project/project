`timescale 1ns / 1ps

module lut3(

   input shift_clk, 
   input shift_en, 
   input shift_i, 
   output reg shift_o, 
   
   input a, 
   input b, 
   input c, 
   output reg y); 
   
   reg [7:0] store; 
   integer i; 
   //assign the output based on the select lines 
   always @(posedge shift_clk) begin 
   
   if (shift_en) begin //if shift is enabled
   
   
   for (i = 0; i < 8; i = i + 1) begin  //assign store to shift_i
   
      store[i] = shift_i;
      
   end
   
   case(a & b & c)   //implement a 8:1 mux to get the output 
   
      3'b000: y = store[0]; 
      3'b001: y = store[1];
      3'b010: y = store[2];
      3'b011: y = store[3];
      3'b100: y = store[4];
      3'b101: y = store[5];
      3'b110: y = store[6];
      3'b111: y = store[7];
   
   default: y = 1'bx; 
   endcase 
  
   end //end for if clause 
   else begin 
   
      y = 0; 
   end //else 
   
   
   end //always block
   
   
endmodule 
