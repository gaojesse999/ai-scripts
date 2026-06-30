# Multiplication → Multiply-Subtract → Semi-Complex 32x16

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x16

Semi-Complex 32x16

Semi-Complex 32x16
Performs semi-complex multiply-subtract 32x16 between a complex number and a real number.
The complex source consists of real 32-bit part and imaginary 32-bit part. The real source
consists of real 16-bit part. Each of the real and the imaginary products are subtrcated from the
40-bit destination respectively.
Available Switches
           Number of atomic operations. An atomic operation is defined as a single semi-complex
           multiply-accumulate operation.Used for two vector destinations, while the first vector
Ohop
           destination is always fully written, the second vector destination number of atomic
           operation is set by Ohop. 5op œ Ohop œ 8op
           Number of atomic operations. An atomic operation is defined as a semi-complex
Qop
           multiply-subtract 32x16 operation. 1op ≤ Qop ≤ 4op
SHX        SHX is a pseudo-switch which is replaced by either >>8 or <
conj       conjugate complex operation
vmpsX Selects the VMSNX and VPSX set within modv0 or modv2 mode registers.

Intrinsic Names
vmsulwxr_v32_v32_v32_v40_v40_conj
vmsulwxr_v32_v32_v32_v40_v40_conj_vmpsX
vmsulwxr_v32_v32_v32_v40_v40
vmsulwxr_v32_v32_v32_v40_v40_vmpsX
vmsulwxr_v32_v32_v40_SHFL16_conj
vmsulwxr_v32_v32_v40_SHFL16_conj_vmpsX
vmsulwxr_v32_v32_v40_SHFL16
vmsulwxr_v32_v32_v40_SHFL16_vmpsX
vmsulwxr_v32_v32_v40_SHFR8_conj
vmsulwxr_v32_v32_v40_SHFR8_conj_vmpsX
vmsulwxr_v32_v32_v40_SHFR8
vmsulwxr_v32_v32_v40_SHFR8_vmpsX
vmsulwxr_v32_v32_v32_v40_v40_SHFL16_conj
vmsulwxr_v32_v32_v32_v40_v40_SHFL16_conj_vmpsX
vmsulwxr_v32_v32_v32_v40_v40_SHFL16
vmsulwxr_v32_v32_v32_v40_v40_SHFL16_vmpsX
vmsulwxr_v32_v32_v32_v40_v40_SHFR8_conj
vmsulwxr_v32_v32_v32_v40_v40_SHFR8_conj_vmpsX
vmsulwxr_v32_v32_v32_v40_v40_SHFR8
vmsulwxr_v32_v32_v32_v40_v40_SHFR8_vmpsX
vmsulwxr_v32_v32_v40_conj
vmsulwxr_v32_v32_v40_conj_vmpsX
vmsulwxr_v32_v32_v40
vmsulwxr_v32_v32_v40_vmpsX
Instruction details in the instruction set specification
Intrinsic     vmsulwxr_v32_v32_v32_v40_v40_conj[_p]
name
Spec syntax   vmsulwxr {Ohop [,conj][,vmpsX]} vx[0], vy[0], vv[V]p, voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    OHOP           uint8     5..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              4    IN3_V32        vec_t                      Input vector operand

Operands      5    IN3_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             4

              6    IN3_PART       uint8     LOW,HIGH         Word part which is used for operand 4
              7    IN4_V40        vec40_t                    Output vector operand
              8    RES2_V40       vec40_t                    Output vector result operand
              9    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec40_t vRes1;
C example     vec40_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vmsulwxr_v32_v32_v32_v40_v40_conj_p (8, vIn, vIn2, vIn3, 0, LOW, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vmsulwxr_v32_v32_v32_v40_v40_conj_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to

2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).


Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x16
Intrinsic     vmsulwxr_v32_v32_v32_v40_v40_conj_vmpsX[_p]
name
Spec syntax   vmsulwxr {Ohop [,conj][,vmpsX]} vx[0], vy[0], vv[V]p, voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    OHOP           uint8     5..8             Number of atomic operations
                                                             Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
Operands                                                     modv0/modv2 mode registers
              3    IN1_V32        vec_t                      Input vector operand
              4    IN2_V32        vec_t                      Input vector operand
              5    IN3_V32        vec_t                     Input vector operand

              6    IN3_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            5

              7    IN3_PART       uint8     LOW,HIGH        Word part which is used for operand 5
              8    IN4_V40        vec40_t                   Output vector operand
              9    RES2_V40       vec40_t                   Output vector result operand
              10   IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec40_t vRes1;
