# Multiplication → Multiply-Subtract → Semi-Complex 16x16

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Multiplication → Multiply-Subtract → Semi-Complex 16x16

Semi-Complex 16x16

Semi-Complex 16x16
Performs complex by real multipliy-subtract between a complex number and a real number. The

complex source consists of real 16-bit part and imaginary 16-bit part, the real number source
consists of 16-bit. Each of the real and the imaginary products are subtracted from the 40-bit
destination respectively.
Available Switches
                 Number of atomic operations. An atomic operation is defined as a single multiply-
Ohop
                 subtract operation. 5op ≤ Ohop ≤ 8op
                 Number of atomic operations. An atomic operation is defined as pair of multiply-
Qop
                 subtract operation. 1op ≤ Qop ≤ 4op.
conj             Performs complex multiply-accumulate using complex conjugate of vx[X]
const            When used, vy[Y]p is constant throughout the operations.
vmpsX            Selects the VMSNX and VPSX set within modv0 or modv2 mode registers.
Intrinsic Names
vmsuxr_v32_c32_v40_conj
vmsuxr_v32_c32_v40_conj_vmpsX
vmsuxr_v32_c32_v40
vmsuxr_v32_c32_v40_vmpsX
vmsuxr_v32_v32_v40_conj
vmsuxr_v32_v32_v40_conj_vmpsX
vmsuxr_v32_v32_v40_const_conj
vmsuxr_v32_v32_v40_const_conj_vmpsX
vmsuxr_v32_v32_v40_const
vmsuxr_v32_v32_v40_const_vmpsX
vmsuxr_v32_v32_v40
vmsuxr_v32_v32_v40_vmpsX
vmsuxr_v32_v32_v40_v40_conj
vmsuxr_v32_v32_v40_v40_conj_vmpsX
vmsuxr_v32_v32_v40_v40_const_conj
vmsuxr_v32_v32_v40_v40_const_conj_vmpsX
vmsuxr_v32_v32_v40_v40_const
vmsuxr_v32_v32_v40_v40_const_vmpsX
vmsuxr_v32_v32_v40_v40
vmsuxr_v32_v32_v40_v40_vmpsX
vmsuxr_v32_c32_v40_v40_conj
vmsuxr_v32_c32_v40_v40_conj_vmpsX
vmsuxr_v32_c32_v40_v40
vmsuxr_v32_c32_v40_v40_vmpsX
Instruction details in the instruction set specification
Intrinsic     vmsuxr_v32_c32_v40_conj[_p]
name
Spec syntax   vmsuxr {Qop [,conj][,vmpsX]} vx[X], vcYp, voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             2
Operands      4    IN2_C32        coef_t                     Coefficient operand
              5    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 4
              6    IN3_V40        vec40_t                    Output vector operand
              7    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec40_t vRes;

coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vmsuxr_v32_c32_v40_conj_p (4, vIn, 0, vcoefIn, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for vmsuxr_v32_c32_v40_conj_p
Comments      1.
                   version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 16x16
Intrinsic     vmsuxr_v32_c32_v40_conj_vmpsX[_p]
name
Spec syntax   vmsuxr {Qop [,conj][,vmpsX]} vx[X], vcYp, voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4             Number of atomic operations
                                                             Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                             modv0/modv2 mode registers
              3    IN1_V32        vec_t                      Input vector operand

              4    IN1_OFST       uint8     0..7             Offset for the first DW used from operand
Operands                                                     3

              5    IN2_C32        coef_t                     Coefficient operand
              6    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 5
              7    IN3_V40        vec40_t                    Output vector operand
              8    IN_VPR         vprex_t                    Vector predicate operand
C example     vec_t vIn;
              vec40_t vRes;
              coef_t vcoefIn;
              vprex_t vecPred;
              ...
              vRes = vmsuxr_v32_c32_v40_conj_vmpsX_p (4, 1, vIn, 0, vcoefIn, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsuxr_v32_c32_v40_conj_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 16x16
Intrinsic     vmsuxr_v32_c32_v40[_p]
name
Spec syntax   vmsuxr {Qop [,conj][,vmpsX]} vx[X], vcYp, voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             2
Operands      4    IN2_C32        coef_t                     Coefficient operand

5    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 4
              6    IN3_V40        vec40_t                    Output vector operand
              7    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec40_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vmsuxr_v32_c32_v40_p (4, vIn, 0, vcoefIn, LOW, vRes, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmsuxr_v32_c32_v40_p version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 16x16
Intrinsic     vmsuxr_v32_c32_v40_vmpsX[_p]
name
Spec syntax   vmsuxr {Qop [,conj][,vmpsX]} vx[X], vcYp, voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4             Number of atomic operations
                                                             Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
Operands                                                     modv0/modv2 mode registers
              3    IN1_V32        vec_t                      Input vector operand
              4    IN1_OFST       uint8     0..7             Offset for the first DW used from operand
                                                           3

            5    IN2_C32        coef_t                     Coefficient operand
            6    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 5
            7    IN3_V40        vec40_t                    Output vector operand
            8    IN_VPR         vprex_t                    Vector predicate operand
            vec_t vIn;
            vec40_t vRes;
            coef_t vcoefIn;
C example   vprex_t vecPred;
            ...
            vRes = vmsuxr_v32_c32_v40_vmpsX_p (4, 1, vIn, 0, vcoefIn, LOW, vRes, vecPred);

                 IN_VPR last operand is relevant only for vmsuxr_v32_c32_v40_vmpsX_p
Comments    1.
                 version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 16x16
Intrinsic     vmsuxr_v32_v32_v40_conj[_p]
name
Spec syntax   vmsuxr {Qop [,const][,conj][,vmpsX]} vx[X], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0..7

Offset for the first DW used from operand
                                                             2

              4    IN2_V32        vec_t                      Input vector operand
Operands
              5    IN2_OFST       uint8     0..7
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
              vRes = vmsuxr_v32_v32_v40_conj_p (4, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for vmsuxr_v32_v32_v40_conj_p
Comments      1.
                   version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 16x16
Intrinsic     vmsuxr_v32_v32_v40_conj_vmpsX[_p]
name
Spec syntax   vmsuxr {Qop [,const][,conj][,vmpsX]} vx[X], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4             Number of atomic operations
                                                             Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                             modv0/modv2 mode registers
              3    IN1_V32        vec_t                      Input vector operand

Operands      4    IN1_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             3

              5    IN2_V32        vec_t                      Input vector operand

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

vRes = vmsuxr_v32_v32_v40_conj_vmpsX_p (4, 1, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsuxr_v32_v32_v40_conj_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 16x16
Intrinsic     vmsuxr_v32_v32_v40_const_conj[_p]
name
Spec syntax   vmsuxr {Qop [,const][,conj][,vmpsX]} vx[X], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             2

              4    IN2_V32        vec_t                      Input vector operand
Operands
              5    IN2_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             4

              6    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 4
              7    IN3_V40        vec40_t                    Output vector operand
              8    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsuxr_v32_v32_v40_const_conj_p (4, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsuxr_v32_v32_v40_const_conj_p version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 16x16
Intrinsic     vmsuxr_v32_v32_v40_const_conj_vmpsX[_p]
name
Spec syntax   vmsuxr {Qop [,const][,conj][,vmpsX]} vx[X], vy[Y]p, voz[0], ?vprX

Return type   vec40_t
              1    QOP            uint8     1..4             Number of atomic operations
                                                             Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                             modv0/modv2 mode registers
              3    IN1_V32        vec_t                      Input vector operand

              4    IN1_OFST       uint8     0..7

Offset for the first DW used from operand
                                                             3
Operands      5    IN2_V32        vec_t                      Input vector operand

              6    IN2_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             5

              7    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 5
              8    IN3_V40        vec40_t                    Output vector operand
              9    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsuxr_v32_v32_v40_const_conj_vmpsX_p (4, 1, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsuxr_v32_v32_v40_const_conj_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 16x16
Intrinsic     vmsuxr_v32_v32_v40_const[_p]
name
Spec syntax   vmsuxr {Qop [,const][,conj][,vmpsX]} vx[X], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             2

              4    IN2_V32        vec_t                      Input vector operand
Operands
              5    IN2_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             4

              6    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 4
              7    IN3_V40        vec40_t                    Output vector operand
              8    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
C example     vec_t vIn2;
              vec40_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmsuxr_v32_v32_v40_const_p (4, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

IN_VPR last operand is relevant only for vmsuxr_v32_v32_v40_const_p
Comments      1.
                   version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 16x16
Intrinsic     vmsuxr_v32_v32_v40_const_vmpsX[_p]
name
Spec syntax   vmsuxr {Qop [,const][,conj][,vmpsX]} vx[X], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4             Number of atomic operations
                                                             Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                             modv0/modv2 mode registers
              3    IN1_V32        vec_t                      Input vector operand

              4    IN1_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             3
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
              vRes = vmsuxr_v32_v32_v40_const_vmpsX_p (4, 1, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsuxr_v32_v32_v40_const_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 16x16
Intrinsic     vmsuxr_v32_v32_v40[_p]
name
Spec syntax   vmsuxr {Qop [,const][,conj][,vmpsX]} vx[X], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

Operands      1    QOP            uint8     1..4             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8      0..7            Offset for the first DW used from operand
                                                             2

              4    IN2_V32        vec_t                      Input vector operand

5    IN2_OFST       uint8      0..7            Offset for the first DW used from operand
                                                             4

              6    IN2_PART       uint8      LOW,HIGH        Word part which is used for operand 4
              7    IN3_V40        vec40_t                    Output vector operand
              8    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsuxr_v32_v32_v40_p (4, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmsuxr_v32_v32_v40_p version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 16x16
Intrinsic     vmsuxr_v32_v32_v40_vmpsX[_p]
name
Spec syntax   vmsuxr {Qop [,const][,conj][,vmpsX]} vx[X], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8      1..4            Number of atomic operations
                                                             Selects the VMSNX and VPSX set within
              2    VMPSX          uint8      0,1
                                                             modv0/modv2 mode registers
              3    IN1_V32        vec_t                      Input vector operand

              4    IN1_OFST       uint8      0..7            Offset for the first DW used from operand
                                                             3
Operands      5    IN2_V32        vec_t                      Input vector operand

              6    IN2_OFST       uint8      0..7
                                                             Offset for the first DW used from operand
                                                             5

              7    IN2_PART       uint8      LOW,HIGH        Word part which is used for operand 5
              8    IN3_V40        vec40_t                    Output vector operand
              9    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsuxr_v32_v32_v40_vmpsX_p (4, 1, vIn, 0, vIn2, 0, LOW, vRes, vecPred);
                 IN_VPR last operand is relevant only for vmsuxr_v32_v32_v40_vmpsX_p
Comments    1.
                 version.

Main table → Multiplication → Multiply-Subtract → Semi-Complex 16x16
Intrinsic     vmsuxr_v32_v32_v40_v40_conj[_p]
name
Spec syntax   vmsuxr {Ohop [,const][,conj][,vmpsX]} vx[X], vy[Y]p, voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    OHOP           uint8     5..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             2

              4    IN2_V32        vec_t                      Input vector operand
Operands      5    IN2_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             4

              6    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 4
              7    IN3_V40        vec40_t                    Output vector operand
              8    IN4_V40        vec40_t                    Output vector operand
              9    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes1;
C example     vec40_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vmsuxr_v32_v32_v40_v40_conj_p (8, vIn, 0, vIn2, 0, LOW, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for vmsuxr_v32_v32_v40_v40_conj_p
Comments      1.
                   version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 16x16
Intrinsic     vmsuxr_v32_v32_v40_v40_conj_vmpsX[_p]
name
Spec syntax   vmsuxr {Ohop [,const][,conj][,vmpsX]} vx[X], vy[Y]p, voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    OHOP           uint8     5..8             Number of atomic operations
                                                             Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                             modv0/modv2 mode registers
              3    IN1_V32        vec_t                      Input vector operand
Operands
              4    IN1_OFST       uint8     0..7
                                                             Offset for the first DW used from operand

3

              5    IN2_V32        vec_t                      Input vector operand
              6    IN2_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             5

              7    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 5
              8    IN3_V40        vec40_t                    Output vector operand
              9    IN4_V40        vec40_t                    Output vector operand
              10   IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes1;
C example     vec40_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vmsuxr_v32_v32_v40_v40_conj_vmpsX_p (8, 1, vIn, 0, vIn2, 0, LOW, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsuxr_v32_v32_v40_v40_conj_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 16x16
Intrinsic     vmsuxr_v32_v32_v40_v40_const_conj[_p]
name
Spec syntax   vmsuxr {Ohop [,const][,conj][,vmpsX]} vx[X], vy[Y]p, voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    OHOP           uint8     5..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             2

              4    IN2_V32        vec_t                      Input vector operand
Operands      5    IN2_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             4

              6    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 4
              7    IN3_V40        vec40_t                    Output vector operand
              8    IN4_V40        vec40_t                    Output vector operand
              9    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes1;
C example     vec40_t vRes2;
              vprex_t vecPred;
              ...

vRes1 = vmsuxr_v32_v32_v40_v40_const_conj_p (8, vIn, 0, vIn2, 0, LOW, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsuxr_v32_v32_v40_v40_const_conj_p version.

Main table → Multiplication → Multiply-Subtract → Semi-Complex 16x16
Intrinsic     vmsuxr_v32_v32_v40_v40_const_conj_vmpsX[_p]
name
Spec syntax   vmsuxr {Ohop [,const][,conj][,vmpsX]} vx[X], vy[Y]p, voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    OHOP           uint8     5..8            Number of atomic operations
                                                            Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand

              4    IN1_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            3

Operands      5    IN2_V32        vec_t                     Input vector operand

              6    IN2_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            5

              7    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 5
              8    IN3_V40        vec40_t                   Output vector operand
              9    IN4_V40        vec40_t                   Output vector operand
              10   IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes1;
              vec40_t vRes2;
C example     vprex_t vecPred;
              ...
              vRes1 = vmsuxr_v32_v32_v40_v40_const_conj_vmpsX_p (8, 1, vIn, 0, vIn2, 0, LOW, vRes1, vRes2,
              vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsuxr_v32_v32_v40_v40_const_conj_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 16x16
Intrinsic     vmsuxr_v32_v32_v40_v40_const[_p]
name
Spec syntax   vmsuxr {Ohop [,const][,conj][,vmpsX]} vx[X], vy[Y]p, voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    OHOP           uint8     5..8            Number of atomic operations

Operands
              2    IN1_V32        vec_t                     Input vector operand

3    IN1_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            2
              4    IN2_V32        vec_t                      Input vector operand

              5    IN2_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             4

              6    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 4
              7    IN3_V40        vec40_t                    Output vector operand
              8    IN4_V40        vec40_t                    Output vector operand
              9    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes1;
C example     vec40_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vmsuxr_v32_v32_v40_v40_const_p (8, vIn, 0, vIn2, 0, LOW, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for vmsuxr_v32_v32_v40_v40_const_p
Comments      1.
                   version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 16x16
Intrinsic     vmsuxr_v32_v32_v40_v40_const_vmpsX[_p]
name
Spec syntax   vmsuxr {Ohop [,const][,conj][,vmpsX]} vx[X], vy[Y]p, voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    OHOP           uint8     5..8             Number of atomic operations
                                                             Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                             modv0/modv2 mode registers
              3    IN1_V32        vec_t                      Input vector operand

              4    IN1_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             3

Operands      5    IN2_V32        vec_t                      Input vector operand

              6    IN2_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             5

              7    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 5
              8    IN3_V40        vec40_t                    Output vector operand

9    IN4_V40        vec40_t                    Output vector operand
              10   IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
C example     vec40_t vRes1;
              vec40_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vmsuxr_v32_v32_v40_v40_const_vmpsX_p (8, 1, vIn, 0, vIn2, 0, LOW, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsuxr_v32_v32_v40_v40_const_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 16x16
Intrinsic     vmsuxr_v32_v32_v40_v40[_p]
name
Spec syntax   vmsuxr {Ohop [,const][,conj][,vmpsX]} vx[X], vy[Y]p, voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    OHOP           uint8     5..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             2

              4    IN2_V32        vec_t                      Input vector operand
Operands      5    IN2_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             4

              6    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 4
              7    IN3_V40        vec40_t                    Output vector operand
              8    IN4_V40        vec40_t                    Output vector operand
              9    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes1;
C example     vec40_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vmsuxr_v32_v32_v40_v40_p (8, vIn, 0, vIn2, 0, LOW, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for vmsuxr_v32_v32_v40_v40_p
Comments      1.
                   version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 16x16
Intrinsic     vmsuxr_v32_v32_v40_v40_vmpsX[_p]
name
Spec syntax   vmsuxr {Ohop [,const][,conj][,vmpsX]} vx[X], vy[Y]p, voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    OHOP           uint8     5..8             Number of atomic operations
Operands

2    VMPSX          uint8     0,1              Selects the VMSNX and VPSX set within
                                                          modv0/modv2 mode registers
            3    IN1_V32        vec_t                     Input vector operand

            4    IN1_OFST       uint8     0..7            Offset for the first DW used from operand
                                                          3

            5    IN2_V32        vec_t                     Input vector operand

            6    IN2_OFST       uint8     0..7
                                                          Offset for the first DW used from operand
                                                          5

            7    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 5
            8    IN3_V40        vec40_t                   Output vector operand
            9    IN4_V40        vec40_t                   Output vector operand
            10   IN_VPR         vprex_t                   Vector predicate operand
            vec_t vIn;
            vec_t vIn2;
            vec40_t vRes1;
C example   vec40_t vRes2;
            vprex_t vecPred;
            ...
            vRes1 = vmsuxr_v32_v32_v40_v40_vmpsX_p (8, 1, vIn, 0, vIn2, 0, LOW, vRes1, vRes2, vecPred);

                 IN_VPR last operand is relevant only for
Comments    1.
                 vmsuxr_v32_v32_v40_v40_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 16x16
Intrinsic     vmsuxr_v32_c32_v40_v40_conj[_p]
name
Spec syntax   vmsuxr {Ohop [,conj][,vmpsX]} vx[X], vcYp, voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    OHOP           uint8     5..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             2

Operands
              4    IN2_C32        coef_t                     Coefficient operand
              5    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 4
              6    IN3_V40        vec40_t                    Output vector operand
              7    IN4_V40        vec40_t                    Output vector operand
              8    IN_VPR         vprex_t                    Vector predicate operand

vec_t vIn;
              vec40_t vRes1;
              vec40_t vRes2;
C example     coef_t vcoefIn;
              vprex_t vecPred;
              ...
              vRes1 = vmsuxr_v32_c32_v40_v40_conj_p (8, vIn, 0, vcoefIn, LOW, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for vmsuxr_v32_c32_v40_v40_conj_p
Comments      1.
                   version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 16x16
Intrinsic     vmsuxr_v32_c32_v40_v40_conj_vmpsX[_p]
name
Spec syntax   vmsuxr {Ohop [,conj][,vmpsX]} vx[X], vcYp, voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    OHOP           uint8     5..8             Number of atomic operations
                                                             Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                             modv0/modv2 mode registers
              3    IN1_V32        vec_t                      Input vector operand
Operands      4    IN1_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             3

              5    IN2_C32        coef_t                     Coefficient operand
              6    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 5
              7    IN3_V40        vec40_t                    Output vector operand
              8    IN4_V40        vec40_t                    Output vector operand
              9    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec40_t vRes1;
              vec40_t vRes2;
C example     coef_t vcoefIn;
              vprex_t vecPred;
              ...
              vRes1 = vmsuxr_v32_c32_v40_v40_conj_vmpsX_p (8, 1, vIn, 0, vcoefIn, LOW, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsuxr_v32_c32_v40_v40_conj_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 16x16
Intrinsic     vmsuxr_v32_c32_v40_v40[_p]
name
Spec syntax   vmsuxr {Ohop [,conj][,vmpsX]} vx[X], vcYp, voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    OHOP           uint8     5..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0..7

Offset for the first DW used from operand
                                                             2

Operands
              4    IN2_C32        coef_t                     Coefficient operand
              5    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 4
              6    IN3_V40        vec40_t                    Output vector operand
              7    IN4_V40        vec40_t                    Output vector operand
              8    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec40_t vRes1;
              vec40_t vRes2;
C example     coef_t vcoefIn;
              vprex_t vecPred;
              ...
              vRes1 = vmsuxr_v32_c32_v40_v40_p (8, vIn, 0, vcoefIn, LOW, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for vmsuxr_v32_c32_v40_v40_p
Comments      1.
                   version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 16x16
Intrinsic     vmsuxr_v32_c32_v40_v40_vmpsX[_p]
name
Spec syntax   vmsuxr {Ohop [,conj][,vmpsX]} vx[X], vcYp, voz1[0], voz2[0], ?vprX
Return type   vec40_t

              1    OHOP           uint8     5..8            Number of atomic operations

              2
                                                            Selects the VMSNX and VPSX set within
                   VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand

              4    IN1_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            3
Operands
              5    IN2_C32        coef_t                    Coefficient operand
              6    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 5
              7    IN3_V40        vec40_t                   Output vector operand
              8    IN4_V40        vec40_t                   Output vector operand
              9    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec40_t vRes1;
              vec40_t vRes2;
C example     coef_t vcoefIn;
              vprex_t vecPred;
              ...

vRes1 = vmsuxr_v32_c32_v40_v40_vmpsX_p (8, 1, vIn, 0, vcoefIn, LOW, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsuxr_v32_c32_v40_v40_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 16x16
