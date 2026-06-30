# Move And Pack → Move → Vector Move Immediate

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Move And Pack → Move → Vector Move Immediate

Vector Move Immediate

Vector Move Immediate
Performs data move of an immediate value to destination. The destination is either 32-bit or 40-
bit wide determined by the vector register type.
Available Switches
u          When used, the rest of voz[Z] is zero-extended.
vuX        Determines the destination VCU of the instruction. X is replaced by 0 or 1.
Intrinsic Names
vmovi_imm32_6_v40
vmovi_imm32_6_v40_u
vmovi_uimm16_7_vpr_vuX
vmovi_imm32_6_v32
vmovi_uimm16_7_vpr
vmovi_imm32_6_v40_vuX
vmovi_imm32_6_v40_vuX_u
vmovi_imm8_v40ext_vuX
vmovi_imm8_v40ext
vmovi_imm32_6_c32
vmovi_imm32_6_c32_vuX
vmovi_imm32_6_v32_vuX
Instruction details in the instruction set specification

Intrinsic     vmovi_imm32_6_v40[_p]
name
Spec syntax   vmovi {[u]} #imm32_6, voz[Z], ?vprX

Return type   vec40_t
                                              31   31
              1    IN1_IMM32_6 int32        -2 ..2 -1         32 bit immediate
                                                              Offset for the first DW used from the
Operands      2    OUT_OFST       uint8     0..7
                                                              result operand
              3    IN_VPR         vprex_t                     Vector predicate operand
              vec40_t vRes;
              vprex_t vecPred;
