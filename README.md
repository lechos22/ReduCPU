## ReduCPU
This proccessor has super llama powers

# ---16 BITS---

0x0-0xF: All

0x0-0x7: Sub-Instruction

0x8-0xF: Parameter

# ---Sub-Instructions---

0x00: ZER, Empty CPU Clock cycle

0x01: GET, Load byte from memory into RA

0x02: SET, Set byte in memory to RA

0x03: ADD, Add value of byte in memory to RA

0x04: SUB, Subtract value of byte in memory from RA

0x05: VAL, Load parameter value into RA

0x06: RGG, Set RA to parameter register's value

0x07: RGS, Set parameter register's value to RA

0x08: RST, Reset CC


# ---Registers---

0x00: RA, Accumulator

0x01: IP, Instruction Pointer

0x02: PO, Program Offset

0x03: MO, Memory Offset

0x04: CC, Condition Check
