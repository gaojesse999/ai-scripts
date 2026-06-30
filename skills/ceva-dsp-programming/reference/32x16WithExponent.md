# Multiplication → Multiply-Subtract → 32x16 with Exponent

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Multiplication → Multiply-Subtract → 32x16 with Exponent

32x16 with Exponent

32x16 with Exponent
Performs multiply-subtract with exponent. The first source is 32-bit wide and the second source
is 16-bit wide. The products are subtractd with the 40-bit destination.
Available Switches

Number of atomic operations. An atomic operation is defined as a single 32x16
Oop
              multiply-subtract with Exponent operation.
vmpsX         Selects the VMSNX and VPSX set within modv0 or modv2 mode registers.
Intrinsic Names
vmsulwe_v32_v32_v32_v40
vmsulwe_v32_v32_v32_v40_vmpsX
Instruction details in the instruction set specification
Intrinsic     vmsulwe_v32_v32_v32_v40[_p]
name
Spec syntax   vmsulwe {Oop [,vmpsX]} vx[X], vy[Y]p, vv[V]p, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             2

              4    IN2_V32        vec_t                      Input vector operand

              5    IN2_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             4
Operands      6    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 4
              7    IN3_V32        vec_t                      Input vector operand

              8    IN3_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             7

              9    IN3_PART       uint8     LOW,HIGH         Word part which is used for operand 7
              10   IN4_V40        vec40_t                    Output vector operand
              11   IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
C example     vec40_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmsulwe_v32_v32_v32_v40_p (8, vIn, 0, vIn2, 0, LOW, vIn3, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for vmsulwe_v32_v32_v32_v40_p
Comments      1.
                   version.


Main table → Multiplication → Multiply-Subtract → 32x16 with Exponent
Intrinsic     vmsulwe_v32_v32_v32_v40_vmpsX[_p]
name
Spec syntax   vmsulwe {Oop [,vmpsX]} vx[X], vy[Y]p, vv[V]p, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8             Number of atomic operations

Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
Operands                                                     modv0/modv2 mode registers
              3    IN1_V32        vec_t                      Input vector operand
              4    IN1_OFST       uint8     0..7             Offset for the first DW used from operand
                                                           3

            5    IN2_V32        vec_t                      Input vector operand

            6    IN2_OFST       uint8     0..7             Offset for the first DW used from operand
                                                           5

            7    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 5
            8    IN3_V32        vec_t                      Input vector operand

            9    IN3_OFST       uint8     0..7             Offset for the first DW used from operand
                                                           8

            10   IN3_PART       uint8     LOW,HIGH         Word part which is used for operand 8
            11   IN4_V40        vec40_t                    Output vector operand
            12   IN_VPR         vprex_t                    Vector predicate operand
            vec_t vIn;
            vec_t vIn2;
            vec_t vIn3;
C example   vec40_t vRes;
            vprex_t vecPred;
            ...
            vRes = vmsulwe_v32_v32_v32_v40_vmpsX_p (8, 1, vIn, 0, vIn2, 0, LOW, vIn3, 0, LOW, vRes, vecPred);

                 IN_VPR last operand is relevant only for
Comments    1.
                 vmsulwe_v32_v32_v32_v40_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → 32x16 with Exponent
