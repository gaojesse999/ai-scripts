# Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU

Move Vector Data to GCU

Move Vector Data to GCU
Performs data move from source to destination. The source is 40-bit wide. The destination is a
GCU 40-bit accumulator.
Available Switches
None
Intrinsic Names
movv_c32_a4_1op_vuX
movv_c32_a4_1op_vuX_u
movv_c32_a4_2op_vuX
movv_c32_a4_2op_vuX_u
movv_c32_a4_3op_vuX
movv_c32_a4_3op_vuX_u
movv_c32_a4_4op_vuX
movv_c32_a4_4op_vuX_u
movv_v40_a0_1op_vuX
movv_v40_a0_2op_vuX
movv_v40_a0_3op_vuX
movv_v40_a0_4op_vuX
movv_v40_a0_5op_vuX
movv_v40_a0_6op_vuX
movv_v40_a0_7op_vuX
movv_v40_a0_8op_vuX
movv_c32_a0_1op_vuX
movv_c32_a0_1op_vuX_u
movv_c32_a0_2op_vuX
movv_c32_a0_2op_vuX_u
movv_c32_a0_3op_vuX
movv_c32_a0_3op_vuX_u
movv_c32_a0_4op_vuX
movv_c32_a0_4op_vuX_u
movv_c32_a20_1op_vuX
movv_c32_a20_1op_vuX_u
movv_c32_a20_2op_vuX
movv_c32_a20_2op_vuX_u
movv_c32_a20_3op_vuX
movv_c32_a20_3op_vuX_u
movv_c32_a20_4op_vuX
movv_c32_a20_4op_vuX_u
movv_v40_a16_1op_vuX
movv_v40_a16_2op_vuX
movv_v40_a16_3op_vuX
movv_v40_a16_4op_vuX
movv_v40_a16_5op_vuX
movv_v40_a16_6op_vuX
movv_v40_a16_7op_vuX
movv_v40_a16_8op_vuX
movv_c32_a16_1op_vuX
movv_c32_a16_1op_vuX_u

movv_c32_a16_2op_vuX
movv_c32_a16_2op_vuX_u
movv_c32_a16_3op_vuX
movv_c32_a16_3op_vuX_u
movv_c32_a16_4op_vuX
movv_c32_a16_4op_vuX_u
movv_modv0_a8
movv_modv2_a8
movv_c32_acc_vuX
movv_c32_acc_vuX_u
movv_v40_a8_1op_vuX
movv_v40_a8_2op_vuX
movv_v40_a8_3op_vuX
movv_v40_a8_4op_vuX
movv_v40_a8_5op_vuX
movv_v40_a8_6op_vuX
movv_v40_a8_7op_vuX
movv_v40_a8_8op_vuX
movv_c32_a12_1op_vuX
movv_c32_a12_1op_vuX_u
movv_c32_a12_2op_vuX
movv_c32_a12_2op_vuX_u
movv_c32_a12_3op_vuX
movv_c32_a12_3op_vuX_u
movv_c32_a12_4op_vuX
movv_c32_a12_4op_vuX_u
movv_modv0_a0
movv_modv2_a0
movv_c32_a8_1op_vuX
movv_c32_a8_1op_vuX_u
movv_c32_a8_2op_vuX
movv_c32_a8_2op_vuX_u
movv_c32_a8_3op_vuX
movv_c32_a8_3op_vuX_u
movv_c32_a8_4op_vuX
movv_c32_a8_4op_vuX_u
Instruction details in the instruction set specification
Intrinsic     movv_c32_a4_1op_vuX
name
Spec syntax   movv {Qop, vuX [,u]} vc0, a4

Return type   int

              1     VUX           uint8      0..3            Determines the source VCU
Operands                                                     Coefficient operand (register vc0 is
              2     IN1_VC0       coef_t
                                                             expected)
              int accRes;
              coef_t vcoefIn;
C example     ...
              accRes = movv_c32_a4_1op_vuX (1, vcoefIn);

Comments


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_c32_a4_1op_vuX_u
name
Spec syntax   movv {Qop, vuX [,u]} vc0, a4

Return type   int

              1     VUX           uint8      0..3            Determines the source VCU
Operands                                                     Coefficient operand (register vc0 is
              2     IN1_VC0       coef_t
                                                             expected)
              int accRes;
              coef_t vcoefIn;
C example     ...
              accRes = movv_c32_a4_1op_vuX_u (1, vcoefIn);

Comments


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_c32_a4_2op_vuX
name
Spec syntax   movv {Qop, vuX [,u]} vc0, a4

Return type   int

              1     VUX           uint8      0..3            Determines the source VCU
                                                             Coefficient operand (register vc0 is
              2     IN1_VC0       coef_t
                                                             expected)
Operands

Coefficient operand (register vc1 is
              3     IN2_VC1       coef_t
                                                             expected)
              4     RES2_A5       int32                      Accumulator result operand (register a5 is
                                                             expected)
              int accRes1;
              int accRes2;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              ...
              accRes1 = movv_c32_a4_2op_vuX (1, vcoefIn, vcoefIn2, accRes2);

                    This intrinsic returns two results. The first result variable should be placed to
Comments      1.    the left of the = sign (lvalue). The second result variable should be passed as
                    an additional parameter (RES2_A5).


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_c32_a4_2op_vuX_u
name
Spec syntax   movv {Qop, vuX [,u]} vc0, a4

Return type   int

              1     VUX           uint8      0..3            Determines the source VCU
                                                             Coefficient operand (register vc0 is
              2     IN1_VC0       coef_t
                                                             expected)
Operands                                                     Coefficient operand (register vc1 is
              3     IN2_VC1       coef_t
                                                             expected)
                                                             Accumulator result operand (register a5 is
              4     RES2_A5       int32
                                                             expected)
              int accRes1;
              int accRes2;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              ...
              accRes1 = movv_c32_a4_2op_vuX_u (1, vcoefIn, vcoefIn2, accRes2);

                    This intrinsic returns two results. The first result variable should be placed to
Comments      1.    the left of the = sign (lvalue). The second result variable should be passed as
                    an additional parameter (RES2_A5).


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_c32_a4_3op_vuX
name
Spec syntax   movv {Qop, vuX [,u]} vc0, a4

Return type   int

              1     VUX           uint8      0..3            Determines the source VCU

Operands                                                     Coefficient operand (register vc0 is
              2     IN1_VC0       coef_t
                                                             expected)
                                                             Coefficient operand (register vc1 is
              3     IN2_VC1        coef_t
                                                             expected)
                                                             Coefficient operand (register vc2 is
              4     IN3_VC2        coef_t
                                                             expected)

              5
                                                             Accumulator result operand (register a5 is
                    RES2_A5        int32
                                                             expected)
                                                             Accumulator result operand (register a6 is
              6     RES3_A6        int32
                                                             expected)
              int accRes1;
              int accRes2;
              int accRes3;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              coef_t vcoefIn3;
              ...
              accRes1 = movv_c32_a4_3op_vuX (1, vcoefIn, vcoefIn2, vcoefIn3, accRes2, accRes3);

                    This intrinsic returns more than one result. The first result variable should be
Comments      1.    placed to the left of the = sign (lvalue). Additional result variables should be
                    passed as parameters.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_c32_a4_3op_vuX_u
name
Spec syntax   movv {Qop, vuX [,u]} vc0, a4

Return type   int

              1     VUX            uint8     0..3            Determines the source VCU
                                                             Coefficient operand (register vc0 is
              2     IN1_VC0        coef_t
                                                             expected)
                                                             Coefficient operand (register vc1 is
              3     IN2_VC1        coef_t
                                                             expected)
Operands                                                     Coefficient operand (register vc2 is
              4     IN3_VC2        coef_t

expected)
                                                             Accumulator result operand (register a5 is
              5     RES2_A5        int32
                                                             expected)

              6
                                                             Accumulator result operand (register a6 is
                    RES3_A6        int32
                                                             expected)
              int accRes1;
              int accRes2;
              int accRes3;
C example     coef_t vcoefIn;
              coef_t vcoefIn2;
              coef_t vcoefIn3;
              ...
              accRes1 = movv_c32_a4_3op_vuX_u (1, vcoefIn, vcoefIn2, vcoefIn3, accRes2, accRes3);

                    This intrinsic returns more than one result. The first result variable should be
Comments      1.    placed to the left of the = sign (lvalue). Additional result variables should be
                    passed as parameters.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_c32_a4_4op_vuX
name
Spec syntax   movv {Qop, vuX [,u]} vc0, a4

Return type   int

              1     VUX            uint8     0..3             Determines the source VCU
                                                              Coefficient operand (register vc0 is
              2     IN1_VC0        coef_t
                                                              expected)
                                                              Coefficient operand (register vc1 is
              3     IN2_VC1        coef_t
                                                              expected)
                                                              Coefficient operand (register vc2 is
              4     IN3_VC2        coef_t
                                                              expected)
Operands                                                      Coefficient operand (register vc3 is
              5     IN4_VC3        coef_t
                                                              expected)
                                                              Accumulator result operand (register a5 is
              6     RES2_A5        int32
                                                              expected)
                                                              Accumulator result operand (register a6 is
              7     RES3_A6        int32

expected)

              8
                                                              Accumulator result operand (register a7 is
                    RES4_A7        int32
                                                              expected)
              int accRes1;
              int accRes2;
              int accRes3;
              int accRes4;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              coef_t vcoefIn3;
              coef_t vcoefIn4;
              ...
              accRes1 = movv_c32_a4_4op_vuX (1, vcoefIn, vcoefIn2, vcoefIn3, vcoefIn4, accRes2, accRes3, accRes4);

                    This intrinsic returns more than one result. The first result variable should be
