# Bit Manipulation → Shift → Vector Shift Complex 72-bit

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Bit Manipulation → Shift → Vector Shift Complex 72-bit

Vector Shift Complex 72-bit

Vector Shift Complex 72-bit
Performs an arithmetic or logic shift operations on a complex source comprised of 72-bit image
and real parts. The results for each complex part are written into either 64-bit or 72-bit
destinations determined by the register type.
Available Switches
       Number of atomic operations. An atomic operation is defined as a complex 40-bit shift
Dop
       operation. 1op ≤ Dop ≤ 2op
       Selects arithmetic (ar) or logic (lg) shift. When shifting right, the MSBs of the destination
ar     are sign-extended according to bit 71 for an arithmetic shift, and zero-extended for a logic
       shift. The default is an arithmetic shift.
lg
w      Shift values are given by words
Intrinsic Names
vshiftx72_v40_v40_v32_w
vshiftx72_v40_v40_v32_w_s
vshiftx72_v40_v40_v32_w_us
Instruction details in the instruction set specification
Intrinsic     vshiftx72_v40_v40_v32_w[_p]
name
Spec syntax   vshiftx72 {Dop, w [,us_s]} vox[0], voy[Y], vz[0], ?vprX

Return type   vec_t

              1    DOP             uint8     1..2             Number of atomic operations
              2    IN1_V40         vec40_t                    Output vector operand

Operands

3    IN2_V40         vec40_t                    Output vector operand

              4    IN2_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
                                                              3

              5    IN_VPR          vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec40_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vshiftx72_v40_v40_v32_w_p (2, vIn, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for vshiftx72_v40_v40_v32_w_p
Comments      1.
                   version.


Main table → Bit Manipulation → Shift → Vector Shift Complex 72-bit
Intrinsic     vshiftx72_v40_v40_v32_w_s[_p]
name
Spec syntax   vshiftx72 {Dop, w [,us_s]} vox[0], voy[Y], vz[0], ?vprX

Return type   vec_t

              1    DOP             uint8     1..2             Number of atomic operations
              2    IN1_V40         vec40_t                    Output vector operand

Operands
              3    IN2_V40         vec40_t                    Output vector operand

              4    IN2_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
                                                              3

              5    IN_VPR          vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec40_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vshiftx72_v40_v40_v32_w_s_p (2, vIn, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for vshiftx72_v40_v40_v32_w_s_p
Comments      1.
                   version.


Main table → Bit Manipulation → Shift → Vector Shift Complex 72-bit
Intrinsic     vshiftx72_v40_v40_v32_w_us[_p]
name
Spec syntax   vshiftx72 {Dop, w [,us_s]} vox[0], voy[Y], vz[0], ?vprX

Return type   vec_t

              1    DOP             uint8     1..2             Number of atomic operations
              2    IN1_V40         vec40_t                    Output vector operand

Operands
              3    IN2_V40         vec40_t                    Output vector operand

              4    IN2_OFST        uint8     0..7
                                                              Offset for the first DW used from operand

3

              5    IN_VPR          vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec40_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vshiftx72_v40_v40_v32_w_us_p (2, vIn, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for vshiftx72_v40_v40_v32_w_us_p
Comments      1.
                   version.


Main table → Bit Manipulation → Shift → Vector Shift Complex 72-bit
