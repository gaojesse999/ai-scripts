# Move And Pack → Move → Vector Move VB Word Parts

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Move And Pack → Move → Vector Move VB Word Parts

Vector Move VB Word Parts

Vector Move VB Word Parts
Performs two data move from source to destination. The sources are 16-bit wide and the
destinations are either 16-bit or 20-bit wide packed into 32-bit or 40-bit wide determined by the
vector register type.
Available Switches
           Number of atomic operations. An atomic operation is defined as a single move
Oop
           operation. 1op ≤ Oop ≤ 8op
           Number of atomic operations. An atomic operation is defined as a single move
Qop
           operation. 1op ≤ Qop ≤ 4op
lone       Performs leading one detection on predicate source
lzero      Performs leading zero detection on predicate source
           When used, the rest of each destination which is written is zero-extended. The default is
u
           sign-extended.

When used, the rest of each destination which is written is unchanged. The default is
unch
           sign-extended.
vuX        Determines the destination VCU of the instruction. X is replaced by 0 or 1.
Intrinsic Names
vmovw_c32_v40_1op
vmovw_c32_v40_1op_u
vmovw_c32_v40_2op
vmovw_c32_v40_2op_u
vmovw_c32_v40_3op
vmovw_c32_v40_3op_u
vmovw_c32_v40_4op
vmovw_c32_v40_4op_u
vmovw_v32_v40
vmovw_v32_v40_u
vmovw_v32_v40_unch
vmovw_v32_vpr_c32_lzero
vmovw_v32_v32
vmovw_c32_v32_1op
vmovw_c32_v32_2op
vmovw_c32_v32_3op
vmovw_c32_v32_4op
vmovw_c32
vmovw_v32_vpr_c32_lone
vmovw_v32_c32_1op
vmovw_v32_c32_2op
vmovw_v32_c32_3op
vmovw_v32_c32_4op
vmovw_c32_vuX
Instruction details in the instruction set specification
Intrinsic     vmovw_c32_v40_1op[_p]
name
Spec syntax   vmovw {Qop [,u]} vc0, voz[0], ?vprX

Return type   vec40_t


              1
                                                            Coefficient operand (register vc0 is
                   IN1_VC0        coef_t
                                                            expected)
