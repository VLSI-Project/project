`timescale 1ns/1ps
`include "defs.v"

module test_clb;
  
  parameter SHIFT_W = `CLB_CONFIG_LEN + 2*(`LUT_CONFIG_LEN);
  reg shift_i, shift_clk, shift_en;
  reg a, b, c, d, k;
  wire x, y, shift_o;

  clb clb1(
      .shift_clk(shift_clk),
      .shift_en(shift_en),
      .shift_i(shift_i),
      .shift_o(shift_o),
      .a(a),
      .b(b),
      .c(c),
      .d(d),
      .k(k),
      .x(x),
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
    input [SHIFT_W-1:0] val);
    integer i;
    begin
      shift_en = 1;
      for(i = 0; i < SHIFT_W; i=i+1)
        shift_bit(val[i]);
      shift_en = 0;
    end
  endtask


  always #5 k = ~k;
  // 3 buffer bits to check shift_o
  task test(
    input [SHIFT_W-1:0] val,
    input [15:0] x_expected,
    input [15:0] y_expected,
    input seq);
    integer i;
    begin
      shift_bits(val);
      #5;
      // Set Flip-Flop
      a = 1'b1;
      k = 1'b0;
      @(posedge k); 
      for(i = 0; i < 16; i=i+1) begin
        {a,b,c,d} = i;
        #10;
        if((x !== x_expected[i] || y !== y_expected[i]) && !seq) begin
          $display("Test failed: bits=%38b, abcd=%4b, y=%b (expected y=%b), x=%b (expected x=%b)", val, {a,b,c,d}, y, y_expected[i], x, x_expected[i]);
          //$finish;
        end 
        else begin
          $display("Test passed! abcd=%4b, x=%b, y=%b", {a,b,c,d}, x, y);
        end
      end
    end
  endtask


  initial begin
    $dumpfile("test_clb.vcd");
    $dumpvars;

    /* Two 3-var test:
     *  AND(A,B,C) on 'x' and XOR(B C D) on 'y' 
     *  */
    $display("XOR/AND test:");
    test({4'b0000, 4'b1110, 1'b0, 9'b000000000, 2'b00, 2'b10, `AND3_CFG, `XOR3_CFG},
        {16'b1100000000000000},
        {`XOR3_REV_CFG, `XOR3_REV_CFG}, 0);
    
    /* Dynamic selection, 4-var test:
     * MAJ(A,B,C,D) on x,y : 1 if at least 2 1's asserted
     */ 
    $display("\nMAJ4 test");
    #100
    test({4'b0110, 4'b0110, 1'b1, 9'b000000000, 2'b10, 2'b01, `MAJ3_CFG, `MAJ3_CFG_B},
        {16'b1111111011101000},
        {16'b1111111011101000}, 0);

    /* X = G
     * Y = Q
     * F = B ^ C ^ Q
     * G = 1 AND B AND Q
     * A set: Q starts at 1
    */ 
    $display("\nSequential test");
    #100
    test({4'b1101, 4'b0001, 1'b0, 9'b010110000, 2'b10, 2'b00, 8'b01101001, 8'b00010001},
        {16'b1111000011010000},
        {16'b1111111111010111}, 0);
    
    
    $display("All tests passed!");
    $finish;
  end

endmodule

