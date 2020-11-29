`include "defs.v"
`default_nettype none

module test_clb;
  
  parameter SHIFT_W = `CLB_CONFIG_LEN + 2*(`LUT_CONFIG_LEN);
  reg shift_i, shift_clk;
  reg a, b, c, d, k;
  wire x, y, shift_o;

  clb clb1(
      .shift_clk(shift_clk),
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
      for(i = 0; i < SHIFT_W; i=i+1)
        shift_bit(val[i]);
    end
  endtask

  // 3 buffer bits to check shift_o
  task test(
    input [SHIFT_W-1:0] val,
    input [15:0] x_expected,
    input [15:0] y_expected);
    integer i;
    begin
      k = 1'b0;
      shift_bits(val);
      #5;
      for(i = 15; i >=0; i=i-1) begin
        {a,b,c,d} = i;
        #5;
        if(x !== x_expected[i] || y !== y_expected[i]) begin
          $display("Test failed: bits=%36b, abcd=%4b, y=%b (expected y=%b), x=%b (expected x=%b)", val, i, y, y_expected[i], x, x_expected[i]);
          $finish;
        end 
        else begin
          $display("Test passed! abcd=%4b, x=%b, y=%b", i, x, y);
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
    test({1'b0, 3'b000, 3'b111, 1'b0, 8'b00000000, 2'b00, 2'b10, `AND3_CFG, `XOR3_CFG},
        {16'b1100000000000000},
        {`XOR3_REV_CFG, `XOR3_REV_CFG});
    
    /* Dynamic selection, 4-var test:
     * MAJ(A,B,C,D) on x,y : 1 if at least 2 1's asserted
     */ 
    test({1'b0, 3'b011, 3'b011, 1'b1, 8'b00000000, 2'b10, 2'b01, `MAJ3_CFG, `MAJ3_CFG_B},
        {16'b1111111011101000},
        {16'b1111111011101000});
    
    $display("All tests passed!");
    $finish;
  end

endmodule

