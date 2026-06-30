# Move And Pack → Move → Vector Move Accumulator

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Move And Pack → Move → Vector Move Accumulator

Vector Move Accumulator

Vector Move Accumulator
Performs data move from source to destination. The source is a GCU 32-bit accumulator. The
destination is 32-bit wide.
Available Switches
      Number of atomic operations. An atomic operation is defined as a single move operation.
Oop
      1op ≤ Oop ≤ 8op
      Number of atomic operations. An atomic operation is defined as a single move operation.
Qop
      1op ≤ Qop ≤ 4op
vuX Determines the destination VCU of the instruction. X is replaced by 0 or 1.
Intrinsic Names
vmova_a20_c32_1op
vmova_a20_c32_2op
vmova_a20_c32_3op
vmova_a20_c32_4op
vmova_a0_modv0
vmova_a0_modv2
vmova_a0_v32_1op
vmova_a0_v32_2op
vmova_a0_v32_3op
vmova_a0_v32_4op
vmova_a0_v32_5op
vmova_a0_v32_6op
vmova_a0_v32_7op
vmova_a0_v32_8op
vmova_a16_v32_1op
vmova_a16_v32_2op
vmova_a16_v32_3op
vmova_a16_v32_4op
vmova_a16_v32_5op
vmova_a16_v32_6op
vmova_a16_v32_7op
vmova_a16_v32_8op
vmova_a16_c32_1op
vmova_a16_c32_2op
vmova_a16_c32_3op
vmova_a16_c32_4op
vmova_a0_c32_1op_vuX
vmova_a0_c32_2op_vuX
vmova_a0_c32_3op_vuX
vmova_a0_c32_4op_vuX
vmova_a16_c32_1op_vuX
vmova_a16_c32_2op_vuX
vmova_a16_c32_3op_vuX
vmova_a16_c32_4op_vuX
vmova_a4_c32_1op
vmova_a4_c32_2op
vmova_a4_c32_3op
vmova_a4_c32_4op
vmova_acc_c32_vuX

vmova_a20_c32_1op_vuX
vmova_a20_c32_2op_vuX
vmova_a20_c32_3op_vuX
vmova_a20_c32_4op_vuX
vmova_a8_c32_1op_vuX
vmova_a8_c32_2op_vuX
vmova_a8_c32_3op_vuX
vmova_a8_c32_4op_vuX
vmova_a8_modv0
vmova_a8_modv2
vmova_a16_v32_1op_vuX
vmova_a16_v32_2op_vuX
vmova_a16_v32_3op_vuX
vmova_a16_v32_4op_vuX
vmova_a16_v32_5op_vuX
vmova_a16_v32_6op_vuX
vmova_a16_v32_7op_vuX
vmova_a16_v32_8op_vuX
vmova_a0_c32_1op
vmova_a0_c32_2op
vmova_a0_c32_3op
vmova_a0_c32_4op
vmova_a8_v32_1op_vuX
vmova_a8_v32_2op_vuX
vmova_a8_v32_3op_vuX
vmova_a8_v32_4op_vuX
vmova_a8_v32_5op_vuX
vmova_a8_v32_6op_vuX
vmova_a8_v32_7op_vuX
vmova_a8_v32_8op_vuX
vmova_a8_c32_1op
vmova_a8_c32_2op
vmova_a8_c32_3op
vmova_a8_c32_4op
vmova_a12_c32_1op
vmova_a12_c32_2op
vmova_a12_c32_3op
vmova_a12_c32_4op
vmova_a8_v32_1op
vmova_a8_v32_2op
vmova_a8_v32_3op
vmova_a8_v32_4op
vmova_a8_v32_5op
vmova_a8_v32_6op
vmova_a8_v32_7op
vmova_a8_v32_8op
vmova_a12_c32_1op_vuX
vmova_a12_c32_2op_vuX
vmova_a12_c32_3op_vuX
vmova_a12_c32_4op_vuX
vmova_a0_v32_1op_vuX
vmova_a0_v32_2op_vuX
vmova_a0_v32_3op_vuX
vmova_a0_v32_4op_vuX
vmova_a0_v32_5op_vuX
vmova_a0_v32_6op_vuX
vmova_a0_v32_7op_vuX
vmova_a0_v32_8op_vuX
vmova_a4_c32_1op_vuX
vmova_a4_c32_2op_vuX
vmova_a4_c32_3op_vuX
vmova_a4_c32_4op_vuX
Instruction details in the instruction set specification
Intrinsic     vmova_a20_c32_1op[_p]
name
Spec syntax   vmova {Qop} a20, vc0, ?vprX

Return type   coef_t


              1
                                                             Accumulator operand (register a20 is
                   IN1_A20        int32
Operands                                                     expected)
              2    IN_VPR         vprex_t                    Vector predicate operand
              int accIn;
              coef_t vcoefRes;
C example     vprex_t vecPred;
              ...
              vcoefRes = vmova_a20_c32_1op_p (accIn, vecPred);

              1.   IN_VPR last operand is relevant only for vmova_a20_c32_1op_p version.

Comments           When using movv/vmova intrinsics with high accumulators (a16-a23) in -
              2.   Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                   corresponding a16-a23 registers.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a20_c32_2op[_p]
name
Spec syntax   vmova {Qop} a20, vc0, ?vprX

Return type   coef_t

                                                             Accumulator operand (register a20 is

1    IN1_A20        int32
                                                             expected)
                                                             Accumulator operand (register a21 is
              2    IN2_A21        int32
Operands                                                     expected)
                                                             Coefficient result operand (register vc1 is
              3    RES2_VC1       coef_t
                                                             expected)
              4    IN_VPR         vprex_t                    Vector predicate operand
              int accIn;
              int accIn2;
              coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              vprex_t vecPred;
              ...
              vcoefRes1 = vmova_a20_c32_2op_p (accIn, accIn2, vcoefRes2, vecPred);

              1.   IN_VPR last operand is relevant only for vmova_a20_c32_2op_p version.

Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_VC1).
                   When using movv/vmova intrinsics with high accumulators (a16-a23) in -
              3.   Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                   corresponding a16-a23 registers.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a20_c32_3op[_p]
name
Spec syntax   vmova {Qop} a20, vc0, ?vprX

Return type   coef_t


              1
                                                              Accumulator operand (register a20 is
                   IN1_A20         int32
                                                              expected)
                                                              Accumulator operand (register a21 is
              2    IN2_A21         int32
                                                              expected)
                                                              Accumulator operand (register a22 is
              3    IN3_A22         int32
Operands                                                      expected)
                                                              Coefficient result operand (register vc1 is
              4    RES2_VC1        coef_t
                                                              expected)

Coefficient result operand (register vc2 is
              5    RES3_VC2        coef_t
                                                              expected)
              6    IN_VPR          vprex_t                    Vector predicate operand
              int accIn;
              int accIn2;
              int accIn3;
              coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              coef_t vcoefRes3;
              vprex_t vecPred;
              ...
              vcoefRes1 = vmova_a20_c32_3op_p (accIn, accIn2, accIn3, vcoefRes2, vcoefRes3, vecPred);

              1.   IN_VPR last operand is relevant only for vmova_a20_c32_3op_p version.
                   This intrinsic returns more than one result. The first result variable should be
              2.   placed to the left of the = sign (lvalue). Additional result variables should be
Comments           passed as parameters.
                   When using movv/vmova intrinsics with high accumulators (a16-a23) in -
              3.   Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                   corresponding a16-a23 registers.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a20_c32_4op[_p]
name
Spec syntax   vmova {Qop} a20, vc0, ?vprX
Return type   coef_t

                                                              Accumulator operand (register a20 is
              1    IN1_A20         int32
                                                              expected)

              2
                                                              Accumulator operand (register a21 is
                   IN2_A21         int32
                                                              expected)
                                                              Accumulator operand (register a22 is
              3    IN3_A22         int32
                                                              expected)
                                                              Accumulator operand (register a23 is
              4    IN4_A23         int32
Operands                                                      expected)
                                                              Coefficient result operand (register vc1 is
              5    RES2_VC1        coef_t
                                                              expected)
                                                              Coefficient result operand (register vc2 is

6    RES3_VC2        coef_t
                                                              expected)
                                                              Coefficient result operand (register vc3 is
              7    RES4_VC3        coef_t
                                                              expected)
              8    IN_VPR          vprex_t                    Vector predicate operand
              int accIn;
              int accIn2;
              int accIn3;
              int accIn4;
              coef_t vcoefRes1;
              coef_t vcoefRes2;
C example     coef_t vcoefRes3;
              coef_t vcoefRes4;
              vprex_t vecPred;
              ...
              vcoefRes1 = vmova_a20_c32_4op_p (accIn, accIn2, accIn3, accIn4, vcoefRes2, vcoefRes3, vcoefRes4,
              vecPred);

              1.   IN_VPR last operand is relevant only for vmova_a20_c32_4op_p version.
                   This intrinsic returns more than one result. The first result variable should be
              2.   placed to the left of the = sign (lvalue). Additional result variables should be
Comments           passed as parameters.
                   When using movv/vmova intrinsics with high accumulators (a16-a23) in -
              3.   Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                   corresponding a16-a23 registers.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a0_modv0
name
Spec syntax   vmova a0, modv0

Return type   void

                                          Accumulator operand (register a0 is
Operands      1      IN1_A0      int32
                                          expected)
              int accIn;
C example     ...
              vmova_a0_modv0(accIn);

Comments


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a0_modv2
name
Spec syntax   vmova a0, modv2

Return type   void

                                          Accumulator operand (register a0 is
Operands      1      IN1_A0      int32
                                          expected)
              int accIn;
C example     ...
              vmova_a0_modv2(accIn);

Comments


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a0_v32_1op[_p]
name
Spec syntax   vmova {Oop} a0, vz[0], ?vprX