Comments      1.    placed to the left of the = sign (lvalue). Additional result variables should be
                    passed as parameters.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_c32_a4_4op_vuX_u
name
Spec syntax   movv {Qop, vuX [,u]} vc0, a4

Return type   int

              1     VUX            uint8     0..3            Determines the source VCU
                                                             Coefficient operand (register vc0 is
              2     IN1_VC0        coef_t
                                                             expected)
                                                             Coefficient operand (register vc1 is
              3     IN2_VC1        coef_t
                                                             expected)
                                                             Coefficient operand (register vc2 is
              4     IN3_VC2        coef_t
                                                             expected)
Operands                                                     Coefficient operand (register vc3 is
              5     IN4_VC3        coef_t
                                                             expected)
                                                             Accumulator result operand (register a5 is
              6     RES2_A5        int32
                                                             expected)
                                                             Accumulator result operand (register a6 is
              7     RES3_A6        int32
                                                             expected)

Accumulator result operand (register a7 is
              8     RES4_A7        int32
                                                             expected)
              int accRes1;
              int accRes2;
              int accRes3;
              int accRes4;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              coef_t vcoefIn3;
              coef_t vcoefIn4;
              ...
              accRes1 = movv_c32_a4_4op_vuX_u (1, vcoefIn, vcoefIn2, vcoefIn3, vcoefIn4, accRes2, accRes3,
              accRes4);

                    This intrinsic returns more than one result. The first result variable should be
Comments      1.    placed to the left of the = sign (lvalue). Additional result variables should be
                    passed as parameters.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_v40_a0_1op_vuX
name
Spec syntax   movv {Oop, vuX} vox[0], a0

Return type   acc_t

              1    VUX            uint8     0..3            Determines the source VCU
Operands
              2    IN1_V40        vec40_t                   Output vector operand
              acc_t accRes;
              vec40_t vIn;
C example     ...
              accRes = movv_v40_a0_1op_vuX (1, vIn);

Comments


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_v40_a0_2op_vuX
name
Spec syntax   movv {Oop, vuX} vox[0], a0

Return type   acc_t

              1    VUX            uint8     0..3            Determines the source VCU
              2    IN1_V40        vec40_t                   Output vector operand
Operands
                                                            Accumulator result operand (register a1 is
              3    RES2_A1        acc_t
                                                            expected)
              acc_t accRes1;
              acc_t accRes2;
C example     vec40_t vIn;
              ...
              accRes1 = movv_v40_a0_2op_vuX (1, vIn, accRes2);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_A1).


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_v40_a0_3op_vuX
name
Spec syntax   movv {Oop, vuX} vox[0], a0

Return type   acc_t

1    VUX            uint8     0..3            Determines the source VCU
Operands      2    IN1_V40        vec40_t                   Output vector operand
              3    RES2_A1        acc_t                     Accumulator result operand (register a1 is
                                                            expected)
                                                            Accumulator result operand (register a2 is
              4    RES3_A2        acc_t
                                                            expected)
              acc_t accRes1;
              acc_t accRes2;
              acc_t accRes3;
C example     vec40_t vIn;
              ...
              accRes1 = movv_v40_a0_3op_vuX (1, vIn, accRes2, accRes3);

                   This intrinsic returns more than one result. The first result variable should be
Comments      1.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_v40_a0_4op_vuX
name
Spec syntax   movv {Oop, vuX} vox[0], a0

Return type   acc_t

              1    VUX            uint8     0..3            Determines the source VCU
              2    IN1_V40        vec40_t                   Output vector operand
                                                            Accumulator result operand (register a1 is
              3    RES2_A1        acc_t
                                                            expected)
Operands
                                                            Accumulator result operand (register a2 is
              4    RES3_A2        acc_t
                                                            expected)
                                                            Accumulator result operand (register a3 is
              5    RES4_A3        acc_t
                                                            expected)
              acc_t accRes1;
              acc_t accRes2;
              acc_t accRes3;
C example     acc_t accRes4;
              vec40_t vIn;
              ...
              accRes1 = movv_v40_a0_4op_vuX (1, vIn, accRes2, accRes3, accRes4);

                   This intrinsic returns more than one result. The first result variable should be
Comments      1.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.

Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_v40_a0_5op_vuX
name
Spec syntax   movv {Oop, vuX} vox[0], a0
Return type   acc_t

              1    VUX            uint8     0..3             Determines the source VCU
              2    IN1_V40        vec40_t                    Output vector operand
                                                             Accumulator result operand (register a1 is
              3    RES2_A1        acc_t
                                                             expected)

Operands                                                     Accumulator result operand (register a2 is
              4    RES3_A2        acc_t
                                                             expected)
                                                             Accumulator result operand (register a3 is
              5    RES4_A3        acc_t
                                                             expected)
                                                             Accumulator result operand (register a4 is
              6    RES5_A4        acc_t
                                                             expected)
              acc_t accRes1;
              acc_t accRes2;
              acc_t accRes3;
              acc_t accRes4;
C example     acc_t accRes5;
              vec40_t vIn;
              ...
              accRes1 = movv_v40_a0_5op_vuX (1, vIn, accRes2, accRes3, accRes4, accRes5);

                   This intrinsic returns more than one result. The first result variable should be
Comments      1.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_v40_a0_6op_vuX
name
Spec syntax   movv {Oop, vuX} vox[0], a0

Return type   acc_t

              1    VUX            uint8     0..3             Determines the source VCU
              2    IN1_V40        vec40_t                    Output vector operand
                                                             Accumulator result operand (register a1 is
              3    RES2_A1        acc_t
                                                             expected)
                                                             Accumulator result operand (register a2 is
              4    RES3_A2        acc_t

Operands                                                     expected)
                                                             Accumulator result operand (register a3 is
              5    RES4_A3        acc_t
                                                             expected)
                                                             Accumulator result operand (register a4 is
              6    RES5_A4        acc_t
                                                             expected)
              7    RES6_A5        acc_t                      Accumulator result operand (register a5 is
                                                             expected)
              acc_t accRes1;
              acc_t accRes2;
              acc_t accRes3;
              acc_t accRes4;
C example     acc_t accRes5;
              acc_t accRes6;
              vec40_t vIn;
              ...
              accRes1 = movv_v40_a0_6op_vuX (1, vIn, accRes2, accRes3, accRes4, accRes5, accRes6);

                   This intrinsic returns more than one result. The first result variable should be
Comments      1.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_v40_a0_7op_vuX
name
Spec syntax   movv {Oop, vuX} vox[0], a0

Return type   acc_t

              1    VUX            uint8     0..3             Determines the source VCU
              2    IN1_V40        vec40_t                    Output vector operand
                                                             Accumulator result operand (register a1 is
              3    RES2_A1        acc_t
                                                             expected)
                                                             Accumulator result operand (register a2 is
              4    RES3_A2        acc_t
                                                             expected)

Operands      5
                                                             Accumulator result operand (register a3 is
                   RES4_A3        acc_t
                                                             expected)
                                                             Accumulator result operand (register a4 is
              6    RES5_A4        acc_t
                                                             expected)

Accumulator result operand (register a5 is
              7    RES6_A5        acc_t
                                                             expected)
                                                             Accumulator result operand (register a6 is
              8    RES7_A6        acc_t
                                                             expected)
              acc_t accRes1;
              acc_t accRes2;
              acc_t accRes3;
              acc_t accRes4;
              acc_t accRes5;
C example     acc_t accRes6;
              acc_t accRes7;
              vec40_t vIn;
              ...
              accRes1 = movv_v40_a0_7op_vuX (1, vIn, accRes2, accRes3, accRes4, accRes5, accRes6, accRes7);
                   This intrinsic returns more than one result. The first result variable should be
Comments      1.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_v40_a0_8op_vuX
name
Spec syntax   movv {Oop, vuX} vox[0], a0

Return type   acc_t

              1    VUX            uint8     0..3             Determines the source VCU
              2    IN1_V40        vec40_t                    Output vector operand
                                                             Accumulator result operand (register a1 is
              3    RES2_A1        acc_t
                                                             expected)
                                                             Accumulator result operand (register a2 is
              4    RES3_A2        acc_t
                                                             expected)
                                                             Accumulator result operand (register a3 is
              5    RES4_A3        acc_t
                                                             expected)
Operands
              6
                                                             Accumulator result operand (register a4 is
                   RES5_A4        acc_t
                                                             expected)
                                                             Accumulator result operand (register a5 is
              7    RES6_A5        acc_t
                                                             expected)

Accumulator result operand (register a6 is
              8    RES7_A6        acc_t
                                                             expected)
                                                             Accumulator result operand (register a7 is
              9    RES8_A7        acc_t
                                                             expected)
              acc_t accRes1;
              acc_t accRes2;
              acc_t accRes3;
              acc_t accRes4;
              acc_t accRes5;
              acc_t accRes6;
C example     acc_t accRes7;
              acc_t accRes8;
              vec40_t vIn;
              ...
              accRes1 = movv_v40_a0_8op_vuX (1, vIn, accRes2, accRes3, accRes4, accRes5, accRes6, accRes7,
              accRes8);

                   This intrinsic returns more than one result. The first result variable should be
Comments      1.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_c32_a0_1op_vuX
name
Spec syntax   movv {Qop, vuX [,u]} vc0, a0

Return type   int

              1     VUX           uint8      0..3            Determines the source VCU
Operands                                                     Coefficient operand (register vc0 is
              2     IN1_VC0       coef_t
                                                             expected)
              int accRes;
              coef_t vcoefIn;
C example     ...
              accRes = movv_c32_a0_1op_vuX (1, vcoefIn);

Comments


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_c32_a0_1op_vuX_u
name
Spec syntax   movv {Qop, vuX [,u]} vc0, a0

