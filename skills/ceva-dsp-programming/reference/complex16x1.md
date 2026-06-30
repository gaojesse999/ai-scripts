# Multiplication → Multiply and Add Two Products → Complex 16x1

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Multiplication → Multiply and Add Two Products → Complex 16x1
Multiply and Add Two Products

Complex 16x1 Multiply and Add Two Products

Complex 16x1 Multiply and Add Two Products
Performs complex multiply operation between complex data number, and a complex sign (+/-1,
+/-j1) control value. The data source consists of real 16-bit part and imaginary 16-bit part. The
control source consists of 1-bit real part and 1-bit imaginary part. The result consists of 20-bits
real and 20-bits imaginary parts.
Available Switches
           Number of atomic operations. An atomic operation is defined as complex multiply-and-
Qop
           add operation. 1op ≤ Qop ≤ 4op
Intrinsic Names
vmadwbitx_v32_c32_v32_conj
vmadwbitx_v32_c32_v32
Instruction details in the instruction set specification
Intrinsic     vmadwbitx_v32_c32_v32_conj[_p]
name

Spec syntax   vmadwbitx {Qop [,conj]} vx[X], vcY, vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand

              3    IN1_OFST        uint8     0,4
                                                              Offset for the first DW used from operand
                                                              2
Operands
              4    IN2_C32         coef_t                     Coefficient operand
                                                              Offset for the first DW used from the
              5    OUT_OFST        uint8     0,4
                                                              result operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vmadwbitx_v32_c32_v32_conj_p (4, vIn, 0, vcoefIn, 0, vecPred);

                   IN_VPR last operand is relevant only for vmadwbitx_v32_c32_v32_conj_p
Comments      1.
                   version.


Main table → Multiplication → Multiply and Add Two Products → Complex 16x1
Multiply and Add Two Products
Intrinsic     vmadwbitx_v32_c32_v32[_p]
name
Spec syntax   vmadwbitx {Qop [,conj]} vx[X], vcY, vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand

              3    IN1_OFST        uint8     0,4
                                                              Offset for the first DW used from operand
                                                              2
Operands
              4    IN2_C32         coef_t                     Coefficient operand
                                                              Offset for the first DW used from the
              5    OUT_OFST        uint8     0,4
                                                              result operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     coef_t vcoefIn;
              vprex_t vecPred;
            ...
            vRes = vmadwbitx_v32_c32_v32_p (4, vIn, 0, vcoefIn, 0, vecPred);

IN_VPR last operand is relevant only for vmadwbitx_v32_c32_v32_p
Comments    1.
                 version.


Main table → Multiplication → Multiply and Add Two Products → Complex 16x1
Multiply and Add Two Products
