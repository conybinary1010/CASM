
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
    if instruction not in instruction_set:
        raise ValueError(f"invalid instruction: {instruction}")
    elif reg not in reg_set:
        raise ValueError(f"invalid reg : {reg}")

    machine_code = []

    if  instruction == "HALT":
        machine_code.append(instruction_set[instruction])
        return machine_code
    elif  instruction == "LOAD":
        machine_code.append(instruction_set[instruction])
        return machine_code
    elif  instruction == "READ":
        machine_code.append(instruction_set[instruction])
        return machine_code

    if reg == "r0":
        machine_code.append(reg_set[reg])
        return machine_code
    elif reg == "r1":
        machine_code.append(reg_set[reg])
        return machine_code
    elif reg == "r2":
        machine_code.append(reg_set[reg])
        return machine_code


print("macine code:", assemble_instructions("HALT", "r0, 0x00"))