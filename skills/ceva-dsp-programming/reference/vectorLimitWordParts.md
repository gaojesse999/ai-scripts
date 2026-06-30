# Arithmetic → Limit → Vector Limit Word Parts

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Arithmetic → Limit → Vector Limit Word Parts

Vector Limit Word Parts

Vector Limit Word Parts
Performs two limit operations on a source into destination. Each source is 20-bit wide. Each
result is 20-bit wide packed into into 40-bit destination.
Available Switches
         Number of atomic operations. An atomic operation is defined as two limit operations. 1op
Oop
         ≤ Oop ≤ 8op
Intrinsic Names
vlimw_v40_v40
Instruction details in the instruction set specification
Intrinsic     vlimw_v40_v40[_p]
name
Spec syntax   vlimw {Oop} vox[0],voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8          Number of atomic operations
Operands      2    IN1_V40        vec40_t                 Output vector operand
              3    IN_VPR         vprex_t                 Vector predicate operand
              vec40_t vIn;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vlimw_v40_v40_p (8, vIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vlimw_v40_v40_p version.

Main table → Arithmetic → Limit → Vector Limit Word Parts
