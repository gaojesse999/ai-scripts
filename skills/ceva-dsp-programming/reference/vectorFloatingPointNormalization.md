# Floating Point → Float Normalize → Vector Floating Point Normalization

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Floating Point → Float Normalize → Vector Floating Point Normalization

Vector Floating Point Normalization

Vector Floating Point Normalization
Performs normalization of the mantissa and updates the exponent field accordingly. This
instruction is part of the non-native VFLPADD, VFLPSUB operations.
Available Switches
None
Intrinsic Names
vflpnorm_v32_v32_v32
Instruction details in the instruction set specification
Intrinsic     vflpnorm_v32_v32_v32[_p]
name
Spec syntax   vflpnorm {Oop} vx[0], vy[0], vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8            Number of atomic operations
              2    IN1_V32         vec_t                     Input vector operand
Operands
              3    IN2_V32         vec_t                     Input vector operand
              4    IN_VPR          vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vflpnorm_v32_v32_v32_p (8, vIn, vIn2, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vflpnorm_v32_v32_v32_p version.


Main table → Floating Point → Float Normalize → Vector Floating Point Normalization