Return type   int

              1     VUX           uint8      0..3            Determines the source VCU
Operands                                                     Coefficient operand (register vc0 is
              2     IN1_VC0       coef_t
                                                             expected)
              int accRes;
              coef_t vcoefIn;
C example     ...
              accRes = movv_c32_a0_1op_vuX_u (1, vcoefIn);

Comments


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_c32_a0_2op_vuX
name
Spec syntax   movv {Qop, vuX [,u]} vc0, a0

Return type   int

1     VUX           uint8      0..3            Determines the source VCU
                                                             Coefficient operand (register vc0 is
              2     IN1_VC0       coef_t
                                                             expected)
Operands
                                                             Coefficient operand (register vc1 is
              3     IN2_VC1       coef_t
                                                             expected)
              4     RES2_A1       int32                      Accumulator result operand (register a1 is
                                                             expected)
              int accRes1;
              int accRes2;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              ...
              accRes1 = movv_c32_a0_2op_vuX (1, vcoefIn, vcoefIn2, accRes2);

                    This intrinsic returns two results. The first result variable should be placed to
Comments      1.    the left of the = sign (lvalue). The second result variable should be passed as
                    an additional parameter (RES2_A1).


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_c32_a0_2op_vuX_u
name
Spec syntax   movv {Qop, vuX [,u]} vc0, a0

Return type   int

              1     VUX           uint8      0..3            Determines the source VCU
                                                             Coefficient operand (register vc0 is
              2     IN1_VC0       coef_t
                                                             expected)
Operands                                                     Coefficient operand (register vc1 is
              3     IN2_VC1       coef_t
                                                             expected)
                                                             Accumulator result operand (register a1 is
              4     RES2_A1       int32
                                                             expected)
              int accRes1;
              int accRes2;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              ...
              accRes1 = movv_c32_a0_2op_vuX_u (1, vcoefIn, vcoefIn2, accRes2);

                    This intrinsic returns two results. The first result variable should be placed to
Comments      1.    the left of the = sign (lvalue). The second result variable should be passed as

an additional parameter (RES2_A1).


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_c32_a0_3op_vuX
name
Spec syntax   movv {Qop, vuX [,u]} vc0, a0

Return type   int

              1     VUX           uint8      0..3            Determines the source VCU
Operands                                                     Coefficient operand (register vc0 is
              2     IN1_VC0       coef_t
                                                             expected)
                                                             Coefficient operand (register vc1 is
              3     IN2_VC1        coef_t
                                                             expected)
                                                             Coefficient operand (register vc2 is
              4     IN3_VC2        coef_t
                                                             expected)

              5
                                                             Accumulator result operand (register a1 is
                    RES2_A1        int32
                                                             expected)
                                                             Accumulator result operand (register a2 is
              6     RES3_A2        int32
                                                             expected)
              int accRes1;
              int accRes2;
              int accRes3;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              coef_t vcoefIn3;
              ...
              accRes1 = movv_c32_a0_3op_vuX (1, vcoefIn, vcoefIn2, vcoefIn3, accRes2, accRes3);

                    This intrinsic returns more than one result. The first result variable should be
Comments      1.    placed to the left of the = sign (lvalue). Additional result variables should be
                    passed as parameters.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_c32_a0_3op_vuX_u
name
Spec syntax   movv {Qop, vuX [,u]} vc0, a0

Return type   int

              1     VUX            uint8     0..3            Determines the source VCU
                                                             Coefficient operand (register vc0 is
              2     IN1_VC0        coef_t
                                                             expected)
                                                             Coefficient operand (register vc1 is

3     IN2_VC1        coef_t
                                                             expected)
Operands                                                     Coefficient operand (register vc2 is
              4     IN3_VC2        coef_t
                                                             expected)
                                                             Accumulator result operand (register a1 is
              5     RES2_A1        int32
                                                             expected)

              6
                                                             Accumulator result operand (register a2 is
                    RES3_A2        int32
                                                             expected)
              int accRes1;
              int accRes2;
              int accRes3;
C example     coef_t vcoefIn;
              coef_t vcoefIn2;
              coef_t vcoefIn3;
              ...
              accRes1 = movv_c32_a0_3op_vuX_u (1, vcoefIn, vcoefIn2, vcoefIn3, accRes2, accRes3);

                    This intrinsic returns more than one result. The first result variable should be
Comments      1.    placed to the left of the = sign (lvalue). Additional result variables should be
                    passed as parameters.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_c32_a0_4op_vuX
name
Spec syntax   movv {Qop, vuX [,u]} vc0, a0

Return type   int

              1     VUX            uint8     0..3             Determines the source VCU
                                                              Coefficient operand (register vc0 is
              2     IN1_VC0        coef_t
                                                              expected)
                                                              Coefficient operand (register vc1 is
              3     IN2_VC1        coef_t
                                                              expected)
                                                              Coefficient operand (register vc2 is
              4     IN3_VC2        coef_t
                                                              expected)
Operands                                                      Coefficient operand (register vc3 is
              5     IN4_VC3        coef_t
                                                              expected)

Accumulator result operand (register a1 is
              6     RES2_A1        int32
                                                              expected)
                                                              Accumulator result operand (register a2 is
              7     RES3_A2        int32
                                                              expected)

              8
                                                              Accumulator result operand (register a3 is
                    RES4_A3        int32
                                                              expected)
              int accRes1;
              int accRes2;
              int accRes3;
              int accRes4;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              coef_t vcoefIn3;
              coef_t vcoefIn4;
              ...
              accRes1 = movv_c32_a0_4op_vuX (1, vcoefIn, vcoefIn2, vcoefIn3, vcoefIn4, accRes2, accRes3, accRes4);

                    This intrinsic returns more than one result. The first result variable should be
Comments      1.    placed to the left of the = sign (lvalue). Additional result variables should be
                    passed as parameters.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_c32_a0_4op_vuX_u
name
Spec syntax   movv {Qop, vuX [,u]} vc0, a0

Return type   int

              1     VUX            uint8     0..3            Determines the source VCU
                                                             Coefficient operand (register vc0 is
              2     IN1_VC0        coef_t
                                                             expected)
                                                             Coefficient operand (register vc1 is
              3     IN2_VC1        coef_t
                                                             expected)
                                                             Coefficient operand (register vc2 is
              4     IN3_VC2        coef_t
                                                             expected)
Operands                                                     Coefficient operand (register vc3 is
              5     IN4_VC3        coef_t
                                                             expected)
                                                             Accumulator result operand (register a1 is
              6     RES2_A1        int32

expected)
                                                             Accumulator result operand (register a2 is
              7     RES3_A2        int32
                                                             expected)
                                                             Accumulator result operand (register a3 is
              8     RES4_A3        int32
                                                             expected)
              int accRes1;
              int accRes2;
              int accRes3;
              int accRes4;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              coef_t vcoefIn3;
              coef_t vcoefIn4;
              ...
              accRes1 = movv_c32_a0_4op_vuX_u (1, vcoefIn, vcoefIn2, vcoefIn3, vcoefIn4, accRes2, accRes3,
              accRes4);

                    This intrinsic returns more than one result. The first result variable should be
Comments      1.    placed to the left of the = sign (lvalue). Additional result variables should be
                    passed as parameters.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_c32_a20_1op_vuX
name
Spec syntax   movv {Qop, vuX [,u]} vc0, a20

Return type   int

              1     VUX           uint8    0..3               Determines the source VCU
Operands                                                      Coefficient operand (register vc0 is
              2     IN1_VC0       coef_t
                                                              expected)
              int accRes;
              coef_t vcoefIn;
C example     ...
              accRes = movv_c32_a20_1op_vuX (1, vcoefIn);

                    When using movv/vmova intrinsics with high accumulators (a16-a23) in -
Comments      1.    Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                    corresponding a16-a23 registers.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_c32_a20_1op_vuX_u
name
Spec syntax   movv {Qop, vuX [,u]} vc0, a20

Return type   int

              1     VUX           uint8    0..3               Determines the source VCU
Operands                                                      Coefficient operand (register vc0 is
              2     IN1_VC0       coef_t
                                                              expected)
              int accRes;
              coef_t vcoefIn;
C example     ...

accRes = movv_c32_a20_1op_vuX_u (1, vcoefIn);

                    When using movv/vmova intrinsics with high accumulators (a16-a23) in -
Comments      1.    Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                    corresponding a16-a23 registers.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_c32_a20_2op_vuX
name
Spec syntax   movv {Qop, vuX [,u]} vc0, a20

Return type   int

              1     VUX           uint8    0..3               Determines the source VCU
Operands                                                      Coefficient operand (register vc0 is
              2     IN1_VC0       coef_t
                                                              expected)
                                                            Coefficient operand (register vc1 is
              3     IN2_VC1       coef_t
                                                            expected)
                                                            Accumulator result operand (register a21
              4     RES2_A21      int32
                                                            is expected)
              int accRes1;
              int accRes2;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              ...
              accRes1 = movv_c32_a20_2op_vuX (1, vcoefIn, vcoefIn2, accRes2);

                    This intrinsic returns two results. The first result variable should be placed to
              1.    the left of the = sign (lvalue). The second result variable should be passed as
                    an additional parameter (RES2_A21).
Comments
                    When using movv/vmova intrinsics with high accumulators (a16-a23) in -
              2.    Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                    corresponding a16-a23 registers.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_c32_a20_2op_vuX_u
name
Spec syntax   movv {Qop, vuX [,u]} vc0, a20

Return type   int

              1     VUX           uint8     0..3            Determines the source VCU
                                                            Coefficient operand (register vc0 is
              2     IN1_VC0       coef_t
                                                            expected)
