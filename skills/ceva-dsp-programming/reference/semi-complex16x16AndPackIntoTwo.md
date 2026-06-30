# Multiplication → Multiply → Semi-Complex 16x16 and Pack into Two

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Multiplication → Multiply → Semi-Complex 16x16 and Pack into Two
Words

Semi-Complex 16x16 and Pack into Two Words

Semi-Complex 16x16 and Pack into Two Words
Performs two complex by real multiplication between a complex number and a real 16-bit
number. The complex source consists of real 16-bit part and imaginary 16-bit part. Each product
is placed into either real or image destination respecitvely and packed into either 32-bit or 40-bit
destination determined by the vector register type.
Available Switches
                  Number of atomic operations. An atomic operation is defined as two
Oop
                  multiplications. 1op ≤ Oop ≤ 8op
conj              Performs complex multiply using complex conjugate of vx[X]
const             When used, vy[Y]p is constant throughout the operations.
pneg              When used, the product is negated
vmpsX             Selects the VMSNX and VPSX set within modv0 or modv2 mode registers.
Intrinsic Names

vmpyxrp_v32_c32_v32_conj
vmpyxrp_v32_c32_v32_conj_pneg
vmpyxrp_v32_c32_v32_conj_pneg_vmpsX
vmpyxrp_v32_c32_v32_conj_vmpsX
vmpyxrp_v32_c32_v32
vmpyxrp_v32_c32_v32_pneg
vmpyxrp_v32_c32_v32_pneg_vmpsX
vmpyxrp_v32_c32_v32_vmpsX
vmpyxrp_v32_v32_v32_conj
vmpyxrp_v32_v32_v32_conj_pneg
vmpyxrp_v32_v32_v32_conj_pneg_vmpsX
vmpyxrp_v32_v32_v32_conj_vmpsX
vmpyxrp_v32_v32_v32_const_conj
vmpyxrp_v32_v32_v32_const_conj_pneg
vmpyxrp_v32_v32_v32_const_conj_pneg_vmpsX
vmpyxrp_v32_v32_v32_const_conj_vmpsX
vmpyxrp_v32_v32_v32_const
vmpyxrp_v32_v32_v32_const_pneg
vmpyxrp_v32_v32_v32_const_pneg_vmpsX
vmpyxrp_v32_v32_v32_const_vmpsX
vmpyxrp_v32_v32_v32
vmpyxrp_v32_v32_v32_pneg
vmpyxrp_v32_v32_v32_pneg_vmpsX
vmpyxrp_v32_v32_v32_vmpsX
Instruction details in the instruction set specification
Intrinsic     vmpyxrp_v32_c32_v32_conj[_p]
name
Spec syntax   vmpyxrp {Oop [,conj] [,pneg][,vmpsX]} vx[X], vcYp, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            2
Operands
              4    IN2_C32        coef_t                    Coefficient operand
              5    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 4
              6    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vmpyxrp_v32_c32_v32_conj_p (8, vIn, 0, vcoefIn, LOW, vecPred);

                   IN_VPR last operand is relevant only for vmpyxrp_v32_c32_v32_conj_p
Comments      1.
                   version.


Main table → Multiplication → Multiply → Semi-Complex 16x16 and Pack into Two
Words
Intrinsic     vmpyxrp_v32_c32_v32_conj_pneg[_p]
name
Spec syntax   vmpyxrp {Oop [,conj] [,pneg][,vmpsX]} vx[X], vcYp, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0..7
                                                            Offset for the first DW used from operand

2
Operands
              4    IN2_C32        coef_t                    Coefficient operand
              5    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 4
              6    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vmpyxrp_v32_c32_v32_conj_pneg_p (8, vIn, 0, vcoefIn, LOW, vecPred);
                   IN_VPR last operand is relevant only for
Comments      1.
                   vmpyxrp_v32_c32_v32_conj_pneg_p version.


