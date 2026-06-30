# Multiplication → Multiply and Subtract Two Products → 16x16 Multiply,

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Multiplication → Multiply and Subtract Two Products → 16x16 Multiply,
Subtract using Two Products and Accumulate

16x16 Multiply, Subtract using Two Products and Accumulate

16x16 Multiply, Subtract using Two Products and Accumulate
Performs multiply-addition-subtract using two products. Each source is 16-bit wide. The first
product is added to the 40-bit destination and the second product is subtracted from the 40-bit
destination.
Available Switches
              Number of atomic operations. An atomic operation is defined as a single multiply-
Hhop
              add-and-subtract-two-products operation. 9op ≤ Hhop ≤ 16op
              Number of atomic operations. An atomic operation is defined as a single multiply-
Oop
              add-and-subtract-two-products operation. 1op ≤ Oop ≤ 8op
              Consecutive indices. When used, the vx/vy indices are consecutive and not the
cn
              registers' parts.
const         When used, vy[Y]p/vy[V]p are constant throughout the operations.
vmpsX         Selects the VMSNX and VPSX set within modv0 or modv2 mode registers.
Intrinsic Names
vmas3_v32_v32_v40_v40_const
vmas3_v32_v32_v40_v40_const_vmpsX
vmas3_v32_v32_v40_cn
vmas3_v32_v32_v40_cn_vmpsX
vmas3_v32_v32_v40_const

vmas3_v32_v32_v40_const_vmpsX
vmas3_v32_v32_v40
vmas3_v32_v32_v40_vmpsX
vmas3_v32_c32_c32_v40_v40
vmas3_v32_c32_c32_v40_v40_vmpsX
vmas3_v32_c32_c32_v40
vmas3_v32_c32_c32_v40_vmpsX
Instruction details in the instruction set specification
Intrinsic     vmas3_v32_v32_v40_v40_const[_p]
name
Spec syntax   vmas3 {Hhop ,const [,vmpsX]} vx[X]p, vy[Y]p, vx[W]p, vy[V]p, voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    HHOP           uint8     9..16          Number of atomic operations
              2    IN1_V32        vec_t                    Input vector operand

              3    IN1_OFST       uint8     0..7
                                                           Offset for the first DW used from operand
                                                           2

              4    IN1_PART       uint8     LOW,HIGH       Word part which is used for operand 2
              5    IN2_V32        vec_t                    Input vector operand

              6    IN2_OFST       uint8     0..7           Offset for the first DW used from operand
                                                           5

              7    IN2_PART       uint8     LOW,HIGH       Word part which is used for operand 5
Operands
              8    IN3_OFST       uint8     0..7           Offset for the first DW used from operand
                                                           2

              9    IN3_PART       uint8     LOW,HIGH       Word part which is used for operand 2

              10   IN4_OFST       uint8     0..7           Offset for the first DW used from operand
                                                           5

              11   IN4_PART       uint8     LOW,HIGH       Word part which is used for operand 5
              12   IN5_V40        vec40_t                  Output vector operand
              13   RES2_V40       vec40_t                  Output vector result operand
              14   IN_VPR         vprex_t                  Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes1;
              vec40_t vRes2;
C example     vprex_t vecPred;
              ...
              vRes1 = vmas3_v32_v32_v40_v40_const_p (16, vIn, 0, LOW, vIn2, 0, LOW, 0, LOW, 0, LOW, vRes1,
              vRes2, vecPred);

                   IN_VPR last operand is relevant only for vmas3_v32_v32_v40_v40_const_p
              1.
                   version.

Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).


Main table → Multiplication → Multiply and Subtract Two Products → 16x16 Multiply,
Subtract using Two Products and Accumulate
Intrinsic     vmas3_v32_v32_v40_v40_const_vmpsX[_p]
name
Spec syntax   vmas3 {Hhop ,const [,vmpsX]} vx[X]p, vy[Y]p, vx[W]p, vy[V]p, voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    HHOP          uint8     9..16           Number of atomic operations
                                                           Selects the VMSNX and VPSX set within
              2    VMPSX         uint8     0,1
                                                           modv0/modv2 mode registers
              3    IN1_V32       vec_t                     Input vector operand

              4    IN1_OFST      uint8     0..7
                                                           Offset for the first DW used from operand
                                                           3

              5    IN1_PART      uint8     LOW,HIGH        Word part which is used for operand 3
              6    IN2_V32       vec_t                     Input vector operand

              7    IN2_OFST      uint8     0..7            Offset for the first DW used from operand
                                                           6
