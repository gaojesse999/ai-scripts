# Floating Point → Float Division → Vector Floating Point Reciprocal SQRT

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Floating Point → Float Division → Vector Floating Point Reciprocal SQRT

Vector Floating Point Reciprocal SQRT

Vector Floating Point Reciprocal SQRT
Performs a reciprocal sqaure-root action on a 32-bit single precision floating-point source. The
sources and the destination are either 32-bit or 40-bit wide determined by the vector register
type. This is a non-native instruction and is implemented as software sequence.
Available Switches
None
Intrinsic Names
vflpsqrti
Instruction details in the instruction set specification
Intrinsic     vflpsqrti[_p]
name
Spec syntax   vflpsqrti vx[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32          vec_t             Input vector operand
Operands
              2    IN_VPR           vprex_t           Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vflpsqrti_p(vIn, vRes, vecPred);

              1.   IN_VPR last operand is relevant only for vflpsqrti_p version.
Comments           vflpsqrti is a macro which expands into a sequence of several Vec-C
              2.

intrinsics. For macro definition, click the "Spec Syntax" link above.


Main table → Floating Point → Float Division → Vector Floating Point Reciprocal SQRT

Main table → Floating Point → Float Division → Vector Floating Point Reciprocal SQRT
(4 Operations)

Vector Floating Point Reciprocal SQRT (4 Operations)

Vector Floating Point Reciprocal SQRT (4 Operations)
Performs a reciprocal sqaure-root action on a 32-bit single precision floating-point source. The
sources and the destination are either 32-bit or 40-bit wide determined by the vector register
type. This is a non-native instruction and is implemented as software sequence.
Available Switches
None
Intrinsic Names
vflpsqrti4
Instruction details in the instruction set specification
Intrinsic     vflpsqrti4[_p]
name
Spec syntax   vflpsqrti4 vx[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32          vec_t            Input vector operand
Operands
              2    IN_VPR           vprex_t          Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vflpsqrti4_p(vIn, vRes, vecPred);

              1.   IN_VPR last operand is relevant only for vflpsqrti4_p version.
Comments           vflpsqrti4 is a macro which expands into a sequence of several Vec-C
              2.
                   intrinsics. For macro definition, click the "Spec Syntax" link above.


Main table → Floating Point → Float Division → Vector Floating Point Reciprocal SQRT
(4 Operations)

Main table → Floating Point → Float Division → Vector Floating Point Reciprocal SQRT
(N-R)

Vector Floating Point Reciprocal SQRT (N-R)

Vector Floating Point Reciprocal SQRT (N-R)
Performs a reciprocal sqaure-root action on a 32-bit single precision floating-point source, with
Newton-Raphson algorithm which extends the mantissa’s precision. The sources and the
destination are either 32-bit or 40-bit wide determined by the vector register type. This is a non-
native instruction and is implemented as software sequence.
Available Switches
None
Intrinsic Names
vflpsqrtinr
Instruction details in the instruction set specification
Intrinsic     vflpsqrtinr[_p]
name
Spec syntax   vflpsqrtinr vx[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32          vec_t            Input vector operand
Operands
              2    IN_VPR           vprex_t          Vector predicate operand
              vec_t vIn;
              vec_t vRes;

C example     vprex_t vecPred;
              ...
              vflpsqrtinr_p(vIn, vRes, vecPred);

              1.   IN_VPR last operand is relevant only for vflpsqrtinr_p version.
Comments           vflpsqrtinr is a macro which expands into a sequence of several Vec-C
              2.
                   intrinsics. For macro definition, click the "Spec Syntax" link above.


Main table → Floating Point → Float Division → Vector Floating Point Reciprocal SQRT
(N-R)

Main table → Floating Point → Float Division → Vector Floating Point Reciprocal SQRT
(N-R, 4 Operations)

Vector Floating Point Reciprocal SQRT (N-R, 4 Operations)

Vector Floating Point Reciprocal SQRT (N-R, 4 Operations)
Performs a reciprocal sqaure-root action on a 32-bit single precision floating-point source, with
Newton-Raphson algorithm which extends the mantissa’s precision. The sources and the
destination are either 32-bit or 40-bit wide determined by the vector register type. This is a non-
native instruction and is implemented as software sequence.
Available Switches
None
Intrinsic Names
vflpsqrtinr4
Instruction details in the instruction set specification
Intrinsic     vflpsqrtinr4[_p]
name
Spec syntax   vflpsqrtinr4 vx[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32          vec_t            Input vector operand
Operands
              2    IN_VPR           vprex_t          Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vflpsqrtinr4_p(vIn, vRes, vecPred);

              1.   IN_VPR last operand is relevant only for vflpsqrtinr4_p version.
Comments           vflpsqrtinr4 is a macro which expands into a sequence of several Vec-C
              2.
                   intrinsics. For macro definition, click the "Spec Syntax" link above.


Main table → Floating Point → Float Division → Vector Floating Point Reciprocal SQRT
(N-R, 4 Operations)
