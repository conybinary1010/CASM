
from asyncio.windows_events import NULL


instruction_set = {
    "HALT" : 0x01,
    "LOAD" : 0x2,
    "READ" : 0x3
}

reg_set = {
    "r0" : 0x1,
    "r1" : 0x2,
    "r2": 0x3
}


def assemble_instructions(instruction, reg, value):
    if instruction not in instruction_set and instruction is not NULL:
        raise ValueError(f"invalid instruction: {instruction}")
    elif reg not in reg_set and reg is not NULL :
        raise ValueError(f"invalid reg : {reg}")

    machine_code_instr = []
    machine_code_reg = []
    machine_code_value = []

    if  instruction == "HALT":
        machine_code_instr.append(instruction_set[instruction])
        return machine_code_instr
    elif  instruction == "LOAD":
        machine_code_instr.append(instruction_set[instruction])
        return machine_code_instr
    elif  instruction == "READ":
        machine_code_instr.append(instruction_set[instruction])
        return machine_code_instr

    elif reg == "r0":
        machine_code_reg.append(reg_set[reg])
        return machine_code_reg
    elif reg == "r1":
        machine_code_reg.append(reg_set[reg])
        return machine_code_reg
    elif reg == "r2":
        machine_code_reg.append(reg_set[reg])
        return machine_code_reg

    elif value is hex:
        machine_code_value.append(int(value, 16))

print("macine code:", assemble_instructions("LOAD", NULL, NULL))
print("macine code:", assemble_instructions(NULL, "r0", NULL))
print("macine code:", assemble_instructions(NULL, NULL, "0x00"))