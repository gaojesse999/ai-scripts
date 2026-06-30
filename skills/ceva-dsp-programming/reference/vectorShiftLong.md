# Bit Manipulation → Shift → Vector Shift Long

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Bit Manipulation → Shift → Vector Shift Long

Vector Shift Long

Vector Shift Long
Performs arithmetic or logic shift operation on a 64-bit source into either 64-bit or 72-bit
destination determined by the register type.
Available Switches
       Number of atomic operations. An atomic operation is defined as a single shift operation.
Qop
       1op ≤ Qop ≤ 4op
       Selects arithmetic (ar) or logic (lg) shift. When shifting right, the MSBs of the destination
ar     are sign-extended according to bit 31 for an arithmetic shift, and zero-extended for a logic
       shift. The default is an arithmetic shift.
b      Shift values are given by bytes
dw     Shift values are given by double-words
lg
w      Shift values are given by words
Intrinsic Names
vshiftl_v32_v32_v32_b_ar
vshiftl_v32_v32_v32_b_lg
vshiftl_v32_v32_v32_b
vshiftl_v32_c32p_v32_ar
vshiftl_v32_c32p_v32_lg
vshiftl_v32_c32p_v32
vshiftl_v32_c32_v32_ar
vshiftl_v32_c32_v32_lg
vshiftl_v32_c32_v32
vshiftl_v32_v32_v32_dw_ar
vshiftl_v32_v32_v32_dw_lg
vshiftl_v32_v32_v32_dw
vshiftl_v32_imm7_v32_ar
vshiftl_v32_imm7_v32_lg
vshiftl_v32_imm7_v32
vshiftl_v32_v32_v32_w_ar
vshiftl_v32_v32_v32_w_lg
vshiftl_v32_v32_v32_w
Instruction details in the instruction set specification
Intrinsic     vshiftl_v32_v32_v32_b_ar[_p]
name
Spec syntax   vshiftl {Qop, b [,ar | lg]} vx[0], vy[Y], vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8      1..4             Number of atomic operations
              2    IN1_V32         vec_t                       Input vector operand

Operands
              3    IN2_V32         vec_t                       Input vector operand

              4    IN2_OFST        uint8      0,4
                                                               Offset for the first DW used from operand
                                                               3

              5    IN_VPR          vprex_t                     Vector predicate operand
              vec_t vIn;

vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vshiftl_v32_v32_v32_b_ar_p (4, vIn, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for vshiftl_v32_v32_v32_b_ar_p
Comments      1.
                   version.


Main table → Bit Manipulation → Shift → Vector Shift Long
Intrinsic     vshiftl_v32_v32_v32_b_lg[_p]
name
Spec syntax   vshiftl {Qop, b [,ar | lg]} vx[0], vy[Y], vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8      1..4             Number of atomic operations
              2    IN1_V32         vec_t                       Input vector operand

Operands
              3    IN2_V32         vec_t                       Input vector operand

              4    IN2_OFST        uint8      0,4
                                                               Offset for the first DW used from operand
                                                               3

              5    IN_VPR          vprex_t                     Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vshiftl_v32_v32_v32_b_lg_p (4, vIn, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for vshiftl_v32_v32_v32_b_lg_p
Comments      1.
                   version.


Main table → Bit Manipulation → Shift → Vector Shift Long
Intrinsic     vshiftl_v32_v32_v32_b[_p]
name
Spec syntax   vshiftl {Qop, b [,ar | lg]} vx[0], vy[Y], vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8      1..4             Number of atomic operations
              2    IN1_V32         vec_t                       Input vector operand

Operands
              3    IN2_V32         vec_t                       Input vector operand

              4    IN2_OFST        uint8      0,4
                                                               Offset for the first DW used from operand
                                                               3

              5    IN_VPR          vprex_t                     Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vshiftl_v32_v32_v32_b_p (4, vIn, vIn2, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vshiftl_v32_v32_v32_b_p version.

Main table → Bit Manipulation → Shift → Vector Shift Long
Intrinsic     vshiftl_v32_c32p_v32_ar[_p]
name
Spec syntax   vshiftl {Qop [,ar | lg]} vx[0], vcYp, vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand
Operands      3    IN2_C32         coef_t                     Coefficient operand
              4    IN2_PART        uint8     LOW,HIGH         Word part which is used for operand 3
              5    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vshiftl_v32_c32p_v32_ar_p (4, vIn, vcoefIn, LOW, vecPred);

                   IN_VPR last operand is relevant only for vshiftl_v32_c32p_v32_ar_p
Comments      1.
                   version.


Main table → Bit Manipulation → Shift → Vector Shift Long
Intrinsic     vshiftl_v32_c32p_v32_lg[_p]
name
Spec syntax   vshiftl {Qop [,ar | lg]} vx[0], vcYp, vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand
Operands      3    IN2_C32         coef_t                     Coefficient operand
              4    IN2_PART        uint8     LOW,HIGH         Word part which is used for operand 3
              5    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vshiftl_v32_c32p_v32_lg_p (4, vIn, vcoefIn, LOW, vecPred);

                   IN_VPR last operand is relevant only for vshiftl_v32_c32p_v32_lg_p
Comments      1.
                   version.


Main table → Bit Manipulation → Shift → Vector Shift Long
Intrinsic     vshiftl_v32_c32p_v32[_p]
name
Spec syntax   vshiftl {Qop [,ar | lg]} vx[0], vcYp, vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand
Operands      3    IN2_C32         coef_t                     Coefficient operand
              4    IN2_PART        uint8     LOW,HIGH         Word part which is used for operand 3

5    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vshiftl_v32_c32p_v32_p (4, vIn, vcoefIn, LOW, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vshiftl_v32_c32p_v32_p version.


Main table → Bit Manipulation → Shift → Vector Shift Long
Intrinsic     vshiftl_v32_c32_v32_ar[_p]
name
Spec syntax   vshiftl {Qop [,ar | lg]} vx[0], vcY, vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8      1..4             Number of atomic operations
              2    IN1_V32         vec_t                       Input vector operand
Operands
              3    IN2_C32         coef_t                      Coefficient operand
              4    IN_VPR          vprex_t                     Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vshiftl_v32_c32_v32_ar_p (4, vIn, vcoefIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vshiftl_v32_c32_v32_ar_p version.


Main table → Bit Manipulation → Shift → Vector Shift Long
Intrinsic     vshiftl_v32_c32_v32_lg[_p]
name
Spec syntax   vshiftl {Qop [,ar | lg]} vx[0], vcY, vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8      1..4             Number of atomic operations
              2    IN1_V32         vec_t                       Input vector operand
Operands
              3    IN2_C32         coef_t                      Coefficient operand
              4    IN_VPR          vprex_t                     Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vshiftl_v32_c32_v32_lg_p (4, vIn, vcoefIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vshiftl_v32_c32_v32_lg_p version.


Main table → Bit Manipulation → Shift → Vector Shift Long
Intrinsic     vshiftl_v32_c32_v32[_p]
name
Spec syntax   vshiftl {Qop [,ar | lg]} vx[0], vcY, vz[0], ?vprX

Return type   vec_t
            1    QOP             uint8      1..4             Number of atomic operations
            2    IN1_V32         vec_t                       Input vector operand
Operands

3    IN2_C32         coef_t                      Coefficient operand
            4    IN_VPR          vprex_t                     Vector predicate operand
            vec_t vIn;
            vec_t vRes;
            coef_t vcoefIn;
C example   vprex_t vecPred;
            ...
            vRes = vshiftl_v32_c32_v32_p (4, vIn, vcoefIn, vecPred);

Comments    1.   IN_VPR last operand is relevant only for vshiftl_v32_c32_v32_p version.


Main table → Bit Manipulation → Shift → Vector Shift Long
Intrinsic     vshiftl_v32_v32_v32_dw_ar[_p]
name
Spec syntax   vshiftl {Qop, dw [,ar | lg]} vx[0], vy[0], vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4              Number of atomic operations
              2    IN1_V32         vec_t                       Input vector operand

Operands
              3    IN2_V32         vec_t                       Input vector operand

              4    IN2_OFST        uint8     0,4
                                                               Offset for the first DW used from operand
                                                               3

              5    IN_VPR          vprex_t                     Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vshiftl_v32_v32_v32_dw_ar_p (4, vIn, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for vshiftl_v32_v32_v32_dw_ar_p
Comments      1.
                   version.


Main table → Bit Manipulation → Shift → Vector Shift Long
Intrinsic     vshiftl_v32_v32_v32_dw_lg[_p]
name
Spec syntax   vshiftl {Qop, dw [,ar | lg]} vx[0], vy[0], vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4              Number of atomic operations
              2    IN1_V32         vec_t                       Input vector operand

Operands
              3    IN2_V32         vec_t                       Input vector operand

              4    IN2_OFST        uint8     0,4
                                                               Offset for the first DW used from operand
                                                               3

              5    IN_VPR          vprex_t                     Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...

vRes = vshiftl_v32_v32_v32_dw_lg_p (4, vIn, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for vshiftl_v32_v32_v32_dw_lg_p
Comments      1.
                   version.


Main table → Bit Manipulation → Shift → Vector Shift Long
Intrinsic     vshiftl_v32_v32_v32_dw[_p]
name
Spec syntax   vshiftl {Qop, dw [,ar | lg]} vx[0], vy[0], vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4              Number of atomic operations
              2    IN1_V32         vec_t                       Input vector operand

Operands
              3    IN2_V32         vec_t                       Input vector operand

              4    IN2_OFST        uint8     0,4
                                                               Offset for the first DW used from operand
                                                               3

              5    IN_VPR          vprex_t                     Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vshiftl_v32_v32_v32_dw_p (4, vIn, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for vshiftl_v32_v32_v32_dw_p
Comments      1.
                   version.


Main table → Bit Manipulation → Shift → Vector Shift Long
Intrinsic     vshiftl_v32_imm7_v32_ar[_p]
name
Spec syntax   vshiftl {Qop [,ar | lg]} vx[0], #imm7, vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand
Operands
              3    IN2_IMM7        int8      -64..63          7 bit immediate
              4    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vshiftl_v32_imm7_v32_ar_p (4, vIn, 2, vecPred);

                   IN_VPR last operand is relevant only for vshiftl_v32_imm7_v32_ar_p
Comments      1.
                   version.


Main table → Bit Manipulation → Shift → Vector Shift Long
Intrinsic     vshiftl_v32_imm7_v32_lg[_p]
name
Spec syntax   vshiftl {Qop [,ar | lg]} vx[0], #imm7, vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4             Number of atomic operations

2    IN1_V32         vec_t                      Input vector operand
Operands
              3    IN2_IMM7        int8      -64..63          7 bit immediate
              4    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vshiftl_v32_imm7_v32_lg_p (4, vIn, 2, vecPred);

                   IN_VPR last operand is relevant only for vshiftl_v32_imm7_v32_lg_p
Comments      1.
                   version.


Main table → Bit Manipulation → Shift → Vector Shift Long
Intrinsic     vshiftl_v32_imm7_v32[_p]
name
Spec syntax   vshiftl {Qop [,ar | lg]} vx[0], #imm7, vz[0], ?vprX

Return type   vec_t
            1    QOP             uint8     1..4             Number of atomic operations
            2    IN1_V32         vec_t                      Input vector operand
Operands
            3    IN2_IMM7        int8      -64..63          7 bit immediate
            4    IN_VPR          vprex_t                    Vector predicate operand
            vec_t vIn;
            vec_t vRes;
C example   vprex_t vecPred;
            ...
            vRes = vshiftl_v32_imm7_v32_p (4, vIn, 2, vecPred);

Comments    1.   IN_VPR last operand is relevant only for vshiftl_v32_imm7_v32_p version.


Main table → Bit Manipulation → Shift → Vector Shift Long
Intrinsic     vshiftl_v32_v32_v32_w_ar[_p]
name
Spec syntax   vshiftl {Qop, w [,ar | lg]} vx[0], vy[Ye], vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4              Number of atomic operations
              2    IN1_V32         vec_t                       Input vector operand

Operands
              3    IN2_V32         vec_t                       Input vector operand

              4    IN2_OFST        uint8     0,4
                                                               Offset for the first DW used from operand
                                                               3

              5    IN_VPR          vprex_t                     Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vshiftl_v32_v32_v32_w_ar_p (4, vIn, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for vshiftl_v32_v32_v32_w_ar_p
Comments      1.
                   version.


Main table → Bit Manipulation → Shift → Vector Shift Long

Intrinsic     vshiftl_v32_v32_v32_w_lg[_p]
name
Spec syntax   vshiftl {Qop, w [,ar | lg]} vx[0], vy[Ye], vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4              Number of atomic operations
              2    IN1_V32         vec_t                       Input vector operand

Operands
              3    IN2_V32         vec_t                       Input vector operand

              4    IN2_OFST        uint8     0,4
                                                               Offset for the first DW used from operand
                                                               3

              5    IN_VPR          vprex_t                     Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vshiftl_v32_v32_v32_w_lg_p (4, vIn, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for vshiftl_v32_v32_v32_w_lg_p
Comments      1.
                   version.


Main table → Bit Manipulation → Shift → Vector Shift Long
Intrinsic     vshiftl_v32_v32_v32_w[_p]
name
Spec syntax   vshiftl {Qop, w [,ar | lg]} vx[0], vy[Ye], vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4              Number of atomic operations
              2    IN1_V32         vec_t                       Input vector operand

Operands
              3    IN2_V32         vec_t                       Input vector operand

              4    IN2_OFST        uint8     0,4
                                                               Offset for the first DW used from operand
                                                               3

              5    IN_VPR          vprex_t                     Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vshiftl_v32_v32_v32_w_p (4, vIn, vIn2, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vshiftl_v32_v32_v32_w_p version.


Main table → Bit Manipulation → Shift → Vector Shift Long
