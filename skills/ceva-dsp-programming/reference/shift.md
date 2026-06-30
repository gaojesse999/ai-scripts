# Bit Manipulation → Shift

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Bit Manipulation → Shift

Shift

Instruction Type and Width        Instruction description
                                  By default performs two arithmetic shift operations on a 20-bit
Vector Shift                      sources packed into either 32-bit or 40-bit destination
                                  determined by the register type.
                                  By default performs an arithmetic shift operation on a 40-bit
Vector Shift 40-bit               source, the result is written to either 32-bit or 40-bit destination
                                  determined by the register type.
                                  By default performs an arithmetic shift operation on a 72-bit
Vector Shift 72-bit               source, the result is written to either 64-bit or 72-bit destination
                                  determined by the register type.
                                  Performs arithmetic or logic shift operation on complex
                                  numbers. Each complex number consists of a real 32-bit part
Vector Shift Complex              and an imaginary 32-bit part. The results for each complex part
                                  are placed into 32-bit or 40-bit register destination determinedby
                                  the vector register type.
                                  Performs an arithmetic or logic shift operations on a complex
                                  source comprised of 40-bit image and real parts. The results for
Vector Shift Complex 40-bit
                                  each complex part are written into either 32-bit or 40-bit
                                  destinations determined by the register type.
                                  Performs an arithmetic or logic shift operations on a complex

source comprised of 72-bit image and real parts. The results for
Vector Shift Complex 72-bit
                                  each complex part are written into either 64-bit or 72-bit
                                  destinations determined by the register type.
                                  Performs arithmetic or logic shift operation on a 64-bit source
Vector Shift Long                 into either 64-bit or 72-bit destination determined by the register
                                  type.
                                  Performs two arithmetic or logic shift operations on two 16-bit
Vector Shift Word Parts           sources. The results are packed into either 32-bit or 40-bit
                                  destination determined by the register type.
                                  Performs two arithmetic or logic shift operations on two 16-bit
Vector Shift Word Parts Complex   sources. The results are packed into either 32-bit or 40-bit
                                  destination determined by the register type.
