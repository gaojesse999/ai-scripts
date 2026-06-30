# Move And Pack → Fill → Vector Fill

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Move And Pack → Fill → Vector Fill

Vector Fill

Vector Fill
Fills destination with a constant value. Each source is either 8-bit or 32-bit wide. The destination
is either four bytes or 32-bit or 40-bit wide.
Available Switches
         Number of atomic operations. An atomic operation is defined as a single fill operation.
Oop
         1op ≤ Oop ≤ 8op
         Number of atomic operations. An atomic operation is defined as a single fill operation.
Qop
         1op ≤ Qop ≤ 4op
b        Each destination is filled by bytes.
dw       Each destination is filled by double-words.
u        When used, the rest of each destination which is written is zero-extended.
Intrinsic Names
vfill_imm8_v40_b
vfill_c32_v40_b
vfill_imm8_c32_1op_b
vfill_imm8_c32_1op_dw
vfill_imm8_c32_2op_b
vfill_imm8_c32_2op_dw
vfill_imm8_c32_3op_b
vfill_imm8_c32_3op_dw
vfill_imm8_c32_4op_b
vfill_imm8_c32_4op_dw
vfill_c32_v40_dw
vfill_c32_v40_dw_u
vfill_imm8_3_v32_b
vfill_imm8_3_v32_dw
vfill_imm8_v40_dw
vfill_imm8_v40_dw_u
vfill_c32_v32_b
vfill_c32_v32_dw
vfill_c32_c32_1op_b
vfill_c32_c32_1op_dw
vfill_c32_c32_2op_b
vfill_c32_c32_2op_dw
vfill_c32_c32_3op_b
vfill_c32_c32_3op_dw
vfill_c32_c32_4op_b
vfill_c32_c32_4op_dw
Instruction details in the instruction set specification
Intrinsic     vfill_imm8_v40_b[_p]
name
Spec syntax   vfill {Oop, b} #imm8, voz[0], ?vprX

Return type   vec40_t

              1    OOP             uint8     1..8          Number of atomic operations
Operands      2    IN1_IMM8        int16     -128..127     8 bit immediate
              3    IN_VPR          vprex_t                 Vector predicate operand
              vec40_t vRes;
              vprex_t vecPred;
