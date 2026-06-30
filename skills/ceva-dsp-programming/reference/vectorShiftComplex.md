# Bit Manipulation → Shift → Vector Shift Complex

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Bit Manipulation → Shift → Vector Shift Complex

Vector Shift Complex

Vector Shift Complex
Performs arithmetic or logic shift operation on complex numbers. Each complex number consists
of a real 32-bit part and an imaginary 32-bit part. The results for each complex part are placed
into 32-bit or 40-bit register destination determinedby the vector register type.
Available Switches
        Number of atomic operations. An atomic operation is defined as complex shift operation.
Qop
        1op ≤ Qop ≤ 4op
        Selects arithmetic (ar) or logic (lg) shift. When shifting right, the MSBs of the destination
ar      are sign-extended according to bit 31 for an arithmetic shift, and zero-extended for a logic
        shift. The default is an arithmetic shift.
b       Shift values are given by bytes
dw      Shift values are given by double-words
lg
w       Shift values are given by words
Intrinsic Names
vshiftx_v32_v32_v32_dw_ar
vshiftx_v32_v32_v32_dw_lg
vshiftx_v32_v32_v32_dw
vshiftx_v32_v32_v32_w_ar
vshiftx_v32_v32_v32_w_lg
vshiftx_v32_v32_v32_w
vshiftx_v32_v32_v32_b_ar
vshiftx_v32_v32_v32_b_lg
vshiftx_v32_v32_v32_b
Instruction details in the instruction set specification
Intrinsic     vshiftx_v32_v32_v32_dw_ar[_p]
name
Spec syntax   vshiftx {Qop, dw [,ar | lg]} vx[0], vy[0], vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4             Number of atomic operations
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
              vRes = vshiftx_v32_v32_v32_dw_ar_p (4, vIn, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for vshiftx_v32_v32_v32_dw_ar_p
Comments      1.
                   version.


Main table → Bit Manipulation → Shift → Vector Shift Complex
Intrinsic     vshiftx_v32_v32_v32_dw_lg[_p]
name
Spec syntax   vshiftx {Qop, dw [,ar | lg]} vx[0], vy[0], vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4             Number of atomic operations
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
              vRes = vshiftx_v32_v32_v32_dw_lg_p (4, vIn, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for vshiftx_v32_v32_v32_dw_lg_p
Comments      1.
                   version.


Main table → Bit Manipulation → Shift → Vector Shift Complex
Intrinsic     vshiftx_v32_v32_v32_dw[_p]
name
Spec syntax   vshiftx {Qop, dw [,ar | lg]} vx[0], vy[0], vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4             Number of atomic operations
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
              vRes = vshiftx_v32_v32_v32_dw_p (4, vIn, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for vshiftx_v32_v32_v32_dw_p
Comments      1.
                   version.

Main table → Bit Manipulation → Shift → Vector Shift Complex
Intrinsic     vshiftx_v32_v32_v32_w_ar[_p]
name
Spec syntax   vshiftx {Qop, w [,ar | lg]} vx[0], vy[Ye], vz[0], ?vprX

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
              vRes = vshiftx_v32_v32_v32_w_ar_p (4, vIn, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for vshiftx_v32_v32_v32_w_ar_p
Comments      1.
                   version.


Main table → Bit Manipulation → Shift → Vector Shift Complex
Intrinsic     vshiftx_v32_v32_v32_w_lg[_p]
name
Spec syntax   vshiftx {Qop, w [,ar | lg]} vx[0], vy[Ye], vz[0], ?vprX

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
              vRes = vshiftx_v32_v32_v32_w_lg_p (4, vIn, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for vshiftx_v32_v32_v32_w_lg_p
Comments      1.
                   version.


Main table → Bit Manipulation → Shift → Vector Shift Complex
Intrinsic     vshiftx_v32_v32_v32_w[_p]
name
Spec syntax   vshiftx {Qop, w [,ar | lg]} vx[0], vy[Ye], vz[0], ?vprX

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
              vRes = vshiftx_v32_v32_v32_w_p (4, vIn, vIn2, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vshiftx_v32_v32_v32_w_p version.


Main table → Bit Manipulation → Shift → Vector Shift Complex
Intrinsic     vshiftx_v32_v32_v32_b_ar[_p]
name
Spec syntax   vshiftx {Qop, b [,ar | lg]} vx[0], vy[Y], vz[0], ?vprX

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
              vRes = vshiftx_v32_v32_v32_b_ar_p (4, vIn, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for vshiftx_v32_v32_v32_b_ar_p
Comments      1.
                   version.


Main table → Bit Manipulation → Shift → Vector Shift Complex
Intrinsic     vshiftx_v32_v32_v32_b_lg[_p]
name
Spec syntax   vshiftx {Qop, b [,ar | lg]} vx[0], vy[Y], vz[0], ?vprX

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
              vRes = vshiftx_v32_v32_v32_b_lg_p (4, vIn, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for vshiftx_v32_v32_v32_b_lg_p
Comments      1.
                   version.


Main table → Bit Manipulation → Shift → Vector Shift Complex
Intrinsic     vshiftx_v32_v32_v32_b[_p]
name
Spec syntax   vshiftx {Qop, b [,ar | lg]} vx[0], vy[Y], vz[0], ?vprX

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
              vRes = vshiftx_v32_v32_v32_b_p (4, vIn, vIn2, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vshiftx_v32_v32_v32_b_p version.


Main table → Bit Manipulation → Shift → Vector Shift Complex
