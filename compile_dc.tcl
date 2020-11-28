analyze -format verilog switch.v
read_verilog -rtl [list [glob rtl/*.v] clb.v iob.v lut3.v pip.v pip_uni.v]
current_design top
link
uniquify
check_design

set_disable_timing gscl45nm/TBUFX1
set_disable_timing gscl45nm/TBUFX2
compile
write_file -hierarchy -format verilog -output netlist.v top

report_area

quit
