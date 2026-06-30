# Multiplication → Multiply-Subtract → 16x16 with Exponent

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Multiplication → Multiply-Subtract → 16x16 with Exponent

16x16 with Exponent

16x16 with Exponent
Performs multiply-Subtract between two sources with exponent operation using third source.
Each source is 16-bit wide. The product is accumulated with the 40-bit destination.
Available Switches

Number of atomic operations. An atomic operation is defined as a single 16x16
           multiply-Subtract with exponent operation. Writes to two vector destinations, where the
Hhop
           first vector destination is fully written, and the second vector destination is set according
           to Hhop switch.
           Number of atomic operations. An atomic operation is defined as a single 16x16
Oop
           multiply-Subtract with exponent operation.
vmpsX Selects the VMSNX and VPSX set within modv0 or modv2 mode registers.
Intrinsic Names
vmsue_v32_v32_v32_v40
vmsue_v32_v32_v32_v40_vmpsX
vmsue_v32_v32_v32_v40_v40
vmsue_v32_v32_v32_v40_v40_vmpsX
Instruction details in the instruction set specification
Intrinsic     vmsue_v32_v32_v32_v40[_p]
name
Spec syntax   vmsue {Oop [,vmpsX]} vx[X]p, vy[Y]p, vv[V]p, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             2

              4    IN1_PART       uint8     LOW,HIGH         Word part which is used for operand 2
              5    IN2_V32        vec_t                      Input vector operand

              6    IN2_OFST       uint8     0..7             Offset for the first DW used from operand
Operands                                                     5

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
C example     vec40_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmsue_v32_v32_v32_v40_p (8, vIn, 0, LOW, vIn2, 0, LOW, vIn3, 0, LOW, vRes, vecPred);

IN_VPR last operand is relevant only for vmsue_v32_v32_v32_v40_p
Comments      1.
                   version.


Main table → Multiplication → Multiply-Subtract → 16x16 with Exponent
Intrinsic     vmsue_v32_v32_v32_v40_vmpsX[_p]
name
Spec syntax   vmsue {Oop [,vmpsX]} vx[X]p, vy[Y]p, vv[V]p, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8             Number of atomic operations
                                                             Selects the VMSNX and VPSX set within
Operands      2    VMPSX          uint8     0,1
                                                             modv0/modv2 mode registers
              3    IN1_V32        vec_t                      Input vector operand
            4    IN1_OFST       uint8     0..7            Offset for the first DW used from operand
                                                          3

            5    IN1_PART       uint8     LOW,HIGH        Word part which is used for operand 3
            6    IN2_V32        vec_t                     Input vector operand

            7    IN2_OFST       uint8     0..7            Offset for the first DW used from operand
                                                          6

            8    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 6
            9    IN3_V32        vec_t                     Input vector operand

            10   IN3_OFST       uint8     0..7
                                                          Offset for the first DW used from operand
                                                          9

            11   IN3_PART       uint8     LOW,HIGH        Word part which is used for operand 9
            12   IN4_V40        vec40_t                   Output vector operand
            13   IN_VPR         vprex_t                   Vector predicate operand
            vec_t vIn;
            vec_t vIn2;
            vec_t vIn3;
            vec40_t vRes;
C example   vprex_t vecPred;
            ...
            vRes = vmsue_v32_v32_v32_v40_vmpsX_p (8, 1, vIn, 0, LOW, vIn2, 0, LOW, vIn3, 0, LOW, vRes,
            vecPred);

                 IN_VPR last operand is relevant only for
Comments    1.
                 vmsue_v32_v32_v32_v40_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → 16x16 with Exponent
Intrinsic     vmsue_v32_v32_v32_v40_v40[_p]
name
Spec syntax   vmsue {Hhop [,vmpsX]} vx[X]p, vy[Y]p, vv[V]p, voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    HHOP           uint8     9..16           Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            2

              4    IN1_PART       uint8     LOW,HIGH        Word part which is used for operand 2
              5    IN2_V32        vec_t                     Input vector operand

              6    IN2_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            5
Operands      7    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 5
              8    IN3_V32        vec_t                     Input vector operand

              9    IN3_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            8

              10   IN3_PART       uint8     LOW,HIGH        Word part which is used for operand 8
              11   IN4_V40        vec40_t                   Output vector operand
              12   RES2_V40       vec40_t                   Output vector result operand
              13   IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec40_t vRes1;
C example     vec40_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vmsue_v32_v32_v32_v40_v40_p (16, vIn, 0, LOW, vIn2, 0, LOW, vIn3, 0, LOW, vRes1, vRes2,
              vecPred);

                   IN_VPR last operand is relevant only for vmsue_v32_v32_v32_v40_v40_p
              1.
                   version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).


Main table → Multiplication → Multiply-Subtract → 16x16 with Exponent
Intrinsic     vmsue_v32_v32_v32_v40_v40_vmpsX[_p]
name
Spec syntax   vmsue {Hhop [,vmpsX]} vx[X]p, vy[Y]p, vv[V]p, voz1[0], voz2[0], ?vprX
Return type   vec40_t

              1    HHOP          uint8     9..16           Number of atomic operations

              2

Selects the VMSNX and VPSX set within
                   VMPSX         uint8     0,1
                                                           modv0/modv2 mode registers
              3    IN1_V32       vec_t                     Input vector operand

              4    IN1_OFST      uint8     0..7
                                                           Offset for the first DW used from operand
                                                           3

              5    IN1_PART      uint8     LOW,HIGH        Word part which is used for operand 3
              6    IN2_V32       vec_t                     Input vector operand

              7    IN2_OFST      uint8     0..7            Offset for the first DW used from operand
Operands                                                   6

              8    IN2_PART      uint8     LOW,HIGH        Word part which is used for operand 6
              9    IN3_V32       vec_t                     Input vector operand

              10   IN3_OFST      uint8     0..7            Offset for the first DW used from operand
                                                           9

              11   IN3_PART      uint8     LOW,HIGH        Word part which is used for operand 9
              12   IN4_V40       vec40_t                   Output vector operand
              13   RES2_V40      vec40_t                   Output vector result operand
              14   IN_VPR        vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec40_t vRes1;
C example     vec40_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vmsue_v32_v32_v32_v40_v40_vmpsX_p (16, 1, vIn, 0, LOW, vIn2, 0, LOW, vIn3, 0, LOW,
              vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vmsue_v32_v32_v32_v40_v40_vmpsX_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).


Main table → Multiplication → Multiply-Subtract → 16x16 with Exponent
