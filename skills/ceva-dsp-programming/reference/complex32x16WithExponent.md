# Multiplication → Multiply-Subtract → Complex 32x16 with Exponent

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Multiplication → Multiply-Subtract → Complex 32x16 with Exponent

Complex 32x16 with Exponent

Complex 32x16 with Exponent
Performs complex multiply-subtract with exponent between two complex numbers. The first
complex source consists of real 32-bit part and imaginary 32-bit part. The second complex
source consists of real 16-bit part and imaginary 16-bit part. Each of the real and the imaginary
products are subtractd with the 40-bit destination respectively.
Available Switches
                 Number of atomic operations. An atomic operation is defined as a complex 32x16
Qop
                 multiply-subtract with exponenet operation.
conj             conjugate complex operation on 16-bit complex source
conj32           conjugate complex operation on 32-bit complex source
vmpsX            Selects the VMSNX and VPSX set within modv0 or modv2 mode registers.
Intrinsic Names
vmsulwxe_v32_v32_v32_v40_conj32
vmsulwxe_v32_v32_v32_v40_conj32_vmpsX
vmsulwxe_v32_v32_v32_v40_conj
vmsulwxe_v32_v32_v32_v40_conj_vmpsX
vmsulwxe_v32_v32_v32_v40
vmsulwxe_v32_v32_v32_v40_vmpsX
Instruction details in the instruction set specification
Intrinsic     vmsulwxe_v32_v32_v32_v40_conj32[_p]
name
Spec syntax   vmsulwxe {Qop [,conj_conj32][,vmpsX]} vx[Xe], vy[Y], vv[V]p, voz[0], ?vprX

Return type   vec40_t

1    QOP            uint8      1..4            Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8      0,4
                                                             Offset for the first DW used from operand
                                                             2

              4    IN2_V32        vec_t                      Input vector operand

              5    IN2_OFST       uint8      0,4
                                                             Offset for the first DW used from operand
                                                             4
Operands
              6    IN3_V32        vec_t                      Input vector operand

              7    IN3_OFST       uint8      0,4             Offset for the first DW used from operand
                                                             6

              8    IN3_PART       uint8      LOW,HIGH        Word part which is used for operand 6
              9    IN4_V40        vec40_t                    Output vector operand
              10   IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
