# Data Reordering → Transpose → Vector Transpose Double Words

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Data Reordering → Transpose → Vector Transpose Double Words

Vector Transpose Double Words

Vector Transpose Double Words
Performs transpose of vertical double-word vector within a matrix into an horizontal double-
word vector destination.
Available Switches
2dw            Two vectors with double-word sources are read

3dw            Three vectors with double-word sources are read
4dw            Four vectors with double-word sources are read
Dop            Number of atomic operations. 1op ≤ Dop ≤ 2op
Intrinsic Names
vtransdw_v32_v32_v32_c32_v32_3dw
vtransdw_v32_v32_v32_v32_c32_v32_4dw
vtransdw_v32_v32_v32_v32_uimm3_v32_4dw
vtransdw_v32_v32_v32_uimm3_v32_3dw
vtransdw_v32_v32_c32_v32_2dw
vtransdw_v32_v32_v32_v32_uimm3_v32_v32_4dw_2op
vtransdw_v32_v32_uimm3_v32_2dw
vtransdw_v32_v32_v32_v32_c32_v32_v32_4dw_2op
Instruction details in the instruction set specification
Intrinsic     vtransdw_v32_v32_v32_c32_v32_3dw[_p]
name
Spec syntax   vtransdw {3dw ,Dop} vix, viy, vip, vcY, vz[0], ?vprX

