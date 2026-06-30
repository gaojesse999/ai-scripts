# Bit Manipulation → Shift → Vector Shift Word Parts Complex

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Bit Manipulation → Shift → Vector Shift Word Parts Complex

Vector Shift Word Parts Complex

Vector Shift Word Parts Complex
Performs two arithmetic or logic shift operations on two 16-bit sources. The results are packed
into either 32-bit or 40-bit destination determined by the register type.
Available Switches
       Number of atomic operations. An atomic operation is defined as a word complex shift
Oop
       operation. 1op ≤ Oop ≤ 8op
       Selects arithmetic (ar) or logic (lg) shift. When shifting right, the MSBs of the destination
ar     are sign-extended according to bit 31 and bit 15 for an arithmetic shift, and zero-extended
       for a logic shift. The default is an arithmetic shift.
b      Shift values are given by bytes
lg
w      Shift values are given by words
Intrinsic Names
vshiftwx_v32_v32_v32_b_ar
vshiftwx_v32_v32_v32_b_lg
vshiftwx_v32_v32_v32_b
vshiftwx_v32_v32_v32_w_ar
vshiftwx_v32_v32_v32_w_lg
vshiftwx_v32_v32_v32_w
Instruction details in the instruction set specification
Intrinsic     vshiftwx_v32_v32_v32_b_ar[_p]
name
Spec syntax   vshiftwx {Oop, b [,ar | lg]} vx[0], vy[Ye], vz[0], ?vprX

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
              vRes = vshiftwx_v32_v32_v32_b_ar_p (8, vIn, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for vshiftwx_v32_v32_v32_b_ar_p
Comments      1.
                   version.


Main table → Bit Manipulation → Shift → Vector Shift Word Parts Complex
Intrinsic     vshiftwx_v32_v32_v32_b_lg[_p]
name
Spec syntax   vshiftwx {Oop, b [,ar | lg]} vx[0], vy[Ye], vz[0], ?vprX

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
              vRes = vshiftwx_v32_v32_v32_b_lg_p (8, vIn, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for vshiftwx_v32_v32_v32_b_lg_p
Comments      1.
                   version.


Main table → Bit Manipulation → Shift → Vector Shift Word Parts Complex
Intrinsic     vshiftwx_v32_v32_v32_b[_p]
name
Spec syntax   vshiftwx {Oop, b [,ar | lg]} vx[0], vy[Ye], vz[0], ?vprX

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
              vRes = vshiftwx_v32_v32_v32_b_p (8, vIn, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for vshiftwx_v32_v32_v32_b_p
Comments      1.
                   version.


Main table → Bit Manipulation → Shift → Vector Shift Word Parts Complex
Intrinsic     vshiftwx_v32_v32_v32_w_ar[_p]
name
Spec syntax   vshiftwx {Oop, w [,ar | lg]} vx[0], vy[0], vz[0], ?vprX

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
              vRes = vshiftwx_v32_v32_v32_w_ar_p (8, vIn, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for vshiftwx_v32_v32_v32_w_ar_p
Comments      1.
                   version.


Main table → Bit Manipulation → Shift → Vector Shift Word Parts Complex
Intrinsic     vshiftwx_v32_v32_v32_w_lg[_p]
name
Spec syntax   vshiftwx {Oop, w [,ar | lg]} vx[0], vy[0], vz[0], ?vprX

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
              vRes = vshiftwx_v32_v32_v32_w_lg_p (8, vIn, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for vshiftwx_v32_v32_v32_w_lg_p
Comments      1.
                   version.


Main table → Bit Manipulation → Shift → Vector Shift Word Parts Complex
Intrinsic     vshiftwx_v32_v32_v32_w[_p]
name
Spec syntax   vshiftwx {Oop, w [,ar | lg]} vx[0], vy[0], vz[0], ?vprX

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
              vRes = vshiftwx_v32_v32_v32_w_p (8, vIn, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for vshiftwx_v32_v32_v32_w_p
Comments      1.

version.


Main table → Bit Manipulation → Shift → Vector Shift Word Parts Complex
