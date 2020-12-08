`timescale 1ns/1ps

module switch #(
  parameter N = 1,
  parameter E = 1,
  parameter S = 1,
  parameter W = 1
  )(
  input  shift_clk,
  input  shift_en,
  input  shift_i,
  output shift_o,

  inout  pin1,
  inout  pin2,
  inout  pin3,
  inout  pin4,
  inout  pin5,
  inout  pin6,
  inout  pin7,
  inout  pin8);

  reg [39:0] data;
  assign shift_o = data[39];
  always @(posedge shift_clk)
    data <= {data[38:0],shift_i};

  // 1_3
  assign pin1 = (data[0] && !shift_en) ? pin3 : 1'bz;
  assign pin3 = (data[1] && !shift_en) ? pin1 : 1'bz;

  // 1_5
  assign pin1 = (data[2] && !shift_en) ? pin5 : 1'bz;
  assign pin5 = (data[3] && !shift_en) ? pin1 : 1'bz;

  // 1_6
  assign pin1 = (data[4] && !shift_en) ? pin6 : 1'bz;
  assign pin6 = (data[5] && !shift_en) ? pin1 : 1'bz;

  // 1_7
  assign pin1 = (data[6] && !shift_en) ? pin7 : 1'bz;
  assign pin7 = (data[7] && !shift_en) ? pin1 : 1'bz;

  // 1_8
  assign pin1 = (data[6] && !shift_en) ? pin8 : 1'bz;
  assign pin8 = (data[7] && !shift_en) ? pin1 : 1'bz;

  // 2_3
  assign pin2 = (data[8] && !shift_en) ? pin3 : 1'bz;
  assign pin3 = (data[9] && !shift_en) ? pin2 : 1'bz;

  // 2_4
  assign pin2 = (data[10] && !shift_en) ? pin4 : 1'bz;
  assign pin4 = (data[11] && !shift_en) ? pin2 : 1'bz;

  // 2_5
  assign pin2 = (data[12] && !shift_en) ? pin5 : 1'bz;
  assign pin5 = (data[13] && !shift_en) ? pin2 : 1'bz;

  // 2_6
  assign pin2 = (data[14] && !shift_en) ? pin6 : 1'bz;
  assign pin6 = (data[15] && !shift_en) ? pin2 : 1'bz;

  // 2_8
  assign pin2 = (data[16] && !shift_en) ? pin8 : 1'bz;
  assign pin8 = (data[17] && !shift_en) ? pin2 : 1'bz;

  // 3_5
  assign pin3 = (data[18] && !shift_en) ? pin5 : 1'bz;
  assign pin5 = (data[19] && !shift_en) ? pin3 : 1'bz;

  // 3_7
  assign pin3 = (data[20] && !shift_en) ? pin7 : 1'bz;
  assign pin7 = (data[21] && !shift_en) ? pin3 : 1'bz;

  // 3_8
  assign pin3 = (data[22] && !shift_en) ? pin8 : 1'bz;
  assign pin8 = (data[23] && !shift_en) ? pin3 : 1'bz;

  // 4_5
  assign pin4 = (data[24] && !shift_en) ? pin5 : 1'bz;
  assign pin5 = (data[25] && !shift_en) ? pin4 : 1'bz;

  // 4_6
  assign pin4 = (data[26] && !shift_en) ? pin6 : 1'bz;
  assign pin6 = (data[27] && !shift_en) ? pin4 : 1'bz;

  // 4_7
  assign pin4 = (data[28] && !shift_en) ? pin7 : 1'bz;
  assign pin7 = (data[29] && !shift_en) ? pin4 : 1'bz;

  // 4_8
  assign pin4 = (data[30] && !shift_en) ? pin8 : 1'bz;
  assign pin8 = (data[31] && !shift_en) ? pin4 : 1'bz;

  // 5_7
  assign pin5 = (data[32] && !shift_en) ? pin7 : 1'bz;
  assign pin7 = (data[33] && !shift_en) ? pin5 : 1'bz;

  // 6_7
  assign pin6 = (data[34] && !shift_en) ? pin7 : 1'bz;
  assign pin7 = (data[35] && !shift_en) ? pin6 : 1'bz;

  // 6_8
  assign pin6 = (data[36] && !shift_en) ? pin8 : 1'bz;
  assign pin8 = (data[37] && !shift_en) ? pin6 : 1'bz;

endmodule
