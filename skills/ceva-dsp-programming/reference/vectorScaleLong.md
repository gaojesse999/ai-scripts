# Bit Manipulation → Scale → Vector Scale Long

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Bit Manipulation → Scale → Vector Scale Long

Vector Scale Long

Vector Scale Long
By default performs an arithmetic shift operation on a 72-bit source into either 64-bit or 72-bit
destination determined by the register type.
Available Switches
       Number of atomic operations. An atomic operation is defined as a single shift operation.
Dop
       1op ≤ Dop ≤ 2op
       Number of atomic operations. An atomic operation is defined as a single shift operation.
Qop
       1op ≤ Qop ≤ 4op
       Signed saturation, when used the shifted number is regarded as a signed value. When
s
       shifting right, the MSBs of the destination are sign-extended
       Unsigned saturation, when used the shifted number saturation is regarded as an unsigned
us
       value. When shifting right, the MSBs of the destination are zero-extended
Intrinsic Names
vscalel_v40_c32p_v32
vscalel_v40_c32p_v32_s
vscalel_v40_c32p_v32_us
vscalel_v40_imm4_v32
vscalel_v40_imm4_v32_s
vscalel_v40_imm4_v32_us
vscalel_v40_c32_v32
vscalel_v40_c32_v32_s
vscalel_v40_c32_v32_us
Instruction details in the instruction set specification
Intrinsic     vscalel_v40_c32p_v32[_p]
name
Spec syntax   vscalel {Qop [,us_s]} vox[0], vcYp, vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4             Number of atomic operations
              2    IN1_V40         vec40_t                    Output vector operand
Operands      3    IN2_C32         coef_t                     Coefficient operand
              4    IN2_PART        uint8     LOW,HIGH         Word part which is used for operand 3
              5    IN_VPR          vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vscalel_v40_c32p_v32_p (4, vIn, vcoefIn, LOW, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vscalel_v40_c32p_v32_p version.


Main table → Bit Manipulation → Scale → Vector Scale Long
Intrinsic     vscalel_v40_c32p_v32_s[_p]
name
Spec syntax   vscalel {Qop [,us_s]} vox[0], vcYp, vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4             Number of atomic operations
              2    IN1_V40         vec40_t                    Output vector operand
Operands      3    IN2_C32         coef_t                     Coefficient operand
              4    IN2_PART        uint8     LOW,HIGH         Word part which is used for operand 3
              5    IN_VPR          vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vscalel_v40_c32p_v32_s_p (4, vIn, vcoefIn, LOW, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vscalel_v40_c32p_v32_s_p version.


Main table → Bit Manipulation → Scale → Vector Scale Long
Intrinsic     vscalel_v40_c32p_v32_us[_p]
name
Spec syntax   vscalel {Qop [,us_s]} vox[0], vcYp, vz[0], ?vprX

Return type   vec_t

              1    QOP            uint8      1..4            Number of atomic operations
              2    IN1_V40        vec40_t                    Output vector operand
Operands      3    IN2_C32        coef_t                     Coefficient operand
              4    IN2_PART       uint8      LOW,HIGH        Word part which is used for operand 3
              5    IN_VPR         vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vscalel_v40_c32p_v32_us_p (4, vIn, vcoefIn, LOW, vecPred);

                   IN_VPR last operand is relevant only for vscalel_v40_c32p_v32_us_p
Comments      1.
                   version.


Main table → Bit Manipulation → Scale → Vector Scale Long
Intrinsic     vscalel_v40_imm4_v32[_p]
name
Spec syntax   vscalel {Qop [,us_s]} vox[0], #imm4, vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4             Number of atomic operations
              2    IN1_V40         vec40_t                    Output vector operand
Operands
              3    IN2_IMM4        int8      -8..7            4 bit immediate

4    IN_VPR          vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vscalel_v40_imm4_v32_p (4, vIn, 2, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vscalel_v40_imm4_v32_p version.


Main table → Bit Manipulation → Scale → Vector Scale Long
Intrinsic     vscalel_v40_imm4_v32_s[_p]
name
Spec syntax   vscalel {Qop [,us_s]} vox[0], #imm4, vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4             Number of atomic operations
              2    IN1_V40         vec40_t                    Output vector operand
Operands
              3    IN2_IMM4        int8      -8..7            4 bit immediate
              4    IN_VPR          vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vscalel_v40_imm4_v32_s_p (4, vIn, 2, vecPred);

                   IN_VPR last operand is relevant only for vscalel_v40_imm4_v32_s_p
Comments      1.
                   version.


Main table → Bit Manipulation → Scale → Vector Scale Long
Intrinsic     vscalel_v40_imm4_v32_us[_p]
name
Spec syntax   vscalel {Qop [,us_s]} vox[0], #imm4, vz[0], ?vprX

Return type   vec_t

Operands      1    QOP             uint8     1..4             Number of atomic operations
            2    IN1_V40        vec40_t                     Output vector operand
            3    IN2_IMM4       int8       -8..7            4 bit immediate
            4    IN_VPR         vprex_t                     Vector predicate operand
            vec40_t vIn;
            vec_t vRes;
C example   vprex_t vecPred;
            ...
            vRes = vscalel_v40_imm4_v32_us_p (4, vIn, 2, vecPred);

                 IN_VPR last operand is relevant only for vscalel_v40_imm4_v32_us_p
Comments    1.
                 version.


Main table → Bit Manipulation → Scale → Vector Scale Long
Intrinsic     vscalel_v40_c32_v32[_p]
name
Spec syntax   vscalel {Qop [,us_s]} vox[0], vcY, vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8      1..4             Number of atomic operations
              2    IN1_V40         vec40_t                     Output vector operand
Operands
              3    IN2_C32         coef_t                      Coefficient operand

4    IN_VPR          vprex_t                     Vector predicate operand
              vec40_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vscalel_v40_c32_v32_p (4, vIn, vcoefIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vscalel_v40_c32_v32_p version.


Main table → Bit Manipulation → Scale → Vector Scale Long
Intrinsic     vscalel_v40_c32_v32_s[_p]
name
Spec syntax   vscalel {Qop [,us_s]} vox[0], vcY, vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8      1..4             Number of atomic operations
              2    IN1_V40         vec40_t                     Output vector operand
Operands
              3    IN2_C32         coef_t                      Coefficient operand
              4    IN_VPR          vprex_t                     Vector predicate operand
              vec40_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vscalel_v40_c32_v32_s_p (4, vIn, vcoefIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vscalel_v40_c32_v32_s_p version.


Main table → Bit Manipulation → Scale → Vector Scale Long
Intrinsic     vscalel_v40_c32_v32_us[_p]
name
Spec syntax   vscalel {Qop [,us_s]} vox[0], vcY, vz[0], ?vprX

Return type   vec_t
            1    QOP             uint8     1..4              Number of atomic operations
            2    IN1_V40         vec40_t                     Output vector operand
Operands
            3    IN2_C32         coef_t                      Coefficient operand
            4    IN_VPR          vprex_t                     Vector predicate operand
            vec40_t vIn;
            vec_t vRes;
            coef_t vcoefIn;
C example   vprex_t vecPred;
            ...
            vRes = vscalel_v40_c32_v32_us_p (4, vIn, vcoefIn, vecPred);

Comments    1.   IN_VPR last operand is relevant only for vscalel_v40_c32_v32_us_p version.


Main table → Bit Manipulation → Scale → Vector Scale Long