Main table → Multiplication → Multiply → Semi-Complex 16x16 and Pack into Two
Words
Intrinsic     vmpyxrp_v32_c32_v32_conj_pneg_vmpsX[_p]
name
Spec syntax   vmpyxrp {Oop [,conj] [,pneg][,vmpsX]} vx[X], vcYp, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8           Number of atomic operations
                                                           Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                           modv0/modv2 mode registers
              3    IN1_V32        vec_t                    Input vector operand
Operands      4    IN1_OFST       uint8     0..7           Offset for the first DW used from operand
                                                           3

              5    IN2_C32        coef_t                   Coefficient operand
              6    IN2_PART       uint8     LOW,HIGH       Word part which is used for operand 5
              7    IN_VPR         vprex_t                  Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vmpyxrp_v32_c32_v32_conj_pneg_vmpsX_p (8, 1, vIn, 0, vcoefIn, LOW, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmpyxrp_v32_c32_v32_conj_pneg_vmpsX_p version.


Main table → Multiplication → Multiply → Semi-Complex 16x16 and Pack into Two
Words
Intrinsic     vmpyxrp_v32_c32_v32_conj_vmpsX[_p]
name
Spec syntax   vmpyxrp {Oop [,conj] [,pneg][,vmpsX]} vx[X], vcYp, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8           Number of atomic operations
                                                           Selects the VMSNX and VPSX set within

2    VMPSX          uint8     0,1
Operands                                                   modv0/modv2 mode registers
              3    IN1_V32        vec_t                    Input vector operand
              4    IN1_OFST       uint8     0..7           Offset for the first DW used from operand
                                                             3

              5    IN2_C32        coef_t                     Coefficient operand
              6    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 5
              7    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vmpyxrp_v32_c32_v32_conj_vmpsX_p (8, 1, vIn, 0, vcoefIn, LOW, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmpyxrp_v32_c32_v32_conj_vmpsX_p version.


Main table → Multiplication → Multiply → Semi-Complex 16x16 and Pack into Two
Words
Intrinsic     vmpyxrp_v32_c32_v32[_p]
name
Spec syntax   vmpyxrp {Oop [,conj] [,pneg][,vmpsX]} vx[X], vcYp, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             2
Operands
              4    IN2_C32        coef_t                     Coefficient operand
              5    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 4
              6    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vmpyxrp_v32_c32_v32_p (8, vIn, 0, vcoefIn, LOW, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmpyxrp_v32_c32_v32_p version.


Main table → Multiplication → Multiply → Semi-Complex 16x16 and Pack into Two
Words
Intrinsic     vmpyxrp_v32_c32_v32_pneg[_p]
name
Spec syntax   vmpyxrp {Oop [,conj] [,pneg][,vmpsX]} vx[X], vcYp, vz[0], ?vprX

Return type   vec_t
              1    OOP            uint8     1..8            Number of atomic operations

2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0..7            Offset for the first DW used from operand
Operands                                                    2

              4    IN2_C32        coef_t                    Coefficient operand
              5    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 4
              6    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vmpyxrp_v32_c32_v32_pneg_p (8, vIn, 0, vcoefIn, LOW, vecPred);

                   IN_VPR last operand is relevant only for vmpyxrp_v32_c32_v32_pneg_p
Comments      1.
                   version.


Main table → Multiplication → Multiply → Semi-Complex 16x16 and Pack into Two
Words
Intrinsic     vmpyxrp_v32_c32_v32_pneg_vmpsX[_p]
name
Spec syntax   vmpyxrp {Oop [,conj] [,pneg][,vmpsX]} vx[X], vcYp, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
                                                            Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand
Operands      4    IN1_OFST       uint8                     Offset for the first DW used from operand
                                            0..7
                                                            3

              5    IN2_C32        coef_t                    Coefficient operand
              6    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 5
              7    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vmpyxrp_v32_c32_v32_pneg_vmpsX_p (8, 1, vIn, 0, vcoefIn, LOW, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmpyxrp_v32_c32_v32_pneg_vmpsX_p version.

Main table → Multiplication → Multiply → Semi-Complex 16x16 and Pack into Two
Words
Intrinsic     vmpyxrp_v32_c32_v32_vmpsX[_p]
name

Spec syntax   vmpyxrp {Oop [,conj] [,pneg][,vmpsX]} vx[X], vcYp, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
                                                            Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand
Operands      4    IN1_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            3

              5    IN2_C32        coef_t                    Coefficient operand
              6    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 5
              7    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vmpyxrp_v32_c32_v32_vmpsX_p (8, 1, vIn, 0, vcoefIn, LOW, vecPred);

                   IN_VPR last operand is relevant only for vmpyxrp_v32_c32_v32_vmpsX_p
Comments      1.
                   version.


Main table → Multiplication → Multiply → Semi-Complex 16x16 and Pack into Two
Words
Intrinsic     vmpyxrp_v32_v32_v32_conj[_p]
name
Spec syntax   vmpyxrp {Oop [,const][,conj] [,pneg][,vmpsX]} vx[X], vy[Y]p, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             2

Operands      4    IN2_V32        vec_t                      Input vector operand

              5    IN2_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             4

              6    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 4
              7    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;

C example     vprex_t vecPred;
              ...
              vRes = vmpyxrp_v32_v32_v32_conj_p (8, vIn, 0, vIn2, 0, LOW, vecPred);

                   IN_VPR last operand is relevant only for vmpyxrp_v32_v32_v32_conj_p
Comments      1.
                   version.


Main table → Multiplication → Multiply → Semi-Complex 16x16 and Pack into Two
Words
Intrinsic     vmpyxrp_v32_v32_v32_conj_pneg[_p]
name
Spec syntax   vmpyxrp {Oop [,const][,conj] [,pneg][,vmpsX]} vx[X], vy[Y]p, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             2

Operands      4    IN2_V32        vec_t                      Input vector operand

              5    IN2_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             4

              6    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 4
              7    IN_VPR         vprex_t                    Vector predicate operand
C example     vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmpyxrp_v32_v32_v32_conj_pneg_p (8, vIn, 0, vIn2, 0, LOW, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmpyxrp_v32_v32_v32_conj_pneg_p version.


Main table → Multiplication → Multiply → Semi-Complex 16x16 and Pack into Two
Words
Intrinsic     vmpyxrp_v32_v32_v32_conj_pneg_vmpsX[_p]
name
Spec syntax   vmpyxrp {Oop [,const][,conj] [,pneg][,vmpsX]} vx[X], vy[Y]p, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
                                                            Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand

              4    IN1_OFST       uint8     0..7

Offset for the first DW used from operand
Operands                                                    3

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
              vRes = vmpyxrp_v32_v32_v32_conj_pneg_vmpsX_p (8, 1, vIn, 0, vIn2, 0, LOW, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmpyxrp_v32_v32_v32_conj_pneg_vmpsX_p version.


Main table → Multiplication → Multiply → Semi-Complex 16x16 and Pack into Two
Words
Intrinsic     vmpyxrp_v32_v32_v32_conj_vmpsX[_p]
name
Spec syntax   vmpyxrp {Oop [,const][,conj] [,pneg][,vmpsX]} vx[X], vy[Y]p, vz[0], ?vprX

Return type   vec_t
              1    OOP            uint8     1..8            Number of atomic operations
                                                            Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand

              4    IN1_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
Operands                                                    3

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
              vRes = vmpyxrp_v32_v32_v32_conj_vmpsX_p (8, 1, vIn, 0, vIn2, 0, LOW, vecPred);

IN_VPR last operand is relevant only for
Comments      1.
                   vmpyxrp_v32_v32_v32_conj_vmpsX_p version.


Main table → Multiplication → Multiply → Semi-Complex 16x16 and Pack into Two
Words
Intrinsic     vmpyxrp_v32_v32_v32_const_conj[_p]
name
Spec syntax   vmpyxrp {Oop [,const][,conj] [,pneg][,vmpsX]} vx[X], vy[Y]p, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            2

Operands      4    IN2_V32        vec_t                     Input vector operand

              5    IN2_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            4

              6    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 4
              7    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
C example     vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmpyxrp_v32_v32_v32_const_conj_p (8, vIn, 0, vIn2, 0, LOW, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmpyxrp_v32_v32_v32_const_conj_p version.


Main table → Multiplication → Multiply → Semi-Complex 16x16 and Pack into Two
Words
Intrinsic     vmpyxrp_v32_v32_v32_const_conj_pneg[_p]
name
Spec syntax   vmpyxrp {Oop [,const][,conj] [,pneg][,vmpsX]} vx[X], vy[Y]p, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             2

Operands      4    IN2_V32        vec_t                      Input vector operand

              5    IN2_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             4

6    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 4
              7    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmpyxrp_v32_v32_v32_const_conj_pneg_p (8, vIn, 0, vIn2, 0, LOW, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmpyxrp_v32_v32_v32_const_conj_pneg_p version.


Main table → Multiplication → Multiply → Semi-Complex 16x16 and Pack into Two
Words
Intrinsic     vmpyxrp_v32_v32_v32_const_conj_pneg_vmpsX[_p]
name
Spec syntax   vmpyxrp {Oop [,const][,conj] [,pneg][,vmpsX]} vx[X], vy[Y]p, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations
                                                             Selects the VMSNX and VPSX set within
Operands      2    VMPSX          uint8     0,1
                                                             modv0/modv2 mode registers
              3    IN1_V32        vec_t                      Input vector operand
              4    IN1_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            3

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
              vRes = vmpyxrp_v32_v32_v32_const_conj_pneg_vmpsX_p (8, 1, vIn, 0, vIn2, 0, LOW, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmpyxrp_v32_v32_v32_const_conj_pneg_vmpsX_p version.


Main table → Multiplication → Multiply → Semi-Complex 16x16 and Pack into Two
Words
Intrinsic     vmpyxrp_v32_v32_v32_const_conj_vmpsX[_p]
name
Spec syntax   vmpyxrp {Oop [,const][,conj] [,pneg][,vmpsX]} vx[X], vy[Y]p, vz[0], ?vprX

Return type   vec_t

1    OOP            uint8     1..8            Number of atomic operations
                                                            Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand

              4    IN1_OFST       uint8     0..7            Offset for the first DW used from operand
Operands                                                    3

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
              vRes = vmpyxrp_v32_v32_v32_const_conj_vmpsX_p (8, 1, vIn, 0, vIn2, 0, LOW, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmpyxrp_v32_v32_v32_const_conj_vmpsX_p version.

Main table → Multiplication → Multiply → Semi-Complex 16x16 and Pack into Two
Words
Intrinsic     vmpyxrp_v32_v32_v32_const[_p]
name
Spec syntax   vmpyxrp {Oop [,const][,conj] [,pneg][,vmpsX]} vx[X], vy[Y]p, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             2

Operands      4    IN2_V32        vec_t                      Input vector operand

              5    IN2_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             4

              6    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 4
              7    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;

vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmpyxrp_v32_v32_v32_const_p (8, vIn, 0, vIn2, 0, LOW, vecPred);

                   IN_VPR last operand is relevant only for vmpyxrp_v32_v32_v32_const_p
Comments      1.
                   version.


Main table → Multiplication → Multiply → Semi-Complex 16x16 and Pack into Two
Words
Intrinsic     vmpyxrp_v32_v32_v32_const_pneg[_p]
name
Spec syntax   vmpyxrp {Oop [,const][,conj] [,pneg][,vmpsX]} vx[X], vy[Y]p, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             2
Operands
              4    IN2_V32        vec_t                      Input vector operand

              5    IN2_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             4

              6    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 4
              7    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmpyxrp_v32_v32_v32_const_pneg_p (8, vIn, 0, vIn2, 0, LOW, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmpyxrp_v32_v32_v32_const_pneg_p version.


Main table → Multiplication → Multiply → Semi-Complex 16x16 and Pack into Two
Words
Intrinsic     vmpyxrp_v32_v32_v32_const_pneg_vmpsX[_p]
name
Spec syntax   vmpyxrp {Oop [,const][,conj] [,pneg][,vmpsX]} vx[X], vy[Y]p, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
                                                            Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand

              4    IN1_OFST       uint8     0..7

Offset for the first DW used from operand
Operands                                                    3

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
              vRes = vmpyxrp_v32_v32_v32_const_pneg_vmpsX_p (8, 1, vIn, 0, vIn2, 0, LOW, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmpyxrp_v32_v32_v32_const_pneg_vmpsX_p version.


Main table → Multiplication → Multiply → Semi-Complex 16x16 and Pack into Two
Words
Intrinsic     vmpyxrp_v32_v32_v32_const_vmpsX[_p]
name
Spec syntax   vmpyxrp {Oop [,const][,conj] [,pneg][,vmpsX]} vx[X], vy[Y]p, vz[0], ?vprX
Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations

              2
                                                            Selects the VMSNX and VPSX set within
                   VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand

              4    IN1_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
Operands                                                    3

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
              vRes = vmpyxrp_v32_v32_v32_const_vmpsX_p (8, 1, vIn, 0, vIn2, 0, LOW, vecPred);

IN_VPR last operand is relevant only for
Comments      1.
                   vmpyxrp_v32_v32_v32_const_vmpsX_p version.


Main table → Multiplication → Multiply → Semi-Complex 16x16 and Pack into Two
Words
Intrinsic     vmpyxrp_v32_v32_v32[_p]
name
Spec syntax   vmpyxrp {Oop [,const][,conj] [,pneg][,vmpsX]} vx[X], vy[Y]p, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            2

Operands      4    IN2_V32        vec_t                     Input vector operand

              5    IN2_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            4

              6    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 4
              7    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
C example     vec_t vIn2;
              vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmpyxrp_v32_v32_v32_p (8, vIn, 0, vIn2, 0, LOW, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmpyxrp_v32_v32_v32_p version.


Main table → Multiplication → Multiply → Semi-Complex 16x16 and Pack into Two
Words
Intrinsic     vmpyxrp_v32_v32_v32_pneg[_p]
name
Spec syntax   vmpyxrp {Oop [,const][,conj] [,pneg][,vmpsX]} vx[X], vy[Y]p, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             2

Operands      4    IN2_V32        vec_t                      Input vector operand

              5    IN2_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             4

              6    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 4

7    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmpyxrp_v32_v32_v32_pneg_p (8, vIn, 0, vIn2, 0, LOW, vecPred);

                   IN_VPR last operand is relevant only for vmpyxrp_v32_v32_v32_pneg_p
Comments      1.
                   version.


Main table → Multiplication → Multiply → Semi-Complex 16x16 and Pack into Two
Words
Intrinsic     vmpyxrp_v32_v32_v32_pneg_vmpsX[_p]
name
Spec syntax   vmpyxrp {Oop [,const][,conj] [,pneg][,vmpsX]} vx[X], vy[Y]p, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations
                                                             Selects the VMSNX and VPSX set within
Operands      2    VMPSX          uint8     0,1
                                                             modv0/modv2 mode registers
              3    IN1_V32        vec_t                      Input vector operand
              4    IN1_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            3

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
              vRes = vmpyxrp_v32_v32_v32_pneg_vmpsX_p (8, 1, vIn, 0, vIn2, 0, LOW, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmpyxrp_v32_v32_v32_pneg_vmpsX_p version.


Main table → Multiplication → Multiply → Semi-Complex 16x16 and Pack into Two
Words
Intrinsic     vmpyxrp_v32_v32_v32_vmpsX[_p]
name
Spec syntax   vmpyxrp {Oop [,const][,conj] [,pneg][,vmpsX]} vx[X], vy[Y]p, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
                                                            Selects the VMSNX and VPSX set within

2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand

              4    IN1_OFST       uint8     0..7            Offset for the first DW used from operand
Operands                                                    3

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
              vRes = vmpyxrp_v32_v32_v32_vmpsX_p (8, 1, vIn, 0, vIn2, 0, LOW, vecPred);

                   IN_VPR last operand is relevant only for vmpyxrp_v32_v32_v32_vmpsX_p
Comments      1.
                   version.

Main table → Multiplication → Multiply → Semi-Complex 16x16 and Pack into Two
Words
