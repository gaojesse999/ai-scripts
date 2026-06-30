# Arithmetic → Round → Vector Round Long

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Arithmetic → Round → Vector Round Long

Vector Round Long

Vector Round Long
Performs round operation on a 72-bit source into 72-bit destination.
Available Switches
       Number of atomic operations. An atomic operation is defined as a single rounding
Qop
       operation. 1op ≤ Qop ≤ 4op
Intrinsic Names
vroundl_v40_v40
Instruction details in the instruction set specification
Intrinsic     vroundl_v40_v40[_p]
name
Spec syntax   vroundl {Qop} vox[0], voz[0], ?vprX

Return type   vec40_t

              1    QOP             uint8     1..4           Number of atomic operations
Operands      2    IN1_V40         vec40_t                  Output vector operand
              3    IN_VPR          vprex_t                  Vector predicate operand
              vec40_t vIn;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vroundl_v40_v40_p (4, vIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vroundl_v40_v40_p version.


Main table → Arithmetic → Round → Vector Round Long
