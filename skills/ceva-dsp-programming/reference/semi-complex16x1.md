# Multiplication → Multiply and Add Two Products → Semi-Complex 16x1

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Multiplication → Multiply and Add Two Products → Semi-Complex 16x1
Multiply and Add Four Products

Semi-Complex 16x1 Multiply and Add Four Products

Semi-Complex 16x1 Multiply and Add Four Products
Performs four semi-complex multiply-and-add operation between complex data numbers and
real sign (+/-1) control numbers. Each of the four data sources consists of real 16-bit part and
imaginary 16-bit part. Each of the four real sign control sources consists of 1-bit real part. Each
of complex data is multiplied by a 1-bit control real value. The four complex products are
summed togather, producing a complex 20-bits result.
Available Switches
     Number of atomic operations. An atomic operation is defined as quad 16*1-bit semi-
     complex multiply-and-add four products operation. Used for two vector sources, while
Qhop
     the first vector is always fully used, the second vector number of atomic operation is set
     by Qhop. 3op œ Qhop œ 4op
Intrinsic Names
vmadwbitxr3_v32_c32_v32_conj
vmadwbitxr3_v32_c32_v32
vmadwbitxr3_v32_v32_c32_v32_conj
vmadwbitxr3_v32_v32_c32_v32
Instruction details in the instruction set specification
Intrinsic     vmadwbitxr3_v32_c32_v32_conj[_p]
name
Spec syntax   vmadwbitxr3 {Dop [,conj]} vx[X], vcYb, vz[Ze], ?vprX

Return type   vec_t

              1    DOP             uint8     1..2             Number of atomic operations
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

vRes = vmadwbitxr3_v32_c32_v32_conj_p (2, vIn, 0, vcoefIn, 0, vecPred);

                   IN_VPR last operand is relevant only for vmadwbitxr3_v32_c32_v32_conj_p
Comments      1.
                   version.


Main table → Multiplication → Multiply and Add Two Products → Semi-Complex 16x1
Multiply and Add Four Products
Intrinsic     vmadwbitxr3_v32_c32_v32[_p]
name
Spec syntax   vmadwbitxr3 {Dop [,conj]} vx[X], vcYb, vz[Ze], ?vprX

Return type   vec_t

              1    DOP             uint8     1..2             Number of atomic operations
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
            vRes = vmadwbitxr3_v32_c32_v32_p (2, vIn, 0, vcoefIn, 0, vecPred);

                 IN_VPR last operand is relevant only for vmadwbitxr3_v32_c32_v32_p
Comments    1.
                 version.


Main table → Multiplication → Multiply and Add Two Products → Semi-Complex 16x1
Multiply and Add Four Products
Intrinsic     vmadwbitxr3_v32_v32_c32_v32_conj[_p]
name
Spec syntax   vmadwbitxr3 {Qhop [,conj]} vx[0], vy[0], vcVp, vz[0], ?vprX

Return type   vec_t

              1    QHOP           uint8     3..4             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              4    IN3_C32        coef_t                     Coefficient operand
Operands
              5    IN3_PART       uint8     LOW,HIGH         Word part which is used for operand 4
                                                             Offset for the first DW used from the
              6    OUT_OFST       uint8     0,4

