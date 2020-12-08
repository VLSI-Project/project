#!/usr/bin/env python3

import tkinter as tk
import io
from defines import *
import sys

SCALE = 2

XSPACE = 93.75
YSPACE = 94

class CfgVar(tk.IntVar):
    def __init__(self, name: str, width: int, value: int):
        super().__init__()
        self.name = name
        self.width = width
        self.fmt = "0" + str(width) + "b"
        self.set(value)
    def writeBits(self, bitfile):
        bitfile.write(format(self.get(), self.fmt)[::-1])
    def readBits(self, bitfile):
        self.set(int(bitfile.read(self.width)[::-1], 2))
    def writeCfg(self, prefix: str, cfgfile):
        cfgfile.write("{}{} = {}\n".format(prefix, self.name, format(self.get(), self.fmt)[::-1]))

class Module:
    def __init__(self, name: str, canvas: tk.Canvas, x: int, y: int, width: int, height: int, scale: int = SCALE):
        self.name = name
        self.x = x * scale
        self.y = y * scale
        self.canvas = canvas
        self.width = width * scale
        self.height = height * scale
        self.cfgVars = []
        self.children = []
        self.scale = scale
    def addCfgVar(self, name: str, width: int, value: int = 0):
        self.cfgVars.append(CfgVar(name, width, value))
    def addChild(self, child: "Module"):
        self.children.append(child)
    def writeBits(self, bitfile):
        for cfgVar in self.cfgVars:
            cfgVar.writeBits(bitfile)
        for child in self.children:
            child.writeBits(bitfile)
    def readBits(self, bitfile):
        for cfgVar in self.cfgVars:
            cfgVar.readBits(bitfile)
        for child in self.children:
            child.readBits(bitfile)
    def writeCfg(self, prefix: str, cfgfile):
        prefix = prefix + self.name + "."
        for cfgVar in self.cfgVars:
            cfgVar.writeCfg(prefix, cfgfile)
        for child in self.children:
            child.writeCfg(prefix, cfgfile)
    def getCfgVar(self, path: str):
        idx = path.find(".")
        name = path
        path = None
        if idx != -1:
            path = name[idx+1:]
            name = name[:idx]
            for child in self.children:
                if child.name != name:
                    continue
                return child.getCfgVar(path)
            return None
        for cfgVar in self.cfgVars:
            if cfgVar.name != name:
                continue
            return cfgVar
        return None
    def getChild(self, path: str):
        idx = path.find(".")
        name = path
        path = None
        if idx != -1:
            path = name[idx+1:]
            name = name[:idx]
        for child in self.children:
            if child.name != name:
                continue
            return child.getChild(path) if path else child
        return None
    def show(self):
        for child in self.children:
            child.show()
    def hide(self):
        for child in self.children:
            child.hide()
    def onClick(self):
        pass
    def intersect(self, x: int, y: int) -> bool:
        x -= 2
        y -= 2
        return x >= self.x and y >= self.y and x < self.x+self.width and y < self.y+self.height

class Mux(Module):
    def __init__(self, name: str, canvas: tk.Canvas, x: int, y: int, numInputs: int, value: int, scale: int = SCALE):
        super().__init__(name, canvas, x, y, 28, 56, scale)
        self.numInputs = numInputs
        self.spacing = (36*scale) / (numInputs - 1)
        self.addCfgVar("SEL", (numInputs-1).bit_length(), value)
        self.line = None
    def show(self):
        super().show()
        self.line = self.canvas.create_line(0, 0, 0, 0, width=2*self.scale)
        self.updateLine()
    def hide(self):
        super().hide()
        self.canvas.delete(self.line)
        self.line = None
    def onClick(self):
        state = self.cfgVars[0].get() + 1
        if state >= self.numInputs:
            state = 0
        self.cfgVars[0].set(state)
        self.updateLine()
    def updateLine(self):
        state = self.cfgVars[0].get()
        self.canvas.coords(self.line,
                           self.x,
                           self.y + (10*self.scale) + (state * self.spacing),
                           self.x + self.width,
                           self.y + (self.height / 2))

