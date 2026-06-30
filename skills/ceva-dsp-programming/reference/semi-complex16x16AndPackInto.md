# Multiplication → Multiply-Subtract → Semi-Complex 16x16 and Pack into

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Multiplication → Multiply-Subtract → Semi-Complex 16x16 and Pack into
Two Words

Semi-Complex 16x16 and Pack into Two Words

Semi-Complex 16x16 and Pack into Two Words
Performs two complex by real multipliy-subtract operations between a complex number and a
real number. The complex source consists of real 16-bit part and imaginary 16-bit part, the real
number source consists of 16-bit. Each product is subtracted from the 20-bit destination part
respectively and packed into 40-bit destination.
Available Switches
                 Number of atomic operations. An atomic operation is defined as pair of multiply-
Oop
                 subtract operations. 1op ≤ Oop ≤ 8op
conj             Performs complex multiply-accumulate using complex conjugate of vx[X]
const            When used, vy[Y]p is constant throughout the operations.
vmpsX            Selects the VMSNX and VPSX set within modv0 or modv2 mode registers.
Intrinsic Names
vmsuxrp_v32_v32_v40_conj
vmsuxrp_v32_v32_v40_conj_vmpsX
vmsuxrp_v32_v32_v40_const_conj
vmsuxrp_v32_v32_v40_const_conj_vmpsX
vmsuxrp_v32_v32_v40_const
vmsuxrp_v32_v32_v40_const_vmpsX
vmsuxrp_v32_v32_v40
vmsuxrp_v32_v32_v40_vmpsX
vmsuxrp_v32_c32_v40_conj
vmsuxrp_v32_c32_v40_conj_vmpsX
vmsuxrp_v32_c32_v40
vmsuxrp_v32_c32_v40_vmpsX
Instruction details in the instruction set specification
Intrinsic     vmsuxrp_v32_v32_v40_conj[_p]
name
Spec syntax   vmsuxrp {Oop [,const][,conj][,vmpsX]} vx[X], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0,4
                                                             Offset for the first DW used from operand
                                                             2

              4    IN2_V32        vec_t                      Input vector operand
Operands
              5    IN2_OFST       uint8     0,4
                                                             Offset for the first DW used from operand
                                                             4

