# Multiplication → Absolute Square → Vector Complex Absolute Square

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Multiplication → Absolute Square → Vector Complex Absolute Square

Vector Complex Absolute Square

Vector Complex Absolute Square
Performs squaring of complex absolute. Each complex source is 32-bits wide (16-bit real and 16-
bit imaginary). The products are written to 40-bit destinations.
Available Switches
           Number of atomic operations. An atomic operation is defined as a single Complex
           Absolute Square operation. Writes to two vector destinations, where the first vector
Hhop
           destination is fully written, and the second vector destination is set according to Hhop
           switch.
           Number of atomic operations. An atomic operation is defined as a single Complex
Oop
           Absolute Square operation. 1op ≤ Oop ≤ 8op
vmpsX Selects the VMSNX and VPSX set within modv0 or modv2 mode registers.
Intrinsic Names
vsqax_v32_v32
vsqax_v32_v32_vmpsX
vsqax_v32_v32_v32_v32
vsqax_v32_v32_v32_v32_vmpsX
Instruction details in the instruction set specification
Intrinsic     vsqax_v32_v32[_p]
name
Spec syntax   vsqax {Oop [,vmpsX]} vx[X], vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8            Number of atomic operations
              2    IN1_V32         vec_t                     Input vector operand
Operands                                                     Offset for the first DW used from operand
              3    IN1_OFST        uint8     0..7
                                                             2

              4    IN_VPR          vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vsqax_v32_v32_p (8, vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vsqax_v32_v32_p version.


Main table → Multiplication → Absolute Square → Vector Complex Absolute Square
Intrinsic     vsqax_v32_v32_vmpsX[_p]
name
Spec syntax   vsqax {Oop [,vmpsX]} vx[X], vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8            Number of atomic operations

              2
                                                             Selects the VMSNX and VPSX set within
                   VMPSX           uint8     0,1
                                                             modv0/modv2 mode registers
Operands      3    IN1_V32         vec_t                     Input vector operand

4    IN1_OFST        uint8     0..7
                                                             Offset for the first DW used from operand
                                                             3

              5    IN_VPR          vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vsqax_v32_v32_vmpsX_p (8, 1, vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vsqax_v32_v32_vmpsX_p version.


Main table → Multiplication → Absolute Square → Vector Complex Absolute Square
Intrinsic     vsqax_v32_v32_v32_v32[_p]
name
Spec syntax   vsqax {Hhop [,vmpsX]} vx[X], vy[Y], vz1[0], vz2[0], ?vprX

Return type   vec_t

              1    HHOP            uint8     9..16            Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand

              3    IN1_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
                                                              2

Operands      4    IN2_V32         vec_t                      Input vector operand

              5    IN2_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
                                                              4

              6    RES2_V32        vec_t                      Input vector result operand
              7    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes1;
C example     vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vsqax_v32_v32_v32_v32_p (16, vIn, 0, vIn2, 0, vRes2, vecPred);

                   IN_VPR last operand is relevant only for vsqax_v32_v32_v32_v32_p
              1.
                   version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Multiplication → Absolute Square → Vector Complex Absolute Square
Intrinsic     vsqax_v32_v32_v32_v32_vmpsX[_p]
name
Spec syntax   vsqax {Hhop [,vmpsX]} vx[X], vy[Y], vz1[0], vz2[0], ?vprX

Return type   vec_t

1    HHOP            uint8     9..16            Number of atomic operations

              2
                                                              Selects the VMSNX and VPSX set within
                   VMPSX           uint8     0,1
                                                              modv0/modv2 mode registers
Operands      3    IN1_V32         vec_t                      Input vector operand

              4    IN1_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
                                                              3

              5    IN2_V32         vec_t                      Input vector operand
            6    IN2_OFST        uint8     0..7            Offset for the first DW used from operand
                                                           5

            7    RES2_V32        vec_t                     Input vector result operand
            8    IN_VPR          vprex_t                   Vector predicate operand
            vec_t vIn;
            vec_t vIn2;
            vec_t vRes1;
C example   vec_t vRes2;
            vprex_t vecPred;
            ...
            vRes1 = vsqax_v32_v32_v32_v32_vmpsX_p (16, 1, vIn, 0, vIn2, 0, vRes2, vecPred);

                 IN_VPR last operand is relevant only for
            1.
                 vsqax_v32_v32_v32_v32_vmpsX_p version.
Comments         This intrinsic returns two results. The first result variable should be placed to
            2.   the left of the = sign (lvalue). The second result variable should be passed as
                 an additional parameter (RES2_V32).


Main table → Multiplication → Absolute Square → Vector Complex Absolute Square

Main table → Multiplication → Absolute Square → Vector Complex Absolute Square
Long

Vector Complex Absolute Square Long

Vector Complex Absolute Square Long
Performs squaring of complex absolute. Each complex source is 64-bits wide (32-bit real and 32-
bit imaginary). The products are written to 64-bit or 72-bit destinations determined by the vector
register type.
Available Switches
              Number of atomic operations. An atomic operation is defined as a single complex
Qop
              absolute square operation. 1op ≤ Qop ≤ 4op
vmpsX         Selects the VMSNX and VPSX set within modv0 or modv2 mode registers.
Intrinsic Names
vsqaxll_v32_v32
vsqaxll_v32_v32_vmpsX
Instruction details in the instruction set specification

Intrinsic     vsqaxll_v32_v32[_p]
name
Spec syntax   vsqaxll {Qop [,vmpsX]} vx[Xe], vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8      1..4             Number of atomic operations
              2    IN1_V32         vec_t                       Input vector operand
Operands                                                       Offset for the first DW used from operand
              3    IN1_OFST        uint8      0,4
                                                               2

              4    IN_VPR          vprex_t                     Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vsqaxll_v32_v32_p (4, vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vsqaxll_v32_v32_p version.


Main table → Multiplication → Absolute Square → Vector Complex Absolute Square
Long
Intrinsic     vsqaxll_v32_v32_vmpsX[_p]
name
Spec syntax   vsqaxll {Qop [,vmpsX]} vx[Xe], vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8      1..4             Number of atomic operations

              2
                                                               Selects the VMSNX and VPSX set within
                   VMPSX           uint8      0,1
                                                               modv0/modv2 mode registers
Operands      3    IN1_V32         vec_t                       Input vector operand

              4    IN1_OFST        uint8      0,4
                                                               Offset for the first DW used from operand
                                                               3

              5    IN_VPR          vprex_t                     Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vsqaxll_v32_v32_vmpsX_p (4, 1, vIn, 0, vecPred);

                   IN_VPR last operand is relevant only for vsqaxll_v32_v32_vmpsX_p
Comments      1.
                   version.


Main table → Multiplication → Absolute Square → Vector Complex Absolute Square
Long
