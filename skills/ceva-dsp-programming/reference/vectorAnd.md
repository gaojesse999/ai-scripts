# Logic → And → Vector And

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Logic → And → Vector And

Vector And

Vector And
Performs logic-AND operation between two sources. Each source is 32-bit wide. The destination
is 32-bit wide.
Available Switches
       Number of atomic operations. An atomic operation is defined as a single logic-and
Oop
       operation. 1op ≤ Oop ≤ 8op
Intrinsic Names
vand_v32_v32_v32
Instruction details in the instruction set specification
Intrinsic     vand_v32_v32_v32[_p]
name

Spec syntax   vand {Oop} vx[0], vy[0], vz[0], ?vprX

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
              vRes = vand_v32_v32_v32_p (8, vIn, vIn2, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vand_v32_v32_v32_p version.


Main table → Logic → And → Vector And
