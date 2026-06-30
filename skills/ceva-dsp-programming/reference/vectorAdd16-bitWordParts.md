# Arithmetic → Addition → Vector Add 16-bit Word Parts

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Arithmetic → Addition → Vector Add 16-bit Word Parts

Vector Add 16-bit Word Parts

Vector Add 16-bit Word Parts
Performs two additions. Each addition is between two sources into destination. The sources are
16-bit and the destinations are either 16-bit or 20-bit wide and are packed into either 32-bit or
40-bit destination determined by the vector register type.
Available Switches
           Number of atomic operations. An atomic operation is defined as a two additions. 1op ≤
Oop
           Oop ≤ 8op
Intrinsic Names
vadd16_v32_v32_v32
vadd16_v32_c32_v32
vadd16_c32_c32_c32
Instruction details in the instruction set specification
Intrinsic     vadd16_v32_v32_v32[_p]
name
Spec syntax   vadd16 {Oop} vx[0], vy[0], vz[0], ?vprX

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
              vRes = vadd16_v32_v32_v32_p (8, vIn, vIn2, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vadd16_v32_v32_v32_p version.


Main table → Arithmetic → Addition → Vector Add 16-bit Word Parts
Intrinsic     vadd16_v32_c32_v32[_p]
name
Spec syntax   vadd16 {Oop} vx[0], vcYp, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations

2    IN1_V32        vec_t                      Input vector operand
Operands      3    IN2_C32        coef_t                     Coefficient operand
              4    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 3
              5    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vadd16_v32_c32_v32_p (8, vIn, vcoefIn, LOW, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vadd16_v32_c32_v32_p version.


Main table → Arithmetic → Addition → Vector Add 16-bit Word Parts
Intrinsic     vadd16_c32_c32_c32[_p]
name
Spec syntax   vadd16 vcXp, vcYp, vcZp, ?vprX

Return type   coef_t

              1    IN1_C32       coef_t                    Coefficient operand
              2    IN1_PART      uint8     LOW,HIGH        Word part which is used for operand 1
              3    IN2_C32       coef_t                    Coefficient operand
Operands      4    IN2_PART      uint8     LOW,HIGH        Word part which is used for operand 3
                                                           Word part which is used for the result
              5    OUT_PART      uint8     LOW,HIGH
                                                           operand
              6    IN_VPR        vprex_t                   Vector predicate operand
              coef_t vcoefIn;
              coef_t vcoefIn2;
              coef_t vcoefRes;
C example     vprex_t vecPred;
              ...
              vcoefRes = vadd16_c32_c32_c32_p (vcoefIn, LOW, vcoefIn2, LOW, LOW, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vadd16_c32_c32_c32_p version.


Main table → Arithmetic → Addition → Vector Add 16-bit Word Parts
