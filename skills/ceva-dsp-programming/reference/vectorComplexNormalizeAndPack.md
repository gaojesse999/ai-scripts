# Move And Pack → Normalize → Vector Complex Normalize and Pack

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Move And Pack → Normalize → Vector Complex Normalize and Pack

Vector Complex Normalize and Pack

Vector Complex Normalize and Pack
Converts complex source into an exponent and two mantissa parts, one is real and the other is
image. Each complex source consists of real 40bit part and imaginary 40-bit part determined by
the vector register type. The mantissa real and image parts are packed into one 32-bit or 40-bit
type destination depending on the register type. The exponent part is written either into 16-bit or
20-bit register.
Available Switches
           Number of atomic operations. An atomic operation is defined as normalize complex
           number to exponent and mantissa parts. Used for two vector sources, while the first
Ohop
           vector source is always fully read, the second vector source number of atomic operation
           is set by Ohop.
           Number of atomic operations. An atomic operation is defined as normalize complex
Qop
           number to exponent and mantissa parts.
           When used, the exponent calculated will be rounded down to an even number. In cases
even       where the exponent should be an odd number, it will be decremented by 1, and the
           mantissa will shifted accordingly.
uns        When used, the evaluated source operand is unsigned. The default is signed.
zero       When used, if the source is zero, then the result is zero.
Intrinsic Names
vnormxp_v40_v40_v32_v32_even
vnormxp_v40_v40_v32_v32
vnormxp_v40_v40_v32_v32_uns_even
vnormxp_v40_v40_v32_v32_uns
vnormxp_v40_v40_v32_v32_uns_zero_even
vnormxp_v40_v40_v32_v32_uns_zero
vnormxp_v40_v40_v32_v32_zero_even
vnormxp_v40_v40_v32_v32_zero
vnormxp_v40_v32_v32_even
vnormxp_v40_v32_v32
vnormxp_v40_v32_v32_uns_even
vnormxp_v40_v32_v32_uns
vnormxp_v40_v32_v32_uns_zero_even
vnormxp_v40_v32_v32_uns_zero
vnormxp_v40_v32_v32_zero_even

vnormxp_v40_v32_v32_zero
Instruction details in the instruction set specification
Intrinsic     vnormxp_v40_v40_v32_v32_even[_p]
name
Spec syntax   vnormxp {Ohop [,uns][,zero_sw][,even]} vox[0], voy[0], vz1[0], vz2[0], ?vprX

Return type   vec_t

              1    OHOP          uint8     5..8           Number of atomic operations
              2    IN1_V40       vec40_t                  Output vector operand
              3    IN2_V40       vec40_t                  Output vector operand
Operands                                                  Offset for the first DW used from the
              4    OUT_OFST      uint8     0,4
                                                          result operand
              5    RES2_V32      vec_t                    Input vector result operand
              6    IN_VPR        vprex_t                  Vector predicate operand
              vec40_t vComplexSource;
              vec40_t vComplexSource2;
              vec_t vExponentOut;
              vec_t vMantissa;
