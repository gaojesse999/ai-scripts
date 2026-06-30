# Move And Pack → Normalize → Vector Complex Normalize

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Move And Pack → Normalize → Vector Complex Normalize

Vector Complex Normalize

Vector Complex Normalize
Converts complex source into an exponent and two mantissa parts, one is real and the other is
image. Each complex source consists of real 40bit part and imaginary 40-bit part determined by
the vector register type. The mantissa parts both real and image are written into 32-bit or 40-bit
type registers vector depending on the register type. The complex exponent part is written either
into 16-bit or 20-bit register in depending on the register type.
Available Switches
          Number of atomic operations. An atomic operation is defined as normalize complex
Qop
          number to exponent and mantissa parts.
          When used, the exponent calculated will be rounded down to an even number. In cases
even      where the exponent should be an odd number, it will be decremented by 1, and the
          mantissa will shifted accordingly.
uns       When used, the evaluated source operand is unsigned. The default is signed.
zero      When used, if the source is zero, then the result is zero.
Intrinsic Names
vnormx_v40_v32_v32_even
vnormx_v40_v32_v32
vnormx_v40_v32_v32_uns_even
vnormx_v40_v32_v32_uns
vnormx_v40_v32_v32_uns_zero_even
vnormx_v40_v32_v32_uns_zero
vnormx_v40_v32_v32_zero_even
vnormx_v40_v32_v32_zero
Instruction details in the instruction set specification
Intrinsic     vnormx_v40_v32_v32_even[_p]
name
Spec syntax   vnormx {Qop [,uns][,zero_sw][,even]} vox[0], vz1[0], vz2[Ze], ?vprX

Return type   vec_t

              1    QOP            uint8     1..4            Number of atomic operations
              2    IN1_V40        vec40_t                   Output vector operand
              3    RES2_V32       vec_t                     Input vector result operand
Operands
                                                            Offset for the first DW used from the
              4    OUT_OFST       uint8     0..7
                                                            result operand
              5    IN_VPR         vprex_t                   Vector predicate operand
              vec40_t vComplexSource;
              vec_t vExponentOut;
              vec_t vMantissa;
C example     vprex_t vecPred;
              ...
              vMantissa = vnormx_v40_v32_v32_even_p (4, vComplexSource, vExponentOut, 0, vecPred);

IN_VPR last operand is relevant only for vnormx_v40_v32_v32_even_p
              1.
                   version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Move And Pack → Normalize → Vector Complex Normalize
Intrinsic     vnormx_v40_v32_v32[_p]
name
Spec syntax   vnormx {Qop [,uns][,zero_sw][,even]} vox[0], vz1[0], vz2[Ze], ?vprX

Return type   vec_t

              1    QOP            uint8     1..4            Number of atomic operations
              2    IN1_V40        vec40_t                   Output vector operand
              3    RES2_V32       vec_t                     Input vector result operand
Operands
                                                            Offset for the first DW used from the
              4    OUT_OFST       uint8     0..7
                                                            result operand
              5    IN_VPR         vprex_t                   Vector predicate operand
              vec40_t vComplexSource;
              vec_t vExponentOut;
              vec_t vMantissa;
C example     vprex_t vecPred;
              ...
              vMantissa = vnormx_v40_v32_v32_p (4, vComplexSource, vExponentOut, 0, vecPred);
              1.   IN_VPR last operand is relevant only for vnormx_v40_v32_v32_p version.

Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Move And Pack → Normalize → Vector Complex Normalize
Intrinsic     vnormx_v40_v32_v32_uns_even[_p]
name
Spec syntax   vnormx {Qop [,uns][,zero_sw][,even]} vox[0], vz1[0], vz2[Ze], ?vprX

Return type   vec_t

              1    QOP            uint8     1..4           Number of atomic operations
              2    IN1_V40        vec40_t                  Output vector operand
              3    RES2_V32       vec_t                    Input vector result operand
Operands
                                                           Offset for the first DW used from the
              4    OUT_OFST       uint8     0..7
                                                           result operand

5    IN_VPR         vprex_t                  Vector predicate operand
              vec40_t vComplexSource;
              vec_t vExponentOut;
              vec_t vMantissa;
C example     vprex_t vecPred;
              ...
              vMantissa = vnormx_v40_v32_v32_uns_even_p (4, vComplexSource, vExponentOut, 0, vecPred);

                   IN_VPR last operand is relevant only for vnormx_v40_v32_v32_uns_even_p
              1.
                   version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Move And Pack → Normalize → Vector Complex Normalize
Intrinsic     vnormx_v40_v32_v32_uns[_p]
name
Spec syntax   vnormx {Qop [,uns][,zero_sw][,even]} vox[0], vz1[0], vz2[Ze], ?vprX

Return type   vec_t

              1    QOP            uint8     1..4           Number of atomic operations
              2    IN1_V40        vec40_t                  Output vector operand
