# Multiplication → Multiply and Add Two Products

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Multiplication → Multiply and Add Two Products

Multiply and Add Two Products

Instruction Type and Width                  Instruction description
                                            Performs four real multiply-and-add operation between real data
                                            numbers and real sign (+/-1) control numbers. Each of the four
                                            data sources consists of 16-bit real number. Each of the four
16x1 Multiply and Add Four Products         real sign control sources consists of 1-bit real part. Each of data
                                            is multiplied by the 1-bit control real value. The four products
                                            are summed togather, producing a 20-bits result for each part
                                            (real, imaginary).
                                            Performs two real multiply-and-add operation between real data
                                            numbers and real sign (+/-1) control numbers. Each of the two
                                            data sources consists of 16-bit real number. Each of the two real
16x1 Multiply and Add Two Products          sign control sources consists of 1-bit real part. Each of data is
                                            multiplied by the 1-bit control real value. The two products are
                                            summed togather, producing a 20-bits result for each part (real,
                                            imaginary).
                                            Performs multiplication and addition between two products.
16x16 Multiply and Add Two Products         Each source is 16-bit wide. The result is placed into 40-bit
                                            destination.
                                            Performs two multiplication operations between two sources
16x8 Multiply and Add Two Products into Two and a constant, and addition between the two products. The

Words                                       sources are 16-bit wide each and a constant of 8-bit. The 20-bit
                                            results are packed into a 40-bit destination.
                                            Performs multiplication and addition between two products.
32x32 Multiply and Add Two Products         Each source is 32-bit wide. The result is placed into 72-bit
                                            destination.
                                           Performs complex multiply operation between complex data
                                           number, and a complex sign (+/-1, +/-j1) control value. The data
                                           source consists of real 16-bit part and imaginary 16-bit part. The
Complex 16x1 Multiply and Add Two Products
                                           control source consists of 1-bit real part and 1-bit imaginary
                                           part. The result consists of 20-bits real and 20-bits imaginary
                                           parts.
                                            Performs four semi-complex multiply-and-add operation
                                            between complex data numbers and real sign (+/-1) control
                                            numbers. Each of the four data sources consists of real 16-bit
Semi-Complex 16x1 Multiply and Add Four     part and imaginary 16-bit part. Each of the four real sign control
Products                                    sources consists of 1-bit real part. Each of complex data is
                                            multiplied by a 1-bit control real value. The four complex
                                            products are summed togather, producing a complex 20-bits
                                            result.
                                            Performs two semi-complex multiply-and-add operation between
                                            complex data numbers and real sign (+/-1) control numbers.
                                            Each of the two data sources consists of real 16-bit part and
Semi-Complex 16x1 Multiply and Add Two
                                            imaginary 16-bit part. Each of the two real sign control sources
Products
                                            consists of 1-bit real part. Each of complex data is multiplied by

a 1-bit control real value. The two complex products are
                                            summed togather, producing a complex 20-bits result.
