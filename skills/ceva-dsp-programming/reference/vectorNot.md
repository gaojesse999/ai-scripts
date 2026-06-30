# Logic → Not → Vector Not

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Logic → Not → Vector Not

Vector Not

Vector Not
Performs logic-NOT operation on a 32-bit source into a 32-bit destination.
Available Switches
       Number of atomic operations. An atomic operation is defined as a single logic-not
Oop
       operation. 1op ≤ Oop ≤ 8op
Intrinsic Names
vnot_v32_v32
Instruction details in the instruction set specification
Intrinsic     vnot_v32_v32[_p]
name
Spec syntax   vnot {Oop} vx[0], vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8        Number of atomic operations
Operands      2    IN1_V32         vec_t                 Input vector operand
              3    IN_VPR          vprex_t               Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vnot_v32_v32_p (8, vIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vnot_v32_v32_p version.


Main table → Logic → Not → Vector Not
