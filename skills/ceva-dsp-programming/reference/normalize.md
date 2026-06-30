# Move And Pack → Normalize

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Move And Pack → Normalize

Normalize

Instruction Type and Width          Instruction description
                                    Converts complex source into an exponent and two mantissa
                                    parts, one is real and the other is image. Each complex source
                                    consists of real 40bit part and imaginary 40-bit part determined
                                    by the vector register type. The mantissa parts both real and
Vector Complex Normalize
                                    image are written into 32-bit or 40-bit type registers vector
                                    depending on the register type. The complex exponent part is
                                    written either into 16-bit or 20-bit register in depending on the
                                    register type.
                                    Converts complex source into an exponent and two mantissa
                                    parts, one is real and the other is image. Each complex source
                                    consists of real 40bit part and imaginary 40-bit part determined
Vector Complex Normalize and Pack   by the vector register type. The mantissa real and image parts
                                    are packed into one 32-bit or 40-bit type destination depending
                                    on the register type. The exponent part is written either into 16-
                                    bit or 20-bit register.
                                    Normalizes a 40 bit source into a mantissa part and an exponent
                                    part. The mantissa is written into a 32-bit or 40-bit register
Vector Normalize                    depending on the destination register type. The exponent is
                                    wriiten into a 16-bit or 20-bit register depending on the
                                    destination register type.
                                    Normalizes and packs a 40 bit source into a mantissa part and
                                    an exponent part. Each part is written into a 16-bit or 20-bit
Vector Normalize and Pack

register within a different vector depending on the destination
                                    register type.
