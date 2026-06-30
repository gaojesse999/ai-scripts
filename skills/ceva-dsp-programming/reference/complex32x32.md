# Multiplication → Multiply-Subtract → Complex 32x32

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Multiplication → Multiply-Subtract → Complex 32x32

Complex 32x32

Complex 32x32
Performs complex multiplication subtract complex numbers. Each source is 64-bits wide (32-bit
real and 32-bit Imaginary). The products are accumulated into two 72-bit destinations.
Available Switches
              Number of atomic operations. An atomic operation is defined as a single complex
Dop
              multiply-subtract operation. 1op œ Dop œ 2op
conj          Performs complex multiply using complex conjugate of vcYe/vy[Ye]
const         When used, vy[Ye] is constant throughout the operations.
vmpsX         Selects the VMSNX and VPSX set within modv0 or modv2 mode registers.
Intrinsic Names
vmsullx_v32_c32_v40_1op_conj
vmsullx_v32_c32_v40_1op_conj_vmpsX
vmsullx_v32_c32_v40_1op

vmsullx_v32_c32_v40_1op_vmpsX
vmsullx_v32_v32_v40_conj_const
vmsullx_v32_v32_v40_conj_const_vmpsX
vmsullx_v32_v32_v40_conj
vmsullx_v32_v32_v40_conj_vmpsX
vmsullx_v32_v32_v40_const
vmsullx_v32_v32_v40_const_vmpsX
vmsullx_v32_v32_v40
vmsullx_v32_v32_v40_vmpsX
vmsullx_v32_c32_v40_conj
vmsullx_v32_c32_v40_conj_vmpsX
vmsullx_v32_c32_v40
vmsullx_v32_c32_v40_vmpsX
vmsullx_v32_v32_v40_1op_conj
vmsullx_v32_v32_v40_1op_conj_vmpsX
vmsullx_v32_v32_v40_1op
vmsullx_v32_v32_v40_1op_vmpsX
Instruction details in the instruction set specification
Intrinsic     vmsullx_v32_c32_v40_1op_conj[_p]
name
Spec syntax   vmsullx {1op [,conj] [,vmpsX]} vx[Xe], vcYe, vcX, voz[4], ?vprX

Return type   vec40_t

              1    IN1_V32         vec_t                      Input vector operand

              2    IN1_OFST        uint8     0,4
                                                              Offset for the first DW used from operand
                                                              1

Operands
              3    IN2_C32         coef_t                     Coefficient operand
              4    IN3_C32         coef_t                     Coefficient operand
              5    IN4_V40         vec40_t                    Output vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec40_t vRes;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              vprex_t vecPred;
              ...
              vRes = vmsullx_v32_c32_v40_1op_conj_p (vIn, 0, vcoefIn, vcoefIn2, vRes, vecPred);

                   IN_VPR last operand is relevant only for vmsullx_v32_c32_v40_1op_conj_p
Comments      1.
                   version.


Main table → Multiplication → Multiply-Subtract → Complex 32x32
Intrinsic     vmsullx_v32_c32_v40_1op_conj_vmpsX[_p]
name
Spec syntax   vmsullx {1op [,conj] [,vmpsX]} vx[Xe], vcYe, vcX, voz[4], ?vprX

Return type   vec40_t

                                                              Selects the VMSNX and VPSX set within
              1    VMPSX           uint8     0,1
                                                              modv0/modv2 mode registers
              2    IN1_V32         vec_t                      Input vector operand

              3    IN1_OFST        uint8     0,4              Offset for the first DW used from operand
                                                              2
Operands

4    IN2_C32         coef_t                     Coefficient operand
              5    IN3_C32         coef_t                     Coefficient operand
              6    IN4_V40         vec40_t                    Output vector operand
              7    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec40_t vRes;
