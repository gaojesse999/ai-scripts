# Multiplication → Multiply-Accumulate → Semi-Complex 16x32 into Two

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Multiplication → Multiply-Accumulate → Semi-Complex 16x32 into Two
Words

Semi-Complex 16x32 into Two Words

Semi-Complex 16x32 into Two Words
Performs semi-complex 16x32 multiply-accumulate between a complex number and a real
number. The complex source consists of real 16-bit part and imaginary 16-bit part. The real
source consists of real 32-bit part. Each of the real and the imaginary products are accumulated
with the 40-bit destination respectively.
Available Switches
           Number of atomic operations. An atomic operation is defined as a semi-complex 16x32
           multiply-accumulate operation.Used for two vector destinations, while the first vector
Ohop
           destination is always fully written, the second vector destination number of atomic
           operation is set by Ohop. 5op œ Ohop œ 8op
           Number of atomic operations. An atomic operation is defined as a semi-complex 16x32
Qop
           multiply-accumulate operation. 1op ≤ Qop ≤ 4op
SHX        SHX is a pseudo-switch which is replaced by either >>8 or <
conj       conjugate complex operation
vmpsX Selects the VMSNX and VPSX set within modv0 or modv2 mode registers.
Intrinsic Names
vmacwlxr_v32_v32_v40_v40_conj
vmacwlxr_v32_v32_v40_v40_conj_vmpsX
vmacwlxr_v32_v32_v40_v40
vmacwlxr_v32_v32_v40_v40_vmpsX
vmacwlxr_v32_v32_v40_SHFL16_conj
vmacwlxr_v32_v32_v40_SHFL16_conj_vmpsX
vmacwlxr_v32_v32_v40_SHFL16

vmacwlxr_v32_v32_v40_SHFL16_vmpsX
vmacwlxr_v32_v32_v40_SHFR8_conj
vmacwlxr_v32_v32_v40_SHFR8_conj_vmpsX
vmacwlxr_v32_v32_v40_SHFR8
vmacwlxr_v32_v32_v40_SHFR8_vmpsX
vmacwlxr_v32_v32_v40_v40_SHFL16_conj
vmacwlxr_v32_v32_v40_v40_SHFL16_conj_vmpsX
vmacwlxr_v32_v32_v40_v40_SHFL16
vmacwlxr_v32_v32_v40_v40_SHFL16_vmpsX
vmacwlxr_v32_v32_v40_v40_SHFR8_conj
vmacwlxr_v32_v32_v40_v40_SHFR8_conj_vmpsX
vmacwlxr_v32_v32_v40_v40_SHFR8
vmacwlxr_v32_v32_v40_v40_SHFR8_vmpsX
vmacwlxr_v32_v32_v40_conj
vmacwlxr_v32_v32_v40_conj_vmpsX
vmacwlxr_v32_v32_v40
vmacwlxr_v32_v32_v40_vmpsX
Instruction details in the instruction set specification
Intrinsic     vmacwlxr_v32_v32_v40_v40_conj[_p]
name
Spec syntax   vmacwlxr {Ohop [,conj][,vmpsX]} vx[X], vy[Y], voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    OHOP           uint8      5..8             Number of atomic operations
              2    IN1_V32        vec_t                       Input vector operand

              3    IN1_OFST       uint8      0..7
                                                              Offset for the first DW used from operand
                                                              2

              4    IN2_V32        vec_t                       Input vector operand
Operands
              5    IN2_OFST       uint8      0..7
                                                              Offset for the first DW used from operand
                                                              4

              6    IN3_V40        vec40_t                     Output vector operand
              7    RES2_V40       vec40_t                     Output vector result operand
              8    IN_VPR         vprex_t                     Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes1;
C example     vec40_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vmacwlxr_v32_v32_v40_v40_conj_p (8, vIn, 0, vIn2, 0, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vmacwlxr_v32_v32_v40_v40_conj_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).


Main table → Multiplication → Multiply-Accumulate → Semi-Complex 16x32 into Two
Words

Intrinsic     vmacwlxr_v32_v32_v40_v40_conj_vmpsX[_p]
name
Spec syntax   vmacwlxr {Ohop [,conj][,vmpsX]} vx[X], vy[Y], voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    OHOP           uint8      5..8             Number of atomic operations
                                                              Selects the VMSNX and VPSX set within
              2    VMPSX          uint8      0,1
                                                              modv0/modv2 mode registers
