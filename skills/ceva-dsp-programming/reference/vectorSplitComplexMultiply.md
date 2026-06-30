# Multiplication → Split Multiply → Vector Split Complex Multiply

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Multiplication → Split Multiply → Vector Split Complex Multiply

Vector Split Complex Multiply

Vector Split Complex Multiply
Performs two independent sets of complex multiplication between two complex numbers. The
complex sources consists of real 16-bit part and imaginary 16-bit part. The multipication
products are accumulated into the destination parts respectively.
Available Switches
        Split operations. Pseudo switch which represents the number of atomic operations for
        each operation set. An atomic operation is defined as a single complex multiplication.
Sop
        The optional values for this switch are: 1op1op, 1op2op, 1op3op, 2op1op, 2op2op or
        3op1op.
conj    Performs complex multiply using complex conjugate of vcY/vcV/vy[Y]/vy[V]
const   vy[Y], vy[V] are constant throughout the operations.
vmpsX Selects the VMSNX and VPSX set within modv0 or modv2 mode registers.
Intrinsic Names
vsmpyx_v32_c32_v32_c32_v40_1op1op_conj
vsmpyx_v32_c32_v32_c32_v40_1op1op_conj_vmpsX
vsmpyx_v32_c32_v32_c32_v40_1op1op
vsmpyx_v32_c32_v32_c32_v40_1op1op_vmpsX
vsmpyx_v32_c32_v32_c32_v40_1op2op_conj
vsmpyx_v32_c32_v32_c32_v40_1op2op_conj_vmpsX
vsmpyx_v32_c32_v32_c32_v40_1op2op
vsmpyx_v32_c32_v32_c32_v40_1op2op_vmpsX
vsmpyx_v32_c32_v32_c32_v40_1op3op_conj
vsmpyx_v32_c32_v32_c32_v40_1op3op_conj_vmpsX
vsmpyx_v32_c32_v32_c32_v40_1op3op
vsmpyx_v32_c32_v32_c32_v40_1op3op_vmpsX
vsmpyx_v32_c32_v32_c32_v40_2op1op_conj
vsmpyx_v32_c32_v32_c32_v40_2op1op_conj_vmpsX
vsmpyx_v32_c32_v32_c32_v40_2op1op
vsmpyx_v32_c32_v32_c32_v40_2op1op_vmpsX
vsmpyx_v32_c32_v32_c32_v40_2op2op_conj
vsmpyx_v32_c32_v32_c32_v40_2op2op_conj_vmpsX
vsmpyx_v32_c32_v32_c32_v40_2op2op
vsmpyx_v32_c32_v32_c32_v40_2op2op_vmpsX
vsmpyx_v32_c32_v32_c32_v40_3op1op_conj
vsmpyx_v32_c32_v32_c32_v40_3op1op_conj_vmpsX
vsmpyx_v32_c32_v32_c32_v40_3op1op
vsmpyx_v32_c32_v32_c32_v40_3op1op_vmpsX
vsmpyx_v32_v32_v40_1op1op_const_conj
vsmpyx_v32_v32_v40_1op1op_const_conj_vmpsX
vsmpyx_v32_v32_v40_1op1op_const
vsmpyx_v32_v32_v40_1op1op_const_vmpsX
vsmpyx_v32_v32_v40_1op2op_const_conj
vsmpyx_v32_v32_v40_1op2op_const_conj_vmpsX
vsmpyx_v32_v32_v40_1op2op_const
vsmpyx_v32_v32_v40_1op2op_const_vmpsX
vsmpyx_v32_v32_v40_1op3op_const_conj
vsmpyx_v32_v32_v40_1op3op_const_conj_vmpsX
vsmpyx_v32_v32_v40_1op3op_const
vsmpyx_v32_v32_v40_1op3op_const_vmpsX
vsmpyx_v32_v32_v40_2op1op_const_conj

vsmpyx_v32_v32_v40_2op1op_const_conj_vmpsX
vsmpyx_v32_v32_v40_2op1op_const
vsmpyx_v32_v32_v40_2op1op_const_vmpsX
vsmpyx_v32_v32_v40_2op2op_const_conj
vsmpyx_v32_v32_v40_2op2op_const_conj_vmpsX
vsmpyx_v32_v32_v40_2op2op_const
vsmpyx_v32_v32_v40_2op2op_const_vmpsX
vsmpyx_v32_v32_v40_3op1op_const_conj
vsmpyx_v32_v32_v40_3op1op_const_conj_vmpsX
vsmpyx_v32_v32_v40_3op1op_const
vsmpyx_v32_v32_v40_3op1op_const_vmpsX
Instruction details in the instruction set specification
Intrinsic     vsmpyx_v32_c32_v32_c32_v40_1op1op_conj[_p]
name
Spec syntax   vsmpyx {Sop [,conj][,vmpsX]} vx[X], vcY, vw[W], vcV ,voz[0], ?vprX

Return type   vec40_t

              1    IN1_V32        vec_t                      Input vector operand

              2    IN1_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             1

              3    IN2_C32        coef_t                     Coefficient operand