Operands                                                    Coefficient operand (register vc1 is

3     IN2_VC1       coef_t
                                                            expected)
                                                            Accumulator result operand (register a21
              4     RES2_A21      int32
                                                            is expected)
              int accRes1;
              int accRes2;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              ...
              accRes1 = movv_c32_a20_2op_vuX_u (1, vcoefIn, vcoefIn2, accRes2);

                    This intrinsic returns two results. The first result variable should be placed to
              1.    the left of the = sign (lvalue). The second result variable should be passed as
                    an additional parameter (RES2_A21).
Comments
                    When using movv/vmova intrinsics with high accumulators (a16-a23) in -
              2.    Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                    corresponding a16-a23 registers.

Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_c32_a20_3op_vuX
name
Spec syntax   movv {Qop, vuX [,u]} vc0, a20

Return type   int

              1     VUX           uint8     0..3             Determines the source VCU
                                                             Coefficient operand (register vc0 is
              2     IN1_VC0       coef_t
                                                             expected)
                                                             Coefficient operand (register vc1 is
              3     IN2_VC1       coef_t
                                                             expected)
Operands                                                     Coefficient operand (register vc2 is
              4     IN3_VC2       coef_t
                                                             expected)
                                                             Accumulator result operand (register a21
              5     RES2_A21      int32
                                                             is expected)

              6
                                                             Accumulator result operand (register a22
                    RES3_A22      int32
                                                             is expected)
              int accRes1;
              int accRes2;
              int accRes3;
              coef_t vcoefIn;

C example     coef_t vcoefIn2;
              coef_t vcoefIn3;
              ...
              accRes1 = movv_c32_a20_3op_vuX (1, vcoefIn, vcoefIn2, vcoefIn3, accRes2, accRes3);

                    This intrinsic returns more than one result. The first result variable should be
              1.    placed to the left of the = sign (lvalue). Additional result variables should be
                    passed as parameters.
Comments
                    When using movv/vmova intrinsics with high accumulators (a16-a23) in -
              2.    Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                    corresponding a16-a23 registers.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_c32_a20_3op_vuX_u
name
Spec syntax   movv {Qop, vuX [,u]} vc0, a20

Return type   int

              1     VUX           uint8     0..3             Determines the source VCU
Operands                                                     Coefficient operand (register vc0 is
              2     IN1_VC0       coef_t
                                                             expected)
                                                             Coefficient operand (register vc1 is
              3     IN2_VC1       coef_t
                                                             expected)
                                                             Coefficient operand (register vc2 is
              4     IN3_VC2       coef_t
                                                             expected)

              5
                                                             Accumulator result operand (register a21
                    RES2_A21      int32
                                                             is expected)
                                                             Accumulator result operand (register a22
              6     RES3_A22      int32
                                                             is expected)
              int accRes1;
              int accRes2;
              int accRes3;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              coef_t vcoefIn3;
              ...
              accRes1 = movv_c32_a20_3op_vuX_u (1, vcoefIn, vcoefIn2, vcoefIn3, accRes2, accRes3);

                    This intrinsic returns more than one result. The first result variable should be

1.    placed to the left of the = sign (lvalue). Additional result variables should be
                    passed as parameters.
Comments
                    When using movv/vmova intrinsics with high accumulators (a16-a23) in -
              2.    Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                    corresponding a16-a23 registers.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_c32_a20_4op_vuX
name
Spec syntax   movv {Qop, vuX [,u]} vc0, a20

Return type   int

              1     VUX           uint8     0..3             Determines the source VCU

              2
                                                             Coefficient operand (register vc0 is
                    IN1_VC0       coef_t
                                                             expected)
                                                             Coefficient operand (register vc1 is
              3     IN2_VC1       coef_t
                                                             expected)
                                                             Coefficient operand (register vc2 is
Operands      4     IN3_VC2       coef_t
                                                             expected)

              5
                                                             Coefficient operand (register vc3 is
                    IN4_VC3       coef_t
                                                             expected)
                                                             Accumulator result operand (register a21
              6     RES2_A21      int32
                                                             is expected)
              7     RES3_A22      int32                      Accumulator result operand (register a22
                                                              is expected)
                                                              Accumulator result operand (register a23
              8     RES4_A23       int32
                                                              is expected)
              int accRes1;
              int accRes2;
              int accRes3;
              int accRes4;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              coef_t vcoefIn3;
              coef_t vcoefIn4;
              ...

accRes1 = movv_c32_a20_4op_vuX (1, vcoefIn, vcoefIn2, vcoefIn3, vcoefIn4, accRes2, accRes3, accRes4);

                    This intrinsic returns more than one result. The first result variable should be
              1.    placed to the left of the = sign (lvalue). Additional result variables should be
                    passed as parameters.
Comments
                    When using movv/vmova intrinsics with high accumulators (a16-a23) in -
              2.    Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                    corresponding a16-a23 registers.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_c32_a20_4op_vuX_u
name
Spec syntax   movv {Qop, vuX [,u]} vc0, a20

Return type   int

              1     VUX            uint8     0..3             Determines the source VCU
                                                              Coefficient operand (register vc0 is
              2     IN1_VC0        coef_t
                                                              expected)

              3
                                                              Coefficient operand (register vc1 is
                    IN2_VC1        coef_t
                                                              expected)
                                                              Coefficient operand (register vc2 is
              4     IN3_VC2        coef_t
                                                              expected)
Operands                                                      Coefficient operand (register vc3 is
              5     IN4_VC3        coef_t
                                                              expected)
                                                              Accumulator result operand (register a21
              6     RES2_A21       int32
                                                              is expected)
                                                              Accumulator result operand (register a22
              7     RES3_A22       int32
                                                              is expected)
                                                              Accumulator result operand (register a23
              8     RES4_A23       int32
                                                              is expected)
C example     int accRes1;
           int accRes2;
           int accRes3;
           int accRes4;

coef_t vcoefIn;
           coef_t vcoefIn2;
           coef_t vcoefIn3;
           coef_t vcoefIn4;
           ...
           accRes1 = movv_c32_a20_4op_vuX_u (1, vcoefIn, vcoefIn2, vcoefIn3, vcoefIn4, accRes2, accRes3,
           accRes4);

                This intrinsic returns more than one result. The first result variable should be
           1.   placed to the left of the = sign (lvalue). Additional result variables should be
                passed as parameters.
Comments
                When using movv/vmova intrinsics with high accumulators (a16-a23) in -
           2.   Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                corresponding a16-a23 registers.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_v40_a16_1op_vuX
name
Spec syntax   movv {Oop, vuX} vox[0], a16

Return type   acc_t

              1    VUX            uint8     0..3           Determines the source VCU
Operands
              2    IN1_V40        vec40_t                  Output vector operand
              acc_t accRes;
              vec40_t vIn;
C example     ...
              accRes = movv_v40_a16_1op_vuX (1, vIn);

                   When using movv/vmova intrinsics with high accumulators (a16-a23) in -
Comments      1.   Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                   corresponding a16-a23 registers.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_v40_a16_2op_vuX
name
Spec syntax   movv {Oop, vuX} vox[0], a16

Return type   acc_t

              1    VUX            uint8     0..3           Determines the source VCU
              2    IN1_V40        vec40_t                  Output vector operand
Operands
                                                           Accumulator result operand (register a17
              3    RES2_A17       acc_t
                                                           is expected)
              acc_t accRes1;
              acc_t accRes2;
C example     vec40_t vIn;
              ...
              accRes1 = movv_v40_a16_2op_vuX (1, vIn, accRes2);

                   This intrinsic returns two results. The first result variable should be placed to
              1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_A17).
Comments

When using movv/vmova intrinsics with high accumulators (a16-a23) in -
              2.   Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                   corresponding a16-a23 registers.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_v40_a16_3op_vuX
name
Spec syntax   movv {Oop, vuX} vox[0], a16
Return type   acc_t

              1    VUX            uint8     0..3            Determines the source VCU
              2    IN1_V40        vec40_t                   Output vector operand

Operands                                                    Accumulator result operand (register a17
              3    RES2_A17       acc_t
                                                            is expected)
                                                            Accumulator result operand (register a18
              4    RES3_A18       acc_t
                                                            is expected)
              acc_t accRes1;
              acc_t accRes2;
              acc_t accRes3;
C example     vec40_t vIn;
              ...
              accRes1 = movv_v40_a16_3op_vuX (1, vIn, accRes2, accRes3);

                   This intrinsic returns more than one result. The first result variable should be
              1.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.
Comments
                   When using movv/vmova intrinsics with high accumulators (a16-a23) in -
              2.   Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                   corresponding a16-a23 registers.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_v40_a16_4op_vuX
name
Spec syntax   movv {Oop, vuX} vox[0], a16

Return type   acc_t

              1    VUX            uint8     0..3            Determines the source VCU
              2    IN1_V40        vec40_t                   Output vector operand
                                                            Accumulator result operand (register a17
              3    RES2_A17       acc_t
                                                            is expected)
Operands
                                                            Accumulator result operand (register a18
              4    RES3_A18       acc_t
                                                            is expected)

Accumulator result operand (register a19
              5    RES4_A19       acc_t
                                                            is expected)
              acc_t accRes1;
              acc_t accRes2;
              acc_t accRes3;
C example     acc_t accRes4;
              vec40_t vIn;
              ...
              accRes1 = movv_v40_a16_4op_vuX (1, vIn, accRes2, accRes3, accRes4);

Comments      1.   This intrinsic returns more than one result. The first result variable should be
                   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.
                   When using movv/vmova intrinsics with high accumulators (a16-a23) in -
              2.   Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                   corresponding a16-a23 registers.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_v40_a16_5op_vuX
name
Spec syntax   movv {Oop, vuX} vox[0], a16

Return type   acc_t

              1    VUX            uint8     0..3             Determines the source VCU
              2    IN1_V40        vec40_t                    Output vector operand
                                                             Accumulator result operand (register a17
              3    RES2_A17       acc_t
                                                             is expected)

