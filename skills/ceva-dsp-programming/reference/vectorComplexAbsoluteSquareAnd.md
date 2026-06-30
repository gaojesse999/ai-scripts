# Multiplication → Absolute Square → Vector Complex Absolute Square and

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Multiplication → Absolute Square → Vector Complex Absolute Square and
Pack

Vector Complex Absolute Square and Pack

Vector Complex Absolute Square and Pack
Performs two operations of squaring of complex absolute. Each complex source is 32-bits wide

(16-bit real and 16-bit imaginary). The products are packed and written to 40-bit destinations.
Available Switches
              Number of atomic operations. An atomic operation is defined as two Complex
Ohop
              Absolute Square operation. 5op ≤ Ohop ≤ 8op
vmpsX         Selects the VMSNX and VPSX set within modv0 or modv2 mode registers.
Intrinsic Names
vsqaxp_v32_v32_v32
vsqaxp_v32_v32_v32_vmpsX
vsqaxp_v32_v32
vsqaxp_v32_v32_vmpsX
Instruction details in the instruction set specification
Intrinsic     vsqaxp_v32_v32_v32[_p]
name
Spec syntax   vsqaxp {Ohop [,vmpsX]} vx[0], vy[0], vz[0], ?vprX

Return type   vec_t

              1    OHOP            uint8     5..8             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand
