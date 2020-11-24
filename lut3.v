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
   
   reg [7:0] store; //create a store register to hold the shifted inputs 
   integer i; 
   
   
   //store the values in the register
   always @(posedge shift_clk) begin 
   
   if(shift_en) begin   //if the shift is enabled 
     
     for (i = 0; i < 8;) begin  //go through 8 bits of the store register
   
        if (shift_clk)begin     //at every clock cycle,store the shift_i bits into the register, and increment the count
           store[i] = shift_i; 
           i = i + 1;     //increment the array count only if there is a value stored in it. 
        end 
      end
   
   end 
   
   end 
   
   
   
   //get the output based on the select lines 
   always @(posedge shift_clk) begin
   
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
 
   
   
   end //2nd always block
   
   
endmodule