Operands                                                     Accumulator result operand (register a18
              4    RES3_A18       acc_t
                                                             is expected)

              5
                                                             Accumulator result operand (register a19
                   RES4_A19       acc_t
                                                             is expected)
                                                             Accumulator result operand (register a20
              6    RES5_A20       acc_t
                                                             is expected)
              acc_t accRes1;
              acc_t accRes2;
              acc_t accRes3;
              acc_t accRes4;
C example     acc_t accRes5;
              vec40_t vIn;
              ...
              accRes1 = movv_v40_a16_5op_vuX (1, vIn, accRes2, accRes3, accRes4, accRes5);

                   This intrinsic returns more than one result. The first result variable should be

1.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.
Comments
                   When using movv/vmova intrinsics with high accumulators (a16-a23) in -
              2.   Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                   corresponding a16-a23 registers.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_v40_a16_6op_vuX
name
Spec syntax   movv {Oop, vuX} vox[0], a16
Return type   acc_t

              1    VUX            uint8     0..3             Determines the source VCU
              2    IN1_V40        vec40_t                    Output vector operand
                                                             Accumulator result operand (register a17
              3    RES2_A17       acc_t
                                                             is expected)
                                                             Accumulator result operand (register a18
              4    RES3_A18       acc_t
                                                             is expected)
Operands
                                                             Accumulator result operand (register a19
              5    RES4_A19       acc_t
                                                             is expected)
                                                             Accumulator result operand (register a20
              6    RES5_A20       acc_t
                                                             is expected)
                                                             Accumulator result operand (register a21
              7    RES6_A21       acc_t
                                                             is expected)
              acc_t accRes1;
              acc_t accRes2;
              acc_t accRes3;
              acc_t accRes4;
C example     acc_t accRes5;
              acc_t accRes6;
              vec40_t vIn;
              ...
              accRes1 = movv_v40_a16_6op_vuX (1, vIn, accRes2, accRes3, accRes4, accRes5, accRes6);

                   This intrinsic returns more than one result. The first result variable should be
              1.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.
Comments
                   When using movv/vmova intrinsics with high accumulators (a16-a23) in -

2.   Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                   corresponding a16-a23 registers.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_v40_a16_7op_vuX
name
Spec syntax   movv {Oop, vuX} vox[0], a16

Return type   acc_t

              1    VUX            uint8     0..3             Determines the source VCU
              2    IN1_V40        vec40_t                    Output vector operand

Operands      3
                                                             Accumulator result operand (register a17
                   RES2_A17       acc_t
                                                             is expected)
                                                             Accumulator result operand (register a18
              4    RES3_A18       acc_t
                                                             is expected)
                                                             Accumulator result operand (register a19
              5    RES4_A19       acc_t
                                                             is expected)
                                                             Accumulator result operand (register a20
              6    RES5_A20       acc_t
                                                             is expected)

              7
                                                             Accumulator result operand (register a21
                   RES6_A21       acc_t
                                                             is expected)
                                                             Accumulator result operand (register a22
              8    RES7_A22       acc_t
                                                             is expected)
              acc_t accRes1;
              acc_t accRes2;
              acc_t accRes3;
              acc_t accRes4;
              acc_t accRes5;
C example     acc_t accRes6;
              acc_t accRes7;
              vec40_t vIn;
              ...
              accRes1 = movv_v40_a16_7op_vuX (1, vIn, accRes2, accRes3, accRes4, accRes5, accRes6, accRes7);

                   This intrinsic returns more than one result. The first result variable should be
              1.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.
Comments

When using movv/vmova intrinsics with high accumulators (a16-a23) in -
              2.   Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                   corresponding a16-a23 registers.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_v40_a16_8op_vuX
name
Spec syntax   movv {Oop, vuX} vox[0], a16

Return type   acc_t

              1    VUX            uint8     0..3             Determines the source VCU
              2    IN1_V40        vec40_t                    Output vector operand
                                                             Accumulator result operand (register a17
              3    RES2_A17       acc_t
                                                             is expected)
                                                             Accumulator result operand (register a18
              4    RES3_A18       acc_t
Operands                                                     is expected)
                                                             Accumulator result operand (register a19
              5    RES4_A19       acc_t
                                                             is expected)
                                                             Accumulator result operand (register a20
              6    RES5_A20       acc_t
                                                             is expected)
              7    RES6_A21       acc_t                      Accumulator result operand (register a21
                                                           is expected)
                                                           Accumulator result operand (register a22
            8    RES7_A22       acc_t
                                                           is expected)

            9
                                                           Accumulator result operand (register a23
                 RES8_A23       acc_t
                                                           is expected)
            acc_t accRes1;
            acc_t accRes2;
            acc_t accRes3;
            acc_t accRes4;
            acc_t accRes5;
            acc_t accRes6;
C example   acc_t accRes7;
            acc_t accRes8;
            vec40_t vIn;
            ...
            accRes1 = movv_v40_a16_8op_vuX (1, vIn, accRes2, accRes3, accRes4, accRes5, accRes6, accRes7,
            accRes8);

This intrinsic returns more than one result. The first result variable should be
            1.   placed to the left of the = sign (lvalue). Additional result variables should be
                 passed as parameters.
Comments
                 When using movv/vmova intrinsics with high accumulators (a16-a23) in -
            2.   Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                 corresponding a16-a23 registers.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_c32_a16_1op_vuX
name
Spec syntax   movv {Qop, vuX [,u]} vc0, a16

Return type   int

              1     VUX           uint8    0..3               Determines the source VCU
Operands                                                      Coefficient operand (register vc0 is
              2     IN1_VC0       coef_t
                                                              expected)
              int accRes;
              coef_t vcoefIn;
C example     ...
              accRes = movv_c32_a16_1op_vuX (1, vcoefIn);

                    When using movv/vmova intrinsics with high accumulators (a16-a23) in -
Comments      1.    Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                    corresponding a16-a23 registers.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_c32_a16_1op_vuX_u
name
Spec syntax   movv {Qop, vuX [,u]} vc0, a16

Return type   int

              1     VUX           uint8    0..3               Determines the source VCU
Operands                                                      Coefficient operand (register vc0 is
              2     IN1_VC0       coef_t
                                                              expected)
              int accRes;
              coef_t vcoefIn;
C example     ...
              accRes = movv_c32_a16_1op_vuX_u (1, vcoefIn);

                    When using movv/vmova intrinsics with high accumulators (a16-a23) in -
Comments      1.    Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                    corresponding a16-a23 registers.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_c32_a16_2op_vuX
name
Spec syntax   movv {Qop, vuX [,u]} vc0, a16

Return type   int

              1     VUX           uint8    0..3               Determines the source VCU

Operands                                                      Coefficient operand (register vc0 is
              2     IN1_VC0       coef_t
                                                              expected)
                                                            Coefficient operand (register vc1 is
              3     IN2_VC1       coef_t
                                                            expected)
                                                            Accumulator result operand (register a17
              4     RES2_A17      int32
                                                            is expected)
              int accRes1;
              int accRes2;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              ...
              accRes1 = movv_c32_a16_2op_vuX (1, vcoefIn, vcoefIn2, accRes2);

                    This intrinsic returns two results. The first result variable should be placed to
              1.    the left of the = sign (lvalue). The second result variable should be passed as
                    an additional parameter (RES2_A17).
Comments
                    When using movv/vmova intrinsics with high accumulators (a16-a23) in -
              2.    Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                    corresponding a16-a23 registers.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_c32_a16_2op_vuX_u
name
Spec syntax   movv {Qop, vuX [,u]} vc0, a16

Return type   int

              1     VUX           uint8     0..3            Determines the source VCU
                                                            Coefficient operand (register vc0 is
              2     IN1_VC0       coef_t
                                                            expected)
Operands                                                    Coefficient operand (register vc1 is
              3     IN2_VC1       coef_t
                                                            expected)
                                                            Accumulator result operand (register a17
              4     RES2_A17      int32
                                                            is expected)
              int accRes1;
              int accRes2;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              ...
              accRes1 = movv_c32_a16_2op_vuX_u (1, vcoefIn, vcoefIn2, accRes2);

This intrinsic returns two results. The first result variable should be placed to
              1.    the left of the = sign (lvalue). The second result variable should be passed as
                    an additional parameter (RES2_A17).
Comments
                    When using movv/vmova intrinsics with high accumulators (a16-a23) in -
              2.    Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                    corresponding a16-a23 registers.

Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_c32_a16_3op_vuX
name
Spec syntax   movv {Qop, vuX [,u]} vc0, a16

Return type   int

              1     VUX           uint8     0..3             Determines the source VCU
                                                             Coefficient operand (register vc0 is
              2     IN1_VC0       coef_t
                                                             expected)
                                                             Coefficient operand (register vc1 is
              3     IN2_VC1       coef_t
                                                             expected)
Operands                                                     Coefficient operand (register vc2 is
              4     IN3_VC2       coef_t
                                                             expected)
                                                             Accumulator result operand (register a17
              5     RES2_A17      int32
                                                             is expected)

              6
                                                             Accumulator result operand (register a18
                    RES3_A18      int32
                                                             is expected)
              int accRes1;
              int accRes2;
              int accRes3;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              coef_t vcoefIn3;
              ...
              accRes1 = movv_c32_a16_3op_vuX (1, vcoefIn, vcoefIn2, vcoefIn3, accRes2, accRes3);

                    This intrinsic returns more than one result. The first result variable should be
              1.    placed to the left of the = sign (lvalue). Additional result variables should be
                    passed as parameters.
Comments
                    When using movv/vmova intrinsics with high accumulators (a16-a23) in -

