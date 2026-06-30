# Multiplication → Multiply → Complex 16x16 with Exponent and Pack into

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Multiplication → Multiply → Complex 16x16 with Exponent and Pack into
Two Words

Complex 16x16 with Exponent and Pack into Two Words

Complex 16x16 with Exponent and Pack into Two Words
Performs complex multiply with exponent between two complex numbers. Each complex source
consists of real 16-bit part and imaginary 16-bit part. The third source is the exponent. The

complex product is packed into either 32-bit or 40-bit destination determined by the vector
register type.
Available Switches
                Number of atomic operations. An atomic operation is defined as a single 16x16
Oop
                complex multiply with exponent. 1op ≤ Oop ≤ 8op
                Number of atomic operations. An atomic operation is defined as a single 16x16
Qop
                complex multiply with exponent. 1op ≤ Qop ≤ 4op
conj            Performs complex multiply using complex conjugate of vy[Y]
pneg            When used, the product is negated
vmpsX           Selects the VMSNX and VPSX set within modv0 or modv2 mode registers.
Intrinsic Names
vmpyxep_v32_v32_v32_v32_conj
vmpyxep_v32_v32_v32_v32_conj_pneg
vmpyxep_v32_v32_v32_v32_conj_pneg_vmpsX
vmpyxep_v32_v32_v32_v32_conj_vmpsX
vmpyxep_v32_v32_v32_v32
vmpyxep_v32_v32_v32_v32_pneg
vmpyxep_v32_v32_v32_v32_pneg_vmpsX
vmpyxep_v32_v32_v32_v32_vmpsX
Instruction details in the instruction set specification
Intrinsic     vmpyxep_v32_v32_v32_v32_conj[_p]
name
Spec syntax   vmpyxep {Oop [,conj][,pneg][,vmpsX]} vx[X], vy[Y], vv[V]p, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0,4
                                                             Offset for the first DW used from operand
                                                             2

              4    IN2_V32        vec_t                      Input vector operand

Operands      5    IN2_OFST       uint8     0,4
                                                             Offset for the first DW used from operand
                                                             4

              6    IN3_V32        vec_t                      Input vector operand

              7    IN3_OFST       uint8     0,4              Offset for the first DW used from operand
                                                             6

              8    IN3_PART       uint8     LOW,HIGH         Word part which is used for operand 6
              9    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
C example     vec_t vRes;
              vprex_t vecPred;
              ...

