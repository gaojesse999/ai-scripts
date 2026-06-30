# Multiplication → Absolute Square and Subtract → Vector Complex

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Multiplication → Absolute Square and Subtract → Vector Complex
Absolute Square and Subtract

Vector Complex Absolute Square and Subtract

Vector Complex Absolute Square and Subtract
Performs complex absolute squaring and subtraction. Each complex source is 32-bits wide (16-
bit real and 16-bit imaginary). The products are subtracted from the 40-bit destination.
Available Switches
             Number of atomic operations. An atomic operation is defined as a single complex
Hhop
             absolute square subtract operation. 9op ≤ Hhop ≤ 16op
             Number of atomic operations. An atomic operation is defined as a single complex
Oop
             absolute square subtract operation. 1op ≤ Oop ≤ 8op
vmpsX        Selects the VMSNX and VPSX set within modv0 or modv2 mode registers.
Intrinsic Names
vsqasx_v32_v40
vsqasx_v32_v40_vmpsX
vsqasx_v32_v32_v40_v40
vsqasx_v32_v32_v40_v40_vmpsX
Instruction details in the instruction set specification
Intrinsic     vsqasx_v32_v40[_p]
name
Spec syntax   vsqasx {Oop [,vmpsX]} vx[X], voz[0], ?vprX

Return type   vec40_t

              1    OOP             uint8     1..8              Number of atomic operations

2    IN1_V32         vec_t                       Input vector operand

