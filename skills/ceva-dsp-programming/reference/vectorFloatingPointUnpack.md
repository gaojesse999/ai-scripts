# Floating Point → Float Special Operations → Vector Floating Point Unpack

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Floating Point → Float Special Operations → Vector Floating Point Unpack
Low Shift Left

Vector Floating Point Unpack Low Shift Left

Vector Floating Point Unpack Low Shift Left
Performs unpack shifted left by byte of either 32-bit or 40-bit source into two destinations of
either 32-bit or 40-bit wide determined by the register type. This instruction is part of the non-
native VFLPSQRT, VFLPSQRTI operations.
Available Switches
None
Intrinsic Names
vflpunpklsl_v32_v32
vflpunpklsl_v32_v32_rcp
Instruction details in the instruction set specification
Intrinsic     vflpunpklsl_v32_v32[_p]
name
Spec syntax   vflpunpklsl {Qop [,rcp]} vx[0], vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4              Number of atomic operations
              2    IN1_V32         vec_t                       Input vector operand
Operands                                                       Offset for the first DW used from operand
              3    IN1_OFST        uint8     0,4
                                                               2

              4    IN_VPR          vprex_t                     Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vflpunpklsl_v32_v32_p (4, vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vflpunpklsl_v32_v32_p version.


Main table → Floating Point → Float Special Operations → Vector Floating Point Unpack
Low Shift Left
Intrinsic     vflpunpklsl_v32_v32_rcp[_p]
name
Spec syntax   vflpunpklsl {Qop [,rcp]} vx[0], vz[0], ?vprX

Return type   vec_t

1    QOP             uint8     1..4              Number of atomic operations
              2    IN1_V32         vec_t                       Input vector operand
Operands                                                       Offset for the first DW used from operand
              3    IN1_OFST        uint8     0,4
                                                               2

              4    IN_VPR          vprex_t                     Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vflpunpklsl_v32_v32_rcp_p (4, vIn, 0, vecPred);

                   IN_VPR last operand is relevant only for vflpunpklsl_v32_v32_rcp_p
Comments      1.
                   version.


Main table → Floating Point → Float Special Operations → Vector Floating Point Unpack
Low Shift Left