C example     vprex_t vecPred;
              ...
              vMantissa = vnormxp_v40_v40_v32_v32_even_p (8, vComplexSource, vComplexSource2, 0,
              vExponentOut, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vnormxp_v40_v40_v32_v32_even_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Move And Pack → Normalize → Vector Complex Normalize and Pack
Intrinsic     vnormxp_v40_v40_v32_v32[_p]
name
Spec syntax   vnormxp {Ohop [,uns][,zero_sw][,even]} vox[0], voy[0], vz1[0], vz2[0], ?vprX

Return type   vec_t

              1    OHOP          uint8     5..8           Number of atomic operations
              2    IN1_V40       vec40_t                  Output vector operand
              3    IN2_V40       vec40_t                  Output vector operand
Operands                                                  Offset for the first DW used from the
              4    OUT_OFST      uint8     0,4
                                                          result operand
              5    RES2_V32      vec_t                    Input vector result operand
              6    IN_VPR        vprex_t                  Vector predicate operand

C example     vec40_t vComplexSource;
              vec40_t vComplexSource2;
              vec_t vExponentOut;
              vec_t vMantissa;
              vprex_t vecPred;
              ...
              vMantissa = vnormxp_v40_v40_v32_v32_p (8, vComplexSource, vComplexSource2, 0, vExponentOut,
              vecPred);

                   IN_VPR last operand is relevant only for vnormxp_v40_v40_v32_v32_p
              1.
                   version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Move And Pack → Normalize → Vector Complex Normalize and Pack
Intrinsic     vnormxp_v40_v40_v32_v32_uns_even[_p]
name
Spec syntax   vnormxp {Ohop [,uns][,zero_sw][,even]} vox[0], voy[0], vz1[0], vz2[0], ?vprX

Return type   vec_t

              1    OHOP          uint8     5..8            Number of atomic operations
              2    IN1_V40       vec40_t                   Output vector operand
              3    IN2_V40       vec40_t                   Output vector operand
Operands                                                   Offset for the first DW used from the
              4    OUT_OFST      uint8     0,4
                                                           result operand
              5    RES2_V32      vec_t                     Input vector result operand
              6    IN_VPR        vprex_t                   Vector predicate operand
              vec40_t vComplexSource;
              vec40_t vComplexSource2;
              vec_t vExponentOut;
              vec_t vMantissa;
C example     vprex_t vecPred;
              ...
              vMantissa = vnormxp_v40_v40_v32_v32_uns_even_p (8, vComplexSource, vComplexSource2, 0,
              vExponentOut, vecPred);

              1.
                   IN_VPR last operand is relevant only for
                   vnormxp_v40_v40_v32_v32_uns_even_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Move And Pack → Normalize → Vector Complex Normalize and Pack
Intrinsic     vnormxp_v40_v40_v32_v32_uns[_p]
name

Spec syntax   vnormxp {Ohop [,uns][,zero_sw][,even]} vox[0], voy[0], vz1[0], vz2[0], ?vprX

Return type   vec_t

              1    OHOP          uint8     5..8           Number of atomic operations
              2    IN1_V40       vec40_t                  Output vector operand
              3    IN2_V40       vec40_t                  Output vector operand
Operands                                                  Offset for the first DW used from the
              4    OUT_OFST      uint8     0,4
                                                          result operand
              5    RES2_V32      vec_t                    Input vector result operand
              6    IN_VPR        vprex_t                  Vector predicate operand
              vec40_t vComplexSource;
              vec40_t vComplexSource2;
              vec_t vExponentOut;
              vec_t vMantissa;
C example     vprex_t vecPred;
              ...
              vMantissa = vnormxp_v40_v40_v32_v32_uns_p (8, vComplexSource, vComplexSource2, 0,
              vExponentOut, vecPred);

                   IN_VPR last operand is relevant only for vnormxp_v40_v40_v32_v32_uns_p
              1.
                   version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Move And Pack → Normalize → Vector Complex Normalize and Pack
Intrinsic     vnormxp_v40_v40_v32_v32_uns_zero_even[_p]
name
Spec syntax   vnormxp {Ohop [,uns][,zero_sw][,even]} vox[0], voy[0], vz1[0], vz2[0], ?vprX

Return type   vec_t

              1    OHOP          uint8     5..8           Number of atomic operations
              2    IN1_V40       vec40_t                  Output vector operand
              3    IN2_V40       vec40_t                  Output vector operand
Operands                                                  Offset for the first DW used from the
              4    OUT_OFST      uint8     0,4
                                                          result operand
              5    RES2_V32      vec_t                    Input vector result operand
              6    IN_VPR        vprex_t                  Vector predicate operand
              vec40_t vComplexSource;
              vec40_t vComplexSource2;
C example     vec_t vExponentOut;
              vec_t vMantissa;

vprex_t vecPred;
              ...
              vMantissa = vnormxp_v40_v40_v32_v32_uns_zero_even_p (8, vComplexSource, vComplexSource2, 0,
              vExponentOut, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vnormxp_v40_v40_v32_v32_uns_zero_even_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Move And Pack → Normalize → Vector Complex Normalize and Pack
Intrinsic     vnormxp_v40_v40_v32_v32_uns_zero[_p]
name
Spec syntax   vnormxp {Ohop [,uns][,zero_sw][,even]} vox[0], voy[0], vz1[0], vz2[0], ?vprX

Return type   vec_t

              1    OHOP          uint8     5..8           Number of atomic operations
              2    IN1_V40       vec40_t                  Output vector operand
              3    IN2_V40       vec40_t                  Output vector operand
Operands                                                  Offset for the first DW used from the
              4    OUT_OFST      uint8     0,4
                                                          result operand
              5    RES2_V32      vec_t                    Input vector result operand
              6    IN_VPR        vprex_t                  Vector predicate operand
              vec40_t vComplexSource;
              vec40_t vComplexSource2;
              vec_t vExponentOut;
              vec_t vMantissa;
C example     vprex_t vecPred;
              ...
              vMantissa = vnormxp_v40_v40_v32_v32_uns_zero_p (8, vComplexSource, vComplexSource2, 0,
              vExponentOut, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vnormxp_v40_v40_v32_v32_uns_zero_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Move And Pack → Normalize → Vector Complex Normalize and Pack
Intrinsic     vnormxp_v40_v40_v32_v32_zero_even[_p]
name
Spec syntax   vnormxp {Ohop [,uns][,zero_sw][,even]} vox[0], voy[0], vz1[0], vz2[0], ?vprX
Return type   vec_t

1    OHOP          uint8     5..8            Number of atomic operations
              2    IN1_V40       vec40_t                   Output vector operand
              3    IN2_V40       vec40_t                   Output vector operand
Operands                                                   Offset for the first DW used from the
              4    OUT_OFST      uint8     0,4
                                                           result operand
              5    RES2_V32      vec_t                     Input vector result operand
              6    IN_VPR        vprex_t                   Vector predicate operand
              vec40_t vComplexSource;
              vec40_t vComplexSource2;
              vec_t vExponentOut;
              vec_t vMantissa;
C example     vprex_t vecPred;
              ...
              vMantissa = vnormxp_v40_v40_v32_v32_zero_even_p (8, vComplexSource, vComplexSource2, 0,
              vExponentOut, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vnormxp_v40_v40_v32_v32_zero_even_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Move And Pack → Normalize → Vector Complex Normalize and Pack
Intrinsic     vnormxp_v40_v40_v32_v32_zero[_p]
name
Spec syntax   vnormxp {Ohop [,uns][,zero_sw][,even]} vox[0], voy[0], vz1[0], vz2[0], ?vprX

Return type   vec_t

              1    OHOP          uint8     5..8            Number of atomic operations
              2    IN1_V40       vec40_t                   Output vector operand
              3    IN2_V40       vec40_t                   Output vector operand
Operands                                                   Offset for the first DW used from the
              4    OUT_OFST      uint8     0,4
                                                           result operand
              5    RES2_V32      vec_t                     Input vector result operand
              6    IN_VPR        vprex_t                   Vector predicate operand
              vec40_t vComplexSource;
              vec40_t vComplexSource2;
              vec_t vExponentOut;
C example     vec_t vMantissa;
              vprex_t vecPred;
              ...

vMantissa = vnormxp_v40_v40_v32_v32_zero_p (8, vComplexSource, vComplexSource2, 0,
            vExponentOut, vecPred);

                 IN_VPR last operand is relevant only for
            1.
                 vnormxp_v40_v40_v32_v32_zero_p version.
Comments         This intrinsic returns two results. The first result variable should be placed to
            2.   the left of the = sign (lvalue). The second result variable should be passed as
                 an additional parameter (RES2_V32).


Main table → Move And Pack → Normalize → Vector Complex Normalize and Pack
Intrinsic     vnormxp_v40_v32_v32_even[_p]
name
Spec syntax   vnormxp {Qop [,uns][,zero_sw][,even]} vox[0], vz1[0], vz2[Ze], ?vprX

Return type   vec_t

              1    QOP            uint8     1..4            Number of atomic operations
              2    IN1_V40        vec40_t                   Output vector operand
                                                            Offset for the first DW used from the first
              3    RES1_OFST      uint8     0,4
                                                            result operand
Operands
              4    RES2_V32       vec_t                     Input vector result operand
                                                            Offset for the first DW used from the
              5    RES2_OFST      uint8     0,4
                                                            second result operand
              6    IN_VPR         vprex_t                   Vector predicate operand
              vec40_t vComplexSource;
              vec_t vExponentOut;
              vec_t vMantissa;
C example     vprex_t vecPred;
              ...
              vMantissa = vnormxp_v40_v32_v32_even_p (4, vComplexSource, 0, vExponentOut, 0, vecPred);

                   IN_VPR last operand is relevant only for vnormxp_v40_v32_v32_even_p
              1.
                   version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Move And Pack → Normalize → Vector Complex Normalize and Pack
Intrinsic     vnormxp_v40_v32_v32[_p]
name
Spec syntax   vnormxp {Qop [,uns][,zero_sw][,even]} vox[0], vz1[0], vz2[Ze], ?vprX

Return type   vec_t

              1    QOP            uint8     1..4            Number of atomic operations

2    IN1_V40        vec40_t                   Output vector operand
                                                            Offset for the first DW used from the first
              3    RES1_OFST      uint8     0,4
                                                            result operand
Operands
              4    RES2_V32       vec_t                     Input vector result operand
                                                            Offset for the first DW used from the
              5    RES2_OFST      uint8     0,4
                                                            second result operand
              6    IN_VPR         vprex_t                   Vector predicate operand
              vec40_t vComplexSource;
              vec_t vExponentOut;
              vec_t vMantissa;
C example     vprex_t vecPred;
              ...
              vMantissa = vnormxp_v40_v32_v32_p (4, vComplexSource, 0, vExponentOut, 0, vecPred);

              1.   IN_VPR last operand is relevant only for vnormxp_v40_v32_v32_p version.

Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Move And Pack → Normalize → Vector Complex Normalize and Pack
Intrinsic     vnormxp_v40_v32_v32_uns_even[_p]
name
Spec syntax   vnormxp {Qop [,uns][,zero_sw][,even]} vox[0], vz1[0], vz2[Ze], ?vprX

Return type   vec_t

              1    QOP            uint8     1..4            Number of atomic operations
              2    IN1_V40        vec40_t                   Output vector operand
                                                            Offset for the first DW used from the first
              3    RES1_OFST      uint8     0,4
                                                            result operand
Operands
              4    RES2_V32       vec_t                     Input vector result operand
                                                            Offset for the first DW used from the
              5    RES2_OFST      uint8     0,4
                                                            second result operand
              6    IN_VPR         vprex_t                   Vector predicate operand
              vec40_t vComplexSource;
              vec_t vExponentOut;
              vec_t vMantissa;
C example     vprex_t vecPred;
              ...

vMantissa = vnormxp_v40_v32_v32_uns_even_p (4, vComplexSource, 0, vExponentOut, 0, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vnormxp_v40_v32_v32_uns_even_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Move And Pack → Normalize → Vector Complex Normalize and Pack
Intrinsic     vnormxp_v40_v32_v32_uns[_p]
name
Spec syntax   vnormxp {Qop [,uns][,zero_sw][,even]} vox[0], vz1[0], vz2[Ze], ?vprX
Return type   vec_t

              1    QOP            uint8     1..4            Number of atomic operations
              2    IN1_V40        vec40_t                   Output vector operand
                                                            Offset for the first DW used from the first
              3    RES1_OFST      uint8     0,4
                                                            result operand
Operands
              4    RES2_V32       vec_t                     Input vector result operand
                                                            Offset for the first DW used from the
              5    RES2_OFST      uint8     0,4
                                                            second result operand
              6    IN_VPR         vprex_t                   Vector predicate operand
              vec40_t vComplexSource;
              vec_t vExponentOut;
              vec_t vMantissa;
C example     vprex_t vecPred;
              ...
              vMantissa = vnormxp_v40_v32_v32_uns_p (4, vComplexSource, 0, vExponentOut, 0, vecPred);

                   IN_VPR last operand is relevant only for vnormxp_v40_v32_v32_uns_p
              1.
                   version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Move And Pack → Normalize → Vector Complex Normalize and Pack
Intrinsic     vnormxp_v40_v32_v32_uns_zero_even[_p]
name
Spec syntax   vnormxp {Qop [,uns][,zero_sw][,even]} vox[0], vz1[0], vz2[Ze], ?vprX

Return type   vec_t

              1    QOP            uint8     1..4            Number of atomic operations

2    IN1_V40        vec40_t                   Output vector operand
                                                            Offset for the first DW used from the first
              3    RES1_OFST      uint8     0,4
                                                            result operand
Operands
              4    RES2_V32       vec_t                     Input vector result operand
                                                            Offset for the first DW used from the
              5    RES2_OFST      uint8     0,4
                                                            second result operand
              6    IN_VPR         vprex_t                   Vector predicate operand
              vec40_t vComplexSource;
              vec_t vExponentOut;
              vec_t vMantissa;
C example     vprex_t vecPred;
              ...
              vMantissa = vnormxp_v40_v32_v32_uns_zero_even_p (4, vComplexSource, 0, vExponentOut, 0,
              vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vnormxp_v40_v32_v32_uns_zero_even_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Move And Pack → Normalize → Vector Complex Normalize and Pack
Intrinsic     vnormxp_v40_v32_v32_uns_zero[_p]
name
Spec syntax   vnormxp {Qop [,uns][,zero_sw][,even]} vox[0], vz1[0], vz2[Ze], ?vprX

Return type   vec_t

              1    QOP            uint8     1..4            Number of atomic operations
              2    IN1_V40        vec40_t                   Output vector operand
                                                            Offset for the first DW used from the first
              3    RES1_OFST      uint8     0,4
                                                            result operand
Operands
              4    RES2_V32       vec_t                     Input vector result operand
                                                            Offset for the first DW used from the
              5    RES2_OFST      uint8     0,4
                                                            second result operand
              6    IN_VPR         vprex_t                   Vector predicate operand
              vec40_t vComplexSource;
              vec_t vExponentOut;

vec_t vMantissa;
C example     vprex_t vecPred;
              ...
              vMantissa = vnormxp_v40_v32_v32_uns_zero_p (4, vComplexSource, 0, vExponentOut, 0, vecPred);

              1.
                   IN_VPR last operand is relevant only for
                   vnormxp_v40_v32_v32_uns_zero_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Move And Pack → Normalize → Vector Complex Normalize and Pack
Intrinsic     vnormxp_v40_v32_v32_zero_even[_p]
name
Spec syntax   vnormxp {Qop [,uns][,zero_sw][,even]} vox[0], vz1[0], vz2[Ze], ?vprX

Return type   vec_t

Operands      1    QOP            uint8     1..4            Number of atomic operations
              2    IN1_V40        vec40_t                   Output vector operand
                                                            Offset for the first DW used from the first
              3    RES1_OFST      uint8     0,4
                                                            result operand
              4    RES2_V32       vec_t                     Input vector result operand
                                                            Offset for the first DW used from the
              5    RES2_OFST      uint8     0,4
                                                            second result operand
              6    IN_VPR         vprex_t                   Vector predicate operand
              vec40_t vComplexSource;
              vec_t vExponentOut;
              vec_t vMantissa;
C example     vprex_t vecPred;
              ...
              vMantissa = vnormxp_v40_v32_v32_zero_even_p (4, vComplexSource, 0, vExponentOut, 0, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vnormxp_v40_v32_v32_zero_even_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Move And Pack → Normalize → Vector Complex Normalize and Pack
Intrinsic     vnormxp_v40_v32_v32_zero[_p]
name
Spec syntax   vnormxp {Qop [,uns][,zero_sw][,even]} vox[0], vz1[0], vz2[Ze], ?vprX

Return type   vec_t

1    QOP            uint8     1..4            Number of atomic operations
              2    IN1_V40        vec40_t                   Output vector operand
                                                            Offset for the first DW used from the first
              3    RES1_OFST      uint8     0,4
                                                            result operand
Operands
              4    RES2_V32       vec_t                     Input vector result operand
                                                            Offset for the first DW used from the
              5    RES2_OFST      uint8     0,4
                                                            second result operand
              6    IN_VPR         vprex_t                   Vector predicate operand
              vec40_t vComplexSource;
              vec_t vExponentOut;
              vec_t vMantissa;
C example     vprex_t vecPred;
              ...
              vMantissa = vnormxp_v40_v32_v32_zero_p (4, vComplexSource, 0, vExponentOut, 0, vecPred);

                   IN_VPR last operand is relevant only for vnormxp_v40_v32_v32_zero_p
Comments      1.
                   version.
                 This intrinsic returns two results. The first result variable should be placed to
            2.   the left of the = sign (lvalue). The second result variable should be passed as
                 an additional parameter (RES2_V32).


Main table → Move And Pack → Normalize → Vector Complex Normalize and Pack