C example     coef_t vcoefIn;
              coef_t vcoefIn2;
              vprex_t vecPred;
              ...
              vRes = vmsullx_v32_c32_v40_1op_conj_vmpsX_p (1, vIn, 0, vcoefIn, vcoefIn2, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsullx_v32_c32_v40_1op_conj_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Complex 32x32
Intrinsic     vmsullx_v32_c32_v40_1op[_p]
name
Spec syntax   vmsullx {1op [,conj] [,vmpsX]} vx[Xe], vcYe, vcX, voz[4], ?vprX

Return type   vec40_t

              1    IN1_V32         vec_t                      Input vector operand

              2    IN1_OFST        uint8     0,4              Offset for the first DW used from operand
                                                              1

Operands
              3    IN2_C32         coef_t                     Coefficient operand
              4    IN3_C32         coef_t                     Coefficient operand
              5    IN4_V40         vec40_t                    Output vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec40_t vRes;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              vprex_t vecPred;
              ...
              vRes = vmsullx_v32_c32_v40_1op_p (vIn, 0, vcoefIn, vcoefIn2, vRes, vecPred);

                   IN_VPR last operand is relevant only for vmsullx_v32_c32_v40_1op_p
Comments      1.
                   version.


Main table → Multiplication → Multiply-Subtract → Complex 32x32
Intrinsic     vmsullx_v32_c32_v40_1op_vmpsX[_p]
name
Spec syntax   vmsullx {1op [,conj] [,vmpsX]} vx[Xe], vcYe, vcX, voz[4], ?vprX

Return type   vec40_t

                                                              Selects the VMSNX and VPSX set within
              1    VMPSX           uint8     0,1
                                                              modv0/modv2 mode registers
              2    IN1_V32         vec_t                      Input vector operand
Operands

3    IN1_OFST        uint8     0,4
                                                              Offset for the first DW used from operand
                                                              2

              4    IN2_C32         coef_t                     Coefficient operand
            5    IN3_C32        coef_t                     Coefficient operand
            6    IN4_V40        vec40_t                    Output vector operand
            7    IN_VPR         vprex_t                    Vector predicate operand
            vec_t vIn;
            vec40_t vRes;
            coef_t vcoefIn;
C example   coef_t vcoefIn2;
            vprex_t vecPred;
            ...
            vRes = vmsullx_v32_c32_v40_1op_vmpsX_p (1, vIn, 0, vcoefIn, vcoefIn2, vRes, vecPred);

                 IN_VPR last operand is relevant only for
Comments    1.
                 vmsullx_v32_c32_v40_1op_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Complex 32x32
Intrinsic     vmsullx_v32_v32_v40_conj_const[_p]
name
Spec syntax   vmsullx {Dop [,conj][,const][,vmpsX]} vx[Xe], vy[Ye], voz[0], ?vprX

Return type   vec40_t

              1    DOP             uint8     1..2             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand

              3    IN1_OFST        uint8     0,4
                                                              Offset for the first DW used from operand
                                                              2

Operands      4    IN2_V32         vec_t                      Input vector operand

              5    IN2_OFST        uint8     0,4
                                                              Offset for the first DW used from operand
                                                              4

              6    IN3_V40         vec40_t                    Output vector operand
              7    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsullx_v32_v32_v40_conj_const_p (2, vIn, 0, vIn2, 0, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsullx_v32_v32_v40_conj_const_p version.


Main table → Multiplication → Multiply-Subtract → Complex 32x32
Intrinsic     vmsullx_v32_v32_v40_conj_const_vmpsX[_p]
name

Spec syntax   vmsullx {Dop [,conj][,const][,vmpsX]} vx[Xe], vy[Ye], voz[0], ?vprX

Return type   vec40_t

              1    DOP             uint8     1..2             Number of atomic operations

              2
                                                              Selects the VMSNX and VPSX set within
                   VMPSX           uint8     0,1
                                                              modv0/modv2 mode registers
              3    IN1_V32         vec_t                      Input vector operand

              4    IN1_OFST        uint8     0,4
                                                              Offset for the first DW used from operand
Operands                                                      3

              5    IN2_V32         vec_t                      Input vector operand

              6    IN2_OFST        uint8     0,4
                                                              Offset for the first DW used from operand
                                                              5

              7    IN3_V40         vec40_t                    Output vector operand
              8    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsullx_v32_v32_v40_conj_const_vmpsX_p (2, 1, vIn, 0, vIn2, 0, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsullx_v32_v32_v40_conj_const_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Complex 32x32
Intrinsic     vmsullx_v32_v32_v40_conj[_p]
name
Spec syntax   vmsullx {Dop [,conj][,const][,vmpsX]} vx[Xe], vy[Ye], voz[0], ?vprX

Return type   vec40_t

              1    DOP             uint8     1..2              Number of atomic operations
              2    IN1_V32         vec_t                       Input vector operand

              3    IN1_OFST        uint8     0,4
                                                               Offset for the first DW used from operand
                                                               2

Operands      4    IN2_V32         vec_t                       Input vector operand

              5    IN2_OFST        uint8     0,4
                                                               Offset for the first DW used from operand

4

              6    IN3_V40         vec40_t                     Output vector operand
              7    IN_VPR          vprex_t                     Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsullx_v32_v32_v40_conj_p (2, vIn, 0, vIn2, 0, vRes, vecPred);

                   IN_VPR last operand is relevant only for vmsullx_v32_v32_v40_conj_p
Comments      1.
                   version.


Main table → Multiplication → Multiply-Subtract → Complex 32x32
Intrinsic     vmsullx_v32_v32_v40_conj_vmpsX[_p]
name
Spec syntax   vmsullx {Dop [,conj][,const][,vmpsX]} vx[Xe], vy[Ye], voz[0], ?vprX

Return type   vec40_t

              1    DOP             uint8     1..2              Number of atomic operations
Operands                                                       Selects the VMSNX and VPSX set within
              2    VMPSX           uint8     0,1
                                                               modv0/modv2 mode registers
              3    IN1_V32         vec_t                       Input vector operand

              4    IN1_OFST        uint8     0,4               Offset for the first DW used from operand
                                                               3

              5    IN2_V32         vec_t                       Input vector operand

              6    IN2_OFST        uint8     0,4               Offset for the first DW used from operand
                                                               5

              7    IN3_V40         vec40_t                     Output vector operand
              8    IN_VPR          vprex_t                     Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsullx_v32_v32_v40_conj_vmpsX_p (2, 1, vIn, 0, vIn2, 0, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsullx_v32_v32_v40_conj_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Complex 32x32
Intrinsic     vmsullx_v32_v32_v40_const[_p]
name
Spec syntax   vmsullx {Dop [,conj][,const][,vmpsX]} vx[Xe], vy[Ye], voz[0], ?vprX

Return type   vec40_t

              1    DOP             uint8     1..2              Number of atomic operations

2    IN1_V32         vec_t                       Input vector operand

              3    IN1_OFST        uint8     0,4               Offset for the first DW used from operand
                                                               2

Operands      4    IN2_V32         vec_t                       Input vector operand

              5    IN2_OFST        uint8     0,4               Offset for the first DW used from operand
                                                               4

              6    IN3_V40         vec40_t                     Output vector operand
              7    IN_VPR          vprex_t                     Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsullx_v32_v32_v40_const_p (2, vIn, 0, vIn2, 0, vRes, vecPred);

                   IN_VPR last operand is relevant only for vmsullx_v32_v32_v40_const_p
Comments      1.
                   version.


Main table → Multiplication → Multiply-Subtract → Complex 32x32
Intrinsic     vmsullx_v32_v32_v40_const_vmpsX[_p]
name
Spec syntax   vmsullx {Dop [,conj][,const][,vmpsX]} vx[Xe], vy[Ye], voz[0], ?vprX

Return type   vec40_t

              1    DOP             uint8     1..2             Number of atomic operations
                                                              Selects the VMSNX and VPSX set within
              2    VMPSX           uint8     0,1
                                                              modv0/modv2 mode registers
              3    IN1_V32         vec_t                      Input vector operand

              4    IN1_OFST        uint8     0,4
                                                              Offset for the first DW used from operand
Operands                                                      3

              5    IN2_V32         vec_t                      Input vector operand

              6    IN2_OFST        uint8     0,4              Offset for the first DW used from operand
                                                              5

              7    IN3_V40         vec40_t                    Output vector operand
              8    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...

vRes = vmsullx_v32_v32_v40_const_vmpsX_p (2, 1, vIn, 0, vIn2, 0, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsullx_v32_v32_v40_const_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Complex 32x32
Intrinsic     vmsullx_v32_v32_v40[_p]
name
Spec syntax   vmsullx {Dop [,conj][,const][,vmpsX]} vx[Xe], vy[Ye], voz[0], ?vprX

Return type   vec40_t

              1    DOP             uint8     1..2             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand

              3    IN1_OFST        uint8     0,4
                                                              Offset for the first DW used from operand
                                                              2

Operands      4    IN2_V32         vec_t                      Input vector operand

              5    IN2_OFST        uint8     0,4
                                                              Offset for the first DW used from operand
                                                              4

              6    IN3_V40         vec40_t                    Output vector operand
              7    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsullx_v32_v32_v40_p (2, vIn, 0, vIn2, 0, vRes, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmsullx_v32_v32_v40_p version.


Main table → Multiplication → Multiply-Subtract → Complex 32x32
Intrinsic     vmsullx_v32_v32_v40_vmpsX[_p]
name
Spec syntax   vmsullx {Dop [,conj][,const][,vmpsX]} vx[Xe], vy[Ye], voz[0], ?vprX

Return type   vec40_t

              1    DOP             uint8      1..2             Number of atomic operations
                                                               Selects the VMSNX and VPSX set within
              2    VMPSX           uint8      0,1
                                                               modv0/modv2 mode registers
              3    IN1_V32         vec_t                       Input vector operand

              4    IN1_OFST        uint8      0,4
                                                               Offset for the first DW used from operand
Operands                                                       3

5    IN2_V32         vec_t                       Input vector operand

              6    IN2_OFST        uint8      0,4
                                                               Offset for the first DW used from operand
                                                               5

              7    IN3_V40         vec40_t                     Output vector operand
              8    IN_VPR          vprex_t                     Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsullx_v32_v32_v40_vmpsX_p (2, 1, vIn, 0, vIn2, 0, vRes, vecPred);

                   IN_VPR last operand is relevant only for vmsullx_v32_v32_v40_vmpsX_p
Comments      1.
                   version.


Main table → Multiplication → Multiply-Subtract → Complex 32x32
Intrinsic     vmsullx_v32_c32_v40_conj[_p]
name
Spec syntax   vmsullx {Dop [,conj] [,vmpsX]} vx[Xe], vcYe, vcX, voz[0], ?vprX

Return type   vec40_t

              1    DOP             uint8     1..2              Number of atomic operations
              2    IN1_V32         vec_t                       Input vector operand

              3    IN1_OFST        uint8     0,4
                                                               Offset for the first DW used from operand
                                                               2
Operands      4    IN2_C32         coef_t                      Coefficient operand
              5    IN3_C32         coef_t                      Coefficient operand
              6    IN4_V40         vec40_t                     Output vector operand
              7    IN_VPR          vprex_t                     Vector predicate operand
              vec_t vIn;
              vec40_t vRes;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              vprex_t vecPred;
              ...
              vRes = vmsullx_v32_c32_v40_conj_p (2, vIn, 0, vcoefIn, vcoefIn2, vRes, vecPred);

                   IN_VPR last operand is relevant only for vmsullx_v32_c32_v40_conj_p
Comments      1.
                   version.


Main table → Multiplication → Multiply-Subtract → Complex 32x32
Intrinsic     vmsullx_v32_c32_v40_conj_vmpsX[_p]
name
Spec syntax   vmsullx {Dop [,conj] [,vmpsX]} vx[Xe], vcYe, vcX, voz[0], ?vprX

Return type   vec40_t

              1    DOP             uint8     1..2              Number of atomic operations

              2

Selects the VMSNX and VPSX set within
                   VMPSX           uint8     0,1
                                                               modv0/modv2 mode registers
              3    IN1_V32         vec_t                       Input vector operand

              4    IN1_OFST        uint8     0,4
                                                               Offset for the first DW used from operand
Operands                                                       3

              5    IN2_C32         coef_t                      Coefficient operand
              6    IN3_C32         coef_t                      Coefficient operand
              7    IN4_V40         vec40_t                     Output vector operand
              8    IN_VPR          vprex_t                     Vector predicate operand
              vec_t vIn;
              vec40_t vRes;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              vprex_t vecPred;
              ...
              vRes = vmsullx_v32_c32_v40_conj_vmpsX_p (2, 1, vIn, 0, vcoefIn, vcoefIn2, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsullx_v32_c32_v40_conj_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Complex 32x32
Intrinsic     vmsullx_v32_c32_v40[_p]
name
Spec syntax   vmsullx {Dop [,conj] [,vmpsX]} vx[Xe], vcYe, vcX, voz[0], ?vprX

Return type   vec40_t

              1    DOP             uint8      1..2             Number of atomic operations
              2    IN1_V32         vec_t                       Input vector operand

              3    IN1_OFST        uint8      0,4              Offset for the first DW used from operand
                                                               2
Operands      4    IN2_C32         coef_t                      Coefficient operand
              5    IN3_C32         coef_t                      Coefficient operand
              6    IN4_V40         vec40_t                     Output vector operand
              7    IN_VPR          vprex_t                     Vector predicate operand
              vec_t vIn;
              vec40_t vRes;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              vprex_t vecPred;
              ...
              vRes = vmsullx_v32_c32_v40_p (2, vIn, 0, vcoefIn, vcoefIn2, vRes, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmsullx_v32_c32_v40_p version.

Main table → Multiplication → Multiply-Subtract → Complex 32x32
Intrinsic     vmsullx_v32_c32_v40_vmpsX[_p]
name
Spec syntax   vmsullx {Dop [,conj] [,vmpsX]} vx[Xe], vcYe, vcX, voz[0], ?vprX

Return type   vec40_t

              1    DOP             uint8      1..2             Number of atomic operations
Operands                                                       Selects the VMSNX and VPSX set within
              2    VMPSX           uint8      0,1
                                                               modv0/modv2 mode registers
            3    IN1_V32         vec_t                      Input vector operand

            4    IN1_OFST        uint8     0,4              Offset for the first DW used from operand
                                                            3

            5    IN2_C32         coef_t                     Coefficient operand
            6    IN3_C32         coef_t                     Coefficient operand
            7    IN4_V40         vec40_t                    Output vector operand
            8    IN_VPR          vprex_t                    Vector predicate operand
            vec_t vIn;
            vec40_t vRes;
            coef_t vcoefIn;
C example   coef_t vcoefIn2;
            vprex_t vecPred;
            ...
            vRes = vmsullx_v32_c32_v40_vmpsX_p (2, 1, vIn, 0, vcoefIn, vcoefIn2, vRes, vecPred);

                 IN_VPR last operand is relevant only for vmsullx_v32_c32_v40_vmpsX_p
Comments    1.
                 version.


Main table → Multiplication → Multiply-Subtract → Complex 32x32
Intrinsic     vmsullx_v32_v32_v40_1op_conj[_p]
name
Spec syntax   vmsullx {1op [,conj][,vmpsX]} vx[Xe], vy[Ye], voz[4], ?vprX

Return type   vec40_t

              1    IN1_V32         vec_t                      Input vector operand

              2    IN1_OFST        uint8     0,4
                                                              Offset for the first DW used from operand
                                                              1

              3    IN2_V32         vec_t                      Input vector operand
Operands
              4    IN2_OFST        uint8     0,4
                                                              Offset for the first DW used from operand
                                                              3

              5    IN3_V40         vec40_t                    Output vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand

vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsullx_v32_v32_v40_1op_conj_p (vIn, 0, vIn2, 0, vRes, vecPred);

                   IN_VPR last operand is relevant only for vmsullx_v32_v32_v40_1op_conj_p
Comments      1.
                   version.


Main table → Multiplication → Multiply-Subtract → Complex 32x32
Intrinsic     vmsullx_v32_v32_v40_1op_conj_vmpsX[_p]
name
Spec syntax   vmsullx {1op [,conj][,vmpsX]} vx[Xe], vy[Ye], voz[4], ?vprX

Return type   vec40_t

                                                              Selects the VMSNX and VPSX set within
              1    VMPSX           uint8     0,1
                                                              modv0/modv2 mode registers
              2    IN1_V32         vec_t                      Input vector operand

              3    IN1_OFST        uint8     0,4              Offset for the first DW used from operand
                                                              2
Operands      4    IN2_V32         vec_t                      Input vector operand

              5    IN2_OFST        uint8     0,4
                                                              Offset for the first DW used from operand
                                                              4

              6    IN3_V40         vec40_t                    Output vector operand
              7    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
C example     vec_t vIn2;
              vec40_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmsullx_v32_v32_v40_1op_conj_vmpsX_p (1, vIn, 0, vIn2, 0, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsullx_v32_v32_v40_1op_conj_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Complex 32x32
Intrinsic     vmsullx_v32_v32_v40_1op[_p]
name
Spec syntax   vmsullx {1op [,conj][,vmpsX]} vx[Xe], vy[Ye], voz[4], ?vprX

Return type   vec40_t

              1    IN1_V32         vec_t                      Input vector operand

              2    IN1_OFST        uint8     0,4              Offset for the first DW used from operand
                                                              1

              3    IN2_V32         vec_t                      Input vector operand
Operands

4    IN2_OFST        uint8     0,4              Offset for the first DW used from operand
                                                              3

              5    IN3_V40         vec40_t                    Output vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsullx_v32_v32_v40_1op_p (vIn, 0, vIn2, 0, vRes, vecPred);

                   IN_VPR last operand is relevant only for vmsullx_v32_v32_v40_1op_p
Comments      1.
                   version.


Main table → Multiplication → Multiply-Subtract → Complex 32x32
Intrinsic     vmsullx_v32_v32_v40_1op_vmpsX[_p]
name
Spec syntax   vmsullx {1op [,conj][,vmpsX]} vx[Xe], vy[Ye], voz[4], ?vprX

Return type   vec40_t

                                                              Selects the VMSNX and VPSX set within
              1    VMPSX           uint8     0,1
                                                              modv0/modv2 mode registers
              2    IN1_V32         vec_t                      Input vector operand
Operands
              3    IN1_OFST        uint8     0,4
                                                              Offset for the first DW used from operand
                                                              2

              4    IN2_V32         vec_t                      Input vector operand
            5    IN2_OFST       uint8     0,4              Offset for the first DW used from operand
                                                           4

            6    IN3_V40        vec40_t                    Output vector operand
            7    IN_VPR         vprex_t                    Vector predicate operand
            vec_t vIn;
            vec_t vIn2;
            vec40_t vRes;
C example   vprex_t vecPred;
            ...
            vRes = vmsullx_v32_v32_v40_1op_vmpsX_p (1, vIn, 0, vIn2, 0, vRes, vecPred);

                 IN_VPR last operand is relevant only for
Comments    1.
                 vmsullx_v32_v32_v40_1op_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Complex 32x32
