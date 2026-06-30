# Multiplication → Multiply-Accumulate

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Multiplication → Multiply-Accumulate

Multiply-Accumulate

Instruction Type and Width                   Instruction description

Performs multiply-accumulate between two sources. Each
16x16                                        source is 16-bit wide. The product is accumulated with the 40-bit
                                             destination.
                                             Performs two sets of operations: eight multiply-accumulate
                                             operations according to first operands set and multiplication
                                             according to the second operands set. The sources are 16-bit
16x16 MAC and Multiply                       wide. Each set is written into different vector destinations. The
                                             eight multiply-accumulate products are accumulated with eight
                                             40-bit wide destinations respectively. The multiplication product
                                             is placed into 40-bit destination.
                                             Performs two multiply-accumulate operations between two
                                             sources. Each source is 16-bit wide. Each product is
16x16 and Pack into Two Words
                                             accumulated with the 20-bit destination part respectively and
                                             packed into 40-bit destination.
                                             Performs multiply-accumulate using two products. Each source
16x16 using Two Products                     is 16-bit wide. The products are accumulated with the 40-bit
                                             destination.
                                             Performs multiply-accumulate between two sources with
16x16 with Exponent                          exponent operation using third source. Each source is 16-bit
                                             wide. The product is accumulated with the 40-bit destination.
                                             Performs two multiply-accumulate operations between two
                                             sources and a constant, using two products. The sources are
16x8 using Two Products into Two Words       16-bit each and a constant of 8-bit. The products are
                                             accumulated with the 20-bit destination respectively and are
                                             packed into 40-bit destination.

Performs multiply-accumulate 32x16 operation. The first source
32x16                                        is 32-bit wide and the second source is 16-bit wide. The
                                             products are accumulated with the 40-bit destination.
                                             Performs multiply-accumulate with exponent. The first source is
32x16 with Exponent                          32-bit wide and the second source is 16-bit wide. The products
                                             are accumulated with the 40-bit destination.
                                             Performs multiply-accumulate between two sources. Each
32x32                                        source is 32-bit wide. The product is accumulated with the 72-bit
                                             destination.
                                             Performs complex multiply-accumulate between two complex
                                             numbers. Each complex source consists of real 16-bit part and
Complex 16x16                                imaginary 16-bit part. Each of the real and the imaginary
                                             products are accumulated with the 40-bit destination
                                             respectively.
                                           Performs complex multiply-pack accumulate and subtract
                                           between two complex numbers. Each complex source consists
                                           of real 16-bit part and imaginary 16-bit part. Each of the real and
Complex 16x16 Multiply Pack-Accumulate and
                                           the imaginary products are accumulated with and subtracted
Subtract
                                           from the 20-bit accumulator. The accumulation result is written
                                           to 20-bit destination. The subtarction result is written to a 16-bit
                                           or 20-bit destination.
Complex 16x16 with Exponent                  Performs complex multiply-accumulate with exponent between
                                       two complex numbers. Each complex source consists of real 16-
                                       bit part and imaginary 16-bit part. The third source is the
                                       exponent. Each of the real and the imaginary products are

accumulated with the 40-bit destination respectively.
                                       Performs complex multiply-accumulate between two complex
                                       numbers. The first complex source consists of real 16-bit part
                                       and imaginary 16-bit part, and the second complex source
Complex 16x8 into Two Words
                                       consists of real 8-bit part and imaginary 8-bit part. Each of the
                                       real and the imaginary products is accumulated with the 20-bit
                                       destination respectively and packed into 40-bit destination.
                                       Performs complex multiply-accumulate between two complex
                                       numbers. The first complex source consists of real 32-bit part
                                       and imaginary 32-bit part. The second complex source consists
Complex 32x16
                                       of real 16-bit part and imaginary 16-bit part. Each of the real and
                                       the imaginary products are accumulated with the 40-bit
                                       destination respectively.
                                       Performs complex multiply-accumulate with exponent between
                                       two complex numbers. The first complex source consists of real
                                       32-bit part and imaginary 32-bit part. The second complex
Complex 32x16 with Exponent
                                       source consists of real 16-bit part and imaginary 16-bit part.
                                       Each of the real and the imaginary products are accumulated
                                       with the 40-bit destination respectively.
                                       Performs complex multiplication accumulate using four
                                       products. Each source is 64-bits wide (32-bit real and 32-bit
Complex 32x32
                                       Imaginary). The products are accumulated into two 72-bit
                                       destinations.
                                       Performs complex multiply-and-accumulate operation between
                                       complex data number, and a complex sign (+/-1, +/-j1) control

value. The data source consists of real 16-bit part and imaginary
Complex and Accumulate 16x1
                                       16-bit part. The control source consists of 1-bit real part and 1-
                                       bit imaginary part. The results are accumulated to a 40-bits
                                       accumulators.
                                       Performs multipliy-accumulate between a complex number and
                                       a real number. The complex source consists of real 16-bit part
Semi-Complex 16x16                     and imaginary 16-bit part. The real number source consists of
                                       16-bit. Each of the real and the imaginary products is
                                       accumulated with the 40-bit destination respectively.
                                       Performs two-complex by real multipliy-accumulate operations
                                       between a complex number and a real number. The complex
Semi-Complex 16x16 and Pack into Two   source consists of real 16-bit part and imaginary 16-bit part. The
Words                                  real number source is 16-bit wide. Each product is accumulated
                                       with the 20-bit destination part respectively and packed into 40-
                                       bit destination.
                                       Performs complex operation by real multipliy-accumulate with
                                       exponent between a complex number and a real number. The
                                       complex source consists of real 16-bit part and imaginary 16-bit
Semi-Complex 16x16 with Exponent
                                       part. The real number source consists of 16-bit. Each of the real
                                       and the imaginary products is accumulated with the 40-bit
                                       destination respectively.
                                       Performs semi-complex 16x32 multiply-accumulate between a
                                       complex number and a real number. The complex source
                                       consists of real 16-bit part and imaginary 16-bit part. The real
Semi-Complex 16x32 into Two Words
                                       source consists of real 32-bit part. Each of the real and the

imaginary products are accumulated with the 40-bit destination
                                       respectively.
                                   Performs semi-complex multiply-accumulate with exponent
                                   between a complex number and a real number. The complex
                                   source consists of real 16-bit part and imaginary 16-bit part. The
Semi-Complex 16x32 with Exponent
                                   real source consists of real 32-bit part. Each of the real and the
                                   imaginary products are accumulated with the 40-bit destination
                                   respectively.
                                   Performs semi-complex multiply-accumulate 32x16 between a
                                   complex number and a real number. The complex source
                                   consists of real 32-bit part and imaginary 32-bit part. The real
Semi-Complex 32x16
                                   source consists of real 16-bit part. Each of the real and the
                                   imaginary products are accumulated with the 40-bit destination
                                   respectively.
                                   Performs semi-complex multiply-accumulate with exponent
                                   between a complex number and a real number. The complex
                                   source consists of real 32-bit part and imaginary 32-bit part. The
Semi-Complex 32x16 with Exponent
                                   real source consists of real 16-bit part. Each of the real and the
                                   imaginary products are accumulated with the 40-bit destination
                                   respectively.
                                   Performs semi-complex multiplication accumulate using two
                                   products. Complex source is 64-bits wide (32-bit real and 32-bit
Semi-Complex 32x32
                                   Imaginary). Real source is 32-bits wide. The products are
                                   accumulated into two 72-bit destinations.
