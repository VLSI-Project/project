`timescale 1ns/1ps

module switch #(
  parameter N = 1,
  parameter E = 1,
  parameter S = 1,
  parameter W = 1
  )(
  input  shift_clk,
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
  assign pin1 = data[0] ? pin3 : 1'bz;
  assign pin3 = data[1] ? pin1 : 1'bz;

  // 1_5
  assign pin1 = data[2] ? pin5 : 1'bz;
  assign pin5 = data[3] ? pin1 : 1'bz;

  // 1_6
  assign pin1 = data[4] ? pin6 : 1'bz;
  assign pin6 = data[5] ? pin1 : 1'bz;

  // 1_7
  assign pin1 = data[6] ? pin7 : 1'bz;
  assign pin7 = data[7] ? pin1 : 1'bz;

  // 1_8
  assign pin1 = data[6] ? pin8 : 1'bz;
  assign pin8 = data[7] ? pin1 : 1'bz;

  // 2_3
  assign pin2 = data[8] ? pin3 : 1'bz;
  assign pin3 = data[9] ? pin2 : 1'bz;

  // 2_4
  assign pin2 = data[10] ? pin4 : 1'bz;
  assign pin4 = data[11] ? pin2 : 1'bz;

  // 2_5
  assign pin2 = data[12] ? pin5 : 1'bz;
  assign pin5 = data[13] ? pin2 : 1'bz;

  // 2_6
  assign pin2 = data[14] ? pin6 : 1'bz;
  assign pin6 = data[15] ? pin2 : 1'bz;

  // 2_8
  assign pin2 = data[16] ? pin8 : 1'bz;
  assign pin8 = data[17] ? pin2 : 1'bz;

  // 3_5
  assign pin3 = data[18] ? pin5 : 1'bz;
  assign pin5 = data[19] ? pin3 : 1'bz;

  // 3_7
  assign pin3 = data[20] ? pin7 : 1'bz;
  assign pin7 = data[21] ? pin3 : 1'bz;

  // 3_8
  assign pin3 = data[22] ? pin8 : 1'bz;
  assign pin8 = data[23] ? pin3 : 1'bz;

  // 4_5
  assign pin4 = data[24] ? pin5 : 1'bz;
  assign pin5 = data[25] ? pin4 : 1'bz;

  // 4_6
  assign pin4 = data[26] ? pin6 : 1'bz;
  assign pin6 = data[27] ? pin4 : 1'bz;

  // 4_7
  assign pin4 = data[28] ? pin7 : 1'bz;
  assign pin7 = data[29] ? pin4 : 1'bz;

  // 4_8
  assign pin4 = data[30] ? pin8 : 1'bz;
  assign pin8 = data[31] ? pin4 : 1'bz;

  // 5_7
  assign pin5 = data[32] ? pin7 : 1'bz;
  assign pin7 = data[33] ? pin5 : 1'bz;

  // 6_7
  assign pin6 = data[34] ? pin7 : 1'bz;
  assign pin7 = data[35] ? pin6 : 1'bz;

  // 6_8
  assign pin6 = data[36] ? pin8 : 1'bz;
  assign pin8 = data[37] ? pin6 : 1'bz;

endmodule
