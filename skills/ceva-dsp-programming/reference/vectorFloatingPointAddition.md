# Floating Point → Float Arithmetic → Vector Floating Point Addition

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Floating Point → Float Arithmetic → Vector Floating Point Addition

Vector Floating Point Addition

Vector Floating Point Addition
Performs addition between two 32-bit single precision floating-point sources into a destination.
The sources and the destination are either 32-bit or 40-bit wide determined by the vector register
type. This is a non-native instruction and is implemented as software sequence.
Available Switches
None
Intrinsic Names
vflpadd
Instruction details in the instruction set specification
Intrinsic     vflpadd[_p]
name
Spec syntax   vflpadd vx[0], vy[0], vz[0], ?vprX

Return type   vec_t

1    IN1_V32          vec_t            Input vector operand
Operands      2    IN2_V32          vec_t            Input vector operand
              3    IN_VPR           vprex_t          Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vflpadd_p(vIn, vIn2, vRes, vecPred);

              1.   IN_VPR last operand is relevant only for vflpadd_p version.
Comments           vflpadd is a macro which expands into a sequence of several Vec-C intrinsics.
              2.
                   For macro definition, click the "Spec Syntax" link above.


Main table → Floating Point → Float Arithmetic → Vector Floating Point Addition
