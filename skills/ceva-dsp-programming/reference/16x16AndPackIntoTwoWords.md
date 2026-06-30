# Multiplication → Multiply-Subtract → 16x16 and Pack into Two Words

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Multiplication → Multiply-Subtract → 16x16 and Pack into Two Words

16x16 and Pack into Two Words

16x16 and Pack into Two Words
Performs two multiply-subtract operations between two sources. Each source is 16-bit wide.
Each product is subtracted from the 20-bit destination part respectively and packed into 40-bit
destination.
Available Switches
               Number of atomic operations. An atomic operation is defined as two multiply-
Oop
               subtract operations. 1op ≤ Oop ≤ 8op
const          If used, the same vy[Y]p is used in the multiplications
vmpsX          Selects the VMSNX and VPSX set within modv0 or modv2 mode registers.
Intrinsic Names
vmsup_v32_v32_v40_const
vmsup_v32_v32_v40_const_vmpsX
vmsup_v32_v32_v40
vmsup_v32_v32_v40_vmpsX
vmsup_v32_c32_v40
vmsup_v32_c32_v40_vmpsX
Instruction details in the instruction set specification
Intrinsic     vmsup_v32_v32_v40_const[_p]
name
Spec syntax   vmsup {Oop [,const] [,vmpsX]} vx[X]p, vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             2

              4    IN1_PART       uint8     LOW,HIGH         Word part which is used for operand 2
Operands      5    IN2_V32        vec_t                      Input vector operand

              6    IN2_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             5

              7    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 5
              8    IN3_V40        vec40_t                    Output vector operand
              9    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsup_v32_v32_v40_const_p (8, vIn, 0, LOW, vIn2, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for vmsup_v32_v32_v40_const_p
Comments      1.
                   version.


Main table → Multiplication → Multiply-Subtract → 16x16 and Pack into Two Words

Intrinsic     vmsup_v32_v32_v40_const_vmpsX[_p]
name
Spec syntax   vmsup {Oop [,const] [,vmpsX]} vx[X]p, vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8             Number of atomic operations
                                                             Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                             modv0/modv2 mode registers
              3    IN1_V32        vec_t                      Input vector operand
Operands
              4    IN1_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             3

              5    IN1_PART       uint8     LOW,HIGH         Word part which is used for operand 3
              6    IN2_V32        vec_t                      Input vector operand
              7    IN2_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             6

              8    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 6
              9    IN3_V40        vec40_t                    Output vector operand
              10   IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsup_v32_v32_v40_const_vmpsX_p (8, 1, vIn, 0, LOW, vIn2, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsup_v32_v32_v40_const_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → 16x16 and Pack into Two Words
Intrinsic     vmsup_v32_v32_v40[_p]
name
Spec syntax   vmsup {Oop [,const] [,vmpsX]} vx[X]p, vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             2

              4    IN1_PART       uint8     LOW,HIGH         Word part which is used for operand 2
Operands      5    IN2_V32        vec_t                      Input vector operand

6    IN2_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             5

              7    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 5
              8    IN3_V40        vec40_t                    Output vector operand
              9    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsup_v32_v32_v40_p (8, vIn, 0, LOW, vIn2, 0, LOW, vRes, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmsup_v32_v32_v40_p version.


Main table → Multiplication → Multiply-Subtract → 16x16 and Pack into Two Words
Intrinsic     vmsup_v32_v32_v40_vmpsX[_p]
name
Spec syntax   vmsup {Oop [,const] [,vmpsX]} vx[X]p, vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8            Number of atomic operations
                                                            Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand

              4    IN1_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            3

Operands      5    IN1_PART       uint8     LOW,HIGH        Word part which is used for operand 3
              6    IN2_V32        vec_t                     Input vector operand

              7    IN2_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            6

              8    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 6
              9    IN3_V40        vec40_t                   Output vector operand
              10   IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsup_v32_v32_v40_vmpsX_p (8, 1, vIn, 0, LOW, vIn2, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for vmsup_v32_v32_v40_vmpsX_p

Comments      1.
                   version.


Main table → Multiplication → Multiply-Subtract → 16x16 and Pack into Two Words
Intrinsic     vmsup_v32_c32_v40[_p]
name
Spec syntax   vmsup {Oop [,vmpsX]} vx[X]p, vcYp, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            2

Operands
              4    IN1_PART       uint8     LOW,HIGH        Word part which is used for operand 2
              5    IN2_C32        coef_t                    Coefficient operand
              6    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 5
              7    IN3_V40        vec40_t                   Output vector operand
              8    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec40_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vmsup_v32_c32_v40_p (8, vIn, 0, LOW, vcoefIn, LOW, vRes, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmsup_v32_c32_v40_p version.


Main table → Multiplication → Multiply-Subtract → 16x16 and Pack into Two Words
Intrinsic     vmsup_v32_c32_v40_vmpsX[_p]
name
Spec syntax   vmsup {Oop [,vmpsX]} vx[X]p, vcYp, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8            Number of atomic operations
                                                            Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand

              4    IN1_OFST       uint8     0..7            Offset for the first DW used from operand
Operands                                                    3

              5    IN1_PART       uint8     LOW,HIGH        Word part which is used for operand 3
              6    IN2_C32        coef_t                    Coefficient operand
              7    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 6

8    IN3_V40        vec40_t                   Output vector operand
            9    IN_VPR         vprex_t                   Vector predicate operand
            vec_t vIn;
            vec40_t vRes;
            coef_t vcoefIn;
C example   vprex_t vecPred;
            ...
            vRes = vmsup_v32_c32_v40_vmpsX_p (8, 1, vIn, 0, LOW, vcoefIn, LOW, vRes, vecPred);

                 IN_VPR last operand is relevant only for vmsup_v32_c32_v40_vmpsX_p
Comments    1.
                 version.


Main table → Multiplication → Multiply-Subtract → 16x16 and Pack into Two Words
