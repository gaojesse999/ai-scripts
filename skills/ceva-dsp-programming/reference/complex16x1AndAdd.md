# Multiplication → Multiply → Complex 16x1 and Add

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Multiplication → Multiply → Complex 16x1 and Add

Complex 16x1 and Add

Complex 16x1 and Add
Performs complex multiply operation between complex number and complex sign (+/-1, +/-j1)
control. The data source consists of real 16-bit part and imaginary 16-bit part. The control source
consists of 1-bit real part and 1-bit imaginary part. The real and the imaginary results are written
each into 20-bit destination.
Available Switches
           Number of atomic operations. An atomic operation is defined as single complex
Oop
           multiply operation. 1op ≤ Oop ≤ 8op
Intrinsic Names
vmpywbitx_v32X_c32_v32_conj
vmpywbitx_v32X_c32_v32
vmpywbitx_v32_c32_v32_conj
vmpywbitx_v32_c32_v32
Instruction details in the instruction set specification
Intrinsic     vmpywbitx_v32X_c32_v32_conj[_p]
name
Spec syntax   vmpywbitx {Oop [,conj]} vx[X], vcYp, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            2
Operands
              4    IN2_C32        coef_t                    Coefficient operand
              5    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 4
              6    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vmpywbitx_v32X_c32_v32_conj_p (8, vIn, 0, vcoefIn, LOW, vecPred);

                   IN_VPR last operand is relevant only for vmpywbitx_v32X_c32_v32_conj_p
Comments      1.

version.


Main table → Multiplication → Multiply → Complex 16x1 and Add
Intrinsic     vmpywbitx_v32X_c32_v32[_p]
name
Spec syntax   vmpywbitx {Oop [,conj]} vx[X], vcYp, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            2
Operands
              4    IN2_C32        coef_t                    Coefficient operand
              5    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 4
              6    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vmpywbitx_v32X_c32_v32_p (8, vIn, 0, vcoefIn, LOW, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmpywbitx_v32X_c32_v32_p
                version.


Main table → Multiplication → Multiply → Complex 16x1 and Add
Intrinsic     vmpywbitx_v32_c32_v32_conj[_p]
name
Spec syntax   vmpywbitx {Oop [,conj]} vx[0], vcYp, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand
Operands      3    IN2_C32        coef_t                    Coefficient operand
              4    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 3
              5    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vmpywbitx_v32_c32_v32_conj_p (8, vIn, vcoefIn, LOW, vecPred);

                   IN_VPR last operand is relevant only for vmpywbitx_v32_c32_v32_conj_p
Comments      1.
                   version.


Main table → Multiplication → Multiply → Complex 16x1 and Add
Intrinsic     vmpywbitx_v32_c32_v32[_p]
name
Spec syntax   vmpywbitx {Oop [,conj]} vx[0], vcYp, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations

2    IN1_V32        vec_t                     Input vector operand
Operands      3    IN2_C32        coef_t                    Coefficient operand
              4    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 3
              5    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vmpywbitx_v32_c32_v32_p (8, vIn, vcoefIn, LOW, vecPred);

                   IN_VPR last operand is relevant only for vmpywbitx_v32_c32_v32_p
Comments      1.
                   version.


Main table → Multiplication → Multiply → Complex 16x1 and Add
