import lief
import sys

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Error, specify the executable to read")
        exit(-1)
    exe_name = sys.argv[1]

    binary = lief.parse(exe_name)
    section = lief.ELF.Section(".deps")
    section.content = bytearray("zlib/1.2.8, openssl/1.0.2j, libpng/1.0.6", "utf-8")
    binary.add(section)
    binary.write(exe_name)

    # To read section:
    # objcopy main /dev/null --dump-section .deps=/dev/stdout