Operands      8    IN2_PART      uint8     LOW,HIGH        Word part which is used for operand 6

              9    IN3_OFST      uint8     0..7            Offset for the first DW used from operand
                                                           3

              10   IN3_PART      uint8     LOW,HIGH        Word part which is used for operand 3

              11   IN4_OFST      uint8     0..7            Offset for the first DW used from operand
                                                           6

              12   IN4_PART      uint8     LOW,HIGH        Word part which is used for operand 6
              13   IN5_V40       vec40_t                   Output vector operand
              14   RES2_V40      vec40_t                   Output vector result operand
              15   IN_VPR        vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes1;
              vec40_t vRes2;

C example     vprex_t vecPred;
              ...
              vRes1 = vmas3_v32_v32_v40_v40_const_vmpsX_p (16, 1, vIn, 0, LOW, vIn2, 0, LOW, 0, LOW, 0, LOW,
              vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vmas3_v32_v32_v40_v40_const_vmpsX_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).


Main table → Multiplication → Multiply and Subtract Two Products → 16x16 Multiply,
Subtract using Two Products and Accumulate
Intrinsic     vmas3_v32_v32_v40_cn[_p]
name
Spec syntax   vmas3 {Oop ,cn [,vmpsX]} vx[X]p, vy[Y]p, vx[W]p, vy[V]p, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            2

              4    IN1_PART       uint8     LOW,HIGH        Word part which is used for operand 2
              5    IN2_V32        vec_t                     Input vector operand

              6    IN2_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            5

Operands      7    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 5

              8    IN3_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            2

              9    IN3_PART       uint8     LOW,HIGH        Word part which is used for operand 2

              10   IN4_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            5

              11   IN4_PART       uint8     LOW,HIGH        Word part which is used for operand 5
              12   IN5_V40        vec40_t                   Output vector operand
              13   IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;

