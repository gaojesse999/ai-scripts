# Floating Point → Float Special Operations → Vector Floating Point Square

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Floating Point → Float Special Operations → Vector Floating Point Square
Root Mantissa

Vector Floating Point Square Root Mantissa

Vector Floating Point Square Root Mantissa
Performs a square-root operation on the floating-point source’s 16 MSBs of the mantissa value
(including the hidden 1 bit). This instruction is part of the non-native VFLPSQRT operation.
Available Switches
None
Intrinsic Names
vflpsqrtmnt_v32_v32
Instruction details in the instruction set specification
Intrinsic     vflpsqrtmnt_v32_v32[_p]
name
Spec syntax   vflpsqrtmnt vx[X], vz[Z]l, ?vprX

Return type   vec_t

              1    IN1_V32        vec_t                      Input vector operand

              2    IN1_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             1

                                                             Offset for the first DW used from the
Operands      3    OUT_OFST       uint8     0..7
                                                             result operand
                                                             Word part which is used for the result
              4    OUT_PART       uint8     LOW,HIGH
                                                             operand
              5    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vflpsqrtmnt_v32_v32_p (vIn, 0, 0, LOW, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vflpsqrtmnt_v32_v32_p version.


Main table → Floating Point → Float Special Operations → Vector Floating Point Square
Root Mantissa

Main table → Floating Point → Float Special Operations → Vector Floating Point Square
Root Result Concat

Vector Floating Point Square Root Result Concat

Vector Floating Point Square Root Result Concat

Calculate the exponent value for the reciprocal value of the 32-bit single precision floating point
source, compute the correct mantissa value and concatenate the final result. This instruction is
part of the non-native VFLPSQRT operation.
Available Switches
None
Intrinsic Names
vflpsqrtcnct_v32_v32_v32_v32
Instruction details in the instruction set specification
Intrinsic     vflpsqrtcnct_v32_v32_v32_v32[_p]
name
Spec syntax   vflpsqrtcnct {Oop} vx[0], vy[0], vip[0]l, vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8            Number of atomic operations
              2    IN1_V32         vec_t                     Input vector operand
              3    IN2_V32         vec_t                     Input vector operand
Operands
              4    IN3_V32         vec_t                     Input vector operand
              5    IN3_PART        uint8     LOW,HIGH        Word part which is used for operand 4
              6    IN_VPR          vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
C example     vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vflpsqrtcnct_v32_v32_v32_v32_p (8, vIn, vIn2, vIn3, LOW, vecPred);

                   IN_VPR last operand is relevant only for vflpsqrtcnct_v32_v32_v32_v32_p
Comments      1.
                   version.


Main table → Floating Point → Float Special Operations → Vector Floating Point Square
Root Result Concat

Main table → Floating Point → Float Special Operations → Vector Floating Point Square
Root To Reciprocal Input

Vector Floating Point Square Root To Reciprocal Input

Vector Floating Point Square Root To Reciprocal Input
Calculate and choose the correct square root approximation for the reciprocal calculation of the
reciprocal square root SW sequence. This instruction is part of the non-native VFLPSQRTINR
operation.
Available Switches
None
Intrinsic Names
vflpsqrt2div_v32_v32_v32_v32_v32
Instruction details in the instruction set specification
Intrinsic     vflpsqrt2div_v32_v32_v32_v32_v32[_p]
name
Spec syntax   vflpsqrt2div {Oop} vx[0], vy[0], vip[0], vz1[0], vz2[0]l, ?vprX

Return type   vec_t

              1    OOP             uint8     1..8             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand
              3    IN2_V32         vec_t                      Input vector operand
Operands

4    IN3_V32         vec_t                      Input vector operand
              5    RES2_V32        vec_t                      Input vector result operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vRes1;
C example     vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vflpsqrt2div_v32_v32_v32_v32_v32_p (8, vIn, vIn2, vIn3, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vflpsqrt2div_v32_v32_v32_v32_v32_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Floating Point → Float Special Operations → Vector Floating Point Square
Root To Reciprocal Input

Main table → Floating Point → Float Special Operations → Vector Floating Point Square
Root With N-R Mantissa

Vector Floating Point Square Root With N-R Mantissa

Vector Floating Point Square Root With N-R Mantissa
Performs a square-root operation on the floating-point source’s 16 MSBs of the mantissa value
(including the hidden 1 bit). This instruction is part of the non-native VFLPSQRTNR operation.
Available Switches
None
Intrinsic Names
vflpsqrtnrmnt_v32_v32_v32
Instruction details in the instruction set specification
Intrinsic     vflpsqrtnrmnt_v32_v32_v32[_p]
name
Spec syntax   vflpsqrtnrmnt vx[X], vz1[Z]l, vz2[Z], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand

              2    IN1_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
                                                              1

              3    IN2_V32         vec_t                      Input vector operand
Operands                                                      Offset for the first DW used from the first
              4    RES1_OFST       uint8     0..7
                                                              result operand
                                                              Offset for the first DW used from the
              5    RES2_OFST       uint8     0..7

second result operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes1;
              vec_t vRes2;
C example     vprex_t vecPred;
              ...
              vRes1 = vflpsqrtnrmnt_v32_v32_v32_p (vIn, 0, vRes2, 0, 0, vecPred);

                   IN_VPR last operand is relevant only for vflpsqrtnrmnt_v32_v32_v32_p
              1.
                   version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_OFST).


Main table → Floating Point → Float Special Operations → Vector Floating Point Square
Root With N-R Mantissa