result operand
              7    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     coef_t vcoefIn;
              vprex_t vecPred;
              ...
              vRes = vmadwbitxr3_v32_v32_c32_v32_conj_p (4, vIn, vIn2, vcoefIn, LOW, 0, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmadwbitxr3_v32_v32_c32_v32_conj_p version.


Main table → Multiplication → Multiply and Add Two Products → Semi-Complex 16x1
Multiply and Add Four Products
Intrinsic     vmadwbitxr3_v32_v32_c32_v32[_p]
name
Spec syntax   vmadwbitxr3 {Qhop [,conj]} vx[0], vy[0], vcVp, vz[0], ?vprX

Return type   vec_t

              1    QHOP           uint8     3..4             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              4    IN3_C32        coef_t                     Coefficient operand
Operands
              5    IN3_PART       uint8     LOW,HIGH         Word part which is used for operand 4

              6
                                                             Offset for the first DW used from the
                   OUT_OFST       uint8     0,4
                                                             result operand
              7    IN_VPR         vprex_t                    Vector predicate operand
C example     vec_t vIn;
            vec_t vIn2;
            vec_t vRes;
            coef_t vcoefIn;
            vprex_t vecPred;
            ...
            vRes = vmadwbitxr3_v32_v32_c32_v32_p (4, vIn, vIn2, vcoefIn, LOW, 0, vecPred);

                 IN_VPR last operand is relevant only for vmadwbitxr3_v32_v32_c32_v32_p
Comments    1.
                 version.


Main table → Multiplication → Multiply and Add Two Products → Semi-Complex 16x1
Multiply and Add Four Products

Main table → Multiplication → Multiply and Add Two Products → Semi-Complex 16x1
Multiply and Add Two Products

Semi-Complex 16x1 Multiply and Add Two Products

Semi-Complex 16x1 Multiply and Add Two Products
Performs two semi-complex multiply-and-add operation between complex data numbers and real
sign (+/-1) control numbers. Each of the two data sources consists of real 16-bit part and
imaginary 16-bit part. Each of the two real sign control sources consists of 1-bit real part. Each

of complex data is multiplied by a 1-bit control real value. The two complex products are
summed togather, producing a complex 20-bits result.
Available Switches
     Number of atomic operations. An atomic operation is defined as double 16*1-bit semi-
     complex multiply-and-add operation.Used for two vector sources, while the first vector
Ohop
     is always fully used, the second vector number of atomic operation is set by Ohop. 5op œ
     Ohop œ 8op
Intrinsic Names
vmadwbitxr_v32_c32_v32_conj
vmadwbitxr_v32_c32_v32
vmadwbitxr_v32_v32_c32_v32_conj
vmadwbitxr_v32_v32_c32_v32
Instruction details in the instruction set specification
Intrinsic     vmadwbitxr_v32_c32_v32_conj[_p]
name
Spec syntax   vmadwbitxr {Qop [,conj]} vx[X], vcYb, vz[0], ?vprX

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
              vRes = vmadwbitxr_v32_c32_v32_conj_p (4, vIn, 0, vcoefIn, 0, vecPred);

                   IN_VPR last operand is relevant only for vmadwbitxr_v32_c32_v32_conj_p
Comments      1.
                   version.


Main table → Multiplication → Multiply and Add Two Products → Semi-Complex 16x1
Multiply and Add Two Products
Intrinsic     vmadwbitxr_v32_c32_v32[_p]
name
Spec syntax   vmadwbitxr {Qop [,conj]} vx[X], vcYb, vz[0], ?vprX

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
            vRes = vmadwbitxr_v32_c32_v32_p (4, vIn, 0, vcoefIn, 0, vecPred);

                 IN_VPR last operand is relevant only for vmadwbitxr_v32_c32_v32_p
Comments    1.
                 version.


Main table → Multiplication → Multiply and Add Two Products → Semi-Complex 16x1
Multiply and Add Two Products
Intrinsic     vmadwbitxr_v32_v32_c32_v32_conj[_p]
name
Spec syntax   vmadwbitxr {Ohop [,conj]} vx[0], vy[0], vcVp, vz[0], ?vprX

Return type   vec_t

              1    OHOP           uint8     5..8            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
Operands
              4    IN3_C32        coef_t                    Coefficient operand
              5    IN3_PART       uint8     LOW,HIGH        Word part which is used for operand 4
              6    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     coef_t vcoefIn;
              vprex_t vecPred;
              ...
              vRes = vmadwbitxr_v32_v32_c32_v32_conj_p (8, vIn, vIn2, vcoefIn, LOW, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmadwbitxr_v32_v32_c32_v32_conj_p version.


Main table → Multiplication → Multiply and Add Two Products → Semi-Complex 16x1
Multiply and Add Two Products
Intrinsic     vmadwbitxr_v32_v32_c32_v32[_p]
name
Spec syntax   vmadwbitxr {Ohop [,conj]} vx[0], vy[0], vcVp, vz[0], ?vprX

Return type   vec_t

              1    OHOP           uint8     5..8            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
Operands

4    IN3_C32        coef_t                    Coefficient operand
              5    IN3_PART       uint8     LOW,HIGH        Word part which is used for operand 4
              6    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     coef_t vcoefIn;
              vprex_t vecPred;
              ...
              vRes = vmadwbitxr_v32_v32_c32_v32_p (8, vIn, vIn2, vcoefIn, LOW, vecPred);
                 IN_VPR last operand is relevant only for vmadwbitxr_v32_v32_c32_v32_p
Comments    1.
                 version.


Main table → Multiplication → Multiply and Add Two Products → Semi-Complex 16x1
Multiply and Add Two Products
