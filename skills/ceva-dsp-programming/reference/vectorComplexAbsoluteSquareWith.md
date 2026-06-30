# Multiplication → Absolute Square → Vector Complex Absolute Square with

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Multiplication → Absolute Square → Vector Complex Absolute Square with
Exponent

Vector Complex Absolute Square with Exponent

Vector Complex Absolute Square with Exponent
Performs complex absolute squaring. Each complex source is 32-bits wide (16-bit real and 16-bit
imaginary). The second source is the exponent. The products are written to the 40-bit destination.
Available Switches
              Number of atomic operations. An atomic operation is defined as a single complex
Hhop
              absolute square accumulate operation. 9op ≤ Hhop ≤ 16op
vmpsX         Selects the VMSNX and VPSX set within modv0 or modv2 mode registers.
Intrinsic Names
vsqaxe_v32_v32_v32
vsqaxe_v32_v32_v32_vmpsX
vsqaxe_v32_v32_v32_v32_v32
vsqaxe_v32_v32_v32_v32_v32_vmpsX
Instruction details in the instruction set specification
Intrinsic     vsqaxe_v32_v32_v32[_p]
name
Spec syntax   vsqaxe {Oop [,vmpsX]} vx[X], vy[Y]p, vz[0], ?vprX

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
              vec_t vExponentValue;
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vsqaxe_v32_v32_v32_p (8, vIn, 0, vExponentValue, 0, LOW, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vsqaxe_v32_v32_v32_p version.


Main table → Multiplication → Absolute Square → Vector Complex Absolute Square with
Exponent
Intrinsic     vsqaxe_v32_v32_v32_vmpsX[_p]
name
Spec syntax   vsqaxe {Oop [,vmpsX]} vx[X], vy[Y]p, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations

              2
                                                             Selects the VMSNX and VPSX set within
                   VMPSX          uint8     0,1
                                                             modv0/modv2 mode registers
              3    IN1_V32        vec_t                      Input vector operand

              4    IN1_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
Operands                                                     3

              5    IN2_V32        vec_t                      Input vector operand

              6    IN2_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             5

              7    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 5
              8    IN_VPR         vprex_t                    Vector predicate operand
            vec_t vExponentValue;
            vec_t vIn;
            vec_t vRes;
C example   vprex_t vecPred;
            ...
            vRes = vsqaxe_v32_v32_v32_vmpsX_p (8, 1, vIn, 0, vExponentValue, 0, LOW, vecPred);

                 IN_VPR last operand is relevant only for vsqaxe_v32_v32_v32_vmpsX_p
Comments    1.
                 version.


Main table → Multiplication → Absolute Square → Vector Complex Absolute Square with
Exponent
Intrinsic     vsqaxe_v32_v32_v32_v32_v32[_p]
name

Spec syntax   vsqaxe {Hhop [,vmpsX]} vx[0], vy[0], vv[V]p, vz1[0], vz2[0], ?vprX

Return type   vec_t

              1    HHOP           uint8     9..16           Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              4    IN3_V32        vec_t                     Input vector operand
Operands                                                    Offset for the first DW used from operand
              5    IN3_OFST       uint8     0..7
                                                            4

              6    IN3_PART       uint8     LOW,HIGH        Word part which is used for operand 4
              7    RES2_V32       vec_t                     Input vector result operand
              8    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vExponentValue;
              vec_t vIn;
              vec_t vIn3;
              vec_t vRes1;
C example     vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vsqaxe_v32_v32_v32_v32_v32_p (16, vIn, vExponentValue, vIn3, 0, LOW, vRes2, vecPred);

                   IN_VPR last operand is relevant only for vsqaxe_v32_v32_v32_v32_v32_p
              1.
                   version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Multiplication → Absolute Square → Vector Complex Absolute Square with
Exponent
Intrinsic     vsqaxe_v32_v32_v32_v32_v32_vmpsX[_p]
name
Spec syntax   vsqaxe {Hhop [,vmpsX]} vx[0], vy[0], vv[V]p, vz1[0], vz2[0], ?vprX

Return type   vec_t

              1    HHOP           uint8     9..16           Number of atomic operations
                                                            Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
Operands                                                    modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand
              4    IN2_V32        vec_t                     Input vector operand
            5    IN3_V32        vec_t                    Input vector operand

6    IN3_OFST       uint8     0..7           Offset for the first DW used from operand
                                                         5

            7    IN3_PART       uint8     LOW,HIGH       Word part which is used for operand 5
            8    RES2_V32       vec_t                    Input vector result operand
            9    IN_VPR         vprex_t                  Vector predicate operand
            vec_t vExponentValue;
            vec_t vIn;
            vec_t vIn3;
            vec_t vRes1;
C example   vec_t vRes2;
            vprex_t vecPred;
            ...
            vRes1 = vsqaxe_v32_v32_v32_v32_v32_vmpsX_p (16, 1, vIn, vExponentValue, vIn3, 0, LOW, vRes2,
            vecPred);

                 IN_VPR last operand is relevant only for
            1.
                 vsqaxe_v32_v32_v32_v32_v32_vmpsX_p version.
Comments         This intrinsic returns two results. The first result variable should be placed to
            2.   the left of the = sign (lvalue). The second result variable should be passed as
                 an additional parameter (RES2_V32).


Main table → Multiplication → Absolute Square → Vector Complex Absolute Square with
Exponent
