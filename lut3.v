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
   
   reg [7:0] store; //create a store register to hold the shifted inputs 
   integer i; 
   reg [2:0] sel; 
   
   //store the values in the register
   always @(*) begin 
   

   sel [2:0] = {a,b,c}; //for the case statement later 
   
   if(shift_en) begin   //if the shift is enabled 
     
     //store each bit, only getting the first bit 
     store[7] = store[6];
     store[6] = store[5];
     store[5] = store[4];
     store[4] = store[3];
     store[3] = store[2];
     store[2] = store[1];
     store[1] = store[0];
     store[0] = shift_i; 
    
     shift_o = store[7];
      
   end   
   
   case(sel)   //implement a 8:1 mux to get the output 
   
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
   
   end 
   
   

   
   
endmodule