# Multiplication → Multiply and Add Two Products → 16x1 Multiply and

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Multiplication → Multiply and Add Two Products → 16x1 Multiply and
Add Four Products

16x1 Multiply and Add Four Products

16x1 Multiply and Add Four Products
Performs four real multiply-and-add operation between real data numbers and real sign (+/-1)
control numbers. Each of the four data sources consists of 16-bit real number. Each of the four
real sign control sources consists of 1-bit real part. Each of data is multiplied by the 1-bit control
real value. The four products are summed togather, producing a 20-bits result for each part (real,
imaginary).
Available Switches
     Number of atomic operations. An atomic operation is defined as quad 16*1-bit real
     multiply-and-add four products operation. Used for two vector sources, while the first
Qhop
     vector is always fully used, the second vector number of atomic operation is set by Qhop.
     3op œ Qhop œ 4op
Intrinsic Names
vmadwbit3_v32_v32_c32_v32
vmadwbit3_v32_c32_v32
Instruction details in the instruction set specification
Intrinsic     vmadwbit3_v32_v32_c32_v32[_p]
name
Spec syntax   vmadwbit3 {Qhop} vx[X], vy[Y], vcV, vz[0], ?vprX

Return type   vec_t

              1    QHOP            uint8     3..4             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand

              3    IN1_OFST        uint8     0,4
                                                              Offset for the first DW used from operand
                                                              2

              4    IN2_V32         vec_t                      Input vector operand
Operands                                                      Offset for the first DW used from operand
              5    IN2_OFST        uint8     0,4
                                                              4

              6    IN3_C32         coef_t                     Coefficient operand
                                                              Offset for the first DW used from the
              7    OUT_OFST        uint8     0,4
                                                              result operand
              8    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;

C example     coef_t vcoefIn;
              vprex_t vecPred;
              ...
              vRes = vmadwbit3_v32_v32_c32_v32_p (4, vIn, 0, vIn2, 0, vcoefIn, 0, vecPred);

                   IN_VPR last operand is relevant only for vmadwbit3_v32_v32_c32_v32_p
Comments      1.
                   version.


Main table → Multiplication → Multiply and Add Two Products → 16x1 Multiply and
Add Four Products
Intrinsic     vmadwbit3_v32_c32_v32[_p]
name
Spec syntax   vmadwbit3 {Dop} vx[X], vcYp, vz[Ze], ?vprX

Return type   vec_t

              1    DOP            uint8     1..2             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0,4
                                                             Offset for the first DW used from operand
                                                             2

Operands      4    IN2_C32        coef_t                     Coefficient operand
              5    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 4

              6
                                                             Offset for the first DW used from the
                   OUT_OFST       uint8     0,4
                                                             result operand
              7    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vmadwbit3_v32_c32_v32_p (2, vIn, 0, vcoefIn, LOW, 0, vecPred);

                   IN_VPR last operand is relevant only for vmadwbit3_v32_c32_v32_p
Comments      1.
                   version.


Main table → Multiplication → Multiply and Add Two Products → 16x1 Multiply and
Add Four Products

Main table → Multiplication → Multiply and Add Two Products → 16x1 Multiply and
Add Two Products

16x1 Multiply and Add Two Products

16x1 Multiply and Add Two Products
Performs two real multiply-and-add operation between real data numbers and real sign (+/-1)
control numbers. Each of the two data sources consists of 16-bit real number. Each of the two
real sign control sources consists of 1-bit real part. Each of data is multiplied by the 1-bit control
real value. The two products are summed togather, producing a 20-bits result for each part (real,
imaginary).
Available Switches

Number of atomic operations. An atomic operation is defined as double 16*1-bit real
     multiply-and-add operation.Used for two vector sources, while the first vector is always
Ohop
     fully used, the second vector number of atomic operation is set by Ohop. 5op œ Ohop œ
     8op
Intrinsic Names
vmadwbit_v32_c32_v32
vmadwbit_v32_v32_c32_v32
Instruction details in the instruction set specification
Intrinsic     vmadwbit_v32_c32_v32[_p]
name
Spec syntax   vmadwbit {Qop} vx[X], vcYp, vz[0], ?vprX

Return type   vec_t

              1    QOP            uint8     1..4             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0,4
                                                             Offset for the first DW used from operand
                                                             2

Operands      4    IN2_C32        coef_t                     Coefficient operand
              5    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 4

              6
                                                             Offset for the first DW used from the
                   OUT_OFST       uint8     0,4
                                                             result operand
              7    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vmadwbit_v32_c32_v32_p (4, vIn, 0, vcoefIn, LOW, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmadwbit_v32_c32_v32_p version.


Main table → Multiplication → Multiply and Add Two Products → 16x1 Multiply and
Add Two Products
Intrinsic     vmadwbit_v32_v32_c32_v32[_p]
name
Spec syntax   vmadwbit {Ohop} vx[X], vy[Y], vcV, vz[0], ?vprX

Return type   vec_t

              1    OHOP            uint8     5..8             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand

              3    IN1_OFST        uint8     0,4
                                                              Offset for the first DW used from operand
                                                              2

Operands      4    IN2_V32         vec_t                      Input vector operand

              5    IN2_OFST        uint8     0,4

Offset for the first DW used from operand
                                                              4

              6    IN3_C32         coef_t                     Coefficient operand
              7    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     coef_t vcoefIn;
              vprex_t vecPred;
              ...
              vRes = vmadwbit_v32_v32_c32_v32_p (8, vIn, 0, vIn2, 0, vcoefIn, vecPred);

                   IN_VPR last operand is relevant only for vmadwbit_v32_v32_c32_v32_p
Comments      1.
                   version.


Main table → Multiplication → Multiply and Add Two Products → 16x1 Multiply and
Add Two Products
