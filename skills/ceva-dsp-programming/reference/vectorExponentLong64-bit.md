# Bit Manipulation → Exponent → Vector Exponent Long 64-bit

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Bit Manipulation → Exponent → Vector Exponent Long 64-bit

Vector Exponent Long 64-bit

Vector Exponent Long 64-bit
Returns the exponent value of the source. The source is 64-bits wide. The destination is either
16-bit or 8-bit wide determined by the vector register type.
Available Switches
         Number of atomic operations. An atomic operation is defined as a single exponent
Qop

operation. 1op ≤ Qop ≤ 4op
b        When used, the exponent values are written to bytes
uns      When used, the evaluated source operand is unsigned. The default is signed.
w        When used, the exponent values are written to words
zero     When used, if the source is zero, then the result is zero,
Intrinsic Names
vexp64_v32_v32_b
vexp64_v32_v32_b_uns
vexp64_v32_v32_b_zero
vexp64_v32_v32_b_zero_uns
vexp64_v32_v32_w
vexp64_v32_v32_w_uns
vexp64_v32_v32_w_zero
vexp64_v32_v32_w_zero_uns
Instruction details in the instruction set specification
Intrinsic     vexp64_v32_v32_b[_p]
name
Spec syntax   vexp64 {Qop ,b [,zero_sw][,uns]} vx[0], vz[Z], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4               Number of atomic operations
              2    IN1_V32         vec_t                        Input vector operand
Operands                                                        Offset for the first DW used from the
              3    OUT_OFST        uint8     0..7
                                                                result operand
              4    IN_VPR          vprex_t                      Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vexp64_v32_v32_b_p (4, vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vexp64_v32_v32_b_p version.


Main table → Bit Manipulation → Exponent → Vector Exponent Long 64-bit
Intrinsic     vexp64_v32_v32_b_uns[_p]
name
Spec syntax   vexp64 {Qop ,b [,zero_sw][,uns]} vx[0], vz[Z], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4               Number of atomic operations
              2    IN1_V32         vec_t                        Input vector operand
Operands                                                        Offset for the first DW used from the
              3    OUT_OFST        uint8     0..7
                                                                result operand
              4    IN_VPR          vprex_t                      Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vexp64_v32_v32_b_uns_p (4, vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vexp64_v32_v32_b_uns_p version.


Main table → Bit Manipulation → Exponent → Vector Exponent Long 64-bit
Intrinsic     vexp64_v32_v32_b_zero[_p]

name
Spec syntax   vexp64 {Qop ,b [,zero_sw][,uns]} vx[0], vz[Z], ?vprX

Return type   vec_t
              1    QOP             uint8     1..4            Number of atomic operations
              2    IN1_V32         vec_t                     Input vector operand
Operands                                                     Offset for the first DW used from the
              3    OUT_OFST        uint8     0..7
                                                             result operand
              4    IN_VPR          vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vexp64_v32_v32_b_zero_p (4, vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vexp64_v32_v32_b_zero_p version.


Main table → Bit Manipulation → Exponent → Vector Exponent Long 64-bit
Intrinsic     vexp64_v32_v32_b_zero_uns[_p]
name
Spec syntax   vexp64 {Qop ,b [,zero_sw][,uns]} vx[0], vz[Z], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4            Number of atomic operations
              2    IN1_V32         vec_t                     Input vector operand
Operands                                                     Offset for the first DW used from the
              3    OUT_OFST        uint8     0..7
                                                             result operand
              4    IN_VPR          vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vexp64_v32_v32_b_zero_uns_p (4, vIn, 0, vecPred);

                   IN_VPR last operand is relevant only for vexp64_v32_v32_b_zero_uns_p
Comments      1.
                   version.


Main table → Bit Manipulation → Exponent → Vector Exponent Long 64-bit
Intrinsic     vexp64_v32_v32_w[_p]
name
Spec syntax   vexp64 {Qop ,w [,zero_sw][,uns]} vx[0], vz[Ze], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4               Number of atomic operations
              2    IN1_V32         vec_t                        Input vector operand
Operands                                                        Offset for the first DW used from the
              3    OUT_OFST        uint8     0..7
                                                                result operand

4    IN_VPR          vprex_t                      Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vexp64_v32_v32_w_p (4, vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vexp64_v32_v32_w_p version.


Main table → Bit Manipulation → Exponent → Vector Exponent Long 64-bit
Intrinsic     vexp64_v32_v32_w_uns[_p]
name
Spec syntax   vexp64 {Qop ,w [,zero_sw][,uns]} vx[0], vz[Ze], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4               Number of atomic operations
              2    IN1_V32         vec_t                        Input vector operand
Operands                                                        Offset for the first DW used from the
              3    OUT_OFST        uint8     0..7
                                                                result operand
              4    IN_VPR          vprex_t                      Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vexp64_v32_v32_w_uns_p (4, vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vexp64_v32_v32_w_uns_p version.


Main table → Bit Manipulation → Exponent → Vector Exponent Long 64-bit
Intrinsic     vexp64_v32_v32_w_zero[_p]
name
Spec syntax   vexp64 {Qop ,w [,zero_sw][,uns]} vx[0], vz[Ze], ?vprX

Return type   vec_t
              1    QOP            uint8     1..4             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand
Operands                                                     Offset for the first DW used from the
              3    OUT_OFST       uint8     0..7
                                                             result operand
              4    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vexp64_v32_v32_w_zero_p (4, vIn, 0, vecPred);

                   IN_VPR last operand is relevant only for vexp64_v32_v32_w_zero_p
Comments      1.
                   version.


Main table → Bit Manipulation → Exponent → Vector Exponent Long 64-bit
Intrinsic     vexp64_v32_v32_w_zero_uns[_p]
name
Spec syntax   vexp64 {Qop ,w [,zero_sw][,uns]} vx[0], vz[Ze], ?vprX

Return type   vec_t

1    QOP            uint8     1..4             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand
Operands                                                     Offset for the first DW used from the
              3    OUT_OFST       uint8     0..7
                                                             result operand
              4    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vexp64_v32_v32_w_zero_uns_p (4, vIn, 0, vecPred);

                   IN_VPR last operand is relevant only for vexp64_v32_v32_w_zero_uns_p
Comments      1.
                   version.


Main table → Bit Manipulation → Exponent → Vector Exponent Long 64-bit
