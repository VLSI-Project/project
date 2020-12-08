`timescale 1ns/1ps

module test_top();

  reg        shift_clk;
  reg        shift_en;
  reg        shift_i;
  wire       shift_o;
  tri [15:0] iob_pin_top;
  tri [15:0] iob_pin_right;
  tri [15:0] iob_pin_bot;
  tri [15:0] iob_pin_left;
  top top(
    .shift_clk(shift_clk),
    .shift_en(shift_en),
    .shift_i(shift_i),
    .shift_o(shift_o),
    .iob_pin_top(iob_pin_top),
    .iob_pin_right(iob_pin_right),
    .iob_pin_bot(iob_pin_bot),
    .iob_pin_left(iob_pin_left));

  reg        cnt_clk;
  reg        cnt_clr;
  reg        cnt_ci;
  wire [7:0] cnt_val;
  wire       cnt_co;
  assign iob_pin_top[0] = cnt_clk;
  assign iob_pin_top[2] = cnt_clr;
  assign iob_pin_left[2] = cnt_ci;
  assign cnt_val[0] = iob_pin_top[1];
  assign cnt_val[1] = iob_pin_top[3];
  assign cnt_val[2] = iob_pin_top[5];
  assign cnt_val[3] = iob_pin_top[7];
  assign cnt_val[4] = iob_pin_top[9];
  assign cnt_val[5] = iob_pin_top[11];
  assign cnt_val[6] = iob_pin_top[13];
  assign cnt_val[7] = iob_pin_top[15];
  assign cnt_co = iob_pin_right[2];

  task shift_bit(
    input value);
    begin
      shift_i = value;
      #5;
      shift_clk = 1;
      #5;
      shift_clk = 0;
    end
  endtask

  task clk_times(
    input integer times);
    integer i;
    begin
      $display("Clock %0d times", times);
      for(i = 0; i < times; i=i+1) begin
        $display("%0d", i);
        #5;
        cnt_clk = 1;
        #5;
        cnt_clk = 0;
      end
    end
  endtask

  task check_cnt(
    input [7:0] val_exp,
    input co_exp);
    begin
      if(cnt_val !== val_exp || cnt_co !== co_exp) begin
        $display("Test failed: val=%0d, co=%b (expected val=%0d, co=%b)", cnt_val, cnt_co, val_exp, co_exp);
        $finish;
      end
    end
  endtask

  integer fd;
  integer i;
  reg [8:0] char;
  initial begin
    $dumpfile("test_top.vcd");
    $dumpvars;

    shift_clk = 0;
    shift_en = 0;
    shift_i = 0;
    cnt_clk = 0;
    cnt_clr = 0;
    cnt_ci = 0;

    $display("Loading bitstream");
    shift_en = 1;
    fd = $fopen("counter_bits.txt", "r");
    char = $fgetc(fd);
    for(i = 0; char != 9'h1ff; i=i+1) begin
      if((i % 100) == 0)
        $display("%0d", i);
      shift_bit(char != "0");
      char = $fgetc(fd);
    end
    $fclose(fd);
    shift_en = 0;
    $display("Configuration complete");
    #100;

    clk_times(10);
    check_cnt(0, 0);

    cnt_ci = 1;
    clk_times(100);
    check_cnt(100, 0);

    cnt_ci = 0;
    clk_times(100);
    check_cnt(100, 0);

    cnt_ci = 1;
    clk_times(154);
    check_cnt(254, 0);

    clk_times(1);
    check_cnt(255, 1);
    cnt_ci = 0;
    #10;
    check_cnt(255, 0);
    cnt_ci = 1;

    clk_times(10);
    check_cnt(9, 0);

    cnt_clr = 1;
    clk_times(1);
    check_cnt(0, 0);

    clk_times(10);
    check_cnt(0, 0);

    $display("All tests passed.");
    $finish;
  end

endmodule
