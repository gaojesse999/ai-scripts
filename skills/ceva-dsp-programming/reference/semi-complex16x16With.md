# Multiplication → Multiply-Accumulate → Semi-Complex 16x16 with

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Multiplication → Multiply-Accumulate → Semi-Complex 16x16 with
Exponent

Semi-Complex 16x16 with Exponent

Semi-Complex 16x16 with Exponent
Performs complex operation by real multipliy-accumulate with exponent between a complex
number and a real number. The complex source consists of real 16-bit part and imaginary 16-bit
part. The real number source consists of 16-bit. Each of the real and the imaginary products is
accumulated with the 40-bit destination respectively.
Available Switches
            Number of atomic operations. An atomic operation is defined as a single multiply-
            accumulate complex by real with exponent operation. Writes to two vector
Ohop
            destinations, where the first vector destination is fully written, and the second vector
            destination is set according to Ohop switch.

Number of atomic operations. An atomic operation is defined as pair of multiply-
Qop
            accumulate complex by real with exponent operation.
conj        Performs complex multiply-accumulate using complex conjugate of vx[X]
vmpsX Selects the VMSNX and VPSX set within modv0 or modv2 mode registers.
Intrinsic Names
vmacxre_v32_v32_v32_v40_v40_conj
vmacxre_v32_v32_v32_v40_v40_conj_vmpsX
vmacxre_v32_v32_v32_v40_v40
vmacxre_v32_v32_v32_v40_v40_vmpsX
vmacxre_v32_v32_v32_v40_conj
vmacxre_v32_v32_v32_v40_conj_vmpsX
vmacxre_v32_v32_v32_v40
vmacxre_v32_v32_v32_v40_vmpsX
Instruction details in the instruction set specification
Intrinsic     vmacxre_v32_v32_v32_v40_v40_conj[_p]
name
Spec syntax   vmacxre {Ohop [,conj][,vmpsX]} vx[X], vy[Y]p, vv[V]p, voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    OHOP           uint8     5..8            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            2

              4    IN2_V32        vec_t                     Input vector operand

              5    IN2_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            4

Operands
              6    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 4
              7    IN3_V32        vec_t                     Input vector operand

              8    IN3_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            7

              9    IN3_PART       uint8     LOW,HIGH        Word part which is used for operand 7
              10   IN4_V40        vec40_t                   Output vector operand
              11   RES2_V40       vec40_t                   Output vector result operand
              12   IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec40_t vRes1;
C example     vec40_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vmacxre_v32_v32_v32_v40_v40_conj_p (8, vIn, 0, vIn2, 0, LOW, vIn3, 0, LOW, vRes1, vRes2,

vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vmacxre_v32_v32_v32_v40_v40_conj_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).


Main table → Multiplication → Multiply-Accumulate → Semi-Complex 16x16 with
Exponent
Intrinsic     vmacxre_v32_v32_v32_v40_v40_conj_vmpsX[_p]
name
Spec syntax   vmacxre {Ohop [,conj][,vmpsX]} vx[X], vy[Y]p, vv[V]p, voz1[0], voz2[0], ?vprX
Return type   vec40_t

              1    OHOP           uint8     5..8            Number of atomic operations

              2
                                                            Selects the VMSNX and VPSX set within
                   VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand

              4    IN1_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            3

              5    IN2_V32        vec_t                     Input vector operand

              6    IN2_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            5
Operands
              7    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 5
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

vRes1 = vmacxre_v32_v32_v32_v40_v40_conj_vmpsX_p (8, 1, vIn, 0, vIn2, 0, LOW, vIn3, 0, LOW,
              vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vmacxre_v32_v32_v32_v40_v40_conj_vmpsX_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).


Main table → Multiplication → Multiply-Accumulate → Semi-Complex 16x16 with
Exponent
Intrinsic     vmacxre_v32_v32_v32_v40_v40[_p]
name
Spec syntax   vmacxre {Ohop [,conj][,vmpsX]} vx[X], vy[Y]p, vv[V]p, voz1[0], voz2[0], ?vprX

Return type   vec40_t
              1    OHOP           uint8     5..8            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            2

              4    IN2_V32        vec_t                     Input vector operand

              5    IN2_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            4

Operands
              6    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 4
              7    IN3_V32        vec_t                     Input vector operand

              8    IN3_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            7

              9    IN3_PART       uint8     LOW,HIGH        Word part which is used for operand 7
              10   IN4_V40        vec40_t                   Output vector operand
              11   RES2_V40       vec40_t                   Output vector result operand
              12   IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec40_t vRes1;
C example     vec40_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vmacxre_v32_v32_v32_v40_v40_p (8, vIn, 0, vIn2, 0, LOW, vIn3, 0, LOW, vRes1, vRes2,
              vecPred);

1.
                   IN_VPR last operand is relevant only for vmacxre_v32_v32_v32_v40_v40_p
                   version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).


