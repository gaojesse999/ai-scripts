# Generic → Generic Multiply-Accumulate

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Generic → Generic Multiply-Accumulate

Generic Multiply-Accumulate

Instruction Type and Width                Instruction description
                                          Performs configurable multiply-accumulate between two
                                          sources using CISA. The multiplicands and products signs are
16x16
                                          user configured according to the configuration register set.

Each source is 16-bit wide. The destination is 40-bit.
                                          Performs configurable multiplication between four sources and
                                          accumulation using two products by using CISA. The
16x16 MAC3                                multiplicands, products signs, and accumulation operations are
                                          user configured according to the configuration register set.
                                          Each source is 16-bit wide. The destination is 40-bit wide.
                                          Performs configurable multiply-accumulate between two
                                          sources using CISA. The multiplicands, products signs and
16x16 Multiply or MAC and Pack Into Two   accumulation operations are user configuredaccording to the
Words                                     configuration register set. Each source is 16-bit wide. The
                                          addition results are 20-bit wide and packed into 40-bit
                                          destination.
                                          Performs configurable multiplication between four sources and
                                          accumulation using two products by using CISA. The
                                          multiplicands, products signs and accumulation operations are
16x8 MAC3 into Two Words
                                          user configured according to the configuration regsiter set. The
                                          sources are 16-bit and 8-bit wide. The accumulation results are
                                          20-bit wide each and are packed into 40-bit destination.
                                          Performs configurable 32x16 multiply-accumulate/subtract using
                                          CISA mechanism. The multiplicands, products signs, and
                                          accumulation operations are user configured according to the
32x16
                                          configuration register set. The first source is 32-bit wide
                                          compound from 2 configurable 16-bit wide sources. The second
                                          source is 16-bit wide source. The destination is 40-bit wide.
                                          Performs configurable multiply-accumulate between two

sources using CISA. The multiplicands and products signs are
32x32
                                          user configured according to the configuration register set.
                                          Each source is 32-bit wide. The destination is 72-bit.
                                          Performs configurable multiplication between four sources and
                                          accumulation using two products by using CISA. The
32x32 MAC3                                multiplicands, products signs, and accumulation operations are
                                          user configured according to the configuration register set.
                                          Each source is 32-bit wide. The destination is 72-bit wide.
                                          Performs complex multiply-accumulate between two complex
                                          numbers. Each complex source consists of real 16-bit part and
Complex 16x16                             imaginary 16-bit part. Each of the real and the imaginary
                                          products are accumulated with the 40-bit destination
                                          respectively.
