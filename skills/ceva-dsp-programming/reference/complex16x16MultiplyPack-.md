# Multiplication → Multiply-Accumulate → Complex 16x16 Multiply Pack-

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Multiplication → Multiply-Accumulate → Complex 16x16 Multiply Pack-
Accumulate and Subtract

Complex 16x16 Multiply Pack-Accumulate and Subtract

Complex 16x16 Multiply Pack-Accumulate and Subtract
Performs complex multiply-pack accumulate and subtract between two complex numbers. Each
complex source consists of real 16-bit part and imaginary 16-bit part. Each of the real and the
imaginary products are accumulated with and subtracted from the 20-bit accumulator. The
accumulation result is written to 20-bit destination. The subtarction result is written to a 16-bit or
20-bit destination.
Available Switches
                Number of atomic operations. An atomic operation is defined as two multiply pack-
Oop
                accumulate and subtract operations. 1op ≤ Oop ≤ 8op
conj            Performs complex multiply-accumulate using complex conjugate of vcY/vy[Y]
const           When used, vy[Y] is constant throughout the operations.
vmpsX           Selects the VMSNX and VPSX set within modv0 or modv2 mode registers.
Intrinsic Names
vmacsxp_v32_c32_v40_v32_conj
vmacsxp_v32_c32_v40_v32_conj_vmpsX
vmacsxp_v32_c32_v40_v32
vmacsxp_v32_c32_v40_v32_vmpsX
vmacsxp_v32_v32_v40_v32_conj
vmacsxp_v32_v32_v40_v32_conj_vmpsX
vmacsxp_v32_v32_v40_v32_const_conj
vmacsxp_v32_v32_v40_v32_const_conj_vmpsX
vmacsxp_v32_v32_v40_v32_const
vmacsxp_v32_v32_v40_v32_const_vmpsX
vmacsxp_v32_v32_v40_v32
vmacsxp_v32_v32_v40_v32_vmpsX
Instruction details in the instruction set specification

Intrinsic     vmacsxp_v32_c32_v40_v32_conj[_p]
name
Spec syntax   vmacsxp {Oop [,conj][,vmpsX]} vx[X], vcY, voz[0], vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             2
Operands      4    IN2_C32        coef_t                     Coefficient operand
              5    IN3_V40        vec40_t                    Output vector operand
              6    RES2_V32       vec_t                      Input vector result operand
              7    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec40_t vRes1;
              vec_t vRes2;
