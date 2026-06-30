# Bit Manipulation → Exponent → Vector Complex Exponent 32-bit

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Bit Manipulation → Exponent → Vector Complex Exponent 32-bit

Vector Complex Exponent 32-bit

Vector Complex Exponent 32-bit
Outputs an exponent value for a complex number. Each complex source consists of real 40-bit
part and imaginary 40-bit part. The exponent is written either to 16-bit or 20-bit register.
Available Switches
     Number of atomic operations. An atomic operation is defined as complex exponent
     number.Used for two vector destinations, while the first vector destination is always fully
Ohop

written, the second vector destination number of atomic operation is set by Ohop. 5op œ
     Ohop œ 8op
         Number of atomic operations. An atomic operation is defined as complex exponent
Qop
         number. 1op ≤ Qop ≤ 4op
         When used, the sources represented by the 32-bits of the vector part are treated as
uns
         unsigned values (by default they are treated as signed values).
w        When used, the exponent values are written to words
zero     When used, if the source is zero, then the result is zero.
Intrinsic Names
vexpx40_v40_v40_v32_w
vexpx40_v40_v40_v32_w_uns
vexpx40_v40_v40_v32_w_zero
vexpx40_v40_v40_v32_w_zero_uns
vexpx40_v40_v32_w
vexpx40_v40_v32_w_uns
vexpx40_v40_v32_w_zero
vexpx40_v40_v32_w_zero_uns
Instruction details in the instruction set specification
Intrinsic     vexpx40_v40_v40_v32_w[_p]
name
Spec syntax   vexpx40 {Ohop ,w [,zero_sw][,uns]} vox[0], voy[0], vz[0], ?vprX

Return type   vec_t

              1    OHOP           uint8     5..8             Number of atomic operations
              2    IN1_V40        vec40_t                    Output vector operand
              3    IN2_V40        vec40_t                    Output vector operand
