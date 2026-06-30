# Multiplication → Multiply-Subtract → Complex 16x8 into Two Words

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Multiplication → Multiply-Subtract → Complex 16x8 into Two Words

Complex 16x8 into Two Words

Complex 16x8 into Two Words
Performs complex multiply-subtract between two complex numbers. The first complex source
consists of real 16-bit part and imaginary 16-bit part, and the second complex source consists of
real 8-bit part and imaginary 8-bit part. Each of the real and the imaginary products is subtracted
from the 20-bit destination respectively and packed into 40-bit destination.
Available Switches
                 Number of atomic operations. An atomic operation is defined as a single complex
Oop
                 multiply-subtract operation. 1op ≤ Oop ≤ 8op
conj             Performs complex multiply using complex conjugate of vcY/vy[Y]
const            When used, vy[Y]p is constant throughout the operations.
                 When used, the 20 LSBs of the products are taken (instead of the high parts). The
low
                 default behavior is the high parts.
vmpsX            Selects the VMSNX and VPSX set within modv0 or modv2 mode registers.
Intrinsic Names
vmsuwbx_v32_c32_v40_conj
vmsuwbx_v32_c32_v40_conj_vmpsX
vmsuwbx_v32_c32_v40_low_conj
vmsuwbx_v32_c32_v40_low_conj_vmpsX
vmsuwbx_v32_c32_v40_low

vmsuwbx_v32_c32_v40_low_vmpsX
vmsuwbx_v32_c32_v40
vmsuwbx_v32_c32_v40_vmpsX
vmsuwbx_v32_v32_v40_conj
vmsuwbx_v32_v32_v40_conj_vmpsX
vmsuwbx_v32_v32_v40_const_conj
vmsuwbx_v32_v32_v40_const_conj_vmpsX
vmsuwbx_v32_v32_v40_const
vmsuwbx_v32_v32_v40_const_vmpsX
vmsuwbx_v32_v32_v40_low_conj
vmsuwbx_v32_v32_v40_low_conj_vmpsX
vmsuwbx_v32_v32_v40_low_const_conj
vmsuwbx_v32_v32_v40_low_const_conj_vmpsX
vmsuwbx_v32_v32_v40_low_const
vmsuwbx_v32_v32_v40_low_const_vmpsX
vmsuwbx_v32_v32_v40_low
vmsuwbx_v32_v32_v40_low_vmpsX
vmsuwbx_v32_v32_v40
vmsuwbx_v32_v32_v40_vmpsX
Instruction details in the instruction set specification
Intrinsic     vmsuwbx_v32_c32_v40_conj[_p]
name
Spec syntax   vmsuwbx {Oop [,low][,conj][,vmpsX]} vx[X], vcYp, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0,4
                                                            Offset for the first DW used from operand
                                                            2
