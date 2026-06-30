# Multiplication → Multiply-Accumulate → 16x8 using Two Products into

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Multiplication → Multiply-Accumulate → 16x8 using Two Products into
Two Words

16x8 using Two Products into Two Words

16x8 using Two Products into Two Words
Performs two multiply-accumulate operations between two sources and a constant, using two
products. The sources are 16-bit each and a constant of 8-bit. The products are accumulated with
the 20-bit destination respectively and are packed into 40-bit destination.
Available Switches
               Number of atomic operations. An atomic operation is defined as two multiply-
Oop
               accumulate using two products operations. 1op ≤ Oop ≤ 8op

When used, the 20 LSBs of the products are taken (instead of the high parts). The
low
               default behavior is the high parts.
vmpsX          Selects the VMSNX and VPSX set within modv0 or modv2 mode registers.
Intrinsic Names
vmacwb3_v32_v32_c32_v40_low
vmacwb3_v32_v32_c32_v40_low_vmpsX
vmacwb3_v32_v32_c32_v40
vmacwb3_v32_v32_c32_v40_vmpsX
Instruction details in the instruction set specification
Intrinsic     vmacwb3_v32_v32_c32_v40_low[_p]
name
Spec syntax   vmacwb3 {Oop [,low][,vmpsX]} vx[X]p, vy[Y]p, vcWp, voz[0], ?vprX

Return type   vec40_t

              1    OOP           uint8     1..8            Number of atomic operations
              2    IN1_V32       vec_t                     Input vector operand

              3    IN1_OFST      uint8     0,4
                                                           Offset for the first DW used from operand
                                                           2

              4    IN1_PART      uint8     LOW,HIGH        Word part which is used for operand 2
              5    IN2_V32       vec_t                     Input vector operand
Operands      6    IN2_OFST      uint8     0,4             Offset for the first DW used from operand
                                                           5

              7    IN2_PART      uint8     LOW,HIGH        Word part which is used for operand 5
              8    IN3_C32       coef_t                    Coefficient operand
              9    IN3_PART      uint8     LOW,HIGH        Word part which is used for operand 8
              10   IN4_V40       vec40_t                   Output vector operand
              11   IN_VPR        vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vmacwb3_v32_v32_c32_v40_low_p (8, vIn, 0, LOW, vIn2, 0, LOW, vcoefIn, LOW, vRes,
              vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmacwb3_v32_v32_c32_v40_low_p version.


Main table → Multiplication → Multiply-Accumulate → 16x8 using Two Products into
Two Words
Intrinsic     vmacwb3_v32_v32_c32_v40_low_vmpsX[_p]
name
Spec syntax   vmacwb3 {Oop [,low][,vmpsX]} vx[X]p, vy[Y]p, vcWp, voz[0], ?vprX

Return type   vec40_t

              1    OOP           uint8     1..8            Number of atomic operations

Selects the VMSNX and VPSX set within
Operands      2    VMPSX         uint8     0,1
                                                           modv0/modv2 mode registers
              3    IN1_V32       vec_t                     Input vector operand
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
              vRes = vmacwb3_v32_v32_c32_v40_low_vmpsX_p (8, 1, vIn, 0, LOW, vIn2, 0, LOW, vcoefIn, LOW,
              vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmacwb3_v32_v32_c32_v40_low_vmpsX_p version.


Main table → Multiplication → Multiply-Accumulate → 16x8 using Two Products into
Two Words
Intrinsic     vmacwb3_v32_v32_c32_v40[_p]
name
Spec syntax   vmacwb3 {Oop [,low][,vmpsX]} vx[X]p, vy[Y]p, vcWp, voz[0], ?vprX

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
              vRes = vmacwb3_v32_v32_c32_v40_p (8, vIn, 0, LOW, vIn2, 0, LOW, vcoefIn, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for vmacwb3_v32_v32_c32_v40_p
Comments      1.
                   version.


Main table → Multiplication → Multiply-Accumulate → 16x8 using Two Products into
Two Words
Intrinsic     vmacwb3_v32_v32_c32_v40_vmpsX[_p]
name
Spec syntax   vmacwb3 {Oop [,low][,vmpsX]} vx[X]p, vy[Y]p, vcWp, voz[0], ?vprX

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
            vRes = vmacwb3_v32_v32_c32_v40_vmpsX_p (8, 1, vIn, 0, LOW, vIn2, 0, LOW, vcoefIn, LOW, vRes,
            vecPred);

                 IN_VPR last operand is relevant only for
Comments    1.
                 vmacwb3_v32_v32_c32_v40_vmpsX_p version.


Main table → Multiplication → Multiply-Accumulate → 16x8 using Two Products into
Two Words