C example     vec40_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmsulwxe_v32_v32_v32_v40_conj32_p (4, vIn, 0, vIn2, 0, vIn3, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsulwxe_v32_v32_v32_v40_conj32_p version.


Main table → Multiplication → Multiply-Subtract → Complex 32x16 with Exponent
Intrinsic     vmsulwxe_v32_v32_v32_v40_conj32_vmpsX[_p]
name
Spec syntax   vmsulwxe {Qop [,conj_conj32][,vmpsX]} vx[Xe], vy[Y], vv[V]p, voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8      1..4            Number of atomic operations
                                                             Selects the VMSNX and VPSX set within
              2    VMPSX          uint8      0,1
                                                             modv0/modv2 mode registers
Operands
              3    IN1_V32        vec_t                      Input vector operand

              4    IN1_OFST       uint8      0,4
                                                             Offset for the first DW used from operand
                                                             3

5    IN2_V32        vec_t                     Input vector operand

              6    IN2_OFST       uint8     0,4             Offset for the first DW used from operand
                                                            5

              7    IN3_V32        vec_t                     Input vector operand

              8    IN3_OFST       uint8     0,4             Offset for the first DW used from operand
                                                            7

              9    IN3_PART       uint8     LOW,HIGH        Word part which is used for operand 7
              10   IN4_V40        vec40_t                   Output vector operand
              11   IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsulwxe_v32_v32_v32_v40_conj32_vmpsX_p (4, 1, vIn, 0, vIn2, 0, vIn3, 0, LOW, vRes,
              vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsulwxe_v32_v32_v32_v40_conj32_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Complex 32x16 with Exponent
Intrinsic     vmsulwxe_v32_v32_v32_v40_conj[_p]
name
Spec syntax   vmsulwxe {Qop [,conj_conj32][,vmpsX]} vx[Xe], vy[Y], vv[V]p, voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0,4
                                                            Offset for the first DW used from operand
                                                            2

              4    IN2_V32        vec_t                     Input vector operand

              5    IN2_OFST       uint8     0,4
                                                            Offset for the first DW used from operand
                                                            4
Operands
              6    IN3_V32        vec_t                     Input vector operand

              7    IN3_OFST       uint8     0,4             Offset for the first DW used from operand
                                                            6

              8    IN3_PART       uint8     LOW,HIGH        Word part which is used for operand 6

9    IN4_V40        vec40_t                   Output vector operand
              10   IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
C example     vec40_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmsulwxe_v32_v32_v32_v40_conj_p (4, vIn, 0, vIn2, 0, vIn3, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsulwxe_v32_v32_v32_v40_conj_p version.


Main table → Multiplication → Multiply-Subtract → Complex 32x16 with Exponent
Intrinsic     vmsulwxe_v32_v32_v32_v40_conj_vmpsX[_p]
name
Spec syntax   vmsulwxe {Qop [,conj_conj32][,vmpsX]} vx[Xe], vy[Y], vv[V]p, voz[0], ?vprX

Return type   vec40_t

              1    QOP             uint8     1..4             Number of atomic operations
                                                              Selects the VMSNX and VPSX set within
              2    VMPSX           uint8     0,1
                                                              modv0/modv2 mode registers
              3    IN1_V32         vec_t                      Input vector operand

              4    IN1_OFST        uint8     0,4              Offset for the first DW used from operand
                                                              3

              5    IN2_V32         vec_t                      Input vector operand
Operands      6    IN2_OFST        uint8                      Offset for the first DW used from operand
                                             0,4
                                                              5

              7    IN3_V32         vec_t                      Input vector operand

              8    IN3_OFST        uint8     0,4
                                                              Offset for the first DW used from operand
                                                              7

              9    IN3_PART        uint8     LOW,HIGH         Word part which is used for operand 7
              10   IN4_V40         vec40_t                    Output vector operand
              11   IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
C example     vec40_t vRes;
              vprex_t vecPred;
              ...

vRes = vmsulwxe_v32_v32_v32_v40_conj_vmpsX_p (4, 1, vIn, 0, vIn2, 0, vIn3, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsulwxe_v32_v32_v32_v40_conj_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Complex 32x16 with Exponent
Intrinsic     vmsulwxe_v32_v32_v32_v40[_p]
name
Spec syntax   vmsulwxe {Qop [,conj_conj32][,vmpsX]} vx[Xe], vy[Y], vv[V]p, voz[0], ?vprX

Return type   vec40_t

              1    QOP             uint8     1..4             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand

              3    IN1_OFST        uint8     0,4
                                                              Offset for the first DW used from operand
                                                              2

              4    IN2_V32         vec_t                      Input vector operand

              5    IN2_OFST        uint8     0,4
                                                              Offset for the first DW used from operand
                                                              4
Operands
              6    IN3_V32         vec_t                      Input vector operand

              7    IN3_OFST        uint8     0,4              Offset for the first DW used from operand
                                                              6

              8    IN3_PART        uint8     LOW,HIGH         Word part which is used for operand 6
              9    IN4_V40         vec40_t                    Output vector operand
              10   IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
C example     vec40_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmsulwxe_v32_v32_v32_v40_p (4, vIn, 0, vIn2, 0, vIn3, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for vmsulwxe_v32_v32_v32_v40_p
Comments      1.
                   version.


Main table → Multiplication → Multiply-Subtract → Complex 32x16 with Exponent
Intrinsic     vmsulwxe_v32_v32_v32_v40_vmpsX[_p]
name
Spec syntax   vmsulwxe {Qop [,conj_conj32][,vmpsX]} vx[Xe], vy[Y], vv[V]p, voz[0], ?vprX

Return type   vec40_t

              1    QOP             uint8     1..4             Number of atomic operations

Selects the VMSNX and VPSX set within
              2    VMPSX           uint8     0,1
                                                              modv0/modv2 mode registers
Operands
              3    IN1_V32         vec_t                      Input vector operand

              4    IN1_OFST        uint8     0,4
                                                              Offset for the first DW used from operand
                                                              3
            5    IN2_V32        vec_t                      Input vector operand

            6    IN2_OFST       uint8     0,4              Offset for the first DW used from operand
                                                           5

            7    IN3_V32        vec_t                      Input vector operand

            8    IN3_OFST       uint8     0,4              Offset for the first DW used from operand
                                                           7

            9    IN3_PART       uint8     LOW,HIGH         Word part which is used for operand 7
            10   IN4_V40        vec40_t                    Output vector operand
            11   IN_VPR         vprex_t                    Vector predicate operand
            vec_t vIn;
            vec_t vIn2;
            vec_t vIn3;
C example   vec40_t vRes;
            vprex_t vecPred;
            ...
            vRes = vmsulwxe_v32_v32_v32_v40_vmpsX_p (4, 1, vIn, 0, vIn2, 0, vIn3, 0, LOW, vRes, vecPred);

                 IN_VPR last operand is relevant only for
Comments    1.
                 vmsulwxe_v32_v32_v32_v40_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Complex 32x16 with Exponent
