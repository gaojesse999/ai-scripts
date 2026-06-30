# Move And Pack → Fill → Vector Fill Words

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Move And Pack → Fill → Vector Fill Words

Vector Fill Words

Vector Fill Words
Fills destination with a constant value. Each source is 16-bit wide. The values are packed into
either 32-bit or 40-bit destination according to the register type.
Available Switches
         Number of atomic operations. An atomic operation is defined as a single fill operation.
Oop
         1op ≤ Oop ≤ 8op
         Number of atomic operations. An atomic operation is defined as a single fill operation.
Qop
         1op ≤ Qop ≤ 4op
u        When used, the rest of each destination which is written is zero-extended.
Intrinsic Names
vfillw_imm8_v40
vfillw_imm8_v40_u
vfillw_c32_v32
vfillw_c32_v40
vfillw_c32_v40_u
vfillw_imm8_c32_1op
vfillw_imm8_c32_2op
vfillw_imm8_c32_3op
vfillw_imm8_c32_4op
vfillw_imm8_3_v32
vfillw_c32_c32_1op
vfillw_c32_c32_2op
vfillw_c32_c32_3op
vfillw_c32_c32_4op
Instruction details in the instruction set specification
Intrinsic     vfillw_imm8_v40[_p]
name
Spec syntax   vfillw {Oop [,u]} #imm8, voz[0], ?vprX

Return type   vec40_t

              1    OOP             uint8     1..8           Number of atomic operations
Operands      2    IN1_IMM8        int16     -128..127      8 bit immediate
              3    IN_VPR          vprex_t                  Vector predicate operand
              vec40_t vRes;
              vprex_t vecPred;
