# Multiplication → Multiply and Subtract Two Products → 16x16 Multiply

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Multiplication → Multiply and Subtract Two Products → 16x16 Multiply
and Subtract Two Products

16x16 Multiply and Subtract Two Products

16x16 Multiply and Subtract Two Products
Performs multiplication and subtraction between two products. Each source is 16-bit wide. The
result is placed into 40-bit destination.
Available Switches
           Number of atomic operations. An atomic operation is defined as a single add-and-
Hhop
           subtract-two-products operation. 9op ≤ Hhop ≤ 16op
           Number of atomic operations. An atomic operation is defined as a single add-and-
Oop
           subtract-two-products operation. 1op ≤ Oop ≤ 8op
           Consecutive indices. When used, the vx/vy indices are consecutive and not the registers'
cn
           parts.
const      When used, vy[Y]p/vy[V]p are constant throughout the operations.
vmpsX Selects the VMSNX and VPSX set within modv0 or modv2 mode registers.
Intrinsic Names
vmas_v32_v32_v32_v32_const
vmas_v32_v32_v32_v32_const_vmpsX
vmas_v32_v32_v32_cn
vmas_v32_v32_v32_cn_vmpsX
vmas_v32_c32_c32_v32_v32
vmas_v32_c32_c32_v32_v32_vmpsX
vmas_v32_v32_v32_const
vmas_v32_v32_v32_const_vmpsX
vmas_v32_v32_v32
vmas_v32_v32_v32_vmpsX
vmas_v32_c32_c32_v32
vmas_v32_c32_c32_v32_vmpsX
Instruction details in the instruction set specification
Intrinsic     vmas_v32_v32_v32_v32_const[_p]
name
Spec syntax   vmas {Hhop ,const [,vmpsX]} vx[X]p, vy[Y]p, vx[W]p, vy[V]p, vz1[0], vz2[0], ?vprX

Return type   vec_t

              1    HHOP           uint8     9..16          Number of atomic operations
              2    IN1_V32        vec_t                    Input vector operand

              3    IN1_OFST       uint8     0..7
                                                           Offset for the first DW used from operand
                                                           2

              4    IN1_PART       uint8     LOW,HIGH       Word part which is used for operand 2
              5    IN2_V32        vec_t                    Input vector operand

6    IN2_OFST       uint8     0..7           Offset for the first DW used from operand
                                                           5

Operands      7    IN2_PART       uint8     LOW,HIGH       Word part which is used for operand 5

              8    IN3_OFST       uint8     0..7           Offset for the first DW used from operand
                                                           2

              9    IN3_PART       uint8     LOW,HIGH       Word part which is used for operand 2

              10   IN4_OFST       uint8     0..7           Offset for the first DW used from operand
                                                           5

              11   IN4_PART       uint8     LOW,HIGH       Word part which is used for operand 5
              12   RES2_V32       vec_t                    Input vector result operand
              13   IN_VPR         vprex_t                  Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes1;
              vec_t vRes2;
C example     vprex_t vecPred;
              ...
              vRes1 = vmas_v32_v32_v32_v32_const_p (16, vIn, 0, LOW, vIn2, 0, LOW, 0, LOW, 0, LOW, vRes2,
              vecPred);

                   IN_VPR last operand is relevant only for vmas_v32_v32_v32_v32_const_p
              1.
                   version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Multiplication → Multiply and Subtract Two Products → 16x16 Multiply
and Subtract Two Products
Intrinsic     vmas_v32_v32_v32_v32_const_vmpsX[_p]
name
Spec syntax   vmas {Hhop ,const [,vmpsX]} vx[X]p, vy[Y]p, vx[W]p, vy[V]p, vz1[0], vz2[0], ?vprX

Return type   vec_t

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
Operands                                                   6

              8    IN2_PART      uint8     LOW,HIGH        Word part which is used for operand 6

              9    IN3_OFST      uint8     0..7            Offset for the first DW used from operand
                                                           3

              10   IN3_PART      uint8     LOW,HIGH        Word part which is used for operand 3

              11   IN4_OFST      uint8     0..7            Offset for the first DW used from operand
                                                           6

              12   IN4_PART      uint8     LOW,HIGH        Word part which is used for operand 6
              13   RES2_V32      vec_t                     Input vector result operand
              14   IN_VPR        vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes1;
              vec_t vRes2;
