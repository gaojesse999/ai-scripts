# Floating Point → Float/Integer Conversion

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Floating Point → Float/Integer Conversion

Float/Integer Conversion

Instruction Type and Width                    Instruction description
                                              Performs a conversion of a 32-bit single precision floating-point
                                              source into an integer destination. The sources and the

Vector Floating Point To Integer Conversion   destination are either 32-bit or 40-bit wide determined by the
                                              vector register type. This is a non-native instruction and is
                                              implemented as software sequence
                                              Performs a conversion of an absolute value signed/unsigned
                                              integer number into floating point representation. If the input is a
Vector Integer to Float Conversion            signed integer, its MSB bit is disregarded and used in order to
                                              determine the sign of the result. This instruction is part of the
                                              non-native VINTFLP operation.
                                              Performs a conversion of a signed/unsigned short integer into a
                                              32-bit single precision floating-point source destination. The
Vector Short Integer to Float Conversion      sources and the destination are either 32-bit or 40-bit wide
                                              determined by the vector register type. This is a non-native
                                              instruction and is implemented as software sequence.