Operands      3    IN1_OFST        uint8     0..7
                                                               Offset for the first DW used from operand
                                                               2

              4    IN2_V40         vec40_t                     Output vector operand
              5    IN_VPR          vprex_t                     Vector predicate operand
              vec_t vIn;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vsqasx_v32_v40_p (8, vIn, 0, vRes, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vsqasx_v32_v40_p version.


Main table → Multiplication → Absolute Square and Subtract → Vector Complex
Absolute Square and Subtract
Intrinsic     vsqasx_v32_v40_vmpsX[_p]
name
Spec syntax   vsqasx {Oop [,vmpsX]} vx[X], voz[0], ?vprX

Return type   vec40_t

              1    OOP             uint8     1..8              Number of atomic operations
                                                               Selects the VMSNX and VPSX set within
              2    VMPSX           uint8     0,1
                                                               modv0/modv2 mode registers
              3    IN1_V32         vec_t                       Input vector operand
Operands
              4    IN1_OFST        uint8     0..7
                                                               Offset for the first DW used from operand
                                                               3

              5    IN2_V40         vec40_t                     Output vector operand
              6    IN_VPR          vprex_t                     Vector predicate operand
              vec_t vIn;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vsqasx_v32_v40_vmpsX_p (8, 1, vIn, 0, vRes, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vsqasx_v32_v40_vmpsX_p version.

Main table → Multiplication → Absolute Square and Subtract → Vector Complex
Absolute Square and Subtract
Intrinsic     vsqasx_v32_v32_v40_v40[_p]
name
Spec syntax   vsqasx {Hhop [,vmpsX]} vx[X], vy[Y], voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    HHOP            uint8     9..16            Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand

3    IN1_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
                                                              2

              4    IN2_V32         vec_t                      Input vector operand
Operands
              5    IN2_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
                                                              4

              6    IN3_V40         vec40_t                    Output vector operand
              7    IN4_V40         vec40_t                    Output vector operand
              8    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes1;
C example     vec40_t vRes2;
              vprex_t vecPred;
              ...
              vRes2 = vsqasx_v32_v32_v40_v40_p (16, vIn, 0, vIn2, 0, vRes1, vRes1, vecPred);

                   IN_VPR last operand is relevant only for vsqasx_v32_v32_v40_v40_p
Comments      1.
                   version.


Main table → Multiplication → Absolute Square and Subtract → Vector Complex
Absolute Square and Subtract
Intrinsic     vsqasx_v32_v32_v40_v40_vmpsX[_p]
name
Spec syntax   vsqasx {Hhop [,vmpsX]} vx[X], vy[Y], voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    HHOP            uint8     9..16            Number of atomic operations

              2
                                                              Selects the VMSNX and VPSX set within
                   VMPSX           uint8     0,1
                                                              modv0/modv2 mode registers
              3    IN1_V32         vec_t                      Input vector operand
Operands
              4    IN1_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
                                                              3

              5    IN2_V32         vec_t                      Input vector operand
              6    IN2_OFST        uint8     0..7             Offset for the first DW used from operand
                                                            5

            7    IN3_V40        vec40_t                     Output vector operand
            8    IN4_V40        vec40_t                     Output vector operand

9    IN_VPR         vprex_t                     Vector predicate operand
            vec_t vIn;
            vec_t vIn2;
            vec40_t vRes1;
C example   vec40_t vRes2;
            vprex_t vecPred;
            ...
            vRes2 = vsqasx_v32_v32_v40_v40_vmpsX_p (16, 1, vIn, 0, vIn2, 0, vRes1, vRes1, vecPred);

                 IN_VPR last operand is relevant only for
Comments    1.
                 vsqasx_v32_v32_v40_v40_vmpsX_p version.


Main table → Multiplication → Absolute Square and Subtract → Vector Complex
Absolute Square and Subtract

Main table → Multiplication → Absolute Square and Subtract → Vector Complex
Absolute Square and Subtract Long

Vector Complex Absolute Square and Subtract Long

Vector Complex Absolute Square and Subtract Long
Performs squaring of complex absolute and subtract. Each complex source is 64-bits wide (32-bit
real and 32-bit imaginary). The products are subtracted from the 72-bit destination.
Available Switches
             Number of atomic operations. An atomic operation is defined as a single complex
Qop
             absolute square and subtract operation. 1op ≤ Qop ≤ 4op
vmpsX Selects the VMSNX and VPSX set within modv0 or modv2 mode registers.
Intrinsic Names
vsqasxll_v32_v40
vsqasxll_v32_v40_vmpsX
Instruction details in the instruction set specification
Intrinsic     vsqasxll_v32_v40[_p]
name
Spec syntax   vsqasxll {Qop [,vmpsX]} vx[Xe], voz[0], ?vprX

Return type   vec40_t

              1    QOP             uint8      1..4             Number of atomic operations
              2    IN1_V32         vec_t                       Input vector operand

Operands      3    IN1_OFST        uint8      0,4
                                                               Offset for the first DW used from operand
                                                               2

              4    IN2_V40         vec40_t                     Output vector operand
              5    IN_VPR          vprex_t                     Vector predicate operand
              vec_t vIn;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vsqasxll_v32_v40_p (4, vIn, 0, vRes, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vsqasxll_v32_v40_p version.


Main table → Multiplication → Absolute Square and Subtract → Vector Complex
Absolute Square and Subtract Long
Intrinsic     vsqasxll_v32_v40_vmpsX[_p]
name
Spec syntax   vsqasxll {Qop [,vmpsX]} vx[Xe], voz[0], ?vprX

Return type   vec40_t

              1    QOP             uint8      1..4             Number of atomic operations
                                                               Selects the VMSNX and VPSX set within
              2    VMPSX           uint8      0,1
                                                               modv0/modv2 mode registers
              3    IN1_V32         vec_t                       Input vector operand
Operands
              4    IN1_OFST        uint8      0,4
                                                               Offset for the first DW used from operand
                                                               3

              5    IN2_V40         vec40_t                     Output vector operand
              6    IN_VPR          vprex_t                     Vector predicate operand
              vec_t vIn;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vsqasxll_v32_v40_vmpsX_p (4, 1, vIn, 0, vRes, vecPred);

                   IN_VPR last operand is relevant only for vsqasxll_v32_v40_vmpsX_p
Comments      1.
                   version.

Main table → Multiplication → Absolute Square and Subtract → Vector Complex
Absolute Square and Subtract Long

Main table → Multiplication → Absolute Square and Subtract → Vector Complex
Absolute Square and Subtract with Exponent

Vector Complex Absolute Square and Subtract with Exponent

Vector Complex Absolute Square and Subtract with Exponent
Performs complex absolute squaring and subtraction. Each complex source is 32-bits wide (16-
bit real and 16-bit imaginary). The second source is the exponent. The products are subtracted
from the 40-bit destination.
Available Switches
               Number of atomic operations. An atomic operation is defined as a single complex
Hhop
               absolute square subtract operation. 9op ≤ Hhop ≤ 16op
vmpsX          Selects the VMSNX and VPSX set within modv0 or modv2 mode registers.
Intrinsic Names
vsqasxe_v32_v32_v40
vsqasxe_v32_v32_v40_vmpsX
vsqasxe_v32_v32_v32_v40_v40
vsqasxe_v32_v32_v32_v40_v40_vmpsX
Instruction details in the instruction set specification
Intrinsic     vsqasxe_v32_v32_v40[_p]
name
Spec syntax   vsqasxe {Oop [,vmpsX]} vx[X], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

3    IN1_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             2

              4    IN2_V32        vec_t                      Input vector operand
Operands
              5    IN2_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             4

              6    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 4
              7    IN3_V40        vec40_t                    Output vector operand
              8    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vExponentValue;
              vec_t vIn;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vsqasxe_v32_v32_v40_p (8, vIn, 0, vExponentValue, 0, LOW, vRes, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vsqasxe_v32_v32_v40_p version.


Main table → Multiplication → Absolute Square and Subtract → Vector Complex
Absolute Square and Subtract with Exponent
Intrinsic     vsqasxe_v32_v32_v40_vmpsX[_p]
name
Spec syntax   vsqasxe {Oop [,vmpsX]} vx[X], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8             Number of atomic operations
                                                             Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                             modv0/modv2 mode registers
              3    IN1_V32        vec_t                      Input vector operand

Operands      4    IN1_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             3

              5    IN2_V32        vec_t                      Input vector operand

              6    IN2_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             5

              7    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 5
            8    IN3_V40        vec40_t                    Output vector operand
            9    IN_VPR         vprex_t                    Vector predicate operand
            vec_t vExponentValue;

vec_t vIn;
            vec40_t vRes;
C example   vprex_t vecPred;
            ...
            vRes = vsqasxe_v32_v32_v40_vmpsX_p (8, 1, vIn, 0, vExponentValue, 0, LOW, vRes, vecPred);

                 IN_VPR last operand is relevant only for vsqasxe_v32_v32_v40_vmpsX_p
Comments    1.
                 version.


Main table → Multiplication → Absolute Square and Subtract → Vector Complex
Absolute Square and Subtract with Exponent
Intrinsic     vsqasxe_v32_v32_v32_v40_v40[_p]
name
Spec syntax   vsqasxe {Hhop [,vmpsX]} vx[0], vy[0], vv[V]p, voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    HHOP           uint8     9..16           Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              4    IN3_V32        vec_t                     Input vector operand

Operands      5    IN3_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            4

              6    IN3_PART       uint8     LOW,HIGH        Word part which is used for operand 4
              7    IN4_V40        vec40_t                   Output vector operand
              8    IN5_V40        vec40_t                   Output vector operand
              9    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vExponentValue;
              vec_t vIn;
              vec_t vIn3;
              vec40_t vRes1;
C example     vec40_t vRes2;
              vprex_t vecPred;
              ...
              vRes2 = vsqasxe_v32_v32_v32_v40_v40_p (16, vIn, vExponentValue, vIn3, 0, LOW, vRes1, vRes1,
              vecPred);

                   IN_VPR last operand is relevant only for vsqasxe_v32_v32_v32_v40_v40_p
Comments      1.
                   version.


Main table → Multiplication → Absolute Square and Subtract → Vector Complex
Absolute Square and Subtract with Exponent
Intrinsic     vsqasxe_v32_v32_v32_v40_v40_vmpsX[_p]
name
Spec syntax   vsqasxe {Hhop [,vmpsX]} vx[0], vy[0], vv[V]p, voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    HHOP           uint8     9..16           Number of atomic operations
                                                            Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1

modv0/modv2 mode registers
Operands      3    IN1_V32        vec_t                     Input vector operand
              4    IN2_V32        vec_t                     Input vector operand
              5    IN3_V32        vec_t                     Input vector operand
            6    IN3_OFST       uint8     0..7            Offset for the first DW used from operand
                                                          5

            7    IN3_PART       uint8     LOW,HIGH        Word part which is used for operand 5
            8    IN4_V40        vec40_t                   Output vector operand
            9    IN5_V40        vec40_t                   Output vector operand
            10   IN_VPR         vprex_t                   Vector predicate operand
            vec_t vExponentValue;
            vec_t vIn;
            vec_t vIn3;
            vec40_t vRes1;
C example   vec40_t vRes2;
            vprex_t vecPred;
            ...
            vRes2 = vsqasxe_v32_v32_v32_v40_v40_vmpsX_p (16, 1, vIn, vExponentValue, vIn3, 0, LOW, vRes1,
            vRes1, vecPred);

                 IN_VPR last operand is relevant only for
Comments    1.
                 vsqasxe_v32_v32_v32_v40_v40_vmpsX_p version.


Main table → Multiplication → Absolute Square and Subtract → Vector Complex
Absolute Square and Subtract with Exponent
