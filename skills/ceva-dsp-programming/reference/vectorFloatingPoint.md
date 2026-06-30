# Floating Point → Float Special Operations → Vector Floating Point

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Floating Point → Float Special Operations → Vector Floating Point
Reciprocal Result with N-R Concat

Vector Floating Point Reciprocal Result with N-R Concat

Vector Floating Point Reciprocal Result with N-R Concat
Calculate the exponent value for the reciprocal value of the 32-bit single precision floating point
source, compute the correct mantissa value and concatenate the final result. This instruction is
part of the VFLPDIVNR Macro operation.
Available Switches
None
Intrinsic Names
vflprcpnrcnct_v32_v32_v32
Instruction details in the instruction set specification
Intrinsic     vflprcpnrcnct_v32_v32_v32[_p]
name
Spec syntax   vflprcpnrcnct {Oop} vx[0], vy[0], vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand
Operands
              3    IN2_V32         vec_t                      Input vector operand
              4    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vflprcpnrcnct_v32_v32_v32_p (8, vIn, vIn2, vecPred);

IN_VPR last operand is relevant only for vflprcpnrcnct_v32_v32_v32_p
Comments      1.
                   version.


Main table → Floating Point → Float Special Operations → Vector Floating Point
Reciprocal Result with N-R Concat

Main table → Floating Point → Float Special Operations → Vector Floating Point
Constant Shift

Vector Floating Point Constant Shift

Vector Floating Point Constant Shift
Performs a constant right shift by 30 (>>30) on a 64-bit source, and packs the result into 32 bits.
This instruction is part of the non-native VFLPSQRT, VFLPSQRTI operations.
Available Switches
None
Intrinsic Names
vflpshift_v32_v32_v32
vflpshift_v32_v32_v32_rcp
vflpshift_v32_v32
vflpshift_v32_v32_rcp
Instruction details in the instruction set specification
Intrinsic     vflpshift_v32_v32_v32[_p]
name
Spec syntax   vflpshift {Ohop [,rcp]} vx[0], vy[0], vz[0], ?vprX

Return type   vec_t

              1    OHOP            uint8      5..8             Number of atomic operations
              2    IN1_V32         vec_t                       Input vector operand