Operands                                                    Offset for the first DW used from the
              2    OUT_OFST       uint8     0,4
                                                            result operand
              3    IN_VPR         vprex_t                   Vector predicate operand
              vec40_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vmovw_c32_v40_1op_p (vcoefIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmovw_c32_v40_1op_p version.


Main table → Move And Pack → Move → Vector Move VB Word Parts
Intrinsic     vmovw_c32_v40_1op_u[_p]
name
Spec syntax   vmovw {Qop [,u]} vc0, voz[0], ?vprX

Return type   vec40_t

                                                            Coefficient operand (register vc0 is
              1    IN1_VC0        coef_t
                                                            expected)
Operands                                                    Offset for the first DW used from the
              2    OUT_OFST       uint8     0,4
                                                            result operand
              3    IN_VPR         vprex_t                   Vector predicate operand
              vec40_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vmovw_c32_v40_1op_u_p (vcoefIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmovw_c32_v40_1op_u_p version.


Main table → Move And Pack → Move → Vector Move VB Word Parts
Intrinsic     vmovw_c32_v40_2op[_p]
name
Spec syntax   vmovw {Qop [,u]} vc0, voz[0], ?vprX

Return type   vec40_t

Operands      1    IN1_VC0        coef_t                    Coefficient operand (register vc0 is
                                                             expected)
                                                             Coefficient operand (register vc1 is
              2    IN2_VC1        coef_t
                                                             expected)

              3
                                                             Offset for the first DW used from the
                   OUT_OFST       uint8     0,4
                                                             result operand
              4    IN_VPR         vprex_t                    Vector predicate operand
              vec40_t vRes;
              coef_t vcoefIn;
              coef_t vcoefIn2;
C example     vprex_t vecPred;
              ...
              vRes = vmovw_c32_v40_2op_p (vcoefIn, vcoefIn2, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmovw_c32_v40_2op_p version.


Main table → Move And Pack → Move → Vector Move VB Word Parts
Intrinsic     vmovw_c32_v40_2op_u[_p]
name
Spec syntax   vmovw {Qop [,u]} vc0, voz[0], ?vprX

Return type   vec40_t

                                                             Coefficient operand (register vc0 is
              1    IN1_VC0        coef_t
                                                             expected)
                                                             Coefficient operand (register vc1 is
              2    IN2_VC1        coef_t
Operands                                                     expected)
                                                             Offset for the first DW used from the
              3    OUT_OFST       uint8     0,4
                                                             result operand
              4    IN_VPR         vprex_t                    Vector predicate operand
              vec40_t vRes;
              coef_t vcoefIn;
              coef_t vcoefIn2;
C example     vprex_t vecPred;
              ...
              vRes = vmovw_c32_v40_2op_u_p (vcoefIn, vcoefIn2, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmovw_c32_v40_2op_u_p version.

Main table → Move And Pack → Move → Vector Move VB Word Parts
Intrinsic     vmovw_c32_v40_3op[_p]
name
Spec syntax   vmovw {Qop [,u]} vc0, voz[0], ?vprX

Return type   vec40_t

Operands      1    IN1_VC0        coef_t                     Coefficient operand (register vc0 is
                                                             expected)
                                                             Coefficient operand (register vc1 is
              2    IN2_VC1         coef_t
                                                             expected)

              3
                                                             Coefficient operand (register vc2 is
                   IN3_VC2         coef_t
                                                             expected)
                                                             Offset for the first DW used from the
              4    OUT_OFST        uint8     0,4
                                                             result operand
              5    IN_VPR          vprex_t                   Vector predicate operand
              vec40_t vRes;
              coef_t vcoefIn;
              coef_t vcoefIn2;
C example     coef_t vcoefIn3;
              vprex_t vecPred;
              ...
              vRes = vmovw_c32_v40_3op_p (vcoefIn, vcoefIn2, vcoefIn3, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmovw_c32_v40_3op_p version.


Main table → Move And Pack → Move → Vector Move VB Word Parts
Intrinsic     vmovw_c32_v40_3op_u[_p]
name
Spec syntax   vmovw {Qop [,u]} vc0, voz[0], ?vprX

Return type   vec40_t

                                                             Coefficient operand (register vc0 is
              1    IN1_VC0         coef_t
                                                             expected)
                                                             Coefficient operand (register vc1 is
              2    IN2_VC1         coef_t
                                                             expected)
Operands                                                     Coefficient operand (register vc2 is
              3    IN3_VC2         coef_t
                                                             expected)

              4
                                                             Offset for the first DW used from the
                   OUT_OFST        uint8     0,4
                                                             result operand

5    IN_VPR          vprex_t                   Vector predicate operand
              vec40_t vRes;
              coef_t vcoefIn;
              coef_t vcoefIn2;
C example     coef_t vcoefIn3;
              vprex_t vecPred;
              ...
              vRes = vmovw_c32_v40_3op_u_p (vcoefIn, vcoefIn2, vcoefIn3, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmovw_c32_v40_3op_u_p version.


Main table → Move And Pack → Move → Vector Move VB Word Parts
Intrinsic     vmovw_c32_v40_4op[_p]
name
Spec syntax   vmovw {Qop [,u]} vc0, voz[0], ?vprX

Return type   vec40_t


              1
                                                              Coefficient operand (register vc0 is
                   IN1_VC0         coef_t
                                                              expected)
                                                              Coefficient operand (register vc1 is
              2    IN2_VC1         coef_t
                                                              expected)
                                                              Coefficient operand (register vc2 is
              3    IN3_VC2         coef_t
Operands                                                      expected)
                                                              Coefficient operand (register vc3 is
              4    IN4_VC3         coef_t
                                                              expected)
                                                              Offset for the first DW used from the
              5    OUT_OFST        uint8     0,4
                                                              result operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec40_t vRes;
              coef_t vcoefIn;
              coef_t vcoefIn2;
              coef_t vcoefIn3;
C example     coef_t vcoefIn4;
              vprex_t vecPred;
              ...
              vRes = vmovw_c32_v40_4op_p (vcoefIn, vcoefIn2, vcoefIn3, vcoefIn4, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmovw_c32_v40_4op_p version.


Main table → Move And Pack → Move → Vector Move VB Word Parts
Intrinsic     vmovw_c32_v40_4op_u[_p]
name
Spec syntax   vmovw {Qop [,u]} vc0, voz[0], ?vprX

Return type   vec40_t

                                                              Coefficient operand (register vc0 is
              1    IN1_VC0         coef_t

expected)
                                                              Coefficient operand (register vc1 is
              2    IN2_VC1         coef_t
                                                              expected)
Operands                                                      Coefficient operand (register vc2 is
              3    IN3_VC2         coef_t
                                                              expected)
                                                              Coefficient operand (register vc3 is
              4    IN4_VC3         coef_t
                                                              expected)
              5    OUT_OFST        uint8     0,4              Offset for the first DW used from the
                                                            result operand
            6    IN_VPR          vprex_t                    Vector predicate operand
            vec40_t vRes;
            coef_t vcoefIn;
            coef_t vcoefIn2;
            coef_t vcoefIn3;
C example   coef_t vcoefIn4;
            vprex_t vecPred;
            ...
            vRes = vmovw_c32_v40_4op_u_p (vcoefIn, vcoefIn2, vcoefIn3, vcoefIn4, 0, vecPred);

Comments    1.   IN_VPR last operand is relevant only for vmovw_c32_v40_4op_u_p version.


Main table → Move And Pack → Move → Vector Move VB Word Parts
Intrinsic     vmovw_v32_v40[_p]
name
Spec syntax   vmovw {Oop [,u_unch]} vx[0], voz[0], ?vprX

Return type   vec40_t

              1    OOP             uint8     1..8               Number of atomic operations
              2    IN1_V32         vec_t                        Input vector operand

              3    IN1_OFST        uint8     0,4
                                                                Offset for the first DW used from operand
Operands                                                        2

                                                                Offset for the first DW used from the
              4    OUT_OFST        uint8     0,4
                                                                result operand
              5    IN_VPR          vprex_t                      Vector predicate operand
              vec_t vIn;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmovw_v32_v40_p (8, vIn, 0, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmovw_v32_v40_p version.


Main table → Move And Pack → Move → Vector Move VB Word Parts

Intrinsic     vmovw_v32_v40_u[_p]
name
Spec syntax   vmovw {Oop [,u_unch]} vx[0], voz[0], ?vprX

Return type   vec40_t

              1    OOP             uint8     1..8               Number of atomic operations
              2    IN1_V32         vec_t                        Input vector operand

              3    IN1_OFST        uint8     0,4
                                                                Offset for the first DW used from operand
Operands                                                        2

                                                                Offset for the first DW used from the
              4    OUT_OFST        uint8     0,4
                                                                result operand
              5    IN_VPR          vprex_t                      Vector predicate operand
              vec_t vIn;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmovw_v32_v40_u_p (8, vIn, 0, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmovw_v32_v40_u_p version.


Main table → Move And Pack → Move → Vector Move VB Word Parts
Intrinsic     vmovw_v32_v40_unch[_p]
name
Spec syntax   vmovw {Oop [,u_unch]} vx[0], voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0,4
                                                             Offset for the first DW used from operand
Operands                                                     2

                                                             Offset for the first DW used from the
              4    OUT_OFST       uint8     0,4
                                                             result operand
              5    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmovw_v32_v40_unch_p (8, vIn, 0, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmovw_v32_v40_unch_p version.


Main table → Move And Pack → Move → Vector Move VB Word Parts
Intrinsic     vmovw_v32_vpr_c32_lzero
name
Spec syntax   vmovw {lzero} vx, VPREX, vcZp

Return type   coef_t

              1    IN1_V32        vec_t                     Input vector operand
Operands

2    IN2_VPR        vprex_t                   Vector predicate operand
              vec_t vIn;
              coef_t vcoefRes;
C example     vprex_t vecPredRes;
              ...
              vcoefRes = vmovw_v32_vpr_c32_lzero (vIn, vecPredRes);

Comments


Main table → Move And Pack → Move → Vector Move VB Word Parts
Intrinsic     vmovw_v32_v32[_p]
name
Spec syntax   vmovw {Oop} vx[0], viz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8               Number of atomic operations
              2    IN1_V32         vec_t                        Input vector operand

              3    IN1_OFST        uint8     0,4
                                                                Offset for the first DW used from operand
Operands                                                        2

                                                                Offset for the first DW used from the
              4    OUT_OFST        uint8     0,4
                                                                result operand
              5    IN_VPR          vprex_t                      Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmovw_v32_v32_p (8, vIn, 0, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmovw_v32_v32_p version.


Main table → Move And Pack → Move → Vector Move VB Word Parts
Intrinsic     vmovw_c32_v32_1op[_p]
name
Spec syntax   vmovw {Qop} vc0, viz[0], ?vprX

Return type   vec_t


              1
                                                             Coefficient operand (register vc0 is
                   IN1_VC0        coef_t
                                                             expected)
Operands                                                     Offset for the first DW used from the
              2    OUT_OFST       uint8     0,4
                                                             result operand
              3    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vmovw_c32_v32_1op_p (vcoefIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmovw_c32_v32_1op_p version.


Main table → Move And Pack → Move → Vector Move VB Word Parts
Intrinsic     vmovw_c32_v32_2op[_p]
name

Spec syntax   vmovw {Qop} vc0, viz[0], ?vprX

Return type   vec_t

                                                             Coefficient operand (register vc0 is
              1    IN1_VC0        coef_t
                                                             expected)
                                                             Coefficient operand (register vc1 is
              2    IN2_VC1        coef_t
Operands                                                     expected)
                                                             Offset for the first DW used from the
              3    OUT_OFST       uint8     0,4
                                                             result operand
              4    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vRes;
              coef_t vcoefIn;
              coef_t vcoefIn2;
C example     vprex_t vecPred;
              ...
              vRes = vmovw_c32_v32_2op_p (vcoefIn, vcoefIn2, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmovw_c32_v32_2op_p version.


Main table → Move And Pack → Move → Vector Move VB Word Parts
Intrinsic     vmovw_c32_v32_3op[_p]
name
Spec syntax   vmovw {Qop} vc0, viz[0], ?vprX
Return type   vec_t

                                                             Coefficient operand (register vc0 is
              1    IN1_VC0         coef_t
                                                             expected)

              2
                                                             Coefficient operand (register vc1 is
                   IN2_VC1         coef_t
                                                             expected)
Operands                                                     Coefficient operand (register vc2 is
              3    IN3_VC2         coef_t
                                                             expected)
                                                             Offset for the first DW used from the
              4    OUT_OFST        uint8     0,4
                                                             result operand
              5    IN_VPR          vprex_t                   Vector predicate operand
              vec_t vRes;
              coef_t vcoefIn;
              coef_t vcoefIn2;
C example     coef_t vcoefIn3;
              vprex_t vecPred;
              ...
              vRes = vmovw_c32_v32_3op_p (vcoefIn, vcoefIn2, vcoefIn3, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmovw_c32_v32_3op_p version.


Main table → Move And Pack → Move → Vector Move VB Word Parts
Intrinsic     vmovw_c32_v32_4op[_p]
name
Spec syntax   vmovw {Qop} vc0, viz[0], ?vprX

Return type   vec_t

                                                             Coefficient operand (register vc0 is
              1    IN1_VC0         coef_t
                                                             expected)
                                                             Coefficient operand (register vc1 is
              2    IN2_VC1         coef_t
                                                             expected)

              3
                                                             Coefficient operand (register vc2 is
                   IN3_VC2         coef_t
Operands                                                     expected)
                                                             Coefficient operand (register vc3 is
              4    IN4_VC3         coef_t
                                                             expected)
                                                             Offset for the first DW used from the
              5    OUT_OFST        uint8     0,4
                                                             result operand
              6    IN_VPR          vprex_t                   Vector predicate operand
              vec_t vRes;
              coef_t vcoefIn;
              coef_t vcoefIn2;
C example     coef_t vcoefIn3;
              coef_t vcoefIn4;
              vprex_t vecPred;
           ...
           vRes = vmovw_c32_v32_4op_p (vcoefIn, vcoefIn2, vcoefIn3, vcoefIn4, 0, vecPred);

Comments   1.   IN_VPR last operand is relevant only for vmovw_c32_v32_4op_p version.


Main table → Move And Pack → Move → Vector Move VB Word Parts
Intrinsic     vmovw_c32[_p]
name
Spec syntax   vmovw vcX, vcZ, ?vprX

Return type   coef_t

              1    IN1_C32        coef_t                   Coefficient operand
Operands
              2    IN_VPR         vprex_t                  Vector predicate operand
              coef_t vcoefIn;
              coef_t vcoefRes;
C example     vprex_t vecPred;
              ...
              vcoefRes = vmovw_c32_p (vcoefIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmovw_c32_p version.


Main table → Move And Pack → Move → Vector Move VB Word Parts
Intrinsic     vmovw_v32_vpr_c32_lone
name

Spec syntax   vmovw {lone} vx, VPREX, vcZp

Return type   coef_t

              1    IN1_V32        vec_t                    Input vector operand
Operands
              2    IN2_VPR        vprex_t                  Vector predicate operand
              vec_t vIn;
              coef_t vcoefRes;
C example     vprex_t vecPredRes;
              ...
              vcoefRes = vmovw_v32_vpr_c32_lone (vIn, vecPredRes);

Comments


Main table → Move And Pack → Move → Vector Move VB Word Parts
Intrinsic     vmovw_v32_c32_1op[_p]
name
Spec syntax   vmovw {Qop} vx[0], vc0, ?vprX

Return type   coef_t

              1    IN1_V32        vec_t                     Input vector operand

Operands      2    IN1_OFST       uint8     0,4
                                                            Offset for the first DW used from operand
                                                            1

              3    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              coef_t vcoefRes;
C example     vprex_t vecPred;
              ...
              vcoefRes = vmovw_v32_c32_1op_p (vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmovw_v32_c32_1op_p version.


Main table → Move And Pack → Move → Vector Move VB Word Parts
Intrinsic     vmovw_v32_c32_2op[_p]
name
Spec syntax   vmovw {Qop} vx[0], vc0, ?vprX

Return type   coef_t

              1    IN1_V32        vec_t                     Input vector operand

              2    IN1_OFST       uint8     0,4             Offset for the first DW used from operand
                                                            1
Operands
                                                            Coefficient result operand (register vc1 is
              3    RES2_VC1       coef_t
                                                            expected)
              4    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              coef_t vcoefRes1;
              coef_t vcoefRes2;
C example     vprex_t vecPred;
              ...
              vcoefRes1 = vmovw_v32_c32_2op_p (vIn, 0, vcoefRes2, vecPred);

              1.   IN_VPR last operand is relevant only for vmovw_v32_c32_2op_p version.

Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as

an additional parameter (RES2_VC1).


Main table → Move And Pack → Move → Vector Move VB Word Parts
Intrinsic     vmovw_v32_c32_3op[_p]
name
Spec syntax   vmovw {Qop} vx[0], vc0, ?vprX

Return type   coef_t

              1    IN1_V32        vec_t                      Input vector operand

              2    IN1_OFST       uint8     0,4
                                                             Offset for the first DW used from operand
                                                             1

                                                             Coefficient result operand (register vc1 is
Operands      3    RES2_VC1       coef_t
                                                             expected)
                                                             Coefficient result operand (register vc2 is
              4    RES3_VC2       coef_t
                                                             expected)
              5    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              coef_t vcoefRes1;
              coef_t vcoefRes2;
C example     coef_t vcoefRes3;
              vprex_t vecPred;
              ...
              vcoefRes1 = vmovw_v32_c32_3op_p (vIn, 0, vcoefRes2, vcoefRes3, vecPred);

              1.   IN_VPR last operand is relevant only for vmovw_v32_c32_3op_p version.

Comments           This intrinsic returns more than one result. The first result variable should be
              2.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.


Main table → Move And Pack → Move → Vector Move VB Word Parts
Intrinsic     vmovw_v32_c32_4op[_p]
name
Spec syntax   vmovw {Qop} vx[0], vc0, ?vprX

Return type   coef_t

              1    IN1_V32        vec_t                      Input vector operand

              2    IN1_OFST       uint8     0,4              Offset for the first DW used from operand
                                                             1

                                                             Coefficient result operand (register vc1 is
              3    RES2_VC1       coef_t
                                                             expected)
Operands
              4
                                                             Coefficient result operand (register vc2 is
                   RES3_VC2       coef_t
                                                             expected)

Coefficient result operand (register vc3 is
              5    RES4_VC3       coef_t
                                                             expected)
              6    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
C example     coef_t vcoefRes1;
              coef_t vcoefRes2;
           coef_t vcoefRes3;
           coef_t vcoefRes4;
           vprex_t vecPred;
           ...
           vcoefRes1 = vmovw_v32_c32_4op_p (vIn, 0, vcoefRes2, vcoefRes3, vcoefRes4, vecPred);

           1.   IN_VPR last operand is relevant only for vmovw_v32_c32_4op_p version.

Comments        This intrinsic returns more than one result. The first result variable should be
           2.   placed to the left of the = sign (lvalue). Additional result variables should be
                passed as parameters.


Main table → Move And Pack → Move → Vector Move VB Word Parts
Intrinsic     vmovw_c32_vuX[_p]
name
Spec syntax   vmovw {vuX} vcX, vcZ, ?vprX

Return type   coef_t

              1    VUX            uint8     0..3            Determines the source VCU
Operands      2    IN1_C32        coef_t                    Coefficient operand
              3    IN_VPR         vprex_t                   Vector predicate operand
              coef_t vcoefIn;
              coef_t vcoefRes;
C example     vprex_t vecPred;
              ...
              vcoefRes = vmovw_c32_vuX_p (1, vcoefIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmovw_c32_vuX_p version.


Main table → Move And Pack → Move → Vector Move VB Word Parts
