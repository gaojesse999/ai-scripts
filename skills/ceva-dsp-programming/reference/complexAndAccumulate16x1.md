# Multiplication → Multiply-Accumulate → Complex and Accumulate 16x1

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Multiplication → Multiply-Accumulate → Complex and Accumulate 16x1

Complex and Accumulate 16x1

Complex and Accumulate 16x1
Performs complex multiply-and-accumulate operation between complex data number, and a

complex sign (+/-1, +/-j1) control value. The data source consists of real 16-bit part and
imaginary 16-bit part. The control source consists of 1-bit real part and 1-bit imaginary part. The
results are accumulated to a 40-bits accumulators.
Available Switches
           Number of atomic operations. An atomic operation is defined as complex multiply-and-
Qop
           accumulate operation. 1op ≤ Qop ≤ 4op
Intrinsic Names
vmacwbitx3_v32_c32_v40_conj
vmacwbitx3_v32_c32_v40
Instruction details in the instruction set specification
Intrinsic     vmacwbitx3_v32_c32_v40_conj[_p]
name
Spec syntax   vmacwbitx3 {Qop [,conj]} vx[X], vcY, voz[0], ?vprX

Return type   vec40_t

              1    QOP             uint8     1..4             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand

              3    IN1_OFST        uint8     0,4
                                                              Offset for the first DW used from operand
                                                              2
Operands
              4    IN2_C32         coef_t                     Coefficient operand
              5    IN3_V40         vec40_t                    Output vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec40_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vmacwbitx3_v32_c32_v40_conj_p (4, vIn, 0, vcoefIn, vRes, vecPred);

                   IN_VPR last operand is relevant only for vmacwbitx3_v32_c32_v40_conj_p
Comments      1.
                   version.


Main table → Multiplication → Multiply-Accumulate → Complex and Accumulate 16x1
Intrinsic     vmacwbitx3_v32_c32_v40[_p]
name
Spec syntax   vmacwbitx3 {Qop [,conj]} vx[X], vcY, voz[0], ?vprX

Return type   vec40_t

              1    QOP             uint8     1..4             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand

              3    IN1_OFST        uint8     0,4
                                                              Offset for the first DW used from operand
                                                              2
Operands
              4    IN2_C32         coef_t                     Coefficient operand
              5    IN3_V40         vec40_t                    Output vector operand

6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec40_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vmacwbitx3_v32_c32_v40_p (4, vIn, 0, vcoefIn, vRes, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmacwbitx3_v32_c32_v40_p
                version.


Main table → Multiplication → Multiply-Accumulate → Complex and Accumulate 16x1