class PIPUnidir(Module):
    def __init__(self, name: str, canvas: tk.Canvas, x: int, y: int):
        super().__init__(name, canvas, x, y, 4, 4)
        self.addCfgVar("EN", 1, 0)
        self.cfgVars[0].trace("w", lambda *_: self.updateRect())
        self.rect = None
    def show(self):
        super().show()
        self.rect = self.canvas.create_rectangle(self.x, self.y, self.x+(3*self.scale), self.y+(3*self.scale))
        self.updateRect()
    def hide(self):
        super().hide()
        self.canvas.delete(self.rect)
        self.rect = None
    def onClick(self):
        self.cfgVars[0].set(self.cfgVars[0].get() ^ 1)
        self.updateRect()
    def updateRect(self):
        if not self.rect:
            return
        state = self.cfgVars[0].get()
        fill = "green" if (state != 0) else "red"
        self.canvas.itemconfig(self.rect, fill=fill)
    def writeCfg(self, prefix: str, cfgfile):
        cfgfile.write("{}{} = {}\n".format(prefix, self.name, self.cfgVars[0].get()))

class PIPBidir(Module):
    def __init__(self, name: str, canvas: tk.Canvas, x: int, y: int):
        super().__init__(name, canvas, x, y, 4, 4)
        self.addCfgVar("EN", 2, 0)
        self.cfgVars[0].trace("w", lambda *_: self.updateRect())
        self.rect = None
        self.horLine = None
        self.vertLine = None
    def show(self):
        super().show()
        self.rect = self.canvas.create_rectangle(self.x, self.y, self.x+(3*self.scale), self.y+(3*self.scale), fill="red")
        self.horLine = self.canvas.create_line(self.x-self.scale, self.y+(2*self.scale), self.x+(5*self.scale), self.y+(2*self.scale), fill="green", width=2*self.scale)
        self.vertLine = self.canvas.create_line(self.x+(2*self.scale), self.y-self.scale, self.x+(2*self.scale), self.y+(5*self.scale), fill="green", width=2*self.scale)
        self.updateRect()
    def hide(self):
        super().hide()
        self.canvas.delete(self.rect)
        self.canvas.delete(self.horLine)
        self.canvas.delete(self.vertLine)
        self.rect = None
        self.horLine = None
        self.vertLine = None
    def onClick(self):
        stateNext = self.cfgVars[0].get() + 1
        if stateNext == 3:
            stateNext = 0
        self.cfgVars[0].set(stateNext)
        self.updateRect()
    def updateRect(self):
        if not self.rect:
            return
        state = self.cfgVars[0].get()
        if state == 0:
            self.canvas.itemconfig(self.rect, state="normal")
            self.canvas.itemconfig(self.horLine, state="hidden")
            self.canvas.itemconfig(self.vertLine, state="hidden")
        elif state == 1:
            self.canvas.itemconfig(self.rect, state="hidden")
            self.canvas.itemconfig(self.horLine, state="normal")
            self.canvas.itemconfig(self.vertLine, state="hidden")
        else:
            self.canvas.itemconfig(self.rect, state="hidden")
            self.canvas.itemconfig(self.horLine, state="hidden")
            self.canvas.itemconfig(self.vertLine, state="normal")
    def writeCfg(self, prefix: str, cfgfile):
        cfgfile.write("{}{} = {}\n".format(prefix, self.name, format(self.cfgVars[0].get(), "02b")[::-1]))

