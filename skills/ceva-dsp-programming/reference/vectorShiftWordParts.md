# Bit Manipulation → Shift → Vector Shift Word Parts

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Bit Manipulation → Shift → Vector Shift Word Parts

Vector Shift Word Parts

Vector Shift Word Parts
Performs two arithmetic or logic shift operations on two 16-bit sources. The results are packed
into either 32-bit or 40-bit destination determined by the register type.
Available Switches

Number of atomic operations. An atomic operation is defined as two shift operations. 1op
Oop
       ≤ Oop ≤ 8op
       Selects arithmetic (ar) or logic (lg) shift. When shifting right, the MSBs of the destinations
ar     are sign-extended according to bit 31 and bit 15 for an arithmetic shift, and zero-extended
       for a logic shift. The default is an arithmetic shift.
b      Shift values are given by bytes
lg
w      Shift values are given by words
Intrinsic Names
vshiftw_v32_imm5_v32_ar
vshiftw_v32_imm5_v32_lg
vshiftw_v32_imm5_v32
vshiftw_v32_c32p_v32_ar
vshiftw_v32_c32p_v32_lg
vshiftw_v32_c32p_v32
vshiftw_v32_v32_v32_w_ar
vshiftw_v32_v32_v32_w_lg
vshiftw_v32_v32_v32_w
vshiftw_v32_v32_v32_b_ar
vshiftw_v32_v32_v32_b_lg
vshiftw_v32_v32_v32_b
vshiftw_v32_c32_v32_ar
vshiftw_v32_c32_v32_lg
vshiftw_v32_c32_v32
Instruction details in the instruction set specification
Intrinsic     vshiftw_v32_imm5_v32_ar[_p]
name
Spec syntax   vshiftw {Oop [,ar | lg]} vx[0], #imm5, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand
Operands
              3    IN2_IMM5       int16     -16..15          5 bit immediate
              4    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vshiftw_v32_imm5_v32_ar_p (8, vIn, 2, vecPred);

                   IN_VPR last operand is relevant only for vshiftw_v32_imm5_v32_ar_p
Comments      1.
                   version.


Main table → Bit Manipulation → Shift → Vector Shift Word Parts
Intrinsic     vshiftw_v32_imm5_v32_lg[_p]
name
Spec syntax   vshiftw {Oop [,ar | lg]} vx[0], #imm5, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand
Operands
              3    IN2_IMM5       int16     -16..15          5 bit immediate
              4    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vshiftw_v32_imm5_v32_lg_p (8, vIn, 2, vecPred);

                   IN_VPR last operand is relevant only for vshiftw_v32_imm5_v32_lg_p
Comments      1.

version.


Main table → Bit Manipulation → Shift → Vector Shift Word Parts
Intrinsic     vshiftw_v32_imm5_v32[_p]
name
Spec syntax   vshiftw {Oop [,ar | lg]} vx[0], #imm5, vz[0], ?vprX

Return type   vec_t
            1    OOP            uint8     1..8             Number of atomic operations
            2    IN1_V32        vec_t                      Input vector operand
Operands
            3    IN2_IMM5       int16     -16..15          5 bit immediate
            4    IN_VPR         vprex_t                    Vector predicate operand
            vec_t vIn;
            vec_t vRes;
C example   vprex_t vecPred;
            ...
            vRes = vshiftw_v32_imm5_v32_p (8, vIn, 2, vecPred);

Comments    1.   IN_VPR last operand is relevant only for vshiftw_v32_imm5_v32_p version.


Main table → Bit Manipulation → Shift → Vector Shift Word Parts
Intrinsic     vshiftw_v32_c32p_v32_ar[_p]
name
Spec syntax   vshiftw {Oop [,ar | lg]} vx[0], vcYp, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand
Operands      3    IN2_C32        coef_t                     Coefficient operand
              4    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 3
              5    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vshiftw_v32_c32p_v32_ar_p (8, vIn, vcoefIn, LOW, vecPred);

                   IN_VPR last operand is relevant only for vshiftw_v32_c32p_v32_ar_p
Comments      1.
                   version.


Main table → Bit Manipulation → Shift → Vector Shift Word Parts
Intrinsic     vshiftw_v32_c32p_v32_lg[_p]
name
Spec syntax   vshiftw {Oop [,ar | lg]} vx[0], vcYp, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand
Operands      3    IN2_C32        coef_t                     Coefficient operand
              4    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 3
              5    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              coef_t vcoefIn;

C example     vprex_t vecPred;
              ...
              vRes = vshiftw_v32_c32p_v32_lg_p (8, vIn, vcoefIn, LOW, vecPred);

                   IN_VPR last operand is relevant only for vshiftw_v32_c32p_v32_lg_p
Comments      1.
                   version.


