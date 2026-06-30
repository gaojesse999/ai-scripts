# Multiplication → Multiply-Subtract

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Multiplication → Multiply-Subtract

Multiply-Subtract

Instruction Type and Width               Instruction description
                                         Performs multiply-subtract between two sources. Each source is
16x16                                    16-bit wide. The product is subtracted from the 40-bit
                                         destination.
                                         Performs two sets of operations: eight multiply-subtract
                                         operations and multiply operation according to the Oop switch.
                                         The sources are 16-bit. Each set is written into different vector
16x16 MSU and Multiply
                                         destinations. The eight multiply-accumulate products are
                                         subtracted from eight 40-bit destinations respectively. The
                                         multiply product is placed into 40-bit destination.
                                         Performs two multiply-subtract operations between two sources.
                                         Each source is 16-bit wide. Each product is subtracted from the
16x16 and Pack into Two Words
                                         20-bit destination part respectively and packed into 40-bit
                                         destination.
                                         Performs multiply-subtract using two products. Each source is

16x16 using Two Products
                                         16-bit. The products are subtracted from the 40-bit destination.
                                         Performs multiply-Subtract between two sources with exponent
16x16 with Exponent                      operation using third source. Each source is 16-bit wide. The
                                         product is accumulated with the 40-bit destination.
                                         Performs two multiply-subtract operations between two sources
                                         and a constant, using two products. The sources are 16-bit wide
16x8 using Two Products into Two Words   each and a constant of 8-bit. The products are subtracted from
                                         the 20-bit destination respectively and packed into 40-bit
                                         destination.
                                         Performs multiply-subtract 32x16 operation. The first source is
32x16                                    32-bit wide and the second source is 16-bit wide. The products
                                         are accumulated with the 40-bit destination.
                                         Performs multiply-subtract with exponent. The first source is 32-
32x16 with Exponent                      bit wide and the second source is 16-bit wide. The products are
                                         subtractd with the 40-bit destination.
                                         Performs multiply-subtract between two sources. Each source is
32x32                                    32-bit wide. The products is subtracted from the 72-bit
                                         destination.
                                         Performs complex multiply-subtract between two complex
                                         numbers. Each complex source consists of real 16-bit part and
Complex 16x16
                                         imaginary 16-bit part. Each of the real and the imaginary
                                         products is subtracted from the 40-bit destination respectively.
                                         Performs complex multiply-subtract with exponent between two
                                         complex numbers. Each complex source consists of real 16-bit
Complex 16x16 with Exponent              part and imaginary 16-bit part. The third source is the exponent.

Each of the real and the imaginary products are subtractd with
                                         the 40-bit destination respectively.
                                         Performs complex multiply-subtract between two complex
                                         numbers. The first complex source consists of real 16-bit part
                                         and imaginary 16-bit part, and the second complex source
Complex 16x8 into Two Words
                                         consists of real 8-bit part and imaginary 8-bit part. Each of the
                                         real and the imaginary products is subtracted from the 20-bit
                                         destination respectively and packed into 40-bit destination.
                                       Performs complex multiply-subtract between two complex
                                       numbers. The first complex source consists of real 32-bit part
                                       and imaginary 32-bit part. The second complex source consists
Complex 32x16
                                       of real 16-bit part and imaginary 16-bit part. Each of the real and
                                       the imaginary products are accumulated with the 40-bit
                                       destination respectively.
                                       Performs complex multiply-subtract with exponent between two
                                       complex numbers. The first complex source consists of real 32-
                                       bit part and imaginary 32-bit part. The second complex source
Complex 32x16 with Exponent
                                       consists of real 16-bit part and imaginary 16-bit part. Each of the
                                       real and the imaginary products are subtractd with the 40-bit
                                       destination respectively.
                                       Performs complex multiplication subtract complex numbers.
Complex 32x32                          Each source is 64-bits wide (32-bit real and 32-bit Imaginary).
                                       The products are accumulated into two 72-bit destinations.
                                       Performs complex by real multipliy-subtract between a complex
                                       number and a real number. The complex source consists of real

Semi-Complex 16x16                     16-bit part and imaginary 16-bit part, the real number source
                                       consists of 16-bit. Each of the real and the imaginary products
                                       are subtracted from the 40-bit destination respectively.
                                       Performs two complex by real multipliy-subtract operations
                                       between a complex number and a real number. The complex
Semi-Complex 16x16 and Pack into Two   source consists of real 16-bit part and imaginary 16-bit part, the
Words                                  real number source consists of 16-bit. Each product is
                                       subtracted from the 20-bit destination part respectively and
                                       packed into 40-bit destination.
                                       Performs complex operation by real multipliy-subtract with
                                       exponent between a complex number and a real number. The
                                       complex source consists of real 16-bit part and imaginary 16-bit
Semi-Complex 16x16 with Exponent
                                       part. The real number source consists of 16-bit. Each of the real
                                       and the imaginary products is subtractd with the 40-bit
                                       destination respectively.
                                       Performs semi-complex 16x32 multiply-subtract between a
                                       complex number and a real number. The complex source
                                       consists of real 16-bit part and imaginary 16-bit part. The real
Semi-Complex 16x32
                                       source consists of real 32-bit part. Each of the real and the
                                       imaginary products are subtracted from the 40-bit destination
                                       respectively.
                                       Performs semi-complex multiply-subtract with exponent
                                       between a complex number and a real number. The complex
                                       source consists of real 16-bit part and imaginary 16-bit part. The
Semi-Complex 16x32 with Exponent
                                       real source consists of real 32-bit part. Each of the real and the

imaginary products are subtractd with the 40-bit destination
                                       respectively.
                                       Performs semi-complex multiply-subtract 32x16 between a
                                       complex number and a real number. The complex source
                                       consists of real 32-bit part and imaginary 32-bit part. The real
Semi-Complex 32x16
                                       source consists of real 16-bit part. Each of the real and the
                                       imaginary products are subtrcated from the 40-bit destination
                                       respectively.
                                       Performs semi-complex multiply-subtract with exponent
                                       between a complex number and a real number. The complex
                                       source consists of real 32-bit part and imaginary 32-bit part. The
Semi-Complex 32x16 with Exponent
                                       real source consists of real 16-bit part. Each of the real and the
                                       imaginary products are Subtractd with the 40-bit destination
                                       respectively.
                     Performs semi-complex multiplication subtract using two
                     products. Complex source is 64-bits wide (32-bit real and 32-bit
Semi-Complex 32x32
                     Imaginary). Real source is 32-bits wide. The products are
                     subtracted from two 72-bit destinations.