class Switch(Module):
    def __init__(self, name: str, canvas: tk.Canvas, x: int, y: int, frame: "SwitchFrame", sides: str = "NESW"):
        super().__init__(name, canvas, x, y, 11, 11)
        self.frame = frame
        self.sides = sides
        if "N" in sides:
            if "E" in sides:
                self.addCfgVar("1_3", 1, 0)
                self.addCfgVar("3_1", 1, 0)
                self.addCfgVar("2_3", 1, 0)
                self.addCfgVar("3_2", 1, 0)
                self.addCfgVar("2_4", 1, 0)
                self.addCfgVar("4_2", 1, 0)
            if "S" in sides:
                self.addCfgVar("1_5", 1, 0)
                self.addCfgVar("5_1", 1, 0)
                self.addCfgVar("1_6", 1, 0)
                self.addCfgVar("6_1", 1, 0)
                self.addCfgVar("2_5", 1, 0)
                self.addCfgVar("5_2", 1, 0)
                self.addCfgVar("2_6", 1, 0)
                self.addCfgVar("6_2", 1, 0)
            if "W" in sides:
                self.addCfgVar("1_7", 1, 0)
                self.addCfgVar("7_1", 1, 0)
                self.addCfgVar("1_8", 1, 0)
                self.addCfgVar("8_1", 1, 0)
                self.addCfgVar("2_8", 1, 0)
                self.addCfgVar("8_2", 1, 0)
        if "E" in sides:
            if "S" in sides:
                self.addCfgVar("3_5", 1, 0)
                self.addCfgVar("5_3", 1, 0)
                self.addCfgVar("4_5", 1, 0)
                self.addCfgVar("5_4", 1, 0)
                self.addCfgVar("4_6", 1, 0)
                self.addCfgVar("6_4", 1, 0)
            if "W" in sides:
                self.addCfgVar("3_7", 1, 0)
                self.addCfgVar("7_3", 1, 0)
                self.addCfgVar("3_8", 1, 0)
                self.addCfgVar("8_3", 1, 0)
                self.addCfgVar("4_7", 1, 0)
                self.addCfgVar("7_4", 1, 0)
                self.addCfgVar("4_8", 1, 0)
                self.addCfgVar("8_4", 1, 0)
        if "S" in sides and "W" in sides:
            self.addCfgVar("5_7", 1, 0)
            self.addCfgVar("7_5", 1, 0)
            self.addCfgVar("6_7", 1, 0)
            self.addCfgVar("7_6", 1, 0)
            self.addCfgVar("6_8", 1, 0)
            self.addCfgVar("8_6", 1, 0)
    def onClick(self):
        self.frame.showSwitch(self)
    def writeBits(self, bitfile):
        for conn in SWITCH_CONNS:
            cfgVar = self.getCfgVar(conn)
            if cfgVar:
                cfgVar.writeBits(bitfile)
            else:
                bitfile.write("0")
    def readBits(self, bitfile):
        for conn in SWITCH_CONNS:
            cfgVar = self.getCfgVar(conn)
            if cfgVar:
                cfgVar.readBits(bitfile)
            else:
                bitfile.read(1)
    def writeCfg(self, prefix: str, cfgfile):
        bits = io.StringIO()
        self.writeBits(bits)
        cfgfile.write("{}{} = {}\n".format(prefix, self.name, bits.getvalue()))

