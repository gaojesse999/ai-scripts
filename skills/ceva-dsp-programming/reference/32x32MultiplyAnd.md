# Multiplication → Multiply and Add Two Products → 32x32 Multiply and

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Multiplication → Multiply and Add Two Products → 32x32 Multiply and
Add Two Products

32x32 Multiply and Add Two Products

32x32 Multiply and Add Two Products
Performs multiplication and addition between two products. Each source is 32-bit wide. The
result is placed into 72-bit destination.
Available Switches
           Number of atomic operations. An atomic operation is defined as a single add-two-
Qop
           products operation. 1op ≤ Qop ≤ 4op
const      When used, vy[Y]/vy[V] are constant throughout the operations.
vmpsX Selects the VMSNX and VPSX set within modv0 or modv2 mode registers.
Intrinsic Names
vmadll_v32_c32_c32_v32
vmadll_v32_c32_c32_v32_vmpsX
vmadll_v32_v32_v32_const
vmadll_v32_v32_v32_const_vmpsX
vmadll_v32_v32_v32
vmadll_v32_v32_v32_vmpsX
Instruction details in the instruction set specification
Intrinsic     vmadll_v32_c32_c32_v32[_p]
name
Spec syntax   vmadll {Qop [,vmpsX]} vx[X], vcY, vx[W], vcV, vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4              Number of atomic operations
              2    IN1_V32         vec_t                       Input vector operand

              3    IN1_OFST        uint8     0,4
                                                               Offset for the first DW used from operand
                                                               2

Operands      4    IN2_C32         vec_t                       Coefficient operand

              5    IN3_OFST        uint8     0,4
                                                               Offset for the first DW used from operand
                                                               2

              6    IN4_C32         coef_t                      Coefficient operand
              7    IN_VPR          vprex_t                     Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              vec_t vcoefIn;
C example     coef_t vcoefIn2;
              vprex_t vecPred;
              ...
              vRes = vmadll_v32_c32_c32_v32_p (4, vIn, 0, vcoefIn, 0, vcoefIn2, vecPred);

                   IN_VPR last operand is relevant only for vmadll_v32_c32_c32_v32_p
Comments      1.
                   version.


Main table → Multiplication → Multiply and Add Two Products → 32x32 Multiply and
Add Two Products
Intrinsic     vmadll_v32_c32_c32_v32_vmpsX[_p]
name
Spec syntax   vmadll {Qop [,vmpsX]} vx[X], vcY, vx[W], vcV, vz[0], ?vprX

Return type   vec_t

1    QOP             uint8     1..4              Number of atomic operations
                                                               Selects the VMSNX and VPSX set within
              2    VMPSX           uint8     0,1
                                                               modv0/modv2 mode registers
              3    IN1_V32         vec_t                       Input vector operand
Operands
              4    IN1_OFST        uint8     0,4
                                                               Offset for the first DW used from operand
                                                               3

              5    IN2_C32         vec_t                       Coefficient operand

              6    IN3_OFST        uint8     0,4
                                                               Offset for the first DW used from operand
                                                               3
            7    IN4_C32         coef_t                     Coefficient operand
            8    IN_VPR          vprex_t                    Vector predicate operand
            vec_t vIn;
            vec_t vRes;
            vec_t vcoefIn;
C example   coef_t vcoefIn2;
            vprex_t vecPred;
            ...
            vRes = vmadll_v32_c32_c32_v32_vmpsX_p (4, 1, vIn, 0, vcoefIn, 0, vcoefIn2, vecPred);

                 IN_VPR last operand is relevant only for
Comments    1.
                 vmadll_v32_c32_c32_v32_vmpsX_p version.


Main table → Multiplication → Multiply and Add Two Products → 32x32 Multiply and
Add Two Products
Intrinsic     vmadll_v32_v32_v32_const[_p]
name
Spec syntax   vmadll {Qop [,const][,vmpsX]} vx[X], vy[Y], vx[W], vy[V], vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8      1..4              Number of atomic operations
              2    IN1_V32         vec_t                        Input vector operand

              3    IN1_OFST        uint8      0,4
                                                                Offset for the first DW used from operand
                                                                2

              4    IN2_V32         vec_t                        Input vector operand
Operands      5    IN2_OFST        uint8      0,4
                                                                Offset for the first DW used from operand
                                                                4

              6    IN3_OFST        uint8      0,4