Operands      3    RES2_V32       vec_t                    Input vector result operand

              4
                                                           Offset for the first DW used from the
                   OUT_OFST       uint8     0..7
                                                           result operand
              5    IN_VPR         vprex_t                   Vector predicate operand
              vec40_t vComplexSource;
              vec_t vExponentOut;
              vec_t vMantissa;
C example     vprex_t vecPred;
              ...
              vMantissa = vnormx_v40_v32_v32_uns_p (4, vComplexSource, vExponentOut, 0, vecPred);

                   IN_VPR last operand is relevant only for vnormx_v40_v32_v32_uns_p
              1.
                   version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Move And Pack → Normalize → Vector Complex Normalize
Intrinsic     vnormx_v40_v32_v32_uns_zero_even[_p]
name
Spec syntax   vnormx {Qop [,uns][,zero_sw][,even]} vox[0], vz1[0], vz2[Ze], ?vprX

Return type   vec_t

              1    QOP            uint8     1..4            Number of atomic operations

2    IN1_V40        vec40_t                   Output vector operand
              3    RES2_V32       vec_t                     Input vector result operand
Operands
                                                            Offset for the first DW used from the
              4    OUT_OFST       uint8     0..7
                                                            result operand
              5    IN_VPR         vprex_t                   Vector predicate operand
              vec40_t vComplexSource;
              vec_t vExponentOut;
              vec_t vMantissa;
C example     vprex_t vecPred;
              ...
              vMantissa = vnormx_v40_v32_v32_uns_zero_even_p (4, vComplexSource, vExponentOut, 0, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vnormx_v40_v32_v32_uns_zero_even_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Move And Pack → Normalize → Vector Complex Normalize
Intrinsic     vnormx_v40_v32_v32_uns_zero[_p]
name
Spec syntax   vnormx {Qop [,uns][,zero_sw][,even]} vox[0], vz1[0], vz2[Ze], ?vprX
Return type   vec_t

              1    QOP            uint8     1..4            Number of atomic operations
              2    IN1_V40        vec40_t                   Output vector operand
              3    RES2_V32       vec_t                     Input vector result operand
Operands
                                                            Offset for the first DW used from the
              4    OUT_OFST       uint8     0..7
                                                            result operand
              5    IN_VPR         vprex_t                   Vector predicate operand
              vec40_t vComplexSource;
              vec_t vExponentOut;
              vec_t vMantissa;
C example     vprex_t vecPred;
              ...
              vMantissa = vnormx_v40_v32_v32_uns_zero_p (4, vComplexSource, vExponentOut, 0, vecPred);

                   IN_VPR last operand is relevant only for vnormx_v40_v32_v32_uns_zero_p
              1.
                   version.
Comments           This intrinsic returns two results. The first result variable should be placed to

2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Move And Pack → Normalize → Vector Complex Normalize
Intrinsic     vnormx_v40_v32_v32_zero_even[_p]
name
Spec syntax   vnormx {Qop [,uns][,zero_sw][,even]} vox[0], vz1[0], vz2[Ze], ?vprX

Return type   vec_t

              1    QOP            uint8     1..4            Number of atomic operations
              2    IN1_V40        vec40_t                   Output vector operand
              3    RES2_V32       vec_t                     Input vector result operand
Operands
                                                            Offset for the first DW used from the
              4    OUT_OFST       uint8     0..7
                                                            result operand
              5    IN_VPR         vprex_t                   Vector predicate operand
              vec40_t vComplexSource;
              vec_t vExponentOut;
              vec_t vMantissa;
C example     vprex_t vecPred;
              ...
              vMantissa = vnormx_v40_v32_v32_zero_even_p (4, vComplexSource, vExponentOut, 0, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vnormx_v40_v32_v32_zero_even_p version.
Comments
                   This intrinsic returns two results. The first result variable should be placed to
              2.
                   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Move And Pack → Normalize → Vector Complex Normalize
Intrinsic     vnormx_v40_v32_v32_zero[_p]
name
Spec syntax   vnormx {Qop [,uns][,zero_sw][,even]} vox[0], vz1[0], vz2[Ze], ?vprX

Return type   vec_t

              1    QOP            uint8     1..4            Number of atomic operations
              2    IN1_V40        vec40_t                   Output vector operand
              3    RES2_V32       vec_t                     Input vector result operand
Operands
                                                            Offset for the first DW used from the
              4    OUT_OFST       uint8     0..7
                                                            result operand
              5    IN_VPR         vprex_t                   Vector predicate operand
              vec40_t vComplexSource;
              vec_t vExponentOut;

vec_t vMantissa;
C example     vprex_t vecPred;
              ...
              vMantissa = vnormx_v40_v32_v32_zero_p (4, vComplexSource, vExponentOut, 0, vecPred);

                   IN_VPR last operand is relevant only for vnormx_v40_v32_v32_zero_p
              1.
                   version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Move And Pack → Normalize → Vector Complex Normalize
