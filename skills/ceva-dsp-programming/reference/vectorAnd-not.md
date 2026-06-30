# Logic → And-Not → Vector And-Not

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Logic → And-Not → Vector And-Not

Vector And-Not

Vector And-Not
Performs logic-AND-NOT operation between two sources. Each source is 32-bit wide. The
destination is 32-bit wide.
Available Switches
       Number of atomic operations. An atomic operation is defined as a single logic-and
Oop
       operation. 1op ≤ Oop ≤ 8op
Intrinsic Names
vandnot_v32_v32_v32
Instruction details in the instruction set specification
Intrinsic     vandnot_v32_v32_v32[_p]
name
Spec syntax   vandnot {Oop} vx[0], vy[0], vz[0], ?vprX

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
              vRes = vandnot_v32_v32_v32_p (8, vIn, vIn2, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vandnot_v32_v32_v32_p version.


Main table → Logic → And-Not → Vector And-Not
