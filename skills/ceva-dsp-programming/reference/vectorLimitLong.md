# Arithmetic → Limit → Vector Limit Long

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Arithmetic → Limit → Vector Limit Long

Vector Limit Long

Vector Limit Long
Performs limit operation on a source into a destination. Each source is 72-bit wide. The
destination is 72-bit wide.
Available Switches
       Number of atomic operations. An atomic operation is defined as a single limit operation.
Qop
       1op ≤ Qop ≤ 4op
Intrinsic Names
vliml_v40_v40
Instruction details in the instruction set specification
Intrinsic     vliml_v40_v40[_p]
name
Spec syntax   vliml {Qop} vox[0],voz[0], ?vprX

Return type   vec40_t

              1    QOP             uint8     1..4         Number of atomic operations
Operands      2    IN1_V40         vec40_t                Output vector operand
              3    IN_VPR          vprex_t                Vector predicate operand
              vec40_t vIn;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vliml_v40_v40_p (4, vIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vliml_v40_v40_p version.


Main table → Arithmetic → Limit → Vector Limit Long
