# Floating Point → Float/Integer Conversion → Vector Floating Point To

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Floating Point → Float/Integer Conversion → Vector Floating Point To
Integer Conversion

Vector Floating Point To Integer Conversion

Vector Floating Point To Integer Conversion
Performs a conversion of a 32-bit single precision floating-point source into an integer
destination. The sources and the destination are either 32-bit or 40-bit wide determined by the
vector register type. This is a non-native instruction and is implemented as software sequence
Available Switches
None
Intrinsic Names
vflpint_u
vflpint_s
Instruction details in the instruction set specification
Intrinsic     vflpint_u[_p]
name
Spec syntax   vflpint{u} vx[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32          vec_t            Input vector operand
Operands
              2    IN_VPR           vprex_t          Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vflpint_u_p(vIn, vRes, vecPred);

              1.   IN_VPR last operand is relevant only for vflpint_u_p version.

Comments           vflpint_u is a macro which expands into a sequence of several Vec-C
              2.
                   intrinsics. For macro definition, click the "Spec Syntax" link above.


Main table → Floating Point → Float/Integer Conversion → Vector Floating Point To
Integer Conversion
Intrinsic     vflpint_s[_p]
name
Spec syntax   vflpint{s} vx[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32          vec_t             Input vector operand
Operands
              2    IN_VPR           vprex_t           Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vflpint_s_p(vIn, vRes, vecPred);

              1.   IN_VPR last operand is relevant only for vflpint_s_p version.
Comments           vflpint_s is a macro which expands into a sequence of several Vec-C
              2.
                   intrinsics. For macro definition, click the "Spec Syntax" link above.


Main table → Floating Point → Float/Integer Conversion → Vector Floating Point To
Integer Conversion
