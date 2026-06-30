# Multiplication → Multiply-Accumulate → 16x16 MAC and Multiply

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Multiplication → Multiply-Accumulate → 16x16 MAC and Multiply

16x16 MAC and Multiply

16x16 MAC and Multiply
Performs two sets of operations: eight multiply-accumulate operations according to first
operands set and multiplication according to the second operands set. The sources are 16-bit

wide. Each set is written into different vector destinations. The eight multiply-accumulate
products are accumulated with eight 40-bit wide destinations respectively. The multiplication
product is placed into 40-bit destination.
Available Switches
     Number of atomic operations. The atomic operations are eight multiply-accumulate using
     the two first sources and multiplication using the next two sources. Writes to two vector
Hhop
     destinations, where the first vector destination is fully written, and the second vector
     destination is set according to Hhop switch.
const When used, vy[Y]p/vy[V]p are constant throughout the operations.
Intrinsic Names
vmacy_v32_v32_v40_v32_Hhop
vmacy_v32_v32_v40_v32_const_Hhop
vmacy_v32_v32_v40_Hhop
vmacy_v32_v32_v40_const_Hhop
vmacy_v32_c32_v32_c32_v40_Hhop
vmacy_v32_c32_v32_c32_v40_v32_Hhop
Instruction details in the instruction set specification
Intrinsic     vmacy_v32_v32_v40_v32_Hhop[_p]
name
Spec syntax   vmacy {Hhop [,const]} vx[X]p, vy[Y]p, vx[W]p, vy[V]p ,voz[0], vz[0], ?vprX

Return type   vec_t

              1    HHOP          uint8     9..16           Number of atomic operations
              2    IN1_V32       vec_t                     Input vector operand

              3    IN1_OFST      uint8     0..7
                                                           Offset for the first DW used from operand
                                                           2

              4    IN1_PART      uint8     LOW,HIGH        Word part which is used for operand 2
              5    IN2_V32       vec_t                     Input vector operand

              6    IN2_OFST      uint8     0..7            Offset for the first DW used from operand
                                                           5

              7    IN2_PART      uint8     LOW,HIGH        Word part which is used for operand 5
Operands
              8    IN3_OFST      uint8     0..7            Offset for the first DW used from operand
                                                           2

              9    IN3_PART      uint8     LOW,HIGH        Word part which is used for operand 2

              10   IN4_OFST      uint8     0..7            Offset for the first DW used from operand
                                                           5

              11   IN4_PART      uint8     LOW,HIGH        Word part which is used for operand 5
              12   IN5_V40       vec40_t                   Output vector operand

13   RES2_V32      vec_t                     Input vector result operand
              14   IN_VPR        vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes1;
              vec_t vRes2;
C example     vprex_t vecPred;
              ...
              vRes1 = vmacy_v32_v32_v40_v32_Hhop_p (16, vIn, 0, LOW, vIn2, 0, LOW, 0, LOW, 0, LOW, vRes1,
              vRes2, vecPred);

                   IN_VPR last operand is relevant only for vmacy_v32_v32_v40_v32_Hhop_p
              1.
                   version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Multiplication → Multiply-Accumulate → 16x16 MAC and Multiply
Intrinsic     vmacy_v32_v32_v40_v32_const_Hhop[_p]
name
Spec syntax   vmacy {Hhop [,const]} vx[X]p, vy[Y]p, vx[W]p, vy[V]p ,voz[0], vz[0], ?vprX

Return type   vec_t

              1    HHOP          uint8     9..16          Number of atomic operations
              2    IN1_V32       vec_t                    Input vector operand

              3    IN1_OFST      uint8     0..7
                                                          Offset for the first DW used from operand
                                                          2

              4    IN1_PART      uint8     LOW,HIGH       Word part which is used for operand 2
              5    IN2_V32       vec_t                    Input vector operand

              6    IN2_OFST      uint8     0..7           Offset for the first DW used from operand
                                                          5

              7    IN2_PART      uint8     LOW,HIGH       Word part which is used for operand 5
Operands
              8    IN3_OFST      uint8     0..7           Offset for the first DW used from operand
                                                          2

              9    IN3_PART      uint8     LOW,HIGH       Word part which is used for operand 2

              10   IN4_OFST      uint8     0..7           Offset for the first DW used from operand
                                                          5

              11   IN4_PART      uint8     LOW,HIGH       Word part which is used for operand 5
              12   IN5_V40       vec40_t                  Output vector operand

