# Multiplication → Multiply → 16x16 and Pack into Two 16-bit Words

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Multiplication → Multiply → 16x16 and Pack into Two 16-bit Words

16x16 and Pack into Two 16-bit Words

16x16 and Pack into Two 16-bit Words
Performs multiplication and packing between two sources. Each source is 16-bit wide. Either the

16-bit msbs or 16-bit lsbs are taken from the products and packed into either 32-bit or 40-bit
destination determined by the vector register type.
Available Switches
               Number of atomic operations. An atomic operation is defined as pair of
Oop
               multiplications and packing them. 1op ≤ Oop ≤ 8op
hi             The high parts are packed into the destination operands.
low            The low parts are packed into the destination operands.
vmpsX          Selects the VMSNX and VPSX set within modv0 or modv2 mode registers.
Intrinsic Names
vmpyp16_v32_c32_v32_hi
vmpyp16_v32_c32_v32_hi_vmpsX
vmpyp16_v32_c32_v32_low
vmpyp16_v32_c32_v32_low_vmpsX
vmpyp16_v32_v32_v32_hi_const
vmpyp16_v32_v32_v32_hi_const_vmpsX
vmpyp16_v32_v32_v32_hi
vmpyp16_v32_v32_v32_hi_vmpsX
vmpyp16_v32_v32_v32_low_const
vmpyp16_v32_v32_v32_low_const_vmpsX
vmpyp16_v32_v32_v32_low
vmpyp16_v32_v32_v32_low_vmpsX
Instruction details in the instruction set specification
Intrinsic     vmpyp16_v32_c32_v32_hi[_p]
name
Spec syntax   vmpyp16 {Oop ,low|hi [,vmpsX]} vx[X]p, vcYp, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            2
Operands      4    IN1_PART       uint8     LOW,HIGH        Word part which is used for operand 2
              5    IN2_C32        coef_t                    Coefficient operand
              6    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 5
              7    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vmpyp16_v32_c32_v32_hi_p (8, vIn, 0, LOW, vcoefIn, LOW, vecPred);

                   IN_VPR last operand is relevant only for vmpyp16_v32_c32_v32_hi_p
Comments      1.
                   version.


Main table → Multiplication → Multiply → 16x16 and Pack into Two 16-bit Words
Intrinsic     vmpyp16_v32_c32_v32_hi_vmpsX[_p]
name
Spec syntax   vmpyp16 {Oop ,low|hi [,vmpsX]} vx[X]p, vcYp, vz[0], ?vprX

Return type   vec_t

1    OOP            uint8     1..8            Number of atomic operations
                                                            Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand

              4    IN1_OFST       uint8     0..7            Offset for the first DW used from operand
Operands                                                    3

              5    IN1_PART       uint8     LOW,HIGH        Word part which is used for operand 3
              6    IN2_C32        coef_t                    Coefficient operand
              7    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 6
              8    IN_VPR         vprex_t                   Vector predicate operand
