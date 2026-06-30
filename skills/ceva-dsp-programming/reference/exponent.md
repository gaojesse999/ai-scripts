# Bit Manipulation → Exponent

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Bit Manipulation → Exponent

Exponent

Instruction Type and Width       Instruction description
                                 Outputs an exponent value for a complex number. Each complex
Vector Complex Exponent 32-bit   source consists of real 40-bit part and imaginary 40-bit part. The
                                 exponent is written either to 16-bit or 20-bit register.
                                 Returns the exponent value of the source. The source is 32-bit
                                 wide. The exponent value (a 6-bit unsigned number) is zero-
Vector Exponent 32-bit
                                 extended before it is written to the destination. The destination
                                 is either 16-bit or 8-bit wide.
                                 Returns the exponent value of the source. The source is 40-bit
                                 wide. The exponent value (a 6-bit signed number) is sign-
Vector Exponent 40-bit
                                 extended before it is written to the destination. The destination
                                 is either 16-bit or 8-bit wide.
                                 Returns the exponent value of the source. The source is 64-bits
Vector Exponent Long 64-bit      wide. The destination is either 16-bit or 8-bit wide determined by
                                 the vector register type.
                                 Returns the exponent value of the source. The source is 72-bits
Vector Exponent Long 72-bit      wide. The destination is either 16-bit or 8-bit wide determined by
                                 the vector register type.