13   RES2_V32      vec_t                    Input vector result operand
              14   IN_VPR        vprex_t                  Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes1;
              vec_t vRes2;
C example     vprex_t vecPred;
              ...
              vRes1 = vmacy_v32_v32_v40_v32_const_Hhop_p (16, vIn, 0, LOW, vIn2, 0, LOW, 0, LOW, 0, LOW,
              vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vmacy_v32_v32_v40_v32_const_Hhop_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Multiplication → Multiply-Accumulate → 16x16 MAC and Multiply
Intrinsic   vmacy_v32_v32_v40_Hhop[_p]
name
Spec        vmacy {Hhop [,const]} vx[X]p, vy[Y]p, vx[W]p, vy[V]p ,vou[0], ?vprX
syntax
Return      vec40_t
type
            1    HHOP                uint8     9..16        Number of atomic operations
            2    IN1_V32             vec_t                  Input vector operand
                                                            Offset for the first DW used from
            3    IN1_OFST            uint8     0..7
                                                            operand 2
            4    IN1_PART            uint8     LOW,HIGH     Word part which is used for operand 2
            5    IN2_V32             vec_t                  Input vector operand
                                                            Offset for the first DW used from
            6    IN2_OFST            uint8     0..7
                                                            operand 5
            7    IN2_PART            uint8     LOW,HIGH     Word part which is used for operand 5
Operands
                                                            Offset for the first DW used from
            8    IN3_OFST            uint8     0..7
                                                            operand 2
            9    IN3_PART            uint8     LOW,HIGH     Word part which is used for operand 2
                                                            Offset for the first DW used from
            10 IN4_OFST              uint8     0..7
                                                            operand 5

11 IN4_PART              uint8     LOW,HIGH     Word part which is used for operand 5
            12 IN5_V40               vec40_t                Output vector operand
            13 IMPLIED_RES_V40 vec40_t                      Output vector result operand
            14 IN_VPR                vprex_t                Vector predicate operand
            vec_t vIn;
            vec_t vIn2;
            vec40_t vRes1;
            vec40_t vRes2;
C example   vprex_t vecPred;
            vec40_t vo0;
            ...
            vRes2 = vmacy_v32_v32_v40_Hhop_p (16, vIn, 0, LOW, vIn2, 0, LOW, 0, LOW, 0, LOW, vRes1, vo0,
            vecPred);

                 IN_VPR last operand is relevant only for vmacy_v32_v32_v40_Hhop_p
Comments    1.
                 version.


Main table → Multiplication → Multiply-Accumulate → 16x16 MAC and Multiply
Intrinsic   vmacy_v32_v32_v40_const_Hhop[_p]
name
Spec        vmacy {Hhop [,const]} vx[X]p, vy[Y]p, vx[W]p, vy[V]p ,vou[0], ?vprX
syntax
Return      vec40_t
type
            1    HHOP                uint8     9..16        Number of atomic operations
            2    IN1_V32             vec_t                  Input vector operand
                                                            Offset for the first DW used from
            3    IN1_OFST            uint8     0..7
                                                            operand 2
            4    IN1_PART            uint8     LOW,HIGH     Word part which is used for operand 2
            5    IN2_V32             vec_t                  Input vector operand
                                                            Offset for the first DW used from
            6    IN2_OFST            uint8     0..7
                                                            operand 5
            7    IN2_PART            uint8     LOW,HIGH     Word part which is used for operand 5
Operands
                                                            Offset for the first DW used from
            8    IN3_OFST            uint8     0..7
                                                            operand 2
            9    IN3_PART            uint8     LOW,HIGH     Word part which is used for operand 2
                                                            Offset for the first DW used from
            10 IN4_OFST              uint8     0..7
                                                            operand 5

11 IN4_PART              uint8     LOW,HIGH     Word part which is used for operand 5
            12 IN5_V40               vec40_t                Output vector operand
            13 IMPLIED_RES_V40 vec40_t                      Output vector result operand
            14 IN_VPR                vprex_t                Vector predicate operand
            vec_t vIn;
            vec_t vIn2;
            vec40_t vRes1;
            vec40_t vRes2;
C example   vprex_t vecPred;
            vec40_t vo0;
            ...
            vRes2 = vmacy_v32_v32_v40_const_Hhop_p (16, vIn, 0, LOW, vIn2, 0, LOW, 0, LOW, 0, LOW, vRes1,
            vo0, vecPred);

                 IN_VPR last operand is relevant only for vmacy_v32_v32_v40_const_Hhop_p
Comments    1.
                 version.


Main table → Multiplication → Multiply-Accumulate → 16x16 MAC and Multiply
Intrinsic   vmacy_v32_c32_v32_c32_v40_Hhop[_p]
name
Spec        vmacy {Hhop} vx[X]p, vcYp, vw[W]p, vcVp ,vou[0], ?vprX
syntax
Return      vec40_t
type
            1    HHOP                uint8     9..16        Number of atomic operations
            2    IN1_V32             vec_t                  Input vector operand
                                                            Offset for the first DW used from
            3    IN1_OFST            uint8     0..7
                                                            operand 2
            4    IN1_PART            uint8     LOW,HIGH     Word part which is used for operand 2
            5    IN2_C32             coef_t                 Coefficient operand
            6    IN2_PART            uint8     LOW,HIGH     Word part which is used for operand 5
            7    IN3_V32             vec_t                  Input vector operand
Operands
                                                            Offset for the first DW used from
            8    IN3_OFST            uint8     0..7
                                                            operand 7
            9    IN3_PART            uint8     LOW,HIGH     Word part which is used for operand 7
            10 IN4_C32               coef_t                 Coefficient operand
            11 IN4_PART              uint8     LOW,HIGH     Word part which is used for operand 10
            12 IN5_V40               vec40_t                Output vector operand
            13 IMPLIED_RES_V40 vec40_t                      Output vector result operand

14 IN_VPR                vprex_t                Vector predicate operand
            vec_t vIn;
            vec_t vIn2;
            vec40_t vRes1;
            vec40_t vRes2;
            coef_t vcoefIn;
C example   coef_t vcoefIn2;
            vprex_t vecPred;
            vec40_t vo0;
            ...
            vRes2 = vmacy_v32_c32_v32_c32_v40_Hhop_p (16, vIn, 0, LOW, vcoefIn, LOW, vIn2, 0, LOW, vcoefIn2,
            LOW, vRes1, vo0, vecPred);

                 IN_VPR last operand is relevant only for
Comments    1.
                 vmacy_v32_c32_v32_c32_v40_Hhop_p version.


Main table → Multiplication → Multiply-Accumulate → 16x16 MAC and Multiply
Intrinsic     vmacy_v32_c32_v32_c32_v40_v32_Hhop[_p]
name
Spec syntax   vmacy {Hhop} vx[X]p, vcYp, vw[W]p, vcVp, voz[0], vz[0], ?vprX

Return type   vec_t

              1    HHOP          uint8     9..16          Number of atomic operations
              2    IN1_V32       vec_t                    Input vector operand

              3    IN1_OFST      uint8     0..7
                                                          Offset for the first DW used from operand
                                                          2

              4    IN1_PART      uint8     LOW,HIGH       Word part which is used for operand 2
              5    IN2_C32       coef_t                   Coefficient operand
              6    IN2_PART      uint8     LOW,HIGH       Word part which is used for operand 5
              7    IN3_V32       vec_t                    Input vector operand
Operands
              8    IN3_OFST      uint8     0..7           Offset for the first DW used from operand
                                                          7

              9    IN3_PART      uint8     LOW,HIGH       Word part which is used for operand 7
              10   IN4_C32       coef_t                   Coefficient operand
              11   IN4_PART      uint8     LOW,HIGH       Word part which is used for operand 10
              12   IN5_V40       vec40_t                  Output vector operand
              13   RES2_V32      vec_t                    Input vector result operand
              14   IN_VPR        vprex_t                  Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes1;
              vec_t vRes2;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              vprex_t vecPred;
              ...

vRes1 = vmacy_v32_c32_v32_c32_v40_v32_Hhop_p (16, vIn, 0, LOW, vcoefIn, LOW, vIn2, 0, LOW,
              vcoefIn2, LOW, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vmacy_v32_c32_v32_c32_v40_v32_Hhop_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Multiplication → Multiply-Accumulate → 16x16 MAC and Multiply
