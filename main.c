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

int file_output(){
    FILE *out = fopen("program.bin", "wb");
    if (!out){
        perror("File errror");
        return 0;
    }
    
    uint16_t instru1 = assembly_instruction(LOAD, r0, 20);
    uint16_t instru2 = assembly_instruction(READ,r0, 0);
    uint16_t instru3 = assembly_instruction(HALT, 0, 0);

    if (fwrite(&instru1, sizeof(uint16_t), 1, out) != 1){
        perror("error writing to file");
        fclose(out);
        return 1;
    }
   
    fclose(out);
    printf("program succesfuly assembled to program.bin\n");
    return 0;
}

int main(){
    return file_output();
}