vRes = vmpyxep_v32_v32_v32_v32_conj_p (8, vIn, 0, vIn2, 0, vIn3, 0, LOW, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmpyxep_v32_v32_v32_v32_conj_p version.


Main table → Multiplication → Multiply → Complex 16x16 with Exponent and Pack into
Two Words
Intrinsic     vmpyxep_v32_v32_v32_v32_conj_pneg[_p]
name
Spec syntax   vmpyxep {Oop [,conj][,pneg][,vmpsX]} vx[X], vy[Y], vv[V]p, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0,4
                                                             Offset for the first DW used from operand
Operands                                                     2

              4    IN2_V32        vec_t                      Input vector operand

              5    IN2_OFST       uint8     0,4
                                                             Offset for the first DW used from operand
                                                             4
              6    IN3_V32        vec_t                      Input vector operand

              7    IN3_OFST       uint8     0,4              Offset for the first DW used from operand
                                                             6

              8    IN3_PART       uint8     LOW,HIGH         Word part which is used for operand 6
              9    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
C example     vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmpyxep_v32_v32_v32_v32_conj_pneg_p (8, vIn, 0, vIn2, 0, vIn3, 0, LOW, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmpyxep_v32_v32_v32_v32_conj_pneg_p version.


Main table → Multiplication → Multiply → Complex 16x16 with Exponent and Pack into
Two Words
Intrinsic     vmpyxep_v32_v32_v32_v32_conj_pneg_vmpsX[_p]
name
Spec syntax   vmpyxep {Oop [,conj][,pneg][,vmpsX]} vx[X], vy[Y], vv[V]p, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations
                                                             Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1

modv0/modv2 mode registers
              3    IN1_V32        vec_t                      Input vector operand

              4    IN1_OFST       uint8     0,4
                                                             Offset for the first DW used from operand
                                                             3

              5    IN2_V32        vec_t                      Input vector operand
Operands
              6    IN2_OFST       uint8     0,4              Offset for the first DW used from operand
                                                             5

              7    IN3_V32        vec_t                      Input vector operand

              8    IN3_OFST       uint8     0,4              Offset for the first DW used from operand
                                                             7

              9    IN3_PART       uint8     LOW,HIGH         Word part which is used for operand 7
              10   IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
C example     vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmpyxep_v32_v32_v32_v32_conj_pneg_vmpsX_p (8, 1, vIn, 0, vIn2, 0, vIn3, 0, LOW, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmpyxep_v32_v32_v32_v32_conj_pneg_vmpsX_p version.


Main table → Multiplication → Multiply → Complex 16x16 with Exponent and Pack into
Two Words
Intrinsic     vmpyxep_v32_v32_v32_v32_conj_vmpsX[_p]
name
Spec syntax   vmpyxep {Oop [,conj][,pneg][,vmpsX]} vx[X], vy[Y], vv[V]p, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations
                                                             Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                             modv0/modv2 mode registers
              3    IN1_V32        vec_t                      Input vector operand

              4    IN1_OFST       uint8     0,4
                                                             Offset for the first DW used from operand
                                                             3

              5    IN2_V32        vec_t                      Input vector operand
Operands

6    IN2_OFST       uint8     0,4              Offset for the first DW used from operand
                                                             5

              7    IN3_V32        vec_t                      Input vector operand

              8    IN3_OFST       uint8     0,4              Offset for the first DW used from operand
                                                             7

              9    IN3_PART       uint8     LOW,HIGH         Word part which is used for operand 7
              10   IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
C example     vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmpyxep_v32_v32_v32_v32_conj_vmpsX_p (8, 1, vIn, 0, vIn2, 0, vIn3, 0, LOW, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmpyxep_v32_v32_v32_v32_conj_vmpsX_p version.


Main table → Multiplication → Multiply → Complex 16x16 with Exponent and Pack into
Two Words
Intrinsic     vmpyxep_v32_v32_v32_v32[_p]
name
Spec syntax   vmpyxep {Oop [,conj][,pneg][,vmpsX]} vx[X], vy[Y], vv[V]p, vz[0], ?vprX
Return type   vec_t

              1    OOP             uint8     1..8            Number of atomic operations
              2    IN1_V32         vec_t                     Input vector operand

              3    IN1_OFST        uint8     0,4
                                                             Offset for the first DW used from operand
                                                             2

              4    IN2_V32         vec_t                     Input vector operand

Operands      5    IN2_OFST        uint8     0,4
                                                             Offset for the first DW used from operand
                                                             4

              6    IN3_V32         vec_t                     Input vector operand

              7    IN3_OFST        uint8     0,4
                                                             Offset for the first DW used from operand
                                                             6

              8    IN3_PART        uint8     LOW,HIGH        Word part which is used for operand 6
              9    IN_VPR          vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;

C example     vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmpyxep_v32_v32_v32_v32_p (8, vIn, 0, vIn2, 0, vIn3, 0, LOW, vecPred);

                   IN_VPR last operand is relevant only for vmpyxep_v32_v32_v32_v32_p
Comments      1.
                   version.


Main table → Multiplication → Multiply → Complex 16x16 with Exponent and Pack into
Two Words
Intrinsic     vmpyxep_v32_v32_v32_v32_pneg[_p]
name
Spec syntax   vmpyxep {Oop [,conj][,pneg][,vmpsX]} vx[X], vy[Y], vv[V]p, vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8            Number of atomic operations
              2    IN1_V32         vec_t                     Input vector operand

              3    IN1_OFST        uint8     0,4             Offset for the first DW used from operand
                                                             2

Operands
              4    IN2_V32         vec_t                     Input vector operand

              5    IN2_OFST        uint8     0,4             Offset for the first DW used from operand
                                                             4

              6    IN3_V32         vec_t                     Input vector operand

              7    IN3_OFST        uint8     0,4
                                                             Offset for the first DW used from operand
                                                             6
              8    IN3_PART       uint8     LOW,HIGH         Word part which is used for operand 6
              9    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
C example     vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmpyxep_v32_v32_v32_v32_pneg_p (8, vIn, 0, vIn2, 0, vIn3, 0, LOW, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmpyxep_v32_v32_v32_v32_pneg_p version.


Main table → Multiplication → Multiply → Complex 16x16 with Exponent and Pack into
Two Words
Intrinsic     vmpyxep_v32_v32_v32_v32_pneg_vmpsX[_p]
name
Spec syntax   vmpyxep {Oop [,conj][,pneg][,vmpsX]} vx[X], vy[Y], vv[V]p, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations

              2
                                                             Selects the VMSNX and VPSX set within

VMPSX          uint8     0,1
                                                             modv0/modv2 mode registers
              3    IN1_V32        vec_t                      Input vector operand

              4    IN1_OFST       uint8     0,4
                                                             Offset for the first DW used from operand
                                                             3

              5    IN2_V32        vec_t                      Input vector operand
Operands
              6    IN2_OFST       uint8     0,4
                                                             Offset for the first DW used from operand
                                                             5

              7    IN3_V32        vec_t                      Input vector operand

              8    IN3_OFST       uint8     0,4              Offset for the first DW used from operand
                                                             7

              9    IN3_PART       uint8     LOW,HIGH         Word part which is used for operand 7
              10   IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
C example     vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmpyxep_v32_v32_v32_v32_pneg_vmpsX_p (8, 1, vIn, 0, vIn2, 0, vIn3, 0, LOW, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmpyxep_v32_v32_v32_v32_pneg_vmpsX_p version.

Main table → Multiplication → Multiply → Complex 16x16 with Exponent and Pack into
Two Words
Intrinsic     vmpyxep_v32_v32_v32_v32_vmpsX[_p]
name
Spec syntax   vmpyxep {Oop [,conj][,pneg][,vmpsX]} vx[X], vy[Y], vv[V]p, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations
                                                             Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                             modv0/modv2 mode registers
              3    IN1_V32        vec_t                      Input vector operand

              4    IN1_OFST       uint8     0,4              Offset for the first DW used from operand
                                                             3

              5    IN2_V32        vec_t                      Input vector operand
Operands

6    IN2_OFST       uint8     0,4              Offset for the first DW used from operand
                                                             5

              7    IN3_V32        vec_t                      Input vector operand

              8    IN3_OFST       uint8     0,4              Offset for the first DW used from operand
                                                             7

              9    IN3_PART       uint8     LOW,HIGH         Word part which is used for operand 7
              10   IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
C example     vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmpyxep_v32_v32_v32_v32_vmpsX_p (8, 1, vIn, 0, vIn2, 0, vIn3, 0, LOW, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmpyxep_v32_v32_v32_v32_vmpsX_p version.


Main table → Multiplication → Multiply → Complex 16x16 with Exponent and Pack into
Two Words
