# Multiplication → Multiply → Complex 16x16 and Pack into Two Words

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Multiplication → Multiply → Complex 16x16 and Pack into Two Words

Complex 16x16 and Pack into Two Words

Complex 16x16 and Pack into Two Words
Performs complex multiplication between two complex numbers. Each complex source consists
of real 16-bit part and imaginary 16-bit part. The multipication products are accumulated into 20-
bit destination parts respectively.
Available Switches
               Number of atomic operations. An atomic operation is defined as a single complex
Oop
               multiplication and pack operation. 1op ≤ Oop ≤ 8op
conj           Performs complex multiply using complex conjugate of vcY/vy[Y]
const          When used, vy[Y] is constant throughout the operations.
pneg           When used, the product is negated
vmpsX          Selects the VMSNX and VPSX set within modv0 or modv2 mode registers.
Intrinsic Names
vmpyxp_v32_c32_v32_conj
vmpyxp_v32_c32_v32_conj_pneg
vmpyxp_v32_c32_v32_conj_pneg_vmpsX
vmpyxp_v32_c32_v32_conj_vmpsX
vmpyxp_v32_c32_v32
vmpyxp_v32_c32_v32_pneg
vmpyxp_v32_c32_v32_pneg_vmpsX
vmpyxp_v32_c32_v32_vmpsX
vmpyxp_v32_v32_v32_conj
vmpyxp_v32_v32_v32_conj_pneg
vmpyxp_v32_v32_v32_conj_pneg_vmpsX
vmpyxp_v32_v32_v32_conj_vmpsX
vmpyxp_v32_v32_v32_const_conj
vmpyxp_v32_v32_v32_const_conj_pneg
vmpyxp_v32_v32_v32_const_conj_pneg_vmpsX
vmpyxp_v32_v32_v32_const_conj_vmpsX
vmpyxp_v32_v32_v32_const
vmpyxp_v32_v32_v32_const_pneg
vmpyxp_v32_v32_v32_const_pneg_vmpsX
vmpyxp_v32_v32_v32_const_vmpsX
vmpyxp_v32_v32_v32
vmpyxp_v32_v32_v32_pneg
vmpyxp_v32_v32_v32_pneg_vmpsX
vmpyxp_v32_v32_v32_vmpsX
Instruction details in the instruction set specification
Intrinsic     vmpyxp_v32_c32_v32_conj[_p]
name
Spec syntax   vmpyxp {Oop [,conj] [,pneg][,vmpsX]} vx[X], vcY, vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8            Number of atomic operations
              2    IN1_V32         vec_t                     Input vector operand

Operands      3    IN1_OFST        uint8     0,4

Offset for the first DW used from operand
                                                             2

              4    IN2_C32         coef_t                    Coefficient operand
              5    IN_VPR          vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vmpyxp_v32_c32_v32_conj_p (8, vIn, 0, vcoefIn, vecPred);

                   IN_VPR last operand is relevant only for vmpyxp_v32_c32_v32_conj_p
Comments      1.
                   version.


Main table → Multiplication → Multiply → Complex 16x16 and Pack into Two Words
Intrinsic     vmpyxp_v32_c32_v32_conj_pneg[_p]
name
Spec syntax   vmpyxp {Oop [,conj] [,pneg][,vmpsX]} vx[X], vcY, vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8            Number of atomic operations
              2    IN1_V32         vec_t                     Input vector operand

