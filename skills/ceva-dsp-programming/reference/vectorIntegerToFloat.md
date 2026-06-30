# Floating Point → Float/Integer Conversion → Vector Integer to Float

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Floating Point → Float/Integer Conversion → Vector Integer to Float
Conversion

Vector Integer to Float Conversion

Vector Integer to Float Conversion
Performs a conversion of an absolute value signed/unsigned integer number into floating point
representation. If the input is a signed integer, its MSB bit is disregarded and used in order to
determine the sign of the result. This instruction is part of the non-native VINTFLP operation.
Available Switches
None
Intrinsic Names
vintflp_u
vintflp_s
Instruction details in the instruction set specification
Intrinsic     vintflp_u[_p]
name
Spec syntax   vintflp{u} vx[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32          vec_t            Input vector operand
Operands
              2    IN_VPR           vprex_t          Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vintflp_u_p(vIn, vRes, vecPred);

              1.   IN_VPR last operand is relevant only for vintflp_u_p version.
Comments           vintflp_u is a macro which expands into a sequence of several Vec-C
              2.
                   intrinsics. For macro definition, click the "Spec Syntax" link above.


Main table → Floating Point → Float/Integer Conversion → Vector Integer to Float
Conversion
Intrinsic     vintflp_s[_p]
name

Spec syntax   vintflp{s} vx[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32          vec_t             Input vector operand
Operands
              2    IN_VPR           vprex_t           Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vintflp_s_p(vIn, vRes, vecPred);

              1.   IN_VPR last operand is relevant only for vintflp_s_p version.
Comments           vintflp_s is a macro which expands into a sequence of several Vec-C
              2.
                   intrinsics. For macro definition, click the "Spec Syntax" link above.


Main table → Floating Point → Float/Integer Conversion → Vector Integer to Float
Conversion