Return type   vec_t

              1    DOP            uint8     1..2             Number of atomic operations
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
              vRes = vtransdw_v32_v32_v32_c32_v32_3dw_p (2, vIn, vIn2, vIn3, vcoefIn, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vtransdw_v32_v32_v32_c32_v32_3dw_p version.


Main table → Data Reordering → Transpose → Vector Transpose Double Words
Intrinsic     vtransdw_v32_v32_v32_v32_c32_v32_4dw[_p]
name
Spec syntax   vtransdw {4dw ,Dop} vix, viy, vip, viq, vcY, vz[0], ?vprX

Return type   vec_t

              1    DOP            uint8     1..2             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
Operands      4    IN3_V32        vec_t                      Input vector operand
              5    IN4_V32        vec_t                      Input vector operand
              6    IN5_C32        coef_t                     Coefficient operand
              7    IN_VPR         vprex_t                    Vector predicate operand
              cint16 *pin0;
              cint16 *pin1;

cint16 *pin2;
              cint16 *pin3;
              vec_t vIn3,vIn2,vIn1,vIn;
              vec40_t vRes;
              coef_t     vcoefIn;
              for (i=0; i < count; i++)
C example     {
                 vIn = vlddw_v32(2,pin0,0); pin0+=4;
                 vIn1 = vlddw_v32(2,pin1,0); pin1+=4;
                 vIn2 = vlddw_v32(2,pin2,0); pin2+=4;
                 vIn3 = vlddw_v32(2,pin3,0); pin3+=4;
                 vRes = vtransdw_v32_v32_v32_v32_c32_v32_4dw_p (2, vIn, vIn1, vIn2, vIn3, vcoefIn);
                 vstdw_v40_concat(8,vRes,0,dst); dst+=16;
              }

                   IN_VPR last operand is relevant only for
Comments      1.
                   vtransdw_v32_v32_v32_v32_c32_v32_4dw_p version.


Main table → Data Reordering → Transpose → Vector Transpose Double Words
Intrinsic     vtransdw_v32_v32_v32_v32_uimm3_v32_4dw[_p]
name
Spec syntax   vtransdw {4dw ,Dop} vix, viy, vip, viq, #uimm3, vz[0], ?vprX

Return type   vec_t

              1    DOP            uint8     1..2            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
Operands      4    IN3_V32        vec_t                     Input vector operand
              5    IN4_V32        vec_t                     Input vector operand
              6    IN5_UIMM3      uint8     0..7            3 bit unsigned immediate
              7    IN_VPR         vprex_t                   Vector predicate operand
              cint16 *pin0;
              cint16 *pin1;
              cint16 *pin2;
              cint16 *pin3;
              vec_t vIn3,vIn2,vIn1,vIn;
              vec40_t vRes;
              for (i=0; i < count; i++)
C example     {
                 vIn = vlddw_v32(2,pin0,0); pin0+=4;
                 vIn1 = vlddw_v32(2,pin1,0); pin1+=4;
                 vIn2 = vlddw_v32(2,pin2,0); pin2+=4;
                 vIn3 = vlddw_v32(2,pin3,0); pin3+=4;
                 vRes = vtransdw_v32_v32_v32_v32_uimm3_v32_4dw(2, vIn, vIn1, vIn2, vIn3, 0x0);
                 vstdw_v40_concat(8,vRes,0,dst); dst+=16;
              }

                   IN_VPR last operand is relevant only for
Comments      1.
                   vtransdw_v32_v32_v32_v32_uimm3_v32_4dw_p version.


Main table → Data Reordering → Transpose → Vector Transpose Double Words
Intrinsic     vtransdw_v32_v32_v32_uimm3_v32_3dw[_p]
name

Spec syntax   vtransdw {3dw ,Dop} vix, viy, vip, #uimm3, vz[0], ?vprX

Return type   vec_t

              1    DOP            uint8     1..2            Number of atomic operations
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
              vRes = vtransdw_v32_v32_v32_uimm3_v32_3dw_p (2, vIn, vIn2, vIn3, 2, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vtransdw_v32_v32_v32_uimm3_v32_3dw_p version.


Main table → Data Reordering → Transpose → Vector Transpose Double Words
Intrinsic     vtransdw_v32_v32_c32_v32_2dw[_p]
name
Spec syntax   vtransdw {2dw ,Dop} vix, viy, vcY, vz[0], ?vprX

Return type   vec_t

              1    DOP            uint8     1..2             Number of atomic operations
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
              vRes = vtransdw_v32_v32_c32_v32_2dw_p (2, vIn, vIn2, vcoefIn, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vtransdw_v32_v32_c32_v32_2dw_p version.


Main table → Data Reordering → Transpose → Vector Transpose Double Words
Intrinsic     vtransdw_v32_v32_v32_v32_uimm3_v32_v32_4dw_2op[_p]
name
Spec syntax   vtransdw {4dw ,2op} vix, viy, vip, viq, #uimm3, vz1[0], vz2[0], ?vprX

Return type   vec_t

              1    IN1_V32        vec_t                    Input vector operand
              2    IN2_V32        vec_t                    Input vector operand
              3    IN3_V32        vec_t                    Input vector operand

4    IN4_V32        vec_t                    Input vector operand
Operands      5    IN5_UIMM3      uint8     0..7           3 bit unsigned immediate
                                                           Offset for the first DW used from the
              6    OUT_OFST       uint8     0,4
                                                           result operand
              7    RES2_V32       vec_t                    Input vector result operand
              8    IN_VPR         vprex_t                  Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
              vec_t vRes1;
C example     vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vtransdw_v32_v32_v32_v32_uimm3_v32_v32_4dw_2op_p (vIn, vIn2, vIn3, vIn4, 2, 0, vRes2,
              vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vtransdw_v32_v32_v32_v32_uimm3_v32_v32_4dw_2op_p version.
                   This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).
Comments
                   The vtransdw_v32_v32_v32_v32_uimm3_v32_v32_4dw_2op_p intrinsic has
                   different latency in case the Demapper block is installed/not installed on the
                   HW. When Demapper is not installed, 1/2 cycles are added after the
              3.
                   generated vector instruction. The SDT default is "Demapper installed".
                   Therefore, for ensuring correct execution on the HW, the -mno-demapper
                   Compiler switch must be specified in case Demapper is not installed.


Main table → Data Reordering → Transpose → Vector Transpose Double Words
Intrinsic     vtransdw_v32_v32_uimm3_v32_2dw[_p]
name
Spec syntax   vtransdw {2dw ,Dop} vix, viy, #uimm3, vz[0], ?vprX

Return type   vec_t

              1    DOP            uint8     1..2            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand
Operands      3    IN2_V32        vec_t                     Input vector operand
              4    IN3_UIMM3      uint8     0..7            3 bit unsigned immediate
              5    IN_VPR         vprex_t                   Vector predicate operand

vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vtransdw_v32_v32_uimm3_v32_2dw_p (2, vIn, vIn2, 2, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vtransdw_v32_v32_uimm3_v32_2dw_p version.


Main table → Data Reordering → Transpose → Vector Transpose Double Words
Intrinsic     vtransdw_v32_v32_v32_v32_c32_v32_v32_4dw_2op[_p]
name
Spec syntax   vtransdw {4dw ,2op} vix, viy, vip, viq, vcY, vz1[0], vz2[0], ?vprX

Return type   vec_t

              1    IN1_V32        vec_t                     Input vector operand
              2    IN2_V32        vec_t                     Input vector operand
              3    IN3_V32        vec_t                     Input vector operand
              4    IN4_V32        vec_t                     Input vector operand
Operands      5    IN5_C32        coef_t                    Coefficient operand
                                                            Offset for the first DW used from the
              6    OUT_OFST       uint8     0,4
                                                            result operand
              7    RES2_V32       vec_t                     Input vector result operand
              8    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
              vec_t vRes1;
C example     vec_t vRes2;
              coef_t vcoefIn;
              vprex_t vecPred;
              ...
              vRes1 = vtransdw_v32_v32_v32_v32_c32_v32_v32_4dw_2op_p (vIn, vIn2, vIn3, vIn4, vcoefIn, 0, vRes2,
              vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vtransdw_v32_v32_v32_v32_c32_v32_v32_4dw_2op_p version.
                   This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).
Comments
                   The vtransdw_v32_v32_v32_v32_c32_v32_v32_4dw_2op_p intrinsic has
                   different latency in case the Demapper block is installed/not installed on the
                   HW. When Demapper is not installed, 1/2 cycles are added after the
              3.

generated vector instruction. The SDT default is "Demapper installed".
                   Therefore, for ensuring correct execution on the HW, the -mno-demapper
                   Compiler switch must be specified in case Demapper is not installed.


Main table → Data Reordering → Transpose → Vector Transpose Double Words