C example     ...
              vRes = vmovi_imm32_6_v40_p (2, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmovi_imm32_6_v40_p version.


Main table → Move And Pack → Move → Vector Move Immediate
Intrinsic     vmovi_imm32_6_v40_u[_p]
name
Spec syntax   vmovi {[u]} #imm32_6, voz[Z], ?vprX

Return type   vec40_t
                                              31   31
              1    IN1_IMM32_6 int32        -2 ..2 -1         32 bit immediate
                                                              Offset for the first DW used from the
Operands      2    OUT_OFST       uint8     0..7
                                                              result operand
              3    IN_VPR         vprex_t                     Vector predicate operand
              vec40_t vRes;
              vprex_t vecPred;
C example     ...
              vRes = vmovi_imm32_6_v40_u_p (2, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmovi_imm32_6_v40_u_p version.


Main table → Move And Pack → Move → Vector Move Immediate
Intrinsic     vmovi_uimm16_7_vpr_vuX
name
Spec syntax   vmovi {vuX} #uimm16_7, VPREX

Return type   vprex_t

              1   VUX             uint8    0..3             Determines the destination VCU
Operands
              2   IN1_UIMM16_7 uint16      0..65535         16 bit unsigned immediate
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vmovi_uimm16_7_vpr_vuX (1, 2);

Comments


Main table → Move And Pack → Move → Vector Move Immediate
Intrinsic     vmovi_imm32_6_v32[_p]
name
Spec syntax   vmovi #imm32_6, viz[Z], ?vprX

Return type   vec_t
                                              31   31
              1    IN1_IMM32_6 int32        -2 ..2 -1       32 bit immediate

Offset for the first DW used from the
Operands      2    OUT_OFST       uint8     0..7
                                                            result operand
              3    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vRes;
              vprex_t vecPred;
C example     ...
              vRes = vmovi_imm32_6_v32_p (2, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmovi_imm32_6_v32_p version.


Main table → Move And Pack → Move → Vector Move Immediate
Intrinsic     vmovi_uimm16_7_vpr
name
Spec syntax   vmovi #uimm16_7, VPREX

Return type   vprex_t

Operands      1   IN1_UIMM16_7 uint16      0..65535   16 bit unsigned immediate
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vmovi_uimm16_7_vpr (2);

Comments


Main table → Move And Pack → Move → Vector Move Immediate
Intrinsic     vmovi_imm32_6_v40_vuX[_p]
name
Spec syntax   vmovi {vuX [,u]} #imm32_6, voz[Z], ?vprX

Return type   vec40_t

              1    VUX            uint8     0..3           Determines the destination VCU
                                              31   31
              2    IN1_IMM32_6 int32        -2 ..2 -1      32 bit immediate
Operands                                                   Offset for the first DW used from the
              3    OUT_OFST       uint8     0..7
                                                           result operand
              4    IN_VPR         vprex_t                  Vector predicate operand
              vec40_t vRes;
              vprex_t vecPred;
C example     ...
              vRes = vmovi_imm32_6_v40_vuX_p (1, 2, 0, vecPred);

                   IN_VPR last operand is relevant only for vmovi_imm32_6_v40_vuX_p
Comments      1.
                   version.


Main table → Move And Pack → Move → Vector Move Immediate
Intrinsic     vmovi_imm32_6_v40_vuX_u[_p]
name
Spec syntax   vmovi {vuX [,u]} #imm32_6, voz[Z], ?vprX

Return type   vec40_t

              1    VUX            uint8     0..3           Determines the destination VCU
                                              31   31
              2    IN1_IMM32_6 int32        -2 ..2 -1      32 bit immediate
Operands                                                   Offset for the first DW used from the
              3    OUT_OFST       uint8     0..7
                                                           result operand

4    IN_VPR         vprex_t                  Vector predicate operand
              vec40_t vRes;
              vprex_t vecPred;
C example     ...
              vRes = vmovi_imm32_6_v40_vuX_u_p (1, 2, 0, vecPred);

                   IN_VPR last operand is relevant only for vmovi_imm32_6_v40_vuX_u_p
Comments      1.
                   version.


Main table → Move And Pack → Move → Vector Move Immediate
Intrinsic     vmovi_imm8_v40ext_vuX[_p]
name
Spec syntax   vmovi {vuX} #imm8, voz[Z]ext, ?vprX

Return type   vec40_t

              1    VUX            uint8     0..3            Determines the destination VCU
              2    IN1_IMM8       int16     -128..127       8 bit immediate
Operands                                                    Offset for the first DW used from the
              3    OUT_OFST       uint8     0..7
                                                            result operand
              4    IN_VPR         vprex_t                   Vector predicate operand
              vec40_t vRes;
              vprex_t vecPred;
C example     ...
              vRes = vmovi_imm8_v40ext_vuX_p (1, 2, 0, vecPred);

                   IN_VPR last operand is relevant only for vmovi_imm8_v40ext_vuX_p
Comments      1.
                   version.


Main table → Move And Pack → Move → Vector Move Immediate
Intrinsic     vmovi_imm8_v40ext[_p]
name
Spec syntax   vmovi #imm8, voz[Z]ext, ?vprX

Return type   vec40_t

              1    IN1_IMM8       int16     -128..127       8 bit immediate
                                                            Offset for the first DW used from the
Operands      2    OUT_OFST       uint8     0..7
                                                            result operand
              3    IN_VPR         vprex_t                   Vector predicate operand
              vec40_t vRes;
              vprex_t vecPred;
C example     ...
              vRes = vmovi_imm8_v40ext_p (2, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmovi_imm8_v40ext_p version.


Main table → Move And Pack → Move → Vector Move Immediate
Intrinsic     vmovi_imm32_6_c32[_p]
name
Spec syntax   vmovi #imm32_6, vcZ, ?vprX

Return type   coef_t
                                             31   31
              1    IN1_IMM32_6 int32        -2 ..2 -1        32 bit immediate
Operands
              2    IN_VPR         vprex_t                    Vector predicate operand
              coef_t vcoefRes;
              vprex_t vecPred;

C example     ...
              vcoefRes = vmovi_imm32_6_c32_p (2, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmovi_imm32_6_c32_p version.


Main table → Move And Pack → Move → Vector Move Immediate
Intrinsic     vmovi_imm32_6_c32_vuX[_p]
name
Spec syntax   vmovi {vuX} #imm32_6, vcZ, ?vprX

Return type   coef_t

              1    VUX            uint8     0..3           Determines the destination VCU
                                              31   31
Operands      2    IN1_IMM32_6 int32        -2 ..2 -1      32 bit immediate
              3    IN_VPR         vprex_t                  Vector predicate operand
              coef_t vcoefRes;
              vprex_t vecPred;
C example     ...
              vcoefRes = vmovi_imm32_6_c32_vuX_p (1, 2, vecPred);

                   IN_VPR last operand is relevant only for vmovi_imm32_6_c32_vuX_p
Comments      1.
                   version.


Main table → Move And Pack → Move → Vector Move Immediate
Intrinsic     vmovi_imm32_6_v32_vuX[_p]
name
Spec syntax   vmovi {vuX} #imm32_6, viz[Z], ?vprX

Return type   vec_t

              1    VUX            uint8     0..3           Determines the destination VCU
                                              31   31
              2    IN1_IMM32_6 int32        -2 ..2 -1      32 bit immediate
Operands                                                   Offset for the first DW used from the
              3    OUT_OFST       uint8     0..7
                                                           result operand
              4    IN_VPR         vprex_t                  Vector predicate operand
              vec_t vRes;
              vprex_t vecPred;
C example     ...
              vRes = vmovi_imm32_6_v32_vuX_p (1, 2, 0, vecPred);

                   IN_VPR last operand is relevant only for vmovi_imm32_6_v32_vuX_p
Comments      1.
                   version.


Main table → Move And Pack → Move → Vector Move Immediate