C example     vprex_t vecPred;
              ...
              vRes = vmas3_v32_v32_v40_cn_p (8, vIn, 0, LOW, vIn2, 0, LOW, 0, LOW, 0, LOW, vRes, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmas3_v32_v32_v40_cn_p version.


Main table → Multiplication → Multiply and Subtract Two Products → 16x16 Multiply,
Subtract using Two Products and Accumulate
Intrinsic     vmas3_v32_v32_v40_cn_vmpsX[_p]
name
Spec syntax   vmas3 {Oop ,cn [,vmpsX]} vx[X]p, vy[Y]p, vx[W]p, vy[V]p, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands                                                    Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
            3    IN1_V32       vec_t                     Input vector operand

            4    IN1_OFST      uint8     0..7            Offset for the first DW used from operand
                                                         3

            5    IN1_PART      uint8     LOW,HIGH        Word part which is used for operand 3
            6    IN2_V32       vec_t                     Input vector operand

            7    IN2_OFST      uint8     0..7
                                                         Offset for the first DW used from operand
                                                         6

            8    IN2_PART      uint8     LOW,HIGH        Word part which is used for operand 6

            9    IN3_OFST      uint8     0..7
                                                         Offset for the first DW used from operand
                                                         3

            10   IN3_PART      uint8     LOW,HIGH        Word part which is used for operand 3

            11   IN4_OFST      uint8     0..7
                                                         Offset for the first DW used from operand
                                                         6

            12   IN4_PART      uint8     LOW,HIGH        Word part which is used for operand 6
            13   IN5_V40       vec40_t                   Output vector operand
            14   IN_VPR        vprex_t                   Vector predicate operand
            vec_t vIn;
            vec_t vIn2;
            vec40_t vRes;
C example   vprex_t vecPred;
            ...

vRes = vmas3_v32_v32_v40_cn_vmpsX_p (8, 1, vIn, 0, LOW, vIn2, 0, LOW, 0, LOW, 0, LOW, vRes,
            vecPred);

                 IN_VPR last operand is relevant only for vmas3_v32_v32_v40_cn_vmpsX_p
Comments    1.
                 version.


Main table → Multiplication → Multiply and Subtract Two Products → 16x16 Multiply,
Subtract using Two Products and Accumulate
Intrinsic     vmas3_v32_v32_v40_const[_p]
name
Spec syntax   vmas3 {Oop [,const][,vmpsX]} vx[X]p, vy[Y]p, vx[W]p, vy[V]p, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            2

              4    IN1_PART       uint8     LOW,HIGH        Word part which is used for operand 2
              5    IN2_V32        vec_t                     Input vector operand

              6    IN2_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            5

Operands      7    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 5

              8    IN3_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            2

              9    IN3_PART       uint8     LOW,HIGH        Word part which is used for operand 2

              10   IN4_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            5

              11   IN4_PART       uint8     LOW,HIGH        Word part which is used for operand 5
              12   IN5_V40        vec40_t                   Output vector operand
              13   IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmas3_v32_v32_v40_const_p (8, vIn, 0, LOW, vIn2, 0, LOW, 0, LOW, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for vmas3_v32_v32_v40_const_p
Comments      1.
                   version.

Main table → Multiplication → Multiply and Subtract Two Products → 16x16 Multiply,
Subtract using Two Products and Accumulate
Intrinsic     vmas3_v32_v32_v40_const_vmpsX[_p]
name
Spec syntax   vmas3 {Oop [,const][,vmpsX]} vx[X]p, vy[Y]p, vx[W]p, vy[V]p, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands
              2    VMPSX          uint8     0,1             Selects the VMSNX and VPSX set within
                                                           modv0/modv2 mode registers
              3    IN1_V32        vec_t                    Input vector operand

              4    IN1_OFST       uint8     0..7           Offset for the first DW used from operand
                                                           3

              5    IN1_PART       uint8     LOW,HIGH       Word part which is used for operand 3
              6    IN2_V32        vec_t                    Input vector operand

              7    IN2_OFST       uint8     0..7
                                                           Offset for the first DW used from operand
                                                           6

              8    IN2_PART       uint8     LOW,HIGH       Word part which is used for operand 6

              9    IN3_OFST       uint8     0..7
                                                           Offset for the first DW used from operand
                                                           3

              10   IN3_PART       uint8     LOW,HIGH       Word part which is used for operand 3

              11   IN4_OFST       uint8     0..7
                                                           Offset for the first DW used from operand
                                                           6

              12   IN4_PART       uint8     LOW,HIGH       Word part which is used for operand 6
              13   IN5_V40        vec40_t                  Output vector operand
              14   IN_VPR         vprex_t                  Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmas3_v32_v32_v40_const_vmpsX_p (8, 1, vIn, 0, LOW, vIn2, 0, LOW, 0, LOW, 0, LOW, vRes,
              vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmas3_v32_v32_v40_const_vmpsX_p version.

Main table → Multiplication → Multiply and Subtract Two Products → 16x16 Multiply,
Subtract using Two Products and Accumulate
Intrinsic     vmas3_v32_v32_v40[_p]
name
Spec syntax   vmas3 {Oop [,const][,vmpsX]} vx[X]p, vy[Y]p, vx[W]p, vy[V]p, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8           Number of atomic operations
              2    IN1_V32        vec_t                    Input vector operand
Operands                                                   Offset for the first DW used from operand
              3    IN1_OFST       uint8     0..7
                                                           2

              4    IN1_PART       uint8     LOW,HIGH       Word part which is used for operand 2
              5    IN2_V32        vec_t                     Input vector operand

              6    IN2_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            5

              7    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 5

              8    IN3_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            2

              9    IN3_PART       uint8     LOW,HIGH        Word part which is used for operand 2

              10   IN4_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            5

              11   IN4_PART       uint8     LOW,HIGH        Word part which is used for operand 5
              12   IN5_V40        vec40_t                   Output vector operand
              13   IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmas3_v32_v32_v40_p (8, vIn, 0, LOW, vIn2, 0, LOW, 0, LOW, 0, LOW, vRes, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmas3_v32_v32_v40_p version.


Main table → Multiplication → Multiply and Subtract Two Products → 16x16 Multiply,
Subtract using Two Products and Accumulate
Intrinsic     vmas3_v32_v32_v40_vmpsX[_p]
name
Spec syntax   vmas3 {Oop [,const][,vmpsX]} vx[X]p, vy[Y]p, vx[W]p, vy[V]p, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8            Number of atomic operations

Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand

              4    IN1_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            3
Operands      5    IN1_PART       uint8     LOW,HIGH        Word part which is used for operand 3
              6    IN2_V32        vec_t                     Input vector operand

              7    IN2_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            6

              8    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 6
              9    IN3_OFST       uint8     0..7            Offset for the first DW used from operand
                                                         3

            10   IN3_PART      uint8     LOW,HIGH        Word part which is used for operand 3

            11   IN4_OFST      uint8     0..7            Offset for the first DW used from operand
                                                         6

            12   IN4_PART      uint8     LOW,HIGH        Word part which is used for operand 6
            13   IN5_V40       vec40_t                   Output vector operand
            14   IN_VPR        vprex_t                   Vector predicate operand
            vec_t vIn;
            vec_t vIn2;
            vec40_t vRes;
C example   vprex_t vecPred;
            ...
            vRes = vmas3_v32_v32_v40_vmpsX_p (8, 1, vIn, 0, LOW, vIn2, 0, LOW, 0, LOW, 0, LOW, vRes,
            vecPred);

                 IN_VPR last operand is relevant only for vmas3_v32_v32_v40_vmpsX_p
Comments    1.
                 version.


Main table → Multiplication → Multiply and Subtract Two Products → 16x16 Multiply,
Subtract using Two Products and Accumulate
Intrinsic     vmas3_v32_c32_c32_v40_v40[_p]
name
Spec syntax   vmas3 {Hhop [,vmpsX]} vx[X]p, vcYp, vx[W]p, vcVp, voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    HHOP          uint8     9..16           Number of atomic operations
              2    IN1_V32       vec_t                     Input vector operand

3    IN1_OFST      uint8     0..7
                                                           Offset for the first DW used from operand
                                                           2

              4    IN1_PART      uint8     LOW,HIGH        Word part which is used for operand 2
              5    IN2_C32       coef_t                    Coefficient operand
              6    IN2_PART      uint8     LOW,HIGH        Word part which is used for operand 5
Operands      7    IN3_OFST      uint8     0..7            Offset for the first DW used from operand
                                                           2

              8    IN3_PART      uint8     LOW,HIGH        Word part which is used for operand 2
              9    IN4_C32       vec_t                     Coefficient operand
              10   IN4_PART      uint8     LOW,HIGH        Word part which is used for operand 9
              11   IN5_V40       vec40_t                   Output vector operand
              12   RES2_V40      vec40_t                   Output vector result operand
              13   IN_VPR        vprex_t                   Vector predicate operand
              vec_t vIn;
              vec40_t vRes1;
              vec40_t vRes2;
              coef_t vcoefIn;
C example     vec_t vcoefIn2;
              vprex_t vecPred;
              ...
              vRes1 = vmas3_v32_c32_c32_v40_v40_p (16, vIn, 0, LOW, vcoefIn, LOW, 0, LOW, vcoefIn2, LOW,
              vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for vmas3_v32_c32_c32_v40_v40_p
              1.
                   version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).


Main table → Multiplication → Multiply and Subtract Two Products → 16x16 Multiply,
Subtract using Two Products and Accumulate
Intrinsic     vmas3_v32_c32_c32_v40_v40_vmpsX[_p]
name
Spec syntax   vmas3 {Hhop [,vmpsX]} vx[X]p, vcYp, vx[W]p, vcVp, voz1[0], voz2[0], ?vprX
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
              6    IN2_C32       coef_t                    Coefficient operand

Operands      7    IN2_PART      uint8     LOW,HIGH        Word part which is used for operand 6

              8    IN3_OFST      uint8     0..7            Offset for the first DW used from operand
                                                           3

              9    IN3_PART      uint8     LOW,HIGH        Word part which is used for operand 3
              10   IN4_C32       vec_t                     Coefficient operand
              11   IN4_PART      uint8     LOW,HIGH        Word part which is used for operand 10
              12   IN5_V40       vec40_t                   Output vector operand
              13   RES2_V40      vec40_t                   Output vector result operand
              14   IN_VPR        vprex_t                   Vector predicate operand
              vec_t vIn;
              vec40_t vRes1;
              vec40_t vRes2;
              coef_t vcoefIn;
C example     vec_t vcoefIn2;
              vprex_t vecPred;
              ...
              vRes1 = vmas3_v32_c32_c32_v40_v40_vmpsX_p (16, 1, vIn, 0, LOW, vcoefIn, LOW, 0, LOW, vcoefIn2,
              LOW, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vmas3_v32_c32_c32_v40_v40_vmpsX_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).


Main table → Multiplication → Multiply and Subtract Two Products → 16x16 Multiply,
Subtract using Two Products and Accumulate
Intrinsic     vmas3_v32_c32_c32_v40[_p]
name
Spec syntax   vmas3 {Oop [,vmpsX]} vx[X]p, vcYp, vx[W]p, vcVp, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

3    IN1_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            2

              4    IN1_PART       uint8     LOW,HIGH        Word part which is used for operand 2
              5    IN2_C32        coef_t                    Coefficient operand
              6    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 5
Operands
              7    IN3_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            2

              8    IN3_PART       uint8     LOW,HIGH        Word part which is used for operand 2
              9    IN4_C32        coef_t                    Coefficient operand
              10   IN4_PART       uint8     LOW,HIGH        Word part which is used for operand 9
              11   IN5_V40        vec40_t                   Output vector operand
              12   IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec40_t vRes;
              coef_t vcoefIn;
              coef_t vcoefIn2;
C example     vprex_t vecPred;
              ...
              vRes = vmas3_v32_c32_c32_v40_p (8, vIn, 0, LOW, vcoefIn, LOW, 0, LOW, vcoefIn2, LOW, vRes,
              vecPred);

                   IN_VPR last operand is relevant only for vmas3_v32_c32_c32_v40_p
Comments      1.
                   version.


Main table → Multiplication → Multiply and Subtract Two Products → 16x16 Multiply,
Subtract using Two Products and Accumulate
Intrinsic     vmas3_v32_c32_c32_v40_vmpsX[_p]
name
Spec syntax   vmas3 {Oop [,vmpsX]} vx[X]p, vcYp, vx[W]p, vcVp, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands                                                    Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
            3    IN1_V32       vec_t                     Input vector operand

            4    IN1_OFST      uint8     0..7            Offset for the first DW used from operand
                                                         3

            5    IN1_PART      uint8     LOW,HIGH        Word part which is used for operand 3

6    IN2_C32       coef_t                    Coefficient operand
            7    IN2_PART      uint8     LOW,HIGH        Word part which is used for operand 6

            8    IN3_OFST      uint8     0..7
                                                         Offset for the first DW used from operand
                                                         3

            9    IN3_PART      uint8     LOW,HIGH        Word part which is used for operand 3
            10   IN4_C32       coef_t                    Coefficient operand
            11   IN4_PART      uint8     LOW,HIGH        Word part which is used for operand 10
            12   IN5_V40       vec40_t                   Output vector operand
            13   IN_VPR        vprex_t                   Vector predicate operand
            vec_t vIn;
            vec40_t vRes;
            coef_t vcoefIn;
            coef_t vcoefIn2;
C example   vprex_t vecPred;
            ...
            vRes = vmas3_v32_c32_c32_v40_vmpsX_p (8, 1, vIn, 0, LOW, vcoefIn, LOW, 0, LOW, vcoefIn2, LOW,
            vRes, vecPred);

                 IN_VPR last operand is relevant only for
Comments    1.
                 vmas3_v32_c32_c32_v40_vmpsX_p version.


Main table → Multiplication → Multiply and Subtract Two Products → 16x16 Multiply,
Subtract using Two Products and Accumulate
