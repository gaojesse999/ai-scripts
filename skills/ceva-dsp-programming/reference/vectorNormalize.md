# Move And Pack → Normalize → Vector Normalize

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Move And Pack → Normalize → Vector Normalize

Vector Normalize

Vector Normalize
Normalizes a 40 bit source into a mantissa part and an exponent part. The mantissa is written into
a 32-bit or 40-bit register depending on the destination register type. The exponent is wriiten into
a 16-bit or 20-bit register depending on the destination register type.
Available Switches
         Number of atomic operations. An atomic operation is defined as a normalize to exponent
Oop
         and mantissa parts.
     When used, the exponent calculated will be rounded down to an even number. In cases
even where the exponent should be an odd number, it will be decremented by 1, and the
     mantissa will shifted accordingly.
uns      When used, the evaluated source operand is unsigned. The default is signed.
zero     When used, if the source is zero, then the result is zero.
Intrinsic Names
vnorm_v40_v32_v32_even
vnorm_v40_v32_v32
vnorm_v40_v32_v32_uns_even
vnorm_v40_v32_v32_uns

vnorm_v40_v32_v32_uns_zero_even
vnorm_v40_v32_v32_uns_zero
vnorm_v40_v32_v32_zero_even
vnorm_v40_v32_v32_zero
Instruction details in the instruction set specification
Intrinsic     vnorm_v40_v32_v32_even[_p]
name
Spec syntax   vnorm {Oop [,uns][,zero_sw][,even]} vox[0], vz1[0], vz2[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V40        vec40_t                    Output vector operand
                                                             Offset for the first DW used from the
Operands      3    OUT_OFST       uint8     0,4
                                                             result operand
              4    RES2_V32       vec_t                      Input vector result operand
              5    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vExponentOut;
              vec40_t vFixedPointValue;
              vec_t vMantissa;
C example     vprex_t vecPred;
              ...
              vMantissa = vnorm_v40_v32_v32_even_p (8, vFixedPointValue, 0, vExponentOut, vecPred);

                   IN_VPR last operand is relevant only for vnorm_v40_v32_v32_even_p
              1.
                   version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Move And Pack → Normalize → Vector Normalize
Intrinsic     vnorm_v40_v32_v32[_p]
name
Spec syntax   vnorm {Oop [,uns][,zero_sw][,even]} vox[0], vz1[0], vz2[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V40        vec40_t                    Output vector operand
                                                             Offset for the first DW used from the
Operands      3    OUT_OFST       uint8     0,4
                                                             result operand
              4    RES2_V32       vec_t                      Input vector result operand
              5    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vExponentOut;
              vec40_t vFixedPointValue;
              vec_t vMantissa;
C example     vprex_t vecPred;
              ...

vMantissa = vnorm_v40_v32_v32_p (8, vFixedPointValue, 0, vExponentOut, vecPred);
              1.   IN_VPR last operand is relevant only for vnorm_v40_v32_v32_p version.

Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Move And Pack → Normalize → Vector Normalize
Intrinsic     vnorm_v40_v32_v32_uns_even[_p]
name
Spec syntax   vnorm {Oop [,uns][,zero_sw][,even]} vox[0], vz1[0], vz2[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
              2    IN1_V40        vec40_t                   Output vector operand
                                                            Offset for the first DW used from the
Operands      3    OUT_OFST       uint8     0,4
                                                            result operand
              4    RES2_V32       vec_t                     Input vector result operand
              5    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vExponentOut;
              vec40_t vFixedPointValue;
              vec_t vMantissa;
C example     vprex_t vecPred;
              ...
              vMantissa = vnorm_v40_v32_v32_uns_even_p (8, vFixedPointValue, 0, vExponentOut, vecPred);

                   IN_VPR last operand is relevant only for vnorm_v40_v32_v32_uns_even_p
              1.
                   version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Move And Pack → Normalize → Vector Normalize
Intrinsic     vnorm_v40_v32_v32_uns[_p]
name
Spec syntax   vnorm {Oop [,uns][,zero_sw][,even]} vox[0], vz1[0], vz2[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
              2    IN1_V40        vec40_t                   Output vector operand
Operands                                                    Offset for the first DW used from the
              3    OUT_OFST       uint8     0,4
                                                            result operand

4    RES2_V32       vec_t                     Input vector result operand
              5    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vExponentOut;
              vec40_t vFixedPointValue;
              vec_t vMantissa;
C example     vprex_t vecPred;
              ...
              vMantissa = vnorm_v40_v32_v32_uns_p (8, vFixedPointValue, 0, vExponentOut, vecPred);

                   IN_VPR last operand is relevant only for vnorm_v40_v32_v32_uns_p
              1.
                   version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Move And Pack → Normalize → Vector Normalize
Intrinsic     vnorm_v40_v32_v32_uns_zero_even[_p]
name
Spec syntax   vnorm {Oop [,uns][,zero_sw][,even]} vox[0], vz1[0], vz2[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
              2    IN1_V40        vec40_t                   Output vector operand
                                                            Offset for the first DW used from the
Operands      3    OUT_OFST       uint8     0,4
                                                            result operand
              4    RES2_V32       vec_t                     Input vector result operand
              5    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vExponentOut;
              vec40_t vFixedPointValue;
              vec_t vMantissa;
C example     vprex_t vecPred;
              ...
              vMantissa = vnorm_v40_v32_v32_uns_zero_even_p (8, vFixedPointValue, 0, vExponentOut, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vnorm_v40_v32_v32_uns_zero_even_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Move And Pack → Normalize → Vector Normalize
Intrinsic     vnorm_v40_v32_v32_uns_zero[_p]
name
Spec syntax   vnorm {Oop [,uns][,zero_sw][,even]} vox[0], vz1[0], vz2[0], ?vprX
Return type   vec_t

1    OOP            uint8     1..8            Number of atomic operations
              2    IN1_V40        vec40_t                   Output vector operand
                                                            Offset for the first DW used from the
Operands      3    OUT_OFST       uint8     0,4
                                                            result operand
              4    RES2_V32       vec_t                     Input vector result operand
              5    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vExponentOut;
              vec40_t vFixedPointValue;
              vec_t vMantissa;
C example     vprex_t vecPred;
              ...
              vMantissa = vnorm_v40_v32_v32_uns_zero_p (8, vFixedPointValue, 0, vExponentOut, vecPred);

                   IN_VPR last operand is relevant only for vnorm_v40_v32_v32_uns_zero_p
              1.
                   version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Move And Pack → Normalize → Vector Normalize
Intrinsic     vnorm_v40_v32_v32_zero_even[_p]
name
Spec syntax   vnorm {Oop [,uns][,zero_sw][,even]} vox[0], vz1[0], vz2[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
              2    IN1_V40        vec40_t                   Output vector operand
                                                            Offset for the first DW used from the
Operands      3    OUT_OFST       uint8     0,4
                                                            result operand
              4    RES2_V32       vec_t                     Input vector result operand
              5    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vExponentOut;
              vec40_t vFixedPointValue;
              vec_t vMantissa;
C example     vprex_t vecPred;
              ...
              vMantissa = vnorm_v40_v32_v32_zero_even_p (8, vFixedPointValue, 0, vExponentOut, vecPred);

                   IN_VPR last operand is relevant only for vnorm_v40_v32_v32_zero_even_p
              1.
                   version.
Comments
                   This intrinsic returns two results. The first result variable should be placed to
              2.

the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Move And Pack → Normalize → Vector Normalize
Intrinsic     vnorm_v40_v32_v32_zero[_p]
name
Spec syntax   vnorm {Oop [,uns][,zero_sw][,even]} vox[0], vz1[0], vz2[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V40        vec40_t                    Output vector operand
                                                             Offset for the first DW used from the
Operands      3    OUT_OFST       uint8     0,4
                                                             result operand
              4    RES2_V32       vec_t                      Input vector result operand
              5    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vExponentOut;
              vec40_t vFixedPointValue;
              vec_t vMantissa;
C example     vprex_t vecPred;
              ...
              vMantissa = vnorm_v40_v32_v32_zero_p (8, vFixedPointValue, 0, vExponentOut, vecPred);

                   IN_VPR last operand is relevant only for vnorm_v40_v32_v32_zero_p
              1.
                   version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Move And Pack → Normalize → Vector Normalize