2.    Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                    corresponding a16-a23 registers.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_c32_a16_3op_vuX_u
name
Spec syntax   movv {Qop, vuX [,u]} vc0, a16

Return type   int

              1     VUX           uint8     0..3             Determines the source VCU
Operands                                                     Coefficient operand (register vc0 is
              2     IN1_VC0       coef_t
                                                             expected)
                                                             Coefficient operand (register vc1 is
              3     IN2_VC1       coef_t
                                                             expected)
                                                             Coefficient operand (register vc2 is
              4     IN3_VC2       coef_t
                                                             expected)

              5
                                                             Accumulator result operand (register a17
                    RES2_A17      int32
                                                             is expected)
                                                             Accumulator result operand (register a18
              6     RES3_A18      int32
                                                             is expected)
              int accRes1;
              int accRes2;
              int accRes3;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              coef_t vcoefIn3;
              ...
              accRes1 = movv_c32_a16_3op_vuX_u (1, vcoefIn, vcoefIn2, vcoefIn3, accRes2, accRes3);

                    This intrinsic returns more than one result. The first result variable should be
              1.    placed to the left of the = sign (lvalue). Additional result variables should be
                    passed as parameters.
Comments
                    When using movv/vmova intrinsics with high accumulators (a16-a23) in -
              2.    Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                    corresponding a16-a23 registers.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_c32_a16_4op_vuX
name
Spec syntax   movv {Qop, vuX [,u]} vc0, a16

Return type   int

1     VUX           uint8     0..3             Determines the source VCU

              2
                                                             Coefficient operand (register vc0 is
                    IN1_VC0       coef_t
                                                             expected)
                                                             Coefficient operand (register vc1 is
              3     IN2_VC1       coef_t
                                                             expected)
                                                             Coefficient operand (register vc2 is
Operands      4     IN3_VC2       coef_t
                                                             expected)

              5
                                                             Coefficient operand (register vc3 is
                    IN4_VC3       coef_t
                                                             expected)
                                                             Accumulator result operand (register a17
              6     RES2_A17      int32
                                                             is expected)
              7     RES3_A18      int32                      Accumulator result operand (register a18
                                                              is expected)
                                                              Accumulator result operand (register a19
              8     RES4_A19       int32
                                                              is expected)
              int accRes1;
              int accRes2;
              int accRes3;
              int accRes4;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              coef_t vcoefIn3;
              coef_t vcoefIn4;
              ...
              accRes1 = movv_c32_a16_4op_vuX (1, vcoefIn, vcoefIn2, vcoefIn3, vcoefIn4, accRes2, accRes3, accRes4);

                    This intrinsic returns more than one result. The first result variable should be
              1.    placed to the left of the = sign (lvalue). Additional result variables should be
                    passed as parameters.
Comments
                    When using movv/vmova intrinsics with high accumulators (a16-a23) in -
              2.    Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                    corresponding a16-a23 registers.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU

Intrinsic     movv_c32_a16_4op_vuX_u
name
Spec syntax   movv {Qop, vuX [,u]} vc0, a16

Return type   int

              1     VUX            uint8     0..3             Determines the source VCU
                                                              Coefficient operand (register vc0 is
              2     IN1_VC0        coef_t
                                                              expected)

              3
                                                              Coefficient operand (register vc1 is
                    IN2_VC1        coef_t
                                                              expected)
                                                              Coefficient operand (register vc2 is
              4     IN3_VC2        coef_t
                                                              expected)
Operands                                                      Coefficient operand (register vc3 is
              5     IN4_VC3        coef_t
                                                              expected)
                                                              Accumulator result operand (register a17
              6     RES2_A17       int32
                                                              is expected)
                                                              Accumulator result operand (register a18
              7     RES3_A18       int32
                                                              is expected)
                                                              Accumulator result operand (register a19
              8     RES4_A19       int32
                                                              is expected)
C example     int accRes1;
           int accRes2;
           int accRes3;
           int accRes4;
           coef_t vcoefIn;
           coef_t vcoefIn2;
           coef_t vcoefIn3;
           coef_t vcoefIn4;
           ...
           accRes1 = movv_c32_a16_4op_vuX_u (1, vcoefIn, vcoefIn2, vcoefIn3, vcoefIn4, accRes2, accRes3,
           accRes4);

                This intrinsic returns more than one result. The first result variable should be
           1.   placed to the left of the = sign (lvalue). Additional result variables should be
                passed as parameters.
Comments
                When using movv/vmova intrinsics with high accumulators (a16-a23) in -
           2.   Os3/-Os4 optimization levels, the accumulator variables must be bound to the

corresponding a16-a23 registers.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_modv0_a8
name
Spec syntax   movv modv0, a8

Return type   int

              int accRes;
C example     ...
              accRes = movv_modv0_a8 ();

Comments


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_modv2_a8
name
Spec syntax   movv modv2, a8

Return type   int

              int accRes;
C example     ...
              accRes = movv_modv2_a8 ();

Comments


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_c32_acc_vuX
name
Spec syntax   movv {vuX [,u]} vcX, acZ

Return type   int

              1     VUX           uint8     0..3        Determines the source VCU
Operands
              2     IN1_C32       coef_t                Coefficient operand
              int acc1;
              coef_t vcoefIn;
C example     ...
              acc1 = movv_c32_acc_vuX (1, vcoefIn);

Comments


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_c32_acc_vuX_u
name
Spec syntax   movv {vuX [,u]} vcX, acZ

Return type   int

              1     VUX           uint8     0..3        Determines the source VCU
Operands
              2     IN1_C32       coef_t                Coefficient operand
              int acc1;
              coef_t vcoefIn;
C example     ...
              acc1 = movv_c32_acc_vuX_u (1, vcoefIn);

Comments


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_v40_a8_1op_vuX
name
Spec syntax   movv {Oop, vuX} vox[0], a8

Return type   acc_t

              1    VUX            uint8     0..3            Determines the source VCU
Operands
              2    IN1_V40        vec40_t                   Output vector operand
              acc_t accRes;
              vec40_t vIn;
C example     ...
              accRes = movv_v40_a8_1op_vuX (1, vIn);

Comments


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_v40_a8_2op_vuX
name
Spec syntax   movv {Oop, vuX} vox[0], a8

Return type   acc_t

              1    VUX            uint8     0..3            Determines the source VCU
              2    IN1_V40        vec40_t                   Output vector operand
Operands
                                                            Accumulator result operand (register a9 is

3    RES2_A9        acc_t
                                                            expected)
              acc_t accRes1;
              acc_t accRes2;
C example     vec40_t vIn;
              ...
              accRes1 = movv_v40_a8_2op_vuX (1, vIn, accRes2);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_A9).


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_v40_a8_3op_vuX
name
Spec syntax   movv {Oop, vuX} vox[0], a8

Return type   acc_t

              1    VUX            uint8     0..3            Determines the source VCU
Operands      2    IN1_V40        vec40_t                   Output vector operand
              3    RES2_A9        acc_t                     Accumulator result operand (register a9 is
                                                            expected)
                                                            Accumulator result operand (register a10
              4    RES3_A10       acc_t
                                                            is expected)
              acc_t accRes1;
              acc_t accRes2;
              acc_t accRes3;
C example     vec40_t vIn;
              ...
              accRes1 = movv_v40_a8_3op_vuX (1, vIn, accRes2, accRes3);

                   This intrinsic returns more than one result. The first result variable should be
Comments      1.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_v40_a8_4op_vuX
name
Spec syntax   movv {Oop, vuX} vox[0], a8

Return type   acc_t

              1    VUX            uint8     0..3            Determines the source VCU
              2    IN1_V40        vec40_t                   Output vector operand
                                                            Accumulator result operand (register a9 is
              3    RES2_A9        acc_t
                                                            expected)
Operands
                                                            Accumulator result operand (register a10
              4    RES3_A10       acc_t
                                                            is expected)

Accumulator result operand (register a11
              5    RES4_A11       acc_t
                                                            is expected)
              acc_t accRes1;
              acc_t accRes2;
              acc_t accRes3;
C example     acc_t accRes4;
              vec40_t vIn;
              ...
              accRes1 = movv_v40_a8_4op_vuX (1, vIn, accRes2, accRes3, accRes4);

                   This intrinsic returns more than one result. The first result variable should be
Comments      1.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_v40_a8_5op_vuX
name
Spec syntax   movv {Oop, vuX} vox[0], a8
Return type   acc_t

              1    VUX            uint8     0..3             Determines the source VCU
              2    IN1_V40        vec40_t                    Output vector operand
                                                             Accumulator result operand (register a9 is
              3    RES2_A9        acc_t
                                                             expected)

Operands                                                     Accumulator result operand (register a10
              4    RES3_A10       acc_t
                                                             is expected)
                                                             Accumulator result operand (register a11
              5    RES4_A11       acc_t
                                                             is expected)
                                                             Accumulator result operand (register a12
              6    RES5_A12       acc_t
                                                             is expected)
              acc_t accRes1;
              acc_t accRes2;
              acc_t accRes3;
              acc_t accRes4;
C example     acc_t accRes5;
              vec40_t vIn;
              ...
              accRes1 = movv_v40_a8_5op_vuX (1, vIn, accRes2, accRes3, accRes4, accRes5);

                   This intrinsic returns more than one result. The first result variable should be
Comments      1.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_v40_a8_6op_vuX
name

Spec syntax   movv {Oop, vuX} vox[0], a8