Offset for the first DW used from operand
                                                                2

              7    IN4_OFST        uint8      0,4
                                                                Offset for the first DW used from operand
                                                                4

              8    IN_VPR          vprex_t                      Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmadll_v32_v32_v32_const_p (4, vIn, 0, vIn2, 0, 0, 0, vecPred);

                   IN_VPR last operand is relevant only for vmadll_v32_v32_v32_const_p
Comments      1.
                   version.


Main table → Multiplication → Multiply and Add Two Products → 32x32 Multiply and
Add Two Products
Intrinsic     vmadll_v32_v32_v32_const_vmpsX[_p]
name
Spec syntax   vmadll {Qop [,const][,vmpsX]} vx[X], vy[Y], vx[W], vy[V], vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8      1..4              Number of atomic operations
                                                                Selects the VMSNX and VPSX set within
              2    VMPSX           uint8      0,1
                                                                modv0/modv2 mode registers
Operands      3    IN1_V32         vec_t                        Input vector operand

              4    IN1_OFST        uint8      0,4
                                                                Offset for the first DW used from operand
                                                                3

              5    IN2_V32         vec_t                        Input vector operand
              6    IN2_OFST         uint8     0,4               Offset for the first DW used from operand
                                                                5

              7    IN3_OFST         uint8     0,4               Offset for the first DW used from operand
                                                                3

              8    IN4_OFST         uint8     0,4
                                                                Offset for the first DW used from operand
                                                                5

              9    IN_VPR           vprex_t                     Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;

C example     vprex_t vecPred;
              ...
              vRes = vmadll_v32_v32_v32_const_vmpsX_p (4, 1, vIn, 0, vIn2, 0, 0, 0, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmadll_v32_v32_v32_const_vmpsX_p version.


Main table → Multiplication → Multiply and Add Two Products → 32x32 Multiply and
Add Two Products
Intrinsic     vmadll_v32_v32_v32[_p]
name
Spec syntax   vmadll {Qop [,const][,vmpsX]} vx[X], vy[Y], vx[W], vy[V], vz[0], ?vprX

Return type   vec_t

              1    QOP              uint8     1..4              Number of atomic operations
              2    IN1_V32          vec_t                       Input vector operand

              3    IN1_OFST         uint8     0,4
                                                                Offset for the first DW used from operand
                                                                2

              4    IN2_V32          vec_t                       Input vector operand
Operands      5    IN2_OFST         uint8     0,4
                                                                Offset for the first DW used from operand
                                                                4

              6    IN3_OFST         uint8     0,4
                                                                Offset for the first DW used from operand
                                                                2

              7    IN4_OFST         uint8     0,4
                                                                Offset for the first DW used from operand
                                                                4

              8    IN_VPR           vprex_t                     Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmadll_v32_v32_v32_p (4, vIn, 0, vIn2, 0, 0, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmadll_v32_v32_v32_p version.

Main table → Multiplication → Multiply and Add Two Products → 32x32 Multiply and
Add Two Products
Intrinsic     vmadll_v32_v32_v32_vmpsX[_p]
name
Spec syntax   vmadll {Qop [,const][,vmpsX]} vx[X], vy[Y], vx[W], vy[V], vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4              Number of atomic operations

Selects the VMSNX and VPSX set within
              2    VMPSX           uint8     0,1
                                                               modv0/modv2 mode registers
              3    IN1_V32         vec_t                       Input vector operand

              4    IN1_OFST        uint8     0,4               Offset for the first DW used from operand
                                                               3

Operands      5    IN2_V32         vec_t                       Input vector operand

              6    IN2_OFST        uint8     0,4               Offset for the first DW used from operand
                                                               5

              7    IN3_OFST        uint8     0,4               Offset for the first DW used from operand
                                                               3

              8    IN4_OFST        uint8     0,4
                                                               Offset for the first DW used from operand
                                                               5

              9    IN_VPR          vprex_t                     Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmadll_v32_v32_v32_vmpsX_p (4, 1, vIn, 0, vIn2, 0, 0, 0, vecPred);

                   IN_VPR last operand is relevant only for vmadll_v32_v32_v32_vmpsX_p
Comments      1.
                   version.


Main table → Multiplication → Multiply and Add Two Products → 32x32 Multiply and
Add Two Products