C example     vec40_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vmsulwxr_v32_v32_v32_v40_v40_conj_vmpsX_p (8, 1, vIn, vIn2, vIn3, 0, LOW, vRes1, vRes2,
              vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vmsulwxr_v32_v32_v32_v40_v40_conj_vmpsX_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).


Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x16
Intrinsic     vmsulwxr_v32_v32_v32_v40_v40[_p]
name
Spec syntax   vmsulwxr {Ohop [,conj][,vmpsX]} vx[0], vy[0], vv[V]p, voz1[0], voz2[0], ?vprX

Return type   vec40_t

1    OHOP           uint8     5..8            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              4    IN3_V32        vec_t                     Input vector operand

Operands      5    IN3_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            4

              6    IN3_PART       uint8     LOW,HIGH        Word part which is used for operand 4
              7    IN4_V40        vec40_t                   Output vector operand
              8    RES2_V40       vec40_t                   Output vector result operand
              9    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
C example     vec_t vIn2;
              vec_t vIn3;
              vec40_t vRes1;
              vec40_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vmsulwxr_v32_v32_v32_v40_v40_p (8, vIn, vIn2, vIn3, 0, LOW, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vmsulwxr_v32_v32_v32_v40_v40_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).


Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x16
Intrinsic     vmsulwxr_v32_v32_v32_v40_v40_vmpsX[_p]
name
Spec syntax   vmsulwxr {Ohop [,conj][,vmpsX]} vx[0], vy[0], vv[V]p, voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    OHOP           uint8     5..8             Number of atomic operations
                                                             Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                             modv0/modv2 mode registers
              3    IN1_V32        vec_t                      Input vector operand
              4    IN2_V32        vec_t                      Input vector operand
              5    IN3_V32        vec_t                      Input vector operand
Operands
              6    IN3_OFST       uint8     0..7             Offset for the first DW used from operand

5

              7    IN3_PART       uint8     LOW,HIGH         Word part which is used for operand 5
              8    IN4_V40        vec40_t                    Output vector operand
              9    RES2_V40       vec40_t                    Output vector result operand
              10   IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec40_t vRes1;
C example     vec40_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vmsulwxr_v32_v32_v32_v40_v40_vmpsX_p (8, 1, vIn, vIn2, vIn3, 0, LOW, vRes1, vRes2,
              vecPred);

                   IN_VPR last operand is relevant only for
              1.
Comments           vmsulwxr_v32_v32_v32_v40_v40_vmpsX_p version.
              2.   This intrinsic returns two results. The first result variable should be placed to
                the left of the = sign (lvalue). The second result variable should be passed as
                an additional parameter (RES2_V40).


Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x16
Intrinsic     vmsulwxr_v32_v32_v40_SHFL16_conj[_p]
name
Spec syntax   vmsulwxr {Qop ,SHFR8|SHFL16 [,conj][,vmpsX]} vx[Xe], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            2

              4    IN2_V32        vec_t                     Input vector operand
