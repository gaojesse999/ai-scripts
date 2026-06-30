# Floating Point → Float Arithmetic → Vector Floating Point Negate

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Floating Point → Float Arithmetic → Vector Floating Point Negate

Vector Floating Point Negate

Vector Floating Point Negate
Performs a negation operation on the sign bit of the 32-bit single precision floating point source
Available Switches
None
Intrinsic Names
vflpneg_v32_v32
Instruction details in the instruction set specification
Intrinsic     vflpneg_v32_v32[_p]
name
Spec syntax   vflpneg {Oop} vx[0], vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8           Number of atomic operations
Operands      2    IN1_V32         vec_t                    Input vector operand
              3    IN_VPR          vprex_t                  Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vflpneg_v32_v32_p (8, vIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vflpneg_v32_v32_p version.


Main table → Floating Point → Float Arithmetic → Vector Floating Point Negate
