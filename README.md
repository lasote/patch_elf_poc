1. Compile the executable with `g++ main.cpp -o main`
2. Patch to add a new section with `python patch.py main`
3. Read the patched section with `objcopy main /dev/null --dump-section .deps=/dev/stdout`