C example     vprex_t vecPred;
              ...
              vRes1 = vmas_v32_v32_v32_v32_const_vmpsX_p (16, 1, vIn, 0, LOW, vIn2, 0, LOW, 0, LOW, 0, LOW,
              vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vmas_v32_v32_v32_v32_const_vmpsX_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Multiplication → Multiply and Subtract Two Products → 16x16 Multiply
and Subtract Two Products
Intrinsic     vmas_v32_v32_v32_cn[_p]
name
Spec syntax   vmas {Oop ,cn [,vmpsX]} vx[X]p, vy[Y]p, vx[W]p, vy[V]p, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            2

4    IN1_PART       uint8     LOW,HIGH        Word part which is used for operand 2
              5    IN2_V32        vec_t                     Input vector operand

              6    IN2_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            5
Operands
              7    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 5

              8    IN3_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            2

              9    IN3_PART       uint8     LOW,HIGH        Word part which is used for operand 2

              10   IN4_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            5

              11   IN4_PART       uint8     LOW,HIGH        Word part which is used for operand 5
              12   IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmas_v32_v32_v32_cn_p (8, vIn, 0, LOW, vIn2, 0, LOW, 0, LOW, 0, LOW, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmas_v32_v32_v32_cn_p version.


Main table → Multiplication → Multiply and Subtract Two Products → 16x16 Multiply
and Subtract Two Products
Intrinsic     vmas_v32_v32_v32_cn_vmpsX[_p]
name
Spec syntax   vmas {Oop ,cn [,vmpsX]} vx[X]p, vy[Y]p, vx[W]p, vy[V]p, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
                                                            Selects the VMSNX and VPSX set within
Operands      2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand
            4    IN1_OFST       uint8     0..7           Offset for the first DW used from operand
                                                         3

            5    IN1_PART       uint8     LOW,HIGH       Word part which is used for operand 3
            6    IN2_V32        vec_t                    Input vector operand

            7    IN2_OFST       uint8     0..7           Offset for the first DW used from operand

6

            8    IN2_PART       uint8     LOW,HIGH       Word part which is used for operand 6

            9    IN3_OFST       uint8     0..7           Offset for the first DW used from operand
                                                         3

            10   IN3_PART       uint8     LOW,HIGH       Word part which is used for operand 3

            11   IN4_OFST       uint8     0..7
                                                         Offset for the first DW used from operand
                                                         6

            12   IN4_PART       uint8     LOW,HIGH       Word part which is used for operand 6
            13   IN_VPR         vprex_t                  Vector predicate operand
            vec_t vIn;
            vec_t vIn2;
            vec_t vRes;
C example   vprex_t vecPred;
            ...
            vRes = vmas_v32_v32_v32_cn_vmpsX_p (8, 1, vIn, 0, LOW, vIn2, 0, LOW, 0, LOW, 0, LOW, vecPred);

                 IN_VPR last operand is relevant only for vmas_v32_v32_v32_cn_vmpsX_p
Comments    1.
                 version.


Main table → Multiplication → Multiply and Subtract Two Products → 16x16 Multiply
and Subtract Two Products
Intrinsic     vmas_v32_c32_c32_v32_v32[_p]
name
Spec syntax   vmas {Hhop [,vmpsX]} vx[X]p, vcYp, vx[W]p, vcVp, vz1[0], vz2[0], ?vprX

Return type   vec_t

              1    HHOP          uint8     9..16           Number of atomic operations
              2    IN1_V32       vec_t                     Input vector operand

              3    IN1_OFST      uint8     0..7
                                                           Offset for the first DW used from operand
                                                           2

              4    IN1_PART      uint8     LOW,HIGH        Word part which is used for operand 2
              5    IN2_C32       coef_t                    Coefficient operand
              6    IN2_PART      uint8     LOW,HIGH        Word part which is used for operand 5
Operands
              7    IN3_OFST      uint8     0..7            Offset for the first DW used from operand
                                                           2

              8    IN3_PART      uint8     LOW,HIGH        Word part which is used for operand 2
              9    IN4_C32       vec_t                     Coefficient operand
              10   IN4_PART      uint8     LOW,HIGH        Word part which is used for operand 9

11   RES2_V32      vec_t                     Input vector result operand
              12   IN_VPR        vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes1;
              vec_t vRes2;
              coef_t vcoefIn;
C example     vec_t vcoefIn2;
              vprex_t vecPred;
              ...
              vRes1 = vmas_v32_c32_c32_v32_v32_p (16, vIn, 0, LOW, vcoefIn, LOW, 0, LOW, vcoefIn2, LOW,
              vRes2, vecPred);

                   IN_VPR last operand is relevant only for vmas_v32_c32_c32_v32_v32_p
              1.
                   version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Multiplication → Multiply and Subtract Two Products → 16x16 Multiply
and Subtract Two Products
Intrinsic     vmas_v32_c32_c32_v32_v32_vmpsX[_p]
name
Spec syntax   vmas {Hhop [,vmpsX]} vx[X]p, vcYp, vx[W]p, vcVp, vz1[0], vz2[0], ?vprX

Return type   vec_t
            1    HHOP           uint8     9..16          Number of atomic operations
                                                         Selects the VMSNX and VPSX set within
            2    VMPSX          uint8     0,1
                                                         modv0/modv2 mode registers
            3    IN1_V32        vec_t                    Input vector operand

            4    IN1_OFST       uint8     0..7
                                                         Offset for the first DW used from operand
                                                         3

            5    IN1_PART       uint8     LOW,HIGH       Word part which is used for operand 3
            6    IN2_C32        coef_t                   Coefficient operand
Operands    7    IN2_PART       uint8     LOW,HIGH       Word part which is used for operand 6

            8    IN3_OFST       uint8     0..7           Offset for the first DW used from operand
                                                         3

            9    IN3_PART       uint8     LOW,HIGH       Word part which is used for operand 3
            10   IN4_C32        vec_t                    Coefficient operand
            11   IN4_PART       uint8     LOW,HIGH       Word part which is used for operand 10

12   RES2_V32       vec_t                    Input vector result operand
            13   IN_VPR         vprex_t                  Vector predicate operand
            vec_t vIn;
            vec_t vRes1;
            vec_t vRes2;
            coef_t vcoefIn;
C example   vec_t vcoefIn2;
            vprex_t vecPred;
            ...
            vRes1 = vmas_v32_c32_c32_v32_v32_vmpsX_p (16, 1, vIn, 0, LOW, vcoefIn, LOW, 0, LOW, vcoefIn2,
            LOW, vRes2, vecPred);

                 IN_VPR last operand is relevant only for
            1.
                 vmas_v32_c32_c32_v32_v32_vmpsX_p version.
Comments         This intrinsic returns two results. The first result variable should be placed to
            2.   the left of the = sign (lvalue). The second result variable should be passed as
                 an additional parameter (RES2_V32).


Main table → Multiplication → Multiply and Subtract Two Products → 16x16 Multiply
and Subtract Two Products
Intrinsic     vmas_v32_v32_v32_const[_p]
name
Spec syntax   vmas {Oop [,const] [,vmpsX]} vx[X]p, vy[Y]p, vx[W]p, vy[V]p, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            2

              4    IN1_PART       uint8     LOW,HIGH        Word part which is used for operand 2
              5    IN2_V32        vec_t                     Input vector operand

              6    IN2_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            5
Operands
              7    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 5

              8    IN3_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            2

              9    IN3_PART       uint8     LOW,HIGH        Word part which is used for operand 2

              10   IN4_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            5

              11   IN4_PART       uint8     LOW,HIGH        Word part which is used for operand 5

12   IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmas_v32_v32_v32_const_p (8, vIn, 0, LOW, vIn2, 0, LOW, 0, LOW, 0, LOW, vecPred);

                   IN_VPR last operand is relevant only for vmas_v32_v32_v32_const_p
Comments      1.
                   version.


Main table → Multiplication → Multiply and Subtract Two Products → 16x16 Multiply
and Subtract Two Products
Intrinsic     vmas_v32_v32_v32_const_vmpsX[_p]
name
Spec syntax   vmas {Oop [,const] [,vmpsX]} vx[X]p, vy[Y]p, vx[W]p, vy[V]p, vz[0], ?vprX

Return type   vec_t

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
              13   IN_VPR        vprex_t                   Vector predicate operand
              vec_t vIn;

vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmas_v32_v32_v32_const_vmpsX_p (8, 1, vIn, 0, LOW, vIn2, 0, LOW, 0, LOW, 0, LOW,
              vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmas_v32_v32_v32_const_vmpsX_p version.


Main table → Multiplication → Multiply and Subtract Two Products → 16x16 Multiply
and Subtract Two Products
Intrinsic     vmas_v32_v32_v32[_p]
name
Spec syntax   vmas {Oop [,const] [,vmpsX]} vx[X]p, vy[Y]p, vx[W]p, vy[V]p, vz[0], ?vprX

Return type   vec_t

              1    OOP           uint8     1..8            Number of atomic operations
              2    IN1_V32       vec_t                     Input vector operand

              3    IN1_OFST      uint8     0..7            Offset for the first DW used from operand
                                                           2
Operands
              4    IN1_PART      uint8     LOW,HIGH        Word part which is used for operand 2
              5    IN2_V32       vec_t                     Input vector operand

              6    IN2_OFST      uint8     0..7
                                                           Offset for the first DW used from operand
                                                           5
              7    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 5

              8    IN3_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            2

              9    IN3_PART       uint8     LOW,HIGH        Word part which is used for operand 2

              10   IN4_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            5

              11   IN4_PART       uint8     LOW,HIGH        Word part which is used for operand 5
              12   IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmas_v32_v32_v32_p (8, vIn, 0, LOW, vIn2, 0, LOW, 0, LOW, 0, LOW, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmas_v32_v32_v32_p version.


Main table → Multiplication → Multiply and Subtract Two Products → 16x16 Multiply
and Subtract Two Products

Intrinsic     vmas_v32_v32_v32_vmpsX[_p]
name
Spec syntax   vmas {Oop [,const] [,vmpsX]} vx[X]p, vy[Y]p, vx[W]p, vy[V]p, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
                                                            Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand

              4    IN1_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            3

              5    IN1_PART       uint8     LOW,HIGH        Word part which is used for operand 3

Operands      6    IN2_V32        vec_t                     Input vector operand

              7    IN2_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            6

              8    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 6

              9    IN3_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            3

              10   IN3_PART       uint8     LOW,HIGH        Word part which is used for operand 3

              11   IN4_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            6
            12   IN4_PART       uint8     LOW,HIGH       Word part which is used for operand 6
            13   IN_VPR         vprex_t                  Vector predicate operand
            vec_t vIn;
            vec_t vIn2;
            vec_t vRes;
C example   vprex_t vecPred;
            ...
            vRes = vmas_v32_v32_v32_vmpsX_p (8, 1, vIn, 0, LOW, vIn2, 0, LOW, 0, LOW, 0, LOW, vecPred);

                 IN_VPR last operand is relevant only for vmas_v32_v32_v32_vmpsX_p
Comments    1.
                 version.


Main table → Multiplication → Multiply and Subtract Two Products → 16x16 Multiply
and Subtract Two Products
Intrinsic     vmas_v32_c32_c32_v32[_p]
name
Spec syntax   vmas {Oop [,vmpsX]} vx[X]p, vcYp, vx[W]p, vcVp, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            2

              4    IN1_PART       uint8     LOW,HIGH        Word part which is used for operand 2
              5    IN2_C32        coef_t                    Coefficient operand
Operands      6    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 5

              7    IN3_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            2

              8    IN3_PART       uint8     LOW,HIGH        Word part which is used for operand 2
              9    IN4_C32        coef_t                    Coefficient operand
              10   IN4_PART       uint8     LOW,HIGH        Word part which is used for operand 9
              11   IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              vprex_t vecPred;
              ...
              vRes = vmas_v32_c32_c32_v32_p (8, vIn, 0, LOW, vcoefIn, LOW, 0, LOW, vcoefIn2, LOW, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmas_v32_c32_c32_v32_p version.


Main table → Multiplication → Multiply and Subtract Two Products → 16x16 Multiply
and Subtract Two Products
Intrinsic     vmas_v32_c32_c32_v32_vmpsX[_p]
name
Spec syntax   vmas {Oop [,vmpsX]} vx[X]p, vcYp, vx[W]p, vcVp, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
                                                            Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
Operands
              3    IN1_V32        vec_t                     Input vector operand

              4    IN1_OFST       uint8     0..7            Offset for the first DW used from operand
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
            12   IN_VPR        vprex_t                   Vector predicate operand
            vec_t vIn;
            vec_t vRes;
            coef_t vcoefIn;
            coef_t vcoefIn2;
C example   vprex_t vecPred;
            ...
            vRes = vmas_v32_c32_c32_v32_vmpsX_p (8, 1, vIn, 0, LOW, vcoefIn, LOW, 0, LOW, vcoefIn2, LOW,
            vecPred);

                 IN_VPR last operand is relevant only for vmas_v32_c32_c32_v32_vmpsX_p
Comments    1.
                 version.


Main table → Multiplication → Multiply and Subtract Two Products → 16x16 Multiply
and Subtract Two Products
