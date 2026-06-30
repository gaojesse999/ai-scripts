# Multiplication → Multiply and Subtract Two Products → 16x8 Multiply and

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Multiplication → Multiply and Subtract Two Products → 16x8 Multiply and
Subtract Two Products into Two Words

16x8 Multiply and Subtract Two Products into Two Words

16x8 Multiply and Subtract Two Products into Two Words
Performs two multiplication operations between two sources and a constant, and subtraction
between the two products. The sources are 16-bit wide each and a constant of 8-bit. The 20-bit
results are packed into a 40-bit destination.
Available Switches
               Number of atomic operations. An atomic operation is defined as two add-and-
Oop
               subtract-two-products operations. 1op ≤ Oop ≤ 8op
               When used, the 20 LSBs of the products are taken (instead of the high parts). The
low
               default behavior is the high parts.
vmpsX          Selects the VMSNX and VPSX set within modv0 or modv2 mode registers.
Intrinsic Names
vmaswb_v32_v32_c32_v40_low
vmaswb_v32_v32_c32_v40_low_vmpsX
vmaswb_v32_v32_c32_v40
vmaswb_v32_v32_c32_v40_vmpsX
Instruction details in the instruction set specification
Intrinsic     vmaswb_v32_v32_c32_v40_low[_p]
name

Spec syntax   vmaswb {Oop [,low][,vmpsX]} vx[X]p, vy[Y]p, vcWp, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0,4
                                                            Offset for the first DW used from operand
                                                            2

              4    IN1_PART       uint8     LOW,HIGH        Word part which is used for operand 2
              5    IN2_V32        vec_t                     Input vector operand
Operands
              6    IN2_OFST       uint8     0,4             Offset for the first DW used from operand
                                                            5

              7    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 5
              8    IN3_C32        coef_t                    Coefficient operand
              9    IN3_PART       uint8     LOW,HIGH        Word part which is used for operand 8
              10   IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     coef_t vcoefIn;
              vprex_t vecPred;
              ...
              vRes = vmaswb_v32_v32_c32_v40_low_p (8, vIn, 0, LOW, vIn2, 0, LOW, vcoefIn, LOW, vecPred);

                   IN_VPR last operand is relevant only for vmaswb_v32_v32_c32_v40_low_p
Comments      1.
                   version.


Main table → Multiplication → Multiply and Subtract Two Products → 16x8 Multiply and
Subtract Two Products into Two Words
Intrinsic     vmaswb_v32_v32_c32_v40_low_vmpsX[_p]
name
Spec syntax   vmaswb {Oop [,low][,vmpsX]} vx[X]p, vy[Y]p, vcWp, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8            Number of atomic operations
                                                            Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
Operands
              3    IN1_V32        vec_t                     Input vector operand

              4    IN1_OFST       uint8     0,4             Offset for the first DW used from operand
                                                            3

