`timescale 1ns/1ps

// field-programmable gate array
module fpga(
  // XC2064 has 68 pins
  inout [67:0] pins);

  // 8 x 8 CLB grid
  genvar x, y;
  generate
    for(y = 0; y < 8; y=y+1) begin : clby
      for(x = 0; x < 8; x=x+1) begin : clbx
        intercon_clb clb(
          .shift_clk(),
          .shift_i(),
          .shift_o(),

          .gen_row_top(),
          .gen_row_bot(),
          .gen_col_left(),
          .gen_col_right(),

          .long_row_top(),
          .long_row_bot(),
          .long_col_left(),
          .long_col_right(),

          .global_col_left(),

          .direct_x_top(),
          .direct_x_bot(),
          .direct_y_left(),
          .x(),
          .y());
      end
    end
  endgenerate

  // 9 x 9 interconnect grid
  generate
    for(y = 0; y < 9; y=y+1) begin : switchy
      for(x = 0; x < 9; x=x+1) begin : switchx
        intercon_switch switch(
          .shift_clk(),
          .shift_en(),
          .shift_i(),
          .shift_o(),

          .gen_row_left(),
          .gen_row_right(),
          .gen_col_above(),
          .gen_col_below(),

          .long_row(),
          .long_col(),

          .global_col());
      end
    end
  endgenerate

  // XC2064 has 58 IOBs
  genvar i;
  generate
    for(i = 0; i < 58; i=i+1) begin : iobs
      iob iob(
        .shift_clk(),
        .shift_en(),
        .shift_i(),
        .shift_o(),

        .io_clk(),
        .in(),
        .out_en(),
        .out(),

        .pin());
    end
  endgenerate

endmodule