Operands
              3    IN2_V32         vec_t                      Input vector operand
              4    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vsqaxp_v32_v32_v32_p (8, vIn, vIn2, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vsqaxp_v32_v32_v32_p version.


Main table → Multiplication → Absolute Square → Vector Complex Absolute Square and
Pack
Intrinsic     vsqaxp_v32_v32_v32_vmpsX[_p]
name
Spec syntax   vsqaxp {Ohop [,vmpsX]} vx[0], vy[0], vz[0], ?vprX

Return type   vec_t

              1    OHOP            uint8     5..8             Number of atomic operations

              2
                                                              Selects the VMSNX and VPSX set within
                   VMPSX           uint8     0,1
                                                              modv0/modv2 mode registers
Operands      3    IN1_V32         vec_t                      Input vector operand
              4    IN2_V32         vec_t                      Input vector operand
              5    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vsqaxp_v32_v32_v32_vmpsX_p (8, 1, vIn, vIn2, vecPred);

                   IN_VPR last operand is relevant only for vsqaxp_v32_v32_v32_vmpsX_p
Comments      1.
                   version.

Main table → Multiplication → Absolute Square → Vector Complex Absolute Square and
Pack
Intrinsic     vsqaxp_v32_v32[_p]
name
Spec syntax   vsqaxp {Qop [,vmpsX]} vx[X], vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4                Number of atomic operations
              2    IN1_V32         vec_t                         Input vector operand

              3    IN1_OFST        uint8     0,4
                                                                 Offset for the first DW used from operand
Operands                                                         2

                                                                 Offset for the first DW used from the
              4    OUT_OFST        uint8     0,4
                                                                 result operand
              5    IN_VPR          vprex_t                       Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vsqaxp_v32_v32_p (4, vIn, 0, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vsqaxp_v32_v32_p version.


Main table → Multiplication → Absolute Square → Vector Complex Absolute Square and
Pack
Intrinsic     vsqaxp_v32_v32_vmpsX[_p]
name
Spec syntax   vsqaxp {Qop [,vmpsX]} vx[X], vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4                Number of atomic operations

              2
                                                                 Selects the VMSNX and VPSX set within
                   VMPSX           uint8     0,1
                                                                 modv0/modv2 mode registers
              3    IN1_V32         vec_t                         Input vector operand
Operands                                                         Offset for the first DW used from operand
              4    IN1_OFST        uint8     0,4
                                                                 3

                                                                 Offset for the first DW used from the
              5    OUT_OFST        uint8     0,4
                                                                 result operand
              6    IN_VPR          vprex_t                       Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...

vRes = vsqaxp_v32_v32_vmpsX_p (4, 1, vIn, 0, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vsqaxp_v32_v32_vmpsX_p
                version.


Main table → Multiplication → Absolute Square → Vector Complex Absolute Square and
Pack

Main table → Multiplication → Absolute Square → Vector Complex Absolute Square and
Pack with Exponent

Vector Complex Absolute Square and Pack with Exponent

Vector Complex Absolute Square and Pack with Exponent
Performs two operations of squaring of complex absolute. Each complex source is 32-bits wide
(16-bit real and 16-bit imaginary). The third source is the exponent. The products are packed and
written to 40-bit destinations.
Available Switches
           Number of atomic operations. An atomic operation is defined as two Complex Absolute
           Square operation.Used for two vector destinations, while the first vector destination is
Ohop
           always fully written, the second vector destination number of atomic operation is set by
           Ohop. 5op œ Ohop œ 8op
vmpsX Selects the VMSNX and VPSX set within modv0 or modv2 mode registers.
Intrinsic Names
vsqaxep_v32_v32_v32_v32
vsqaxep_v32_v32_v32_v32_vmpsX
vsqaxep_v32_v32_v32
vsqaxep_v32_v32_v32_vmpsX
Instruction details in the instruction set specification
Intrinsic     vsqaxep_v32_v32_v32_v32[_p]
name
Spec syntax   vsqaxep {Ohop [,vmpsX]} vx[X], vy[Y], vv[V]p, vz[0], ?vprX

Return type   vec_t

              1    OHOP            uint8     5..8            Number of atomic operations
              2    IN1_V32         vec_t                     Input vector operand

              3    IN1_OFST        uint8     0,4
                                                             Offset for the first DW used from operand
                                                             2

              4    IN2_V32         vec_t                     Input vector operand

Operands      5    IN2_OFST        uint8     0,4
                                                             Offset for the first DW used from operand
                                                             4

              6    IN3_V32         vec_t                     Input vector operand

              7    IN3_OFST        uint8     0,4             Offset for the first DW used from operand
                                                             6

              8    IN3_PART        uint8     LOW,HIGH        Word part which is used for operand 6

9    IN_VPR          vprex_t                   Vector predicate operand
              vec_t vExponentValue;
              vec_t vIn;
              vec_t vIn3;
C example     vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vsqaxep_v32_v32_v32_v32_p (8, vIn, 0, vExponentValue, 0, vIn3, 0, LOW, vecPred);

                   IN_VPR last operand is relevant only for vsqaxep_v32_v32_v32_v32_p
Comments      1.
                   version.


Main table → Multiplication → Absolute Square → Vector Complex Absolute Square and
Pack with Exponent
Intrinsic     vsqaxep_v32_v32_v32_v32_vmpsX[_p]
name
Spec syntax   vsqaxep {Ohop [,vmpsX]} vx[X], vy[Y], vv[V]p, vz[0], ?vprX

Return type   vec_t

              1    OHOP            uint8     5..8            Number of atomic operations
                                                             Selects the VMSNX and VPSX set within
              2    VMPSX           uint8     0,1
                                                             modv0/modv2 mode registers
Operands
              3    IN1_V32         vec_t                     Input vector operand

              4    IN1_OFST        uint8     0,4
                                                             Offset for the first DW used from operand
                                                             3
            5    IN2_V32        vec_t                      Input vector operand

            6    IN2_OFST       uint8     0,4              Offset for the first DW used from operand
                                                           5

            7    IN3_V32        vec_t                      Input vector operand

            8    IN3_OFST       uint8     0,4              Offset for the first DW used from operand
                                                           7

            9    IN3_PART       uint8     LOW,HIGH         Word part which is used for operand 7
            10   IN_VPR         vprex_t                    Vector predicate operand
            vec_t vExponentValue;
            vec_t vIn;
            vec_t vIn3;
C example   vec_t vRes;
            vprex_t vecPred;
            ...
            vRes = vsqaxep_v32_v32_v32_v32_vmpsX_p (8, 1, vIn, 0, vExponentValue, 0, vIn3, 0, LOW, vecPred);

                 IN_VPR last operand is relevant only for
Comments    1.
                 vsqaxep_v32_v32_v32_v32_vmpsX_p version.


Main table → Multiplication → Absolute Square → Vector Complex Absolute Square and

Pack with Exponent
Intrinsic     vsqaxep_v32_v32_v32[_p]
name
Spec syntax   vsqaxep {Qop [,vmpsX]} vx[X], vv[V]p, vz[0], ?vprX

Return type   vec_t

              1    QOP            uint8     1..4             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0,4
                                                             Offset for the first DW used from operand
                                                             2

              4    IN2_V32        vec_t                      Input vector operand
Operands                                                     Offset for the first DW used from operand
              5    IN2_OFST       uint8     0,4
                                                             4

              6    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 4
                                                             Offset for the first DW used from the
              7    OUT_OFST       uint8     0,4
                                                             result operand
              8    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vExponentValue;
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vsqaxep_v32_v32_v32_p (4, vIn, 0, vExponentValue, 0, LOW, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vsqaxep_v32_v32_v32_p version.


Main table → Multiplication → Absolute Square → Vector Complex Absolute Square and
Pack with Exponent
Intrinsic     vsqaxep_v32_v32_v32_vmpsX[_p]
name
Spec syntax   vsqaxep {Qop [,vmpsX]} vx[X], vv[V]p, vz[0], ?vprX

Return type   vec_t

              1    QOP            uint8     1..4             Number of atomic operations
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
                                                           Offset for the first DW used from the
            8    OUT_OFST       uint8     0,4
                                                           result operand
            9    IN_VPR         vprex_t                    Vector predicate operand
            vec_t vExponentValue;
            vec_t vIn;
            vec_t vRes;
C example   vprex_t vecPred;
            ...
            vRes = vsqaxep_v32_v32_v32_vmpsX_p (4, 1, vIn, 0, vExponentValue, 0, LOW, 0, vecPred);

                 IN_VPR last operand is relevant only for vsqaxep_v32_v32_v32_vmpsX_p
Comments    1.
                 version.


Main table → Multiplication → Absolute Square → Vector Complex Absolute Square and
Pack with Exponent