Main table → Multiplication → Multiply-Accumulate → Semi-Complex 16x16 with
Exponent
Intrinsic     vmacxre_v32_v32_v32_v40_v40_vmpsX[_p]
name
Spec syntax   vmacxre {Ohop [,conj][,vmpsX]} vx[X], vy[Y]p, vv[V]p, voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    OHOP           uint8     5..8            Number of atomic operations
Operands                                                    Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
            3    IN1_V32        vec_t                     Input vector operand

            4    IN1_OFST       uint8     0..7            Offset for the first DW used from operand
                                                          3

            5    IN2_V32        vec_t                     Input vector operand

            6    IN2_OFST       uint8     0..7            Offset for the first DW used from operand
                                                          5

            7    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 5
            8    IN3_V32        vec_t                     Input vector operand

            9    IN3_OFST       uint8     0..7
                                                          Offset for the first DW used from operand
                                                          8

            10   IN3_PART       uint8     LOW,HIGH        Word part which is used for operand 8
            11   IN4_V40        vec40_t                   Output vector operand
            12   RES2_V40       vec40_t                   Output vector result operand
            13   IN_VPR         vprex_t                   Vector predicate operand
            vec_t vIn;
            vec_t vIn2;
            vec_t vIn3;
            vec40_t vRes1;
C example   vec40_t vRes2;
            vprex_t vecPred;
            ...
            vRes1 = vmacxre_v32_v32_v32_v40_v40_vmpsX_p (8, 1, vIn, 0, vIn2, 0, LOW, vIn3, 0, LOW, vRes1,
            vRes2, vecPred);

IN_VPR last operand is relevant only for
            1.
                 vmacxre_v32_v32_v32_v40_v40_vmpsX_p version.
Comments         This intrinsic returns two results. The first result variable should be placed to
            2.   the left of the = sign (lvalue). The second result variable should be passed as
                 an additional parameter (RES2_V40).


Main table → Multiplication → Multiply-Accumulate → Semi-Complex 16x16 with
Exponent
Intrinsic     vmacxre_v32_v32_v32_v40_conj[_p]
name
Spec syntax   vmacxre {Qop [,conj][,vmpsX]} vx[X], vy[Y]p, vv[V]p, voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4             Number of atomic operations
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
              vRes = vmacxre_v32_v32_v32_v40_conj_p (4, vIn, 0, vIn2, 0, LOW, vIn3, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmacxre_v32_v32_v32_v40_conj_p version.


Main table → Multiplication → Multiply-Accumulate → Semi-Complex 16x16 with
Exponent
Intrinsic     vmacxre_v32_v32_v32_v40_conj_vmpsX[_p]
name

Spec syntax   vmacxre {Qop [,conj][,vmpsX]} vx[X], vy[Y]p, vv[V]p, voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4             Number of atomic operations
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
              8    IN3_V32        vec_t                     Input vector operand

              9    IN3_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            8

              10   IN3_PART       uint8     LOW,HIGH        Word part which is used for operand 8
              11   IN4_V40        vec40_t                   Output vector operand
              12   IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmacxre_v32_v32_v32_v40_conj_vmpsX_p (4, 1, vIn, 0, vIn2, 0, LOW, vIn3, 0, LOW, vRes,
              vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmacxre_v32_v32_v32_v40_conj_vmpsX_p version.


Main table → Multiplication → Multiply-Accumulate → Semi-Complex 16x16 with
Exponent
Intrinsic     vmacxre_v32_v32_v32_v40[_p]
name
Spec syntax   vmacxre {Qop [,conj][,vmpsX]} vx[X], vy[Y]p, vv[V]p, voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0..7

Offset for the first DW used from operand
                                                            2

              4    IN2_V32        vec_t                     Input vector operand
Operands
              5    IN2_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            4

              6    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 4
              7    IN3_V32        vec_t                     Input vector operand
              8    IN3_OFST       uint8     0..7            Offset for the first DW used from operand
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
              vRes = vmacxre_v32_v32_v32_v40_p (4, vIn, 0, vIn2, 0, LOW, vIn3, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for vmacxre_v32_v32_v32_v40_p
Comments      1.
                   version.


Main table → Multiplication → Multiply-Accumulate → Semi-Complex 16x16 with
Exponent
Intrinsic     vmacxre_v32_v32_v32_v40_vmpsX[_p]
name
Spec syntax   vmacxre {Qop [,conj][,vmpsX]} vx[X], vy[Y]p, vv[V]p, voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4             Number of atomic operations
                                                             Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                             modv0/modv2 mode registers
              3    IN1_V32        vec_t                      Input vector operand

              4    IN1_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             3

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
C example     vec_t vIn2;
              vec_t vIn3;
            vec40_t vRes;
            vprex_t vecPred;
            ...
            vRes = vmacxre_v32_v32_v32_v40_vmpsX_p (4, 1, vIn, 0, vIn2, 0, LOW, vIn3, 0, LOW, vRes, vecPred);

                 IN_VPR last operand is relevant only for
Comments    1.
                 vmacxre_v32_v32_v32_v40_vmpsX_p version.


Main table → Multiplication → Multiply-Accumulate → Semi-Complex 16x16 with
Exponent
