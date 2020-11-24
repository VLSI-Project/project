`timescale 1ns/1ps

module test_lut3();

  reg shift_clk;
  reg shift_en;
  reg shift_i;
  reg a;
  reg b;
  reg c;
  wire shift_o;
  wire y;
  lut3 lut3(
    .shift_clk(shift_clk),
    .shift_en(shift_en),
    .shift_i(shift_i),
    .shift_o(shift_o),

    .a(a),
    .b(b),
    .c(c),
    .y(y));

  task shift_bit(
    input val);
    begin
      shift_i = val;
      #5;
      shift_clk = 1;
      #5;
      shift_clk = 0;
    end
  endtask

  task shift_bits(
    input [7:0] val);
    integer i;
    begin
      shift_en = 1;
      for(i = 7; i >= 0; i=i-1)
        shift_bit(val[i]);
      shift_en = 0;
    end
  endtask

  task test(
    input [7:0] val);
    integer i;
    begin
      shift_bits(val);
      #5;
      for(i = 0; i < 8; i=i+1) begin
        {a,b,c} = i;
        #5;
        if(y != val[i]) begin
          $display("Test failed: bits=%8b, abc=%3b, y=%b (expected y=%b)", val, i, y, val[i]);
          $finish;
        end
      end
    end
  endtask

  initial begin
    $dumpfile("test_lut3.vcd");
    $dumpvars;

    test(8'b10000000); // AND
    test(8'b01111111); // NAND

    test(8'b11111110); // OR
    test(8'b00000001); // NOR

    test(8'b10101010); // XOR
    test(8'b01010101); // XNOR

    test(8'b11101010); // Y = AB + C

    $display("Test passed!");
    $finish;
  end

endmodule