Operands
              3    IN1_V32        vec_t                       Input vector operand

              4    IN1_OFST       uint8      0..7
                                                              Offset for the first DW used from operand
                                                              3
              5    IN2_V32        vec_t                      Input vector operand

              6    IN2_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             5

              7    IN3_V40        vec40_t                    Output vector operand
              8    RES2_V40       vec40_t                    Output vector result operand
              9    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes1;
C example     vec40_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vmacwlxr_v32_v32_v40_v40_conj_vmpsX_p (8, 1, vIn, 0, vIn2, 0, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vmacwlxr_v32_v32_v40_v40_conj_vmpsX_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).


Main table → Multiplication → Multiply-Accumulate → Semi-Complex 16x32 into Two
Words
Intrinsic     vmacwlxr_v32_v32_v40_v40[_p]
name
Spec syntax   vmacwlxr {Ohop [,conj][,vmpsX]} vx[X], vy[Y], voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    OHOP           uint8     5..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0..7             Offset for the first DW used from operand

2

              4    IN2_V32        vec_t                      Input vector operand
Operands
              5    IN2_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             4

              6    IN3_V40        vec40_t                    Output vector operand
              7    RES2_V40       vec40_t                    Output vector result operand
              8    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes1;
C example     vec40_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vmacwlxr_v32_v32_v40_v40_p (8, vIn, 0, vIn2, 0, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for vmacwlxr_v32_v32_v40_v40_p
              1.
                   version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).


Main table → Multiplication → Multiply-Accumulate → Semi-Complex 16x32 into Two
Words
Intrinsic     vmacwlxr_v32_v32_v40_v40_vmpsX[_p]
name
Spec syntax   vmacwlxr {Ohop [,conj][,vmpsX]} vx[X], vy[Y], voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    OHOP            uint8     5..8             Number of atomic operations
                                                              Selects the VMSNX and VPSX set within
              2    VMPSX           uint8     0,1
                                                              modv0/modv2 mode registers
              3    IN1_V32         vec_t                      Input vector operand

              4    IN1_OFST        uint8     0..7             Offset for the first DW used from operand
                                                              3
Operands      5    IN2_V32         vec_t                      Input vector operand

              6    IN2_OFST        uint8     0..7             Offset for the first DW used from operand
                                                              5

              7    IN3_V40         vec40_t                    Output vector operand
              8    RES2_V40        vec40_t                    Output vector result operand

9    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes1;
C example     vec40_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vmacwlxr_v32_v32_v40_v40_vmpsX_p (8, 1, vIn, 0, vIn2, 0, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vmacwlxr_v32_v32_v40_v40_vmpsX_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).


Main table → Multiplication → Multiply-Accumulate → Semi-Complex 16x32 into Two
Words
Intrinsic     vmacwlxr_v32_v32_v40_SHFL16_conj[_p]
name
Spec syntax   vmacwlxr {Qop ,SHFR8|SHFL16 [,conj][,vmpsX]} vx[X], vy[Y], voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            2