Operands
              5    IN2_OFST       uint8     0..7
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
              vRes = vmsulwxr_v32_v32_v40_SHFL16_conj_p (4, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

IN_VPR last operand is relevant only for
Comments      1.
                   vmsulwxr_v32_v32_v40_SHFL16_conj_p version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x16
Intrinsic     vmsulwxr_v32_v32_v40_SHFL16_conj_vmpsX[_p]
name
Spec syntax   vmsulwxr {Qop ,SHFR8|SHFL16 [,conj][,vmpsX]} vx[Xe], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4            Number of atomic operations
                                                            Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand

Operands      4    IN1_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            3

              5    IN2_V32        vec_t                     Input vector operand

              6    IN2_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            5

              7    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 5
              8    IN3_V40        vec40_t                   Output vector operand
              9    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsulwxr_v32_v32_v40_SHFL16_conj_vmpsX_p (4, 1, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsulwxr_v32_v32_v40_SHFL16_conj_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x16
Intrinsic     vmsulwxr_v32_v32_v40_SHFL16[_p]
name
Spec syntax   vmsulwxr {Qop ,SHFR8|SHFL16 [,conj][,vmpsX]} vx[Xe], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            2

4    IN2_V32        vec_t                     Input vector operand
Operands
              5    IN2_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            4

              6    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 4
              7    IN3_V40        vec40_t                   Output vector operand
              8    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsulwxr_v32_v32_v40_SHFL16_p (4, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsulwxr_v32_v32_v40_SHFL16_p version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x16
Intrinsic     vmsulwxr_v32_v32_v40_SHFL16_vmpsX[_p]
name
Spec syntax   vmsulwxr {Qop ,SHFR8|SHFL16 [,conj][,vmpsX]} vx[Xe], vy[Y]p, voz[0], ?vprX

Return type   vec40_t
              1    QOP            uint8     1..4           Number of atomic operations
                                                           Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                           modv0/modv2 mode registers
              3    IN1_V32        vec_t                    Input vector operand

              4    IN1_OFST       uint8     0..7
                                                           Offset for the first DW used from operand
                                                           3
Operands      5    IN2_V32        vec_t                    Input vector operand

              6    IN2_OFST       uint8     0..7
                                                           Offset for the first DW used from operand
                                                           5

              7    IN2_PART       uint8     LOW,HIGH       Word part which is used for operand 5
              8    IN3_V40        vec40_t                  Output vector operand
              9    IN_VPR         vprex_t                  Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsulwxr_v32_v32_v40_SHFL16_vmpsX_p (4, 1, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

IN_VPR last operand is relevant only for
Comments      1.
                   vmsulwxr_v32_v32_v40_SHFL16_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x16
Intrinsic     vmsulwxr_v32_v32_v40_SHFR8_conj[_p]
name
Spec syntax   vmsulwxr {Qop ,SHFR8|SHFL16 [,conj][,vmpsX]} vx[Xe], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4           Number of atomic operations
              2    IN1_V32        vec_t                    Input vector operand

              3    IN1_OFST       uint8     0..7
                                                           Offset for the first DW used from operand
                                                           2

              4    IN2_V32        vec_t                    Input vector operand
Operands
              5    IN2_OFST       uint8     0..7
                                                           Offset for the first DW used from operand
                                                           4

              6    IN2_PART       uint8     LOW,HIGH       Word part which is used for operand 4
              7    IN3_V40        vec40_t                  Output vector operand
              8    IN_VPR         vprex_t                  Vector predicate operand
              vec_t vIn;
C example     vec_t vIn2;
              vec40_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmsulwxr_v32_v32_v40_SHFR8_conj_p (4, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsulwxr_v32_v32_v40_SHFR8_conj_p version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x16
Intrinsic     vmsulwxr_v32_v32_v40_SHFR8_conj_vmpsX[_p]
name
Spec syntax   vmsulwxr {Qop ,SHFR8|SHFL16 [,conj][,vmpsX]} vx[Xe], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4            Number of atomic operations
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
              9    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsulwxr_v32_v32_v40_SHFR8_conj_vmpsX_p (4, 1, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsulwxr_v32_v32_v40_SHFR8_conj_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x16
Intrinsic     vmsulwxr_v32_v32_v40_SHFR8[_p]
name
Spec syntax   vmsulwxr {Qop ,SHFR8|SHFL16 [,conj][,vmpsX]} vx[Xe], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

Operands      1    QOP            uint8     1..4            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            2

              4    IN2_V32        vec_t                     Input vector operand

              5    IN2_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            4

              6    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 4
              7    IN3_V40        vec40_t                   Output vector operand
              8    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsulwxr_v32_v32_v40_SHFR8_p (4, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for vmsulwxr_v32_v32_v40_SHFR8_p
Comments      1.
                   version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x16
Intrinsic     vmsulwxr_v32_v32_v40_SHFR8_vmpsX[_p]
name

Spec syntax   vmsulwxr {Qop ,SHFR8|SHFL16 [,conj][,vmpsX]} vx[Xe], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4            Number of atomic operations
                                                            Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand

              4    IN1_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            3
Operands      5    IN2_V32        vec_t                     Input vector operand

              6    IN2_OFST       uint8     0..7
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
            vRes = vmsulwxr_v32_v32_v40_SHFR8_vmpsX_p (4, 1, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

                 IN_VPR last operand is relevant only for
Comments    1.
                 vmsulwxr_v32_v32_v40_SHFR8_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x16
Intrinsic     vmsulwxr_v32_v32_v32_v40_v40_SHFL16_conj[_p]
name
              vmsulwxr {Ohop ,SHFR8|SHFL16 [,conj][,vmpsX]} vx[0], vy[0], vv[V]p, voz1[0], voz2[0],
Spec syntax   ?vprX

Return type   vec40_t

              1    OHOP          uint8     5..8            Number of atomic operations
              2    IN1_V32       vec_t                     Input vector operand
              3    IN2_V32       vec_t                     Input vector operand
              4    IN3_V32       vec_t                     Input vector operand

Operands      5    IN3_OFST      uint8     0..7
                                                           Offset for the first DW used from operand
                                                           4

6    IN3_PART      uint8     LOW,HIGH        Word part which is used for operand 4
              7    IN4_V40       vec40_t                   Output vector operand
              8    RES2_V40      vec40_t                   Output vector result operand
              9    IN_VPR        vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec40_t vRes1;
C example     vec40_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vmsulwxr_v32_v32_v32_v40_v40_SHFL16_conj_p (8, vIn, vIn2, vIn3, 0, LOW, vRes1, vRes2,
              vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vmsulwxr_v32_v32_v32_v40_v40_SHFL16_conj_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).


Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x16
Intrinsic     vmsulwxr_v32_v32_v32_v40_v40_SHFL16_conj_vmpsX[_p]
name
              vmsulwxr {Ohop ,SHFR8|SHFL16 [,conj][,vmpsX]} vx[0], vy[0], vv[V]p, voz1[0], voz2[0],
Spec syntax   ?vprX

Return type   vec40_t

              1    OHOP          uint8     5..8            Number of atomic operations
                                                           Selects the VMSNX and VPSX set within
Operands      2    VMPSX         uint8     0,1
                                                           modv0/modv2 mode registers
              3    IN1_V32       vec_t                     Input vector operand
              4    IN2_V32       vec_t                    Input vector operand
              5    IN3_V32       vec_t                    Input vector operand

              6    IN3_OFST      uint8     0..7           Offset for the first DW used from operand
                                                          5

              7    IN3_PART      uint8     LOW,HIGH       Word part which is used for operand 5
              8    IN4_V40       vec40_t                  Output vector operand
              9    RES2_V40      vec40_t                  Output vector result operand
              10   IN_VPR        vprex_t                  Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;

vec40_t vRes1;
C example     vec40_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vmsulwxr_v32_v32_v32_v40_v40_SHFL16_conj_vmpsX_p (8, 1, vIn, vIn2, vIn3, 0, LOW,
              vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vmsulwxr_v32_v32_v32_v40_v40_SHFL16_conj_vmpsX_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).


Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x16
Intrinsic     vmsulwxr_v32_v32_v32_v40_v40_SHFL16[_p]
name
              vmsulwxr {Ohop ,SHFR8|SHFL16 [,conj][,vmpsX]} vx[0], vy[0], vv[V]p, voz1[0], voz2[0],
Spec syntax   ?vprX

Return type   vec40_t

              1    OHOP          uint8     5..8           Number of atomic operations
              2    IN1_V32       vec_t                    Input vector operand
              3    IN2_V32       vec_t                    Input vector operand
              4    IN3_V32       vec_t                    Input vector operand

Operands      5    IN3_OFST      uint8     0..7
                                                          Offset for the first DW used from operand
                                                          4

              6    IN3_PART      uint8     LOW,HIGH       Word part which is used for operand 4
              7    IN4_V40       vec40_t                  Output vector operand
              8    RES2_V40      vec40_t                  Output vector result operand
              9    IN_VPR        vprex_t                  Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec40_t vRes1;
C example     vec40_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vmsulwxr_v32_v32_v32_v40_v40_SHFL16_p (8, vIn, vIn2, vIn3, 0, LOW, vRes1, vRes2,
              vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vmsulwxr_v32_v32_v32_v40_v40_SHFL16_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as

an additional parameter (RES2_V40).


Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x16
Intrinsic     vmsulwxr_v32_v32_v32_v40_v40_SHFL16_vmpsX[_p]
name
              vmsulwxr {Ohop ,SHFR8|SHFL16 [,conj][,vmpsX]} vx[0], vy[0], vv[V]p, voz1[0], voz2[0],
Spec syntax   ?vprX

Return type   vec40_t

              1    OHOP          uint8     5..8            Number of atomic operations
                                                           Selects the VMSNX and VPSX set within
              2    VMPSX         uint8     0,1
                                                           modv0/modv2 mode registers
              3    IN1_V32       vec_t                     Input vector operand
              4    IN2_V32       vec_t                     Input vector operand
              5    IN3_V32       vec_t                     Input vector operand
Operands
              6    IN3_OFST      uint8     0..7            Offset for the first DW used from operand
                                                           5

              7    IN3_PART      uint8     LOW,HIGH        Word part which is used for operand 5
              8    IN4_V40       vec40_t                   Output vector operand
              9    RES2_V40      vec40_t                   Output vector result operand
              10   IN_VPR        vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec40_t vRes1;
C example     vec40_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vmsulwxr_v32_v32_v32_v40_v40_SHFL16_vmpsX_p (8, 1, vIn, vIn2, vIn3, 0, LOW, vRes1,
              vRes2, vecPred);

Comments      1.   IN_VPR last operand is relevant only for
                   vmsulwxr_v32_v32_v32_v40_v40_SHFL16_vmpsX_p version.
                   This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).


Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x16
Intrinsic     vmsulwxr_v32_v32_v32_v40_v40_SHFR8_conj[_p]
name
              vmsulwxr {Ohop ,SHFR8|SHFL16 [,conj][,vmpsX]} vx[0], vy[0], vv[V]p, voz1[0], voz2[0],
Spec syntax   ?vprX

Return type   vec40_t

              1    OHOP          uint8     5..8            Number of atomic operations

2    IN1_V32       vec_t                     Input vector operand
              3    IN2_V32       vec_t                     Input vector operand
              4    IN3_V32       vec_t                     Input vector operand

Operands      5    IN3_OFST      uint8     0..7
                                                           Offset for the first DW used from operand
                                                           4

              6    IN3_PART      uint8     LOW,HIGH        Word part which is used for operand 4
              7    IN4_V40       vec40_t                   Output vector operand
              8    RES2_V40      vec40_t                   Output vector result operand
              9    IN_VPR        vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec40_t vRes1;
C example     vec40_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vmsulwxr_v32_v32_v32_v40_v40_SHFR8_conj_p (8, vIn, vIn2, vIn3, 0, LOW, vRes1, vRes2,
              vecPred);

              1.
                   IN_VPR last operand is relevant only for
                   vmsulwxr_v32_v32_v32_v40_v40_SHFR8_conj_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).


Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x16
Intrinsic     vmsulwxr_v32_v32_v32_v40_v40_SHFR8_conj_vmpsX[_p]
name
Spec syntax   vmsulwxr {Ohop ,SHFR8|SHFL16 [,conj][,vmpsX]} vx[0], vy[0], vv[V]p, voz1[0], voz2[0],
              ?vprX

Return type   vec40_t

              1    OHOP          uint8     5..8           Number of atomic operations
                                                          Selects the VMSNX and VPSX set within
              2    VMPSX         uint8     0,1
                                                          modv0/modv2 mode registers
              3    IN1_V32       vec_t                    Input vector operand
              4    IN2_V32       vec_t                    Input vector operand
              5    IN3_V32       vec_t                    Input vector operand
Operands
              6    IN3_OFST      uint8     0..7           Offset for the first DW used from operand

5

              7    IN3_PART      uint8     LOW,HIGH       Word part which is used for operand 5
              8    IN4_V40       vec40_t                  Output vector operand
              9    RES2_V40      vec40_t                  Output vector result operand
              10   IN_VPR        vprex_t                  Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec40_t vRes1;
C example     vec40_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vmsulwxr_v32_v32_v32_v40_v40_SHFR8_conj_vmpsX_p (8, 1, vIn, vIn2, vIn3, 0, LOW, vRes1,
              vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vmsulwxr_v32_v32_v32_v40_v40_SHFR8_conj_vmpsX_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).


Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x16
Intrinsic     vmsulwxr_v32_v32_v32_v40_v40_SHFR8[_p]
name
              vmsulwxr {Ohop ,SHFR8|SHFL16 [,conj][,vmpsX]} vx[0], vy[0], vv[V]p, voz1[0], voz2[0],
Spec syntax   ?vprX

Return type   vec40_t

              1    OHOP          uint8     5..8           Number of atomic operations
              2    IN1_V32       vec_t                    Input vector operand
Operands
              3    IN2_V32       vec_t                    Input vector operand
              4    IN3_V32       vec_t                    Input vector operand
              5    IN3_OFST      uint8     0..7            Offset for the first DW used from operand
                                                           4

              6    IN3_PART      uint8     LOW,HIGH        Word part which is used for operand 4
              7    IN4_V40       vec40_t                   Output vector operand
              8    RES2_V40      vec40_t                   Output vector result operand
              9    IN_VPR        vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec40_t vRes1;
C example     vec40_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vmsulwxr_v32_v32_v32_v40_v40_SHFR8_p (8, vIn, vIn2, vIn3, 0, LOW, vRes1, vRes2,

vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vmsulwxr_v32_v32_v32_v40_v40_SHFR8_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).


Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x16
Intrinsic     vmsulwxr_v32_v32_v32_v40_v40_SHFR8_vmpsX[_p]
name
              vmsulwxr {Ohop ,SHFR8|SHFL16 [,conj][,vmpsX]} vx[0], vy[0], vv[V]p, voz1[0], voz2[0],
Spec syntax   ?vprX

Return type   vec40_t

              1    OHOP          uint8     5..8            Number of atomic operations
                                                           Selects the VMSNX and VPSX set within
              2    VMPSX         uint8     0,1
                                                           modv0/modv2 mode registers
              3    IN1_V32       vec_t                     Input vector operand
              4    IN2_V32       vec_t                     Input vector operand
              5    IN3_V32       vec_t                     Input vector operand
Operands
              6    IN3_OFST      uint8     0..7
                                                           Offset for the first DW used from operand
                                                           5

              7    IN3_PART      uint8     LOW,HIGH        Word part which is used for operand 5
              8    IN4_V40       vec40_t                   Output vector operand
              9    RES2_V40      vec40_t                   Output vector result operand
              10   IN_VPR        vprex_t                   Vector predicate operand
            vec_t vIn;
            vec_t vIn2;
            vec_t vIn3;
            vec40_t vRes1;
C example   vec40_t vRes2;
            vprex_t vecPred;
            ...
            vRes1 = vmsulwxr_v32_v32_v32_v40_v40_SHFR8_vmpsX_p (8, 1, vIn, vIn2, vIn3, 0, LOW, vRes1,
            vRes2, vecPred);

                 IN_VPR last operand is relevant only for
            1.
                 vmsulwxr_v32_v32_v32_v40_v40_SHFR8_vmpsX_p version.
Comments         This intrinsic returns two results. The first result variable should be placed to
            2.   the left of the = sign (lvalue). The second result variable should be passed as

an additional parameter (RES2_V40).


Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x16
Intrinsic     vmsulwxr_v32_v32_v40_conj[_p]
name
Spec syntax   vmsulwxr {Qop [,conj][,vmpsX]} vx[Xe], vy[Y]p, voz[0], ?vprX

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
              vRes = vmsulwxr_v32_v32_v40_conj_p (4, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for vmsulwxr_v32_v32_v40_conj_p
Comments      1.
                   version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x16
Intrinsic     vmsulwxr_v32_v32_v40_conj_vmpsX[_p]
name
Spec syntax   vmsulwxr {Qop [,conj][,vmpsX]} vx[Xe], vy[Y]p, voz[0], ?vprX

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
              vRes = vmsulwxr_v32_v32_v40_conj_vmpsX_p (4, 1, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsulwxr_v32_v32_v40_conj_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x16
Intrinsic     vmsulwxr_v32_v32_v40[_p]
name
Spec syntax   vmsulwxr {Qop [,conj][,vmpsX]} vx[Xe], vy[Y]p, voz[0], ?vprX

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
              vRes = vmsulwxr_v32_v32_v40_p (4, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmsulwxr_v32_v32_v40_p version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x16
Intrinsic     vmsulwxr_v32_v32_v40_vmpsX[_p]
name
Spec syntax   vmsulwxr {Qop [,conj][,vmpsX]} vx[Xe], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

1    QOP            uint8     1..4             Number of atomic operations
                                                           Selects the VMSNX and VPSX set within
            2    VMPSX          uint8     0,1
                                                           modv0/modv2 mode registers
            3    IN1_V32        vec_t                      Input vector operand

            4    IN1_OFST       uint8     0..7
                                                           Offset for the first DW used from operand
                                                           3
Operands    5    IN2_V32        vec_t                      Input vector operand

            6    IN2_OFST       uint8     0..7
                                                           Offset for the first DW used from operand
                                                           5

            7    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 5
            8    IN3_V40        vec40_t                    Output vector operand
            9    IN_VPR         vprex_t                    Vector predicate operand
            vec_t vIn;
            vec_t vIn2;
            vec40_t vRes;
C example   vprex_t vecPred;
            ...
            vRes = vmsulwxr_v32_v32_v40_vmpsX_p (4, 1, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

                 IN_VPR last operand is relevant only for vmsulwxr_v32_v32_v40_vmpsX_p
Comments    1.
                 version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x16