6    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 4
              7    IN3_V40        vec40_t                    Output vector operand
              8    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsuxrp_v32_v32_v40_conj_p (8, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for vmsuxrp_v32_v32_v40_conj_p
Comments      1.
                   version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 16x16 and Pack into
Two Words
Intrinsic     vmsuxrp_v32_v32_v40_conj_vmpsX[_p]
name
Spec syntax   vmsuxrp {Oop [,const][,conj][,vmpsX]} vx[X], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8             Number of atomic operations
                                                             Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                             modv0/modv2 mode registers
              3    IN1_V32        vec_t                      Input vector operand
Operands
              4    IN1_OFST       uint8     0,4              Offset for the first DW used from operand
                                                             3

              5    IN2_V32        vec_t                      Input vector operand

              6    IN2_OFST       uint8     0,4              Offset for the first DW used from operand
                                                             5
              7    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 5
              8    IN3_V40        vec40_t                    Output vector operand
              9    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsuxrp_v32_v32_v40_conj_vmpsX_p (8, 1, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsuxrp_v32_v32_v40_conj_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 16x16 and Pack into
Two Words
Intrinsic     vmsuxrp_v32_v32_v40_const_conj[_p]
name

Spec syntax   vmsuxrp {Oop [,const][,conj][,vmpsX]} vx[X], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0,4              Offset for the first DW used from operand
                                                             2

              4    IN2_V32        vec_t                      Input vector operand
Operands
              5    IN2_OFST       uint8     0,4              Offset for the first DW used from operand
                                                             4

              6    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 4
              7    IN3_V40        vec40_t                    Output vector operand
              8    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsuxrp_v32_v32_v40_const_conj_p (8, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsuxrp_v32_v32_v40_const_conj_p version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 16x16 and Pack into
Two Words
Intrinsic     vmsuxrp_v32_v32_v40_const_conj_vmpsX[_p]
name
Spec syntax   vmsuxrp {Oop [,const][,conj][,vmpsX]} vx[X], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8            Number of atomic operations
                                                            Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand

              4    IN1_OFST       uint8     0,4
                                                            Offset for the first DW used from operand
                                                            3
Operands      5    IN2_V32        vec_t                     Input vector operand

              6    IN2_OFST       uint8     0,4             Offset for the first DW used from operand
                                                            5

7    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 5
              8    IN3_V40        vec40_t                   Output vector operand
              9    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsuxrp_v32_v32_v40_const_conj_vmpsX_p (8, 1, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsuxrp_v32_v32_v40_const_conj_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 16x16 and Pack into
Two Words
Intrinsic     vmsuxrp_v32_v32_v40_const[_p]
name
Spec syntax   vmsuxrp {Oop [,const][,conj][,vmpsX]} vx[X], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0,4             Offset for the first DW used from operand
                                                            2
Operands
              4    IN2_V32        vec_t                     Input vector operand

              5    IN2_OFST       uint8     0,4             Offset for the first DW used from operand
                                                            4

              6    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 4
              7    IN3_V40        vec40_t                    Output vector operand
              8    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsuxrp_v32_v32_v40_const_p (8, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for vmsuxrp_v32_v32_v40_const_p
Comments      1.
                   version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 16x16 and Pack into
Two Words
Intrinsic     vmsuxrp_v32_v32_v40_const_vmpsX[_p]
name
Spec syntax   vmsuxrp {Oop [,const][,conj][,vmpsX]} vx[X], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8             Number of atomic operations

Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                             modv0/modv2 mode registers
              3    IN1_V32        vec_t                      Input vector operand

              4    IN1_OFST       uint8     0,4              Offset for the first DW used from operand
                                                             3
Operands      5    IN2_V32        vec_t                      Input vector operand

              6    IN2_OFST       uint8     0,4              Offset for the first DW used from operand
                                                             5

              7    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 5
              8    IN3_V40        vec40_t                    Output vector operand
              9    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsuxrp_v32_v32_v40_const_vmpsX_p (8, 1, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsuxrp_v32_v32_v40_const_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 16x16 and Pack into
Two Words
Intrinsic     vmsuxrp_v32_v32_v40[_p]
name
Spec syntax   vmsuxrp {Oop [,const][,conj][,vmpsX]} vx[X], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0,4
                                                             Offset for the first DW used from operand
                                                             2

              4    IN2_V32        vec_t                      Input vector operand
Operands
              5    IN2_OFST       uint8     0,4
                                                             Offset for the first DW used from operand
                                                             4

              6    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 4
              7    IN3_V40        vec40_t                    Output vector operand

8    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsuxrp_v32_v32_v40_p (8, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmsuxrp_v32_v32_v40_p version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 16x16 and Pack into
Two Words
Intrinsic     vmsuxrp_v32_v32_v40_vmpsX[_p]
name
Spec syntax   vmsuxrp {Oop [,const][,conj][,vmpsX]} vx[X], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8             Number of atomic operations
                                                             Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                             modv0/modv2 mode registers
              3    IN1_V32        vec_t                      Input vector operand

Operands      4    IN1_OFST       uint8     0,4              Offset for the first DW used from operand
                                                             3

              5    IN2_V32        vec_t                      Input vector operand

              6    IN2_OFST       uint8     0,4              Offset for the first DW used from operand
                                                             5

              7    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 5
            8    IN3_V40        vec40_t                    Output vector operand
            9    IN_VPR         vprex_t                    Vector predicate operand
            vec_t vIn;
            vec_t vIn2;
            vec40_t vRes;
C example   vprex_t vecPred;
            ...
            vRes = vmsuxrp_v32_v32_v40_vmpsX_p (8, 1, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

                 IN_VPR last operand is relevant only for vmsuxrp_v32_v32_v40_vmpsX_p
Comments    1.
                 version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 16x16 and Pack into
Two Words
Intrinsic     vmsuxrp_v32_c32_v40_conj[_p]
name
Spec syntax   vmsuxrp {Oop [,conj][,vmpsX]} vx[X], vcYp, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

3    IN1_OFST       uint8     0,4
                                                             Offset for the first DW used from operand
                                                             2
Operands      4    IN2_C32        coef_t                     Coefficient operand
              5    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 4
              6    IN3_V40        vec40_t                    Output vector operand
              7    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec40_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vmsuxrp_v32_c32_v40_conj_p (8, vIn, 0, vcoefIn, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for vmsuxrp_v32_c32_v40_conj_p
Comments      1.
                   version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 16x16 and Pack into
Two Words
Intrinsic     vmsuxrp_v32_c32_v40_conj_vmpsX[_p]
name
Spec syntax   vmsuxrp {Oop [,conj][,vmpsX]} vx[X], vcYp, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8             Number of atomic operations
                                                             Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                             modv0/modv2 mode registers
              3    IN1_V32        vec_t                      Input vector operand

              4    IN1_OFST       uint8     0,4              Offset for the first DW used from operand
Operands                                                     3

              5    IN2_C32        coef_t                     Coefficient operand
              6    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 5
              7    IN3_V40        vec40_t                    Output vector operand
              8    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec40_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vmsuxrp_v32_c32_v40_conj_vmpsX_p (8, 1, vIn, 0, vcoefIn, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsuxrp_v32_c32_v40_conj_vmpsX_p version.

Main table → Multiplication → Multiply-Subtract → Semi-Complex 16x16 and Pack into
Two Words
Intrinsic     vmsuxrp_v32_c32_v40[_p]
name
Spec syntax   vmsuxrp {Oop [,conj][,vmpsX]} vx[X], vcYp, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0,4
                                                             Offset for the first DW used from operand
                                                             2
Operands      4    IN2_C32        coef_t                     Coefficient operand
              5    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 4
              6    IN3_V40        vec40_t                    Output vector operand
              7    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec40_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vmsuxrp_v32_c32_v40_p (8, vIn, 0, vcoefIn, LOW, vRes, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmsuxrp_v32_c32_v40_p version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 16x16 and Pack into
Two Words
Intrinsic     vmsuxrp_v32_c32_v40_vmpsX[_p]
name
Spec syntax   vmsuxrp {Oop [,conj][,vmpsX]} vx[X], vcYp, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands                                                     Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                             modv0/modv2 mode registers
            3    IN1_V32        vec_t                     Input vector operand

            4    IN1_OFST       uint8     0,4             Offset for the first DW used from operand
                                                          3

            5    IN2_C32        coef_t                    Coefficient operand
            6    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 5
            7    IN3_V40        vec40_t                   Output vector operand
            8    IN_VPR         vprex_t                   Vector predicate operand
            vec_t vIn;
            vec40_t vRes;
            coef_t vcoefIn;

C example   vprex_t vecPred;
            ...
            vRes = vmsuxrp_v32_c32_v40_vmpsX_p (8, 1, vIn, 0, vcoefIn, LOW, vRes, vecPred);

                 IN_VPR last operand is relevant only for vmsuxrp_v32_c32_v40_vmpsX_p
Comments    1.
                 version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 16x16 and Pack into
Two Words