C example     ...
              vRes = vfillw_imm8_v40_p (8, 2, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vfillw_imm8_v40_p version.


Main table → Move And Pack → Fill → Vector Fill Words
Intrinsic     vfillw_imm8_v40_u[_p]
name
Spec syntax   vfillw {Oop [,u]} #imm8, voz[0], ?vprX

Return type   vec40_t

              1    OOP             uint8     1..8           Number of atomic operations
Operands      2    IN1_IMM8        int16     -128..127      8 bit immediate
              3    IN_VPR          vprex_t                  Vector predicate operand
              vec40_t vRes;
              vprex_t vecPred;
C example     ...
              vRes = vfillw_imm8_v40_u_p (8, 2, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vfillw_imm8_v40_u_p version.


Main table → Move And Pack → Fill → Vector Fill Words
Intrinsic     vfillw_c32_v32[_p]
name
Spec syntax   vfillw {Oop} vcX, viz[0], ?vprX

Return type   vec_t

              1    OOP             uint8      1..8             Number of atomic operations

Operands      2    IN1_C32         coef_t                      Coefficient operand
              3    IN_VPR          vprex_t                     Vector predicate operand
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vfillw_c32_v32_p (8, vcoefIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vfillw_c32_v32_p version.


Main table → Move And Pack → Fill → Vector Fill Words
Intrinsic     vfillw_c32_v40[_p]
name
Spec syntax   vfillw {Oop [,u]} vcX, voz[0], ?vprX

Return type   vec40_t

              1    OOP             uint8      1..8               Number of atomic operations
Operands      2    IN1_C32         coef_t                        Coefficient operand
              3    IN_VPR          vprex_t                       Vector predicate operand
              vec40_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vfillw_c32_v40_p (8, vcoefIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vfillw_c32_v40_p version.


Main table → Move And Pack → Fill → Vector Fill Words
Intrinsic     vfillw_c32_v40_u[_p]
name
Spec syntax   vfillw {Oop [,u]} vcX, voz[0], ?vprX

Return type   vec40_t

              1    OOP             uint8      1..8               Number of atomic operations
Operands      2    IN1_C32         coef_t                        Coefficient operand
              3    IN_VPR          vprex_t                       Vector predicate operand
              vec40_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vfillw_c32_v40_u_p (8, vcoefIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vfillw_c32_v40_u_p version.


Main table → Move And Pack → Fill → Vector Fill Words
Intrinsic     vfillw_imm8_c32_1op[_p]
name
Spec syntax   vfillw {Qop} #imm8, vc0, ?vprX

Return type   coef_t

              1    IN1_IMM8       int16     -128..127          8 bit immediate
Operands
              2    IN_VPR         vprex_t                      Vector predicate operand
              coef_t vcoefRes;
              vprex_t vecPred;
C example     ...
              vcoefRes = vfillw_imm8_c32_1op_p (2, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vfillw_imm8_c32_1op_p version.


Main table → Move And Pack → Fill → Vector Fill Words
Intrinsic     vfillw_imm8_c32_2op[_p]
name

Spec syntax   vfillw {Qop} #imm8, vc0, ?vprX

Return type   coef_t

              1    IN1_IMM8       int16     -128..127          8 bit immediate
                                                               Coefficient result operand (register vc1 is
Operands      2    RES2_VC1       coef_t
                                                               expected)
              3    IN_VPR         vprex_t                      Vector predicate operand
              coef_t vcoefRes1;
              coef_t vcoefRes2;
C example     vprex_t vecPred;
              ...
              vcoefRes1 = vfillw_imm8_c32_2op_p (2, vcoefRes2, vecPred);

              1.   IN_VPR last operand is relevant only for vfillw_imm8_c32_2op_p version.

Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_VC1).


Main table → Move And Pack → Fill → Vector Fill Words
Intrinsic     vfillw_imm8_c32_3op[_p]
name
Spec syntax   vfillw {Qop} #imm8, vc0, ?vprX

Return type   coef_t

              1    IN1_IMM8       int16     -128..127          8 bit immediate
Operands
              2    RES2_VC1       coef_t                       Coefficient result operand (register vc1 is
                                                             expected)
                                                             Coefficient result operand (register vc2 is
              3    RES3_VC2       coef_t
                                                             expected)
              4    IN_VPR         vprex_t                    Vector predicate operand
              coef_t vcoefRes1;
              coef_t vcoefRes2;
              coef_t vcoefRes3;
C example     vprex_t vecPred;
              ...
              vcoefRes1 = vfillw_imm8_c32_3op_p (2, vcoefRes2, vcoefRes3, vecPred);

              1.   IN_VPR last operand is relevant only for vfillw_imm8_c32_3op_p version.

Comments           This intrinsic returns more than one result. The first result variable should be
              2.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.


Main table → Move And Pack → Fill → Vector Fill Words
Intrinsic     vfillw_imm8_c32_4op[_p]
name
Spec syntax   vfillw {Qop} #imm8, vc0, ?vprX

Return type   coef_t

1    IN1_IMM8       int16     -128..127        8 bit immediate
                                                             Coefficient result operand (register vc1 is
              2    RES2_VC1       coef_t
                                                             expected)
                                                             Coefficient result operand (register vc2 is
Operands      3    RES3_VC2       coef_t
                                                             expected)

              4
                                                             Coefficient result operand (register vc3 is
                   RES4_VC3       coef_t
                                                             expected)
              5    IN_VPR         vprex_t                    Vector predicate operand
              coef_t vcoefRes1;
              coef_t vcoefRes2;
              coef_t vcoefRes3;
C example     coef_t vcoefRes4;
              vprex_t vecPred;
              ...
              vcoefRes1 = vfillw_imm8_c32_4op_p (2, vcoefRes2, vcoefRes3, vcoefRes4, vecPred);

              1.   IN_VPR last operand is relevant only for vfillw_imm8_c32_4op_p version.

Comments           This intrinsic returns more than one result. The first result variable should be
              2.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.


Main table → Move And Pack → Fill → Vector Fill Words
Intrinsic     vfillw_imm8_3_v32[_p]
name
Spec syntax   vfillw {Oop} #imm8_3, viz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_IMM8_3     int16     -128..127       8 bit immediate
              3    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vRes;
              vprex_t vecPred;
C example     ...
              vRes = vfillw_imm8_3_v32_p (8, 2, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vfillw_imm8_3_v32_p version.


Main table → Move And Pack → Fill → Vector Fill Words
Intrinsic     vfillw_c32_c32_1op[_p]
name
Spec syntax   vfillw {Qop} vcX, vc0, ?vprX

Return type   coef_t

              1    IN1_C32         coef_t                     Coefficient operand
Operands
              2    IN_VPR          vprex_t                    Vector predicate operand
              coef_t vcoefIn;
              coef_t vcoefRes;
C example     vprex_t vecPred;

...
              vcoefRes = vfillw_c32_c32_1op_p (vcoefIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vfillw_c32_c32_1op_p version.


Main table → Move And Pack → Fill → Vector Fill Words
Intrinsic     vfillw_c32_c32_2op[_p]
name
Spec syntax   vfillw {Qop} vcX, vc0, ?vprX

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
              vcoefRes1 = vfillw_c32_c32_2op_p (vcoefIn, vcoefRes2, vecPred);

              1.   IN_VPR last operand is relevant only for vfillw_c32_c32_2op_p version.

Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_VC1).


Main table → Move And Pack → Fill → Vector Fill Words
Intrinsic     vfillw_c32_c32_3op[_p]
name
Spec syntax   vfillw {Qop} vcX, vc0, ?vprX

Return type   coef_t

Operands      1    IN1_C32         coef_t                     Coefficient operand
                                                              Coefficient result operand (register vc1 is
              2    RES2_VC1        coef_t
                                                              expected)
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
              vcoefRes1 = vfillw_c32_c32_3op_p (vcoefIn, vcoefRes2, vcoefRes3, vecPred);

              1.   IN_VPR last operand is relevant only for vfillw_c32_c32_3op_p version.

Comments           This intrinsic returns more than one result. The first result variable should be
              2.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.


Main table → Move And Pack → Fill → Vector Fill Words
Intrinsic     vfillw_c32_c32_4op[_p]
name
Spec syntax   vfillw {Qop} vcX, vc0, ?vprX

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
              vcoefRes1 = vfillw_c32_c32_4op_p (vcoefIn, vcoefRes2, vcoefRes3, vcoefRes4, vecPred);

              1.   IN_VPR last operand is relevant only for vfillw_c32_c32_4op_p version.

Comments           This intrinsic returns more than one result. The first result variable should be
              2.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.

Main table → Move And Pack → Fill → Vector Fill Words
