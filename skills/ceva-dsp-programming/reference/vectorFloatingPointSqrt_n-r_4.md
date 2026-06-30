# Floating Point → Float Division → Vector Floating Point SQRT (N-R, 4

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Floating Point → Float Division → Vector Floating Point SQRT (N-R, 4
Operations)

Vector Floating Point SQRT (N-R, 4 Operations)

Vector Floating Point SQRT (N-R, 4 Operations)
Performs a sqaure-root action on a 32-bit single precision floating-point source, with Newton-
Raphson algorithm which extends the mantissa’s precision. The sources and the destination are
either 32-bit or 40-bit wide determined by the vector register type. This is a non-native
instruction and is implemented as software sequence.
Available Switches
None
Intrinsic Names
vflpsqrtnr4
Instruction details in the instruction set specification
Intrinsic     vflpsqrtnr4[_p]
name
Spec syntax   vflpsqrtnr4 vx[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32          vec_t            Input vector operand
Operands
              2    IN_VPR           vprex_t          Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vflpsqrtnr4_p(vIn, vRes, vecPred);

              1.   IN_VPR last operand is relevant only for vflpsqrtnr4_p version.
Comments           vflpsqrtnr4 is a macro which expands into a sequence of several Vec-C
              2.
                   intrinsics. For macro definition, click the "Spec Syntax" link above.


Main table → Floating Point → Float Division → Vector Floating Point SQRT (N-R, 4
Operations)
