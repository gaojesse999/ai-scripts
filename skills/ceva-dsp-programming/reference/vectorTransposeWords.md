# Data Reordering → Transpose → Vector Transpose Words

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Data Reordering → Transpose → Vector Transpose Words

Vector Transpose Words

Vector Transpose Words
Performs transpose of vertical word vector within a matrix into an horizontal word vector
destination.
Available Switches
2w       Two vector with word sources are read
3w       Three vector with word sources are read
4w       Four vector with word sources are read
Nop      Number of atomic operations. Nop is 1op, 2op or 4op. The default is 1op.
Intrinsic Names
vtransw_v32_v32_v32_c32_v32_3w_Nop
vtransw_v32_v32_v32_c32_v32_3w
vtransw_v32_v32_v32_uimm3_v32_3w_Nop
vtransw_v32_v32_v32_uimm3_v32_3w
vtransw_v32_v32_c32_v32_2w_Nop
vtransw_v32_v32_c32_v32_2w
vtransw_v32_v32_uimm3_v32_2w_Nop
vtransw_v32_v32_uimm3_v32_2w
vtransw_v32_v32_v32_v32_c32_v32_4w_Nop
vtransw_v32_v32_v32_v32_c32_v32_4w
vtransw_v32_v32_v32_v32_uimm3_v32_4w_Nop
vtransw_v32_v32_v32_v32_uimm3_v32_4w
Instruction details in the instruction set specification
Intrinsic     vtransw_v32_v32_v32_c32_v32_3w_Nop[_p]
name
Spec syntax   vtransw {3w [,Nop]} vix, viy, vip, vcY, vz[0], ?vprX

Return type   vec_t

              1    NOP            uint8     1,2,4            Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
Operands
              4    IN3_V32        vec_t                      Input vector operand
              5    IN4_C32        coef_t                     Coefficient operand
              6    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vRes;
