# Data Reordering → Transpose → Vector Complex Transpose

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Data Reordering → Transpose → Vector Complex Transpose

Vector Complex Transpose

Vector Complex Transpose

Performs transpose of vertical complex number vector within a matrix into an horizontal
complex vector destination. Each complex source consists of real 32-bit part and imaginary 32-
bit part.
Available Switches
2vec             Two vectors with complex double-word are read
3vec             Three vectors with complex double-word are read
4vec             Four vectors with complex double-word are read
Dop              Number of atomic operations. 1op ≤ Dop ≤ 2op
Intrinsic Names
vtransx_v32_v32_v32_uimm3_v32_3vec
vtransx_v32_v32_v32_c32_v32_3vec
vtransx_v32_v32_v32_v32_uimm3_v32_4vec
vtransx_v32_v32_uimm3_v32_2vec
vtransx_v32_v32_v32_v32_c32_v32_4vec
vtransx_v32_v32_c32_v32_2vec
Instruction details in the instruction set specification
Intrinsic     vtransx_v32_v32_v32_uimm3_v32_3vec[_p]
name
Spec syntax   vtransx {3vec} vix, viy, vip, #uimm3, vz[0], ?vprX

Return type   vec_t

              1    IN1_V32        vec_t                     Input vector operand
              2    IN2_V32        vec_t                     Input vector operand
Operands      3    IN3_V32        vec_t                     Input vector operand
              4    IN4_UIMM3      uint8     0..7            3 bit unsigned immediate
              5    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
C example     vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vtransx_v32_v32_v32_uimm3_v32_3vec_p (vIn, vIn2, vIn3, 2, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vtransx_v32_v32_v32_uimm3_v32_3vec_p version.


Main table → Data Reordering → Transpose → Vector Complex Transpose
Intrinsic     vtransx_v32_v32_v32_c32_v32_3vec[_p]
name
Spec syntax   vtransx {3vec} vix, viy, vip, vcY, vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                     Input vector operand
              2    IN2_V32         vec_t                     Input vector operand
Operands      3    IN3_V32         vec_t                     Input vector operand
              4    IN4_C32         coef_t                    Coefficient operand
              5    IN_VPR          vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vRes;
C example     coef_t vcoefIn;
              vprex_t vecPred;
              ...

vRes = vtransx_v32_v32_v32_c32_v32_3vec_p (vIn, vIn2, vIn3, vcoefIn, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vtransx_v32_v32_v32_c32_v32_3vec_p version.


Main table → Data Reordering → Transpose → Vector Complex Transpose
Intrinsic     vtransx_v32_v32_v32_v32_uimm3_v32_4vec[_p]
name
Spec syntax   vtransx {4vec} vix, viy, vip, viq, #uimm3, vz[0], ?vprX

Return type   vec_t

              1    IN1_V32        vec_t                     Input vector operand
              2    IN2_V32        vec_t                     Input vector operand
              3    IN3_V32        vec_t                     Input vector operand
Operands
              4    IN4_V32        vec_t                     Input vector operand
              5    IN5_UIMM3      uint8     0..7            3 bit unsigned immediate
              6    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vtransx_v32_v32_v32_v32_uimm3_v32_4vec_p (vIn, vIn2, vIn3, vIn4, 2, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vtransx_v32_v32_v32_v32_uimm3_v32_4vec_p version.


Main table → Data Reordering → Transpose → Vector Complex Transpose
Intrinsic     vtransx_v32_v32_uimm3_v32_2vec[_p]
name
Spec syntax   vtransx {2vec ,Dop} vix, viy, #uimm3, vz[0], ?vprX

Return type   vec_t

              1    DOP            uint8     1..2             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand
Operands      3    IN2_V32        vec_t                      Input vector operand
              4    IN3_UIMM3      uint8     0..7             3 bit unsigned immediate
              5    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vtransx_v32_v32_uimm3_v32_2vec_p (2, vIn, vIn2, 2, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vtransx_v32_v32_uimm3_v32_2vec_p version.


Main table → Data Reordering → Transpose → Vector Complex Transpose
Intrinsic     vtransx_v32_v32_v32_v32_c32_v32_4vec[_p]
name

Spec syntax   vtransx {4vec} vix, viy, vip, viq, vcY, vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                     Input vector operand
              2    IN2_V32         vec_t                     Input vector operand
              3    IN3_V32         vec_t                     Input vector operand
Operands
              4    IN4_V32         vec_t                     Input vector operand
              5    IN5_C32         coef_t                    Coefficient operand
              6    IN_VPR          vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes;
              coef_t vcoefIn;
              vprex_t vecPred;
              ...
              vRes = vtransx_v32_v32_v32_v32_c32_v32_4vec_p (vIn, vIn2, vIn3, vIn4, vcoefIn, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vtransx_v32_v32_v32_v32_c32_v32_4vec_p version.


Main table → Data Reordering → Transpose → Vector Complex Transpose
Intrinsic     vtransx_v32_v32_c32_v32_2vec[_p]
name
Spec syntax   vtransx {2vec ,Dop} vix, viy, vcY, vz[0], ?vprX

Return type   vec_t

              1    DOP             uint8     1..2             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand
Operands      3    IN2_V32         vec_t                      Input vector operand
              4    IN3_C32         coef_t                     Coefficient operand
              5    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     coef_t vcoefIn;
              vprex_t vecPred;
              ...
              vRes = vtransx_v32_v32_c32_v32_2vec_p (2, vIn, vIn2, vcoefIn, vecPred);

                   IN_VPR last operand is relevant only for vtransx_v32_v32_c32_v32_2vec_p
Comments      1.
                   version.


Main table → Data Reordering → Transpose → Vector Complex Transpose
