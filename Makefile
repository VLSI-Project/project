SRCS := $(wildcard *.v)

TOP := test_lut3

.PHONY: all run clean

all: simv

simv: $(SRCS)
	vcs -full64 -top $(TOP) $(SRCS)

run: simv
	./simv -q

clean:
	@rm -rf simv ucli.key simv.daidir/ csrc/ *.vcd
