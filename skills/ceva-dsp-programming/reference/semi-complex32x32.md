# Multiplication → Multiply-Subtract → Semi-Complex 32x32

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x32

Semi-Complex 32x32

Semi-Complex 32x32
Performs semi-complex multiplication subtract using two products. Complex source is 64-bits
wide (32-bit real and 32-bit Imaginary). Real source is 32-bits wide. The products are subtracted
from two 72-bit destinations.
Available Switches
           Number of atomic operations. An atomic operation is defined as a single semi complex
Dop
           multiply-subtract operation. 1op œ Dop œ 2op
           Number of atomic operations. An atomic operation is defined as a single semi complex
           multiply-subtract operation. Used for two vector destinations, while the first vector
Qhop
           destination is always fully written, the second vector destination number of atomic
           operation is set by Qhop. 3op œ Qhop œ 4op
conj       Performs complex multiply using complex conjugate of vx[Xe]
const      When used, vy[Y] is constant throughout the operations.
vmpsX Selects the VMSNX and VPSX set within modv0 or modv2 mode registers.
Intrinsic Names
vmsullxr_v32_v32_v40_conj_const
vmsullxr_v32_v32_v40_conj_const_vmpsX
vmsullxr_v32_v32_v40_conj
vmsullxr_v32_v32_v40_conj_vmpsX
vmsullxr_v32_v32_v40_const
vmsullxr_v32_v32_v40_const_vmpsX
vmsullxr_v32_v32_v40
vmsullxr_v32_v32_v40_vmpsX
vmsullxr_v32_c32_v40_v40_conj
vmsullxr_v32_c32_v40_v40_conj_vmpsX
vmsullxr_v32_c32_v40_v40
vmsullxr_v32_c32_v40_v40_vmpsX
vmsullxr_v32_c32_v40_conj
vmsullxr_v32_c32_v40_conj_vmpsX
vmsullxr_v32_c32_v40
vmsullxr_v32_c32_v40_vmpsX
vmsullxr_v32_v32_v40_v40_conj_const
vmsullxr_v32_v32_v40_v40_conj_const_vmpsX
vmsullxr_v32_v32_v40_v40_conj
vmsullxr_v32_v32_v40_v40_conj_vmpsX
vmsullxr_v32_v32_v40_v40_const

vmsullxr_v32_v32_v40_v40_const_vmpsX
vmsullxr_v32_v32_v40_v40
vmsullxr_v32_v32_v40_v40_vmpsX
Instruction details in the instruction set specification
Intrinsic     vmsullxr_v32_v32_v40_conj_const[_p]
name
Spec syntax   vmsullxr {Dop [,conj][,const][,vmpsX]} vx[Xe], vy[Y], voz[0], ?vprX

