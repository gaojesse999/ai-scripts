# Arithmetic → Round → Vector Round Word Parts

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Arithmetic → Round → Vector Round Word Parts

Vector Round Word Parts

Vector Round Word Parts
Performs two round operations on two 20-bit sources into destination parts respectively.
Available Switches
       Number of atomic operations. An atomic operation is defined as two rounding operations.
Oop
       1op ≤ Oop ≤ 8op
Intrinsic Names
vroundw_v40_v40
Instruction details in the instruction set specification
Intrinsic     vroundw_v40_v40[_p]
name
Spec syntax   vroundw {Oop} vox[0], voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V40        vec40_t                   Output vector operand
              3    IN_VPR         vprex_t                   Vector predicate operand

vec40_t vIn;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vroundw_v40_v40_p (8, vIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vroundw_v40_v40_p version.


Main table → Arithmetic → Round → Vector Round Word Parts
