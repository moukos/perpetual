# perpetual
Perpetual Litmus tests

- Assembling C files. Can be used to cross check the assembly we write with the automatically generated one
Example: gcc -S test.c
- Linking assembly and C to build executable:
Example: gcc -o test test.c testAssembly.s 
- When running with OpenMP library:
gcc -o harness -pthread -fopenmp harnessNoAssembly.c 