Operands      4    IN2_C32        coef_t                    Coefficient operand
              5    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 4
              6    IN3_V40        vec40_t                   Output vector operand
              7    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec40_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vmsuwbx_v32_c32_v40_conj_p (8, vIn, 0, vcoefIn, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for vmsuwbx_v32_c32_v40_conj_p
Comments      1.
                   version.


Main table → Multiplication → Multiply-Subtract → Complex 16x8 into Two Words
Intrinsic     vmsuwbx_v32_c32_v40_conj_vmpsX[_p]
name
Spec syntax   vmsuwbx {Oop [,low][,conj][,vmpsX]} vx[X], vcYp, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8            Number of atomic operations
                                                            Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand

4    IN1_OFST       uint8     0,4             Offset for the first DW used from operand
Operands                                                    3

              5    IN2_C32        coef_t                    Coefficient operand
              6    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 5
              7    IN3_V40        vec40_t                   Output vector operand
              8    IN_VPR         vprex_t                   Vector predicate operand
C example     vec_t vIn;
              vec40_t vRes;
              coef_t vcoefIn;
              vprex_t vecPred;
              ...
              vRes = vmsuwbx_v32_c32_v40_conj_vmpsX_p (8, 1, vIn, 0, vcoefIn, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsuwbx_v32_c32_v40_conj_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Complex 16x8 into Two Words
Intrinsic     vmsuwbx_v32_c32_v40_low_conj[_p]
name
Spec syntax   vmsuwbx {Oop [,low][,conj][,vmpsX]} vx[X], vcYp, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0,4
                                                            Offset for the first DW used from operand
                                                            2
Operands      4    IN2_C32        coef_t                    Coefficient operand
              5    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 4
              6    IN3_V40        vec40_t                   Output vector operand
              7    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec40_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vmsuwbx_v32_c32_v40_low_conj_p (8, vIn, 0, vcoefIn, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsuwbx_v32_c32_v40_low_conj_p version.


Main table → Multiplication → Multiply-Subtract → Complex 16x8 into Two Words
Intrinsic     vmsuwbx_v32_c32_v40_low_conj_vmpsX[_p]
name
Spec syntax   vmsuwbx {Oop [,low][,conj][,vmpsX]} vx[X], vcYp, voz[0], ?vprX

Return type   vec40_t

1    OOP            uint8     1..8            Number of atomic operations
                                                            Selects the VMSNX and VPSX set within
Operands      2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand
              4    IN1_OFST       uint8     0,4             Offset for the first DW used from operand
                                                            3

              5    IN2_C32        coef_t                    Coefficient operand
              6    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 5
              7    IN3_V40        vec40_t                   Output vector operand
              8    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec40_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vmsuwbx_v32_c32_v40_low_conj_vmpsX_p (8, 1, vIn, 0, vcoefIn, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsuwbx_v32_c32_v40_low_conj_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Complex 16x8 into Two Words
Intrinsic     vmsuwbx_v32_c32_v40_low[_p]
name
Spec syntax   vmsuwbx {Oop [,low][,conj][,vmpsX]} vx[X], vcYp, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0,4             Offset for the first DW used from operand
                                                            2
Operands      4    IN2_C32        coef_t                    Coefficient operand
              5    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 4
              6    IN3_V40        vec40_t                   Output vector operand
              7    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec40_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vmsuwbx_v32_c32_v40_low_p (8, vIn, 0, vcoefIn, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for vmsuwbx_v32_c32_v40_low_p

Comments      1.
                   version.


Main table → Multiplication → Multiply-Subtract → Complex 16x8 into Two Words
Intrinsic     vmsuwbx_v32_c32_v40_low_vmpsX[_p]
name
Spec syntax   vmsuwbx {Oop [,low][,conj][,vmpsX]} vx[X], vcYp, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8            Number of atomic operations
                                                            Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand

              4    IN1_OFST       uint8     0,4
                                                            Offset for the first DW used from operand
Operands                                                    3

              5    IN2_C32        coef_t                    Coefficient operand
              6    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 5
              7    IN3_V40        vec40_t                   Output vector operand
              8    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec40_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vmsuwbx_v32_c32_v40_low_vmpsX_p (8, 1, vIn, 0, vcoefIn, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsuwbx_v32_c32_v40_low_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Complex 16x8 into Two Words
Intrinsic     vmsuwbx_v32_c32_v40[_p]
name
Spec syntax   vmsuwbx {Oop [,low][,conj][,vmpsX]} vx[X], vcYp, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0,4             Offset for the first DW used from operand
                                                            2
Operands      4    IN2_C32        coef_t                    Coefficient operand
              5    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 4
              6    IN3_V40        vec40_t                   Output vector operand

7    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec40_t vRes;
C example     coef_t vcoefIn;
              vprex_t vecPred;
              ...
              vRes = vmsuwbx_v32_c32_v40_p (8, vIn, 0, vcoefIn, LOW, vRes, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmsuwbx_v32_c32_v40_p version.


Main table → Multiplication → Multiply-Subtract → Complex 16x8 into Two Words
Intrinsic     vmsuwbx_v32_c32_v40_vmpsX[_p]
name
Spec syntax   vmsuwbx {Oop [,low][,conj][,vmpsX]} vx[X], vcYp, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8             Number of atomic operations
                                                             Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                             modv0/modv2 mode registers
              3    IN1_V32        vec_t                      Input vector operand

              4    IN1_OFST       uint8     0,4
                                                             Offset for the first DW used from operand
Operands                                                     3

              5    IN2_C32        coef_t                     Coefficient operand
              6    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 5
              7    IN3_V40        vec40_t                    Output vector operand
              8    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec40_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vmsuwbx_v32_c32_v40_vmpsX_p (8, 1, vIn, 0, vcoefIn, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for vmsuwbx_v32_c32_v40_vmpsX_p
Comments      1.
                   version.


Main table → Multiplication → Multiply-Subtract → Complex 16x8 into Two Words
Intrinsic     vmsuwbx_v32_v32_v40_conj[_p]
name
Spec syntax   vmsuwbx {Oop [,low][,const][,conj][,vmpsX]} vx[X], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0,4

Offset for the first DW used from operand
                                                             2

              4    IN2_V32        vec_t                      Input vector operand
Operands
              5    IN2_OFST       uint8     0,4
                                                             Offset for the first DW used from operand
                                                             4

              6    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 4
              7    IN3_V40        vec40_t                    Output vector operand
              8    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsuwbx_v32_v32_v40_conj_p (8, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for vmsuwbx_v32_v32_v40_conj_p
Comments      1.
                   version.


Main table → Multiplication → Multiply-Subtract → Complex 16x8 into Two Words
Intrinsic     vmsuwbx_v32_v32_v40_conj_vmpsX[_p]
name
Spec syntax   vmsuwbx {Oop [,low][,const][,conj][,vmpsX]} vx[X], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8             Number of atomic operations
                                                             Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                             modv0/modv2 mode registers
              3    IN1_V32        vec_t                      Input vector operand

Operands      4    IN1_OFST       uint8     0,4              Offset for the first DW used from operand
                                                             3

              5    IN2_V32        vec_t                      Input vector operand

              6    IN2_OFST       uint8     0,4              Offset for the first DW used from operand
                                                             5

              7    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 5
              8    IN3_V40        vec40_t                    Output vector operand
              9    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...

vRes = vmsuwbx_v32_v32_v40_conj_vmpsX_p (8, 1, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsuwbx_v32_v32_v40_conj_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Complex 16x8 into Two Words
Intrinsic     vmsuwbx_v32_v32_v40_const_conj[_p]
name
Spec syntax   vmsuwbx {Oop [,low][,const][,conj][,vmpsX]} vx[X], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0,4
                                                             Offset for the first DW used from operand
                                                             2

              4    IN2_V32        vec_t                      Input vector operand
Operands
              5    IN2_OFST       uint8     0,4              Offset for the first DW used from operand
                                                             4

              6    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 4
              7    IN3_V40        vec40_t                    Output vector operand
              8    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsuwbx_v32_v32_v40_const_conj_p (8, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsuwbx_v32_v32_v40_const_conj_p version.


Main table → Multiplication → Multiply-Subtract → Complex 16x8 into Two Words
Intrinsic     vmsuwbx_v32_v32_v40_const_conj_vmpsX[_p]
name
Spec syntax   vmsuwbx {Oop [,low][,const][,conj][,vmpsX]} vx[X], vy[Y]p, voz[0], ?vprX

Return type   vec40_t
              1    OOP            uint8     1..8            Number of atomic operations
                                                            Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand

              4    IN1_OFST       uint8     0,4

Offset for the first DW used from operand
                                                            3
Operands      5    IN2_V32        vec_t                     Input vector operand

              6    IN2_OFST       uint8     0,4
                                                            Offset for the first DW used from operand
                                                            5

              7    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 5
              8    IN3_V40        vec40_t                   Output vector operand
              9    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsuwbx_v32_v32_v40_const_conj_vmpsX_p (8, 1, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsuwbx_v32_v32_v40_const_conj_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Complex 16x8 into Two Words
Intrinsic     vmsuwbx_v32_v32_v40_const[_p]
name
Spec syntax   vmsuwbx {Oop [,low][,const][,conj][,vmpsX]} vx[X], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0,4
                                                            Offset for the first DW used from operand
                                                            2

              4    IN2_V32        vec_t                     Input vector operand
Operands
              5    IN2_OFST       uint8     0,4
                                                            Offset for the first DW used from operand
                                                            4

              6    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 4
              7    IN3_V40        vec40_t                   Output vector operand
              8    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
C example     vec_t vIn2;
              vec40_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmsuwbx_v32_v32_v40_const_p (8, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

IN_VPR last operand is relevant only for vmsuwbx_v32_v32_v40_const_p
Comments      1.
                   version.


Main table → Multiplication → Multiply-Subtract → Complex 16x8 into Two Words
Intrinsic     vmsuwbx_v32_v32_v40_const_vmpsX[_p]
name
Spec syntax   vmsuwbx {Oop [,low][,const][,conj][,vmpsX]} vx[X], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8             Number of atomic operations
                                                             Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                             modv0/modv2 mode registers
              3    IN1_V32        vec_t                      Input vector operand

              4    IN1_OFST       uint8     0,4              Offset for the first DW used from operand
                                                             3
Operands      5    IN2_V32        vec_t                      Input vector operand

              6    IN2_OFST       uint8     0,4              Offset for the first DW used from operand
                                                             5

              7    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 5
              8    IN3_V40        vec40_t                    Output vector operand
              9    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsuwbx_v32_v32_v40_const_vmpsX_p (8, 1, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsuwbx_v32_v32_v40_const_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Complex 16x8 into Two Words
Intrinsic     vmsuwbx_v32_v32_v40_low_conj[_p]
name
Spec syntax   vmsuwbx {Oop [,low][,const][,conj][,vmpsX]} vx[X], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

Operands      1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0,4             Offset for the first DW used from operand
                                                            2

              4    IN2_V32        vec_t                     Input vector operand

5    IN2_OFST       uint8     0,4             Offset for the first DW used from operand
                                                            4

              6    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 4
              7    IN3_V40        vec40_t                   Output vector operand
              8    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsuwbx_v32_v32_v40_low_conj_p (8, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsuwbx_v32_v32_v40_low_conj_p version.


Main table → Multiplication → Multiply-Subtract → Complex 16x8 into Two Words
Intrinsic     vmsuwbx_v32_v32_v40_low_conj_vmpsX[_p]
name
Spec syntax   vmsuwbx {Oop [,low][,const][,conj][,vmpsX]} vx[X], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8            Number of atomic operations
                                                            Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand

              4    IN1_OFST       uint8     0,4             Offset for the first DW used from operand
                                                            3
Operands      5    IN2_V32        vec_t                     Input vector operand

              6    IN2_OFST       uint8     0,4
                                                            Offset for the first DW used from operand
                                                            5

              7    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 5
              8    IN3_V40        vec40_t                   Output vector operand
              9    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
C example     vec40_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmsuwbx_v32_v32_v40_low_conj_vmpsX_p (8, 1, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.

vmsuwbx_v32_v32_v40_low_conj_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Complex 16x8 into Two Words
Intrinsic     vmsuwbx_v32_v32_v40_low_const_conj[_p]
name
Spec syntax   vmsuwbx {Oop [,low][,const][,conj][,vmpsX]} vx[X], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0,4
                                                            Offset for the first DW used from operand
                                                            2

              4    IN2_V32        vec_t                     Input vector operand
Operands
              5    IN2_OFST       uint8     0,4
                                                            Offset for the first DW used from operand
                                                            4

              6    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 4
              7    IN3_V40        vec40_t                   Output vector operand
              8    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsuwbx_v32_v32_v40_low_const_conj_p (8, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsuwbx_v32_v32_v40_low_const_conj_p version.


Main table → Multiplication → Multiply-Subtract → Complex 16x8 into Two Words
Intrinsic     vmsuwbx_v32_v32_v40_low_const_conj_vmpsX[_p]
name
Spec syntax   vmsuwbx {Oop [,low][,const][,conj][,vmpsX]} vx[X], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8            Number of atomic operations
                                                            Selects the VMSNX and VPSX set within
Operands      2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand
              4    IN1_OFST       uint8     0,4              Offset for the first DW used from operand
                                                             3

5    IN2_V32        vec_t                      Input vector operand

              6    IN2_OFST       uint8     0,4              Offset for the first DW used from operand
                                                             5

              7    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 5
              8    IN3_V40        vec40_t                    Output vector operand
              9    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsuwbx_v32_v32_v40_low_const_conj_vmpsX_p (8, 1, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsuwbx_v32_v32_v40_low_const_conj_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Complex 16x8 into Two Words
Intrinsic     vmsuwbx_v32_v32_v40_low_const[_p]
name
Spec syntax   vmsuwbx {Oop [,low][,const][,conj][,vmpsX]} vx[X], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0,4              Offset for the first DW used from operand
                                                             2

              4    IN2_V32        vec_t                      Input vector operand
Operands
              5    IN2_OFST       uint8     0,4              Offset for the first DW used from operand
                                                             4

              6    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 4
              7    IN3_V40        vec40_t                    Output vector operand
              8    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsuwbx_v32_v32_v40_low_const_p (8, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsuwbx_v32_v32_v40_low_const_p version.

Main table → Multiplication → Multiply-Subtract → Complex 16x8 into Two Words
Intrinsic     vmsuwbx_v32_v32_v40_low_const_vmpsX[_p]
name

Spec syntax   vmsuwbx {Oop [,low][,const][,conj][,vmpsX]} vx[X], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8            Number of atomic operations
                                                            Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand

              4    IN1_OFST       uint8     0,4             Offset for the first DW used from operand
                                                            3
Operands      5    IN2_V32        vec_t                     Input vector operand

              6    IN2_OFST       uint8     0,4             Offset for the first DW used from operand
                                                            5

              7    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 5
              8    IN3_V40        vec40_t                   Output vector operand
              9    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsuwbx_v32_v32_v40_low_const_vmpsX_p (8, 1, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsuwbx_v32_v32_v40_low_const_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Complex 16x8 into Two Words
Intrinsic     vmsuwbx_v32_v32_v40_low[_p]
name
Spec syntax   vmsuwbx {Oop [,low][,const][,conj][,vmpsX]} vx[X], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

Operands      3    IN1_OFST       uint8     0,4             Offset for the first DW used from operand
                                                            2

              4    IN2_V32        vec_t                     Input vector operand
              5    IN2_OFST       uint8     0,4             Offset for the first DW used from operand
                                                             4

              6    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 4

7    IN3_V40        vec40_t                    Output vector operand
              8    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsuwbx_v32_v32_v40_low_p (8, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for vmsuwbx_v32_v32_v40_low_p
Comments      1.
                   version.


Main table → Multiplication → Multiply-Subtract → Complex 16x8 into Two Words
Intrinsic     vmsuwbx_v32_v32_v40_low_vmpsX[_p]
name
Spec syntax   vmsuwbx {Oop [,low][,const][,conj][,vmpsX]} vx[X], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8             Number of atomic operations
                                                             Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                             modv0/modv2 mode registers
              3    IN1_V32        vec_t                      Input vector operand

              4    IN1_OFST       uint8     0,4              Offset for the first DW used from operand
                                                             3
Operands      5    IN2_V32        vec_t                      Input vector operand

              6    IN2_OFST       uint8     0,4              Offset for the first DW used from operand
                                                             5

              7    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 5
              8    IN3_V40        vec40_t                    Output vector operand
              9    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsuwbx_v32_v32_v40_low_vmpsX_p (8, 1, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsuwbx_v32_v32_v40_low_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Complex 16x8 into Two Words
Intrinsic     vmsuwbx_v32_v32_v40[_p]
name
Spec syntax   vmsuwbx {Oop [,low][,const][,conj][,vmpsX]} vx[X], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0,4
                                                             Offset for the first DW used from operand
                                                             2

              4    IN2_V32        vec_t                      Input vector operand
Operands
              5    IN2_OFST       uint8     0,4
                                                             Offset for the first DW used from operand
                                                             4

              6    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 4
              7    IN3_V40        vec40_t                    Output vector operand
              8    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsuwbx_v32_v32_v40_p (8, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmsuwbx_v32_v32_v40_p version.


Main table → Multiplication → Multiply-Subtract → Complex 16x8 into Two Words
Intrinsic     vmsuwbx_v32_v32_v40_vmpsX[_p]
name
Spec syntax   vmsuwbx {Oop [,low][,const][,conj][,vmpsX]} vx[X], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8             Number of atomic operations
                                                             Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                             modv0/modv2 mode registers
              3    IN1_V32        vec_t                      Input vector operand

Operands      4    IN1_OFST       uint8     0,4              Offset for the first DW used from operand
                                                             3

              5    IN2_V32        vec_t                      Input vector operand

              6    IN2_OFST       uint8     0,4              Offset for the first DW used from operand
                                                             5

              7    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 5
            8    IN3_V40        vec40_t                   Output vector operand

9    IN_VPR         vprex_t                   Vector predicate operand
            vec_t vIn;
            vec_t vIn2;
            vec40_t vRes;
C example   vprex_t vecPred;
            ...
            vRes = vmsuwbx_v32_v32_v40_vmpsX_p (8, 1, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

                 IN_VPR last operand is relevant only for vmsuwbx_v32_v32_v40_vmpsX_p
Comments    1.
                 version.


Main table → Multiplication → Multiply-Subtract → Complex 16x8 into Two Words
