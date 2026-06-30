# Arithmetic → Negate → Vector Negate Word Parts

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Arithmetic → Negate → Vector Negate Word Parts

Vector Negate Word Parts

Vector Negate Word Parts
Performs two negate operations on two 16-bit or 20-bit sources into destination parts
respectively.
Available Switches

Number of atomic operations. An atomic operation is defined as two negate operations.
Oop
       1op ≤ Oop ≤ 8op
Intrinsic Names
vnegw_v32_v32
vnegw_v32_v40
Instruction details in the instruction set specification
Intrinsic     vnegw_v32_v32[_p]
name
Spec syntax   vnegw {Oop} vx[0], vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8          Number of atomic operations
Operands      2    IN1_V32        vec_t                   Input vector operand
              3    IN_VPR         vprex_t                 Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vnegw_v32_v32_p (8, vIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vnegw_v32_v32_p version.


Main table → Arithmetic → Negate → Vector Negate Word Parts
Intrinsic     vnegw_v32_v40[_p]
name
Spec syntax   vnegw {Oop} vx[0], voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8          Number of atomic operations
Operands      2    IN1_V32        vec_t                   Input vector operand
              3    IN_VPR         vprex_t                 Vector predicate operand
              vec_t vIn;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vnegw_v32_v40_p (8, vIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vnegw_v32_v40_p version.


Main table → Arithmetic → Negate → Vector Negate Word Parts