Return type   acc_t

              1    VUX            uint8     0..3             Determines the source VCU
              2    IN1_V40        vec40_t                    Output vector operand
                                                             Accumulator result operand (register a9 is
              3    RES2_A9        acc_t
                                                             expected)
                                                             Accumulator result operand (register a10
              4    RES3_A10       acc_t
Operands                                                     is expected)
                                                             Accumulator result operand (register a11
              5    RES4_A11       acc_t
                                                             is expected)
                                                             Accumulator result operand (register a12
              6    RES5_A12       acc_t
                                                             is expected)
              7    RES6_A13       acc_t                      Accumulator result operand (register a13
                                                             is expected)
              acc_t accRes1;
              acc_t accRes2;
              acc_t accRes3;
              acc_t accRes4;
C example     acc_t accRes5;
              acc_t accRes6;
              vec40_t vIn;
              ...
              accRes1 = movv_v40_a8_6op_vuX (1, vIn, accRes2, accRes3, accRes4, accRes5, accRes6);

                   This intrinsic returns more than one result. The first result variable should be
Comments      1.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_v40_a8_7op_vuX
name
Spec syntax   movv {Oop, vuX} vox[0], a8

Return type   acc_t

              1    VUX            uint8     0..3             Determines the source VCU
              2    IN1_V40        vec40_t                    Output vector operand
                                                             Accumulator result operand (register a9 is
              3    RES2_A9        acc_t
                                                             expected)

Accumulator result operand (register a10
              4    RES3_A10       acc_t
                                                             is expected)

Operands      5
                                                             Accumulator result operand (register a11
                   RES4_A11       acc_t
                                                             is expected)
                                                             Accumulator result operand (register a12
              6    RES5_A12       acc_t
                                                             is expected)
                                                             Accumulator result operand (register a13
              7    RES6_A13       acc_t
                                                             is expected)
                                                             Accumulator result operand (register a14
              8    RES7_A14       acc_t
                                                             is expected)
              acc_t accRes1;
              acc_t accRes2;
              acc_t accRes3;
              acc_t accRes4;
              acc_t accRes5;
C example     acc_t accRes6;
              acc_t accRes7;
              vec40_t vIn;
              ...
              accRes1 = movv_v40_a8_7op_vuX (1, vIn, accRes2, accRes3, accRes4, accRes5, accRes6, accRes7);
                   This intrinsic returns more than one result. The first result variable should be
Comments      1.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_v40_a8_8op_vuX
name
Spec syntax   movv {Oop, vuX} vox[0], a8

Return type   acc_t

              1    VUX            uint8     0..3             Determines the source VCU
              2    IN1_V40        vec40_t                    Output vector operand
                                                             Accumulator result operand (register a9 is
              3    RES2_A9        acc_t
                                                             expected)
                                                             Accumulator result operand (register a10
              4    RES3_A10       acc_t
                                                             is expected)

Accumulator result operand (register a11
              5    RES4_A11       acc_t
                                                             is expected)
Operands
              6
                                                             Accumulator result operand (register a12
                   RES5_A12       acc_t
                                                             is expected)
                                                             Accumulator result operand (register a13
              7    RES6_A13       acc_t
                                                             is expected)
                                                             Accumulator result operand (register a14
              8    RES7_A14       acc_t
                                                             is expected)
                                                             Accumulator result operand (register a15
              9    RES8_A15       acc_t
                                                             is expected)
              acc_t accRes1;
              acc_t accRes2;
              acc_t accRes3;
              acc_t accRes4;
              acc_t accRes5;
              acc_t accRes6;
C example     acc_t accRes7;
              acc_t accRes8;
              vec40_t vIn;
              ...
              accRes1 = movv_v40_a8_8op_vuX (1, vIn, accRes2, accRes3, accRes4, accRes5, accRes6, accRes7,
              accRes8);

                   This intrinsic returns more than one result. The first result variable should be
Comments      1.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_c32_a12_1op_vuX
name
Spec syntax   movv {Qop, vuX [,u]} vc0, a12

Return type   int

              1     VUX           uint8    0..3               Determines the source VCU
Operands                                                      Coefficient operand (register vc0 is
              2     IN1_VC0       coef_t
                                                              expected)
              int accRes;
              coef_t vcoefIn;
C example     ...
              accRes = movv_c32_a12_1op_vuX (1, vcoefIn);

Comments


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_c32_a12_1op_vuX_u
name
Spec syntax   movv {Qop, vuX [,u]} vc0, a12

Return type   int

              1     VUX           uint8    0..3               Determines the source VCU
Operands                                                      Coefficient operand (register vc0 is
              2     IN1_VC0       coef_t
                                                              expected)
              int accRes;
              coef_t vcoefIn;
C example     ...
              accRes = movv_c32_a12_1op_vuX_u (1, vcoefIn);

Comments


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_c32_a12_2op_vuX
name
Spec syntax   movv {Qop, vuX [,u]} vc0, a12

Return type   int

              1     VUX           uint8    0..3               Determines the source VCU
                                                              Coefficient operand (register vc0 is
              2     IN1_VC0       coef_t
                                                              expected)
Operands
                                                              Coefficient operand (register vc1 is
              3     IN2_VC1       coef_t
                                                              expected)
              4     RES2_A13      int32                       Accumulator result operand (register a13
                                                            is expected)
              int accRes1;
              int accRes2;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              ...
              accRes1 = movv_c32_a12_2op_vuX (1, vcoefIn, vcoefIn2, accRes2);

                    This intrinsic returns two results. The first result variable should be placed to
Comments      1.    the left of the = sign (lvalue). The second result variable should be passed as
                    an additional parameter (RES2_A13).


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_c32_a12_2op_vuX_u
name
Spec syntax   movv {Qop, vuX [,u]} vc0, a12

Return type   int

              1     VUX           uint8     0..3            Determines the source VCU
                                                            Coefficient operand (register vc0 is
              2     IN1_VC0       coef_t
                                                            expected)
Operands                                                    Coefficient operand (register vc1 is
              3     IN2_VC1       coef_t

expected)
                                                            Accumulator result operand (register a13
              4     RES2_A13      int32
                                                            is expected)
              int accRes1;
              int accRes2;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              ...
              accRes1 = movv_c32_a12_2op_vuX_u (1, vcoefIn, vcoefIn2, accRes2);

                    This intrinsic returns two results. The first result variable should be placed to
Comments      1.    the left of the = sign (lvalue). The second result variable should be passed as
                    an additional parameter (RES2_A13).


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_c32_a12_3op_vuX
name
Spec syntax   movv {Qop, vuX [,u]} vc0, a12

Return type   int

              1     VUX           uint8     0..3            Determines the source VCU
Operands                                                    Coefficient operand (register vc0 is
              2     IN1_VC0       coef_t
                                                            expected)
                                                             Coefficient operand (register vc1 is
              3     IN2_VC1       coef_t
                                                             expected)
                                                             Coefficient operand (register vc2 is
              4     IN3_VC2       coef_t
                                                             expected)

              5
                                                             Accumulator result operand (register a13
                    RES2_A13      int32
                                                             is expected)
                                                             Accumulator result operand (register a14
              6     RES3_A14      int32
                                                             is expected)
              int accRes1;
              int accRes2;
              int accRes3;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              coef_t vcoefIn3;
              ...
              accRes1 = movv_c32_a12_3op_vuX (1, vcoefIn, vcoefIn2, vcoefIn3, accRes2, accRes3);

                    This intrinsic returns more than one result. The first result variable should be

Comments      1.    placed to the left of the = sign (lvalue). Additional result variables should be
                    passed as parameters.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_c32_a12_3op_vuX_u
name
Spec syntax   movv {Qop, vuX [,u]} vc0, a12

Return type   int

              1     VUX           uint8     0..3             Determines the source VCU
                                                             Coefficient operand (register vc0 is
              2     IN1_VC0       coef_t
                                                             expected)
                                                             Coefficient operand (register vc1 is
              3     IN2_VC1       coef_t
                                                             expected)
Operands                                                     Coefficient operand (register vc2 is
              4     IN3_VC2       coef_t
                                                             expected)
                                                             Accumulator result operand (register a13
              5     RES2_A13      int32
                                                             is expected)

              6
                                                             Accumulator result operand (register a14
                    RES3_A14      int32
                                                             is expected)
              int accRes1;
              int accRes2;
              int accRes3;
C example     coef_t vcoefIn;
              coef_t vcoefIn2;
              coef_t vcoefIn3;
              ...
              accRes1 = movv_c32_a12_3op_vuX_u (1, vcoefIn, vcoefIn2, vcoefIn3, accRes2, accRes3);

                    This intrinsic returns more than one result. The first result variable should be
Comments      1.    placed to the left of the = sign (lvalue). Additional result variables should be
                    passed as parameters.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_c32_a12_4op_vuX
name
Spec syntax   movv {Qop, vuX [,u]} vc0, a12

Return type   int

              1     VUX            uint8     0..3             Determines the source VCU
                                                              Coefficient operand (register vc0 is
              2     IN1_VC0        coef_t

expected)
                                                              Coefficient operand (register vc1 is
              3     IN2_VC1        coef_t
                                                              expected)
                                                              Coefficient operand (register vc2 is
              4     IN3_VC2        coef_t
                                                              expected)
Operands                                                      Coefficient operand (register vc3 is
              5     IN4_VC3        coef_t
                                                              expected)
                                                              Accumulator result operand (register a13
              6     RES2_A13       int32
                                                              is expected)
                                                              Accumulator result operand (register a14
              7     RES3_A14       int32
                                                              is expected)

              8
                                                              Accumulator result operand (register a15
                    RES4_A15       int32
                                                              is expected)
              int accRes1;
              int accRes2;
              int accRes3;
              int accRes4;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              coef_t vcoefIn3;
              coef_t vcoefIn4;
              ...
              accRes1 = movv_c32_a12_4op_vuX (1, vcoefIn, vcoefIn2, vcoefIn3, vcoefIn4, accRes2, accRes3, accRes4);

                    This intrinsic returns more than one result. The first result variable should be