C example     ...
              vRes = vfill_imm8_v40_b_p (8, 2, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vfill_imm8_v40_b_p version.


Main table → Move And Pack → Fill → Vector Fill
Intrinsic     vfill_c32_v40_b[_p]
name

Spec syntax   vfill {Oop, b} vcX, voz[0], ?vprX

Return type   vec40_t

              1    OOP              uint8     1..8              Number of atomic operations
Operands      2    IN1_C32          coef_t                      Coefficient operand
              3    IN_VPR           vprex_t                     Vector predicate operand
              vec40_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vfill_c32_v40_b_p (8, vcoefIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vfill_c32_v40_b_p version.


Main table → Move And Pack → Fill → Vector Fill
Intrinsic     vfill_imm8_c32_1op_b[_p]
name
Spec syntax   vfill {Qop, b_dw} #imm8, vc0, ?vprX

Return type   coef_t

              1    IN1_IMM8       int16     -128..127           8 bit immediate
Operands
              2    IN_VPR         vprex_t                       Vector predicate operand
              coef_t vcoefRes;
              vprex_t vecPred;
C example     ...
              vcoefRes = vfill_imm8_c32_1op_b_p (2, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vfill_imm8_c32_1op_b_p version.


Main table → Move And Pack → Fill → Vector Fill
Intrinsic     vfill_imm8_c32_1op_dw[_p]
name
Spec syntax   vfill {Qop, b_dw} #imm8, vc0, ?vprX

Return type   coef_t

              1    IN1_IMM8       int16     -128..127           8 bit immediate
Operands
              2    IN_VPR         vprex_t                       Vector predicate operand
              coef_t vcoefRes;
              vprex_t vecPred;
C example     ...
              vcoefRes = vfill_imm8_c32_1op_dw_p (2, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vfill_imm8_c32_1op_dw_p version.


Main table → Move And Pack → Fill → Vector Fill
Intrinsic     vfill_imm8_c32_2op_b[_p]
name
Spec syntax   vfill {Qop, b_dw} #imm8, vc0, ?vprX

Return type   coef_t

              1    IN1_IMM8       int16     -128..127           8 bit immediate
                                                                Coefficient result operand (register vc1 is
Operands      2    RES2_VC1       coef_t
                                                                expected)
              3    IN_VPR         vprex_t                       Vector predicate operand
              coef_t vcoefRes1;
              coef_t vcoefRes2;
C example     vprex_t vecPred;
              ...

vcoefRes1 = vfill_imm8_c32_2op_b_p (2, vcoefRes2, vecPred);
              1.   IN_VPR last operand is relevant only for vfill_imm8_c32_2op_b_p version.

Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_VC1).


Main table → Move And Pack → Fill → Vector Fill
Intrinsic     vfill_imm8_c32_2op_dw[_p]
name
Spec syntax   vfill {Qop, b_dw} #imm8, vc0, ?vprX

Return type   coef_t

              1    IN1_IMM8       int16     -128..127       8 bit immediate
                                                            Coefficient result operand (register vc1 is
Operands      2    RES2_VC1       coef_t
                                                            expected)
              3    IN_VPR         vprex_t                   Vector predicate operand
              coef_t vcoefRes1;
              coef_t vcoefRes2;
C example     vprex_t vecPred;
              ...
              vcoefRes1 = vfill_imm8_c32_2op_dw_p (2, vcoefRes2, vecPred);

              1.   IN_VPR last operand is relevant only for vfill_imm8_c32_2op_dw_p version.

Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_VC1).


Main table → Move And Pack → Fill → Vector Fill
Intrinsic     vfill_imm8_c32_3op_b[_p]
name
Spec syntax   vfill {Qop, b_dw} #imm8, vc0, ?vprX

Return type   coef_t

              1    IN1_IMM8       int16     -128..127       8 bit immediate
                                                            Coefficient result operand (register vc1 is
              2    RES2_VC1       coef_t
                                                            expected)
Operands
                                                            Coefficient result operand (register vc2 is
              3    RES3_VC2       coef_t
                                                            expected)
              4    IN_VPR         vprex_t                   Vector predicate operand
              coef_t vcoefRes1;
              coef_t vcoefRes2;
C example     coef_t vcoefRes3;
              vprex_t vecPred;
              ...
              vcoefRes1 = vfill_imm8_c32_3op_b_p (2, vcoefRes2, vcoefRes3, vecPred);

1.   IN_VPR last operand is relevant only for vfill_imm8_c32_3op_b_p version.

Comments           This intrinsic returns more than one result. The first result variable should be
              2.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.


Main table → Move And Pack → Fill → Vector Fill
Intrinsic     vfill_imm8_c32_3op_dw[_p]
name
Spec syntax   vfill {Qop, b_dw} #imm8, vc0, ?vprX

Return type   coef_t

              1    IN1_IMM8       int16     -128..127        8 bit immediate
                                                             Coefficient result operand (register vc1 is
              2    RES2_VC1       coef_t
                                                             expected)
Operands
                                                             Coefficient result operand (register vc2 is
              3    RES3_VC2       coef_t
                                                             expected)
              4    IN_VPR         vprex_t                    Vector predicate operand
              coef_t vcoefRes1;
              coef_t vcoefRes2;
              coef_t vcoefRes3;
C example     vprex_t vecPred;
              ...
              vcoefRes1 = vfill_imm8_c32_3op_dw_p (2, vcoefRes2, vcoefRes3, vecPred);

              1.   IN_VPR last operand is relevant only for vfill_imm8_c32_3op_dw_p version.

Comments           This intrinsic returns more than one result. The first result variable should be
              2.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.


Main table → Move And Pack → Fill → Vector Fill
Intrinsic     vfill_imm8_c32_4op_b[_p]
name
Spec syntax   vfill {Qop, b_dw} #imm8, vc0, ?vprX

Return type   coef_t

              1    IN1_IMM8       int16     -128..127        8 bit immediate
                                                             Coefficient result operand (register vc1 is
              2    RES2_VC1       coef_t
Operands                                                     expected)
                                                             Coefficient result operand (register vc2 is
              3    RES3_VC2       coef_t
                                                             expected)
                                                             Coefficient result operand (register vc3 is
              4    RES4_VC3       coef_t

expected)
              5    IN_VPR         vprex_t                    Vector predicate operand
              coef_t vcoefRes1;
              coef_t vcoefRes2;
              coef_t vcoefRes3;
C example     coef_t vcoefRes4;
              vprex_t vecPred;
              ...
              vcoefRes1 = vfill_imm8_c32_4op_b_p (2, vcoefRes2, vcoefRes3, vcoefRes4, vecPred);

              1.   IN_VPR last operand is relevant only for vfill_imm8_c32_4op_b_p version.

Comments           This intrinsic returns more than one result. The first result variable should be
              2.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.


Main table → Move And Pack → Fill → Vector Fill
Intrinsic     vfill_imm8_c32_4op_dw[_p]
name
Spec syntax   vfill {Qop, b_dw} #imm8, vc0, ?vprX

Return type   coef_t

              1    IN1_IMM8       int16     -128..127        8 bit immediate
                                                             Coefficient result operand (register vc1 is
              2    RES2_VC1       coef_t
                                                             expected)
                                                             Coefficient result operand (register vc2 is
Operands      3    RES3_VC2       coef_t
                                                             expected)
                                                             Coefficient result operand (register vc3 is
              4    RES4_VC3       coef_t
                                                             expected)
              5    IN_VPR         vprex_t                    Vector predicate operand
              coef_t vcoefRes1;
              coef_t vcoefRes2;
              coef_t vcoefRes3;
C example     coef_t vcoefRes4;
              vprex_t vecPred;
              ...
              vcoefRes1 = vfill_imm8_c32_4op_dw_p (2, vcoefRes2, vcoefRes3, vcoefRes4, vecPred);

              1.   IN_VPR last operand is relevant only for vfill_imm8_c32_4op_dw_p version.

Comments           This intrinsic returns more than one result. The first result variable should be
              2.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.


Main table → Move And Pack → Fill → Vector Fill
Intrinsic     vfill_c32_v40_dw[_p]
name
Spec syntax   vfill {Oop, dw [,u]} vcX, voz[0], ?vprX

Return type   vec40_t

1    OOP             uint8     1..8                Number of atomic operations
Operands      2    IN1_C32         coef_t                        Coefficient operand
              3    IN_VPR          vprex_t                       Vector predicate operand
              vec40_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vfill_c32_v40_dw_p (8, vcoefIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vfill_c32_v40_dw_p version.


Main table → Move And Pack → Fill → Vector Fill
Intrinsic     vfill_c32_v40_dw_u[_p]
name
Spec syntax   vfill {Oop, dw [,u]} vcX, voz[0], ?vprX

Return type   vec40_t

              1    OOP             uint8     1..8                Number of atomic operations
Operands      2    IN1_C32         coef_t                        Coefficient operand
              3    IN_VPR          vprex_t                       Vector predicate operand
              vec40_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vfill_c32_v40_dw_u_p (8, vcoefIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vfill_c32_v40_dw_u_p version.


Main table → Move And Pack → Fill → Vector Fill
Intrinsic     vfill_imm8_3_v32_b[_p]
name
Spec syntax   vfill {Oop, b_dw} #imm8_3, viz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8             Number of atomic operations
Operands      2    IN1_IMM8_3      int16     -128..127        8 bit immediate
              3    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vRes;
              vprex_t vecPred;
C example     ...
              vRes = vfill_imm8_3_v32_b_p (8, 2, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vfill_imm8_3_v32_b_p version.


Main table → Move And Pack → Fill → Vector Fill
Intrinsic     vfill_imm8_3_v32_dw[_p]
name
Spec syntax   vfill {Oop, b_dw} #imm8_3, viz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8             Number of atomic operations
Operands      2    IN1_IMM8_3      int16     -128..127        8 bit immediate
              3    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vRes;
              vprex_t vecPred;
C example     ...
              vRes = vfill_imm8_3_v32_dw_p (8, 2, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vfill_imm8_3_v32_dw_p version.


Main table → Move And Pack → Fill → Vector Fill
Intrinsic     vfill_imm8_v40_dw[_p]
name
Spec syntax   vfill {Oop, dw [,u]} #imm8, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8              Number of atomic operations
Operands      2    IN1_IMM8       int16     -128..127         8 bit immediate
              3    IN_VPR         vprex_t                     Vector predicate operand
              vec40_t vRes;
              vprex_t vecPred;
C example     ...
              vRes = vfill_imm8_v40_dw_p (8, 2, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vfill_imm8_v40_dw_p version.


Main table → Move And Pack → Fill → Vector Fill
Intrinsic     vfill_imm8_v40_dw_u[_p]
name
Spec syntax   vfill {Oop, dw [,u]} #imm8, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8              Number of atomic operations
Operands      2    IN1_IMM8       int16     -128..127         8 bit immediate
              3    IN_VPR         vprex_t                     Vector predicate operand
              vec40_t vRes;
              vprex_t vecPred;
C example     ...
              vRes = vfill_imm8_v40_dw_u_p (8, 2, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vfill_imm8_v40_dw_u_p version.


Main table → Move And Pack → Fill → Vector Fill
Intrinsic     vfill_c32_v32_b[_p]
name
Spec syntax   vfill {Oop, b_dw} vcX, viz[0], ?vprX

Return type   vec_t

              1    OOP              uint8     1..8               Number of atomic operations
Operands      2    IN1_C32          coef_t                       Coefficient operand
              3    IN_VPR           vprex_t                      Vector predicate operand
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vfill_c32_v32_b_p (8, vcoefIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vfill_c32_v32_b_p version.


Main table → Move And Pack → Fill → Vector Fill
Intrinsic     vfill_c32_v32_dw[_p]
name
Spec syntax   vfill {Oop, b_dw} vcX, viz[0], ?vprX

Return type   vec_t

              1    OOP              uint8     1..8               Number of atomic operations
Operands      2    IN1_C32          coef_t                       Coefficient operand

3    IN_VPR           vprex_t                      Vector predicate operand
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vfill_c32_v32_dw_p (8, vcoefIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vfill_c32_v32_dw_p version.


Main table → Move And Pack → Fill → Vector Fill
Intrinsic     vfill_c32_c32_1op_b[_p]
name
Spec syntax   vfill {Qop, b_dw} vcX, vc0, ?vprX

Return type   coef_t

              1    IN1_C32         coef_t                     Coefficient operand
Operands
              2    IN_VPR          vprex_t                    Vector predicate operand
              coef_t vcoefIn;
              coef_t vcoefRes;
C example     vprex_t vecPred;
              ...
              vcoefRes = vfill_c32_c32_1op_b_p (vcoefIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vfill_c32_c32_1op_b_p version.


Main table → Move And Pack → Fill → Vector Fill
Intrinsic     vfill_c32_c32_1op_dw[_p]
name
Spec syntax   vfill {Qop, b_dw} vcX, vc0, ?vprX

Return type   coef_t

              1    IN1_C32         coef_t                     Coefficient operand
Operands
              2    IN_VPR          vprex_t                    Vector predicate operand
              coef_t vcoefIn;
              coef_t vcoefRes;
C example     vprex_t vecPred;
              ...
              vcoefRes = vfill_c32_c32_1op_dw_p (vcoefIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vfill_c32_c32_1op_dw_p version.


Main table → Move And Pack → Fill → Vector Fill
Intrinsic     vfill_c32_c32_2op_b[_p]
name
Spec syntax   vfill {Qop, b_dw} vcX, vc0, ?vprX

Return type   coef_t

              1    IN1_C32         coef_t                     Coefficient operand
                                                              Coefficient result operand (register vc1 is
Operands      2    RES2_VC1        coef_t
                                                              expected)
              3    IN_VPR          vprex_t                    Vector predicate operand
              coef_t vcoefIn;
C example     coef_t vcoefRes1;
              coef_t vcoefRes2;
              vprex_t vecPred;
              ...
              vcoefRes1 = vfill_c32_c32_2op_b_p (vcoefIn, vcoefRes2, vecPred);

              1.   IN_VPR last operand is relevant only for vfill_c32_c32_2op_b_p version.

Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_VC1).


Main table → Move And Pack → Fill → Vector Fill
Intrinsic     vfill_c32_c32_2op_dw[_p]
name
Spec syntax   vfill {Qop, b_dw} vcX, vc0, ?vprX

Return type   coef_t

              1    IN1_C32         coef_t                     Coefficient operand
                                                              Coefficient result operand (register vc1 is
Operands      2    RES2_VC1        coef_t
                                                              expected)
              3    IN_VPR          vprex_t                    Vector predicate operand
              coef_t vcoefIn;
              coef_t vcoefRes1;
              coef_t vcoefRes2;
C example     vprex_t vecPred;
              ...
              vcoefRes1 = vfill_c32_c32_2op_dw_p (vcoefIn, vcoefRes2, vecPred);

              1.   IN_VPR last operand is relevant only for vfill_c32_c32_2op_dw_p version.

Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_VC1).


Main table → Move And Pack → Fill → Vector Fill
Intrinsic     vfill_c32_c32_3op_b[_p]
name
Spec syntax   vfill {Qop, b_dw} vcX, vc0, ?vprX

Return type   coef_t

              1    IN1_C32         coef_t                     Coefficient operand
                                                              Coefficient result operand (register vc1 is
              2    RES2_VC1        coef_t
                                                              expected)
Operands
                                                              Coefficient result operand (register vc2 is
              3    RES3_VC2        coef_t
                                                              expected)
              4    IN_VPR          vprex_t                    Vector predicate operand
              coef_t vcoefIn;
              coef_t vcoefRes1;
              coef_t vcoefRes2;
C example     coef_t vcoefRes3;
              vprex_t vecPred;
              ...
              vcoefRes1 = vfill_c32_c32_3op_b_p (vcoefIn, vcoefRes2, vcoefRes3, vecPred);

1.   IN_VPR last operand is relevant only for vfill_c32_c32_3op_b_p version.

Comments           This intrinsic returns more than one result. The first result variable should be
              2.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.


Main table → Move And Pack → Fill → Vector Fill
Intrinsic     vfill_c32_c32_3op_dw[_p]
name
Spec syntax   vfill {Qop, b_dw} vcX, vc0, ?vprX

Return type   coef_t

              1    IN1_C32         coef_t                     Coefficient operand
                                                              Coefficient result operand (register vc1 is
              2    RES2_VC1        coef_t
                                                              expected)
Operands
                                                              Coefficient result operand (register vc2 is
              3    RES3_VC2        coef_t
                                                              expected)
              4    IN_VPR          vprex_t                    Vector predicate operand
              coef_t vcoefIn;
              coef_t vcoefRes1;
              coef_t vcoefRes2;
C example     coef_t vcoefRes3;
              vprex_t vecPred;
              ...
              vcoefRes1 = vfill_c32_c32_3op_dw_p (vcoefIn, vcoefRes2, vcoefRes3, vecPred);

              1.   IN_VPR last operand is relevant only for vfill_c32_c32_3op_dw_p version.

Comments           This intrinsic returns more than one result. The first result variable should be
              2.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.


Main table → Move And Pack → Fill → Vector Fill
Intrinsic     vfill_c32_c32_4op_b[_p]
name
Spec syntax   vfill {Qop, b_dw} vcX, vc0, ?vprX

Return type   coef_t

Operands      1    IN1_C32         coef_t                     Coefficient operand
                                                              Coefficient result operand (register vc1 is
              2    RES2_VC1        coef_t
                                                              expected)
                                                              Coefficient result operand (register vc2 is
              3    RES3_VC2        coef_t
                                                              expected)

              4

Coefficient result operand (register vc3 is
                   RES4_VC3        coef_t
                                                              expected)
              5    IN_VPR          vprex_t                    Vector predicate operand
              coef_t vcoefIn;
              coef_t vcoefRes1;
              coef_t vcoefRes2;
              coef_t vcoefRes3;
C example     coef_t vcoefRes4;
              vprex_t vecPred;
              ...
              vcoefRes1 = vfill_c32_c32_4op_b_p (vcoefIn, vcoefRes2, vcoefRes3, vcoefRes4, vecPred);

              1.   IN_VPR last operand is relevant only for vfill_c32_c32_4op_b_p version.

Comments           This intrinsic returns more than one result. The first result variable should be
              2.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.


Main table → Move And Pack → Fill → Vector Fill
Intrinsic     vfill_c32_c32_4op_dw[_p]
name
Spec syntax   vfill {Qop, b_dw} vcX, vc0, ?vprX

Return type   coef_t

              1    IN1_C32         coef_t                     Coefficient operand
                                                              Coefficient result operand (register vc1 is
              2    RES2_VC1        coef_t
                                                              expected)
                                                              Coefficient result operand (register vc2 is
Operands      3    RES3_VC2        coef_t
                                                              expected)
                                                              Coefficient result operand (register vc3 is
              4    RES4_VC3        coef_t
                                                              expected)
              5    IN_VPR          vprex_t                    Vector predicate operand
              coef_t vcoefIn;
              coef_t vcoefRes1;
              coef_t vcoefRes2;
              coef_t vcoefRes3;
C example     coef_t vcoefRes4;
              vprex_t vecPred;
              ...
              vcoefRes1 = vfill_c32_c32_4op_dw_p (vcoefIn, vcoefRes2, vcoefRes3, vcoefRes4, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vfill_c32_c32_4op_dw_p version.
                 This intrinsic returns more than one result. The first result variable should be
            2.   placed to the left of the = sign (lvalue). Additional result variables should be

passed as parameters.


Main table → Move And Pack → Fill → Vector Fill