5    IN1_PART      uint8     LOW,HIGH        Word part which is used for operand 3
              6    IN2_V32       vec_t                     Input vector operand

              7    IN2_OFST      uint8     0,4             Offset for the first DW used from operand
                                                           6

              8    IN2_PART      uint8     LOW,HIGH        Word part which is used for operand 6
              9    IN3_C32       coef_t                    Coefficient operand
              10   IN3_PART      uint8     LOW,HIGH        Word part which is used for operand 9
              11   IN_VPR        vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vmaswb_v32_v32_c32_v40_low_vmpsX_p (8, 1, vIn, 0, LOW, vIn2, 0, LOW, vcoefIn, LOW,
              vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmaswb_v32_v32_c32_v40_low_vmpsX_p version.


Main table → Multiplication → Multiply and Subtract Two Products → 16x8 Multiply and
Subtract Two Products into Two Words
Intrinsic     vmaswb_v32_v32_c32_v40[_p]
name
Spec syntax   vmaswb {Oop [,low][,vmpsX]} vx[X]p, vy[Y]p, vcWp, voz[0], ?vprX

Return type   vec40_t

              1    OOP           uint8     1..8            Number of atomic operations
              2    IN1_V32       vec_t                     Input vector operand

              3    IN1_OFST      uint8     0,4             Offset for the first DW used from operand
                                                           2

              4    IN1_PART      uint8     LOW,HIGH        Word part which is used for operand 2
              5    IN2_V32       vec_t                     Input vector operand
Operands
              6    IN2_OFST      uint8     0,4             Offset for the first DW used from operand
                                                           5

              7    IN2_PART      uint8     LOW,HIGH        Word part which is used for operand 5
              8    IN3_C32       coef_t                    Coefficient operand
              9    IN3_PART      uint8     LOW,HIGH        Word part which is used for operand 8
              10   IN_VPR        vprex_t                   Vector predicate operand
C example     vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;

coef_t vcoefIn;
              vprex_t vecPred;
              ...
              vRes = vmaswb_v32_v32_c32_v40_p (8, vIn, 0, LOW, vIn2, 0, LOW, vcoefIn, LOW, vecPred);

                   IN_VPR last operand is relevant only for vmaswb_v32_v32_c32_v40_p
Comments      1.
                   version.


Main table → Multiplication → Multiply and Subtract Two Products → 16x8 Multiply and
Subtract Two Products into Two Words
Intrinsic     vmaswb_v32_v32_c32_v40_vmpsX[_p]
name
Spec syntax   vmaswb {Oop [,low][,vmpsX]} vx[X]p, vy[Y]p, vcWp, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8            Number of atomic operations

              2
                                                            Selects the VMSNX and VPSX set within
                   VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand

              4    IN1_OFST       uint8     0,4
                                                            Offset for the first DW used from operand
                                                            3

              5    IN1_PART       uint8     LOW,HIGH        Word part which is used for operand 3
Operands      6    IN2_V32        vec_t                     Input vector operand

              7    IN2_OFST       uint8     0,4             Offset for the first DW used from operand
                                                            6

              8    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 6
              9    IN3_C32        coef_t                    Coefficient operand
              10   IN3_PART       uint8     LOW,HIGH        Word part which is used for operand 9
              11   IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     coef_t vcoefIn;
              vprex_t vecPred;
              ...
              vRes = vmaswb_v32_v32_c32_v40_vmpsX_p (8, 1, vIn, 0, LOW, vIn2, 0, LOW, vcoefIn, LOW, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmaswb_v32_v32_c32_v40_vmpsX_p version.


Main table → Multiplication → Multiply and Subtract Two Products → 16x8 Multiply and
Subtract Two Products into Two Words

Main table → Multiplication → Multiply and Subtract Two Products → 16x8 Multiply and
Subtract using Two Products and Accumulate into Two Words

16x8 Multiply and Subtract using Two Products and Accumulate into Two Words

16x8 Multiply and Subtract using Two Products and Accumulate into Two Words
Performs two multiply-subtract and accumulate operations. The sources are 16-bit each and a
constant of 8-bit. The first product is added and the second product is subtracted from the 20-bit
destination. Both 20-bit results are packed into 40-bit destination.
Available Switches
               Number of atomic operations. An atomic operation is defined as two multiply-add-
Oop
               and-subtract-two-products operations. 1op ≤ Oop ≤ 8op
               When used, the 20 LSBs of the products are taken (instead of the high parts). The
low
               default behavior is the high parts.
vmpsX          Selects the VMSNX and VPSX set within modv0 or modv2 mode registers.
Intrinsic Names
vmaswb3_v32_v32_c32_v40_low
vmaswb3_v32_v32_c32_v40_low_vmpsX
vmaswb3_v32_v32_c32_v40
vmaswb3_v32_v32_c32_v40_vmpsX
Instruction details in the instruction set specification
Intrinsic     vmaswb3_v32_v32_c32_v40_low[_p]
name
Spec syntax   vmaswb3 {Oop [,low][,vmpsX]} vx[X]p, vy[Y]p, vcWp, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0,4
                                                            Offset for the first DW used from operand
                                                            2

              4    IN1_PART       uint8     LOW,HIGH        Word part which is used for operand 2
              5    IN2_V32        vec_t                     Input vector operand
Operands      6    IN2_OFST       uint8     0,4             Offset for the first DW used from operand
                                                            5

              7    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 5
              8    IN3_C32        coef_t                    Coefficient operand
              9    IN3_PART       uint8     LOW,HIGH        Word part which is used for operand 8
              10   IN4_V40        vec40_t                   Output vector operand
              11   IN_VPR         vprex_t                   Vector predicate operand

vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     coef_t vcoefIn;
              vprex_t vecPred;
              ...
              vRes = vmaswb3_v32_v32_c32_v40_low_p (8, vIn, 0, LOW, vIn2, 0, LOW, vcoefIn, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmaswb3_v32_v32_c32_v40_low_p version.


Main table → Multiplication → Multiply and Subtract Two Products → 16x8 Multiply and
Subtract using Two Products and Accumulate into Two Words
Intrinsic     vmaswb3_v32_v32_c32_v40_low_vmpsX[_p]
name
Spec syntax   vmaswb3 {Oop [,low][,vmpsX]} vx[X]p, vy[Y]p, vcWp, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8            Number of atomic operations
                                                            Selects the VMSNX and VPSX set within
Operands      2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand
              4    IN1_OFST      uint8     0,4             Offset for the first DW used from operand
                                                           3

              5    IN1_PART      uint8     LOW,HIGH        Word part which is used for operand 3
              6    IN2_V32       vec_t                     Input vector operand

              7    IN2_OFST      uint8     0,4             Offset for the first DW used from operand
                                                           6

              8    IN2_PART      uint8     LOW,HIGH        Word part which is used for operand 6
              9    IN3_C32       coef_t                    Coefficient operand
              10   IN3_PART      uint8     LOW,HIGH        Word part which is used for operand 9
              11   IN4_V40       vec40_t                   Output vector operand
              12   IN_VPR        vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vmaswb3_v32_v32_c32_v40_low_vmpsX_p (8, 1, vIn, 0, LOW, vIn2, 0, LOW, vcoefIn, LOW,
              vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmaswb3_v32_v32_c32_v40_low_vmpsX_p version.

Main table → Multiplication → Multiply and Subtract Two Products → 16x8 Multiply and
Subtract using Two Products and Accumulate into Two Words
Intrinsic     vmaswb3_v32_v32_c32_v40[_p]
name
Spec syntax   vmaswb3 {Oop [,low][,vmpsX]} vx[X]p, vy[Y]p, vcWp, voz[0], ?vprX

Return type   vec40_t

              1    OOP           uint8     1..8            Number of atomic operations
              2    IN1_V32       vec_t                     Input vector operand

              3    IN1_OFST      uint8     0,4             Offset for the first DW used from operand
                                                           2

              4    IN1_PART      uint8     LOW,HIGH        Word part which is used for operand 2
Operands
              5    IN2_V32       vec_t                     Input vector operand

              6    IN2_OFST      uint8     0,4             Offset for the first DW used from operand
                                                           5

              7    IN2_PART      uint8     LOW,HIGH        Word part which is used for operand 5
              8    IN3_C32       coef_t                    Coefficient operand
              9    IN3_PART       uint8     LOW,HIGH        Word part which is used for operand 8
              10   IN4_V40        vec40_t                   Output vector operand
              11   IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     coef_t vcoefIn;
              vprex_t vecPred;
              ...
              vRes = vmaswb3_v32_v32_c32_v40_p (8, vIn, 0, LOW, vIn2, 0, LOW, vcoefIn, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for vmaswb3_v32_v32_c32_v40_p
Comments      1.
                   version.


Main table → Multiplication → Multiply and Subtract Two Products → 16x8 Multiply and
Subtract using Two Products and Accumulate into Two Words
Intrinsic     vmaswb3_v32_v32_c32_v40_vmpsX[_p]
name
Spec syntax   vmaswb3 {Oop [,low][,vmpsX]} vx[X]p, vy[Y]p, vcWp, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8            Number of atomic operations
                                                            Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers

3    IN1_V32        vec_t                     Input vector operand

              4    IN1_OFST       uint8     0,4             Offset for the first DW used from operand
                                                            3

              5    IN1_PART       uint8     LOW,HIGH        Word part which is used for operand 3

Operands      6    IN2_V32        vec_t                     Input vector operand

              7    IN2_OFST       uint8     0,4             Offset for the first DW used from operand
                                                            6

              8    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 6
              9    IN3_C32        coef_t                    Coefficient operand
              10   IN3_PART       uint8     LOW,HIGH        Word part which is used for operand 9
              11   IN4_V40        vec40_t                   Output vector operand
              12   IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     coef_t vcoefIn;
              vprex_t vecPred;
              ...
            vRes = vmaswb3_v32_v32_c32_v40_vmpsX_p (8, 1, vIn, 0, LOW, vIn2, 0, LOW, vcoefIn, LOW, vRes,
            vecPred);

                 IN_VPR last operand is relevant only for
Comments    1.
                 vmaswb3_v32_v32_c32_v40_vmpsX_p version.


Main table → Multiplication → Multiply and Subtract Two Products → 16x8 Multiply and
Subtract using Two Products and Accumulate into Two Words