Operands      3    IN1_OFST        uint8     0,4
                                                             Offset for the first DW used from operand
                                                             2

              4    IN2_C32         coef_t                    Coefficient operand
              5    IN_VPR          vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vmpyxp_v32_c32_v32_conj_pneg_p (8, vIn, 0, vcoefIn, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmpyxp_v32_c32_v32_conj_pneg_p version.


Main table → Multiplication → Multiply → Complex 16x16 and Pack into Two Words
Intrinsic     vmpyxp_v32_c32_v32_conj_pneg_vmpsX[_p]
name
Spec syntax   vmpyxp {Oop [,conj] [,pneg][,vmpsX]} vx[X], vcY, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
                                                            Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand
Operands
              4    IN1_OFST       uint8     0,4

Offset for the first DW used from operand
                                                            3

              5    IN2_C32        coef_t                    Coefficient operand
              6    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vmpyxp_v32_c32_v32_conj_pneg_vmpsX_p (8, 1, vIn, 0, vcoefIn, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmpyxp_v32_c32_v32_conj_pneg_vmpsX_p version.


Main table → Multiplication → Multiply → Complex 16x16 and Pack into Two Words
Intrinsic     vmpyxp_v32_c32_v32_conj_vmpsX[_p]
name
Spec syntax   vmpyxp {Oop [,conj] [,pneg][,vmpsX]} vx[X], vcY, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
                                                            Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand
Operands
              4    IN1_OFST       uint8     0,4
                                                            Offset for the first DW used from operand
                                                            3

              5    IN2_C32        coef_t                    Coefficient operand
              6    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vmpyxp_v32_c32_v32_conj_vmpsX_p (8, 1, vIn, 0, vcoefIn, vecPred);
                   IN_VPR last operand is relevant only for
Comments      1.
                   vmpyxp_v32_c32_v32_conj_vmpsX_p version.


Main table → Multiplication → Multiply → Complex 16x16 and Pack into Two Words
Intrinsic     vmpyxp_v32_c32_v32[_p]
name
Spec syntax   vmpyxp {Oop [,conj] [,pneg][,vmpsX]} vx[X], vcY, vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand

Operands      3    IN1_OFST        uint8     0,4

Offset for the first DW used from operand
                                                              2

              4    IN2_C32         coef_t                     Coefficient operand
              5    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vmpyxp_v32_c32_v32_p (8, vIn, 0, vcoefIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmpyxp_v32_c32_v32_p version.


Main table → Multiplication → Multiply → Complex 16x16 and Pack into Two Words
Intrinsic     vmpyxp_v32_c32_v32_pneg[_p]
name
Spec syntax   vmpyxp {Oop [,conj] [,pneg][,vmpsX]} vx[X], vcY, vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand

Operands      3    IN1_OFST        uint8     0,4
                                                              Offset for the first DW used from operand
                                                              2

              4    IN2_C32         coef_t                     Coefficient operand
              5    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vmpyxp_v32_c32_v32_pneg_p (8, vIn, 0, vcoefIn, vecPred);
                   IN_VPR last operand is relevant only for vmpyxp_v32_c32_v32_pneg_p
Comments      1.
                   version.


Main table → Multiplication → Multiply → Complex 16x16 and Pack into Two Words
Intrinsic     vmpyxp_v32_c32_v32_pneg_vmpsX[_p]
name
Spec syntax   vmpyxp {Oop [,conj] [,pneg][,vmpsX]} vx[X], vcY, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
                                                            Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand
Operands
              4    IN1_OFST       uint8     0,4             Offset for the first DW used from operand

3

              5    IN2_C32        coef_t                    Coefficient operand
              6    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vmpyxp_v32_c32_v32_pneg_vmpsX_p (8, 1, vIn, 0, vcoefIn, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmpyxp_v32_c32_v32_pneg_vmpsX_p version.


Main table → Multiplication → Multiply → Complex 16x16 and Pack into Two Words
Intrinsic     vmpyxp_v32_c32_v32_vmpsX[_p]
name
Spec syntax   vmpyxp {Oop [,conj] [,pneg][,vmpsX]} vx[X], vcY, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
                                                            Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand
Operands
              4    IN1_OFST       uint8     0,4
                                                            Offset for the first DW used from operand
                                                            3

              5    IN2_C32        coef_t                    Coefficient operand
              6    IN_VPR         vprex_t                   Vector predicate operand
            vec_t vIn;
            vec_t vRes;
            coef_t vcoefIn;
C example   vprex_t vecPred;
            ...
            vRes = vmpyxp_v32_c32_v32_vmpsX_p (8, 1, vIn, 0, vcoefIn, vecPred);

                 IN_VPR last operand is relevant only for vmpyxp_v32_c32_v32_vmpsX_p
Comments    1.
                 version.


Main table → Multiplication → Multiply → Complex 16x16 and Pack into Two Words
Intrinsic     vmpyxp_v32_v32_v32_conj[_p]
name
Spec syntax   vmpyxp {Oop [,const][,conj] [,pneg][,vmpsX]} vx[X], vy[Y], vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand

              3    IN1_OFST        uint8     0,4
                                                              Offset for the first DW used from operand
                                                              2

Operands
              4    IN2_V32         vec_t                      Input vector operand

              5    IN2_OFST        uint8     0,4
                                                              Offset for the first DW used from operand
                                                              4

              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmpyxp_v32_v32_v32_conj_p (8, vIn, 0, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for vmpyxp_v32_v32_v32_conj_p
Comments      1.
                   version.


Main table → Multiplication → Multiply → Complex 16x16 and Pack into Two Words
Intrinsic     vmpyxp_v32_v32_v32_conj_pneg[_p]
name
Spec syntax   vmpyxp {Oop [,const][,conj] [,pneg][,vmpsX]} vx[X], vy[Y], vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand

              3    IN1_OFST        uint8     0,4              Offset for the first DW used from operand
                                                              2
Operands
              4    IN2_V32         vec_t                      Input vector operand

              5    IN2_OFST        uint8     0,4
                                                              Offset for the first DW used from operand
                                                              4

              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmpyxp_v32_v32_v32_conj_pneg_p (8, vIn, 0, vIn2, 0, vecPred);
                   IN_VPR last operand is relevant only for
Comments      1.
                   vmpyxp_v32_v32_v32_conj_pneg_p version.


Main table → Multiplication → Multiply → Complex 16x16 and Pack into Two Words
Intrinsic     vmpyxp_v32_v32_v32_conj_pneg_vmpsX[_p]
name
Spec syntax   vmpyxp {Oop [,const][,conj] [,pneg][,vmpsX]} vx[X], vy[Y], vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
                                                            Selects the VMSNX and VPSX set within

2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand

Operands      4    IN1_OFST       uint8     0,4             Offset for the first DW used from operand
                                                            3

              5    IN2_V32        vec_t                     Input vector operand

              6    IN2_OFST       uint8     0,4             Offset for the first DW used from operand
                                                            5

              7    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmpyxp_v32_v32_v32_conj_pneg_vmpsX_p (8, 1, vIn, 0, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmpyxp_v32_v32_v32_conj_pneg_vmpsX_p version.


Main table → Multiplication → Multiply → Complex 16x16 and Pack into Two Words
Intrinsic     vmpyxp_v32_v32_v32_conj_vmpsX[_p]
name
Spec syntax   vmpyxp {Oop [,const][,conj] [,pneg][,vmpsX]} vx[X], vy[Y], vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
                                                            Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
Operands
              3    IN1_V32        vec_t                     Input vector operand

              4    IN1_OFST       uint8     0,4
                                                            Offset for the first DW used from operand
                                                            3
              5    IN2_V32         vec_t                     Input vector operand

              6    IN2_OFST        uint8     0,4             Offset for the first DW used from operand
                                                             5

              7    IN_VPR          vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmpyxp_v32_v32_v32_conj_vmpsX_p (8, 1, vIn, 0, vIn2, 0, vecPred);

IN_VPR last operand is relevant only for
Comments      1.
                   vmpyxp_v32_v32_v32_conj_vmpsX_p version.


Main table → Multiplication → Multiply → Complex 16x16 and Pack into Two Words
Intrinsic     vmpyxp_v32_v32_v32_const_conj[_p]
name
Spec syntax   vmpyxp {Oop [,const][,conj] [,pneg][,vmpsX]} vx[X], vy[Y], vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8            Number of atomic operations
              2    IN1_V32         vec_t                     Input vector operand

              3    IN1_OFST        uint8     0,4
                                                             Offset for the first DW used from operand
                                                             2
Operands
              4    IN2_V32         vec_t                     Input vector operand

              5    IN2_OFST        uint8     0,4
                                                             Offset for the first DW used from operand
                                                             4

              6    IN_VPR          vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmpyxp_v32_v32_v32_const_conj_p (8, vIn, 0, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmpyxp_v32_v32_v32_const_conj_p version.


Main table → Multiplication → Multiply → Complex 16x16 and Pack into Two Words
Intrinsic     vmpyxp_v32_v32_v32_const_conj_pneg[_p]
name
Spec syntax   vmpyxp {Oop [,const][,conj] [,pneg][,vmpsX]} vx[X], vy[Y], vz[0], ?vprX

Return type   vec_t
              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0,4              Offset for the first DW used from operand
                                                             2
Operands
              4    IN2_V32        vec_t                      Input vector operand

              5    IN2_OFST       uint8     0,4
                                                             Offset for the first DW used from operand
                                                             4

              6    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;

vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmpyxp_v32_v32_v32_const_conj_pneg_p (8, vIn, 0, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmpyxp_v32_v32_v32_const_conj_pneg_p version.


Main table → Multiplication → Multiply → Complex 16x16 and Pack into Two Words
Intrinsic     vmpyxp_v32_v32_v32_const_conj_pneg_vmpsX[_p]
name
Spec syntax   vmpyxp {Oop [,const][,conj] [,pneg][,vmpsX]} vx[X], vy[Y], vz[0], ?vprX

Return type   vec_t

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

              7    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmpyxp_v32_v32_v32_const_conj_pneg_vmpsX_p (8, 1, vIn, 0, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmpyxp_v32_v32_v32_const_conj_pneg_vmpsX_p version.

Main table → Multiplication → Multiply → Complex 16x16 and Pack into Two Words
Intrinsic     vmpyxp_v32_v32_v32_const_conj_vmpsX[_p]
name
Spec syntax   vmpyxp {Oop [,const][,conj] [,pneg][,vmpsX]} vx[X], vy[Y], vz[0], ?vprX

Return type   vec_t

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

              7    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmpyxp_v32_v32_v32_const_conj_vmpsX_p (8, 1, vIn, 0, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmpyxp_v32_v32_v32_const_conj_vmpsX_p version.


Main table → Multiplication → Multiply → Complex 16x16 and Pack into Two Words
Intrinsic     vmpyxp_v32_v32_v32_const[_p]
name
Spec syntax   vmpyxp {Oop [,const][,conj] [,pneg][,vmpsX]} vx[X], vy[Y], vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0,4
                                                             Offset for the first DW used from operand
                                                             2
Operands
              4    IN2_V32        vec_t                      Input vector operand

              5    IN2_OFST       uint8     0,4
                                                             Offset for the first DW used from operand
                                                             4

              6    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmpyxp_v32_v32_v32_const_p (8, vIn, 0, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for vmpyxp_v32_v32_v32_const_p
Comments      1.
                   version.


Main table → Multiplication → Multiply → Complex 16x16 and Pack into Two Words
Intrinsic     vmpyxp_v32_v32_v32_const_pneg[_p]
name

Spec syntax   vmpyxp {Oop [,const][,conj] [,pneg][,vmpsX]} vx[X], vy[Y], vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand

              3    IN1_OFST        uint8     0,4
                                                              Offset for the first DW used from operand
                                                              2
Operands
              4    IN2_V32         vec_t                      Input vector operand

              5    IN2_OFST        uint8     0,4
                                                              Offset for the first DW used from operand
                                                              4

              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmpyxp_v32_v32_v32_const_pneg_p (8, vIn, 0, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmpyxp_v32_v32_v32_const_pneg_p version.


Main table → Multiplication → Multiply → Complex 16x16 and Pack into Two Words
Intrinsic     vmpyxp_v32_v32_v32_const_pneg_vmpsX[_p]
name
Spec syntax   vmpyxp {Oop [,const][,conj] [,pneg][,vmpsX]} vx[X], vy[Y], vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8             Number of atomic operations
                                                              Selects the VMSNX and VPSX set within
Operands      2    VMPSX           uint8     0,1
                                                              modv0/modv2 mode registers
              3    IN1_V32         vec_t                      Input vector operand
              4    IN1_OFST       uint8     0,4              Offset for the first DW used from operand
                                                             3

              5    IN2_V32        vec_t                      Input vector operand

              6    IN2_OFST       uint8     0,4              Offset for the first DW used from operand
                                                             5

              7    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;

C example     vprex_t vecPred;
              ...
              vRes = vmpyxp_v32_v32_v32_const_pneg_vmpsX_p (8, 1, vIn, 0, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmpyxp_v32_v32_v32_const_pneg_vmpsX_p version.


Main table → Multiplication → Multiply → Complex 16x16 and Pack into Two Words
Intrinsic     vmpyxp_v32_v32_v32_const_vmpsX[_p]
name
Spec syntax   vmpyxp {Oop [,const][,conj] [,pneg][,vmpsX]} vx[X], vy[Y], vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations
                                                             Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                             modv0/modv2 mode registers
              3    IN1_V32        vec_t                      Input vector operand

Operands      4    IN1_OFST       uint8     0,4
                                                             Offset for the first DW used from operand
                                                             3

              5    IN2_V32        vec_t                      Input vector operand

              6    IN2_OFST       uint8     0,4              Offset for the first DW used from operand
                                                             5

              7    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmpyxp_v32_v32_v32_const_vmpsX_p (8, 1, vIn, 0, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmpyxp_v32_v32_v32_const_vmpsX_p version.


Main table → Multiplication → Multiply → Complex 16x16 and Pack into Two Words
Intrinsic     vmpyxp_v32_v32_v32[_p]
name
Spec syntax   vmpyxp {Oop [,const][,conj] [,pneg][,vmpsX]} vx[X], vy[Y], vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand

              3    IN1_OFST        uint8     0,4
                                                              Offset for the first DW used from operand
                                                              2
Operands

4    IN2_V32         vec_t                      Input vector operand

              5    IN2_OFST        uint8     0,4
                                                              Offset for the first DW used from operand
                                                              4

              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmpyxp_v32_v32_v32_p (8, vIn, 0, vIn2, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmpyxp_v32_v32_v32_p version.


Main table → Multiplication → Multiply → Complex 16x16 and Pack into Two Words
Intrinsic     vmpyxp_v32_v32_v32_pneg[_p]
name
Spec syntax   vmpyxp {Oop [,const][,conj] [,pneg][,vmpsX]} vx[X], vy[Y], vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand

              3    IN1_OFST        uint8     0,4              Offset for the first DW used from operand
                                                              2
Operands
              4    IN2_V32         vec_t                      Input vector operand

              5    IN2_OFST        uint8     0,4
                                                              Offset for the first DW used from operand
                                                              4

              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmpyxp_v32_v32_v32_pneg_p (8, vIn, 0, vIn2, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmpyxp_v32_v32_v32_pneg_p
                   version.


Main table → Multiplication → Multiply → Complex 16x16 and Pack into Two Words
Intrinsic     vmpyxp_v32_v32_v32_pneg_vmpsX[_p]
name
Spec syntax   vmpyxp {Oop [,const][,conj] [,pneg][,vmpsX]} vx[X], vy[Y], vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
                                                            Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1

modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand

Operands      4    IN1_OFST       uint8     0,4             Offset for the first DW used from operand
                                                            3

              5    IN2_V32        vec_t                     Input vector operand

              6    IN2_OFST       uint8     0,4             Offset for the first DW used from operand
                                                            5

              7    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmpyxp_v32_v32_v32_pneg_vmpsX_p (8, 1, vIn, 0, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmpyxp_v32_v32_v32_pneg_vmpsX_p version.


Main table → Multiplication → Multiply → Complex 16x16 and Pack into Two Words
Intrinsic     vmpyxp_v32_v32_v32_vmpsX[_p]
name
Spec syntax   vmpyxp {Oop [,const][,conj] [,pneg][,vmpsX]} vx[X], vy[Y], vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
                                                            Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
Operands      3    IN1_V32        vec_t                     Input vector operand

              4    IN1_OFST       uint8     0,4
                                                            Offset for the first DW used from operand
                                                            3

              5    IN2_V32        vec_t                     Input vector operand
            6    IN2_OFST       uint8     0,4              Offset for the first DW used from operand
                                                           5

            7    IN_VPR         vprex_t                    Vector predicate operand
            vec_t vIn;
            vec_t vIn2;
            vec_t vRes;
C example   vprex_t vecPred;
            ...
            vRes = vmpyxp_v32_v32_v32_vmpsX_p (8, 1, vIn, 0, vIn2, 0, vecPred);

                 IN_VPR last operand is relevant only for vmpyxp_v32_v32_v32_vmpsX_p
Comments    1.
                 version.

Main table → Multiplication → Multiply → Complex 16x16 and Pack into Two Words