class SwitchFrame(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.switch = None
        self.checkboxes = []
        for conn in SWITCH_CONNS:
            self.addCheckbox(conn)
        self.protocol("WM_DELETE_WINDOW", self.onClose);
    def addCheckbox(self, name: str):
        col = int(name[0]) - 1
        row = int(name[2]) - 1
        checkbox = tk.Checkbutton(self, text=name)
        checkbox.grid(row=row, column=col, sticky=tk.W)
        self.checkboxes.append(checkbox)
    def onClose(self):
        self.switch.hide()
        self.switch = None
        self.withdraw()
    def showSwitch(self, switch: Switch):
        if self.switch:
            self.switch.hide()
        self.switch = switch
        for checkbox in self.checkboxes:
            checkbox.config(variable=None, state="disabled")
        for cfgVar in switch.cfgVars:
            for checkbox in self.checkboxes:
                if checkbox["text"] == cfgVar.name:
                    checkbox.config(variable=cfgVar, state="normal")
        switch.show()
        self.deiconify()

class Flop(Module):
    def __init__(self, name: str, canvas: tk.Canvas, x: int, y: int, frame: "FlopFrame"):
        super().__init__(name, canvas, x, y, 46, 82)
        self.frame = frame
        self.addCfgVar("EN", 1, 0)
        self.addCfgVar("LATCH", 1, 0)
        self.addCfgVar("EN_SET", 1, 0)
        self.addCfgVar("EN_RST", 1, 0)
        self.addCfgVar("INV_CLK", 1, 0)
    def onClick(self):
        self.frame.showFlop(self)

class FlopFrame(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.flop = None
        self.checkboxes = []
        self.addCheckbox("Enable")
        self.addCheckbox("Latch")
        self.addCheckbox("Enable set")
        self.addCheckbox("Enable reset")
        self.addCheckbox("Invert clock/enable")
        self.protocol("WM_DELETE_WINDOW", self.onClose);
    def addCheckbox(self, name: str):
        checkbox = tk.Checkbutton(self, text=name)
        checkbox.grid(sticky=tk.W)
        self.checkboxes.append(checkbox)
    def onClose(self):
        self.flop.hide()
        self.flop = None
        self.withdraw()
    def showFlop(self, flop: Flop):
        if self.flop:
            self.flop.hide()
        self.flop = flop
        for i in range(len(self.checkboxes)):
            self.checkboxes[i].config(variable=flop.cfgVars[i])
        flop.show()
        self.deiconify()

class LUT3(Module):
    def __init__(self, name: str, canvas: tk.Canvas, x: int, y: int, frame: "LUT3Frame"):
        super().__init__(name, canvas, x, y, 197, 213, 1)
        self.frame = frame
        for i in range(8):
            self.addCfgVar(format(i, "03b"), 1, 0)
    def onClick(self):
        self.frame.showLUT3(self)

class LUT3Frame(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.lut3 = None
        self.checkboxes = []
        for i in range(8):
            self.addCheckbox(format(i, "03b"))
        self.protocol("WM_DELETE_WINDOW", self.onClose)
    def addCheckbox(self, name: str):
        checkbox = tk.Checkbutton(self, text=name)
        checkbox.grid(sticky=tk.W)
        self.checkboxes.append(checkbox)
    def onClose(self):
        self.lut3.hide()
        self.lut3 = None
        self.withdraw()
    def showLUT3(self, lut3: LUT3):
        if self.lut3:
            self.lut3.hide()
        self.lut3 = lut3
        for i in range(len(self.checkboxes)):
            self.checkboxes[i].config(variable=lut3.cfgVars[i])
        lut3.show()
        self.deiconify()

class LUT4(Module):
    def __init__(self, name: str, canvas: tk.Canvas, x: int, y: int, lut4Frame: "LUT4Frame", lut3Frame: LUT3Frame):
        super().__init__(name, canvas, x, y, 109, 110)
        self.frame = lut4Frame
        self.addChild(Mux("INMUX0", lut4Frame.canvas, 133, 120, 2, 0, 1))
        self.addChild(Mux("INMUX1", lut4Frame.canvas, 133, 191, 2, 0, 1))
        self.addChild(Mux("INMUX2", lut4Frame.canvas, 133, 269, 3, 0, 1))
        self.addChild(Mux("INMUX3", lut4Frame.canvas, 133, 394, 2, 0, 1))
        self.addChild(Mux("INMUX4", lut4Frame.canvas, 133, 463, 2, 0, 1))
        self.addChild(Mux("INMUX5", lut4Frame.canvas, 133, 539, 3, 0, 1))
        self.addChild(Mux("FGMUX", lut4Frame.canvas, 555, 199, 2, 0, 1))
        self.addChild(LUT3("LUT0", lut4Frame.canvas, 201, 119, lut3Frame))
        self.addChild(LUT3("LUT1", lut4Frame.canvas, 201, 392, lut3Frame))
    def show(self):
        for i in range(7):
            self.children[i].show()
    def hide(self):
        for i in range(7):
            self.children[i].hide()
    def onClick(self):
        self.frame.showLUT4(self)

class LUT4Frame(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.lut4 = None
        self.canvas = tk.Canvas(self, width=746, height=675)
        self.canvas.pack()
        self.img = tk.PhotoImage(file="lut4.png")
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img)
        self.canvas.bind("<Button-1>", self.onClick)
        self.protocol("WM_DELETE_WINDOW", self.onClose)
    def onClick(self, event: tk.Event):
        for child in self.lut4.children:
            if child.intersect(event.x, event.y):
                child.onClick()
                return
    def onClose(self):
        self.lut4.hide()
        self.lut4 = None
        self.withdraw()
    def showLUT4(self, lut4: LUT4):
        if self.lut4:
            self.lut4.hide()
        self.lut4 = lut4
        lut4.show()
        self.deiconify()

class CLB(Module):
    def __init__(self, name: str, canvas: tk.Canvas, x: int, y: int, clbFrame: "CLBFrame", flopFrame: FlopFrame, lut4Frame: LUT4Frame, lut3Frame: LUT3Frame):
        super().__init__(name, canvas, x, y, 27, 43)
        self.frame = clbFrame
        self.addChild(Mux("SETMUX", clbFrame.canvas, 342, 73, 2, 0))
        self.addChild(Mux("CLKMUX", clbFrame.canvas, 343, 215, 3, 0))
        self.addChild(Mux("RSTMUX", clbFrame.canvas, 343, 304, 2, 0))
        self.addChild(Mux("XMUX", clbFrame.canvas, 493, 28, 3, 0))
        self.addChild(Mux("YMUX", clbFrame.canvas, 493, 126, 3, 0))
        self.addChild(Flop("FLOP", clbFrame.canvas, 404, 188, flopFrame))
        self.addChild(LUT4("LUT4", clbFrame.canvas, 164, 117, lut4Frame, lut3Frame))
    def show(self):
        for i in range(5):
            self.children[i].show()
    def hide(self):
        for i in range(5):
            self.children[i].hide()
    def onClick(self):
        self.frame.showCLB(self)
    def writeBits(self, bitfile):
        for i in range(6):
            self.getCfgVar("LUT4.INMUX{}.SEL".format(i)).writeBits(bitfile)
        self.getCfgVar("LUT4.FGMUX.SEL").writeBits(bitfile)
        self.getCfgVar("CLKMUX.SEL").writeBits(bitfile)
        # Encode EN and INV_CLK
        if self.getCfgVar("FLOP.EN").get() == 0:
            bitfile.write("00")
        elif self.getCfgVar("FLOP.INV_CLK").get() == 0:
            bitfile.write("01")
        else:
            bitfile.write("10")
        # Encode EN_SET and SETMUX
        if self.getCfgVar("FLOP.EN_SET").get() == 0:
            bitfile.write("00")
        elif self.getCfgVar("SETMUX.SEL").get() == 0:
            bitfile.write("10")
        else:
            bitfile.write("01")
        # Encode EN_RST and RSTMUX
        if self.getCfgVar("FLOP.EN_RST").get() == 0:
            bitfile.write("00")
        elif self.getCfgVar("RSTMUX.SEL").get() == 0:
            bitfile.write("10")
        else:
            bitfile.write("01")
        self.getCfgVar("FLOP.LATCH").writeBits(bitfile)
        self.getCfgVar("XMUX.SEL").writeBits(bitfile)
        self.getCfgVar("YMUX.SEL").writeBits(bitfile)
        self.getChild("LUT4.LUT0").writeBits(bitfile)
        self.getChild("LUT4.LUT1").writeBits(bitfile)
    def readBits(self, bitfile):
        for i in range(6):
            self.getCfgVar("LUT4.INMUX{}.SEL".format(i)).readBits(bitfile)
        self.getCfgVar("LUT4.FGMUX.SEL").readBits(bitfile)
        self.getCfgVar("CLKMUX.SEL").readBits(bitfile)
        # Decode EN and INV_CLK
        bits = bitfile.read(2)
        if bits == "00" or bits == "11":
            self.getCfgVar("FLOP.EN").set(0)
            self.getCfgVar("FLOP.INV_CLK").set(0)
        elif bits == "10":
            self.getCfgVar("FLOP.EN").set(1)
            self.getCfgVar("FLOP.INV_CLK").set(1)
        else:
            self.getCfgVar("FLOP.EN").set(1)
            self.getCfgVar("FLOP.INV_CLK").set(0)
        # Encode EN_SET and SETMUX
        bits = bitfile.read(2)
        if bits == "00" or bits == "11":
            self.getCfgVar("FLOP.EN_SET").set(0)
            self.getCfgVar("SETMUX.SEL").set(0)
        elif bits == "10":
            self.getCfgVar("FLOP.EN_SET").set(1)
            self.getCfgVar("SETMUX.SEL").set(0)
        else:
            self.getCfgVar("FLOP.EN_EST").set(1)
            self.getCfgVar("SETMUX.SEL").set(1)
        # Encode EN_RST and RSTMUX
        bits = bitfile.read(2)
        if bits == "00" or bits == "11":
            self.getCfgVar("FLOP.EN_RST").set(0)
            self.getCfgVar("RSTMUX.SEL").set(0)
        elif bits == "10":
            self.getCfgVar("FLOP.EN_RST").set(1)
            self.getCfgVar("RSTMUX.SEL").set(0)
        else:
            self.getCfgVar("FLOP.EN_RST").set(1)
            self.getCfgVar("RSTMUX.SEL").set(1)
        self.getCfgVar("FLOP.LATCH").readBits(bitfile)
        self.getCfgVar("XMUX.SEL").readBits(bitfile)
        self.getCfgVar("YMUX.SEL").readBits(bitfile)
        self.getChild("LUT4.LUT0").readBits(bitfile)
        self.getChild("LUT4.LUT1").readBits(bitfile)
    def writeCfg(self, prefix: str, cfgfile):
        bitfile = io.StringIO()
        self.writeBits(bitfile)
        cfgfile.write("{}{} = {}\n".format(prefix, self.name, bitfile.getvalue()))

class CLBFrame(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.clb = None
        self.canvas = tk.Canvas(self, width=587*SCALE, height=419*SCALE)
        self.canvas.pack()
        self.img = tk.PhotoImage(file="clb.png").zoom(SCALE, SCALE)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img)
        self.canvas.bind("<Button-1>", self.onClick)
        self.protocol("WM_DELETE_WINDOW", self.onClose);
    def onClick(self, event: tk.Event):
        for child in self.clb.children:
            if child.intersect(event.x, event.y):
                child.onClick()
                return
    def onClose(self):
        self.clb.hide()
        self.clb = None
        self.withdraw()
    def showCLB(self, clb: CLB):
        if self.clb:
            self.clb.hide()
        self.clb = clb
        clb.show()
        self.deiconify()

class IOB(Module):
    def __init__(self, name: str, canvas: tk.Canvas, x: int, y: int, horizontal: bool, frame: "IOBFrame"):
        if horizontal:
            super().__init__(name, canvas, x, y, 27, 17)
        else:
            super().__init__(name, canvas, x, y, 17, 35)
        self.frame = frame
        self.addCfgVar("EN", 1, 0)
        self.addCfgVar("TS", 1, 0)
        self.addCfgVar("FLOP", 1, 0)
    def onClick(self):
        self.frame.showIOB(self)
    def writeCfg(self, prefix: str, cfgfile):
        bits = io.StringIO()
        self.writeBits(bits)
        cfgfile.write("{}{} = {}\n".format(prefix, self.name, bits.getvalue()))

class IOBFrame(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.iob = None
        self.checkboxes = []
        self.addCheckbox("Output enable")
        self.addCheckbox("Tristate enable")
        self.addCheckbox("Input flop")
        self.protocol("WM_DELETE_WINDOW", self.onClose);
    def addCheckbox(self, name: str):
        checkbox = tk.Checkbutton(self, text=name)
        checkbox.grid(sticky=tk.W)
        self.checkboxes.append(checkbox)
    def onClose(self):
        self.iob.hide()
        self.iob = None
        self.withdraw()
    def showIOB(self, iob: IOB):
        if self.iob:
            self.iob.hide()
        self.iob = iob
        for i in range(len(self.checkboxes)):
            self.checkboxes[i].config(variable=iob.cfgVars[i])
        iob.show()
        self.deiconify()

class FPGA(Module):
    def __init__(self, canvas: tk.Canvas):
        super().__init__("FPGA", canvas, 0, 0, 890, 898)
        self.canvas = canvas
        self.clbFrame = CLBFrame()
        self.clbFrame.withdraw()
        self.flopFrame = FlopFrame()
        self.flopFrame.withdraw()
        self.switchFrame = SwitchFrame()
        self.switchFrame.withdraw()
        self.iobFrame = IOBFrame()
        self.iobFrame.withdraw()
        self.lut4Frame = LUT4Frame()
        self.lut4Frame.withdraw()
        self.lut3Frame = LUT3Frame()
        self.lut3Frame.withdraw()
        self.numPips = 0
        for x in range(8):
            for y in range(8):
                clbx = 107 + int(x * XSPACE)
                clby = 97 + int(y * YSPACE)
                clbName = chr(0x41+y) + chr(0x41+x)
                self.addChild(CLB("CLB_" + clbName, canvas, clbx, clby, self.clbFrame, self.flopFrame, self.lut4Frame, self.lut3Frame))
                pipName = "PIP_"+clbName
                if y > 0:
                    self.addPips(pipName+"_A", clbx, clby, CLB_PIP_A, True)
                else:
                    self.addPips(pipName+"_A", clbx, clby, CLB_TOP_PIP_A, True)
                if x > 0:
                    self.addPips(pipName+"_B", clbx, clby, CLB_PIP_B, True)
                    self.addPips(pipName+"_C", clbx, clby, CLB_PIP_C, True)
                    self.addPips(pipName+"_K", clbx, clby, CLB_PIP_K, True)
                else:
                    self.addPips(pipName+"_B", clbx, clby, CLB_LEFT_PIP_B, True)
                    self.addPips(pipName+"_C", clbx, clby, CLB_LEFT_PIP_C, True)
                    self.addPips(pipName+"_K", clbx, clby, CLB_LEFT_PIP_K, True)
                if y < 7:
                    self.addPips(pipName+"_D", clbx, clby, CLB_PIP_D, True)
                else:
                    self.addPips(pipName+"_D", clbx, clby, CLB_BOT_PIP_D, True)
                if x < 7:
                    self.addPips(pipName+"_X", clbx, clby, CLB_PIP_X, True)
                    self.addPips(pipName+"_Y", clbx, clby, CLB_PIP_Y, True)
                elif clbName == "EH":
                    self.addPips(pipName+"_X", clbx, clby, CLB_RIGHT_PIP_X, True, ["OUTHI"])
                    self.addPips(pipName+"_Y", clbx, clby, CLB_RIGHT_PIP_Y, True, ["OUTHI"])
                else:
                    self.addPips(pipName+"_X", clbx, clby, CLB_RIGHT_PIP_X, True)
                    self.addPips(pipName+"_Y", clbx, clby, CLB_RIGHT_PIP_Y, True)
        for x in range(7):
            for y in range(7):
                switchx = 144 + int(x * XSPACE)
                switchy = 154 + int(y * YSPACE)
                switchName = chr(0x41+y+1) + chr(0x41+x+1)
                self.addChild(Switch("SW_"+switchName+"_0", canvas, switchx, switchy, self.switchFrame))
                self.addChild(Switch("SW_"+switchName+"_1", canvas, switchx+11, switchy+11, self.switchFrame))
                self.addPips("PIP_SW_"+switchName, switchx, switchy, SWITCH_PIP)
        for y in range(7):
            switchx = 37
            switchy = 154 + int(y * YSPACE)
            switchName = "LEFT" + str(y)
            self.addChild(Switch("SW_"+switchName+"_0", canvas, switchx, switchy, self.switchFrame, "NES"))
            self.addChild(Switch("SW_"+switchName+"_1", canvas, switchx+11, switchy+11, self.switchFrame, "NES"))
            self.addPips("PIP_SW_"+switchName, switchx, switchy, SWITCH_LEFT_PIP)

            switchx = 830
            switchName = "RIGHT" + str(y)
            self.addChild(Switch("SW_"+switchName+"_0", canvas, switchx, switchy, self.switchFrame, "NSW"))
            self.addChild(Switch("SW_"+switchName+"_1", canvas, switchx+11, switchy+11, self.switchFrame, "NSW"))
            self.addPips("PIP_SW_"+switchName, switchx, switchy, SWITCH_RIGHT_PIP)
        for x in range(7):
            switchx = 144 + int(x * XSPACE)
            switchy = 45
            switchName = "TOP" + str(x)
            self.addChild(Switch("SW_"+switchName+"_0", canvas, switchx, switchy, self.switchFrame, "ESW"))
            self.addChild(Switch("SW_"+switchName+"_1", canvas, switchx+11, switchy+11, self.switchFrame, "ESW"))
            self.addPips("PIP_SW_"+switchName, switchx, switchy, SWITCH_TOP_PIP)

            switchy = 828
            switchName = "BOT" + str(x)
            self.addChild(Switch("SW_"+switchName+"_0", canvas, switchx+11, switchy, self.switchFrame, "NEW"))
            self.addChild(Switch("SW_"+switchName+"_1", canvas, switchx, switchy+11, self.switchFrame, "NEW"))
            self.addPips("PIP_SW_"+switchName, switchx, switchy, SWITCH_BOT_PIP)
        for iob in LEFT_IOB:
            self.addChild(IOB("IOB_"+iob[2], canvas, iob[0], iob[1], False, self.iobFrame))
            if iob[2] in ["P11","P13","P15","P17","P19","P21","P23"]:
                pips = IOB_LEFT_TOP_PIP
            else:
                pips = IOB_LEFT_BOT_PIP
            self.addPips("PIP_IOB_"+iob[2], iob[0], iob[1], pips, True)
        for iob in TOP_IOB:
            self.addChild(IOB("IOB_"+iob[2], canvas, iob[0], iob[1], True, self.iobFrame))
            if iob[2] in ["P7","P5","P3","P68","P66","P64","P62"]:
                pips = IOB_TOP_LEFT_PIP
            elif iob[2] == "P9":
                pips = IOB_P9_PIP
            elif iob[2] == "P61":
                pips = IOB_P61_PIP
            else:
                pips = IOB_TOP_RIGHT_PIP
            self.addPips("PIP_IOB_"+iob[2], iob[0], iob[1], pips, True)
        for iob in RIGHT_IOB:
            self.addChild(IOB("IOB_"+iob[2], canvas, iob[0], iob[1], False, self.iobFrame))
            if iob[2] in ["P59","P57","P55","P53","P51","P49","P47"]:
                pips = IOB_RIGHT_TOP_PIP
            else:
                pips = IOB_RIGHT_BOT_PIP
            self.addPips("PIP_IOB_"+iob[2], iob[0], iob[1], pips, True)
        for iob in BOT_IOB:
            self.addChild(IOB("IOB_"+iob[2], canvas, iob[0], iob[1], True, self.iobFrame))
            if iob[2] in ["P29","P31","P33","P36","P38","P40","P42"]:
                pips = IOB_BOT_LEFT_PIP
            elif iob[2] == "P43":
                pips = IOB_P43_PIP
            elif iob[2] == "P27":
                pips = IOB_P27_PIP
            else:
                pips = IOB_BOT_RIGHT_PIP
            self.addPips("PIP_IOB_"+iob[2], iob[0], iob[1], pips, True)
        self.addPips("PIP_TOP_LEFT", 0, 0, TOP_LEFT_CORNER_PIP)
        self.addPips("PIP_GLOBALIN", 0, 0, GLOBALIN_PIP, True)
        self.addPips("PIP_TOP_RIGHT", 0, 0, TOP_RIGHT_CORNER_PIP)
        self.addPips("PIP_BOT_RIGHT", 0, 0, BOT_RIGHT_CORNER_PIP)
        self.addPips("PIP_ALTIN", 0, 0, ALTIN_PIP, True)
        self.addPips("PIP_BOT_LEFT", 0, 0, BOT_LEFT_CORNER_PIP)
    def addPips(self, groupName: str, clbx: int, clby: int, pipData: list, unidir: bool = False, exclude: list = None):
        for pip in pipData:
            if exclude and pip[2] in exclude:
                continue
            if unidir:
                pip = PIPUnidir(groupName+"_"+pip[2], self.canvas, clbx+pip[0], clby+pip[1])
            else:
                pip = PIPBidir(groupName+"_"+pip[2], self.canvas, clbx+pip[0], clby+pip[1])
            pip.show()
            self.addChild(pip)
            self.numPips += 1
    def readBits(self, bitfile):
        super().readBits(bitfile)

class FPGAFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.fpga = None
        self.canvas = tk.Canvas(self, width=890, height=898, scrollregion=(0,0,890*SCALE,898*SCALE))
        self.canvas.pack()
        self.img = tk.PhotoImage(file="intercon_all2.png").zoom(SCALE, SCALE)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img)
        self.canvas.bind("<ButtonPress-1>", self.onClick)
        self.canvas.bind("<B1-Motion>", self.onDrag)
    def setFPGA(self, fpga: FPGA):
        self.fpga = fpga
    def onClick(self, event: tk.Event):
        self.canvas.scan_mark(event.x, event.y)
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        for child in self.fpga.children:
            if child.intersect(x, y):
                child.onClick()
                return
    def onDrag(self, event: tk.Event):
        self.canvas.scan_dragto(event.x, event.y, gain=1)
    def writeBits(self):
        with open("gui_save.txt", "w") as f:
            self.fpga.writeBits(f)
        print("Wrote save file")
    def readBits(self, filename: str):
        with open(filename, "r") as f:
            self.fpga.readBits(f)
        print("Read save file")
    def writeCfg(self):
        with open("config.txt", "w") as f:
            self.fpga.writeCfg("", f)
        print("Wrote config")
    def writeAll(self):
        self.writeBits()
        self.writeCfg()

if __name__ == "__main__":
    root = tk.Tk()
    app = FPGAFrame(root)
    app.pack()
    root.bind("<Escape>", lambda *_: app.writeAll())
    fpga = FPGA(app.canvas)
    app.setFPGA(fpga)
    if len(sys.argv) > 1:
        app.readBits(sys.argv[1])
    app.mainloop()
