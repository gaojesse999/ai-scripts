# Multiplication → Multiply

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Multiplication → Multiply

Multiply

Instruction Type and Width              Instruction description
                                        Performs multiplication between two sources. Each source is
16x16                                   16-bit wide. The destination is either 32-bit or 40-bit determined
                                        by the vector register type.
                                        Performs two sets of operations: eight multiplications according
                                        to the first operands set, and a multiply operation from the
                                        second operand set executed according to the Hhop switch. The
16x16 Multiply and Multiply             sources are 16-bit wide. Each set is written into different vector
                                        destinations. The multiplication products are placed into either
                                        32-bit or 40-bit destination respectively determined by the vector
                                        register type.
                                        Performs two multiplication and pack operations. Each source is
16x16 and Pack into Bytes               16-bit. each destination is 8-bit and are packed into 20-bit or 16-
                                        bit determined by the vector register type.
                                        Performs multiplication and packing between two sources. Each
                                        source is 16-bit wide. Either the 16-bit msbs or 16-bit lsbs are
16x16 and Pack into Two 16-bit Words
                                        taken from the products and packed into either 32-bit or 40-bit

destination determined by the vector register type.
                                        Performs two multiplications between two sources. Each source
16x16 and Pack into Two Words           is 16-bit wide. Both products are packed into either 32-bit or 40-
                                        bit destination determined by the vector register type.
                                        Performs multiplication with exponent between two sources.
16x16 with Exponent                     Each source is 16-bit. The destination is either 32-bit or 40-bit
                                        determined by the vector register type.
                                        Performs multiply of 32-bit by 16-bit. The result is written into
32x16                                   32-bit or 40-bit destination determined by the vector register
                                        type.
                                        Performs multiply with exponent of 32-bit by 16-bit. The first
                                        source is 32-bit and the second is 16-bit wide. The result is
32x16 with Exponent
                                        written into 32-bit or 40-bit determined by the vector register
                                        type.
                                        Performs multiplication. Each source is 32-bit wide. The
32x32                                   products are written into a 64-bit or 72-bits wide determined by
                                        the vector register type.
                                        Performs complex multiply operation between complex number
                                        and complex sign (+/-1, +/-j1) control. The data source consists
Complex 16x1 and Add                    of real 16-bit part and imaginary 16-bit part. The control source
                                        consists of 1-bit real part and 1-bit imaginary part. The real and
                                        the imaginary results are written each into 20-bit destination.
                                        Performs complex multiplication between two complex
                                        numbers. Each complex source consists of real 16-bit part and
Complex 16x16
                                        imaginary 16-bit part. The multipication products are
                                        accumulated into 40-bit destination parts respectively.

Performs complex multiplication between two complex
                                        numbers. Each complex source consists of real 16-bit part and
Complex 16x16 and Pack into Two Words
                                        imaginary 16-bit part. The multipication products are
                                        accumulated into 20-bit destination parts respectively.
                                            Performs complex multiply with exponent between two complex
                                            numbers. Each complex source consists of real 16-bit part and
Complex 16x16 with Exponent                 imaginary 16-bit part. The third source is the exponent. Each of
                                            the real and the imaginary products are accumulated with the
                                            40-bit destination respectively.
                                            Performs complex multiply with exponent between two complex
                                            numbers. Each complex source consists of real 16-bit part and
Complex 16x16 with Exponent and Pack into
                                            imaginary 16-bit part. The third source is the exponent. The
Two Words
                                            complex product is packed into either 32-bit or 40-bit destination
                                            determined by the vector register type.
                                            Performs complex multiplication between two complex
                                            numbers. The first complex source consists of real 16-bit part
                                            and imaginary 16-bit part, and the second complex source
Complex 16x8 into Two Words                 consists of real 8-bit part and imaginary 8-bit part. Each of the
                                            real and the imaginary products is accumulated and placed into
                                            20-bit destination respectively and packed into 40-bit
                                            destination.
                                            Performs complex multiplication between two complex
                                            numbers. The first complex source consists of real 32-bit part
                                            and imaginary 32-bit part. The second complex source consists
Complex 32x16

of real 16-bit part and imaginary 16-bit part. Each of the real and
                                            the imaginary products are written into the 40-bit destination
                                            respectively.
                                            Performs complex multiply with exponent between two complex
                                            numbers. The first complex source consists of real 32-bit part
                                            and imaginary 32-bit part. The second complex source consists
Complex 32x16 with Exponent
                                            of real 16-bit part and imaginary 16-bit part. Each of the real and
                                            the imaginary products are accumulated with the 40-bit
                                            destination respectively.
                                            Performs complex multiplication using four products. Each
Complex 32x32                               source is 64-bits wide (32-bit real and 32-bit Imaginary). The
                                            products are accumulated into two 72-bit destinations.
                                            Performs complex by real multiplication between a complex
                                            number and a real 16-bit number. The complex source consists
Semi-Complex 16x16                          of real 16-bit part and imaginary 16-bit part. The real and the
                                            imaginary products are placed into either 32-bit or 40-bit
                                            destination respectively determined by the vector register type.
                                            Performs two complex by real multiplication between a complex
                                            number and a real 16-bit number. The complex source consists
Semi-Complex 16x16 and Pack into Two        of real 16-bit part and imaginary 16-bit part. Each product is
Words                                       placed into either real or image destination respecitvely and
                                            packed into either 32-bit or 40-bit destination determined by the
                                            vector register type.
                                            Performs complex operation by real multipliy with exponent
                                            between a complex number and a real number. The complex

source consists of real 16-bit part and imaginary 16-bit part. The
Semi-Complex 16x16 with Exponent
                                            real number source consists of 16-bit. Each of the real and the
                                            imaginary products is accumulated with the 40-bit destination
                                            respectively.
                                            Performs semi-complex multiply between a complex number
                                            and a real number. The complex source consists of real 16-bit
Semi-Complex 16x32                          part and imaginary 16-bit part. The real source consists of real
                                            32-bit part. Each of the real and the imaginary products are
                                            written to a 40-bit destination respectively.
Semi-Complex 16x32 with Exponent            Performs semi-complex multiply with exponent between a
                                   complex number and a real number. The complex source
                                   consists of real 16-bit part and imaginary 16-bit part. The real
                                   source consists of real 32-bit part. Each of the real and the
                                   imaginary products are accumulated with the 40-bit destination
                                   respectively.
                                   Performs semi-complex multiply between a complex number
                                   and a real number. The complex source consists of real 32-bit
Semi-Complex 32x16                 part and imaginary 32-bit part. The real source consists of real
                                   16-bit part. Each of the real and the imaginary products are
                                   written to a 40-bit destination respectively.
                                   Performs semi-complex multiply with exponent between a
                                   complex number and a real number. The complex source
                                   consists of real 32-bit part and imaginary 32-bit part. The real
Semi-Complex 32x16 with Exponent
                                   source consists of real 16-bit part. Each of the real and the
                                   imaginary products are accumulated with the 40-bit destination
                                   respectively.

Performs semi-complex multiplication using two products.
                                   Complex source is 64-bits wide (32-bit real and 32-bit Imaginary).
Semi-Complex 32x32
                                   Real source is 32-bits wide. The products are accumulated into
                                   two 72-bit destinations.
