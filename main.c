#include<stdio.h>
#include<stdint.h>

//instruction set
#define HALT 0x1
#define LOAD 0x2
#define READ 0x3

//registers
#define r0 0x1
#define r1 0x2
#define r2 0x3


uint8_t assembly_instruction(uint8_t instruction, uint8_t reg, uint8_t value){
    uint16_t machine_code = (instruction << 12) | (reg << 8) | value;
    printf("Machine code: 0x%04X\n", machine_code);
    return machine_code;
}

int main(){
    assembly_instruction(LOAD, r0, 20);
    assembly_instruction(READ, r0, 0);
    assembly_instruction(HALT, 0, 0);
    return 0;
}