C example     vec_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
              vprex_t vecPred;
              ...
              vRes = vmpyp16_v32_c32_v32_hi_vmpsX_p (8, 1, vIn, 0, LOW, vcoefIn, LOW, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmpyp16_v32_c32_v32_hi_vmpsX_p version.


Main table → Multiplication → Multiply → 16x16 and Pack into Two 16-bit Words
Intrinsic     vmpyp16_v32_c32_v32_low[_p]
name
Spec syntax   vmpyp16 {Oop ,low|hi [,vmpsX]} vx[X]p, vcYp, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8           Number of atomic operations
              2    IN1_V32        vec_t                    Input vector operand

              3    IN1_OFST       uint8     0..7
                                                           Offset for the first DW used from operand
                                                           2
Operands      4    IN1_PART       uint8     LOW,HIGH       Word part which is used for operand 2
              5    IN2_C32        coef_t                   Coefficient operand
              6    IN2_PART       uint8     LOW,HIGH       Word part which is used for operand 5
              7    IN_VPR         vprex_t                  Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vmpyp16_v32_c32_v32_low_p (8, vIn, 0, LOW, vcoefIn, LOW, vecPred);

IN_VPR last operand is relevant only for vmpyp16_v32_c32_v32_low_p
Comments      1.
                   version.


Main table → Multiplication → Multiply → 16x16 and Pack into Two 16-bit Words
Intrinsic     vmpyp16_v32_c32_v32_low_vmpsX[_p]
name
Spec syntax   vmpyp16 {Oop ,low|hi [,vmpsX]} vx[X]p, vcYp, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8           Number of atomic operations
                                                           Selects the VMSNX and VPSX set within
Operands      2    VMPSX          uint8     0,1
                                                           modv0/modv2 mode registers
              3    IN1_V32        vec_t                    Input vector operand
            4    IN1_OFST      uint8     0..7            Offset for the first DW used from operand
                                                         3

            5    IN1_PART      uint8     LOW,HIGH        Word part which is used for operand 3
            6    IN2_C32       coef_t                    Coefficient operand
            7    IN2_PART      uint8     LOW,HIGH        Word part which is used for operand 6
            8    IN_VPR        vprex_t                   Vector predicate operand
            vec_t vIn;
            vec_t vRes;
            coef_t vcoefIn;
C example   vprex_t vecPred;
            ...
            vRes = vmpyp16_v32_c32_v32_low_vmpsX_p (8, 1, vIn, 0, LOW, vcoefIn, LOW, vecPred);

                 IN_VPR last operand is relevant only for
Comments    1.
                 vmpyp16_v32_c32_v32_low_vmpsX_p version.


Main table → Multiplication → Multiply → 16x16 and Pack into Two 16-bit Words
Intrinsic     vmpyp16_v32_v32_v32_hi_const[_p]
name
Spec syntax   vmpyp16 {Oop ,low|hi [,const][,vmpsX]} vx[X]p, vy[Y]p, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            2

              4    IN1_PART       uint8     LOW,HIGH        Word part which is used for operand 2
Operands
              5    IN2_V32        vec_t                     Input vector operand

6    IN2_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            5

              7    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 5
              8    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmpyp16_v32_v32_v32_hi_const_p (8, vIn, 0, LOW, vIn2, 0, LOW, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmpyp16_v32_v32_v32_hi_const_p version.


Main table → Multiplication → Multiply → 16x16 and Pack into Two 16-bit Words
Intrinsic     vmpyp16_v32_v32_v32_hi_const_vmpsX[_p]
name
Spec syntax   vmpyp16 {Oop ,low|hi [,const][,vmpsX]} vx[X]p, vy[Y]p, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
                                                            Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand

Operands      4    IN1_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            3

              5    IN1_PART       uint8     LOW,HIGH        Word part which is used for operand 3
              6    IN2_V32        vec_t                     Input vector operand

              7    IN2_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            6
              8    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 6
              9    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmpyp16_v32_v32_v32_hi_const_vmpsX_p (8, 1, vIn, 0, LOW, vIn2, 0, LOW, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmpyp16_v32_v32_v32_hi_const_vmpsX_p version.


Main table → Multiplication → Multiply → 16x16 and Pack into Two 16-bit Words

Intrinsic     vmpyp16_v32_v32_v32_hi[_p]
name
Spec syntax   vmpyp16 {Oop ,low|hi [,const][,vmpsX]} vx[X]p, vy[Y]p, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            2

              4    IN1_PART       uint8     LOW,HIGH        Word part which is used for operand 2
Operands
              5    IN2_V32        vec_t                     Input vector operand

              6    IN2_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            5

              7    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 5
              8    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmpyp16_v32_v32_v32_hi_p (8, vIn, 0, LOW, vIn2, 0, LOW, vecPred);

                   IN_VPR last operand is relevant only for vmpyp16_v32_v32_v32_hi_p
Comments      1.
                   version.


Main table → Multiplication → Multiply → 16x16 and Pack into Two 16-bit Words
Intrinsic     vmpyp16_v32_v32_v32_hi_vmpsX[_p]
name
Spec syntax   vmpyp16 {Oop ,low|hi [,const][,vmpsX]} vx[X]p, vy[Y]p, vz[0], ?vprX

Return type   vec_t
              1    OOP            uint8     1..8           Number of atomic operations
                                                           Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                           modv0/modv2 mode registers
              3    IN1_V32        vec_t                    Input vector operand

              4    IN1_OFST       uint8     0..7
                                                           Offset for the first DW used from operand
                                                           3
Operands      5    IN1_PART       uint8     LOW,HIGH       Word part which is used for operand 3
              6    IN2_V32        vec_t                    Input vector operand

              7    IN2_OFST       uint8     0..7

Offset for the first DW used from operand
                                                           6

              8    IN2_PART       uint8     LOW,HIGH       Word part which is used for operand 6
              9    IN_VPR         vprex_t                  Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmpyp16_v32_v32_v32_hi_vmpsX_p (8, 1, vIn, 0, LOW, vIn2, 0, LOW, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmpyp16_v32_v32_v32_hi_vmpsX_p version.


Main table → Multiplication → Multiply → 16x16 and Pack into Two 16-bit Words
Intrinsic     vmpyp16_v32_v32_v32_low_const[_p]
name
Spec syntax   vmpyp16 {Oop ,low|hi [,const][,vmpsX]} vx[X]p, vy[Y]p, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8           Number of atomic operations
              2    IN1_V32        vec_t                    Input vector operand

              3    IN1_OFST       uint8     0..7
                                                           Offset for the first DW used from operand
                                                           2

              4    IN1_PART       uint8     LOW,HIGH       Word part which is used for operand 2
Operands
              5    IN2_V32        vec_t                    Input vector operand

              6    IN2_OFST       uint8     0..7
                                                           Offset for the first DW used from operand
                                                           5

              7    IN2_PART       uint8     LOW,HIGH       Word part which is used for operand 5
              8    IN_VPR         vprex_t                  Vector predicate operand
              vec_t vIn;
C example     vec_t vIn2;
              vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmpyp16_v32_v32_v32_low_const_p (8, vIn, 0, LOW, vIn2, 0, LOW, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmpyp16_v32_v32_v32_low_const_p version.


Main table → Multiplication → Multiply → 16x16 and Pack into Two 16-bit Words
Intrinsic     vmpyp16_v32_v32_v32_low_const_vmpsX[_p]
name
Spec syntax   vmpyp16 {Oop ,low|hi [,const][,vmpsX]} vx[X]p, vy[Y]p, vz[0], ?vprX

Return type   vec_t

1    OOP            uint8     1..8            Number of atomic operations
                                                            Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand

              4    IN1_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            3
Operands      5    IN1_PART       uint8     LOW,HIGH        Word part which is used for operand 3
              6    IN2_V32        vec_t                     Input vector operand

              7    IN2_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            6

              8    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 6
              9    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmpyp16_v32_v32_v32_low_const_vmpsX_p (8, 1, vIn, 0, LOW, vIn2, 0, LOW, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmpyp16_v32_v32_v32_low_const_vmpsX_p version.


Main table → Multiplication → Multiply → 16x16 and Pack into Two 16-bit Words
Intrinsic     vmpyp16_v32_v32_v32_low[_p]
name
Spec syntax   vmpyp16 {Oop ,low|hi [,const][,vmpsX]} vx[X]p, vy[Y]p, vz[0], ?vprX

Return type   vec_t

Operands      1    OOP            uint8     1..8            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            2

              4    IN1_PART       uint8     LOW,HIGH        Word part which is used for operand 2
              5    IN2_V32        vec_t                     Input vector operand

              6    IN2_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            5

7    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 5
              8    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmpyp16_v32_v32_v32_low_p (8, vIn, 0, LOW, vIn2, 0, LOW, vecPred);

                   IN_VPR last operand is relevant only for vmpyp16_v32_v32_v32_low_p
Comments      1.
                   version.


Main table → Multiplication → Multiply → 16x16 and Pack into Two 16-bit Words
Intrinsic     vmpyp16_v32_v32_v32_low_vmpsX[_p]
name
Spec syntax   vmpyp16 {Oop ,low|hi [,const][,vmpsX]} vx[X]p, vy[Y]p, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
                                                            Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand

              4    IN1_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            3
Operands      5    IN1_PART       uint8     LOW,HIGH        Word part which is used for operand 3
              6    IN2_V32        vec_t                     Input vector operand

              7    IN2_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            6

              8    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 6
              9    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
C example     vec_t vRes;
              vprex_t vecPred;
            ...
            vRes = vmpyp16_v32_v32_v32_low_vmpsX_p (8, 1, vIn, 0, LOW, vIn2, 0, LOW, vecPred);

                 IN_VPR last operand is relevant only for
Comments    1.
                 vmpyp16_v32_v32_v32_low_vmpsX_p version.


Main table → Multiplication → Multiply → 16x16 and Pack into Two 16-bit Words
