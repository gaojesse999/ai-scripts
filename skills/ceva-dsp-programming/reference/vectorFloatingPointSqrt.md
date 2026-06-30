# Floating Point → Float Special Operations → Vector Floating Point SQRT

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Floating Point → Float Special Operations → Vector Floating Point SQRT
With N-R Result Concat

Vector Floating Point SQRT With N-R Result Concat

Vector Floating Point SQRT With N-R Result Concat
Calculate the exponent value for the reciprocal value of the 32-bit single precision floating point
source, compute the correct mantissa value and concatenate the final result. This instruction is
part of the non-native VFLPSQRTNR operation.
Available Switches
None
Intrinsic Names
vflpsqrtnrcnct_v32_v32_v32_v32
Instruction details in the instruction set specification
Intrinsic     vflpsqrtnrcnct_v32_v32_v32_v32[_p]
name
Spec syntax   vflpsqrtnrcnct {Oop} vx[0], vy[0], vip[0], vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand
Operands      3    IN2_V32         vec_t                      Input vector operand
              4    IN3_V32         vec_t                      Input vector operand
              5    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
C example     vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vflpsqrtnrcnct_v32_v32_v32_v32_p (8, vIn, vIn2, vIn3, vecPred);

                   IN_VPR last operand is relevant only for vflpsqrtnrcnct_v32_v32_v32_v32_p
Comments      1.
                   version.


Main table → Floating Point → Float Special Operations → Vector Floating Point SQRT
With N-R Result Concat
