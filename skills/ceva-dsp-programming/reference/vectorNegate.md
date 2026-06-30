# Arithmetic → Negate → Vector Negate

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Arithmetic → Negate → Vector Negate

Vector Negate

Vector Negate
Performs negate operation on 32-bit or 40-bit source into a destination respectively.
Available Switches
       Number of atomic operations. An atomic operation is defined as a single negate operation.
Oop
       1op ≤ Oop ≤ 8op
Intrinsic Names
vneg_v32_v40
vneg_v32_v32
Instruction details in the instruction set specification
Intrinsic     vneg_v32_v40[_p]
name
Spec syntax   vneg {Oop} vx[0], voz[0], ?vprX

Return type   vec40_t

              1    OOP             uint8     1..8        Number of atomic operations
Operands      2    IN1_V32         vec_t                 Input vector operand
              3    IN_VPR          vprex_t               Vector predicate operand
              vec_t vIn;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vneg_v32_v40_p (8, vIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vneg_v32_v40_p version.


Main table → Arithmetic → Negate → Vector Negate
Intrinsic     vneg_v32_v32[_p]
name
Spec syntax   vneg {Oop} vx[0], vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8        Number of atomic operations
Operands      2    IN1_V32         vec_t                 Input vector operand
              3    IN_VPR          vprex_t               Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vneg_v32_v32_p (8, vIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vneg_v32_v32_p version.


Main table → Arithmetic → Negate → Vector Negate