Operands      4    IN2_V32        vec_t                     Input vector operand

              5    IN2_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            4

              6    IN3_V40        vec40_t                   Output vector operand
              7    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmacwlxr_v32_v32_v40_SHFL16_conj_p (4, vIn, 0, vIn2, 0, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmacwlxr_v32_v32_v40_SHFL16_conj_p version.


Main table → Multiplication → Multiply-Accumulate → Semi-Complex 16x32 into Two
Words
Intrinsic     vmacwlxr_v32_v32_v40_SHFL16_conj_vmpsX[_p]
name
Spec syntax   vmacwlxr {Qop ,SHFR8|SHFL16 [,conj][,vmpsX]} vx[X], vy[Y], voz[0], ?vprX

Return type   vec40_t

1    QOP            uint8     1..4            Number of atomic operations

              2
                                                            Selects the VMSNX and VPSX set within
                   VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand

Operands      4    IN1_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            3

              5    IN2_V32        vec_t                     Input vector operand

              6    IN2_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            5

              7    IN3_V40        vec40_t                   Output vector operand
              8    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmacwlxr_v32_v32_v40_SHFL16_conj_vmpsX_p (4, 1, vIn, 0, vIn2, 0, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmacwlxr_v32_v32_v40_SHFL16_conj_vmpsX_p version.


Main table → Multiplication → Multiply-Accumulate → Semi-Complex 16x32 into Two
Words
Intrinsic     vmacwlxr_v32_v32_v40_SHFL16[_p]
name
Spec syntax   vmacwlxr {Qop ,SHFR8|SHFL16 [,conj][,vmpsX]} vx[X], vy[Y], voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             2

Operands      4    IN2_V32        vec_t                      Input vector operand

              5    IN2_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             4

              6    IN3_V40        vec40_t                    Output vector operand

7    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmacwlxr_v32_v32_v40_SHFL16_p (4, vIn, 0, vIn2, 0, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmacwlxr_v32_v32_v40_SHFL16_p version.


Main table → Multiplication → Multiply-Accumulate → Semi-Complex 16x32 into Two
Words
Intrinsic     vmacwlxr_v32_v32_v40_SHFL16_vmpsX[_p]
name
Spec syntax   vmacwlxr {Qop ,SHFR8|SHFL16 [,conj][,vmpsX]} vx[X], vy[Y], voz[0], ?vprX

Return type   vec40_t
              1    QOP            uint8     1..4            Number of atomic operations
                                                            Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand

              4    IN1_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
Operands                                                    3

              5    IN2_V32        vec_t                     Input vector operand

              6    IN2_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            5

              7    IN3_V40        vec40_t                   Output vector operand
              8    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmacwlxr_v32_v32_v40_SHFL16_vmpsX_p (4, 1, vIn, 0, vIn2, 0, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmacwlxr_v32_v32_v40_SHFL16_vmpsX_p version.


Main table → Multiplication → Multiply-Accumulate → Semi-Complex 16x32 into Two
Words
Intrinsic     vmacwlxr_v32_v32_v40_SHFR8_conj[_p]
name
Spec syntax   vmacwlxr {Qop ,SHFR8|SHFL16 [,conj][,vmpsX]} vx[X], vy[Y], voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4            Number of atomic operations

2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            2

Operands      4    IN2_V32        vec_t                     Input vector operand

              5    IN2_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            4

              6    IN3_V40        vec40_t                   Output vector operand
              7    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
C example     vec40_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmacwlxr_v32_v32_v40_SHFR8_conj_p (4, vIn, 0, vIn2, 0, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmacwlxr_v32_v32_v40_SHFR8_conj_p version.


Main table → Multiplication → Multiply-Accumulate → Semi-Complex 16x32 into Two
Words
Intrinsic     vmacwlxr_v32_v32_v40_SHFR8_conj_vmpsX[_p]
name
Spec syntax   vmacwlxr {Qop ,SHFR8|SHFL16 [,conj][,vmpsX]} vx[X], vy[Y], voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4            Number of atomic operations
                                                            Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand

              4    IN1_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
Operands                                                    3

              5    IN2_V32        vec_t                     Input vector operand

              6    IN2_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            5

              7    IN3_V40        vec40_t                   Output vector operand
              8    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...

vRes = vmacwlxr_v32_v32_v40_SHFR8_conj_vmpsX_p (4, 1, vIn, 0, vIn2, 0, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmacwlxr_v32_v32_v40_SHFR8_conj_vmpsX_p version.


Main table → Multiplication → Multiply-Accumulate → Semi-Complex 16x32 into Two
Words
Intrinsic     vmacwlxr_v32_v32_v40_SHFR8[_p]
name
Spec syntax   vmacwlxr {Qop ,SHFR8|SHFL16 [,conj][,vmpsX]} vx[X], vy[Y], voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4            Number of atomic operations
Operands
              2    IN1_V32        vec_t                     Input vector operand
              3    IN1_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             2

              4    IN2_V32        vec_t                      Input vector operand

              5    IN2_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             4

              6    IN3_V40        vec40_t                    Output vector operand
              7    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmacwlxr_v32_v32_v40_SHFR8_p (4, vIn, 0, vIn2, 0, vRes, vecPred);

                   IN_VPR last operand is relevant only for vmacwlxr_v32_v32_v40_SHFR8_p
Comments      1.
                   version.


Main table → Multiplication → Multiply-Accumulate → Semi-Complex 16x32 into Two
Words
Intrinsic     vmacwlxr_v32_v32_v40_SHFR8_vmpsX[_p]
name
Spec syntax   vmacwlxr {Qop ,SHFR8|SHFL16 [,conj][,vmpsX]} vx[X], vy[Y], voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4             Number of atomic operations
                                                             Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                             modv0/modv2 mode registers
              3    IN1_V32        vec_t                      Input vector operand

              4    IN1_OFST       uint8     0..7             Offset for the first DW used from operand
Operands                                                     3

5    IN2_V32        vec_t                      Input vector operand

              6    IN2_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             5

              7    IN3_V40        vec40_t                    Output vector operand
              8    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmacwlxr_v32_v32_v40_SHFR8_vmpsX_p (4, 1, vIn, 0, vIn2, 0, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmacwlxr_v32_v32_v40_SHFR8_vmpsX_p version.

Main table → Multiplication → Multiply-Accumulate → Semi-Complex 16x32 into Two
Words
Intrinsic     vmacwlxr_v32_v32_v40_v40_SHFL16_conj[_p]
name
Spec syntax   vmacwlxr {Ohop ,SHFR8|SHFL16 [,conj][,vmpsX]} vx[X], vy[Y], voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    OHOP           uint8     5..8            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            2

              4    IN2_V32        vec_t                     Input vector operand
Operands
              5    IN2_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            4

              6    IN3_V40        vec40_t                   Output vector operand
              7    RES2_V40       vec40_t                   Output vector result operand
              8    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes1;
C example     vec40_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vmacwlxr_v32_v32_v40_v40_SHFL16_conj_p (8, vIn, 0, vIn2, 0, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vmacwlxr_v32_v32_v40_v40_SHFL16_conj_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to

2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).


Main table → Multiplication → Multiply-Accumulate → Semi-Complex 16x32 into Two
Words
Intrinsic     vmacwlxr_v32_v32_v40_v40_SHFL16_conj_vmpsX[_p]
name
Spec syntax   vmacwlxr {Ohop ,SHFR8|SHFL16 [,conj][,vmpsX]} vx[X], vy[Y], voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    OHOP           uint8     5..8            Number of atomic operations
                                                            Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
Operands
              3    IN1_V32        vec_t                     Input vector operand

              4    IN1_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            3
              5    IN2_V32        vec_t                    Input vector operand

              6    IN2_OFST       uint8     0..7           Offset for the first DW used from operand
                                                           5

              7    IN3_V40        vec40_t                  Output vector operand
              8    RES2_V40       vec40_t                  Output vector result operand
              9    IN_VPR         vprex_t                  Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes1;
              vec40_t vRes2;
C example     vprex_t vecPred;
              ...
              vRes1 = vmacwlxr_v32_v32_v40_v40_SHFL16_conj_vmpsX_p (8, 1, vIn, 0, vIn2, 0, vRes1, vRes2,
              vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vmacwlxr_v32_v32_v40_v40_SHFL16_conj_vmpsX_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).


Main table → Multiplication → Multiply-Accumulate → Semi-Complex 16x32 into Two
Words
Intrinsic     vmacwlxr_v32_v32_v40_v40_SHFL16[_p]
name
Spec syntax   vmacwlxr {Ohop ,SHFR8|SHFL16 [,conj][,vmpsX]} vx[X], vy[Y], voz1[0], voz2[0], ?vprX

Return type   vec40_t

1    OHOP           uint8     5..8           Number of atomic operations
              2    IN1_V32        vec_t                    Input vector operand

              3    IN1_OFST       uint8     0..7
                                                           Offset for the first DW used from operand
                                                           2

              4    IN2_V32        vec_t                    Input vector operand
Operands
              5    IN2_OFST       uint8     0..7           Offset for the first DW used from operand
                                                           4

              6    IN3_V40        vec40_t                  Output vector operand
              7    RES2_V40       vec40_t                  Output vector result operand
              8    IN_VPR         vprex_t                  Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
C example     vec40_t vRes1;
              vec40_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vmacwlxr_v32_v32_v40_v40_SHFL16_p (8, vIn, 0, vIn2, 0, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vmacwlxr_v32_v32_v40_v40_SHFL16_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).


Main table → Multiplication → Multiply-Accumulate → Semi-Complex 16x32 into Two
Words
Intrinsic     vmacwlxr_v32_v32_v40_v40_SHFL16_vmpsX[_p]
name
Spec syntax   vmacwlxr {Ohop ,SHFR8|SHFL16 [,conj][,vmpsX]} vx[X], vy[Y], voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    OHOP           uint8     5..8            Number of atomic operations
                                                            Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand

              4    IN1_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            3
Operands      5    IN2_V32        vec_t                     Input vector operand

6    IN2_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            5

              7    IN3_V40        vec40_t                   Output vector operand
              8    RES2_V40       vec40_t                   Output vector result operand
              9    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes1;
C example     vec40_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vmacwlxr_v32_v32_v40_v40_SHFL16_vmpsX_p (8, 1, vIn, 0, vIn2, 0, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vmacwlxr_v32_v32_v40_v40_SHFL16_vmpsX_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).

Main table → Multiplication → Multiply-Accumulate → Semi-Complex 16x32 into Two
Words
Intrinsic     vmacwlxr_v32_v32_v40_v40_SHFR8_conj[_p]
name
Spec syntax   vmacwlxr {Ohop ,SHFR8|SHFL16 [,conj][,vmpsX]} vx[X], vy[Y], voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    OHOP           uint8     5..8            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            2

              4    IN2_V32        vec_t                     Input vector operand
Operands
              5    IN2_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            4

              6    IN3_V40        vec40_t                   Output vector operand
              7    RES2_V40       vec40_t                   Output vector result operand
              8    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes1;
C example     vec40_t vRes2;
              vprex_t vecPred;
              ...

vRes1 = vmacwlxr_v32_v32_v40_v40_SHFR8_conj_p (8, vIn, 0, vIn2, 0, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vmacwlxr_v32_v32_v40_v40_SHFR8_conj_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).


Main table → Multiplication → Multiply-Accumulate → Semi-Complex 16x32 into Two
Words
Intrinsic     vmacwlxr_v32_v32_v40_v40_SHFR8_conj_vmpsX[_p]
name
Spec syntax   vmacwlxr {Ohop ,SHFR8|SHFL16 [,conj][,vmpsX]} vx[X], vy[Y], voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    OHOP           uint8     5..8            Number of atomic operations
Operands                                                    Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32       vec_t                     Input vector operand

              4    IN1_OFST      uint8     0..7            Offset for the first DW used from operand
                                                           3

              5    IN2_V32       vec_t                     Input vector operand

              6    IN2_OFST      uint8     0..7            Offset for the first DW used from operand
                                                           5

              7    IN3_V40       vec40_t                   Output vector operand
              8    RES2_V40      vec40_t                   Output vector result operand
              9    IN_VPR        vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes1;
              vec40_t vRes2;
C example     vprex_t vecPred;
              ...
              vRes1 = vmacwlxr_v32_v32_v40_v40_SHFR8_conj_vmpsX_p (8, 1, vIn, 0, vIn2, 0, vRes1, vRes2,
              vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vmacwlxr_v32_v32_v40_v40_SHFR8_conj_vmpsX_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as

an additional parameter (RES2_V40).


Main table → Multiplication → Multiply-Accumulate → Semi-Complex 16x32 into Two
Words
Intrinsic     vmacwlxr_v32_v32_v40_v40_SHFR8[_p]
name
Spec syntax   vmacwlxr {Ohop ,SHFR8|SHFL16 [,conj][,vmpsX]} vx[X], vy[Y], voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    OHOP          uint8     5..8            Number of atomic operations
              2    IN1_V32       vec_t                     Input vector operand

              3    IN1_OFST      uint8     0..7            Offset for the first DW used from operand
                                                           2

              4    IN2_V32       vec_t                     Input vector operand
Operands
              5    IN2_OFST      uint8     0..7            Offset for the first DW used from operand
                                                           4

              6    IN3_V40       vec40_t                   Output vector operand
              7    RES2_V40      vec40_t                   Output vector result operand
              8    IN_VPR        vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes1;
C example     vec40_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vmacwlxr_v32_v32_v40_v40_SHFR8_p (8, vIn, 0, vIn2, 0, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vmacwlxr_v32_v32_v40_v40_SHFR8_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).


Main table → Multiplication → Multiply-Accumulate → Semi-Complex 16x32 into Two
Words
Intrinsic     vmacwlxr_v32_v32_v40_v40_SHFR8_vmpsX[_p]
name
Spec syntax   vmacwlxr {Ohop ,SHFR8|SHFL16 [,conj][,vmpsX]} vx[X], vy[Y], voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    OHOP           uint8     5..8            Number of atomic operations
                                                            Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand

4    IN1_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            3
Operands      5    IN2_V32        vec_t                     Input vector operand

              6    IN2_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            5

              7    IN3_V40        vec40_t                   Output vector operand
              8    RES2_V40       vec40_t                   Output vector result operand
              9    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes1;
C example     vec40_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vmacwlxr_v32_v32_v40_v40_SHFR8_vmpsX_p (8, 1, vIn, 0, vIn2, 0, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
Comments           vmacwlxr_v32_v32_v40_v40_SHFR8_vmpsX_p version.
              2.   This intrinsic returns two results. The first result variable should be placed to
                the left of the = sign (lvalue). The second result variable should be passed as
                an additional parameter (RES2_V40).


Main table → Multiplication → Multiply-Accumulate → Semi-Complex 16x32 into Two
Words
Intrinsic     vmacwlxr_v32_v32_v40_conj[_p]
name
Spec syntax   vmacwlxr {Qop [,conj][,vmpsX]} vx[X], vy[Y], voz[0], ?vprX

Return type   vec40_t

              1    QOP             uint8     1..4             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand

              3    IN1_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
                                                              2

Operands      4    IN2_V32         vec_t                      Input vector operand

              5    IN2_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
                                                              4

              6    IN3_V40         vec40_t                    Output vector operand

7    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmacwlxr_v32_v32_v40_conj_p (4, vIn, 0, vIn2, 0, vRes, vecPred);

                   IN_VPR last operand is relevant only for vmacwlxr_v32_v32_v40_conj_p
Comments      1.
                   version.


Main table → Multiplication → Multiply-Accumulate → Semi-Complex 16x32 into Two
Words
Intrinsic     vmacwlxr_v32_v32_v40_conj_vmpsX[_p]
name
Spec syntax   vmacwlxr {Qop [,conj][,vmpsX]} vx[X], vy[Y], voz[0], ?vprX

Return type   vec40_t

              1    QOP             uint8     1..4             Number of atomic operations

              2
                                                              Selects the VMSNX and VPSX set within
                   VMPSX           uint8     0,1
                                                              modv0/modv2 mode registers
              3    IN1_V32         vec_t                      Input vector operand

Operands      4    IN1_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
                                                              3

              5    IN2_V32         vec_t                      Input vector operand

              6    IN2_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
                                                              5

              7    IN3_V40         vec40_t                    Output vector operand
              8    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmacwlxr_v32_v32_v40_conj_vmpsX_p (4, 1, vIn, 0, vIn2, 0, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmacwlxr_v32_v32_v40_conj_vmpsX_p version.


Main table → Multiplication → Multiply-Accumulate → Semi-Complex 16x32 into Two
Words
Intrinsic     vmacwlxr_v32_v32_v40[_p]
name
Spec syntax   vmacwlxr {Qop [,conj][,vmpsX]} vx[X], vy[Y], voz[0], ?vprX

Return type   vec40_t

              1    QOP             uint8     1..4             Number of atomic operations

2    IN1_V32         vec_t                      Input vector operand

              3    IN1_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
                                                              2

Operands      4    IN2_V32         vec_t                      Input vector operand

              5    IN2_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
                                                              4

              6    IN3_V40         vec40_t                    Output vector operand
              7    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmacwlxr_v32_v32_v40_p (4, vIn, 0, vIn2, 0, vRes, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmacwlxr_v32_v32_v40_p version.


Main table → Multiplication → Multiply-Accumulate → Semi-Complex 16x32 into Two
Words
Intrinsic     vmacwlxr_v32_v32_v40_vmpsX[_p]
name
Spec syntax   vmacwlxr {Qop [,conj][,vmpsX]} vx[X], vy[Y], voz[0], ?vprX

Return type   vec40_t

Operands      1    QOP             uint8     1..4             Number of atomic operations
                                                           Selects the VMSNX and VPSX set within
            2    VMPSX          uint8     0,1
                                                           modv0/modv2 mode registers
            3    IN1_V32        vec_t                      Input vector operand

            4    IN1_OFST       uint8     0..7             Offset for the first DW used from operand
                                                           3

            5    IN2_V32        vec_t                      Input vector operand

            6    IN2_OFST       uint8     0..7
                                                           Offset for the first DW used from operand
                                                           5

            7    IN3_V40        vec40_t                    Output vector operand
            8    IN_VPR         vprex_t                    Vector predicate operand
            vec_t vIn;
            vec_t vIn2;
            vec40_t vRes;
C example   vprex_t vecPred;
            ...

vRes = vmacwlxr_v32_v32_v40_vmpsX_p (4, 1, vIn, 0, vIn2, 0, vRes, vecPred);

                 IN_VPR last operand is relevant only for vmacwlxr_v32_v32_v40_vmpsX_p
Comments    1.
                 version.


Main table → Multiplication → Multiply-Accumulate → Semi-Complex 16x32 into Two
Words
