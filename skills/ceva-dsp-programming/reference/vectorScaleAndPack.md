# Bit Manipulation → Scale → Vector Scale and Pack

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Bit Manipulation → Scale → Vector Scale and Pack

Vector Scale and Pack

Vector Scale and Pack
By default performs an arithmetic shift operation on two 40-bit sources and packing the high part
into either 32-bit or 40-bit destination according to the register type.
Available Switches
       Number of atomic operations. An atomic operation is defined as two shift operations and
Qop

one pack operation. 1op ≤ Qop ≤ 4op
       Signed saturation, when used the shifted number is regarded as a signed value. When
s
       shifting right, the MSBs of the destination are sign-extended
       Unsigned saturation, when used the shifted number saturation is regarded as an unsigned
us
       value. When shifting right, the MSBs of the destination are zero-extended
Intrinsic Names
vscalep_v40_c32_v40
vscalep_v40_c32_v40_s
vscalep_v40_c32_v40_us
vscalep_v40_c32_v32
vscalep_v40_c32_v32_s
vscalep_v40_c32_v32_us
vscalep_v40_imm4_v40
vscalep_v40_imm4_v40_s
vscalep_v40_imm4_v40_us
vscalep_v40_c32p_v32
vscalep_v40_c32p_v32_s
vscalep_v40_c32p_v32_us
vscalep_v40_c32p_v40
vscalep_v40_c32p_v40_s
vscalep_v40_c32p_v40_us
vscalep_v40_imm4_v32
vscalep_v40_imm4_v32_s
vscalep_v40_imm4_v32_us
Instruction details in the instruction set specification
Intrinsic     vscalep_v40_c32_v40[_p]
name
Spec syntax   vscalep {Qop [,us_s]} vox[0], vcY, voz[0], ?vprX

Return type   vec40_t

              1    QOP             uint8      1..4             Number of atomic operations
              2    IN1_V40         vec40_t                     Output vector operand
              3    IN2_C32         coef_t                      Coefficient operand