Operands
              3    IN2_V32         vec_t                       Input vector operand
              4    IN_VPR          vprex_t                     Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vflpshift_v32_v32_v32_p (8, vIn, vIn2, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vflpshift_v32_v32_v32_p version.


Main table → Floating Point → Float Special Operations → Vector Floating Point
Constant Shift
Intrinsic     vflpshift_v32_v32_v32_rcp[_p]
name
Spec syntax   vflpshift {Ohop [,rcp]} vx[0], vy[0], vz[0], ?vprX

Return type   vec_t

              1    OHOP            uint8      5..8             Number of atomic operations
              2    IN1_V32         vec_t                       Input vector operand
Operands
              3    IN2_V32         vec_t                       Input vector operand
              4    IN_VPR          vprex_t                     Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vflpshift_v32_v32_v32_rcp_p (8, vIn, vIn2, vecPred);

                   IN_VPR last operand is relevant only for vflpshift_v32_v32_v32_rcp_p
Comments      1.
                   version.

Main table → Floating Point → Float Special Operations → Vector Floating Point
Constant Shift
Intrinsic     vflpshift_v32_v32[_p]
name
Spec syntax   vflpshift {Qop [,rcp]} vx[0], vz[0], ?vprX

Return type   vec_t

              1    QOP              uint8     1..4               Number of atomic operations
              2    IN1_V32          vec_t                        Input vector operand
Operands                                                         Offset for the first DW used from the
              3    OUT_OFST         uint8     0,4
                                                                 result operand
              4    IN_VPR           vprex_t                      Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vflpshift_v32_v32_p (4, vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vflpshift_v32_v32_p version.


Main table → Floating Point → Float Special Operations → Vector Floating Point
Constant Shift
Intrinsic     vflpshift_v32_v32_rcp[_p]
name
Spec syntax   vflpshift {Qop [,rcp]} vx[0], vz[0], ?vprX

Return type   vec_t

              1    QOP              uint8     1..4               Number of atomic operations
              2    IN1_V32          vec_t                        Input vector operand
Operands                                                         Offset for the first DW used from the
              3    OUT_OFST         uint8     0,4
                                                                 result operand
              4    IN_VPR           vprex_t                      Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vflpshift_v32_v32_rcp_p (4, vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vflpshift_v32_v32_rcp_p version.


Main table → Floating Point → Float Special Operations → Vector Floating Point
Constant Shift

Main table → Floating Point → Float Special Operations → Vector Floating Point
Reciprcoal SQRT Mantissa

Vector Floating Point Reciprcoal SQRT Mantissa

Vector Floating Point Reciprcoal SQRT Mantissa
Performs a square-root operation on the floating-point source’s 16 MSBs of the mantissa value
(including the hidden 1 bit). This instruction is part of the non-native VFLPSQRTI operation.
Available Switches
None
Intrinsic Names
vflpsqrtimnt_v32_v32

Instruction details in the instruction set specification
Intrinsic     vflpsqrtimnt_v32_v32[_p]
name
Spec syntax   vflpsqrtimnt vx[X], vz[Z]l, ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                     Input vector operand

              2    IN1_OFST        uint8     0..7
                                                             Offset for the first DW used from operand
                                                             1

                                                             Offset for the first DW used from the
Operands      3    OUT_OFST        uint8     0..7
                                                             result operand
                                                             Word part which is used for the result
              4    OUT_PART        uint8     LOW,HIGH
                                                             operand
              5    IN_VPR          vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vflpsqrtimnt_v32_v32_p (vIn, 0, 0, LOW, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vflpsqrtimnt_v32_v32_p version.


Main table → Floating Point → Float Special Operations → Vector Floating Point
Reciprcoal SQRT Mantissa

Main table → Floating Point → Float Special Operations → Vector Floating Point
Reciprocal Mantissa

Vector Floating Point Reciprocal Mantissa

Vector Floating Point Reciprocal Mantissa
Performs a reciprocal operation on the floating-point source’s 16 MSBs of the mantissa value
(including the hidden 1 bit). This instruction is part of the non-native VFLPDIV operation.
Available Switches
None
Intrinsic Names
vflprcpmnt_v32_v32
Instruction details in the instruction set specification
Intrinsic     vflprcpmnt_v32_v32[_p]
name
Spec syntax   vflprcpmnt vx[X], vz[Z]l, ?vprX

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
              vRes = vflprcpmnt_v32_v32_p (vIn, 0, 0, LOW, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vflprcpmnt_v32_v32_p version.


Main table → Floating Point → Float Special Operations → Vector Floating Point
Reciprocal Mantissa

Main table → Floating Point → Float Special Operations → Vector Floating Point
Reciprocal Mantissa With N-R

Vector Floating Point Reciprocal Mantissa With N-R

Vector Floating Point Reciprocal Mantissa With N-R
Performs a reciprocal operation on the floating-point source’s 16 MSBs of the mantissa value
(including the hidden 1 bit). This instruction is part of the VFLPDIVNR operation.
Available Switches
None
Intrinsic Names
vflprcpnrmnt_v32_v32_v32
Instruction details in the instruction set specification
Intrinsic     vflprcpnrmnt_v32_v32_v32[_p]
name
Spec syntax   vflprcpnrmnt vx[X], vz1[Z]l, vz2[Z], ?vprX

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
              vRes1 = vflprcpnrmnt_v32_v32_v32_p (vIn, 0, vRes2, 0, 0, vecPred);

                   IN_VPR last operand is relevant only for vflprcpnrmnt_v32_v32_v32_p
              1.

version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_OFST).


Main table → Floating Point → Float Special Operations → Vector Floating Point
Reciprocal Mantissa With N-R

Main table → Floating Point → Float Special Operations → Vector Floating Point
Reciprocal Result Concat

Vector Floating Point Reciprocal Result Concat

Vector Floating Point Reciprocal Result Concat
Calculate the exponent value for the reciprocal value of the 32-bit single precision floating point
source, compute the correct mantissa value and concatenate the final result. This instruction is
part of the non-native VFLPDIV operation.
Available Switches
None
Intrinsic Names
vflprcpcnct_v32_v32_v32
Instruction details in the instruction set specification
Intrinsic     vflprcpcnct_v32_v32_v32[_p]
name
Spec syntax   vflprcpcnct {Oop} vx[0], vy[0]l, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8              Number of atomic operations
              2    IN1_V32        vec_t                       Input vector operand
Operands      3    IN2_V32        vec_t                       Input vector operand
              4    IN2_PART       uint8     LOW,HIGH          Word part which is used for operand 3
              5    IN_VPR         vprex_t                     Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vflprcpcnct_v32_v32_v32_p (8, vIn, vIn2, LOW, vecPred);

                   IN_VPR last operand is relevant only for vflprcpcnct_v32_v32_v32_p
Comments      1.
                   version.


Main table → Floating Point → Float Special Operations → Vector Floating Point
Reciprocal Result Concat

Main table → Floating Point → Float Special Operations → Vector Floating Point
Reciprocal SQRT Result Concat

Vector Floating Point Reciprocal SQRT Result Concat

Vector Floating Point Reciprocal SQRT Result Concat
Calculate the exponent value for the reciprocal value of the 32-bit single precision floating point
source, compute the correct mantissa value and concatenate the final result. This instruction is
part of the non-native VFLPSQRTI operation.
Available Switches
None
Intrinsic Names
vflpsqrticnct_v32_v32_v32_v32

Instruction details in the instruction set specification
Intrinsic     vflpsqrticnct_v32_v32_v32_v32[_p]
name
Spec syntax   vflpsqrticnct {Oop} vx[0], vy[0], vip[0]l, vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand
              3    IN2_V32         vec_t                      Input vector operand
Operands
              4    IN3_V32         vec_t                      Input vector operand
              5    IN3_PART        uint8     LOW,HIGH         Word part which is used for operand 4
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
C example     vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vflpsqrticnct_v32_v32_v32_v32_p (8, vIn, vIn2, vIn3, LOW, vecPred);

                   IN_VPR last operand is relevant only for vflpsqrticnct_v32_v32_v32_v32_p
Comments      1.
                   version.


Main table → Floating Point → Float Special Operations → Vector Floating Point
Reciprocal SQRT Result Concat

Main table → Floating Point → Float Special Operations → Vector Floating Point
Reciprocal SQRT With N-R result Concat

Vector Floating Point Reciprocal SQRT With N-R result Concat

Vector Floating Point Reciprocal SQRT With N-R result Concat
Calculate the exponent value for the reciprocal value of the 32-bit single precision floating point
source, compute the correct mantissa value and concatenate the final result. This instruction is
part of the non-native VFLPSQRTINR operation.
Available Switches
None
Intrinsic Names
vflpsqrtinrcnct_v32_v32_v32
Instruction details in the instruction set specification
Intrinsic     vflpsqrtinrcnct_v32_v32_v32[_p]
name
Spec syntax   vflpsqrtinrcnct {Oop} vx[0], vy[0], vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand
Operands
              3    IN2_V32         vec_t                      Input vector operand
              4    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...

vRes = vflpsqrtinrcnct_v32_v32_v32_p (8, vIn, vIn2, vecPred);

                   IN_VPR last operand is relevant only for vflpsqrtinrcnct_v32_v32_v32_p
Comments      1.
                   version.


Main table → Floating Point → Float Special Operations → Vector Floating Point
Reciprocal SQRT With N-R result Concat