Comments      1.    placed to the left of the = sign (lvalue). Additional result variables should be
                    passed as parameters.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_c32_a12_4op_vuX_u
name
Spec syntax   movv {Qop, vuX [,u]} vc0, a12

Return type   int

              1     VUX            uint8    0..3             Determines the source VCU
                                                             Coefficient operand (register vc0 is
              2     IN1_VC0        coef_t
                                                             expected)

Coefficient operand (register vc1 is
              3     IN2_VC1        coef_t
                                                             expected)
                                                             Coefficient operand (register vc2 is
              4     IN3_VC2        coef_t
                                                             expected)
Operands                                                     Coefficient operand (register vc3 is
              5     IN4_VC3        coef_t
                                                             expected)
                                                             Accumulator result operand (register a13
              6     RES2_A13       int32
                                                             is expected)
                                                             Accumulator result operand (register a14
              7     RES3_A14       int32
                                                             is expected)
                                                             Accumulator result operand (register a15
              8     RES4_A15       int32
                                                             is expected)
              int accRes1;
              int accRes2;
              int accRes3;
              int accRes4;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              coef_t vcoefIn3;
              coef_t vcoefIn4;
              ...
              accRes1 = movv_c32_a12_4op_vuX_u (1, vcoefIn, vcoefIn2, vcoefIn3, vcoefIn4, accRes2, accRes3,
              accRes4);

                    This intrinsic returns more than one result. The first result variable should be
Comments      1.    placed to the left of the = sign (lvalue). Additional result variables should be
                    passed as parameters.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_modv0_a0
name
Spec syntax   movv modv0, a0

Return type   int

              int accRes;
C example     ...
              accRes = movv_modv0_a0 ();

Comments


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_modv2_a0
name
Spec syntax   movv modv2, a0

Return type   int

              int accRes;
C example     ...
              accRes = movv_modv2_a0 ();

Comments


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_c32_a8_1op_vuX
name

Spec syntax   movv {Qop, vuX [,u]} vc0, a8

Return type   int

              1     VUX           uint8      0..3            Determines the source VCU
Operands                                                     Coefficient operand (register vc0 is
              2     IN1_VC0       coef_t
                                                             expected)
              int accRes;
              coef_t vcoefIn;
C example     ...
              accRes = movv_c32_a8_1op_vuX (1, vcoefIn);

Comments


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_c32_a8_1op_vuX_u
name
Spec syntax   movv {Qop, vuX [,u]} vc0, a8

Return type   int

              1     VUX           uint8      0..3            Determines the source VCU
Operands                                                     Coefficient operand (register vc0 is
              2     IN1_VC0       coef_t
                                                             expected)
              int accRes;
              coef_t vcoefIn;
C example     ...
              accRes = movv_c32_a8_1op_vuX_u (1, vcoefIn);

Comments


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_c32_a8_2op_vuX
name
Spec syntax   movv {Qop, vuX [,u]} vc0, a8

Return type   int

              1     VUX           uint8      0..3            Determines the source VCU
                                                             Coefficient operand (register vc0 is
              2     IN1_VC0       coef_t
                                                             expected)
Operands
                                                             Coefficient operand (register vc1 is
              3     IN2_VC1       coef_t
                                                             expected)
              4     RES2_A9       int32                      Accumulator result operand (register a9 is
                                                             expected)
              int accRes1;
              int accRes2;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              ...
              accRes1 = movv_c32_a8_2op_vuX (1, vcoefIn, vcoefIn2, accRes2);

                    This intrinsic returns two results. The first result variable should be placed to
Comments      1.    the left of the = sign (lvalue). The second result variable should be passed as
                    an additional parameter (RES2_A9).

Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_c32_a8_2op_vuX_u
name
Spec syntax   movv {Qop, vuX [,u]} vc0, a8

Return type   int

              1     VUX           uint8      0..3            Determines the source VCU
                                                             Coefficient operand (register vc0 is
              2     IN1_VC0       coef_t
                                                             expected)
Operands                                                     Coefficient operand (register vc1 is
              3     IN2_VC1       coef_t
                                                             expected)
                                                             Accumulator result operand (register a9 is
              4     RES2_A9       int32
                                                             expected)
              int accRes1;
              int accRes2;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              ...
              accRes1 = movv_c32_a8_2op_vuX_u (1, vcoefIn, vcoefIn2, accRes2);

                    This intrinsic returns two results. The first result variable should be placed to
Comments      1.    the left of the = sign (lvalue). The second result variable should be passed as
                    an additional parameter (RES2_A9).


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_c32_a8_3op_vuX
name
Spec syntax   movv {Qop, vuX [,u]} vc0, a8

Return type   int

              1     VUX           uint8      0..3            Determines the source VCU
Operands                                                     Coefficient operand (register vc0 is
              2     IN1_VC0       coef_t
                                                             expected)
                                                             Coefficient operand (register vc1 is
              3     IN2_VC1        coef_t
                                                             expected)
                                                             Coefficient operand (register vc2 is
              4     IN3_VC2        coef_t
                                                             expected)

              5
                                                             Accumulator result operand (register a9 is
                    RES2_A9        int32

expected)
                                                             Accumulator result operand (register a10
              6     RES3_A10       int32
                                                             is expected)
              int accRes1;
              int accRes2;
              int accRes3;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              coef_t vcoefIn3;
              ...
              accRes1 = movv_c32_a8_3op_vuX (1, vcoefIn, vcoefIn2, vcoefIn3, accRes2, accRes3);

                    This intrinsic returns more than one result. The first result variable should be
Comments      1.    placed to the left of the = sign (lvalue). Additional result variables should be
                    passed as parameters.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_c32_a8_3op_vuX_u
name
Spec syntax   movv {Qop, vuX [,u]} vc0, a8

Return type   int

              1     VUX            uint8     0..3            Determines the source VCU
                                                             Coefficient operand (register vc0 is
              2     IN1_VC0        coef_t
                                                             expected)
                                                             Coefficient operand (register vc1 is
              3     IN2_VC1        coef_t
                                                             expected)
Operands                                                     Coefficient operand (register vc2 is
              4     IN3_VC2        coef_t
                                                             expected)
                                                             Accumulator result operand (register a9 is
              5     RES2_A9        int32
                                                             expected)

              6
                                                             Accumulator result operand (register a10
                    RES3_A10       int32
                                                             is expected)
              int accRes1;
              int accRes2;
              int accRes3;
C example     coef_t vcoefIn;
              coef_t vcoefIn2;
              coef_t vcoefIn3;
              ...
              accRes1 = movv_c32_a8_3op_vuX_u (1, vcoefIn, vcoefIn2, vcoefIn3, accRes2, accRes3);

This intrinsic returns more than one result. The first result variable should be
Comments      1.    placed to the left of the = sign (lvalue). Additional result variables should be
                    passed as parameters.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_c32_a8_4op_vuX
name
Spec syntax   movv {Qop, vuX [,u]} vc0, a8

Return type   int

              1     VUX            uint8     0..3             Determines the source VCU
                                                              Coefficient operand (register vc0 is
              2     IN1_VC0        coef_t
                                                              expected)
                                                              Coefficient operand (register vc1 is
              3     IN2_VC1        coef_t
                                                              expected)
                                                              Coefficient operand (register vc2 is
              4     IN3_VC2        coef_t
                                                              expected)
Operands                                                      Coefficient operand (register vc3 is
              5     IN4_VC3        coef_t
                                                              expected)
                                                              Accumulator result operand (register a9 is
              6     RES2_A9        int32
                                                              expected)
                                                              Accumulator result operand (register a10
              7     RES3_A10       int32
                                                              is expected)

              8
                                                              Accumulator result operand (register a11
                    RES4_A11       int32
                                                              is expected)
              int accRes1;
              int accRes2;
              int accRes3;
              int accRes4;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              coef_t vcoefIn3;
              coef_t vcoefIn4;
              ...
              accRes1 = movv_c32_a8_4op_vuX (1, vcoefIn, vcoefIn2, vcoefIn3, vcoefIn4, accRes2, accRes3, accRes4);

                    This intrinsic returns more than one result. The first result variable should be

Comments      1.    placed to the left of the = sign (lvalue). Additional result variables should be
                    passed as parameters.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
Intrinsic     movv_c32_a8_4op_vuX_u
name
Spec syntax   movv {Qop, vuX [,u]} vc0, a8

Return type   int

              1     VUX            uint8     0..3            Determines the source VCU
                                                             Coefficient operand (register vc0 is
              2     IN1_VC0        coef_t
                                                             expected)
                                                             Coefficient operand (register vc1 is
              3     IN2_VC1        coef_t
                                                             expected)
                                                             Coefficient operand (register vc2 is
              4     IN3_VC2        coef_t
                                                             expected)
Operands                                                     Coefficient operand (register vc3 is
              5     IN4_VC3        coef_t
                                                             expected)
                                                             Accumulator result operand (register a9 is
              6     RES2_A9        int32
                                                             expected)
                                                             Accumulator result operand (register a10
              7     RES3_A10       int32
                                                             is expected)
                                                             Accumulator result operand (register a11
              8     RES4_A11       int32
                                                             is expected)
              int accRes1;
              int accRes2;
              int accRes3;
              int accRes4;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              coef_t vcoefIn3;
              coef_t vcoefIn4;
              ...
              accRes1 = movv_c32_a8_4op_vuX_u (1, vcoefIn, vcoefIn2, vcoefIn3, vcoefIn4, accRes2, accRes3,
              accRes4);

                    This intrinsic returns more than one result. The first result variable should be
Comments      1.    placed to the left of the = sign (lvalue). Additional result variables should be

passed as parameters.


Main table → Move And Pack → Move Vector Data to GCU → Move Vector Data to GCU
