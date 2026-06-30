# Bit Manipulation → Shift → Vector Shift Complex 40-bit

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Bit Manipulation → Shift → Vector Shift Complex 40-bit

Vector Shift Complex 40-bit

Vector Shift Complex 40-bit
Performs an arithmetic or logic shift operations on a complex source comprised of 40-bit image
and real parts. The results for each complex part are written into either 32-bit or 40-bit
destinations determined by the register type.
Available Switches
        Number of atomic operations. An atomic operation is defined as a complex 40-bit shift
Qop
        operation. 1op ≤ Qop ≤ 4op
        Signed saturation, when used the shifted number is regarded as a signed value. When
s
        shifting right, the MSBs of the destination are sign-extended according to bit 39.
        Unsigned saturation, when used the shifted number saturation is regarded as an unsigned

us      value. When shifting right, the MSBs of the destination are zero-extended according to bit
        39.
w       Shift values are given by words
Intrinsic Names
vshiftx40_v40_v40_v32_w
vshiftx40_v40_v40_v32_w_s
vshiftx40_v40_v40_v32_w_us
Instruction details in the instruction set specification
Intrinsic     vshiftx40_v40_v40_v32_w[_p]
name
Spec syntax   vshiftx40 {Qop, w [,us_s]} vox[0], voy[Ye], vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4             Number of atomic operations
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
              vRes = vshiftx40_v40_v40_v32_w_p (4, vIn, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for vshiftx40_v40_v40_v32_w_p
Comments      1.
                   version.


Main table → Bit Manipulation → Shift → Vector Shift Complex 40-bit
Intrinsic     vshiftx40_v40_v40_v32_w_s[_p]
name
Spec syntax   vshiftx40 {Qop, w [,us_s]} vox[0], voy[Ye], vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4             Number of atomic operations
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
              vRes = vshiftx40_v40_v40_v32_w_s_p (4, vIn, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for vshiftx40_v40_v40_v32_w_s_p
Comments      1.
                   version.

Main table → Bit Manipulation → Shift → Vector Shift Complex 40-bit
Intrinsic     vshiftx40_v40_v40_v32_w_us[_p]
name
Spec syntax   vshiftx40 {Qop, w [,us_s]} vox[0], voy[Ye], vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4             Number of atomic operations
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
              vRes = vshiftx40_v40_v40_v32_w_us_p (4, vIn, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for vshiftx40_v40_v40_v32_w_us_p
Comments      1.
                   version.


Main table → Bit Manipulation → Shift → Vector Shift Complex 40-bit
