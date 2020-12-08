SRCS := $(wildcard *.v) $(wildcard rtl/*.v)

TOP := test_top

SIM := iverilog
ifeq ($(SIM),vcs)
TARGET := simv
BUILDCMD := vcs -full64 -top $(TOP)
RUNCMD := ./$(TARGET) -q
else ifeq ($(SIM),iverilog)
TARGET := $(TOP)
BUILDCMD := iverilog -Wall -o $(TARGET) -s $(TOP)
RUNCMD := ./$(TARGET)
endif

.PHONY: all run clean

all: $(TARGET)

$(TARGET): $(SRCS)
	$(BUILDCMD) $(SRCS)

run: $(TARGET)
	$(RUNCMD)

clean:
	@rm -rf $(TARGET) ucli.key simv.daidir/ csrc/ *.vcd
