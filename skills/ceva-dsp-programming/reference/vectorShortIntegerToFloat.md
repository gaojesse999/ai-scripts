# Floating Point → Float/Integer Conversion → Vector Short Integer to Float

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Floating Point → Float/Integer Conversion → Vector Short Integer to Float
Conversion

Vector Short Integer to Float Conversion

Vector Short Integer to Float Conversion
Performs a conversion of a signed/unsigned short integer into a 32-bit single precision floating-
point source destination. The sources and the destination are either 32-bit or 40-bit wide
determined by the vector register type. This is a non-native instruction and is implemented as
software sequence.
Available Switches
None
Intrinsic Names
vsintflp_s
vsintflp_u
Instruction details in the instruction set specification
Intrinsic     vsintflp_s[_p]
name
Spec syntax   vsintflp{s} vx[0], vy[0], vprU, vz[0], ?vprX

Return type   vec_t

              1    IN1_V32          vec_t                         Input vector operand
              2    IN2_V32          vec_t                         Input vector operand
Operands
              3    IN3_VPR          vprex_t                       Vector predicate operand
              4    IN_VPR           vprex_t                       Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              vec_t vRes1;
C example     vprex_t vecPred1,vecPred;
              ...
              vsintflp_s_p(vIn, vRes1, vRes, vecPred1,vecPred);

              1.   IN_VPR last operand is relevant only for vsintflp_s_p version.
Comments           vsintflp_s is a macro which expands into a sequence of several Vec-C
              2.
                   intrinsics. For macro definition, click the "Spec Syntax" link above.


Main table → Floating Point → Float/Integer Conversion → Vector Short Integer to Float
Conversion
Intrinsic     vsintflp_u[_p]
name

Spec syntax   vsintflp{u} vx[0], vy[0], vprU, vz[0], ?vprX

Return type   vec_t

              1    IN1_V32          vec_t                         Input vector operand
              2    IN2_V32          vec_t                         Input vector operand
Operands
              3    IN3_VPR          vprex_t                       Vector predicate operand
              4    IN_VPR           vprex_t                       Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              vec_t vRes1;
C example     vprex_t vecPred1,vecPred;
              ...
              vsintflp_u_p(vIn, vRes1, vRes, vecPred1,vecPred);

              1.   IN_VPR last operand is relevant only for vsintflp_u_p version.
Comments           vsintflp_u is a macro which expands into a sequence of several Vec-C
              2.
                   intrinsics. For macro definition, click the "Spec Syntax" link above.


Main table → Floating Point → Float/Integer Conversion → Vector Short Integer to Float
Conversion