Return type   vec40_t

              1    DOP             uint8     1..2             Number of atomic operations
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
              vRes = vmsullxr_v32_v32_v40_conj_const_p (2, vIn, 0, vIn2, 0, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsullxr_v32_v32_v40_conj_const_p version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x32
Intrinsic     vmsullxr_v32_v32_v40_conj_const_vmpsX[_p]
name
Spec syntax   vmsullxr {Dop [,conj][,const][,vmpsX]} vx[Xe], vy[Y], voz[0], ?vprX

Return type   vec40_t

              1    DOP             uint8     1..2             Number of atomic operations

              2
                                                              Selects the VMSNX and VPSX set within
                   VMPSX           uint8     0,1
                                                              modv0/modv2 mode registers
              3    IN1_V32         vec_t                      Input vector operand

              4    IN1_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
Operands                                                      3

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
              vRes = vmsullxr_v32_v32_v40_conj_const_vmpsX_p (2, 1, vIn, 0, vIn2, 0, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsullxr_v32_v32_v40_conj_const_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x32
Intrinsic     vmsullxr_v32_v32_v40_conj[_p]
name
Spec syntax   vmsullxr {Dop [,conj][,const][,vmpsX]} vx[Xe], vy[Y], voz[0], ?vprX

Return type   vec40_t

              1    DOP             uint8     1..2              Number of atomic operations
              2    IN1_V32         vec_t                       Input vector operand

              3    IN1_OFST        uint8     0..7
                                                               Offset for the first DW used from operand
                                                               2

Operands      4    IN2_V32         vec_t                       Input vector operand

              5    IN2_OFST        uint8     0..7
                                                               Offset for the first DW used from operand
                                                               4

              6    IN3_V40         vec40_t                     Output vector operand
              7    IN_VPR          vprex_t                     Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsullxr_v32_v32_v40_conj_p (2, vIn, 0, vIn2, 0, vRes, vecPred);

                   IN_VPR last operand is relevant only for vmsullxr_v32_v32_v40_conj_p
Comments      1.
                   version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x32
Intrinsic     vmsullxr_v32_v32_v40_conj_vmpsX[_p]
name
Spec syntax   vmsullxr {Dop [,conj][,const][,vmpsX]} vx[Xe], vy[Y], voz[0], ?vprX

Return type   vec40_t

              1    DOP             uint8     1..2              Number of atomic operations
Operands                                                       Selects the VMSNX and VPSX set within
              2    VMPSX           uint8     0,1
                                                               modv0/modv2 mode registers
              3    IN1_V32         vec_t                       Input vector operand

              4    IN1_OFST        uint8     0..7              Offset for the first DW used from operand
                                                               3

              5    IN2_V32         vec_t                       Input vector operand

              6    IN2_OFST        uint8     0..7              Offset for the first DW used from operand
                                                               5

              7    IN3_V40         vec40_t                     Output vector operand
              8    IN_VPR          vprex_t                     Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsullxr_v32_v32_v40_conj_vmpsX_p (2, 1, vIn, 0, vIn2, 0, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsullxr_v32_v32_v40_conj_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x32
Intrinsic     vmsullxr_v32_v32_v40_const[_p]
name
Spec syntax   vmsullxr {Dop [,conj][,const][,vmpsX]} vx[Xe], vy[Y], voz[0], ?vprX

Return type   vec40_t

              1    DOP             uint8     1..2              Number of atomic operations
              2    IN1_V32         vec_t                       Input vector operand

              3    IN1_OFST        uint8     0..7              Offset for the first DW used from operand
                                                               2

Operands      4    IN2_V32         vec_t                       Input vector operand

              5    IN2_OFST        uint8     0..7              Offset for the first DW used from operand
                                                               4

              6    IN3_V40         vec40_t                     Output vector operand
              7    IN_VPR          vprex_t                     Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;

C example     vprex_t vecPred;
              ...
              vRes = vmsullxr_v32_v32_v40_const_p (2, vIn, 0, vIn2, 0, vRes, vecPred);

                   IN_VPR last operand is relevant only for vmsullxr_v32_v32_v40_const_p
Comments      1.
                   version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x32
Intrinsic     vmsullxr_v32_v32_v40_const_vmpsX[_p]
name
Spec syntax   vmsullxr {Dop [,conj][,const][,vmpsX]} vx[Xe], vy[Y], voz[0], ?vprX

Return type   vec40_t

              1    DOP             uint8     1..2             Number of atomic operations
                                                              Selects the VMSNX and VPSX set within
              2    VMPSX           uint8     0,1
                                                              modv0/modv2 mode registers
              3    IN1_V32         vec_t                      Input vector operand

              4    IN1_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
Operands                                                      3

              5    IN2_V32         vec_t                      Input vector operand

              6    IN2_OFST        uint8     0..7             Offset for the first DW used from operand
                                                              5

              7    IN3_V40         vec40_t                    Output vector operand
              8    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsullxr_v32_v32_v40_const_vmpsX_p (2, 1, vIn, 0, vIn2, 0, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsullxr_v32_v32_v40_const_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x32
Intrinsic     vmsullxr_v32_v32_v40[_p]
name
Spec syntax   vmsullxr {Dop [,conj][,const][,vmpsX]} vx[Xe], vy[Y], voz[0], ?vprX

Return type   vec40_t

              1    DOP             uint8     1..2             Number of atomic operations
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
              vRes = vmsullxr_v32_v32_v40_p (2, vIn, 0, vIn2, 0, vRes, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmsullxr_v32_v32_v40_p version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x32
Intrinsic     vmsullxr_v32_v32_v40_vmpsX[_p]
name
Spec syntax   vmsullxr {Dop [,conj][,const][,vmpsX]} vx[Xe], vy[Y], voz[0], ?vprX

Return type   vec40_t

              1    DOP             uint8      1..2             Number of atomic operations
                                                               Selects the VMSNX and VPSX set within
              2    VMPSX           uint8      0,1
                                                               modv0/modv2 mode registers
              3    IN1_V32         vec_t                       Input vector operand

              4    IN1_OFST        uint8      0..7
                                                               Offset for the first DW used from operand
Operands                                                       3

              5    IN2_V32         vec_t                       Input vector operand

              6    IN2_OFST        uint8      0..7
                                                               Offset for the first DW used from operand
                                                               5

              7    IN3_V40         vec40_t                     Output vector operand
              8    IN_VPR          vprex_t                     Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsullxr_v32_v32_v40_vmpsX_p (2, 1, vIn, 0, vIn2, 0, vRes, vecPred);

                   IN_VPR last operand is relevant only for vmsullxr_v32_v32_v40_vmpsX_p
Comments      1.
                   version.

Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x32
Intrinsic     vmsullxr_v32_c32_v40_v40_conj[_p]
name
Spec syntax   vmsullxr {Qhop [,conj][,vmpsX]} vx[Xe], vcY, voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    QHOP            uint8     3..4             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand

              3    IN1_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
                                                              2
Operands      4    IN2_C32         coef_t                     Coefficient operand
              5    IN3_V40         vec40_t                    Output vector operand
              6    RES2_V40        vec40_t                    Output vector result operand
              7    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec40_t vRes1;
              vec40_t vRes2;
C example     coef_t vcoefIn;
              vprex_t vecPred;
              ...
              vRes1 = vmsullxr_v32_c32_v40_v40_conj_p (4, vIn, 0, vcoefIn, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vmsullxr_v32_c32_v40_v40_conj_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).


Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x32
Intrinsic     vmsullxr_v32_c32_v40_v40_conj_vmpsX[_p]
name
Spec syntax   vmsullxr {Qhop [,conj][,vmpsX]} vx[Xe], vcY, voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    QHOP            uint8     3..4             Number of atomic operations
                                                              Selects the VMSNX and VPSX set within
              2    VMPSX           uint8     0,1
                                                              modv0/modv2 mode registers
              3    IN1_V32         vec_t                      Input vector operand
Operands
              4    IN1_OFST        uint8     0..7             Offset for the first DW used from operand
                                                              3

5    IN2_C32         coef_t                     Coefficient operand
              6    IN3_V40         vec40_t                    Output vector operand
              7    RES2_V40        vec40_t                    Output vector result operand
              8    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec40_t vRes1;
              vec40_t vRes2;
C example     coef_t vcoefIn;
              vprex_t vecPred;
              ...
              vRes1 = vmsullxr_v32_c32_v40_v40_conj_vmpsX_p (4, 1, vIn, 0, vcoefIn, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vmsullxr_v32_c32_v40_v40_conj_vmpsX_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).


Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x32
Intrinsic     vmsullxr_v32_c32_v40_v40[_p]
name
Spec syntax   vmsullxr {Qhop [,conj][,vmpsX]} vx[Xe], vcY, voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    QHOP            uint8     3..4             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand

              3    IN1_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
                                                              2
Operands      4    IN2_C32         coef_t                     Coefficient operand
              5    IN3_V40         vec40_t                    Output vector operand
              6    RES2_V40        vec40_t                    Output vector result operand
              7    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec40_t vRes1;
              vec40_t vRes2;
C example     coef_t vcoefIn;
              vprex_t vecPred;
              ...
              vRes1 = vmsullxr_v32_c32_v40_v40_p (4, vIn, 0, vcoefIn, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for vmsullxr_v32_c32_v40_v40_p
              1.
                   version.
Comments           This intrinsic returns two results. The first result variable should be placed to

2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).

Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x32
Intrinsic     vmsullxr_v32_c32_v40_v40_vmpsX[_p]
name
Spec syntax   vmsullxr {Qhop [,conj][,vmpsX]} vx[Xe], vcY, voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    QHOP           uint8     3..4             Number of atomic operations
                                                             Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                             modv0/modv2 mode registers
              3    IN1_V32        vec_t                      Input vector operand

              4    IN1_OFST       uint8     0..7             Offset for the first DW used from operand
Operands                                                     3

              5    IN2_C32        coef_t                     Coefficient operand
              6    IN3_V40        vec40_t                    Output vector operand
              7    RES2_V40       vec40_t                    Output vector result operand
              8    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec40_t vRes1;
              vec40_t vRes2;
C example     coef_t vcoefIn;
              vprex_t vecPred;
              ...
              vRes1 = vmsullxr_v32_c32_v40_v40_vmpsX_p (4, 1, vIn, 0, vcoefIn, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vmsullxr_v32_c32_v40_v40_vmpsX_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).


Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x32
Intrinsic     vmsullxr_v32_c32_v40_conj[_p]
name
Spec syntax   vmsullxr {Dop [,conj][,vmpsX]} vx[Xe], vcY, voz[0], ?vprX

Return type   vec40_t

              1    DOP             uint8     1..2             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand

              3    IN1_OFST        uint8     0..7
                                                              Offset for the first DW used from operand

2
Operands
              4    IN2_C32         coef_t                     Coefficient operand
              5    IN3_V40         vec40_t                    Output vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec40_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vmsullxr_v32_c32_v40_conj_p (2, vIn, 0, vcoefIn, vRes, vecPred);

                   IN_VPR last operand is relevant only for vmsullxr_v32_c32_v40_conj_p
Comments      1.
                   version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x32
Intrinsic     vmsullxr_v32_c32_v40_conj_vmpsX[_p]
name
Spec syntax   vmsullxr {Dop [,conj][,vmpsX]} vx[Xe], vcY, voz[0], ?vprX

Return type   vec40_t

              1    DOP             uint8     1..2             Number of atomic operations
                                                              Selects the VMSNX and VPSX set within
              2    VMPSX           uint8     0,1
                                                              modv0/modv2 mode registers
              3    IN1_V32         vec_t                      Input vector operand
Operands      4    IN1_OFST        uint8                      Offset for the first DW used from operand
                                             0..7
                                                              3

              5    IN2_C32         coef_t                     Coefficient operand
              6    IN3_V40         vec40_t                    Output vector operand
              7    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec40_t vRes;
C example     coef_t vcoefIn;
              vprex_t vecPred;
              ...
              vRes = vmsullxr_v32_c32_v40_conj_vmpsX_p (2, 1, vIn, 0, vcoefIn, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsullxr_v32_c32_v40_conj_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x32
Intrinsic     vmsullxr_v32_c32_v40[_p]
name
Spec syntax   vmsullxr {Dop [,conj][,vmpsX]} vx[Xe], vcY, voz[0], ?vprX

Return type   vec40_t

              1    DOP             uint8     1..2              Number of atomic operations
              2    IN1_V32         vec_t                       Input vector operand

3    IN1_OFST        uint8     0..7
                                                               Offset for the first DW used from operand
                                                               2
Operands
              4    IN2_C32         coef_t                      Coefficient operand
              5    IN3_V40         vec40_t                     Output vector operand
              6    IN_VPR          vprex_t                     Vector predicate operand
              vec_t vIn;
              vec40_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vmsullxr_v32_c32_v40_p (2, vIn, 0, vcoefIn, vRes, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmsullxr_v32_c32_v40_p version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x32
Intrinsic     vmsullxr_v32_c32_v40_vmpsX[_p]
name
Spec syntax   vmsullxr {Dop [,conj][,vmpsX]} vx[Xe], vcY, voz[0], ?vprX

Return type   vec40_t

              1    DOP             uint8     1..2              Number of atomic operations

              2
                                                               Selects the VMSNX and VPSX set within
                   VMPSX           uint8     0,1
                                                               modv0/modv2 mode registers
              3    IN1_V32         vec_t                       Input vector operand
Operands
              4    IN1_OFST        uint8     0..7
                                                               Offset for the first DW used from operand
                                                               3

              5    IN2_C32         coef_t                      Coefficient operand
              6    IN3_V40         vec40_t                     Output vector operand
            7    IN_VPR          vprex_t                    Vector predicate operand
            vec_t vIn;
            vec40_t vRes;
            coef_t vcoefIn;
C example   vprex_t vecPred;
            ...
            vRes = vmsullxr_v32_c32_v40_vmpsX_p (2, 1, vIn, 0, vcoefIn, vRes, vecPred);

                 IN_VPR last operand is relevant only for vmsullxr_v32_c32_v40_vmpsX_p
Comments    1.
                 version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x32
Intrinsic     vmsullxr_v32_v32_v40_v40_conj_const[_p]
name
Spec syntax   vmsullxr {Qhop [,conj][,const][,vmpsX]} vx[Xe], vy[Y], voz1[0], voz2[0], ?vprX

Return type   vec40_t

1    QHOP            uint8     3..4             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand

              3    IN1_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
                                                              2

              4    IN2_V32         vec_t                      Input vector operand
Operands
              5    IN2_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
                                                              4

              6    IN3_V40         vec40_t                    Output vector operand
              7    RES2_V40        vec40_t                    Output vector result operand
              8    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes1;
C example     vec40_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vmsullxr_v32_v32_v40_v40_conj_const_p (4, vIn, 0, vIn2, 0, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vmsullxr_v32_v32_v40_v40_conj_const_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).


Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x32
Intrinsic     vmsullxr_v32_v32_v40_v40_conj_const_vmpsX[_p]
name
Spec syntax   vmsullxr {Qhop [,conj][,const][,vmpsX]} vx[Xe], vy[Y], voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    QHOP            uint8     3..4             Number of atomic operations
                                                              Selects the VMSNX and VPSX set within
              2    VMPSX           uint8     0,1
                                                              modv0/modv2 mode registers
Operands
              3    IN1_V32         vec_t                      Input vector operand

              4    IN1_OFST        uint8     0..7
                                                              Offset for the first DW used from operand

3
              5    IN2_V32         vec_t                      Input vector operand

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
              vRes1 = vmsullxr_v32_v32_v40_v40_conj_const_vmpsX_p (4, 1, vIn, 0, vIn2, 0, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vmsullxr_v32_v32_v40_v40_conj_const_vmpsX_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).


Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x32
Intrinsic     vmsullxr_v32_v32_v40_v40_conj[_p]
name
Spec syntax   vmsullxr {Qhop [,conj][,const][,vmpsX]} vx[Xe], vy[Y], voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    QHOP            uint8     3..4             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand

              3    IN1_OFST        uint8     0..7             Offset for the first DW used from operand
                                                              2

              4    IN2_V32         vec_t                      Input vector operand
Operands
              5    IN2_OFST        uint8     0..7             Offset for the first DW used from operand
                                                              4

              6    IN3_V40         vec40_t                    Output vector operand
              7    RES2_V40        vec40_t                    Output vector result operand
              8    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes1;
C example     vec40_t vRes2;
              vprex_t vecPred;
              ...

vRes1 = vmsullxr_v32_v32_v40_v40_conj_p (4, vIn, 0, vIn2, 0, vRes1, vRes2, vecPred);
                   IN_VPR last operand is relevant only for
              1.
                   vmsullxr_v32_v32_v40_v40_conj_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).


Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x32
Intrinsic     vmsullxr_v32_v32_v40_v40_conj_vmpsX[_p]
name
Spec syntax   vmsullxr {Qhop [,conj][,const][,vmpsX]} vx[Xe], vy[Y], voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    QHOP           uint8     3..4             Number of atomic operations
                                                             Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                             modv0/modv2 mode registers
              3    IN1_V32        vec_t                      Input vector operand

              4    IN1_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             3
Operands      5    IN2_V32        vec_t                      Input vector operand

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
              vRes1 = vmsullxr_v32_v32_v40_v40_conj_vmpsX_p (4, 1, vIn, 0, vIn2, 0, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vmsullxr_v32_v32_v40_v40_conj_vmpsX_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).

Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x32
Intrinsic     vmsullxr_v32_v32_v40_v40_const[_p]
name
Spec syntax   vmsullxr {Qhop [,conj][,const][,vmpsX]} vx[Xe], vy[Y], voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    QHOP            uint8     3..4             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand

              3    IN1_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
                                                              2

              4    IN2_V32         vec_t                      Input vector operand
Operands
              5    IN2_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
                                                              4

              6    IN3_V40         vec40_t                    Output vector operand
              7    RES2_V40        vec40_t                    Output vector result operand
              8    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes1;
C example     vec40_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vmsullxr_v32_v32_v40_v40_const_p (4, vIn, 0, vIn2, 0, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vmsullxr_v32_v32_v40_v40_const_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).


Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x32
Intrinsic     vmsullxr_v32_v32_v40_v40_const_vmpsX[_p]
name
Spec syntax   vmsullxr {Qhop [,conj][,const][,vmpsX]} vx[Xe], vy[Y], voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    QHOP            uint8     3..4             Number of atomic operations
                                                              Selects the VMSNX and VPSX set within
              2    VMPSX           uint8     0,1
                                                              modv0/modv2 mode registers

3    IN1_V32         vec_t                      Input vector operand
Operands
              4    IN1_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
                                                              3

              5    IN2_V32         vec_t                      Input vector operand
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
              vRes1 = vmsullxr_v32_v32_v40_v40_const_vmpsX_p (4, 1, vIn, 0, vIn2, 0, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vmsullxr_v32_v32_v40_v40_const_vmpsX_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).


Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x32
Intrinsic     vmsullxr_v32_v32_v40_v40[_p]
name
Spec syntax   vmsullxr {Qhop [,conj][,const][,vmpsX]} vx[Xe], vy[Y], voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    QHOP            uint8     3..4             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand

              3    IN1_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
                                                              2

              4    IN2_V32         vec_t                      Input vector operand
Operands
              5    IN2_OFST        uint8     0..7             Offset for the first DW used from operand
                                                              4

              6    IN3_V40         vec40_t                    Output vector operand

7    RES2_V40        vec40_t                    Output vector result operand
              8    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes1;
C example     vec40_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vmsullxr_v32_v32_v40_v40_p (4, vIn, 0, vIn2, 0, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for vmsullxr_v32_v32_v40_v40_p
Comments      1.
                   version.
                   This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).


Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x32
Intrinsic     vmsullxr_v32_v32_v40_v40_vmpsX[_p]
name
Spec syntax   vmsullxr {Qhop [,conj][,const][,vmpsX]} vx[Xe], vy[Y], voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    QHOP           uint8      3..4             Number of atomic operations
                                                              Selects the VMSNX and VPSX set within
              2    VMPSX          uint8      0,1
                                                              modv0/modv2 mode registers
              3    IN1_V32        vec_t                       Input vector operand

              4    IN1_OFST       uint8      0..7             Offset for the first DW used from operand
                                                              3
Operands      5    IN2_V32        vec_t                       Input vector operand

              6    IN2_OFST       uint8      0..7             Offset for the first DW used from operand
                                                              5

              7    IN3_V40        vec40_t                     Output vector operand
              8    RES2_V40       vec40_t                     Output vector result operand
              9    IN_VPR         vprex_t                     Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes1;
C example     vec40_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vmsullxr_v32_v32_v40_v40_vmpsX_p (4, 1, vIn, 0, vIn2, 0, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.

vmsullxr_v32_v32_v40_v40_vmpsX_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).


Main table → Multiplication → Multiply-Subtract → Semi-Complex 32x32