C example     coef_t vcoefIn;
              vprex_t vecPred;
              ...
              vRes1 = vmacsxp_v32_c32_v40_v32_conj_p (8, vIn, 0, vcoefIn, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vmacsxp_v32_c32_v40_v32_conj_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Multiplication → Multiply-Accumulate → Complex 16x16 Multiply Pack-
Accumulate and Subtract
Intrinsic     vmacsxp_v32_c32_v40_v32_conj_vmpsX[_p]
name
Spec syntax   vmacsxp {Oop [,conj][,vmpsX]} vx[X], vcY, voz[0], vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations
                                                             Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                             modv0/modv2 mode registers
Operands      3    IN1_V32        vec_t                      Input vector operand

              4    IN1_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             3

              5    IN2_C32        coef_t                     Coefficient operand

6    IN3_V40        vec40_t                     Output vector operand
              7    RES2_V32       vec_t                       Input vector result operand
              8    IN_VPR         vprex_t                     Vector predicate operand
              vec_t vIn;
              vec40_t vRes1;
              vec_t vRes2;
C example     coef_t vcoefIn;
              vprex_t vecPred;
              ...
              vRes1 = vmacsxp_v32_c32_v40_v32_conj_vmpsX_p (8, 1, vIn, 0, vcoefIn, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vmacsxp_v32_c32_v40_v32_conj_vmpsX_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Multiplication → Multiply-Accumulate → Complex 16x16 Multiply Pack-
Accumulate and Subtract
Intrinsic     vmacsxp_v32_c32_v40_v32[_p]
name
Spec syntax   vmacsxp {Oop [,conj][,vmpsX]} vx[X], vcY, voz[0], vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8      1..8             Number of atomic operations
              2    IN1_V32        vec_t                       Input vector operand

              3    IN1_OFST       uint8      0..7             Offset for the first DW used from operand
                                                              2
Operands      4    IN2_C32        coef_t                      Coefficient operand
              5    IN3_V40        vec40_t                     Output vector operand
              6    RES2_V32       vec_t                       Input vector result operand
              7    IN_VPR         vprex_t                     Vector predicate operand
              vec_t vIn;
              vec40_t vRes1;
              vec_t vRes2;
C example     coef_t vcoefIn;
              vprex_t vecPred;
              ...
              vRes1 = vmacsxp_v32_c32_v40_v32_p (8, vIn, 0, vcoefIn, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for vmacsxp_v32_c32_v40_v32_p
              1.
                   version.
Comments
                   This intrinsic returns two results. The first result variable should be placed to
              2.
                   the left of the = sign (lvalue). The second result variable should be passed as

an additional parameter (RES2_V32).


Main table → Multiplication → Multiply-Accumulate → Complex 16x16 Multiply Pack-
Accumulate and Subtract
Intrinsic     vmacsxp_v32_c32_v40_v32_vmpsX[_p]
name
Spec syntax   vmacsxp {Oop [,conj][,vmpsX]} vx[X], vcY, voz[0], vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations
                                                             Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                             modv0/modv2 mode registers
              3    IN1_V32        vec_t                      Input vector operand

              4    IN1_OFST       uint8     0..7             Offset for the first DW used from operand
Operands                                                     3

              5    IN2_C32        coef_t                     Coefficient operand
              6    IN3_V40        vec40_t                    Output vector operand
              7    RES2_V32       vec_t                      Input vector result operand
              8    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec40_t vRes1;
              vec_t vRes2;
C example     coef_t vcoefIn;
              vprex_t vecPred;
              ...
              vRes1 = vmacsxp_v32_c32_v40_v32_vmpsX_p (8, 1, vIn, 0, vcoefIn, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vmacsxp_v32_c32_v40_v32_vmpsX_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Multiplication → Multiply-Accumulate → Complex 16x16 Multiply Pack-
Accumulate and Subtract
Intrinsic     vmacsxp_v32_v32_v40_v32_conj[_p]
name
Spec syntax   vmacsxp {Oop [,const][,conj][,vmpsX]} vx[X], vy[Y], voz[0], vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8             Number of atomic operations
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
              7    RES2_V32        vec_t                      Input vector result operand
              8    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes1;
C example     vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vmacsxp_v32_v32_v40_v32_conj_p (8, vIn, 0, vIn2, 0, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vmacsxp_v32_v32_v40_v32_conj_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Multiplication → Multiply-Accumulate → Complex 16x16 Multiply Pack-
Accumulate and Subtract
Intrinsic     vmacsxp_v32_v32_v40_v32_conj_vmpsX[_p]
name
Spec syntax   vmacsxp {Oop [,const][,conj][,vmpsX]} vx[X], vy[Y], voz[0], vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8             Number of atomic operations
                                                              Selects the VMSNX and VPSX set within
              2    VMPSX           uint8     0,1
                                                              modv0/modv2 mode registers
Operands
              3    IN1_V32         vec_t                      Input vector operand

              4    IN1_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
                                                              3
              5    IN2_V32        vec_t                      Input vector operand

              6    IN2_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             5

              7    IN3_V40        vec40_t                    Output vector operand

8    RES2_V32       vec_t                      Input vector result operand
              9    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes1;
C example     vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vmacsxp_v32_v32_v40_v32_conj_vmpsX_p (8, 1, vIn, 0, vIn2, 0, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vmacsxp_v32_v32_v40_v32_conj_vmpsX_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Multiplication → Multiply-Accumulate → Complex 16x16 Multiply Pack-
Accumulate and Subtract
Intrinsic     vmacsxp_v32_v32_v40_v32_const_conj[_p]
name
Spec syntax   vmacsxp {Oop [,const][,conj][,vmpsX]} vx[X], vy[Y], voz[0], vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             2

              4    IN2_V32        vec_t                      Input vector operand
Operands
              5    IN2_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             4

              6    IN3_V40        vec40_t                    Output vector operand
              7    RES2_V32       vec_t                      Input vector result operand
              8    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes1;
C example     vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vmacsxp_v32_v32_v40_v32_const_conj_p (8, vIn, 0, vIn2, 0, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vmacsxp_v32_v32_v40_v32_const_conj_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to

2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Multiplication → Multiply-Accumulate → Complex 16x16 Multiply Pack-
Accumulate and Subtract
Intrinsic     vmacsxp_v32_v32_v40_v32_const_conj_vmpsX[_p]
name
Spec syntax   vmacsxp {Oop [,const][,conj][,vmpsX]} vx[X], vy[Y], voz[0], vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8      1..8            Number of atomic operations
                                                             Selects the VMSNX and VPSX set within
              2    VMPSX          uint8      0,1
                                                             modv0/modv2 mode registers
              3    IN1_V32        vec_t                      Input vector operand

              4    IN1_OFST       uint8      0..7            Offset for the first DW used from operand
                                                             3
Operands      5    IN2_V32        vec_t                      Input vector operand

              6    IN2_OFST       uint8      0..7            Offset for the first DW used from operand
                                                             5

              7    IN3_V40        vec40_t                    Output vector operand
              8    RES2_V32       vec_t                      Input vector result operand
              9    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes1;
C example     vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vmacsxp_v32_v32_v40_v32_const_conj_vmpsX_p (8, 1, vIn, 0, vIn2, 0, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vmacsxp_v32_v32_v40_v32_const_conj_vmpsX_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Multiplication → Multiply-Accumulate → Complex 16x16 Multiply Pack-
Accumulate and Subtract
Intrinsic     vmacsxp_v32_v32_v40_v32_const[_p]
name
Spec syntax   vmacsxp {Oop [,const][,conj][,vmpsX]} vx[X], vy[Y], voz[0], vz[0], ?vprX

Return type   vec_t

1    OOP             uint8     1..8             Number of atomic operations
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
              7    RES2_V32        vec_t                      Input vector result operand
              8    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes1;
C example     vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vmacsxp_v32_v32_v40_v32_const_p (8, vIn, 0, vIn2, 0, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vmacsxp_v32_v32_v40_v32_const_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Multiplication → Multiply-Accumulate → Complex 16x16 Multiply Pack-
Accumulate and Subtract
Intrinsic     vmacsxp_v32_v32_v40_v32_const_vmpsX[_p]
name
Spec syntax   vmacsxp {Oop [,const][,conj][,vmpsX]} vx[X], vy[Y], voz[0], vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8             Number of atomic operations
                                                              Selects the VMSNX and VPSX set within
              2    VMPSX           uint8     0,1
                                                              modv0/modv2 mode registers
Operands
              3    IN1_V32         vec_t                      Input vector operand

              4    IN1_OFST        uint8     0..7
                                                              Offset for the first DW used from operand

3
              5    IN2_V32        vec_t                      Input vector operand

              6    IN2_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             5

              7    IN3_V40        vec40_t                    Output vector operand
              8    RES2_V32       vec_t                      Input vector result operand
              9    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes1;
C example     vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vmacsxp_v32_v32_v40_v32_const_vmpsX_p (8, 1, vIn, 0, vIn2, 0, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vmacsxp_v32_v32_v40_v32_const_vmpsX_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Multiplication → Multiply-Accumulate → Complex 16x16 Multiply Pack-
Accumulate and Subtract
Intrinsic     vmacsxp_v32_v32_v40_v32[_p]
name
Spec syntax   vmacsxp {Oop [,const][,conj][,vmpsX]} vx[X], vy[Y], voz[0], vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             2

              4    IN2_V32        vec_t                      Input vector operand
Operands
              5    IN2_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             4

              6    IN3_V40        vec40_t                    Output vector operand
              7    RES2_V32       vec_t                      Input vector result operand
              8    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes1;
C example     vec_t vRes2;
              vprex_t vecPred;
              ...

vRes1 = vmacsxp_v32_v32_v40_v32_p (8, vIn, 0, vIn2, 0, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for vmacsxp_v32_v32_v40_v32_p
              1.
                   version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Multiplication → Multiply-Accumulate → Complex 16x16 Multiply Pack-
Accumulate and Subtract
Intrinsic     vmacsxp_v32_v32_v40_v32_vmpsX[_p]
name
Spec syntax   vmacsxp {Oop [,const][,conj][,vmpsX]} vx[X], vy[Y], voz[0], vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8             Number of atomic operations
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
              8    RES2_V32        vec_t                      Input vector result operand
              9    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes1;
C example     vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vmacsxp_v32_v32_v40_v32_vmpsX_p (8, 1, vIn, 0, vIn2, 0, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vmacsxp_v32_v32_v40_v32_vmpsX_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).

Main table → Multiplication → Multiply-Accumulate → Complex 16x16 Multiply Pack-
Accumulate and Subtract