Return type   vec_t


              1
                                                             Accumulator operand (register a0 is

IN1_A0         int32
Operands                                                     expected)
              2    IN_VPR         vprex_t                    Vector predicate operand
              int accIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmova_a0_v32_1op_p (accIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmova_a0_v32_1op_p version.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a0_v32_2op[_p]
name
Spec syntax   vmova {Oop} a0, vz[0], ?vprX

Return type   vec_t

                                                             Accumulator operand (register a0 is
              1    IN1_A0         int32
                                                             expected)
Operands                                                     Accumulator operand (register a1 is
              2    IN2_A1         int32
                                                             expected)
              3    IN_VPR         vprex_t                    Vector predicate operand
              int accIn;
              int accIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmova_a0_v32_2op_p (accIn, accIn2, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmova_a0_v32_2op_p version.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a0_v32_3op[_p]
name
Spec syntax   vmova {Oop} a0, vz[0], ?vprX

Return type   vec_t

                                                             Accumulator operand (register a0 is
Operands      1    IN1_A0         int32
                                                             expected)
                                                              Accumulator operand (register a1 is
              2    IN2_A1          int32
                                                              expected)
                                                              Accumulator operand (register a2 is
              3    IN3_A2          int32
                                                              expected)
              4    IN_VPR          vprex_t                    Vector predicate operand
              int accIn;
              int accIn2;
              int accIn3;
C example     vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmova_a0_v32_3op_p (accIn, accIn2, accIn3, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmova_a0_v32_3op_p version.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a0_v32_4op[_p]
name
Spec syntax   vmova {Oop} a0, vz[0], ?vprX

Return type   vec_t


              1
                                                              Accumulator operand (register a0 is
                   IN1_A0          int32
                                                              expected)
                                                              Accumulator operand (register a1 is
              2    IN2_A1          int32
                                                              expected)
Operands                                                      Accumulator operand (register a2 is
              3    IN3_A2          int32
                                                              expected)
                                                              Accumulator operand (register a3 is
              4    IN4_A3          int32
                                                              expected)
              5    IN_VPR          vprex_t                    Vector predicate operand
              int accIn;
              int accIn2;
              int accIn3;
              int accIn4;
C example     vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmova_a0_v32_4op_p (accIn, accIn2, accIn3, accIn4, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmova_a0_v32_4op_p version.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a0_v32_5op[_p]
name
Spec syntax   vmova {Oop} a0, vz[0], ?vprX
Return type   vec_t

                                                              Accumulator operand (register a0 is
              1    IN1_A0          int32
                                                              expected)

              2
                                                              Accumulator operand (register a1 is
                   IN2_A1          int32
                                                              expected)
                                                              Accumulator operand (register a2 is
              3    IN3_A2          int32
Operands                                                      expected)
                                                              Accumulator operand (register a3 is

4    IN4_A3          int32
                                                              expected)
                                                              Accumulator operand (register a4 is
              5    IN5_A4          int32
                                                              expected)
              6    IN_VPR          vprex_t                    Vector predicate operand
              int accIn;
              int accIn2;
              int accIn3;
              int accIn4;
C example     int accIn5;
              vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmova_a0_v32_5op_p (accIn, accIn2, accIn3, accIn4, accIn5, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmova_a0_v32_5op_p version.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a0_v32_6op[_p]
name
Spec syntax   vmova {Oop} a0, vz[0], ?vprX

Return type   vec_t

                                                              Accumulator operand (register a0 is
              1    IN1_A0          int32
                                                              expected)
                                                              Accumulator operand (register a1 is
              2    IN2_A1          int32
                                                              expected)
                                                              Accumulator operand (register a2 is
              3    IN3_A2          int32
                                                              expected)
Operands
                                                              Accumulator operand (register a3 is
              4    IN4_A3          int32
                                                              expected)

              5
                                                              Accumulator operand (register a4 is
                   IN5_A4          int32
                                                              expected)
                                                              Accumulator operand (register a5 is
              6    IN6_A5          int32
                                                              expected)
              7    IN_VPR          vprex_t                     Vector predicate operand
              int accIn;
              int accIn2;
              int accIn3;
              int accIn4;
              int accIn5;
C example     int accIn6;

vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmova_a0_v32_6op_p (accIn, accIn2, accIn3, accIn4, accIn5, accIn6, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmova_a0_v32_6op_p version.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a0_v32_7op[_p]
name
Spec syntax   vmova {Oop} a0, vz[0], ?vprX

Return type   vec_t


              1
                                                               Accumulator operand (register a0 is
                   IN1_A0          int32
                                                               expected)
                                                               Accumulator operand (register a1 is
              2    IN2_A1          int32
                                                               expected)
                                                               Accumulator operand (register a2 is
              3    IN3_A2          int32
                                                               expected)
                                                               Accumulator operand (register a3 is
              4    IN4_A3          int32
Operands                                                       expected)
                                                               Accumulator operand (register a4 is
              5    IN5_A4          int32
                                                               expected)
                                                               Accumulator operand (register a5 is
              6    IN6_A5          int32
                                                               expected)
                                                               Accumulator operand (register a6 is
              7    IN7_A6          int32
                                                               expected)
              8    IN_VPR          vprex_t                     Vector predicate operand
              int accIn;
              int accIn2;
              int accIn3;
              int accIn4;
              int accIn5;
C example     int accIn6;
              int accIn7;
              vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmova_a0_v32_7op_p (accIn, accIn2, accIn3, accIn4, accIn5, accIn6, accIn7, vecPred);
Comments      1.   IN_VPR last operand is relevant only for vmova_a0_v32_7op_p version.

Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a0_v32_8op[_p]
name
Spec syntax   vmova {Oop} a0, vz[0], ?vprX

Return type   vec_t


              1
                                                               Accumulator operand (register a0 is
                   IN1_A0          int32
                                                               expected)
                                                               Accumulator operand (register a1 is
              2    IN2_A1          int32
                                                               expected)
                                                               Accumulator operand (register a2 is
              3    IN3_A2          int32
                                                               expected)
                                                               Accumulator operand (register a3 is
              4    IN4_A3          int32
                                                               expected)
Operands                                                       Accumulator operand (register a4 is
              5    IN5_A4          int32
                                                               expected)

              6
                                                               Accumulator operand (register a5 is
                   IN6_A5          int32
                                                               expected)
                                                               Accumulator operand (register a6 is
              7    IN7_A6          int32
                                                               expected)
                                                               Accumulator operand (register a7 is
              8    IN8_A7          int32
                                                               expected)
              9    IN_VPR          vprex_t                     Vector predicate operand
              int accIn;
              int accIn2;
              int accIn3;
              int accIn4;
              int accIn5;
              int accIn6;
C example     int accIn7;
              int accIn8;
              vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmova_a0_v32_8op_p (accIn, accIn2, accIn3, accIn4, accIn5, accIn6, accIn7, accIn8, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmova_a0_v32_8op_p version.

Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a16_v32_1op[_p]
name
Spec syntax   vmova {Oop} a16, vz[0], ?vprX

Return type   vec_t


              1
                                                             Accumulator operand (register a16 is
                   IN1_A16        int32
Operands                                                     expected)
              2    IN_VPR         vprex_t                    Vector predicate operand
              int accIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmova_a16_v32_1op_p (accIn, vecPred);

              1.   IN_VPR last operand is relevant only for vmova_a16_v32_1op_p version.

Comments           When using movv/vmova intrinsics with high accumulators (a16-a23) in -
              2.   Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                   corresponding a16-a23 registers.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a16_v32_2op[_p]
name
Spec syntax   vmova {Oop} a16, vz[0], ?vprX

Return type   vec_t

                                                             Accumulator operand (register a16 is
              1    IN1_A16        int32
                                                             expected)
Operands                                                     Accumulator operand (register a17 is
              2    IN2_A17        int32
                                                             expected)
              3    IN_VPR         vprex_t                    Vector predicate operand
              int accIn;
              int accIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmova_a16_v32_2op_p (accIn, accIn2, vecPred);

              1.   IN_VPR last operand is relevant only for vmova_a16_v32_2op_p version.

Comments           When using movv/vmova intrinsics with high accumulators (a16-a23) in -
              2.   Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                   corresponding a16-a23 registers.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a16_v32_3op[_p]
name
Spec syntax   vmova {Oop} a16, vz[0], ?vprX

Return type   vec_t


              1
                                                             Accumulator operand (register a16 is
                   IN1_A16        int32

expected)
                                                             Accumulator operand (register a17 is
              2    IN2_A17        int32
Operands                                                     expected)
                                                             Accumulator operand (register a18 is
              3    IN3_A18        int32
                                                             expected)
              4    IN_VPR         vprex_t                    Vector predicate operand
              int accIn;
              int accIn2;
              int accIn3;
C example     vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmova_a16_v32_3op_p (accIn, accIn2, accIn3, vecPred);

              1.   IN_VPR last operand is relevant only for vmova_a16_v32_3op_p version.

Comments           When using movv/vmova intrinsics with high accumulators (a16-a23) in -
              2.   Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                   corresponding a16-a23 registers.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a16_v32_4op[_p]
name
Spec syntax   vmova {Oop} a16, vz[0], ?vprX

Return type   vec_t

                                                             Accumulator operand (register a16 is
              1    IN1_A16        int32
                                                             expected)

              2
                                                             Accumulator operand (register a17 is
                   IN2_A17        int32
                                                             expected)
Operands                                                     Accumulator operand (register a18 is
              3    IN3_A18        int32
                                                             expected)
                                                             Accumulator operand (register a19 is
              4    IN4_A19        int32
                                                             expected)
              5    IN_VPR         vprex_t                    Vector predicate operand
              int accIn;
              int accIn2;
C example     int accIn3;
              int accIn4;
              vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmova_a16_v32_4op_p (accIn, accIn2, accIn3, accIn4, vecPred);

1.   IN_VPR last operand is relevant only for vmova_a16_v32_4op_p version.

Comments           When using movv/vmova intrinsics with high accumulators (a16-a23) in -
              2.   Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                   corresponding a16-a23 registers.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a16_v32_5op[_p]
name
Spec syntax   vmova {Oop} a16, vz[0], ?vprX

Return type   vec_t

                                                              Accumulator operand (register a16 is
              1    IN1_A16         int32
                                                              expected)
                                                              Accumulator operand (register a17 is
              2    IN2_A17         int32
                                                              expected)
                                                              Accumulator operand (register a18 is
              3    IN3_A18         int32
Operands                                                      expected)

              4
                                                              Accumulator operand (register a19 is
                   IN4_A19         int32
                                                              expected)
                                                              Accumulator operand (register a20 is
              5    IN5_A20         int32
                                                              expected)
              6    IN_VPR          vprex_t                    Vector predicate operand
              int accIn;
              int accIn2;
              int accIn3;
              int accIn4;
C example     int accIn5;
              vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmova_a16_v32_5op_p (accIn, accIn2, accIn3, accIn4, accIn5, vecPred);

              1.   IN_VPR last operand is relevant only for vmova_a16_v32_5op_p version.

Comments           When using movv/vmova intrinsics with high accumulators (a16-a23) in -
              2.   Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                   corresponding a16-a23 registers.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a16_v32_6op[_p]
name
Spec syntax   vmova {Oop} a16, vz[0], ?vprX

Return type   vec_t


              1

Accumulator operand (register a16 is
                   IN1_A16         int32
                                                               expected)
                                                               Accumulator operand (register a17 is
              2    IN2_A17         int32
                                                               expected)
                                                               Accumulator operand (register a18 is
              3    IN3_A18         int32
                                                               expected)
Operands                                                       Accumulator operand (register a19 is
              4    IN4_A19         int32
                                                               expected)
                                                               Accumulator operand (register a20 is
              5    IN5_A20         int32
                                                               expected)
                                                               Accumulator operand (register a21 is
              6    IN6_A21         int32
                                                               expected)
              7    IN_VPR          vprex_t                     Vector predicate operand
              int accIn;
              int accIn2;
              int accIn3;
              int accIn4;
              int accIn5;
C example     int accIn6;
              vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmova_a16_v32_6op_p (accIn, accIn2, accIn3, accIn4, accIn5, accIn6, vecPred);

              1.   IN_VPR last operand is relevant only for vmova_a16_v32_6op_p version.

Comments           When using movv/vmova intrinsics with high accumulators (a16-a23) in -
              2.   Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                   corresponding a16-a23 registers.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a16_v32_7op[_p]
name
Spec syntax   vmova {Oop} a16, vz[0], ?vprX

Return type   vec_t

                                                               Accumulator operand (register a16 is
              1    IN1_A16         int32
                                                               expected)
Operands                                                       Accumulator operand (register a17 is
              2    IN2_A17         int32

expected)
              3    IN3_A18         int32                       Accumulator operand (register a18 is
                                                               expected)
                                                               Accumulator operand (register a19 is
              4    IN4_A19         int32
                                                               expected)

              5
                                                               Accumulator operand (register a20 is
                   IN5_A20         int32
                                                               expected)
                                                               Accumulator operand (register a21 is
              6    IN6_A21         int32
                                                               expected)
                                                               Accumulator operand (register a22 is
              7    IN7_A22         int32
                                                               expected)
              8    IN_VPR          vprex_t                     Vector predicate operand
              int accIn;
              int accIn2;
              int accIn3;
              int accIn4;
              int accIn5;
C example     int accIn6;
              int accIn7;
              vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmova_a16_v32_7op_p (accIn, accIn2, accIn3, accIn4, accIn5, accIn6, accIn7, vecPred);

              1.   IN_VPR last operand is relevant only for vmova_a16_v32_7op_p version.

Comments           When using movv/vmova intrinsics with high accumulators (a16-a23) in -
              2.   Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                   corresponding a16-a23 registers.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a16_v32_8op[_p]
name
Spec syntax   vmova {Oop} a16, vz[0], ?vprX

Return type   vec_t

                                                               Accumulator operand (register a16 is
              1    IN1_A16         int32
                                                               expected)

              2
                                                               Accumulator operand (register a17 is
                   IN2_A17         int32
                                                               expected)

Accumulator operand (register a18 is
Operands      3    IN3_A18         int32
                                                               expected)
                                                               Accumulator operand (register a19 is
              4    IN4_A19         int32
                                                               expected)
                                                               Accumulator operand (register a20 is
              5    IN5_A20         int32
                                                               expected)
                                                             Accumulator operand (register a21 is
            6    IN6_A21         int32
                                                             expected)
                                                             Accumulator operand (register a22 is
            7    IN7_A22         int32
                                                             expected)

            8
                                                             Accumulator operand (register a23 is
                 IN8_A23         int32
                                                             expected)
            9    IN_VPR          vprex_t                     Vector predicate operand
            int accIn;
            int accIn2;
            int accIn3;
            int accIn4;
            int accIn5;
            int accIn6;
C example   int accIn7;
            int accIn8;
            vec_t vRes;
            vprex_t vecPred;
            ...
            vRes = vmova_a16_v32_8op_p (accIn, accIn2, accIn3, accIn4, accIn5, accIn6, accIn7, accIn8, vecPred);

            1.   IN_VPR last operand is relevant only for vmova_a16_v32_8op_p version.

Comments         When using movv/vmova intrinsics with high accumulators (a16-a23) in -
            2.   Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                 corresponding a16-a23 registers.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a16_c32_1op[_p]
name
Spec syntax   vmova {Qop} a16, vc0, ?vprX

Return type   coef_t


              1
                                                             Accumulator operand (register a16 is
                   IN1_A16        int32
Operands                                                     expected)
              2    IN_VPR         vprex_t                    Vector predicate operand

int accIn;
              coef_t vcoefRes;
C example     vprex_t vecPred;
              ...
              vcoefRes = vmova_a16_c32_1op_p (accIn, vecPred);

              1.   IN_VPR last operand is relevant only for vmova_a16_c32_1op_p version.

Comments           When using movv/vmova intrinsics with high accumulators (a16-a23) in -
              2.   Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                   corresponding a16-a23 registers.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a16_c32_2op[_p]
name
Spec syntax   vmova {Qop} a16, vc0, ?vprX

Return type   coef_t

                                                             Accumulator operand (register a16 is
              1    IN1_A16        int32
                                                             expected)
                                                             Accumulator operand (register a17 is
              2    IN2_A17        int32
Operands                                                     expected)
                                                             Coefficient result operand (register vc1 is
              3    RES2_VC1       coef_t
                                                             expected)
              4    IN_VPR         vprex_t                    Vector predicate operand
              int accIn;
              int accIn2;
              coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              vprex_t vecPred;
              ...
              vcoefRes1 = vmova_a16_c32_2op_p (accIn, accIn2, vcoefRes2, vecPred);

              1.   IN_VPR last operand is relevant only for vmova_a16_c32_2op_p version.

Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_VC1).
                   When using movv/vmova intrinsics with high accumulators (a16-a23) in -
              3.   Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                   corresponding a16-a23 registers.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a16_c32_3op[_p]
name
Spec syntax   vmova {Qop} a16, vc0, ?vprX

Return type   coef_t


              1
                                                              Accumulator operand (register a16 is

IN1_A16         int32
                                                              expected)
                                                              Accumulator operand (register a17 is
              2    IN2_A17         int32
                                                              expected)
                                                              Accumulator operand (register a18 is
              3    IN3_A18         int32
Operands                                                      expected)
                                                              Coefficient result operand (register vc1 is
              4    RES2_VC1        coef_t
                                                              expected)
                                                              Coefficient result operand (register vc2 is
              5    RES3_VC2        coef_t
                                                              expected)
              6    IN_VPR          vprex_t                    Vector predicate operand
              int accIn;
              int accIn2;
              int accIn3;
              coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              coef_t vcoefRes3;
              vprex_t vecPred;
              ...
              vcoefRes1 = vmova_a16_c32_3op_p (accIn, accIn2, accIn3, vcoefRes2, vcoefRes3, vecPred);

              1.   IN_VPR last operand is relevant only for vmova_a16_c32_3op_p version.
                   This intrinsic returns more than one result. The first result variable should be
              2.   placed to the left of the = sign (lvalue). Additional result variables should be
Comments           passed as parameters.
                   When using movv/vmova intrinsics with high accumulators (a16-a23) in -
              3.   Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                   corresponding a16-a23 registers.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a16_c32_4op[_p]
name
Spec syntax   vmova {Qop} a16, vc0, ?vprX
Return type   coef_t

                                                              Accumulator operand (register a16 is
              1    IN1_A16         int32
                                                              expected)

              2
                                                              Accumulator operand (register a17 is
                   IN2_A17         int32

expected)
                                                              Accumulator operand (register a18 is
              3    IN3_A18         int32
                                                              expected)
                                                              Accumulator operand (register a19 is
              4    IN4_A19         int32
Operands                                                      expected)
                                                              Coefficient result operand (register vc1 is
              5    RES2_VC1        coef_t
                                                              expected)
                                                              Coefficient result operand (register vc2 is
              6    RES3_VC2        coef_t
                                                              expected)
                                                              Coefficient result operand (register vc3 is
              7    RES4_VC3        coef_t
                                                              expected)
              8    IN_VPR          vprex_t                    Vector predicate operand
              int accIn;
              int accIn2;
              int accIn3;
              int accIn4;
              coef_t vcoefRes1;
              coef_t vcoefRes2;
C example     coef_t vcoefRes3;
              coef_t vcoefRes4;
              vprex_t vecPred;
              ...
              vcoefRes1 = vmova_a16_c32_4op_p (accIn, accIn2, accIn3, accIn4, vcoefRes2, vcoefRes3, vcoefRes4,
              vecPred);

              1.   IN_VPR last operand is relevant only for vmova_a16_c32_4op_p version.
                   This intrinsic returns more than one result. The first result variable should be
              2.   placed to the left of the = sign (lvalue). Additional result variables should be
Comments           passed as parameters.
                   When using movv/vmova intrinsics with high accumulators (a16-a23) in -
              3.   Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                   corresponding a16-a23 registers.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a0_c32_1op_vuX[_p]
name
Spec syntax   vmova {Qop, vuX} a0, vc0, ?vprX

Return type   coef_t

              1    VUX            uint8     0..3             Determines the destination VCU

Accumulator operand (register a0 is
Operands      2    IN1_A0         int32
                                                             expected)
              3    IN_VPR         vprex_t                    Vector predicate operand
              int accIn;
              coef_t vcoefRes;
C example     vprex_t vecPred;
              ...
              vcoefRes = vmova_a0_c32_1op_vuX_p (1, accIn, vecPred);

                   IN_VPR last operand is relevant only for vmova_a0_c32_1op_vuX_p
Comments      1.
                   version.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a0_c32_2op_vuX[_p]
name
Spec syntax   vmova {Qop, vuX} a0, vc0, ?vprX

Return type   coef_t

              1    VUX            uint8     0..3             Determines the destination VCU
                                                             Accumulator operand (register a0 is
              2    IN1_A0         int32
                                                             expected)
                                                             Accumulator operand (register a1 is
Operands      3    IN2_A1         int32
                                                             expected)
                                                             Coefficient result operand (register vc1 is
              4    RES2_VC1       coef_t
                                                             expected)
              5    IN_VPR         vprex_t                    Vector predicate operand
              int accIn;
              int accIn2;
              coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              vprex_t vecPred;
              ...
              vcoefRes1 = vmova_a0_c32_2op_vuX_p (1, accIn, accIn2, vcoefRes2, vecPred);

                   IN_VPR last operand is relevant only for vmova_a0_c32_2op_vuX_p
              1.
                   version.
Comments
                   This intrinsic returns two results. The first result variable should be placed to
              2.
                   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_VC1).


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a0_c32_3op_vuX[_p]
name
Spec syntax   vmova {Qop, vuX} a0, vc0, ?vprX

Return type   coef_t

              1    VUX             uint8     0..3            Determines the destination VCU

Accumulator operand (register a0 is
              2    IN1_A0          int32
                                                             expected)
                                                             Accumulator operand (register a1 is
              3    IN2_A1          int32
                                                             expected)
                                                             Accumulator operand (register a2 is
Operands      4    IN3_A2          int32
                                                             expected)
                                                             Coefficient result operand (register vc1 is
              5    RES2_VC1        coef_t
                                                             expected)

              6
                                                             Coefficient result operand (register vc2 is
                   RES3_VC2        coef_t
                                                             expected)
              7    IN_VPR          vprex_t                   Vector predicate operand
              int accIn;
              int accIn2;
              int accIn3;
              coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              coef_t vcoefRes3;
              vprex_t vecPred;
              ...
              vcoefRes1 = vmova_a0_c32_3op_vuX_p (1, accIn, accIn2, accIn3, vcoefRes2, vcoefRes3, vecPred);

                   IN_VPR last operand is relevant only for vmova_a0_c32_3op_vuX_p
              1.
                   version.
Comments           This intrinsic returns more than one result. The first result variable should be
              2.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a0_c32_4op_vuX[_p]
name
Spec syntax   vmova {Qop, vuX} a0, vc0, ?vprX

Return type   coef_t

Operands      1    VUX             uint8     0..3            Determines the destination VCU
                                                           Accumulator operand (register a0 is
            2    IN1_A0          int32
                                                           expected)
                                                           Accumulator operand (register a1 is
            3    IN2_A1          int32
                                                           expected)

            4

Accumulator operand (register a2 is
                 IN3_A2          int32
                                                           expected)
                                                           Accumulator operand (register a3 is
            5    IN4_A3          int32
                                                           expected)
                                                           Coefficient result operand (register vc1 is
            6    RES2_VC1        coef_t
                                                           expected)
                                                           Coefficient result operand (register vc2 is
            7    RES3_VC2        coef_t
                                                           expected)
                                                           Coefficient result operand (register vc3 is
            8    RES4_VC3        coef_t
                                                           expected)
            9    IN_VPR          vprex_t                   Vector predicate operand
            int accIn;
            int accIn2;
            int accIn3;
            int accIn4;
            coef_t vcoefRes1;
            coef_t vcoefRes2;
C example   coef_t vcoefRes3;
            coef_t vcoefRes4;
            vprex_t vecPred;
            ...
            vcoefRes1 = vmova_a0_c32_4op_vuX_p (1, accIn, accIn2, accIn3, accIn4, vcoefRes2, vcoefRes3,
            vcoefRes4, vecPred);

                 IN_VPR last operand is relevant only for vmova_a0_c32_4op_vuX_p
            1.
                 version.
Comments         This intrinsic returns more than one result. The first result variable should be
            2.   placed to the left of the = sign (lvalue). Additional result variables should be
                 passed as parameters.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a16_c32_1op_vuX[_p]
name
Spec syntax   vmova {Qop, vuX} a16, vc0, ?vprX

Return type   coef_t

              1    VUX            uint8     0..3             Determines the destination VCU
                                                             Accumulator operand (register a16 is
Operands      2    IN1_A16        int32
                                                             expected)
              3    IN_VPR         vprex_t                    Vector predicate operand
              int accIn;
              coef_t vcoefRes;
C example     vprex_t vecPred;
              ...

vcoefRes = vmova_a16_c32_1op_vuX_p (1, accIn, vecPred);

                   IN_VPR last operand is relevant only for vmova_a16_c32_1op_vuX_p
              1.
                   version.
Comments           When using movv/vmova intrinsics with high accumulators (a16-a23) in -
              2.   Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                   corresponding a16-a23 registers.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a16_c32_2op_vuX[_p]
name
Spec syntax   vmova {Qop, vuX} a16, vc0, ?vprX

Return type   coef_t

              1    VUX            uint8     0..3             Determines the destination VCU
                                                             Accumulator operand (register a16 is
              2    IN1_A16        int32
                                                             expected)
                                                             Accumulator operand (register a17 is
Operands      3    IN2_A17        int32
                                                             expected)
                                                             Coefficient result operand (register vc1 is
              4    RES2_VC1       coef_t
                                                             expected)
              5    IN_VPR         vprex_t                    Vector predicate operand
              int accIn;
              int accIn2;
              coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              vprex_t vecPred;
              ...
              vcoefRes1 = vmova_a16_c32_2op_vuX_p (1, accIn, accIn2, vcoefRes2, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmova_a16_c32_2op_vuX_p
                   version.
                   This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_VC1).
                   When using movv/vmova intrinsics with high accumulators (a16-a23) in -
              3.   Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                   corresponding a16-a23 registers.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a16_c32_3op_vuX[_p]
name
Spec syntax   vmova {Qop, vuX} a16, vc0, ?vprX

Return type   coef_t

1    VUX            uint8     0..3             Determines the destination VCU
                                                             Accumulator operand (register a16 is
              2    IN1_A16        int32
                                                             expected)
                                                             Accumulator operand (register a17 is
              3    IN2_A17        int32
                                                             expected)
                                                             Accumulator operand (register a18 is
Operands      4    IN3_A18        int32
                                                             expected)
                                                             Coefficient result operand (register vc1 is
              5    RES2_VC1       coef_t
                                                             expected)
                                                             Coefficient result operand (register vc2 is
              6    RES3_VC2       coef_t
                                                             expected)
              7    IN_VPR         vprex_t                    Vector predicate operand
              int accIn;
              int accIn2;
              int accIn3;
              coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              coef_t vcoefRes3;
              vprex_t vecPred;
              ...
              vcoefRes1 = vmova_a16_c32_3op_vuX_p (1, accIn, accIn2, accIn3, vcoefRes2, vcoefRes3, vecPred);

                   IN_VPR last operand is relevant only for vmova_a16_c32_3op_vuX_p
              1.
                   version.
                   This intrinsic returns more than one result. The first result variable should be
Comments      2.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.
              3.   When using movv/vmova intrinsics with high accumulators (a16-a23) in -
                   Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                   corresponding a16-a23 registers.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a16_c32_4op_vuX[_p]
name
Spec syntax   vmova {Qop, vuX} a16, vc0, ?vprX

Return type   coef_t

              1    VUX             uint8     0..3            Determines the destination VCU

Accumulator operand (register a16 is
              2    IN1_A16         int32
                                                             expected)
                                                             Accumulator operand (register a17 is
              3    IN2_A17         int32
                                                             expected)
                                                             Accumulator operand (register a18 is
              4    IN3_A18         int32
                                                             expected)
                                                             Accumulator operand (register a19 is
Operands      5    IN4_A19         int32
                                                             expected)

              6
                                                             Coefficient result operand (register vc1 is
                   RES2_VC1        coef_t
                                                             expected)
                                                             Coefficient result operand (register vc2 is
              7    RES3_VC2        coef_t
                                                             expected)
                                                             Coefficient result operand (register vc3 is
              8    RES4_VC3        coef_t
                                                             expected)
              9    IN_VPR          vprex_t                   Vector predicate operand
              int accIn;
              int accIn2;
              int accIn3;
              int accIn4;
              coef_t vcoefRes1;
              coef_t vcoefRes2;
C example     coef_t vcoefRes3;
              coef_t vcoefRes4;
              vprex_t vecPred;
              ...
              vcoefRes1 = vmova_a16_c32_4op_vuX_p (1, accIn, accIn2, accIn3, accIn4, vcoefRes2, vcoefRes3,
              vcoefRes4, vecPred);

              1.
                   IN_VPR last operand is relevant only for vmova_a16_c32_4op_vuX_p
                   version.
Comments           This intrinsic returns more than one result. The first result variable should be
              2.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.
                When using movv/vmova intrinsics with high accumulators (a16-a23) in -

3.   Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                corresponding a16-a23 registers.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a4_c32_1op[_p]
name
Spec syntax   vmova {Qop} a4, vc0, ?vprX

Return type   coef_t


              1
                                                             Accumulator operand (register a4 is
                   IN1_A4         int32
Operands                                                     expected)
              2    IN_VPR         vprex_t                    Vector predicate operand
              int accIn;
              coef_t vcoefRes;
C example     vprex_t vecPred;
              ...
              vcoefRes = vmova_a4_c32_1op_p (accIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmova_a4_c32_1op_p version.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a4_c32_2op[_p]
name
Spec syntax   vmova {Qop} a4, vc0, ?vprX

Return type   coef_t

                                                             Accumulator operand (register a4 is
              1    IN1_A4         int32
                                                             expected)
                                                             Accumulator operand (register a5 is
              2    IN2_A5         int32
Operands                                                     expected)
                                                             Coefficient result operand (register vc1 is
              3    RES2_VC1       coef_t
                                                             expected)
              4    IN_VPR         vprex_t                    Vector predicate operand
              int accIn;
              int accIn2;
              coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              vprex_t vecPred;
              ...
              vcoefRes1 = vmova_a4_c32_2op_p (accIn, accIn2, vcoefRes2, vecPred);

              1.   IN_VPR last operand is relevant only for vmova_a4_c32_2op_p version.

Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_VC1).


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a4_c32_3op[_p]
name
Spec syntax   vmova {Qop} a4, vc0, ?vprX

Return type   coef_t


              1
                                                              Accumulator operand (register a4 is
                   IN1_A4          int32
                                                              expected)
                                                              Accumulator operand (register a5 is
              2    IN2_A5          int32
                                                              expected)
                                                              Accumulator operand (register a6 is
              3    IN3_A6          int32
Operands                                                      expected)
                                                              Coefficient result operand (register vc1 is
              4    RES2_VC1        coef_t
                                                              expected)
                                                              Coefficient result operand (register vc2 is
              5    RES3_VC2        coef_t
                                                              expected)
              6    IN_VPR          vprex_t                    Vector predicate operand
              int accIn;
              int accIn2;
              int accIn3;
              coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              coef_t vcoefRes3;
              vprex_t vecPred;
              ...
              vcoefRes1 = vmova_a4_c32_3op_p (accIn, accIn2, accIn3, vcoefRes2, vcoefRes3, vecPred);

              1.   IN_VPR last operand is relevant only for vmova_a4_c32_3op_p version.

Comments           This intrinsic returns more than one result. The first result variable should be
              2.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a4_c32_4op[_p]
name
Spec syntax   vmova {Qop} a4, vc0, ?vprX

Return type   coef_t

                                                              Accumulator operand (register a4 is
              1    IN1_A4          int32
                                                              expected)
                                                              Accumulator operand (register a5 is
Operands      2    IN2_A5          int32
                                                              expected)

              3

Accumulator operand (register a6 is
                   IN3_A6          int32
                                                              expected)
                                                            Accumulator operand (register a7 is
            4    IN4_A7          int32
                                                            expected)
                                                            Coefficient result operand (register vc1 is
            5    RES2_VC1        coef_t
                                                            expected)

            6
                                                            Coefficient result operand (register vc2 is
                 RES3_VC2        coef_t
                                                            expected)
                                                            Coefficient result operand (register vc3 is
            7    RES4_VC3        coef_t
                                                            expected)
            8    IN_VPR          vprex_t                    Vector predicate operand
            int accIn;
            int accIn2;
            int accIn3;
            int accIn4;
            coef_t vcoefRes1;
            coef_t vcoefRes2;
C example   coef_t vcoefRes3;
            coef_t vcoefRes4;
            vprex_t vecPred;
            ...
            vcoefRes1 = vmova_a4_c32_4op_p (accIn, accIn2, accIn3, accIn4, vcoefRes2, vcoefRes3, vcoefRes4,
            vecPred);

            1.   IN_VPR last operand is relevant only for vmova_a4_c32_4op_p version.

Comments         This intrinsic returns more than one result. The first result variable should be
            2.   placed to the left of the = sign (lvalue). Additional result variables should be
                 passed as parameters.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_acc_c32_vuX[_p]
name
Spec syntax   vmova {vuX} acX, vcZ, ?vprX

Return type   coef_t

              1    VUX            uint8     0..3            Determines the destination VCU
Operands      2    IN1_ACC        int32                     Accumulator operand
              3    IN_VPR         vprex_t                   Vector predicate operand
              int acc;
              coef_t vcoefRes;
C example     vprex_t vecPred;
              ...
              vcoefRes = vmova_acc_c32_vuX_p (1, acc, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmova_acc_c32_vuX_p version.

Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a20_c32_1op_vuX[_p]
name
Spec syntax   vmova {Qop, vuX} a20, vc0, ?vprX

Return type   coef_t

              1    VUX            uint8     0..3             Determines the destination VCU
                                                             Accumulator operand (register a20 is
Operands      2    IN1_A20        int32
                                                             expected)
              3    IN_VPR         vprex_t                    Vector predicate operand
              int accIn;
              coef_t vcoefRes;
C example     vprex_t vecPred;
              ...
              vcoefRes = vmova_a20_c32_1op_vuX_p (1, accIn, vecPred);

                   IN_VPR last operand is relevant only for vmova_a20_c32_1op_vuX_p
              1.
                   version.
Comments           When using movv/vmova intrinsics with high accumulators (a16-a23) in -
              2.   Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                   corresponding a16-a23 registers.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a20_c32_2op_vuX[_p]
name
Spec syntax   vmova {Qop, vuX} a20, vc0, ?vprX

Return type   coef_t

              1    VUX            uint8     0..3             Determines the destination VCU
                                                             Accumulator operand (register a20 is
              2    IN1_A20        int32
                                                             expected)
                                                             Accumulator operand (register a21 is
Operands      3    IN2_A21        int32
                                                             expected)
                                                             Coefficient result operand (register vc1 is
              4    RES2_VC1       coef_t
                                                             expected)
              5    IN_VPR         vprex_t                    Vector predicate operand
              int accIn;
              int accIn2;
              coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              vprex_t vecPred;
              ...
              vcoefRes1 = vmova_a20_c32_2op_vuX_p (1, accIn, accIn2, vcoefRes2, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmova_a20_c32_2op_vuX_p
                   version.

This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_VC1).
                   When using movv/vmova intrinsics with high accumulators (a16-a23) in -
              3.   Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                   corresponding a16-a23 registers.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a20_c32_3op_vuX[_p]
name
Spec syntax   vmova {Qop, vuX} a20, vc0, ?vprX

Return type   coef_t

              1    VUX            uint8     0..3             Determines the destination VCU
                                                             Accumulator operand (register a20 is
              2    IN1_A20        int32
                                                             expected)
                                                             Accumulator operand (register a21 is
              3    IN2_A21        int32
                                                             expected)
                                                             Accumulator operand (register a22 is
Operands      4    IN3_A22        int32
                                                             expected)
                                                             Coefficient result operand (register vc1 is
              5    RES2_VC1       coef_t
                                                             expected)
                                                             Coefficient result operand (register vc2 is
              6    RES3_VC2       coef_t
                                                             expected)
              7    IN_VPR         vprex_t                    Vector predicate operand
              int accIn;
              int accIn2;
              int accIn3;
              coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              coef_t vcoefRes3;
              vprex_t vecPred;
              ...
              vcoefRes1 = vmova_a20_c32_3op_vuX_p (1, accIn, accIn2, accIn3, vcoefRes2, vcoefRes3, vecPred);

                   IN_VPR last operand is relevant only for vmova_a20_c32_3op_vuX_p
              1.
                   version.
                   This intrinsic returns more than one result. The first result variable should be

Comments      2.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.
              3.   When using movv/vmova intrinsics with high accumulators (a16-a23) in -
                   Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                   corresponding a16-a23 registers.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a20_c32_4op_vuX[_p]
name
Spec syntax   vmova {Qop, vuX} a20, vc0, ?vprX

Return type   coef_t

              1    VUX             uint8     0..3            Determines the destination VCU
                                                             Accumulator operand (register a20 is
              2    IN1_A20         int32
                                                             expected)
                                                             Accumulator operand (register a21 is
              3    IN2_A21         int32
                                                             expected)
                                                             Accumulator operand (register a22 is
              4    IN3_A22         int32
                                                             expected)
                                                             Accumulator operand (register a23 is
Operands      5    IN4_A23         int32
                                                             expected)

              6
                                                             Coefficient result operand (register vc1 is
                   RES2_VC1        coef_t
                                                             expected)
                                                             Coefficient result operand (register vc2 is
              7    RES3_VC2        coef_t
                                                             expected)
                                                             Coefficient result operand (register vc3 is
              8    RES4_VC3        coef_t
                                                             expected)
              9    IN_VPR          vprex_t                   Vector predicate operand
              int accIn;
              int accIn2;
              int accIn3;
              int accIn4;
              coef_t vcoefRes1;
              coef_t vcoefRes2;
C example     coef_t vcoefRes3;
              coef_t vcoefRes4;

vprex_t vecPred;
              ...
              vcoefRes1 = vmova_a20_c32_4op_vuX_p (1, accIn, accIn2, accIn3, accIn4, vcoefRes2, vcoefRes3,
              vcoefRes4, vecPred);

              1.
                   IN_VPR last operand is relevant only for vmova_a20_c32_4op_vuX_p
                   version.
Comments           This intrinsic returns more than one result. The first result variable should be
              2.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.
                When using movv/vmova intrinsics with high accumulators (a16-a23) in -
           3.   Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                corresponding a16-a23 registers.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a8_c32_1op_vuX[_p]
name
Spec syntax   vmova {Qop, vuX} a8, vc0, ?vprX

Return type   coef_t

              1    VUX            uint8     0..3             Determines the destination VCU
                                                             Accumulator operand (register a8 is
Operands      2    IN1_A8         int32
                                                             expected)
              3    IN_VPR         vprex_t                    Vector predicate operand
              int accIn;
              coef_t vcoefRes;
C example     vprex_t vecPred;
              ...
              vcoefRes = vmova_a8_c32_1op_vuX_p (1, accIn, vecPred);

                   IN_VPR last operand is relevant only for vmova_a8_c32_1op_vuX_p
Comments      1.
                   version.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a8_c32_2op_vuX[_p]
name
Spec syntax   vmova {Qop, vuX} a8, vc0, ?vprX

Return type   coef_t

              1    VUX            uint8     0..3             Determines the destination VCU
                                                             Accumulator operand (register a8 is
              2    IN1_A8         int32
                                                             expected)
                                                             Accumulator operand (register a9 is
Operands      3    IN2_A9         int32
                                                             expected)
                                                             Coefficient result operand (register vc1 is
              4    RES2_VC1       coef_t

expected)
              5    IN_VPR         vprex_t                    Vector predicate operand
              int accIn;
              int accIn2;
              coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              vprex_t vecPred;
              ...
              vcoefRes1 = vmova_a8_c32_2op_vuX_p (1, accIn, accIn2, vcoefRes2, vecPred);

                   IN_VPR last operand is relevant only for vmova_a8_c32_2op_vuX_p
              1.
                   version.
Comments
                   This intrinsic returns two results. The first result variable should be placed to
              2.
                   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_VC1).


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a8_c32_3op_vuX[_p]
name
Spec syntax   vmova {Qop, vuX} a8, vc0, ?vprX

Return type   coef_t

              1    VUX             uint8     0..3            Determines the destination VCU
                                                             Accumulator operand (register a8 is
              2    IN1_A8          int32
                                                             expected)
                                                             Accumulator operand (register a9 is
              3    IN2_A9          int32
                                                             expected)
                                                             Accumulator operand (register a10 is
Operands      4    IN3_A10         int32
                                                             expected)
                                                             Coefficient result operand (register vc1 is
              5    RES2_VC1        coef_t
                                                             expected)

              6
                                                             Coefficient result operand (register vc2 is
                   RES3_VC2        coef_t
                                                             expected)
              7    IN_VPR          vprex_t                   Vector predicate operand
              int accIn;
              int accIn2;
              int accIn3;
              coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              coef_t vcoefRes3;
              vprex_t vecPred;
              ...

vcoefRes1 = vmova_a8_c32_3op_vuX_p (1, accIn, accIn2, accIn3, vcoefRes2, vcoefRes3, vecPred);

                   IN_VPR last operand is relevant only for vmova_a8_c32_3op_vuX_p
              1.
                   version.
Comments           This intrinsic returns more than one result. The first result variable should be
              2.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a8_c32_4op_vuX[_p]
name
Spec syntax   vmova {Qop, vuX} a8, vc0, ?vprX

Return type   coef_t

Operands      1    VUX             uint8     0..3            Determines the destination VCU
                                                           Accumulator operand (register a8 is
            2    IN1_A8          int32
                                                           expected)
                                                           Accumulator operand (register a9 is
            3    IN2_A9          int32
                                                           expected)

            4
                                                           Accumulator operand (register a10 is
                 IN3_A10         int32
                                                           expected)
                                                           Accumulator operand (register a11 is
            5    IN4_A11         int32
                                                           expected)
                                                           Coefficient result operand (register vc1 is
            6    RES2_VC1        coef_t
                                                           expected)
                                                           Coefficient result operand (register vc2 is
            7    RES3_VC2        coef_t
                                                           expected)
                                                           Coefficient result operand (register vc3 is
            8    RES4_VC3        coef_t
                                                           expected)
            9    IN_VPR          vprex_t                   Vector predicate operand
            int accIn;
            int accIn2;
            int accIn3;
            int accIn4;
            coef_t vcoefRes1;
            coef_t vcoefRes2;
C example   coef_t vcoefRes3;
            coef_t vcoefRes4;

vprex_t vecPred;
            ...
            vcoefRes1 = vmova_a8_c32_4op_vuX_p (1, accIn, accIn2, accIn3, accIn4, vcoefRes2, vcoefRes3,
            vcoefRes4, vecPred);

                 IN_VPR last operand is relevant only for vmova_a8_c32_4op_vuX_p
            1.
                 version.
Comments         This intrinsic returns more than one result. The first result variable should be
            2.   placed to the left of the = sign (lvalue). Additional result variables should be
                 passed as parameters.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a8_modv0
name
Spec syntax   vmova a8, modv0

Return type   void

                                          Accumulator operand (register a8 is
Operands      1      IN1_A8      int32
                                          expected)
              int accIn;
C example     ...
              vmova_a8_modv0(accIn);

Comments


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a8_modv2
name
Spec syntax   vmova a8, modv2

Return type   void

                                          Accumulator operand (register a8 is
Operands      1      IN1_A8      int32
                                          expected)
              int accIn;
C example     ...
              vmova_a8_modv2(accIn);

Comments


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a16_v32_1op_vuX[_p]
name
Spec syntax   vmova {Oop, vuX} a16, vz[0], ?vprX

Return type   vec_t

              1    VUX            uint8     0..3            Determines the destination VCU
                                                            Accumulator operand (register a16 is
Operands      2    IN1_A16        int32
                                                            expected)
              3    IN_VPR         vprex_t                   Vector predicate operand
              int accIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmova_a16_v32_1op_vuX_p (1, accIn, vecPred);

                   IN_VPR last operand is relevant only for vmova_a16_v32_1op_vuX_p
              1.
                   version.
Comments           When using movv/vmova intrinsics with high accumulators (a16-a23) in -
              2.   Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                   corresponding a16-a23 registers.


Main table → Move And Pack → Move → Vector Move Accumulator

Intrinsic     vmova_a16_v32_2op_vuX[_p]
name
Spec syntax   vmova {Oop, vuX} a16, vz[0], ?vprX

Return type   vec_t

              1    VUX            uint8     0..3            Determines the destination VCU
                                                            Accumulator operand (register a16 is
              2    IN1_A16        int32
                                                            expected)
Operands
                                                            Accumulator operand (register a17 is
              3    IN2_A17        int32
                                                            expected)
              4    IN_VPR         vprex_t                   Vector predicate operand
              int accIn;
              int accIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmova_a16_v32_2op_vuX_p (1, accIn, accIn2, vecPred);

                   IN_VPR last operand is relevant only for vmova_a16_v32_2op_vuX_p
              1.
                   version.
Comments
                   When using movv/vmova intrinsics with high accumulators (a16-a23) in -
              2.
                   Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                   corresponding a16-a23 registers.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a16_v32_3op_vuX[_p]
name
Spec syntax   vmova {Oop, vuX} a16, vz[0], ?vprX

Return type   vec_t

              1    VUX            uint8     0..3             Determines the destination VCU
                                                             Accumulator operand (register a16 is
              2    IN1_A16        int32
                                                             expected)
                                                             Accumulator operand (register a17 is
Operands      3    IN2_A17        int32
                                                             expected)
                                                             Accumulator operand (register a18 is
              4    IN3_A18        int32
                                                             expected)
              5    IN_VPR         vprex_t                    Vector predicate operand
              int accIn;
              int accIn2;
              int accIn3;
C example     vec_t vRes;
              vprex_t vecPred;
              ...

vRes = vmova_a16_v32_3op_vuX_p (1, accIn, accIn2, accIn3, vecPred);

                   IN_VPR last operand is relevant only for vmova_a16_v32_3op_vuX_p
              1.
                   version.
Comments           When using movv/vmova intrinsics with high accumulators (a16-a23) in -
              2.   Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                   corresponding a16-a23 registers.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a16_v32_4op_vuX[_p]
name
Spec syntax   vmova {Oop, vuX} a16, vz[0], ?vprX

Return type   vec_t

              1    VUX            uint8     0..3             Determines the destination VCU
                                                             Accumulator operand (register a16 is
              2    IN1_A16        int32
                                                             expected)
Operands
                                                             Accumulator operand (register a17 is
              3    IN2_A17        int32
                                                             expected)
              4    IN3_A18        int32                      Accumulator operand (register a18 is
                                                             expected)
                                                             Accumulator operand (register a19 is
              5    IN4_A19         int32
                                                             expected)
              6    IN_VPR          vprex_t                   Vector predicate operand
              int accIn;
              int accIn2;
              int accIn3;
              int accIn4;
C example     vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmova_a16_v32_4op_vuX_p (1, accIn, accIn2, accIn3, accIn4, vecPred);

                   IN_VPR last operand is relevant only for vmova_a16_v32_4op_vuX_p
              1.
                   version.
Comments           When using movv/vmova intrinsics with high accumulators (a16-a23) in -
              2.   Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                   corresponding a16-a23 registers.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a16_v32_5op_vuX[_p]
name
Spec syntax   vmova {Oop, vuX} a16, vz[0], ?vprX

Return type   vec_t

1    VUX             uint8     0..3            Determines the destination VCU
                                                             Accumulator operand (register a16 is
              2    IN1_A16         int32
                                                             expected)
                                                             Accumulator operand (register a17 is
              3    IN2_A17         int32
                                                             expected)
                                                             Accumulator operand (register a18 is
Operands      4    IN3_A18         int32
                                                             expected)
                                                             Accumulator operand (register a19 is
              5    IN4_A19         int32
                                                             expected)
                                                             Accumulator operand (register a20 is
              6    IN5_A20         int32
                                                             expected)
              7    IN_VPR          vprex_t                   Vector predicate operand
              int accIn;
              int accIn2;
              int accIn3;
C example     int accIn4;
              int accIn5;
              vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmova_a16_v32_5op_vuX_p (1, accIn, accIn2, accIn3, accIn4, accIn5, vecPred);

                   IN_VPR last operand is relevant only for vmova_a16_v32_5op_vuX_p
              1.
                   version.
Comments           When using movv/vmova intrinsics with high accumulators (a16-a23) in -
              2.   Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                   corresponding a16-a23 registers.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a16_v32_6op_vuX[_p]
name
Spec syntax   vmova {Oop, vuX} a16, vz[0], ?vprX

Return type   vec_t

              1    VUX             uint8     0..3             Determines the destination VCU
                                                              Accumulator operand (register a16 is
              2    IN1_A16         int32
                                                              expected)
                                                              Accumulator operand (register a17 is

3    IN2_A17         int32
                                                              expected)
                                                              Accumulator operand (register a18 is
              4    IN3_A18         int32
                                                              expected)
Operands
                                                              Accumulator operand (register a19 is
              5    IN4_A19         int32
                                                              expected)
                                                              Accumulator operand (register a20 is
              6    IN5_A20         int32
                                                              expected)

              7
                                                              Accumulator operand (register a21 is
                   IN6_A21         int32
                                                              expected)
              8    IN_VPR          vprex_t                    Vector predicate operand
              int accIn;
              int accIn2;
              int accIn3;
              int accIn4;
              int accIn5;
C example     int accIn6;
              vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmova_a16_v32_6op_vuX_p (1, accIn, accIn2, accIn3, accIn4, accIn5, accIn6, vecPred);

                   IN_VPR last operand is relevant only for vmova_a16_v32_6op_vuX_p
              1.
                   version.
Comments
                   When using movv/vmova intrinsics with high accumulators (a16-a23) in -
              2.
                   Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                   corresponding a16-a23 registers.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a16_v32_7op_vuX[_p]
name
Spec syntax   vmova {Oop, vuX} a16, vz[0], ?vprX

Return type   vec_t

              1    VUX             uint8     0..3              Determines the destination VCU
                                                               Accumulator operand (register a16 is
              2    IN1_A16         int32
                                                               expected)
                                                               Accumulator operand (register a17 is
              3    IN2_A17         int32
                                                               expected)

Accumulator operand (register a18 is
              4    IN3_A18         int32
                                                               expected)
                                                               Accumulator operand (register a19 is
Operands      5    IN4_A19         int32
                                                               expected)

              6
                                                               Accumulator operand (register a20 is
                   IN5_A20         int32
                                                               expected)
                                                               Accumulator operand (register a21 is
              7    IN6_A21         int32
                                                               expected)
                                                               Accumulator operand (register a22 is
              8    IN7_A22         int32
                                                               expected)
              9    IN_VPR          vprex_t                     Vector predicate operand
              int accIn;
              int accIn2;
              int accIn3;
              int accIn4;
              int accIn5;
C example     int accIn6;
              int accIn7;
              vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmova_a16_v32_7op_vuX_p (1, accIn, accIn2, accIn3, accIn4, accIn5, accIn6, accIn7, vecPred);

                   IN_VPR last operand is relevant only for vmova_a16_v32_7op_vuX_p
              1.
                   version.
Comments           When using movv/vmova intrinsics with high accumulators (a16-a23) in -
              2.   Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                   corresponding a16-a23 registers.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a16_v32_8op_vuX[_p]
name
Spec syntax   vmova {Oop, vuX} a16, vz[0], ?vprX

Return type   vec_t

              1    VUX             uint8     0..3              Determines the destination VCU
                                                               Accumulator operand (register a16 is
              2    IN1_A16         int32
                                                               expected)
                                                               Accumulator operand (register a17 is
              3    IN2_A17         int32

expected)
                                                               Accumulator operand (register a18 is
              4    IN3_A18         int32
                                                               expected)
                                                               Accumulator operand (register a19 is
              5    IN4_A19         int32
                                                               expected)
Operands
                                                               Accumulator operand (register a20 is
              6    IN5_A20         int32
                                                               expected)
                                                               Accumulator operand (register a21 is
              7    IN6_A21         int32
                                                               expected)
                                                               Accumulator operand (register a22 is
              8    IN7_A22         int32
                                                               expected)
                                                               Accumulator operand (register a23 is
              9    IN8_A23         int32
                                                               expected)
              10   IN_VPR          vprex_t                     Vector predicate operand
              int accIn;
              int accIn2;
              int accIn3;
              int accIn4;
              int accIn5;
              int accIn6;
C example     int accIn7;
              int accIn8;
              vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmova_a16_v32_8op_vuX_p (1, accIn, accIn2, accIn3, accIn4, accIn5, accIn6, accIn7, accIn8,
              vecPred);

                   IN_VPR last operand is relevant only for vmova_a16_v32_8op_vuX_p
              1.
                   version.
Comments           When using movv/vmova intrinsics with high accumulators (a16-a23) in -
              2.   Os3/-Os4 optimization levels, the accumulator variables must be bound to the
                   corresponding a16-a23 registers.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a0_c32_1op[_p]
name
Spec syntax   vmova {Qop} a0, vc0, ?vprX

Return type   coef_t


              1
                                                             Accumulator operand (register a0 is
                   IN1_A0         int32

Operands                                                     expected)
              2    IN_VPR         vprex_t                    Vector predicate operand
              int accIn;
              coef_t vcoefRes;
C example     vprex_t vecPred;
              ...
              vcoefRes = vmova_a0_c32_1op_p (accIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmova_a0_c32_1op_p version.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a0_c32_2op[_p]
name
Spec syntax   vmova {Qop} a0, vc0, ?vprX

Return type   coef_t

                                                             Accumulator operand (register a0 is
              1    IN1_A0         int32
                                                             expected)
                                                             Accumulator operand (register a1 is
              2    IN2_A1         int32
Operands                                                     expected)
                                                             Coefficient result operand (register vc1 is
              3    RES2_VC1       coef_t
                                                             expected)
              4    IN_VPR         vprex_t                    Vector predicate operand
              int accIn;
              int accIn2;
              coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              vprex_t vecPred;
              ...
              vcoefRes1 = vmova_a0_c32_2op_p (accIn, accIn2, vcoefRes2, vecPred);

              1.   IN_VPR last operand is relevant only for vmova_a0_c32_2op_p version.

Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_VC1).


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a0_c32_3op[_p]
name
Spec syntax   vmova {Qop} a0, vc0, ?vprX

Return type   coef_t


              1
                                                              Accumulator operand (register a0 is
                   IN1_A0          int32
                                                              expected)
                                                              Accumulator operand (register a1 is
              2    IN2_A1          int32
                                                              expected)

Accumulator operand (register a2 is
              3    IN3_A2          int32
Operands                                                      expected)
                                                              Coefficient result operand (register vc1 is
              4    RES2_VC1        coef_t
                                                              expected)
                                                              Coefficient result operand (register vc2 is
              5    RES3_VC2        coef_t
                                                              expected)
              6    IN_VPR          vprex_t                    Vector predicate operand
              int accIn;
              int accIn2;
              int accIn3;
              coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              coef_t vcoefRes3;
              vprex_t vecPred;
              ...
              vcoefRes1 = vmova_a0_c32_3op_p (accIn, accIn2, accIn3, vcoefRes2, vcoefRes3, vecPred);

              1.   IN_VPR last operand is relevant only for vmova_a0_c32_3op_p version.

Comments           This intrinsic returns more than one result. The first result variable should be
              2.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a0_c32_4op[_p]
name
Spec syntax   vmova {Qop} a0, vc0, ?vprX

Return type   coef_t

                                                              Accumulator operand (register a0 is
              1    IN1_A0          int32
                                                              expected)
                                                              Accumulator operand (register a1 is
Operands      2    IN2_A1          int32
                                                              expected)

              3
                                                              Accumulator operand (register a2 is
                   IN3_A2          int32
                                                              expected)
                                                            Accumulator operand (register a3 is
            4    IN4_A3          int32
                                                            expected)
                                                            Coefficient result operand (register vc1 is
            5    RES2_VC1        coef_t

expected)

            6
                                                            Coefficient result operand (register vc2 is
                 RES3_VC2        coef_t
                                                            expected)
                                                            Coefficient result operand (register vc3 is
            7    RES4_VC3        coef_t
                                                            expected)
            8    IN_VPR          vprex_t                    Vector predicate operand
            int accIn;
            int accIn2;
            int accIn3;
            int accIn4;
            coef_t vcoefRes1;
            coef_t vcoefRes2;
C example   coef_t vcoefRes3;
            coef_t vcoefRes4;
            vprex_t vecPred;
            ...
            vcoefRes1 = vmova_a0_c32_4op_p (accIn, accIn2, accIn3, accIn4, vcoefRes2, vcoefRes3, vcoefRes4,
            vecPred);

            1.   IN_VPR last operand is relevant only for vmova_a0_c32_4op_p version.

Comments         This intrinsic returns more than one result. The first result variable should be
            2.   placed to the left of the = sign (lvalue). Additional result variables should be
                 passed as parameters.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a8_v32_1op_vuX[_p]
name
Spec syntax   vmova {Oop, vuX} a8, vz[0], ?vprX

Return type   vec_t

              1    VUX            uint8     0..3            Determines the destination VCU
                                                            Accumulator operand (register a8 is
Operands      2    IN1_A8         int32
                                                            expected)
              3    IN_VPR         vprex_t                   Vector predicate operand
              int accIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmova_a8_v32_1op_vuX_p (1, accIn, vecPred);

                   IN_VPR last operand is relevant only for vmova_a8_v32_1op_vuX_p
Comments      1.
                   version.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a8_v32_2op_vuX[_p]
name
Spec syntax   vmova {Oop, vuX} a8, vz[0], ?vprX

Return type   vec_t

              1    VUX            uint8     0..3            Determines the destination VCU
                                                            Accumulator operand (register a8 is

2    IN1_A8         int32
                                                            expected)
Operands
                                                            Accumulator operand (register a9 is
              3    IN2_A9         int32
                                                            expected)
              4    IN_VPR         vprex_t                   Vector predicate operand
              int accIn;
              int accIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmova_a8_v32_2op_vuX_p (1, accIn, accIn2, vecPred);

                   IN_VPR last operand is relevant only for vmova_a8_v32_2op_vuX_p
Comments      1.
                   version.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a8_v32_3op_vuX[_p]
name
Spec syntax   vmova {Oop, vuX} a8, vz[0], ?vprX
Return type   vec_t

              1    VUX            uint8     0..3             Determines the destination VCU

              2
                                                             Accumulator operand (register a8 is
                   IN1_A8         int32
                                                             expected)
                                                             Accumulator operand (register a9 is
Operands      3    IN2_A9         int32
                                                             expected)
                                                             Accumulator operand (register a10 is
              4    IN3_A10        int32
                                                             expected)
              5    IN_VPR         vprex_t                    Vector predicate operand
              int accIn;
              int accIn2;
              int accIn3;
C example     vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmova_a8_v32_3op_vuX_p (1, accIn, accIn2, accIn3, vecPred);

                   IN_VPR last operand is relevant only for vmova_a8_v32_3op_vuX_p
Comments      1.
                   version.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a8_v32_4op_vuX[_p]
name
Spec syntax   vmova {Oop, vuX} a8, vz[0], ?vprX

Return type   vec_t

              1    VUX            uint8     0..3             Determines the destination VCU
                                                             Accumulator operand (register a8 is
              2    IN1_A8         int32

expected)

              3
                                                             Accumulator operand (register a9 is
                   IN2_A9         int32
                                                             expected)
Operands
                                                             Accumulator operand (register a10 is
              4    IN3_A10        int32
                                                             expected)
                                                             Accumulator operand (register a11 is
              5    IN4_A11        int32
                                                             expected)
              6    IN_VPR         vprex_t                    Vector predicate operand
              int accIn;
              int accIn2;
              int accIn3;
C example     int accIn4;
              vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmova_a8_v32_4op_vuX_p (1, accIn, accIn2, accIn3, accIn4, vecPred);

                   IN_VPR last operand is relevant only for vmova_a8_v32_4op_vuX_p
Comments      1.
                   version.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a8_v32_5op_vuX[_p]
name
Spec syntax   vmova {Oop, vuX} a8, vz[0], ?vprX

Return type   vec_t

              1    VUX             uint8     0..3             Determines the destination VCU
                                                              Accumulator operand (register a8 is
              2    IN1_A8          int32
                                                              expected)
                                                              Accumulator operand (register a9 is
              3    IN2_A9          int32
                                                              expected)
                                                              Accumulator operand (register a10 is
Operands      4    IN3_A10         int32
                                                              expected)
                                                              Accumulator operand (register a11 is
              5    IN4_A11         int32
                                                              expected)
                                                              Accumulator operand (register a12 is
              6    IN5_A12         int32
                                                              expected)

7    IN_VPR          vprex_t                    Vector predicate operand
              int accIn;
              int accIn2;
              int accIn3;
              int accIn4;
C example     int accIn5;
              vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmova_a8_v32_5op_vuX_p (1, accIn, accIn2, accIn3, accIn4, accIn5, vecPred);

                   IN_VPR last operand is relevant only for vmova_a8_v32_5op_vuX_p
Comments      1.
                   version.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a8_v32_6op_vuX[_p]
name
Spec syntax   vmova {Oop, vuX} a8, vz[0], ?vprX

Return type   vec_t

Operands      1    VUX             uint8     0..3             Determines the destination VCU
                                                              Accumulator operand (register a8 is
              2    IN1_A8          int32
                                                              expected)
                                                              Accumulator operand (register a9 is
              3    IN2_A9          int32
                                                              expected)

              4
                                                              Accumulator operand (register a10 is
                   IN3_A10         int32
                                                              expected)
                                                              Accumulator operand (register a11 is
              5    IN4_A11         int32
                                                              expected)
                                                              Accumulator operand (register a12 is
              6    IN5_A12         int32
                                                              expected)
                                                              Accumulator operand (register a13 is
              7    IN6_A13         int32
                                                              expected)
              8    IN_VPR          vprex_t                    Vector predicate operand
              int accIn;
              int accIn2;
              int accIn3;
              int accIn4;
              int accIn5;
C example     int accIn6;
              vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmova_a8_v32_6op_vuX_p (1, accIn, accIn2, accIn3, accIn4, accIn5, accIn6, vecPred);

IN_VPR last operand is relevant only for vmova_a8_v32_6op_vuX_p
Comments      1.
                   version.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a8_v32_7op_vuX[_p]
name
Spec syntax   vmova {Oop, vuX} a8, vz[0], ?vprX

Return type   vec_t

              1    VUX             uint8     0..3             Determines the destination VCU
                                                              Accumulator operand (register a8 is
              2    IN1_A8          int32
                                                              expected)
                                                              Accumulator operand (register a9 is
              3    IN2_A9          int32
Operands                                                      expected)
                                                              Accumulator operand (register a10 is
              4    IN3_A10         int32
                                                              expected)
                                                              Accumulator operand (register a11 is
              5    IN4_A11         int32
                                                              expected)
                                                               Accumulator operand (register a12 is
              6    IN5_A12         int32
                                                               expected)
                                                               Accumulator operand (register a13 is
              7    IN6_A13         int32
                                                               expected)

              8
                                                               Accumulator operand (register a14 is
                   IN7_A14         int32
                                                               expected)
              9    IN_VPR          vprex_t                     Vector predicate operand
              int accIn;
              int accIn2;
              int accIn3;
              int accIn4;
              int accIn5;
C example     int accIn6;
              int accIn7;
              vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmova_a8_v32_7op_vuX_p (1, accIn, accIn2, accIn3, accIn4, accIn5, accIn6, accIn7, vecPred);

                   IN_VPR last operand is relevant only for vmova_a8_v32_7op_vuX_p
Comments      1.
                   version.

Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a8_v32_8op_vuX[_p]
name
Spec syntax   vmova {Oop, vuX} a8, vz[0], ?vprX

Return type   vec_t

              1    VUX             uint8     0..3              Determines the destination VCU
                                                               Accumulator operand (register a8 is
              2    IN1_A8          int32
                                                               expected)
                                                               Accumulator operand (register a9 is
              3    IN2_A9          int32
                                                               expected)
                                                               Accumulator operand (register a10 is
              4    IN3_A10         int32
                                                               expected)
Operands                                                       Accumulator operand (register a11 is
              5    IN4_A11         int32
                                                               expected)
                                                               Accumulator operand (register a12 is
              6    IN5_A12         int32
                                                               expected)
                                                               Accumulator operand (register a13 is
              7    IN6_A13         int32
                                                               expected)
                                                               Accumulator operand (register a14 is
              8    IN7_A14         int32
                                                               expected)
                                                             Accumulator operand (register a15 is
            9    IN8_A15         int32
                                                             expected)
            10   IN_VPR          vprex_t                     Vector predicate operand
            int accIn;
            int accIn2;
            int accIn3;
            int accIn4;
            int accIn5;
            int accIn6;
C example   int accIn7;
            int accIn8;
            vec_t vRes;
            vprex_t vecPred;
            ...
            vRes = vmova_a8_v32_8op_vuX_p (1, accIn, accIn2, accIn3, accIn4, accIn5, accIn6, accIn7, accIn8,
            vecPred);

IN_VPR last operand is relevant only for vmova_a8_v32_8op_vuX_p
Comments    1.
                 version.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a8_c32_1op[_p]
name
Spec syntax   vmova {Qop} a8, vc0, ?vprX

Return type   coef_t


              1
                                                             Accumulator operand (register a8 is
                   IN1_A8         int32
Operands                                                     expected)
              2    IN_VPR         vprex_t                    Vector predicate operand
              int accIn;
              coef_t vcoefRes;
C example     vprex_t vecPred;
              ...
              vcoefRes = vmova_a8_c32_1op_p (accIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmova_a8_c32_1op_p version.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a8_c32_2op[_p]
name
Spec syntax   vmova {Qop} a8, vc0, ?vprX

Return type   coef_t

                                                             Accumulator operand (register a8 is
              1    IN1_A8         int32
                                                             expected)
                                                             Accumulator operand (register a9 is
              2    IN2_A9         int32
Operands                                                     expected)
                                                             Coefficient result operand (register vc1 is
              3    RES2_VC1       coef_t
                                                             expected)
              4    IN_VPR         vprex_t                    Vector predicate operand
              int accIn;
              int accIn2;
              coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              vprex_t vecPred;
              ...
              vcoefRes1 = vmova_a8_c32_2op_p (accIn, accIn2, vcoefRes2, vecPred);

              1.   IN_VPR last operand is relevant only for vmova_a8_c32_2op_p version.

Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_VC1).


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a8_c32_3op[_p]
name
Spec syntax   vmova {Qop} a8, vc0, ?vprX

Return type   coef_t


              1

Accumulator operand (register a8 is
                   IN1_A8          int32
                                                              expected)
                                                              Accumulator operand (register a9 is
              2    IN2_A9          int32
                                                              expected)
                                                              Accumulator operand (register a10 is
              3    IN3_A10         int32
Operands                                                      expected)
                                                              Coefficient result operand (register vc1 is
              4    RES2_VC1        coef_t
                                                              expected)
                                                              Coefficient result operand (register vc2 is
              5    RES3_VC2        coef_t
                                                              expected)
              6    IN_VPR          vprex_t                    Vector predicate operand
              int accIn;
              int accIn2;
              int accIn3;
              coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              coef_t vcoefRes3;
              vprex_t vecPred;
              ...
              vcoefRes1 = vmova_a8_c32_3op_p (accIn, accIn2, accIn3, vcoefRes2, vcoefRes3, vecPred);

              1.   IN_VPR last operand is relevant only for vmova_a8_c32_3op_p version.

Comments           This intrinsic returns more than one result. The first result variable should be
              2.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a8_c32_4op[_p]
name
Spec syntax   vmova {Qop} a8, vc0, ?vprX

Return type   coef_t

                                                              Accumulator operand (register a8 is
              1    IN1_A8          int32
                                                              expected)
                                                              Accumulator operand (register a9 is
Operands      2    IN2_A9          int32
                                                              expected)

              3
                                                              Accumulator operand (register a10 is
                   IN3_A10         int32

expected)
                                                            Accumulator operand (register a11 is
            4    IN4_A11         int32
                                                            expected)
                                                            Coefficient result operand (register vc1 is
            5    RES2_VC1        coef_t
                                                            expected)

            6
                                                            Coefficient result operand (register vc2 is
                 RES3_VC2        coef_t
                                                            expected)
                                                            Coefficient result operand (register vc3 is
            7    RES4_VC3        coef_t
                                                            expected)
            8    IN_VPR          vprex_t                    Vector predicate operand
            int accIn;
            int accIn2;
            int accIn3;
            int accIn4;
            coef_t vcoefRes1;
            coef_t vcoefRes2;
C example   coef_t vcoefRes3;
            coef_t vcoefRes4;
            vprex_t vecPred;
            ...
            vcoefRes1 = vmova_a8_c32_4op_p (accIn, accIn2, accIn3, accIn4, vcoefRes2, vcoefRes3, vcoefRes4,
            vecPred);

            1.   IN_VPR last operand is relevant only for vmova_a8_c32_4op_p version.

Comments         This intrinsic returns more than one result. The first result variable should be
            2.   placed to the left of the = sign (lvalue). Additional result variables should be
                 passed as parameters.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a12_c32_1op[_p]
name
Spec syntax   vmova {Qop} a12, vc0, ?vprX

Return type   coef_t


              1
                                                             Accumulator operand (register a12 is
                   IN1_A12        int32
Operands                                                     expected)
              2    IN_VPR         vprex_t                    Vector predicate operand
              int accIn;
              coef_t vcoefRes;
C example     vprex_t vecPred;
              ...
              vcoefRes = vmova_a12_c32_1op_p (accIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmova_a12_c32_1op_p version.


Main table → Move And Pack → Move → Vector Move Accumulator

Intrinsic     vmova_a12_c32_2op[_p]
name
Spec syntax   vmova {Qop} a12, vc0, ?vprX

Return type   coef_t

                                                             Accumulator operand (register a12 is
              1    IN1_A12        int32
                                                             expected)
                                                             Accumulator operand (register a13 is
              2    IN2_A13        int32
Operands                                                     expected)
                                                             Coefficient result operand (register vc1 is
              3    RES2_VC1       coef_t
                                                             expected)
              4    IN_VPR         vprex_t                    Vector predicate operand
              int accIn;
              int accIn2;
              coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              vprex_t vecPred;
              ...
              vcoefRes1 = vmova_a12_c32_2op_p (accIn, accIn2, vcoefRes2, vecPred);

              1.   IN_VPR last operand is relevant only for vmova_a12_c32_2op_p version.

Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_VC1).


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a12_c32_3op[_p]
name
Spec syntax   vmova {Qop} a12, vc0, ?vprX

Return type   coef_t


              1
                                                              Accumulator operand (register a12 is
                   IN1_A12         int32
                                                              expected)
                                                              Accumulator operand (register a13 is
              2    IN2_A13         int32
                                                              expected)
                                                              Accumulator operand (register a14 is
              3    IN3_A14         int32
Operands                                                      expected)
                                                              Coefficient result operand (register vc1 is
              4    RES2_VC1        coef_t
                                                              expected)

Coefficient result operand (register vc2 is
              5    RES3_VC2        coef_t
                                                              expected)
              6    IN_VPR          vprex_t                    Vector predicate operand
              int accIn;
              int accIn2;
              int accIn3;
              coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              coef_t vcoefRes3;
              vprex_t vecPred;
              ...
              vcoefRes1 = vmova_a12_c32_3op_p (accIn, accIn2, accIn3, vcoefRes2, vcoefRes3, vecPred);

              1.   IN_VPR last operand is relevant only for vmova_a12_c32_3op_p version.

Comments           This intrinsic returns more than one result. The first result variable should be
              2.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a12_c32_4op[_p]
name
Spec syntax   vmova {Qop} a12, vc0, ?vprX

Return type   coef_t

                                                              Accumulator operand (register a12 is
              1    IN1_A12         int32
                                                              expected)
                                                              Accumulator operand (register a13 is
Operands      2    IN2_A13         int32
                                                              expected)

              3
                                                              Accumulator operand (register a14 is
                   IN3_A14         int32
                                                              expected)
                                                            Accumulator operand (register a15 is
            4    IN4_A15         int32
                                                            expected)
                                                            Coefficient result operand (register vc1 is
            5    RES2_VC1        coef_t
                                                            expected)

            6
                                                            Coefficient result operand (register vc2 is
                 RES3_VC2        coef_t
                                                            expected)
                                                            Coefficient result operand (register vc3 is

7    RES4_VC3        coef_t
                                                            expected)
            8    IN_VPR          vprex_t                    Vector predicate operand
            int accIn;
            int accIn2;
            int accIn3;
            int accIn4;
            coef_t vcoefRes1;
            coef_t vcoefRes2;
C example   coef_t vcoefRes3;
            coef_t vcoefRes4;
            vprex_t vecPred;
            ...
            vcoefRes1 = vmova_a12_c32_4op_p (accIn, accIn2, accIn3, accIn4, vcoefRes2, vcoefRes3, vcoefRes4,
            vecPred);

            1.   IN_VPR last operand is relevant only for vmova_a12_c32_4op_p version.

Comments         This intrinsic returns more than one result. The first result variable should be
            2.   placed to the left of the = sign (lvalue). Additional result variables should be
                 passed as parameters.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a8_v32_1op[_p]
name
Spec syntax   vmova {Oop} a8, vz[0], ?vprX

Return type   vec_t


              1
                                                             Accumulator operand (register a8 is
                   IN1_A8         int32
Operands                                                     expected)
              2    IN_VPR         vprex_t                    Vector predicate operand
              int accIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmova_a8_v32_1op_p (accIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmova_a8_v32_1op_p version.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a8_v32_2op[_p]
name
Spec syntax   vmova {Oop} a8, vz[0], ?vprX

Return type   vec_t

                                                             Accumulator operand (register a8 is
              1    IN1_A8         int32
                                                             expected)
Operands                                                     Accumulator operand (register a9 is
              2    IN2_A9         int32
                                                             expected)
              3    IN_VPR         vprex_t                    Vector predicate operand
              int accIn;
              int accIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmova_a8_v32_2op_p (accIn, accIn2, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmova_a8_v32_2op_p version.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a8_v32_3op[_p]
name
Spec syntax   vmova {Oop} a8, vz[0], ?vprX

Return type   vec_t

                                                             Accumulator operand (register a8 is
Operands      1    IN1_A8         int32
                                                             expected)
                                                              Accumulator operand (register a9 is
              2    IN2_A9          int32
                                                              expected)
                                                              Accumulator operand (register a10 is
              3    IN3_A10         int32
                                                              expected)
              4    IN_VPR          vprex_t                    Vector predicate operand
              int accIn;
              int accIn2;
              int accIn3;
C example     vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmova_a8_v32_3op_p (accIn, accIn2, accIn3, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmova_a8_v32_3op_p version.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a8_v32_4op[_p]
name
Spec syntax   vmova {Oop} a8, vz[0], ?vprX

Return type   vec_t


              1
                                                              Accumulator operand (register a8 is
                   IN1_A8          int32
                                                              expected)
                                                              Accumulator operand (register a9 is
              2    IN2_A9          int32
                                                              expected)
Operands                                                      Accumulator operand (register a10 is
              3    IN3_A10         int32
                                                              expected)
                                                              Accumulator operand (register a11 is
              4    IN4_A11         int32
                                                              expected)
              5    IN_VPR          vprex_t                    Vector predicate operand
              int accIn;
              int accIn2;
              int accIn3;

int accIn4;
C example     vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmova_a8_v32_4op_p (accIn, accIn2, accIn3, accIn4, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmova_a8_v32_4op_p version.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a8_v32_5op[_p]
name
Spec syntax   vmova {Oop} a8, vz[0], ?vprX
Return type   vec_t

                                                              Accumulator operand (register a8 is
              1    IN1_A8          int32
                                                              expected)

              2
                                                              Accumulator operand (register a9 is
                   IN2_A9          int32
                                                              expected)
                                                              Accumulator operand (register a10 is
              3    IN3_A10         int32
Operands                                                      expected)
                                                              Accumulator operand (register a11 is
              4    IN4_A11         int32
                                                              expected)
                                                              Accumulator operand (register a12 is
              5    IN5_A12         int32
                                                              expected)
              6    IN_VPR          vprex_t                    Vector predicate operand
              int accIn;
              int accIn2;
              int accIn3;
              int accIn4;
C example     int accIn5;
              vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmova_a8_v32_5op_p (accIn, accIn2, accIn3, accIn4, accIn5, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmova_a8_v32_5op_p version.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a8_v32_6op[_p]
name
Spec syntax   vmova {Oop} a8, vz[0], ?vprX

Return type   vec_t

                                                              Accumulator operand (register a8 is
              1    IN1_A8          int32
                                                              expected)
                                                              Accumulator operand (register a9 is
              2    IN2_A9          int32

expected)
                                                              Accumulator operand (register a10 is
              3    IN3_A10         int32
                                                              expected)
Operands
                                                              Accumulator operand (register a11 is
              4    IN4_A11         int32
                                                              expected)

              5
                                                              Accumulator operand (register a12 is
                   IN5_A12         int32
                                                              expected)
                                                              Accumulator operand (register a13 is
              6    IN6_A13         int32
                                                              expected)
              7    IN_VPR          vprex_t                     Vector predicate operand
              int accIn;
              int accIn2;
              int accIn3;
              int accIn4;
              int accIn5;
C example     int accIn6;
              vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmova_a8_v32_6op_p (accIn, accIn2, accIn3, accIn4, accIn5, accIn6, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmova_a8_v32_6op_p version.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a8_v32_7op[_p]
name
Spec syntax   vmova {Oop} a8, vz[0], ?vprX

Return type   vec_t


              1
                                                               Accumulator operand (register a8 is
                   IN1_A8          int32
                                                               expected)
                                                               Accumulator operand (register a9 is
              2    IN2_A9          int32
                                                               expected)
                                                               Accumulator operand (register a10 is
              3    IN3_A10         int32
                                                               expected)
                                                               Accumulator operand (register a11 is
              4    IN4_A11         int32
Operands                                                       expected)

Accumulator operand (register a12 is
              5    IN5_A12         int32
                                                               expected)
                                                               Accumulator operand (register a13 is
              6    IN6_A13         int32
                                                               expected)
                                                               Accumulator operand (register a14 is
              7    IN7_A14         int32
                                                               expected)
              8    IN_VPR          vprex_t                     Vector predicate operand
              int accIn;
              int accIn2;
              int accIn3;
              int accIn4;
              int accIn5;
C example     int accIn6;
              int accIn7;
              vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmova_a8_v32_7op_p (accIn, accIn2, accIn3, accIn4, accIn5, accIn6, accIn7, vecPred);
Comments      1.   IN_VPR last operand is relevant only for vmova_a8_v32_7op_p version.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a8_v32_8op[_p]
name
Spec syntax   vmova {Oop} a8, vz[0], ?vprX

Return type   vec_t


              1
                                                               Accumulator operand (register a8 is
                   IN1_A8          int32
                                                               expected)
                                                               Accumulator operand (register a9 is
              2    IN2_A9          int32
                                                               expected)
                                                               Accumulator operand (register a10 is
              3    IN3_A10         int32
                                                               expected)
                                                               Accumulator operand (register a11 is
              4    IN4_A11         int32
                                                               expected)
Operands                                                       Accumulator operand (register a12 is
              5    IN5_A12         int32
                                                               expected)

              6
                                                               Accumulator operand (register a13 is

IN6_A13         int32
                                                               expected)
                                                               Accumulator operand (register a14 is
              7    IN7_A14         int32
                                                               expected)
                                                               Accumulator operand (register a15 is
              8    IN8_A15         int32
                                                               expected)
              9    IN_VPR          vprex_t                     Vector predicate operand
              int accIn;
              int accIn2;
              int accIn3;
              int accIn4;
              int accIn5;
              int accIn6;
C example     int accIn7;
              int accIn8;
              vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmova_a8_v32_8op_p (accIn, accIn2, accIn3, accIn4, accIn5, accIn6, accIn7, accIn8, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmova_a8_v32_8op_p version.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a12_c32_1op_vuX[_p]
name
Spec syntax   vmova {Qop, vuX} a12, vc0, ?vprX

Return type   coef_t

              1    VUX            uint8     0..3             Determines the destination VCU
                                                             Accumulator operand (register a12 is
Operands      2    IN1_A12        int32
                                                             expected)
              3    IN_VPR         vprex_t                    Vector predicate operand
              int accIn;
              coef_t vcoefRes;
C example     vprex_t vecPred;
              ...
              vcoefRes = vmova_a12_c32_1op_vuX_p (1, accIn, vecPred);

                   IN_VPR last operand is relevant only for vmova_a12_c32_1op_vuX_p
Comments      1.
                   version.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a12_c32_2op_vuX[_p]
name
Spec syntax   vmova {Qop, vuX} a12, vc0, ?vprX

Return type   coef_t

              1    VUX            uint8     0..3             Determines the destination VCU
                                                             Accumulator operand (register a12 is
              2    IN1_A12        int32
                                                             expected)

Accumulator operand (register a13 is
Operands      3    IN2_A13        int32
                                                             expected)
                                                             Coefficient result operand (register vc1 is
              4    RES2_VC1       coef_t
                                                             expected)
              5    IN_VPR         vprex_t                    Vector predicate operand
              int accIn;
              int accIn2;
              coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              vprex_t vecPred;
              ...
              vcoefRes1 = vmova_a12_c32_2op_vuX_p (1, accIn, accIn2, vcoefRes2, vecPred);

                   IN_VPR last operand is relevant only for vmova_a12_c32_2op_vuX_p
              1.
                   version.
Comments
                   This intrinsic returns two results. The first result variable should be placed to
              2.
                   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_VC1).


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a12_c32_3op_vuX[_p]
name
Spec syntax   vmova {Qop, vuX} a12, vc0, ?vprX

Return type   coef_t

              1    VUX            uint8     0..3             Determines the destination VCU
                                                             Accumulator operand (register a12 is
              2    IN1_A12        int32
                                                             expected)
                                                             Accumulator operand (register a13 is
              3    IN2_A13        int32
                                                             expected)
                                                             Accumulator operand (register a14 is
Operands      4    IN3_A14        int32
                                                             expected)
                                                             Coefficient result operand (register vc1 is
              5    RES2_VC1       coef_t
                                                             expected)

              6
                                                             Coefficient result operand (register vc2 is
                   RES3_VC2       coef_t
                                                             expected)

7    IN_VPR         vprex_t                    Vector predicate operand
              int accIn;
              int accIn2;
              int accIn3;
              coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              coef_t vcoefRes3;
              vprex_t vecPred;
              ...
              vcoefRes1 = vmova_a12_c32_3op_vuX_p (1, accIn, accIn2, accIn3, vcoefRes2, vcoefRes3, vecPred);

                   IN_VPR last operand is relevant only for vmova_a12_c32_3op_vuX_p
              1.
                   version.
Comments           This intrinsic returns more than one result. The first result variable should be
              2.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a12_c32_4op_vuX[_p]
name
Spec syntax   vmova {Qop, vuX} a12, vc0, ?vprX

Return type   coef_t

Operands      1    VUX            uint8     0..3             Determines the destination VCU
                                                           Accumulator operand (register a12 is
            2    IN1_A12         int32
                                                           expected)
                                                           Accumulator operand (register a13 is
            3    IN2_A13         int32
                                                           expected)

            4
                                                           Accumulator operand (register a14 is
                 IN3_A14         int32
                                                           expected)
                                                           Accumulator operand (register a15 is
            5    IN4_A15         int32
                                                           expected)
                                                           Coefficient result operand (register vc1 is
            6    RES2_VC1        coef_t
                                                           expected)
                                                           Coefficient result operand (register vc2 is
            7    RES3_VC2        coef_t
                                                           expected)
                                                           Coefficient result operand (register vc3 is
            8    RES4_VC3        coef_t

expected)
            9    IN_VPR          vprex_t                   Vector predicate operand
            int accIn;
            int accIn2;
            int accIn3;
            int accIn4;
            coef_t vcoefRes1;
            coef_t vcoefRes2;
C example   coef_t vcoefRes3;
            coef_t vcoefRes4;
            vprex_t vecPred;
            ...
            vcoefRes1 = vmova_a12_c32_4op_vuX_p (1, accIn, accIn2, accIn3, accIn4, vcoefRes2, vcoefRes3,
            vcoefRes4, vecPred);

                 IN_VPR last operand is relevant only for vmova_a12_c32_4op_vuX_p
            1.
                 version.
Comments         This intrinsic returns more than one result. The first result variable should be
            2.   placed to the left of the = sign (lvalue). Additional result variables should be
                 passed as parameters.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a0_v32_1op_vuX[_p]
name
Spec syntax   vmova {Oop, vuX} a0, vz[0], ?vprX

Return type   vec_t

              1    VUX            uint8     0..3            Determines the destination VCU
                                                            Accumulator operand (register a0 is
Operands      2    IN1_A0         int32
                                                            expected)
              3    IN_VPR         vprex_t                   Vector predicate operand
              int accIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmova_a0_v32_1op_vuX_p (1, accIn, vecPred);

                   IN_VPR last operand is relevant only for vmova_a0_v32_1op_vuX_p
Comments      1.
                   version.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a0_v32_2op_vuX[_p]
name
Spec syntax   vmova {Oop, vuX} a0, vz[0], ?vprX

Return type   vec_t

              1    VUX            uint8     0..3            Determines the destination VCU
                                                            Accumulator operand (register a0 is
              2    IN1_A0         int32
                                                            expected)
Operands
                                                            Accumulator operand (register a1 is
              3    IN2_A1         int32
                                                            expected)
              4    IN_VPR         vprex_t                   Vector predicate operand
              int accIn;

int accIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmova_a0_v32_2op_vuX_p (1, accIn, accIn2, vecPred);

                   IN_VPR last operand is relevant only for vmova_a0_v32_2op_vuX_p
Comments      1.
                   version.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a0_v32_3op_vuX[_p]
name
Spec syntax   vmova {Oop, vuX} a0, vz[0], ?vprX
Return type   vec_t

              1    VUX            uint8     0..3             Determines the destination VCU

              2
                                                             Accumulator operand (register a0 is
                   IN1_A0         int32
                                                             expected)
                                                             Accumulator operand (register a1 is
Operands      3    IN2_A1         int32
                                                             expected)
                                                             Accumulator operand (register a2 is
              4    IN3_A2         int32
                                                             expected)
              5    IN_VPR         vprex_t                    Vector predicate operand
              int accIn;
              int accIn2;
              int accIn3;
C example     vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmova_a0_v32_3op_vuX_p (1, accIn, accIn2, accIn3, vecPred);

                   IN_VPR last operand is relevant only for vmova_a0_v32_3op_vuX_p
Comments      1.
                   version.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a0_v32_4op_vuX[_p]
name
Spec syntax   vmova {Oop, vuX} a0, vz[0], ?vprX

Return type   vec_t

              1    VUX            uint8     0..3             Determines the destination VCU
                                                             Accumulator operand (register a0 is
              2    IN1_A0         int32
                                                             expected)

              3
                                                             Accumulator operand (register a1 is
                   IN2_A1         int32
                                                             expected)
Operands
                                                             Accumulator operand (register a2 is
              4    IN3_A2         int32

expected)
                                                             Accumulator operand (register a3 is
              5    IN4_A3         int32
                                                             expected)
              6    IN_VPR         vprex_t                    Vector predicate operand
              int accIn;
              int accIn2;
              int accIn3;
C example     int accIn4;
              vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmova_a0_v32_4op_vuX_p (1, accIn, accIn2, accIn3, accIn4, vecPred);

                   IN_VPR last operand is relevant only for vmova_a0_v32_4op_vuX_p
Comments      1.
                   version.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a0_v32_5op_vuX[_p]
name
Spec syntax   vmova {Oop, vuX} a0, vz[0], ?vprX

Return type   vec_t

              1    VUX             uint8     0..3             Determines the destination VCU
                                                              Accumulator operand (register a0 is
              2    IN1_A0          int32
                                                              expected)
                                                              Accumulator operand (register a1 is
              3    IN2_A1          int32
                                                              expected)
                                                              Accumulator operand (register a2 is
Operands      4    IN3_A2          int32
                                                              expected)
                                                              Accumulator operand (register a3 is
              5    IN4_A3          int32
                                                              expected)
                                                              Accumulator operand (register a4 is
              6    IN5_A4          int32
                                                              expected)
              7    IN_VPR          vprex_t                    Vector predicate operand
              int accIn;
              int accIn2;
              int accIn3;
              int accIn4;
C example     int accIn5;
              vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmova_a0_v32_5op_vuX_p (1, accIn, accIn2, accIn3, accIn4, accIn5, vecPred);

                   IN_VPR last operand is relevant only for vmova_a0_v32_5op_vuX_p

Comments      1.
                   version.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a0_v32_6op_vuX[_p]
name
Spec syntax   vmova {Oop, vuX} a0, vz[0], ?vprX

Return type   vec_t

Operands      1    VUX             uint8     0..3             Determines the destination VCU
                                                              Accumulator operand (register a0 is
              2    IN1_A0          int32
                                                              expected)
                                                              Accumulator operand (register a1 is
              3    IN2_A1          int32
                                                              expected)

              4
                                                              Accumulator operand (register a2 is
                   IN3_A2          int32
                                                              expected)
                                                              Accumulator operand (register a3 is
              5    IN4_A3          int32
                                                              expected)
                                                              Accumulator operand (register a4 is
              6    IN5_A4          int32
                                                              expected)
                                                              Accumulator operand (register a5 is
              7    IN6_A5          int32
                                                              expected)
              8    IN_VPR          vprex_t                    Vector predicate operand
              int accIn;
              int accIn2;
              int accIn3;
              int accIn4;
              int accIn5;
C example     int accIn6;
              vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmova_a0_v32_6op_vuX_p (1, accIn, accIn2, accIn3, accIn4, accIn5, accIn6, vecPred);

                   IN_VPR last operand is relevant only for vmova_a0_v32_6op_vuX_p
Comments      1.
                   version.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a0_v32_7op_vuX[_p]
name
Spec syntax   vmova {Oop, vuX} a0, vz[0], ?vprX

Return type   vec_t

              1    VUX             uint8     0..3             Determines the destination VCU

Accumulator operand (register a0 is
              2    IN1_A0          int32
                                                              expected)
                                                              Accumulator operand (register a1 is
              3    IN2_A1          int32
Operands                                                      expected)
                                                              Accumulator operand (register a2 is
              4    IN3_A2          int32
                                                              expected)
                                                              Accumulator operand (register a3 is
              5    IN4_A3          int32
                                                              expected)
                                                               Accumulator operand (register a4 is
              6    IN5_A4          int32
                                                               expected)
                                                               Accumulator operand (register a5 is
              7    IN6_A5          int32
                                                               expected)

              8
                                                               Accumulator operand (register a6 is
                   IN7_A6          int32
                                                               expected)
              9    IN_VPR          vprex_t                     Vector predicate operand
              int accIn;
              int accIn2;
              int accIn3;
              int accIn4;
              int accIn5;
C example     int accIn6;
              int accIn7;
              vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmova_a0_v32_7op_vuX_p (1, accIn, accIn2, accIn3, accIn4, accIn5, accIn6, accIn7, vecPred);

                   IN_VPR last operand is relevant only for vmova_a0_v32_7op_vuX_p
Comments      1.
                   version.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a0_v32_8op_vuX[_p]
name
Spec syntax   vmova {Oop, vuX} a0, vz[0], ?vprX

Return type   vec_t

              1    VUX             uint8     0..3              Determines the destination VCU
                                                               Accumulator operand (register a0 is
              2    IN1_A0          int32

expected)
                                                               Accumulator operand (register a1 is
              3    IN2_A1          int32
                                                               expected)
                                                               Accumulator operand (register a2 is
              4    IN3_A2          int32
                                                               expected)
Operands                                                       Accumulator operand (register a3 is
              5    IN4_A3          int32
                                                               expected)
                                                               Accumulator operand (register a4 is
              6    IN5_A4          int32
                                                               expected)
                                                               Accumulator operand (register a5 is
              7    IN6_A5          int32
                                                               expected)
                                                               Accumulator operand (register a6 is
              8    IN7_A6          int32
                                                               expected)
                                                             Accumulator operand (register a7 is
            9    IN8_A7          int32
                                                             expected)
            10   IN_VPR          vprex_t                     Vector predicate operand
            int accIn;
            int accIn2;
            int accIn3;
            int accIn4;
            int accIn5;
            int accIn6;
C example   int accIn7;
            int accIn8;
            vec_t vRes;
            vprex_t vecPred;
            ...
            vRes = vmova_a0_v32_8op_vuX_p (1, accIn, accIn2, accIn3, accIn4, accIn5, accIn6, accIn7, accIn8,
            vecPred);

                 IN_VPR last operand is relevant only for vmova_a0_v32_8op_vuX_p
Comments    1.
                 version.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a4_c32_1op_vuX[_p]
name
Spec syntax   vmova {Qop, vuX} a4, vc0, ?vprX

Return type   coef_t

              1    VUX            uint8     0..3             Determines the destination VCU
                                                             Accumulator operand (register a4 is
Operands      2    IN1_A4         int32

expected)
              3    IN_VPR         vprex_t                    Vector predicate operand
              int accIn;
              coef_t vcoefRes;
C example     vprex_t vecPred;
              ...
              vcoefRes = vmova_a4_c32_1op_vuX_p (1, accIn, vecPred);

                   IN_VPR last operand is relevant only for vmova_a4_c32_1op_vuX_p
Comments      1.
                   version.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a4_c32_2op_vuX[_p]
name
Spec syntax   vmova {Qop, vuX} a4, vc0, ?vprX

Return type   coef_t

              1    VUX            uint8     0..3             Determines the destination VCU
                                                             Accumulator operand (register a4 is
              2    IN1_A4         int32
                                                             expected)
                                                             Accumulator operand (register a5 is
Operands      3    IN2_A5         int32
                                                             expected)
                                                             Coefficient result operand (register vc1 is
              4    RES2_VC1       coef_t
                                                             expected)
              5    IN_VPR         vprex_t                    Vector predicate operand
              int accIn;
              int accIn2;
              coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              vprex_t vecPred;
              ...
              vcoefRes1 = vmova_a4_c32_2op_vuX_p (1, accIn, accIn2, vcoefRes2, vecPred);

                   IN_VPR last operand is relevant only for vmova_a4_c32_2op_vuX_p
              1.
                   version.
Comments
                   This intrinsic returns two results. The first result variable should be placed to
              2.
                   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_VC1).


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a4_c32_3op_vuX[_p]
name
Spec syntax   vmova {Qop, vuX} a4, vc0, ?vprX

Return type   coef_t

              1    VUX             uint8     0..3            Determines the destination VCU
                                                             Accumulator operand (register a4 is
              2    IN1_A4          int32

expected)
                                                             Accumulator operand (register a5 is
              3    IN2_A5          int32
                                                             expected)
                                                             Accumulator operand (register a6 is
Operands      4    IN3_A6          int32
                                                             expected)
                                                             Coefficient result operand (register vc1 is
              5    RES2_VC1        coef_t
                                                             expected)

              6
                                                             Coefficient result operand (register vc2 is
                   RES3_VC2        coef_t
                                                             expected)
              7    IN_VPR          vprex_t                   Vector predicate operand
              int accIn;
              int accIn2;
              int accIn3;
              coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              coef_t vcoefRes3;
              vprex_t vecPred;
              ...
              vcoefRes1 = vmova_a4_c32_3op_vuX_p (1, accIn, accIn2, accIn3, vcoefRes2, vcoefRes3, vecPred);

                   IN_VPR last operand is relevant only for vmova_a4_c32_3op_vuX_p
              1.
                   version.
Comments           This intrinsic returns more than one result. The first result variable should be
              2.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.


Main table → Move And Pack → Move → Vector Move Accumulator
Intrinsic     vmova_a4_c32_4op_vuX[_p]
name
Spec syntax   vmova {Qop, vuX} a4, vc0, ?vprX

Return type   coef_t

Operands      1    VUX             uint8     0..3            Determines the destination VCU
                                                           Accumulator operand (register a4 is
            2    IN1_A4          int32
                                                           expected)
                                                           Accumulator operand (register a5 is
            3    IN2_A5          int32
                                                           expected)

            4
                                                           Accumulator operand (register a6 is
                 IN3_A6          int32

expected)
                                                           Accumulator operand (register a7 is
            5    IN4_A7          int32
                                                           expected)
                                                           Coefficient result operand (register vc1 is
            6    RES2_VC1        coef_t
                                                           expected)
                                                           Coefficient result operand (register vc2 is
            7    RES3_VC2        coef_t
                                                           expected)
                                                           Coefficient result operand (register vc3 is
            8    RES4_VC3        coef_t
                                                           expected)
            9    IN_VPR          vprex_t                   Vector predicate operand
            int accIn;
            int accIn2;
            int accIn3;
            int accIn4;
            coef_t vcoefRes1;
            coef_t vcoefRes2;
C example   coef_t vcoefRes3;
            coef_t vcoefRes4;
            vprex_t vecPred;
            ...
            vcoefRes1 = vmova_a4_c32_4op_vuX_p (1, accIn, accIn2, accIn3, accIn4, vcoefRes2, vcoefRes3,
            vcoefRes4, vecPred);

                 IN_VPR last operand is relevant only for vmova_a4_c32_4op_vuX_p
            1.
                 version.
Comments         This intrinsic returns more than one result. The first result variable should be
            2.   placed to the left of the = sign (lvalue). Additional result variables should be
                 passed as parameters.


Main table → Move And Pack → Move → Vector Move Accumulator
