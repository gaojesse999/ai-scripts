# Bit Manipulation → Exponent → Vector Exponent 40-bit

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Bit Manipulation → Exponent → Vector Exponent 40-bit

Vector Exponent 40-bit

Vector Exponent 40-bit
Returns the exponent value of the source. The source is 40-bit wide. The exponent value (a 6-bit
signed number) is sign-extended before it is written to the destination. The destination is either
16-bit or 8-bit wide.
Available Switches
          Number of atomic operations. An atomic operation is defined as a single exponent
Oop
          operation. 1op ≤ Oop ≤ 8op
b         When used, the exponent values are written to bytes
inc       When used, +1 is added to the exponent result.
uns       When used, the evaluated source operand is unsigned. The default is signed.
w         When used, the exponent values are written to words
zero      When used, if the source is zero, then the result is zero.
Intrinsic Names
vexp40_v40_v32_w_inc
vexp40_v40_v32_w_inc_zero

vexp40_v40_v32_w
vexp40_v40_v32_w_uns
vexp40_v40_v32_w_uns_zero
vexp40_v40_v32_w_zero
vexp40_v40_v32_b_inc
vexp40_v40_v32_b_inc_zero
vexp40_v40_v32_b
vexp40_v40_v32_b_uns
vexp40_v40_v32_b_uns_zero
vexp40_v40_v32_b_zero
Instruction details in the instruction set specification
Intrinsic     vexp40_v40_v32_w_inc[_p]
name
Spec syntax   vexp40 {Oop ,w [,uns_inc][,zero_sw]} vox[0], vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V40        vec40_t                    Output vector operand
Operands                                                     Offset for the first DW used from the
              3    OUT_OFST       uint8     0,4
                                                             result operand
              4    IN_VPR         vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vexp40_v40_v32_w_inc_p (8, vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vexp40_v40_v32_w_inc_p version.


Main table → Bit Manipulation → Exponent → Vector Exponent 40-bit
Intrinsic     vexp40_v40_v32_w_inc_zero[_p]
name
Spec syntax   vexp40 {Oop ,w [,uns_inc][,zero_sw]} vox[0], vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V40        vec40_t                    Output vector operand
Operands                                                     Offset for the first DW used from the
              3    OUT_OFST       uint8     0,4
                                                             result operand
              4    IN_VPR         vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vexp40_v40_v32_w_inc_zero_p (8, vIn, 0, vecPred);

                   IN_VPR last operand is relevant only for vexp40_v40_v32_w_inc_zero_p
Comments      1.
                   version.


Main table → Bit Manipulation → Exponent → Vector Exponent 40-bit
Intrinsic     vexp40_v40_v32_w[_p]
name
Spec syntax   vexp40 {Oop ,w [,uns_inc][,zero_sw]} vox[0], vz[0], ?vprX
Return type   vec_t

              1    OOP            uint8      1..8               Number of atomic operations

2    IN1_V40        vec40_t                       Output vector operand
Operands                                                        Offset for the first DW used from the
              3    OUT_OFST       uint8      0,4
                                                                result operand
              4    IN_VPR         vprex_t                       Vector predicate operand
              vec40_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vexp40_v40_v32_w_p (8, vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vexp40_v40_v32_w_p version.


Main table → Bit Manipulation → Exponent → Vector Exponent 40-bit
Intrinsic     vexp40_v40_v32_w_uns[_p]
name
Spec syntax   vexp40 {Oop ,w [,uns_inc][,zero_sw]} vox[0], vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8      1..8               Number of atomic operations
              2    IN1_V40        vec40_t                       Output vector operand
Operands                                                        Offset for the first DW used from the
              3    OUT_OFST       uint8      0,4
                                                                result operand
              4    IN_VPR         vprex_t                       Vector predicate operand
              vec40_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vexp40_v40_v32_w_uns_p (8, vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vexp40_v40_v32_w_uns_p version.


Main table → Bit Manipulation → Exponent → Vector Exponent 40-bit
Intrinsic     vexp40_v40_v32_w_uns_zero[_p]
name
Spec syntax   vexp40 {Oop ,w [,uns_inc][,zero_sw]} vox[0], vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8      1..8               Number of atomic operations
Operands      2    IN1_V40        vec40_t                       Output vector operand
              3    OUT_OFST       uint8      0,4                Offset for the first DW used from the
                                                             result operand
              4    IN_VPR         vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vexp40_v40_v32_w_uns_zero_p (8, vIn, 0, vecPred);

IN_VPR last operand is relevant only for vexp40_v40_v32_w_uns_zero_p
Comments      1.
                   version.


Main table → Bit Manipulation → Exponent → Vector Exponent 40-bit
Intrinsic     vexp40_v40_v32_w_zero[_p]
name
Spec syntax   vexp40 {Oop ,w [,uns_inc][,zero_sw]} vox[0], vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V40        vec40_t                    Output vector operand
Operands                                                     Offset for the first DW used from the
              3    OUT_OFST       uint8     0,4
                                                             result operand
              4    IN_VPR         vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vexp40_v40_v32_w_zero_p (8, vIn, 0, vecPred);

                   IN_VPR last operand is relevant only for vexp40_v40_v32_w_zero_p
Comments      1.
                   version.


Main table → Bit Manipulation → Exponent → Vector Exponent 40-bit
Intrinsic     vexp40_v40_v32_b_inc[_p]
name
Spec syntax   vexp40 {Oop ,b [,uns_inc][,zero_sw]} vox[0], vz[Ze], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8             Number of atomic operations
              2    IN1_V40         vec40_t                    Output vector operand
Operands                                                      Offset for the first DW used from the
              3    OUT_OFST        uint8     0,2,4,6
                                                              result operand
              4    IN_VPR          vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vexp40_v40_v32_b_inc_p (8, vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vexp40_v40_v32_b_inc_p version.


Main table → Bit Manipulation → Exponent → Vector Exponent 40-bit
Intrinsic     vexp40_v40_v32_b_inc_zero[_p]
name
Spec syntax   vexp40 {Oop ,b [,uns_inc][,zero_sw]} vox[0], vz[Ze], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8             Number of atomic operations
              2    IN1_V40         vec40_t                    Output vector operand

Operands                                                      Offset for the first DW used from the
              3    OUT_OFST        uint8     0,2,4,6
                                                              result operand
              4    IN_VPR          vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vexp40_v40_v32_b_inc_zero_p (8, vIn, 0, vecPred);

                   IN_VPR last operand is relevant only for vexp40_v40_v32_b_inc_zero_p
Comments      1.
                   version.


Main table → Bit Manipulation → Exponent → Vector Exponent 40-bit
Intrinsic     vexp40_v40_v32_b[_p]
name
Spec syntax   vexp40 {Oop ,b [,uns_inc][,zero_sw]} vox[0], vz[Ze], ?vprX
Return type   vec_t

              1    OOP             uint8     1..8               Number of atomic operations
              2    IN1_V40         vec40_t                      Output vector operand
Operands                                                        Offset for the first DW used from the
              3    OUT_OFST        uint8     0,2,4,6
                                                                result operand
              4    IN_VPR          vprex_t                      Vector predicate operand
              vec40_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vexp40_v40_v32_b_p (8, vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vexp40_v40_v32_b_p version.


Main table → Bit Manipulation → Exponent → Vector Exponent 40-bit
Intrinsic     vexp40_v40_v32_b_uns[_p]
name
Spec syntax   vexp40 {Oop ,b [,uns_inc][,zero_sw]} vox[0], vz[Ze], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8               Number of atomic operations
              2    IN1_V40         vec40_t                      Output vector operand
Operands                                                        Offset for the first DW used from the
              3    OUT_OFST        uint8     0,2,4,6
                                                                result operand
              4    IN_VPR          vprex_t                      Vector predicate operand
              vec40_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vexp40_v40_v32_b_uns_p (8, vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vexp40_v40_v32_b_uns_p version.


Main table → Bit Manipulation → Exponent → Vector Exponent 40-bit
Intrinsic     vexp40_v40_v32_b_uns_zero[_p]
name
Spec syntax   vexp40 {Oop ,b [,uns_inc][,zero_sw]} vox[0], vz[Ze], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8               Number of atomic operations
Operands      2    IN1_V40         vec40_t                      Output vector operand
              3    OUT_OFST        uint8     0,2,4,6            Offset for the first DW used from the
                                                             result operand
              4    IN_VPR         vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vexp40_v40_v32_b_uns_zero_p (8, vIn, 0, vecPred);

                   IN_VPR last operand is relevant only for vexp40_v40_v32_b_uns_zero_p
Comments      1.
                   version.


Main table → Bit Manipulation → Exponent → Vector Exponent 40-bit
Intrinsic     vexp40_v40_v32_b_zero[_p]
name
Spec syntax   vexp40 {Oop ,b [,uns_inc][,zero_sw]} vox[0], vz[Ze], ?vprX

Return type   vec_t

              1    OOP            uint8      1..8            Number of atomic operations
              2    IN1_V40        vec40_t                    Output vector operand
Operands                                                     Offset for the first DW used from the
              3    OUT_OFST       uint8      0,2,4,6
                                                             result operand
              4    IN_VPR         vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vexp40_v40_v32_b_zero_p (8, vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vexp40_v40_v32_b_zero_p version.


Main table → Bit Manipulation → Exponent → Vector Exponent 40-bit
