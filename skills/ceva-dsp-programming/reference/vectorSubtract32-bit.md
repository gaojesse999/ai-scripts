# Arithmetic → Subtract → Vector Subtract 32-bit

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Arithmetic → Subtract → Vector Subtract 32-bit

Vector Subtract 32-bit

Vector Subtract 32-bit
Performs subtraction between two sources into a destination. The sources and the destination are
either 32-bit or 40-bit wide determined by the vector register type.
Available Switches
         Number of atomic operations. An atomic operation is defined as a single subtraction. 1op
Oop

≤ Oop ≤ 8op
Intrinsic Names
vsub32_v32_v32_v32
vsub32_v32_c32_v32
vsub32_c32
Instruction details in the instruction set specification
Intrinsic     vsub32_v32_v32_v32[_p]
name
Spec syntax   vsub32 {Oop} vx[0], vy[0], vz[0], ?vprX

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
              vRes = vsub32_v32_v32_v32_p (8, vIn, vIn2, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vsub32_v32_v32_v32_p version.


Main table → Arithmetic → Subtract → Vector Subtract 32-bit
Intrinsic     vsub32_v32_c32_v32[_p]
name
Spec syntax   vsub32 {Oop} vx[0], vcY, vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand
Operands
              3    IN2_C32         coef_t                     Coefficient operand
              4    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vsub32_v32_c32_v32_p (8, vIn, vcoefIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vsub32_v32_c32_v32_p version.


Main table → Arithmetic → Subtract → Vector Subtract 32-bit
Intrinsic     vsub32_c32[_p]
name
Spec syntax   vsub32 vcX, vcY, vcZ, ?vprX

Return type   coef_t

              1    IN1_C32         coef_t                     Coefficient operand
Operands      2    IN2_C32         coef_t                     Coefficient operand
              3    IN_VPR          vprex_t                    Vector predicate operand
              coef_t vcoefIn;
              coef_t vcoefIn2;
              coef_t vcoefRes;
C example     vprex_t vecPred;
              ...
              vcoefRes = vsub32_c32_p (vcoefIn, vcoefIn2, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vsub32_c32_p version.


Main table → Arithmetic → Subtract → Vector Subtract 32-bit