Operands
                                                             Offset for the first DW used from the
              4    OUT_OFST       uint8     0,4
                                                             result operand
              5    IN_VPR         vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec40_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vexpx40_v40_v40_v32_w_p (8, vIn, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for vexpx40_v40_v40_v32_w_p
Comments      1.
                   version.


Main table → Bit Manipulation → Exponent → Vector Complex Exponent 32-bit
Intrinsic     vexpx40_v40_v40_v32_w_uns[_p]
name
Spec syntax   vexpx40 {Ohop ,w [,zero_sw][,uns]} vox[0], voy[0], vz[0], ?vprX

Return type   vec_t

              1    OHOP           uint8     5..8             Number of atomic operations
              2    IN1_V40        vec40_t                    Output vector operand
              3    IN2_V40        vec40_t                    Output vector operand
Operands
                                                             Offset for the first DW used from the
              4    OUT_OFST       uint8     0,4

result operand
              5    IN_VPR         vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec40_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vexpx40_v40_v40_v32_w_uns_p (8, vIn, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for vexpx40_v40_v40_v32_w_uns_p
Comments      1.
                   version.

Main table → Bit Manipulation → Exponent → Vector Complex Exponent 32-bit
Intrinsic     vexpx40_v40_v40_v32_w_zero[_p]
name
Spec syntax   vexpx40 {Ohop ,w [,zero_sw][,uns]} vox[0], voy[0], vz[0], ?vprX

Return type   vec_t

              1    OHOP           uint8     5..8             Number of atomic operations
              2    IN1_V40        vec40_t                    Output vector operand
              3    IN2_V40        vec40_t                    Output vector operand
Operands
                                                             Offset for the first DW used from the
              4    OUT_OFST       uint8     0,4
                                                             result operand
              5    IN_VPR         vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec40_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vexpx40_v40_v40_v32_w_zero_p (8, vIn, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for vexpx40_v40_v40_v32_w_zero_p
Comments      1.
                   version.


Main table → Bit Manipulation → Exponent → Vector Complex Exponent 32-bit
Intrinsic     vexpx40_v40_v40_v32_w_zero_uns[_p]
name
Spec syntax   vexpx40 {Ohop ,w [,zero_sw][,uns]} vox[0], voy[0], vz[0], ?vprX

Return type   vec_t

              1    OHOP           uint8     5..8             Number of atomic operations
              2    IN1_V40        vec40_t                    Output vector operand
              3    IN2_V40        vec40_t                    Output vector operand
Operands
                                                             Offset for the first DW used from the
              4    OUT_OFST       uint8     0,4
                                                             result operand
              5    IN_VPR         vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec40_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;

...
              vRes = vexpx40_v40_v40_v32_w_zero_uns_p (8, vIn, vIn2, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for
                vexpx40_v40_v40_v32_w_zero_uns_p version.


Main table → Bit Manipulation → Exponent → Vector Complex Exponent 32-bit
Intrinsic     vexpx40_v40_v32_w[_p]
name
Spec syntax   vexpx40 {Qop ,w [,zero_sw][,uns]} vox[0], vz[Ze], ?vprX

Return type   vec_t

              1    QOP            uint8     1..4             Number of atomic operations
              2    IN1_V40        vec40_t                    Output vector operand
Operands                                                     Offset for the first DW used from the
              3    OUT_OFST       uint8     0,4
                                                             result operand
              4    IN_VPR         vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vexpx40_v40_v32_w_p (4, vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vexpx40_v40_v32_w_p version.


Main table → Bit Manipulation → Exponent → Vector Complex Exponent 32-bit
Intrinsic     vexpx40_v40_v32_w_uns[_p]
name
Spec syntax   vexpx40 {Qop ,w [,zero_sw][,uns]} vox[0], vz[Ze], ?vprX

Return type   vec_t

              1    QOP            uint8     1..4             Number of atomic operations
              2    IN1_V40        vec40_t                    Output vector operand
Operands                                                     Offset for the first DW used from the
              3    OUT_OFST       uint8     0,4
                                                             result operand
              4    IN_VPR         vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vexpx40_v40_v32_w_uns_p (4, vIn, 0, vecPred);

                   IN_VPR last operand is relevant only for vexpx40_v40_v32_w_uns_p
Comments      1.
                   version.


Main table → Bit Manipulation → Exponent → Vector Complex Exponent 32-bit
Intrinsic     vexpx40_v40_v32_w_zero[_p]
name
Spec syntax   vexpx40 {Qop ,w [,zero_sw][,uns]} vox[0], vz[Ze], ?vprX
Return type   vec_t

              1    QOP            uint8     1..4             Number of atomic operations

2    IN1_V40        vec40_t                    Output vector operand
Operands                                                     Offset for the first DW used from the
              3    OUT_OFST       uint8     0,4
                                                             result operand
              4    IN_VPR         vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vexpx40_v40_v32_w_zero_p (4, vIn, 0, vecPred);

                   IN_VPR last operand is relevant only for vexpx40_v40_v32_w_zero_p
Comments      1.
                   version.


Main table → Bit Manipulation → Exponent → Vector Complex Exponent 32-bit
Intrinsic     vexpx40_v40_v32_w_zero_uns[_p]
name
Spec syntax   vexpx40 {Qop ,w [,zero_sw][,uns]} vox[0], vz[Ze], ?vprX

Return type   vec_t

              1    QOP            uint8     1..4             Number of atomic operations
              2    IN1_V40        vec40_t                    Output vector operand
Operands                                                     Offset for the first DW used from the
              3    OUT_OFST       uint8     0,4
                                                             result operand
              4    IN_VPR         vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vexpx40_v40_v32_w_zero_uns_p (4, vIn, 0, vecPred);

                   IN_VPR last operand is relevant only for vexpx40_v40_v32_w_zero_uns_p
Comments      1.
                   version.


Main table → Bit Manipulation → Exponent → Vector Complex Exponent 32-bit