Operands      4    IN3_V32        vec_t                      Input vector operand

              5    IN3_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             4

              6    IN4_C32        coef_t                     Coefficient operand
              7    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              vprex_t vecPred;
              ...
              vRes = vsmpyx_v32_c32_v32_c32_v40_1op1op_conj_p (vIn, 0, vcoefIn, vIn2, 0, vcoefIn2, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vsmpyx_v32_c32_v32_c32_v40_1op1op_conj_p version.


Main table → Multiplication → Split Multiply → Vector Split Complex Multiply
Intrinsic     vsmpyx_v32_c32_v32_c32_v40_1op1op_conj_vmpsX[_p]
name
Spec syntax   vsmpyx {Sop [,conj][,vmpsX]} vx[X], vcY, vw[W], vcV ,voz[0], ?vprX

Return type   vec40_t

                                                             Selects the VMSNX and VPSX set within
              1    VMPSX          uint8     0,1
                                                             modv0/modv2 mode registers
              2    IN1_V32        vec_t                      Input vector operand

3    IN1_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             2
Operands      4    IN2_C32        coef_t                     Coefficient operand
              5    IN3_V32        vec_t                      Input vector operand

              6    IN3_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             5

              7    IN4_C32        coef_t                     Coefficient operand
              8    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              vprex_t vecPred;
              ...
              vRes = vsmpyx_v32_c32_v32_c32_v40_1op1op_conj_vmpsX_p (1, vIn, 0, vcoefIn, vIn2, 0, vcoefIn2,
              vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vsmpyx_v32_c32_v32_c32_v40_1op1op_conj_vmpsX_p version.


Main table → Multiplication → Split Multiply → Vector Split Complex Multiply
Intrinsic     vsmpyx_v32_c32_v32_c32_v40_1op1op[_p]
name
Spec syntax   vsmpyx {Sop [,conj][,vmpsX]} vx[X], vcY, vw[W], vcV ,voz[0], ?vprX

Return type   vec40_t

              1    IN1_V32        vec_t                      Input vector operand

              2    IN1_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             1

              3    IN2_C32        coef_t                     Coefficient operand
Operands      4    IN3_V32        vec_t                      Input vector operand

              5    IN3_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             4

              6    IN4_C32        coef_t                     Coefficient operand
              7    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              vprex_t vecPred;
              ...
              vRes = vsmpyx_v32_c32_v32_c32_v40_1op1op_p (vIn, 0, vcoefIn, vIn2, 0, vcoefIn2, vecPred);

IN_VPR last operand is relevant only for
Comments      1.
                   vsmpyx_v32_c32_v32_c32_v40_1op1op_p version.


Main table → Multiplication → Split Multiply → Vector Split Complex Multiply
Intrinsic     vsmpyx_v32_c32_v32_c32_v40_1op1op_vmpsX[_p]
name
Spec syntax   vsmpyx {Sop [,conj][,vmpsX]} vx[X], vcY, vw[W], vcV ,voz[0], ?vprX
Return type   vec40_t

                                                             Selects the VMSNX and VPSX set within
              1    VMPSX          uint8     0,1
                                                             modv0/modv2 mode registers
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             2

Operands      4    IN2_C32        coef_t                     Coefficient operand
              5    IN3_V32        vec_t                      Input vector operand

              6    IN3_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             5

              7    IN4_C32        coef_t                     Coefficient operand
              8    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              vprex_t vecPred;
              ...
              vRes = vsmpyx_v32_c32_v32_c32_v40_1op1op_vmpsX_p (1, vIn, 0, vcoefIn, vIn2, 0, vcoefIn2, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vsmpyx_v32_c32_v32_c32_v40_1op1op_vmpsX_p version.


Main table → Multiplication → Split Multiply → Vector Split Complex Multiply
Intrinsic     vsmpyx_v32_c32_v32_c32_v40_1op2op_conj[_p]
name
Spec syntax   vsmpyx {Sop [,conj][,vmpsX]} vx[X], vcY, vw[W], vcV ,voz[0], ?vprX

Return type   vec40_t

              1    IN1_V32        vec_t                      Input vector operand

              2    IN1_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             1

3    IN2_C32        coef_t                     Coefficient operand
Operands      4    IN3_V32        vec_t                      Input vector operand

              5    IN3_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             4

              6    IN4_C32        coef_t                     Coefficient operand
              7    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
C example     vec_t vIn2;
              vec40_t vRes;
              coef_t vcoefIn;
              coef_t vcoefIn2;
              vprex_t vecPred;
              ...
              vRes = vsmpyx_v32_c32_v32_c32_v40_1op2op_conj_p (vIn, 0, vcoefIn, vIn2, 0, vcoefIn2, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vsmpyx_v32_c32_v32_c32_v40_1op2op_conj_p version.


Main table → Multiplication → Split Multiply → Vector Split Complex Multiply
Intrinsic     vsmpyx_v32_c32_v32_c32_v40_1op2op_conj_vmpsX[_p]
name
Spec syntax   vsmpyx {Sop [,conj][,vmpsX]} vx[X], vcY, vw[W], vcV ,voz[0], ?vprX

Return type   vec40_t

                                                             Selects the VMSNX and VPSX set within
              1    VMPSX          uint8     0,1
                                                             modv0/modv2 mode registers
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             2

Operands      4    IN2_C32        coef_t                     Coefficient operand
              5    IN3_V32        vec_t                      Input vector operand

              6    IN3_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             5

              7    IN4_C32        coef_t                     Coefficient operand
              8    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              vprex_t vecPred;
              ...

vRes = vsmpyx_v32_c32_v32_c32_v40_1op2op_conj_vmpsX_p (1, vIn, 0, vcoefIn, vIn2, 0, vcoefIn2,
              vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vsmpyx_v32_c32_v32_c32_v40_1op2op_conj_vmpsX_p version.


Main table → Multiplication → Split Multiply → Vector Split Complex Multiply
Intrinsic     vsmpyx_v32_c32_v32_c32_v40_1op2op[_p]
name
Spec syntax   vsmpyx {Sop [,conj][,vmpsX]} vx[X], vcY, vw[W], vcV ,voz[0], ?vprX

Return type   vec40_t
              1    IN1_V32        vec_t                      Input vector operand

              2    IN1_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             1

              3    IN2_C32        coef_t                     Coefficient operand
Operands      4    IN3_V32        vec_t                      Input vector operand

              5    IN3_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             4

              6    IN4_C32        coef_t                     Coefficient operand
              7    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              vprex_t vecPred;
              ...
              vRes = vsmpyx_v32_c32_v32_c32_v40_1op2op_p (vIn, 0, vcoefIn, vIn2, 0, vcoefIn2, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vsmpyx_v32_c32_v32_c32_v40_1op2op_p version.


Main table → Multiplication → Split Multiply → Vector Split Complex Multiply
Intrinsic     vsmpyx_v32_c32_v32_c32_v40_1op2op_vmpsX[_p]
name
Spec syntax   vsmpyx {Sop [,conj][,vmpsX]} vx[X], vcY, vw[W], vcV ,voz[0], ?vprX

Return type   vec40_t


              1
                                                             Selects the VMSNX and VPSX set within
                   VMPSX          uint8     0,1
                                                             modv0/modv2 mode registers
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0..7
                                                             Offset for the first DW used from operand

2

Operands      4    IN2_C32        coef_t                     Coefficient operand
              5    IN3_V32        vec_t                      Input vector operand

              6    IN3_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             5

              7    IN4_C32        coef_t                     Coefficient operand
              8    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
C example     vec40_t vRes;
              coef_t vcoefIn;
              coef_t vcoefIn2;
              vprex_t vecPred;
              ...
              vRes = vsmpyx_v32_c32_v32_c32_v40_1op2op_vmpsX_p (1, vIn, 0, vcoefIn, vIn2, 0, vcoefIn2, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vsmpyx_v32_c32_v32_c32_v40_1op2op_vmpsX_p version.


Main table → Multiplication → Split Multiply → Vector Split Complex Multiply
Intrinsic     vsmpyx_v32_c32_v32_c32_v40_1op3op_conj[_p]
name
Spec syntax   vsmpyx {Sop [,conj][,vmpsX]} vx[X], vcY, vw[W], vcV ,voz[0], ?vprX

Return type   vec40_t

              1    IN1_V32        vec_t                      Input vector operand

              2    IN1_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             1

              3    IN2_C32        coef_t                     Coefficient operand
Operands      4    IN3_V32        vec_t                      Input vector operand

              5    IN3_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             4

              6    IN4_C32        coef_t                     Coefficient operand
              7    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              vprex_t vecPred;
              ...
              vRes = vsmpyx_v32_c32_v32_c32_v40_1op3op_conj_p (vIn, 0, vcoefIn, vIn2, 0, vcoefIn2, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vsmpyx_v32_c32_v32_c32_v40_1op3op_conj_p version.

Main table → Multiplication → Split Multiply → Vector Split Complex Multiply
Intrinsic     vsmpyx_v32_c32_v32_c32_v40_1op3op_conj_vmpsX[_p]
name
Spec syntax   vsmpyx {Sop [,conj][,vmpsX]} vx[X], vcY, vw[W], vcV ,voz[0], ?vprX

Return type   vec40_t

                                                             Selects the VMSNX and VPSX set within
              1    VMPSX          uint8     0,1
Operands                                                     modv0/modv2 mode registers
              2    IN1_V32        vec_t                      Input vector operand
              3    IN1_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             2

              4    IN2_C32        coef_t                     Coefficient operand
              5    IN3_V32        vec_t                      Input vector operand

              6    IN3_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             5

              7    IN4_C32        coef_t                     Coefficient operand
              8    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              vprex_t vecPred;
              ...
              vRes = vsmpyx_v32_c32_v32_c32_v40_1op3op_conj_vmpsX_p (1, vIn, 0, vcoefIn, vIn2, 0, vcoefIn2,
              vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vsmpyx_v32_c32_v32_c32_v40_1op3op_conj_vmpsX_p version.


Main table → Multiplication → Split Multiply → Vector Split Complex Multiply
Intrinsic     vsmpyx_v32_c32_v32_c32_v40_1op3op[_p]
name
Spec syntax   vsmpyx {Sop [,conj][,vmpsX]} vx[X], vcY, vw[W], vcV ,voz[0], ?vprX

Return type   vec40_t

              1    IN1_V32        vec_t                      Input vector operand

              2    IN1_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             1

              3    IN2_C32        coef_t                     Coefficient operand
Operands      4    IN3_V32        vec_t                      Input vector operand

              5    IN3_OFST       uint8     0..7             Offset for the first DW used from operand

4

              6    IN4_C32        coef_t                     Coefficient operand
              7    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              vprex_t vecPred;
              ...
              vRes = vsmpyx_v32_c32_v32_c32_v40_1op3op_p (vIn, 0, vcoefIn, vIn2, 0, vcoefIn2, vecPred);
                   IN_VPR last operand is relevant only for
Comments      1.
                   vsmpyx_v32_c32_v32_c32_v40_1op3op_p version.


Main table → Multiplication → Split Multiply → Vector Split Complex Multiply
Intrinsic     vsmpyx_v32_c32_v32_c32_v40_1op3op_vmpsX[_p]
name
Spec syntax   vsmpyx {Sop [,conj][,vmpsX]} vx[X], vcY, vw[W], vcV ,voz[0], ?vprX

Return type   vec40_t


              1
                                                             Selects the VMSNX and VPSX set within
                   VMPSX          uint8     0,1
                                                             modv0/modv2 mode registers
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             2

Operands      4    IN2_C32        coef_t                     Coefficient operand
              5    IN3_V32        vec_t                      Input vector operand

              6    IN3_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             5

              7    IN4_C32        coef_t                     Coefficient operand
              8    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              vprex_t vecPred;
              ...
              vRes = vsmpyx_v32_c32_v32_c32_v40_1op3op_vmpsX_p (1, vIn, 0, vcoefIn, vIn2, 0, vcoefIn2, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vsmpyx_v32_c32_v32_c32_v40_1op3op_vmpsX_p version.


Main table → Multiplication → Split Multiply → Vector Split Complex Multiply
Intrinsic     vsmpyx_v32_c32_v32_c32_v40_2op1op_conj[_p]
name

Spec syntax   vsmpyx {Sop [,conj][,vmpsX]} vx[X], vcY, vw[W], vcV ,voz[0], ?vprX

Return type   vec40_t

              1    IN1_V32        vec_t                      Input vector operand

Operands      2    IN1_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             1

              3    IN2_C32        coef_t                     Coefficient operand
              4    IN3_V32        vec_t                      Input vector operand

              5    IN3_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             4

              6    IN4_C32        coef_t                     Coefficient operand
              7    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              vprex_t vecPred;
              ...
              vRes = vsmpyx_v32_c32_v32_c32_v40_2op1op_conj_p (vIn, 0, vcoefIn, vIn2, 0, vcoefIn2, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vsmpyx_v32_c32_v32_c32_v40_2op1op_conj_p version.


Main table → Multiplication → Split Multiply → Vector Split Complex Multiply
Intrinsic     vsmpyx_v32_c32_v32_c32_v40_2op1op_conj_vmpsX[_p]
name
Spec syntax   vsmpyx {Sop [,conj][,vmpsX]} vx[X], vcY, vw[W], vcV ,voz[0], ?vprX

Return type   vec40_t

                                                             Selects the VMSNX and VPSX set within
              1    VMPSX          uint8     0,1
                                                             modv0/modv2 mode registers
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             2

Operands      4    IN2_C32        coef_t                     Coefficient operand
              5    IN3_V32        vec_t                      Input vector operand

              6    IN3_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             5

7    IN4_C32        coef_t                     Coefficient operand
              8    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              vprex_t vecPred;
              ...
              vRes = vsmpyx_v32_c32_v32_c32_v40_2op1op_conj_vmpsX_p (1, vIn, 0, vcoefIn, vIn2, 0, vcoefIn2,
              vecPred);

Comments      1.   IN_VPR last operand is relevant only for
                   vsmpyx_v32_c32_v32_c32_v40_2op1op_conj_vmpsX_p version.


Main table → Multiplication → Split Multiply → Vector Split Complex Multiply
Intrinsic     vsmpyx_v32_c32_v32_c32_v40_2op1op[_p]
name
Spec syntax   vsmpyx {Sop [,conj][,vmpsX]} vx[X], vcY, vw[W], vcV ,voz[0], ?vprX

Return type   vec40_t

              1    IN1_V32        vec_t                      Input vector operand

              2    IN1_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             1

              3    IN2_C32        coef_t                     Coefficient operand
Operands      4    IN3_V32        vec_t                      Input vector operand

              5    IN3_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             4

              6    IN4_C32        coef_t                     Coefficient operand
              7    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              vprex_t vecPred;
              ...
              vRes = vsmpyx_v32_c32_v32_c32_v40_2op1op_p (vIn, 0, vcoefIn, vIn2, 0, vcoefIn2, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vsmpyx_v32_c32_v32_c32_v40_2op1op_p version.


Main table → Multiplication → Split Multiply → Vector Split Complex Multiply
Intrinsic     vsmpyx_v32_c32_v32_c32_v40_2op1op_vmpsX[_p]
name
Spec syntax   vsmpyx {Sop [,conj][,vmpsX]} vx[X], vcY, vw[W], vcV ,voz[0], ?vprX

Return type   vec40_t

                                                             Selects the VMSNX and VPSX set within

1    VMPSX          uint8     0,1
                                                             modv0/modv2 mode registers
              2    IN1_V32        vec_t                      Input vector operand
Operands      3    IN1_OFST       uint8                      Offset for the first DW used from operand
                                            0..7
                                                             2

              4    IN2_C32        coef_t                     Coefficient operand
              5    IN3_V32        vec_t                      Input vector operand
              6    IN3_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             5

              7    IN4_C32        coef_t                     Coefficient operand
              8    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              vprex_t vecPred;
              ...
              vRes = vsmpyx_v32_c32_v32_c32_v40_2op1op_vmpsX_p (1, vIn, 0, vcoefIn, vIn2, 0, vcoefIn2, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vsmpyx_v32_c32_v32_c32_v40_2op1op_vmpsX_p version.


Main table → Multiplication → Split Multiply → Vector Split Complex Multiply
Intrinsic     vsmpyx_v32_c32_v32_c32_v40_2op2op_conj[_p]
name
Spec syntax   vsmpyx {Sop [,conj][,vmpsX]} vx[X], vcY, vw[W], vcV ,voz[0], ?vprX

Return type   vec40_t

              1    IN1_V32        vec_t                      Input vector operand

              2    IN1_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             1

              3    IN2_C32        coef_t                     Coefficient operand
Operands      4    IN3_V32        vec_t                      Input vector operand

              5    IN3_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             4

              6    IN4_C32        coef_t                     Coefficient operand
              7    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
              coef_t vcoefIn;

C example     coef_t vcoefIn2;
              vprex_t vecPred;
              ...
              vRes = vsmpyx_v32_c32_v32_c32_v40_2op2op_conj_p (vIn, 0, vcoefIn, vIn2, 0, vcoefIn2, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vsmpyx_v32_c32_v32_c32_v40_2op2op_conj_p version.


Main table → Multiplication → Split Multiply → Vector Split Complex Multiply
Intrinsic     vsmpyx_v32_c32_v32_c32_v40_2op2op_conj_vmpsX[_p]
name
Spec syntax   vsmpyx {Sop [,conj][,vmpsX]} vx[X], vcY, vw[W], vcV ,voz[0], ?vprX

Return type   vec40_t


              1
                                                            Selects the VMSNX and VPSX set within
                   VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            2

Operands      4    IN2_C32        coef_t                    Coefficient operand
              5    IN3_V32        vec_t                     Input vector operand

              6    IN3_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            5

              7    IN4_C32        coef_t                    Coefficient operand
              8    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              vprex_t vecPred;
              ...
              vRes = vsmpyx_v32_c32_v32_c32_v40_2op2op_conj_vmpsX_p (1, vIn, 0, vcoefIn, vIn2, 0, vcoefIn2,
              vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vsmpyx_v32_c32_v32_c32_v40_2op2op_conj_vmpsX_p version.


Main table → Multiplication → Split Multiply → Vector Split Complex Multiply
Intrinsic     vsmpyx_v32_c32_v32_c32_v40_2op2op[_p]
name
Spec syntax   vsmpyx {Sop [,conj][,vmpsX]} vx[X], vcY, vw[W], vcV ,voz[0], ?vprX

Return type   vec40_t

              1    IN1_V32        vec_t                     Input vector operand

              2    IN1_OFST       uint8     0..7

Offset for the first DW used from operand
                                                            1

              3    IN2_C32        coef_t                    Coefficient operand
Operands
              4    IN3_V32        vec_t                     Input vector operand

              5    IN3_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            4

              6    IN4_C32        coef_t                    Coefficient operand
              7    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              vprex_t vecPred;
              ...
              vRes = vsmpyx_v32_c32_v32_c32_v40_2op2op_p (vIn, 0, vcoefIn, vIn2, 0, vcoefIn2, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vsmpyx_v32_c32_v32_c32_v40_2op2op_p version.


Main table → Multiplication → Split Multiply → Vector Split Complex Multiply
Intrinsic     vsmpyx_v32_c32_v32_c32_v40_2op2op_vmpsX[_p]
name
Spec syntax   vsmpyx {Sop [,conj][,vmpsX]} vx[X], vcY, vw[W], vcV ,voz[0], ?vprX

Return type   vec40_t

                                                             Selects the VMSNX and VPSX set within
              1    VMPSX          uint8     0,1
                                                             modv0/modv2 mode registers
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             2

Operands      4    IN2_C32        coef_t                     Coefficient operand
              5    IN3_V32        vec_t                      Input vector operand

              6    IN3_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             5

              7    IN4_C32        coef_t                     Coefficient operand
              8    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              vprex_t vecPred;

...
              vRes = vsmpyx_v32_c32_v32_c32_v40_2op2op_vmpsX_p (1, vIn, 0, vcoefIn, vIn2, 0, vcoefIn2, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vsmpyx_v32_c32_v32_c32_v40_2op2op_vmpsX_p version.


Main table → Multiplication → Split Multiply → Vector Split Complex Multiply
Intrinsic     vsmpyx_v32_c32_v32_c32_v40_3op1op_conj[_p]
name
Spec syntax   vsmpyx {Sop [,conj][,vmpsX]} vx[X], vcY, vw[W], vcV ,voz[0], ?vprX

Return type   vec40_t

              1    IN1_V32        vec_t                      Input vector operand

              2    IN1_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             1

              3    IN2_C32        coef_t                     Coefficient operand
Operands      4    IN3_V32        vec_t                      Input vector operand

              5    IN3_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             4

              6    IN4_C32        coef_t                     Coefficient operand
              7    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              vprex_t vecPred;
              ...
              vRes = vsmpyx_v32_c32_v32_c32_v40_3op1op_conj_p (vIn, 0, vcoefIn, vIn2, 0, vcoefIn2, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vsmpyx_v32_c32_v32_c32_v40_3op1op_conj_p version.


Main table → Multiplication → Split Multiply → Vector Split Complex Multiply
Intrinsic     vsmpyx_v32_c32_v32_c32_v40_3op1op_conj_vmpsX[_p]
name
Spec syntax   vsmpyx {Sop [,conj][,vmpsX]} vx[X], vcY, vw[W], vcV ,voz[0], ?vprX

Return type   vec40_t

                                                             Selects the VMSNX and VPSX set within
              1    VMPSX          uint8     0,1
                                                             modv0/modv2 mode registers
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0..7             Offset for the first DW used from operand

2

Operands      4    IN2_C32        coef_t                     Coefficient operand
              5    IN3_V32        vec_t                      Input vector operand

              6    IN3_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             5

              7    IN4_C32        coef_t                     Coefficient operand
              8    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              vprex_t vecPred;
              ...
              vRes = vsmpyx_v32_c32_v32_c32_v40_3op1op_conj_vmpsX_p (1, vIn, 0, vcoefIn, vIn2, 0, vcoefIn2,
              vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vsmpyx_v32_c32_v32_c32_v40_3op1op_conj_vmpsX_p version.


Main table → Multiplication → Split Multiply → Vector Split Complex Multiply
Intrinsic     vsmpyx_v32_c32_v32_c32_v40_3op1op[_p]
name
Spec syntax   vsmpyx {Sop [,conj][,vmpsX]} vx[X], vcY, vw[W], vcV ,voz[0], ?vprX

Return type   vec40_t

              1    IN1_V32        vec_t                      Input vector operand

              2    IN1_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             1

              3    IN2_C32        coef_t                     Coefficient operand
Operands      4    IN3_V32        vec_t                      Input vector operand

              5    IN3_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             4

              6    IN4_C32        coef_t                     Coefficient operand
              7    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              vprex_t vecPred;
              ...
              vRes = vsmpyx_v32_c32_v32_c32_v40_3op1op_p (vIn, 0, vcoefIn, vIn2, 0, vcoefIn2, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vsmpyx_v32_c32_v32_c32_v40_3op1op_p version.

Main table → Multiplication → Split Multiply → Vector Split Complex Multiply
Intrinsic     vsmpyx_v32_c32_v32_c32_v40_3op1op_vmpsX[_p]
name
Spec syntax   vsmpyx {Sop [,conj][,vmpsX]} vx[X], vcY, vw[W], vcV ,voz[0], ?vprX

Return type   vec40_t
                                                            Selects the VMSNX and VPSX set within
             1    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
             2    IN1_V32        vec_t                      Input vector operand

             3    IN1_OFST       uint8     0..7             Offset for the first DW used from operand
                                                            2

Operands     4    IN2_C32        coef_t                     Coefficient operand
             5    IN3_V32        vec_t                      Input vector operand

             6    IN3_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            5

             7    IN4_C32        coef_t                     Coefficient operand
             8    IN_VPR         vprex_t                    Vector predicate operand
             vec_t vIn;
             vec_t vIn2;
             vec40_t vRes;
             coef_t vcoefIn;
C example    coef_t vcoefIn2;
             vprex_t vecPred;
             ...
             vRes = vsmpyx_v32_c32_v32_c32_v40_3op1op_vmpsX_p (1, vIn, 0, vcoefIn, vIn2, 0, vcoefIn2, vecPred);

                  IN_VPR last operand is relevant only for
Comments     1.
                  vsmpyx_v32_c32_v32_c32_v40_3op1op_vmpsX_p version.


Main table → Multiplication → Split Multiply → Vector Split Complex Multiply
Intrinsic     vsmpyx_v32_v32_v40_1op1op_const_conj[_p]
name
Spec syntax   vsmpyx {Sop ,const [,conj][,vmpsX]} vx[X], vy[Y], vx[W], vy[V] ,voz[0], ?vprX

Return type   vec40_t

              1    IN1_V32         vec_t                     Input vector operand

              2    IN1_OFST        uint8     0..7
                                                             Offset for the first DW used from operand
                                                             1

              3    IN2_V32         vec_t                     Input vector operand

              4    IN2_OFST        uint8     0..7
                                                             Offset for the first DW used from operand

Operands                                                     3

              5    IN3_OFST        uint8     0..7
                                                             Offset for the first DW used from operand
                                                             1

              6    IN4_OFST        uint8     0..7
                                                             Offset for the first DW used from operand
                                                             3

              7    IN_VPR          vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vsmpyx_v32_v32_v40_1op1op_const_conj_p (vIn, 0, vIn2, 0, 0, 0, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vsmpyx_v32_v32_v40_1op1op_const_conj_p version.


Main table → Multiplication → Split Multiply → Vector Split Complex Multiply
Intrinsic     vsmpyx_v32_v32_v40_1op1op_const_conj_vmpsX[_p]
name
Spec syntax   vsmpyx {Sop ,const [,conj][,vmpsX]} vx[X], vy[Y], vx[W], vy[V] ,voz[0], ?vprX

Return type   vec40_t

                                                             Selects the VMSNX and VPSX set within
              1    VMPSX           uint8     0,1
                                                             modv0/modv2 mode registers
              2    IN1_V32         vec_t                     Input vector operand

              3    IN1_OFST        uint8     0..7            Offset for the first DW used from operand
                                                             2
Operands
              4    IN2_V32         vec_t                     Input vector operand

              5    IN2_OFST        uint8     0..7            Offset for the first DW used from operand
                                                             4

              6    IN3_OFST        uint8     0..7            Offset for the first DW used from operand
                                                             2
              7    IN4_OFST        uint8     0..7             Offset for the first DW used from operand
                                                              4

              8    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;

...
              vRes = vsmpyx_v32_v32_v40_1op1op_const_conj_vmpsX_p (1, vIn, 0, vIn2, 0, 0, 0, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vsmpyx_v32_v32_v40_1op1op_const_conj_vmpsX_p version.


Main table → Multiplication → Split Multiply → Vector Split Complex Multiply
Intrinsic     vsmpyx_v32_v32_v40_1op1op_const[_p]
name
Spec syntax   vsmpyx {Sop ,const [,conj][,vmpsX]} vx[X], vy[Y], vx[W], vy[V] ,voz[0], ?vprX

Return type   vec40_t

              1    IN1_V32         vec_t                      Input vector operand

              2    IN1_OFST        uint8     0..7             Offset for the first DW used from operand
                                                              1

              3    IN2_V32         vec_t                      Input vector operand

              4    IN2_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
Operands                                                      3

              5    IN3_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
                                                              1

              6    IN4_OFST        uint8     0..7             Offset for the first DW used from operand
                                                              3

              7    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vsmpyx_v32_v32_v40_1op1op_const_p (vIn, 0, vIn2, 0, 0, 0, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vsmpyx_v32_v32_v40_1op1op_const_p version.


Main table → Multiplication → Split Multiply → Vector Split Complex Multiply
Intrinsic     vsmpyx_v32_v32_v40_1op1op_const_vmpsX[_p]
name
Spec syntax   vsmpyx {Sop ,const [,conj][,vmpsX]} vx[X], vy[Y], vx[W], vy[V] ,voz[0], ?vprX
Return type   vec40_t

                                                             Selects the VMSNX and VPSX set within
              1    VMPSX          uint8     0,1
                                                             modv0/modv2 mode registers
              2    IN1_V32        vec_t                      Input vector operand

3    IN1_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             2

              4    IN2_V32        vec_t                      Input vector operand
Operands
              5    IN2_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             4

              6    IN3_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             2

              7    IN4_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             4

              8    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vsmpyx_v32_v32_v40_1op1op_const_vmpsX_p (1, vIn, 0, vIn2, 0, 0, 0, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vsmpyx_v32_v32_v40_1op1op_const_vmpsX_p version.


Main table → Multiplication → Split Multiply → Vector Split Complex Multiply
Intrinsic     vsmpyx_v32_v32_v40_1op2op_const_conj[_p]
name
Spec syntax   vsmpyx {Sop ,const [,conj][,vmpsX]} vx[X], vy[Y], vx[W], vy[V] ,voz[0], ?vprX

Return type   vec40_t

              1    IN1_V32        vec_t                      Input vector operand

              2    IN1_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             1

              3    IN2_V32        vec_t                      Input vector operand

              4    IN2_OFST       uint8     0..7             Offset for the first DW used from operand
Operands                                                     3

              5    IN3_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             1

              6    IN4_OFST       uint8     0..7

Offset for the first DW used from operand
                                                             3

              7    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vsmpyx_v32_v32_v40_1op2op_const_conj_p (vIn, 0, vIn2, 0, 0, 0, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vsmpyx_v32_v32_v40_1op2op_const_conj_p version.


Main table → Multiplication → Split Multiply → Vector Split Complex Multiply
Intrinsic     vsmpyx_v32_v32_v40_1op2op_const_conj_vmpsX[_p]
name
Spec syntax   vsmpyx {Sop ,const [,conj][,vmpsX]} vx[X], vy[Y], vx[W], vy[V] ,voz[0], ?vprX

Return type   vec40_t

                                                             Selects the VMSNX and VPSX set within
              1    VMPSX           uint8     0,1
                                                             modv0/modv2 mode registers
              2    IN1_V32         vec_t                     Input vector operand

              3    IN1_OFST        uint8     0..7
                                                             Offset for the first DW used from operand
                                                             2

              4    IN2_V32         vec_t                     Input vector operand
Operands
              5    IN2_OFST        uint8     0..7
                                                             Offset for the first DW used from operand
                                                             4

              6    IN3_OFST        uint8     0..7
                                                             Offset for the first DW used from operand
                                                             2

              7    IN4_OFST        uint8     0..7
                                                             Offset for the first DW used from operand
                                                             4

              8    IN_VPR          vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vsmpyx_v32_v32_v40_1op2op_const_conj_vmpsX_p (1, vIn, 0, vIn2, 0, 0, 0, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.

vsmpyx_v32_v32_v40_1op2op_const_conj_vmpsX_p version.


Main table → Multiplication → Split Multiply → Vector Split Complex Multiply
Intrinsic     vsmpyx_v32_v32_v40_1op2op_const[_p]
name
Spec syntax   vsmpyx {Sop ,const [,conj][,vmpsX]} vx[X], vy[Y], vx[W], vy[V] ,voz[0], ?vprX

Return type   vec40_t
              1    IN1_V32         vec_t                      Input vector operand

              2    IN1_OFST        uint8     0..7             Offset for the first DW used from operand
                                                              1

              3    IN2_V32         vec_t                      Input vector operand

              4    IN2_OFST        uint8     0..7             Offset for the first DW used from operand
Operands                                                      3

              5    IN3_OFST        uint8     0..7             Offset for the first DW used from operand
                                                              1

              6    IN4_OFST        uint8     0..7             Offset for the first DW used from operand
                                                              3

              7    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vsmpyx_v32_v32_v40_1op2op_const_p (vIn, 0, vIn2, 0, 0, 0, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vsmpyx_v32_v32_v40_1op2op_const_p version.


Main table → Multiplication → Split Multiply → Vector Split Complex Multiply
Intrinsic     vsmpyx_v32_v32_v40_1op2op_const_vmpsX[_p]
name
Spec syntax   vsmpyx {Sop ,const [,conj][,vmpsX]} vx[X], vy[Y], vx[W], vy[V] ,voz[0], ?vprX

Return type   vec40_t


              1
                                                              Selects the VMSNX and VPSX set within
                   VMPSX           uint8     0,1
                                                              modv0/modv2 mode registers
              2    IN1_V32         vec_t                      Input vector operand

              3    IN1_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
                                                              2

              4    IN2_V32         vec_t                      Input vector operand
Operands

5    IN2_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
                                                              4

              6    IN3_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
                                                              2

              7    IN4_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
                                                              4

              8    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
C example     vec_t vIn2;
              vec40_t vRes;
              vprex_t vecPred;
              ...
              vRes = vsmpyx_v32_v32_v40_1op2op_const_vmpsX_p (1, vIn, 0, vIn2, 0, 0, 0, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vsmpyx_v32_v32_v40_1op2op_const_vmpsX_p version.


Main table → Multiplication → Split Multiply → Vector Split Complex Multiply
Intrinsic     vsmpyx_v32_v32_v40_1op3op_const_conj[_p]
name
Spec syntax   vsmpyx {Sop ,const [,conj][,vmpsX]} vx[X], vy[Y], vx[W], vy[V] ,voz[0], ?vprX

Return type   vec40_t

              1    IN1_V32         vec_t                     Input vector operand

              2    IN1_OFST        uint8     0..7
                                                             Offset for the first DW used from operand
                                                             1

              3    IN2_V32         vec_t                     Input vector operand

              4    IN2_OFST        uint8     0..7
                                                             Offset for the first DW used from operand
Operands                                                     3

              5    IN3_OFST        uint8     0..7
                                                             Offset for the first DW used from operand
                                                             1

              6    IN4_OFST        uint8     0..7
                                                             Offset for the first DW used from operand
                                                             3

              7    IN_VPR          vprex_t                   Vector predicate operand

vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vsmpyx_v32_v32_v40_1op3op_const_conj_p (vIn, 0, vIn2, 0, 0, 0, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vsmpyx_v32_v32_v40_1op3op_const_conj_p version.


Main table → Multiplication → Split Multiply → Vector Split Complex Multiply
Intrinsic     vsmpyx_v32_v32_v40_1op3op_const_conj_vmpsX[_p]
name
Spec syntax   vsmpyx {Sop ,const [,conj][,vmpsX]} vx[X], vy[Y], vx[W], vy[V] ,voz[0], ?vprX

Return type   vec40_t

                                                             Selects the VMSNX and VPSX set within
              1    VMPSX           uint8     0,1
Operands                                                     modv0/modv2 mode registers
              2    IN1_V32         vec_t                     Input vector operand
              3    IN1_OFST        uint8     0..7             Offset for the first DW used from operand
                                                              2

              4    IN2_V32         vec_t                      Input vector operand

              5    IN2_OFST        uint8     0..7             Offset for the first DW used from operand
                                                              4

              6    IN3_OFST        uint8     0..7             Offset for the first DW used from operand
                                                              2

              7    IN4_OFST        uint8     0..7             Offset for the first DW used from operand
                                                              4

              8    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vsmpyx_v32_v32_v40_1op3op_const_conj_vmpsX_p (1, vIn, 0, vIn2, 0, 0, 0, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vsmpyx_v32_v32_v40_1op3op_const_conj_vmpsX_p version.


Main table → Multiplication → Split Multiply → Vector Split Complex Multiply
Intrinsic     vsmpyx_v32_v32_v40_1op3op_const[_p]
name
Spec syntax   vsmpyx {Sop ,const [,conj][,vmpsX]} vx[X], vy[Y], vx[W], vy[V] ,voz[0], ?vprX

Return type   vec40_t

              1    IN1_V32         vec_t                      Input vector operand

2    IN1_OFST        uint8     0..7             Offset for the first DW used from operand
                                                              1

              3    IN2_V32         vec_t                      Input vector operand

              4    IN2_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
Operands                                                      3

              5    IN3_OFST        uint8     0..7             Offset for the first DW used from operand
                                                              1

              6    IN4_OFST        uint8     0..7             Offset for the first DW used from operand
                                                              3

              7    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vsmpyx_v32_v32_v40_1op3op_const_p (vIn, 0, vIn2, 0, 0, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for
                   vsmpyx_v32_v32_v40_1op3op_const_p version.


Main table → Multiplication → Split Multiply → Vector Split Complex Multiply
Intrinsic     vsmpyx_v32_v32_v40_1op3op_const_vmpsX[_p]
name
Spec syntax   vsmpyx {Sop ,const [,conj][,vmpsX]} vx[X], vy[Y], vx[W], vy[V] ,voz[0], ?vprX

Return type   vec40_t


              1
                                                             Selects the VMSNX and VPSX set within
                   VMPSX          uint8     0,1
                                                             modv0/modv2 mode registers
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             2

              4    IN2_V32        vec_t                      Input vector operand
Operands
              5    IN2_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             4

              6    IN3_OFST       uint8     0..7
                                                             Offset for the first DW used from operand

2

              7    IN4_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             4

              8    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vsmpyx_v32_v32_v40_1op3op_const_vmpsX_p (1, vIn, 0, vIn2, 0, 0, 0, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vsmpyx_v32_v32_v40_1op3op_const_vmpsX_p version.


Main table → Multiplication → Split Multiply → Vector Split Complex Multiply
Intrinsic     vsmpyx_v32_v32_v40_2op1op_const_conj[_p]
name
Spec syntax   vsmpyx {Sop ,const [,conj][,vmpsX]} vx[X], vy[Y], vx[W], vy[V] ,voz[0], ?vprX

Return type   vec40_t

              1    IN1_V32        vec_t                      Input vector operand

              2    IN1_OFST       uint8     0..7             Offset for the first DW used from operand
Operands                                                     1

              3    IN2_V32        vec_t                      Input vector operand
              4    IN2_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             3

              5    IN3_OFST        uint8     0..7            Offset for the first DW used from operand
                                                             1

              6    IN4_OFST        uint8     0..7
                                                             Offset for the first DW used from operand
                                                             3

              7    IN_VPR          vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vsmpyx_v32_v32_v40_2op1op_const_conj_p (vIn, 0, vIn2, 0, 0, 0, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vsmpyx_v32_v32_v40_2op1op_const_conj_p version.


Main table → Multiplication → Split Multiply → Vector Split Complex Multiply
Intrinsic     vsmpyx_v32_v32_v40_2op1op_const_conj_vmpsX[_p]
name

Spec syntax   vsmpyx {Sop ,const [,conj][,vmpsX]} vx[X], vy[Y], vx[W], vy[V] ,voz[0], ?vprX

Return type   vec40_t

                                                             Selects the VMSNX and VPSX set within
              1    VMPSX           uint8     0,1
                                                             modv0/modv2 mode registers
              2    IN1_V32         vec_t                     Input vector operand

              3    IN1_OFST        uint8     0..7
                                                             Offset for the first DW used from operand
                                                             2

              4    IN2_V32         vec_t                     Input vector operand
Operands
              5    IN2_OFST        uint8     0..7
                                                             Offset for the first DW used from operand
                                                             4

              6    IN3_OFST        uint8     0..7
                                                             Offset for the first DW used from operand
                                                             2

              7    IN4_OFST        uint8     0..7            Offset for the first DW used from operand
                                                             4

              8    IN_VPR          vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vsmpyx_v32_v32_v40_2op1op_const_conj_vmpsX_p (1, vIn, 0, vIn2, 0, 0, 0, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vsmpyx_v32_v32_v40_2op1op_const_conj_vmpsX_p version.

Main table → Multiplication → Split Multiply → Vector Split Complex Multiply
Intrinsic     vsmpyx_v32_v32_v40_2op1op_const[_p]
name
Spec syntax   vsmpyx {Sop ,const [,conj][,vmpsX]} vx[X], vy[Y], vx[W], vy[V] ,voz[0], ?vprX

Return type   vec40_t

              1    IN1_V32         vec_t                      Input vector operand

              2    IN1_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
                                                              1

              3    IN2_V32         vec_t                      Input vector operand

              4    IN2_OFST        uint8     0..7

Offset for the first DW used from operand
Operands                                                      3

              5    IN3_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
                                                              1

              6    IN4_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
                                                              3

              7    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vsmpyx_v32_v32_v40_2op1op_const_p (vIn, 0, vIn2, 0, 0, 0, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vsmpyx_v32_v32_v40_2op1op_const_p version.


Main table → Multiplication → Split Multiply → Vector Split Complex Multiply
Intrinsic     vsmpyx_v32_v32_v40_2op1op_const_vmpsX[_p]
name
Spec syntax   vsmpyx {Sop ,const [,conj][,vmpsX]} vx[X], vy[Y], vx[W], vy[V] ,voz[0], ?vprX

Return type   vec40_t

                                                              Selects the VMSNX and VPSX set within
              1    VMPSX           uint8     0,1
                                                              modv0/modv2 mode registers
              2    IN1_V32         vec_t                      Input vector operand

Operands      3    IN1_OFST        uint8     0..7             Offset for the first DW used from operand
                                                              2

              4    IN2_V32         vec_t                      Input vector operand

              5    IN2_OFST        uint8     0..7             Offset for the first DW used from operand
                                                              4
              6    IN3_OFST        uint8     0..7            Offset for the first DW used from operand
                                                             2

              7    IN4_OFST        uint8     0..7            Offset for the first DW used from operand
                                                             4

              8    IN_VPR          vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;

C example     vprex_t vecPred;
              ...
              vRes = vsmpyx_v32_v32_v40_2op1op_const_vmpsX_p (1, vIn, 0, vIn2, 0, 0, 0, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vsmpyx_v32_v32_v40_2op1op_const_vmpsX_p version.


Main table → Multiplication → Split Multiply → Vector Split Complex Multiply
Intrinsic     vsmpyx_v32_v32_v40_2op2op_const_conj[_p]
name
Spec syntax   vsmpyx {Sop ,const [,conj][,vmpsX]} vx[X], vy[Y], vx[W], vy[V] ,voz[0], ?vprX

Return type   vec40_t

              1    IN1_V32         vec_t                     Input vector operand

              2    IN1_OFST        uint8     0..7            Offset for the first DW used from operand
                                                             1

              3    IN2_V32         vec_t                     Input vector operand

              4    IN2_OFST        uint8     0..7
                                                             Offset for the first DW used from operand
Operands                                                     3

              5    IN3_OFST        uint8     0..7            Offset for the first DW used from operand
                                                             1

              6    IN4_OFST        uint8     0..7            Offset for the first DW used from operand
                                                             3

              7    IN_VPR          vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vsmpyx_v32_v32_v40_2op2op_const_conj_p (vIn, 0, vIn2, 0, 0, 0, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vsmpyx_v32_v32_v40_2op2op_const_conj_p version.


Main table → Multiplication → Split Multiply → Vector Split Complex Multiply
Intrinsic     vsmpyx_v32_v32_v40_2op2op_const_conj_vmpsX[_p]
name
Spec syntax   vsmpyx {Sop ,const [,conj][,vmpsX]} vx[X], vy[Y], vx[W], vy[V] ,voz[0], ?vprX

Return type   vec40_t


              1
                                                             Selects the VMSNX and VPSX set within
                   VMPSX          uint8     0,1
                                                             modv0/modv2 mode registers
              2    IN1_V32        vec_t                      Input vector operand

3    IN1_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             2

              4    IN2_V32        vec_t                      Input vector operand
Operands
              5    IN2_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             4

              6    IN3_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             2

              7    IN4_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             4

              8    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vsmpyx_v32_v32_v40_2op2op_const_conj_vmpsX_p (1, vIn, 0, vIn2, 0, 0, 0, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vsmpyx_v32_v32_v40_2op2op_const_conj_vmpsX_p version.


Main table → Multiplication → Split Multiply → Vector Split Complex Multiply
Intrinsic     vsmpyx_v32_v32_v40_2op2op_const[_p]
name
Spec syntax   vsmpyx {Sop ,const [,conj][,vmpsX]} vx[X], vy[Y], vx[W], vy[V] ,voz[0], ?vprX

Return type   vec40_t

              1    IN1_V32        vec_t                      Input vector operand

              2    IN1_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             1

              3    IN2_V32        vec_t                      Input vector operand
Operands      4    IN2_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             3

              5    IN3_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             1

              6    IN4_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             3

7    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vsmpyx_v32_v32_v40_2op2op_const_p (vIn, 0, vIn2, 0, 0, 0, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vsmpyx_v32_v32_v40_2op2op_const_p version.


Main table → Multiplication → Split Multiply → Vector Split Complex Multiply
Intrinsic     vsmpyx_v32_v32_v40_2op2op_const_vmpsX[_p]
name
Spec syntax   vsmpyx {Sop ,const [,conj][,vmpsX]} vx[X], vy[Y], vx[W], vy[V] ,voz[0], ?vprX

Return type   vec40_t


              1
                                                              Selects the VMSNX and VPSX set within
                   VMPSX           uint8     0,1
                                                              modv0/modv2 mode registers
              2    IN1_V32         vec_t                      Input vector operand

              3    IN1_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
                                                              2

              4    IN2_V32         vec_t                      Input vector operand
Operands
              5    IN2_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
                                                              4

              6    IN3_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
                                                              2

              7    IN4_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
                                                              4

              8    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vsmpyx_v32_v32_v40_2op2op_const_vmpsX_p (1, vIn, 0, vIn2, 0, 0, 0, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vsmpyx_v32_v32_v40_2op2op_const_vmpsX_p version.

Main table → Multiplication → Split Multiply → Vector Split Complex Multiply
Intrinsic     vsmpyx_v32_v32_v40_3op1op_const_conj[_p]
name
Spec syntax   vsmpyx {Sop ,const [,conj][,vmpsX]} vx[X], vy[Y], vx[W], vy[V] ,voz[0], ?vprX
Return type   vec40_t

              1    IN1_V32         vec_t                     Input vector operand

              2    IN1_OFST        uint8     0..7            Offset for the first DW used from operand
                                                             1

              3    IN2_V32         vec_t                     Input vector operand

              4    IN2_OFST        uint8     0..7
                                                             Offset for the first DW used from operand
Operands                                                     3

              5    IN3_OFST        uint8     0..7            Offset for the first DW used from operand
                                                             1

              6    IN4_OFST        uint8     0..7            Offset for the first DW used from operand
                                                             3

              7    IN_VPR          vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vsmpyx_v32_v32_v40_3op1op_const_conj_p (vIn, 0, vIn2, 0, 0, 0, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vsmpyx_v32_v32_v40_3op1op_const_conj_p version.


Main table → Multiplication → Split Multiply → Vector Split Complex Multiply
Intrinsic     vsmpyx_v32_v32_v40_3op1op_const_conj_vmpsX[_p]
name
Spec syntax   vsmpyx {Sop ,const [,conj][,vmpsX]} vx[X], vy[Y], vx[W], vy[V] ,voz[0], ?vprX

Return type   vec40_t

                                                             Selects the VMSNX and VPSX set within
              1    VMPSX           uint8     0,1
                                                             modv0/modv2 mode registers
              2    IN1_V32         vec_t                     Input vector operand

              3    IN1_OFST        uint8     0..7
                                                             Offset for the first DW used from operand
                                                             2

              4    IN2_V32         vec_t                     Input vector operand
Operands

5    IN2_OFST        uint8     0..7            Offset for the first DW used from operand
                                                             4

              6    IN3_OFST        uint8     0..7            Offset for the first DW used from operand
                                                             2

              7    IN4_OFST        uint8     0..7
                                                             Offset for the first DW used from operand
                                                             4

              8    IN_VPR          vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vsmpyx_v32_v32_v40_3op1op_const_conj_vmpsX_p (1, vIn, 0, vIn2, 0, 0, 0, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vsmpyx_v32_v32_v40_3op1op_const_conj_vmpsX_p version.


Main table → Multiplication → Split Multiply → Vector Split Complex Multiply
Intrinsic     vsmpyx_v32_v32_v40_3op1op_const[_p]
name
Spec syntax   vsmpyx {Sop ,const [,conj][,vmpsX]} vx[X], vy[Y], vx[W], vy[V] ,voz[0], ?vprX

Return type   vec40_t

              1    IN1_V32         vec_t                      Input vector operand

              2    IN1_OFST        uint8     0..7             Offset for the first DW used from operand
                                                              1

              3    IN2_V32         vec_t                      Input vector operand

              4    IN2_OFST        uint8     0..7             Offset for the first DW used from operand
Operands                                                      3

              5    IN3_OFST        uint8     0..7             Offset for the first DW used from operand
                                                              1

              6    IN4_OFST        uint8     0..7             Offset for the first DW used from operand
                                                              3

              7    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vsmpyx_v32_v32_v40_3op1op_const_p (vIn, 0, vIn2, 0, 0, 0, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.

vsmpyx_v32_v32_v40_3op1op_const_p version.


Main table → Multiplication → Split Multiply → Vector Split Complex Multiply
Intrinsic     vsmpyx_v32_v32_v40_3op1op_const_vmpsX[_p]
name
Spec syntax   vsmpyx {Sop ,const [,conj][,vmpsX]} vx[X], vy[Y], vx[W], vy[V] ,voz[0], ?vprX

Return type   vec40_t

                                                              Selects the VMSNX and VPSX set within
Operands      1    VMPSX           uint8     0,1
                                                              modv0/modv2 mode registers
             2    IN1_V32        vec_t                      Input vector operand

             3    IN1_OFST       uint8     0..7             Offset for the first DW used from operand
                                                            2

             4    IN2_V32        vec_t                      Input vector operand

             5    IN2_OFST       uint8     0..7             Offset for the first DW used from operand
                                                            4

             6    IN3_OFST       uint8     0..7             Offset for the first DW used from operand
                                                            2

             7    IN4_OFST       uint8     0..7             Offset for the first DW used from operand
                                                            4

             8    IN_VPR         vprex_t                    Vector predicate operand
             vec_t vIn;
             vec_t vIn2;
             vec40_t vRes;
C example    vprex_t vecPred;
             ...
             vRes = vsmpyx_v32_v32_v40_3op1op_const_vmpsX_p (1, vIn, 0, vIn2, 0, 0, 0, vecPred);

                  IN_VPR last operand is relevant only for
Comments     1.
                  vsmpyx_v32_v32_v40_3op1op_const_vmpsX_p version.


Main table → Multiplication → Split Multiply → Vector Split Complex Multiply
