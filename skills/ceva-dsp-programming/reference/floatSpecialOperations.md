# Floating Point → Float Special Operations

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Floating Point → Float Special Operations

Float Special Operations

Instruction Type and Width                     Instruction description
                                               Calculate the exponent value for the reciprocal value of the 32-
Vector Floating Point Reciprocal Result with   bit single precision floating point source, compute the correct
N-R Concat                                     mantissa value and concatenate the final result. This instruction
                                               is part of the VFLPDIVNR Macro operation.
                                               Performs a constant right shift by 30 (>>30) on a 64-bit source,
Vector Floating Point Constant Shift           and packs the result into 32 bits. This instruction is part of the
                                               non-native VFLPSQRT, VFLPSQRTI operations.
                                               Performs a square-root operation on the floating-point source’s
Vector Floating Point Reciprcoal SQRT
                                               16 MSBs of the mantissa value (including the hidden 1 bit). This
Mantissa
                                               instruction is part of the non-native VFLPSQRTI operation.
                                               Performs a reciprocal operation on the floating-point source’s 16
Vector Floating Point Reciprocal Mantissa      MSBs of the mantissa value (including the hidden 1 bit). This
                                               instruction is part of the non-native VFLPDIV operation.
                                               Performs a reciprocal operation on the floating-point source’s 16
Vector Floating Point Reciprocal Mantissa
                                               MSBs of the mantissa value (including the hidden 1 bit). This
With N-R
                                               instruction is part of the VFLPDIVNR operation.
                                               Calculate the exponent value for the reciprocal value of the 32-
                                               bit single precision floating point source, compute the correct
Vector Floating Point Reciprocal Result Concat
                                               mantissa value and concatenate the final result. This instruction
                                               is part of the non-native VFLPDIV operation.
                                               Calculate the exponent value for the reciprocal value of the 32-

Vector Floating Point Reciprocal SQRT Result   bit single precision floating point source, compute the correct
Concat                                         mantissa value and concatenate the final result. This instruction
                                               is part of the non-native VFLPSQRTI operation.
                                               Calculate the exponent value for the reciprocal value of the 32-
Vector Floating Point Reciprocal SQRT With     bit single precision floating point source, compute the correct
N-R result Concat                              mantissa value and concatenate the final result. This instruction
                                               is part of the non-native VFLPSQRTINR operation.
                                               Calculate the exponent value for the reciprocal value of the 32-
Vector Floating Point SQRT With N-R Result     bit single precision floating point source, compute the correct
Concat                                         mantissa value and concatenate the final result. This instruction
                                               is part of the non-native VFLPSQRTNR operation.
                                               Performs a subtraction/addition between the mantissas of two
                                               sources in 32-bit single precision floating point format and
                                               determines the sign of the final floating point result. The
                                               mantissa of the smaller source (in absolute value) is shifted
Vector Floating Point Shift Add/Sub
                                               according to the delta between the two exponents, and than
                                               subtracted/added from the mantissa of the larger source. This
                                               instruction is part of the non-native VFLPADD, VFLPSUB
                                               operations.
                                               Performs a square-root operation on the floating-point source’s
Vector Floating Point Square Root Mantissa     16 MSBs of the mantissa value (including the hidden 1 bit). This
                                               instruction is part of the non-native VFLPSQRT operation.
                                               Calculate the exponent value for the reciprocal value of the 32-

Vector Floating Point Square Root Result       bit single precision floating point source, compute the correct
Concat                                         mantissa value and concatenate the final result. This instruction
                                               is part of the non-native VFLPSQRT operation.
                                              Calculate and choose the correct square root approximation for
Vector Floating Point Square Root To          the reciprocal calculation of the reciprocal square root SW
Reciprocal Input                              sequence. This instruction is part of the non-native
                                              VFLPSQRTINR operation.
                                              Performs a square-root operation on the floating-point source’s
Vector Floating Point Square Root With N-R
                                              16 MSBs of the mantissa value (including the hidden 1 bit). This
Mantissa
                                              instruction is part of the non-native VFLPSQRTNR operation.
                                              Performs unpack shifted left by byte of either 32-bit or 40-bit
                                              source into two destinations of either 32-bit or 40-bit wide
Vector Floating Point Unpack Low Shift Left
                                              determined by the register type. This instruction is part of the
                                              non-native VFLPSQRT, VFLPSQRTI operations.
                                              Performs a conversion of the absolute value of a 32-bit single
                                              precision floating point number into signed/unsigned integer
Vector Floating Point to Integer              representation. In case the destination’s type is signed integer,
                                              the MSB bit is the same as the input?s sign-bit. This instruction
                                              is part of the non-native VFLPINT operation.
                                              Performs a conversion of the absolute value of a 32-bit single
                                              precision floating point number into signed/unsigned short-
Vector Floating Point to Short Integer        integer representation. In case the destination’s type is signed

short-integer, the MSB bit is the same as the input’s sign-bit.
                                              This instruction is part of the non-native VFLPSINT operation.
                                              Performs a conversion of an absolute value signed/unsigned
                                              integer number into floating point representation. If the input is a
Vector Integer to Float Conversion            signed integer, its MSB bit is disregarded and used in order to
                                              determine the sign of the result. This instruction is part of the
                                              non-native VINTFLP operation.
                                              Performs a conversion of a signed/unsigned short integer into a
                                              32-bit single precision floating-point source destination. The
Vector Short Integer to Floating Point
                                              sources and the destination are either 32-bit or 40-bit wide
                                              determined by the vector register type.