Main table → Bit Manipulation → Shift → Vector Shift Word Parts
Intrinsic     vshiftw_v32_c32p_v32[_p]
name
Spec syntax   vshiftw {Oop [,ar | lg]} vx[0], vcYp, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand
Operands      3    IN2_C32        coef_t                     Coefficient operand
              4    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 3
              5    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vshiftw_v32_c32p_v32_p (8, vIn, vcoefIn, LOW, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vshiftw_v32_c32p_v32_p version.


Main table → Bit Manipulation → Shift → Vector Shift Word Parts
Intrinsic     vshiftw_v32_v32_v32_w_ar[_p]
name
Spec syntax   vshiftw {Oop, w [,ar | lg]} vx[0], vy[0], vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand
Operands
              3    IN2_V32         vec_t                      Input vector operand
              4    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vshiftw_v32_v32_v32_w_ar_p (8, vIn, vIn2, vecPred);

                   IN_VPR last operand is relevant only for vshiftw_v32_v32_v32_w_ar_p
Comments      1.
                   version.


Main table → Bit Manipulation → Shift → Vector Shift Word Parts
Intrinsic     vshiftw_v32_v32_v32_w_lg[_p]
name
Spec syntax   vshiftw {Oop, w [,ar | lg]} vx[0], vy[0], vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand
Operands

3    IN2_V32         vec_t                      Input vector operand
              4    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vshiftw_v32_v32_v32_w_lg_p (8, vIn, vIn2, vecPred);

                   IN_VPR last operand is relevant only for vshiftw_v32_v32_v32_w_lg_p
Comments      1.
                   version.


Main table → Bit Manipulation → Shift → Vector Shift Word Parts
Intrinsic     vshiftw_v32_v32_v32_w[_p]
name
Spec syntax   vshiftw {Oop, w [,ar | lg]} vx[0], vy[0], vz[0], ?vprX
Return type   vec_t

              1    OOP             uint8     1..8            Number of atomic operations
              2    IN1_V32         vec_t                     Input vector operand
Operands
              3    IN2_V32         vec_t                     Input vector operand
              4    IN_VPR          vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vshiftw_v32_v32_v32_w_p (8, vIn, vIn2, vecPred);

                   IN_VPR last operand is relevant only for vshiftw_v32_v32_v32_w_p
Comments      1.
                   version.


Main table → Bit Manipulation → Shift → Vector Shift Word Parts
Intrinsic     vshiftw_v32_v32_v32_b_ar[_p]
name
Spec syntax   vshiftw {Oop, b [,ar | lg]} vx[0], vy[0], vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand

Operands
              3    IN2_V32         vec_t                      Input vector operand

              4    IN2_OFST        uint8     0,4
                                                              Offset for the first DW used from operand
                                                              3

              5    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vshiftw_v32_v32_v32_b_ar_p (8, vIn, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for vshiftw_v32_v32_v32_b_ar_p
Comments      1.
                   version.

Main table → Bit Manipulation → Shift → Vector Shift Word Parts
Intrinsic     vshiftw_v32_v32_v32_b_lg[_p]
name
Spec syntax   vshiftw {Oop, b [,ar | lg]} vx[0], vy[0], vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand

Operands
              3    IN2_V32         vec_t                      Input vector operand

              4    IN2_OFST        uint8     0,4
                                                              Offset for the first DW used from operand
                                                              3

              5    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vshiftw_v32_v32_v32_b_lg_p (8, vIn, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for vshiftw_v32_v32_v32_b_lg_p
Comments      1.
                   version.


Main table → Bit Manipulation → Shift → Vector Shift Word Parts
Intrinsic     vshiftw_v32_v32_v32_b[_p]
name
Spec syntax   vshiftw {Oop, b [,ar | lg]} vx[0], vy[0], vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand

Operands
              3    IN2_V32         vec_t                      Input vector operand

              4    IN2_OFST        uint8     0,4
                                                              Offset for the first DW used from operand
                                                              3

              5    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vshiftw_v32_v32_v32_b_p (8, vIn, vIn2, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vshiftw_v32_v32_v32_b_p version.


Main table → Bit Manipulation → Shift → Vector Shift Word Parts
Intrinsic     vshiftw_v32_c32_v32_ar[_p]
name
Spec syntax   vshiftw {Oop [,ar | lg]} vx[0], vcY, vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8              Number of atomic operations

2    IN1_V32         vec_t                       Input vector operand
Operands
              3    IN2_C32         coef_t                      Coefficient operand
              4    IN_VPR          vprex_t                     Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vshiftw_v32_c32_v32_ar_p (8, vIn, vcoefIn, vecPred);

                   IN_VPR last operand is relevant only for vshiftw_v32_c32_v32_ar_p
Comments      1.
                   version.


Main table → Bit Manipulation → Shift → Vector Shift Word Parts
Intrinsic     vshiftw_v32_c32_v32_lg[_p]
name
Spec syntax   vshiftw {Oop [,ar | lg]} vx[0], vcY, vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8              Number of atomic operations
              2    IN1_V32         vec_t                       Input vector operand
Operands
              3    IN2_C32         coef_t                      Coefficient operand
              4    IN_VPR          vprex_t                     Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vshiftw_v32_c32_v32_lg_p (8, vIn, vcoefIn, vecPred);

                   IN_VPR last operand is relevant only for vshiftw_v32_c32_v32_lg_p
Comments      1.
                   version.


Main table → Bit Manipulation → Shift → Vector Shift Word Parts
Intrinsic     vshiftw_v32_c32_v32[_p]
name
Spec syntax   vshiftw {Oop [,ar | lg]} vx[0], vcY, vz[0], ?vprX
Return type   vec_t

              1    OOP             uint8     1..8             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand
Operands
              3    IN2_C32         coef_t                     Coefficient operand
              4    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vshiftw_v32_c32_v32_p (8, vIn, vcoefIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vshiftw_v32_c32_v32_p version.


Main table → Bit Manipulation → Shift → Vector Shift Word Parts