Operands
                                                               Offset for the first DW used from the
              4    OUT_OFST        uint8      0,4
                                                               result operand
              5    IN_VPR          vprex_t                     Vector predicate operand
              vec40_t vIn;
              vec40_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vscalep_v40_c32_v40_p (4, vIn, vcoefIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vscalep_v40_c32_v40_p version.


Main table → Bit Manipulation → Scale → Vector Scale and Pack
Intrinsic     vscalep_v40_c32_v40_s[_p]
name
Spec syntax   vscalep {Qop [,us_s]} vox[0], vcY, voz[0], ?vprX

Return type   vec40_t

              1    QOP             uint8      1..4             Number of atomic operations
              2    IN1_V40         vec40_t                     Output vector operand
              3    IN2_C32         coef_t                      Coefficient operand
Operands
                                                               Offset for the first DW used from the
              4    OUT_OFST        uint8      0,4

result operand
              5    IN_VPR          vprex_t                     Vector predicate operand
              vec40_t vIn;
              vec40_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vscalep_v40_c32_v40_s_p (4, vIn, vcoefIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vscalep_v40_c32_v40_s_p version.


Main table → Bit Manipulation → Scale → Vector Scale and Pack
Intrinsic     vscalep_v40_c32_v40_us[_p]
name
Spec syntax   vscalep {Qop [,us_s]} vox[0], vcY, voz[0], ?vprX

Return type   vec40_t

              1    QOP             uint8     1..4              Number of atomic operations
              2    IN1_V40         vec40_t                     Output vector operand
              3    IN2_C32         coef_t                      Coefficient operand
Operands
                                                               Offset for the first DW used from the
              4    OUT_OFST        uint8     0,4
                                                               result operand
              5    IN_VPR          vprex_t                     Vector predicate operand
              vec40_t vIn;
              vec40_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vscalep_v40_c32_v40_us_p (4, vIn, vcoefIn, 0, vecPred);

                   IN_VPR last operand is relevant only for vscalep_v40_c32_v40_us_p
Comments      1.
                   version.


Main table → Bit Manipulation → Scale → Vector Scale and Pack
Intrinsic     vscalep_v40_c32_v32[_p]
name
Spec syntax   vscalep {Qop [,us_s]} vox[0], vcY, viz[0], ?vprX

Return type   vec_t

              1    QOP             uint8      1..4             Number of atomic operations
              2    IN1_V40         vec40_t                     Output vector operand
              3    IN2_C32         coef_t                      Coefficient operand
Operands
                                                               Offset for the first DW used from the
              4    OUT_OFST        uint8      0,4
                                                               result operand
              5    IN_VPR          vprex_t                     Vector predicate operand
              vec40_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...

vRes = vscalep_v40_c32_v32_p (4, vIn, vcoefIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vscalep_v40_c32_v32_p version.


Main table → Bit Manipulation → Scale → Vector Scale and Pack
Intrinsic     vscalep_v40_c32_v32_s[_p]
name
Spec syntax   vscalep {Qop [,us_s]} vox[0], vcY, viz[0], ?vprX

Return type   vec_t

              1    QOP             uint8      1..4             Number of atomic operations
              2    IN1_V40         vec40_t                     Output vector operand
              3    IN2_C32         coef_t                      Coefficient operand
Operands
                                                               Offset for the first DW used from the
              4    OUT_OFST        uint8      0,4
                                                               result operand
              5    IN_VPR          vprex_t                     Vector predicate operand
              vec40_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vscalep_v40_c32_v32_s_p (4, vIn, vcoefIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vscalep_v40_c32_v32_s_p version.


Main table → Bit Manipulation → Scale → Vector Scale and Pack
Intrinsic     vscalep_v40_c32_v32_us[_p]
name
Spec syntax   vscalep {Qop [,us_s]} vox[0], vcY, viz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4              Number of atomic operations
              2    IN1_V40         vec40_t                     Output vector operand
              3    IN2_C32         coef_t                      Coefficient operand
Operands
                                                               Offset for the first DW used from the
              4    OUT_OFST        uint8     0,4
                                                               result operand
              5    IN_VPR          vprex_t                     Vector predicate operand
              vec40_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vscalep_v40_c32_v32_us_p (4, vIn, vcoefIn, 0, vecPred);

                   IN_VPR last operand is relevant only for vscalep_v40_c32_v32_us_p
Comments      1.
                   version.


Main table → Bit Manipulation → Scale → Vector Scale and Pack
Intrinsic     vscalep_v40_imm4_v40[_p]
name

Spec syntax   vscalep {Qop [,us_s]} vox[0], #imm4, voz[0], ?vprX

Return type   vec40_t

              1    QOP             uint8     1..4             Number of atomic operations
              2    IN1_V40         vec40_t                    Output vector operand
              3    IN2_IMM4        int8      -8..7            4 bit immediate
Operands
                                                              Offset for the first DW used from the
              4    OUT_OFST        uint8     0,4
                                                              result operand
              5    IN_VPR          vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vscalep_v40_imm4_v40_p (4, vIn, 2, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vscalep_v40_imm4_v40_p version.


Main table → Bit Manipulation → Scale → Vector Scale and Pack
Intrinsic     vscalep_v40_imm4_v40_s[_p]
name
Spec syntax   vscalep {Qop [,us_s]} vox[0], #imm4, voz[0], ?vprX

Return type   vec40_t

              1    QOP             uint8     1..4             Number of atomic operations
              2    IN1_V40         vec40_t                    Output vector operand
              3    IN2_IMM4        int8      -8..7            4 bit immediate
Operands
                                                              Offset for the first DW used from the
              4    OUT_OFST        uint8     0,4
                                                              result operand
              5    IN_VPR          vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vscalep_v40_imm4_v40_s_p (4, vIn, 2, 0, vecPred);

                   IN_VPR last operand is relevant only for vscalep_v40_imm4_v40_s_p
Comments      1.
                   version.


Main table → Bit Manipulation → Scale → Vector Scale and Pack
Intrinsic     vscalep_v40_imm4_v40_us[_p]
name
Spec syntax   vscalep {Qop [,us_s]} vox[0], #imm4, voz[0], ?vprX

Return type   vec40_t

              1    QOP             uint8     1..4             Number of atomic operations
              2    IN1_V40         vec40_t                    Output vector operand
              3    IN2_IMM4        int8      -8..7            4 bit immediate
Operands

Offset for the first DW used from the
              4    OUT_OFST        uint8     0,4
                                                              result operand
              5    IN_VPR          vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vscalep_v40_imm4_v40_us_p (4, vIn, 2, 0, vecPred);

                   IN_VPR last operand is relevant only for vscalep_v40_imm4_v40_us_p
Comments      1.
                   version.


Main table → Bit Manipulation → Scale → Vector Scale and Pack
Intrinsic     vscalep_v40_c32p_v32[_p]
name
Spec syntax   vscalep {Qop [,us_s]} vox[0], vcYp, viz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4             Number of atomic operations
              2    IN1_V40         vec40_t                    Output vector operand
              3    IN2_C32         coef_t                     Coefficient operand
Operands      4    IN2_PART        uint8     LOW,HIGH         Word part which is used for operand 3
                                                              Offset for the first DW used from the
              5    OUT_OFST        uint8     0,4
                                                              result operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vscalep_v40_c32p_v32_p (4, vIn, vcoefIn, LOW, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vscalep_v40_c32p_v32_p version.


Main table → Bit Manipulation → Scale → Vector Scale and Pack
Intrinsic     vscalep_v40_c32p_v32_s[_p]
name
Spec syntax   vscalep {Qop [,us_s]} vox[0], vcYp, viz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4             Number of atomic operations
              2    IN1_V40         vec40_t                    Output vector operand
              3    IN2_C32         coef_t                     Coefficient operand
Operands      4    IN2_PART        uint8     LOW,HIGH         Word part which is used for operand 3
                                                              Offset for the first DW used from the
              5    OUT_OFST        uint8     0,4

result operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vscalep_v40_c32p_v32_s_p (4, vIn, vcoefIn, LOW, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vscalep_v40_c32p_v32_s_p
                   version.


Main table → Bit Manipulation → Scale → Vector Scale and Pack
Intrinsic     vscalep_v40_c32p_v32_us[_p]
name
Spec syntax   vscalep {Qop [,us_s]} vox[0], vcYp, viz[0], ?vprX

Return type   vec_t

              1    QOP            uint8      1..4             Number of atomic operations
              2    IN1_V40        vec40_t                     Output vector operand
              3    IN2_C32        coef_t                      Coefficient operand
Operands      4    IN2_PART       uint8      LOW,HIGH         Word part which is used for operand 3
                                                              Offset for the first DW used from the
              5    OUT_OFST       uint8      0,4
                                                              result operand
              6    IN_VPR         vprex_t                     Vector predicate operand
              vec40_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vscalep_v40_c32p_v32_us_p (4, vIn, vcoefIn, LOW, 0, vecPred);

                   IN_VPR last operand is relevant only for vscalep_v40_c32p_v32_us_p
Comments      1.
                   version.


Main table → Bit Manipulation → Scale → Vector Scale and Pack
Intrinsic     vscalep_v40_c32p_v40[_p]
name
Spec syntax   vscalep {Qop [,us_s]} vox[0], vcYp, voz[0], ?vprX

Return type   vec40_t

              1    QOP             uint8     1..4             Number of atomic operations
              2    IN1_V40         vec40_t                    Output vector operand
              3    IN2_C32         coef_t                     Coefficient operand
Operands      4    IN2_PART        uint8     LOW,HIGH         Word part which is used for operand 3
                                                              Offset for the first DW used from the
              5    OUT_OFST        uint8     0,4
                                                              result operand

6    IN_VPR          vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec40_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vscalep_v40_c32p_v40_p (4, vIn, vcoefIn, LOW, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vscalep_v40_c32p_v40_p version.


Main table → Bit Manipulation → Scale → Vector Scale and Pack
Intrinsic     vscalep_v40_c32p_v40_s[_p]
name
Spec syntax   vscalep {Qop [,us_s]} vox[0], vcYp, voz[0], ?vprX

Return type   vec40_t

              1    QOP             uint8     1..4             Number of atomic operations
              2    IN1_V40         vec40_t                    Output vector operand
              3    IN2_C32         coef_t                     Coefficient operand
Operands      4    IN2_PART        uint8     LOW,HIGH         Word part which is used for operand 3
                                                              Offset for the first DW used from the
              5    OUT_OFST        uint8     0,4
                                                              result operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec40_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vscalep_v40_c32p_v40_s_p (4, vIn, vcoefIn, LOW, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vscalep_v40_c32p_v40_s_p
                   version.


Main table → Bit Manipulation → Scale → Vector Scale and Pack
Intrinsic     vscalep_v40_c32p_v40_us[_p]
name
Spec syntax   vscalep {Qop [,us_s]} vox[0], vcYp, voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8      1..4             Number of atomic operations
              2    IN1_V40        vec40_t                     Output vector operand
              3    IN2_C32        coef_t                      Coefficient operand
Operands      4    IN2_PART       uint8      LOW,HIGH         Word part which is used for operand 3
                                                              Offset for the first DW used from the
              5    OUT_OFST       uint8      0,4
                                                              result operand
              6    IN_VPR         vprex_t                     Vector predicate operand
              vec40_t vIn;
              vec40_t vRes;

coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vscalep_v40_c32p_v40_us_p (4, vIn, vcoefIn, LOW, 0, vecPred);

                   IN_VPR last operand is relevant only for vscalep_v40_c32p_v40_us_p
Comments      1.
                   version.


Main table → Bit Manipulation → Scale → Vector Scale and Pack
Intrinsic     vscalep_v40_imm4_v32[_p]
name
Spec syntax   vscalep {Qop [,us_s]} vox[0], #imm4, viz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4             Number of atomic operations
              2    IN1_V40         vec40_t                    Output vector operand
              3    IN2_IMM4        int8      -8..7            4 bit immediate
Operands
                                                              Offset for the first DW used from the
              4    OUT_OFST        uint8     0,4
                                                              result operand
              5    IN_VPR          vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vscalep_v40_imm4_v32_p (4, vIn, 2, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vscalep_v40_imm4_v32_p version.


Main table → Bit Manipulation → Scale → Vector Scale and Pack
Intrinsic     vscalep_v40_imm4_v32_s[_p]
name
Spec syntax   vscalep {Qop [,us_s]} vox[0], #imm4, viz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4             Number of atomic operations
              2    IN1_V40         vec40_t                    Output vector operand
              3    IN2_IMM4        int8      -8..7            4 bit immediate
Operands
                                                              Offset for the first DW used from the
              4    OUT_OFST        uint8     0,4
                                                              result operand
              5    IN_VPR          vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vscalep_v40_imm4_v32_s_p (4, vIn, 2, 0, vecPred);

                   IN_VPR last operand is relevant only for vscalep_v40_imm4_v32_s_p
Comments      1.
                   version.


Main table → Bit Manipulation → Scale → Vector Scale and Pack
Intrinsic     vscalep_v40_imm4_v32_us[_p]
name

Spec syntax   vscalep {Qop [,us_s]} vox[0], #imm4, viz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4             Number of atomic operations
              2    IN1_V40         vec40_t                    Output vector operand
              3    IN2_IMM4        int8      -8..7            4 bit immediate
Operands
                                                              Offset for the first DW used from the
              4    OUT_OFST        uint8     0,4
                                                              result operand
              5    IN_VPR          vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vscalep_v40_imm4_v32_us_p (4, vIn, 2, 0, vecPred);

                   IN_VPR last operand is relevant only for vscalep_v40_imm4_v32_us_p
Comments      1.
                   version.


Main table → Bit Manipulation → Scale → Vector Scale and Pack