C example     coef_t vcoefIn;
              vprex_t vecPred;
              ...
              vRes = vtransw_v32_v32_v32_c32_v32_3w_Nop_p (4, vIn, vIn2, vIn3, vcoefIn, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vtransw_v32_v32_v32_c32_v32_3w_Nop_p version.


Main table → Data Reordering → Transpose → Vector Transpose Words
Intrinsic     vtransw_v32_v32_v32_c32_v32_3w[_p]
name

Spec syntax   vtransw {3w [,Nop]} vix, viy, vip, vcY, vz[0], ?vprX

Return type   vec_t

              1    IN1_V32        vec_t                      Input vector operand
              2    IN2_V32        vec_t                      Input vector operand
Operands      3    IN3_V32        vec_t                      Input vector operand
              4    IN4_C32        coef_t                     Coefficient operand
              5    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vRes;
C example     coef_t vcoefIn;
              vprex_t vecPred;
              ...
              vRes = vtransw_v32_v32_v32_c32_v32_3w_p (vIn, vIn2, vIn3, vcoefIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for
               vtransw_v32_v32_v32_c32_v32_3w_p version.


Main table → Data Reordering → Transpose → Vector Transpose Words
Intrinsic     vtransw_v32_v32_v32_uimm3_v32_3w_Nop[_p]
name
Spec syntax   vtransw {3w [,Nop]} vix, viy, vip, #uimm3, vz[0], ?vprX

Return type   vec_t

              1    NOP            uint8     1,2,4           Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
Operands
              4    IN3_V32        vec_t                     Input vector operand
              5    IN4_UIMM3      uint8     0..7            3 bit unsigned immediate
              6    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
C example     vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vtransw_v32_v32_v32_uimm3_v32_3w_Nop_p (4, vIn, vIn2, vIn3, 2, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vtransw_v32_v32_v32_uimm3_v32_3w_Nop_p version.


Main table → Data Reordering → Transpose → Vector Transpose Words
Intrinsic     vtransw_v32_v32_v32_uimm3_v32_3w[_p]
name
Spec syntax   vtransw {3w [,Nop]} vix, viy, vip, #uimm3, vz[0], ?vprX

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
              vRes = vtransw_v32_v32_v32_uimm3_v32_3w_p (vIn, vIn2, vIn3, 2, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vtransw_v32_v32_v32_uimm3_v32_3w_p version.

Main table → Data Reordering → Transpose → Vector Transpose Words
Intrinsic     vtransw_v32_v32_c32_v32_2w_Nop[_p]
name
Spec syntax   vtransw {2w [,Nop]} vix, viy, vcY, vz[0], ?vprX

Return type   vec_t

              1    NOP            uint8     1,2,4            Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand
Operands      3    IN2_V32        vec_t                      Input vector operand
              4    IN3_C32        coef_t                     Coefficient operand
              5    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     coef_t vcoefIn;
              vprex_t vecPred;
              ...
              vRes = vtransw_v32_v32_c32_v32_2w_Nop_p (4, vIn, vIn2, vcoefIn, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vtransw_v32_v32_c32_v32_2w_Nop_p version.


Main table → Data Reordering → Transpose → Vector Transpose Words
Intrinsic     vtransw_v32_v32_c32_v32_2w[_p]
name
Spec syntax   vtransw {2w [,Nop]} vix, viy, vcY, vz[0], ?vprX

Return type   vec_t

              1    IN1_V32        vec_t                      Input vector operand
              2    IN2_V32        vec_t                      Input vector operand
Operands
              3    IN3_C32        coef_t                     Coefficient operand
              4    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     coef_t vcoefIn;
              vprex_t vecPred;
              ...
              vRes = vtransw_v32_v32_c32_v32_2w_p (vIn, vIn2, vcoefIn, vecPred);

                   IN_VPR last operand is relevant only for vtransw_v32_v32_c32_v32_2w_p
Comments      1.
                   version.

Main table → Data Reordering → Transpose → Vector Transpose Words
Intrinsic     vtransw_v32_v32_uimm3_v32_2w_Nop[_p]
name
Spec syntax   vtransw {2w [,Nop]} vix, viy, #uimm3, vz[0], ?vprX

Return type   vec_t

              1    NOP            uint8     1,2,4          Number of atomic operations
              2    IN1_V32        vec_t                    Input vector operand
Operands      3    IN2_V32        vec_t                    Input vector operand
              4    IN3_UIMM3      uint8     0..7           3 bit unsigned immediate
              5    IN_VPR         vprex_t                  Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vtransw_v32_v32_uimm3_v32_2w_Nop_p (4, vIn, vIn2, 2, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vtransw_v32_v32_uimm3_v32_2w_Nop_p version.


Main table → Data Reordering → Transpose → Vector Transpose Words
Intrinsic     vtransw_v32_v32_uimm3_v32_2w[_p]
name
Spec syntax   vtransw {2w [,Nop]} vix, viy, #uimm3, vz[0], ?vprX

Return type   vec_t

              1    IN1_V32        vec_t                    Input vector operand
              2    IN2_V32        vec_t                    Input vector operand
Operands
              3    IN3_UIMM3      uint8     0..7           3 bit unsigned immediate
              4    IN_VPR         vprex_t                  Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vtransw_v32_v32_uimm3_v32_2w_p (vIn, vIn2, 2, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vtransw_v32_v32_uimm3_v32_2w_p version.


Main table → Data Reordering → Transpose → Vector Transpose Words
Intrinsic     vtransw_v32_v32_v32_v32_c32_v32_4w_Nop[_p]
name
Spec syntax   vtransw {4w [,Nop]} vix, viy, vip, viq, vcY, vz[0], ?vprX

Return type   vec_t

              1    NOP            uint8     1,2,4            Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
Operands      4    IN3_V32        vec_t                      Input vector operand
              5    IN4_V32        vec_t                      Input vector operand

6    IN5_C32        coef_t                     Coefficient operand
              7    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes;
              coef_t vcoefIn;
              vprex_t vecPred;
              ...
              vRes = vtransw_v32_v32_v32_v32_c32_v32_4w_Nop_p (4, vIn, vIn2, vIn3, vIn4, vcoefIn, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vtransw_v32_v32_v32_v32_c32_v32_4w_Nop_p version.


Main table → Data Reordering → Transpose → Vector Transpose Words
Intrinsic     vtransw_v32_v32_v32_v32_c32_v32_4w[_p]
name
Spec syntax   vtransw {4w [,Nop]} vix, viy, vip, viq, vcY, vz[0], ?vprX

Return type   vec_t

              1    IN1_V32        vec_t                      Input vector operand
              2    IN2_V32        vec_t                      Input vector operand
              3    IN3_V32        vec_t                      Input vector operand
Operands
              4    IN4_V32        vec_t                      Input vector operand
              5    IN5_C32        coef_t                     Coefficient operand
              6    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
C example     vec_t vIn3;
              vec_t vIn4;
              vec_t vRes;
            coef_t vcoefIn;
            vprex_t vecPred;
            ...
            vRes = vtransw_v32_v32_v32_v32_c32_v32_4w_p (vIn, vIn2, vIn3, vIn4, vcoefIn, vecPred);

                 IN_VPR last operand is relevant only for
Comments    1.
                 vtransw_v32_v32_v32_v32_c32_v32_4w_p version.


Main table → Data Reordering → Transpose → Vector Transpose Words
Intrinsic     vtransw_v32_v32_v32_v32_uimm3_v32_4w_Nop[_p]
name
Spec syntax   vtransw {4w [,Nop]} vix, viy, vip, viq, #uimm3, vz[0], ?vprX

Return type   vec_t

              1    NOP            uint8     1,2,4           Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
Operands      4    IN3_V32        vec_t                     Input vector operand
              5    IN4_V32        vec_t                     Input vector operand

6    IN5_UIMM3      uint8     0..7            3 bit unsigned immediate
              7    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vtransw_v32_v32_v32_v32_uimm3_v32_4w_Nop_p (4, vIn, vIn2, vIn3, vIn4, 2, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vtransw_v32_v32_v32_v32_uimm3_v32_4w_Nop_p version.


Main table → Data Reordering → Transpose → Vector Transpose Words
Intrinsic     vtransw_v32_v32_v32_v32_uimm3_v32_4w[_p]
name
Spec syntax   vtransw {4w [,Nop]} vix, viy, vip, viq, #uimm3, vz[0], ?vprX

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
C example     vec_t vIn4;
              vec_t vRes;
              vprex_t vecPred;
            ...
            vRes = vtransw_v32_v32_v32_v32_uimm3_v32_4w_p (vIn, vIn2, vIn3, vIn4, 2, vecPred);

                 IN_VPR last operand is relevant only for
Comments    1.
                 vtransw_v32_v32_v32_v32_uimm3_v32_4w_p version.


Main table → Data Reordering → Transpose → Vector Transpose Words
