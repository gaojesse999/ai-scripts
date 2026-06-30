# Multiplication → Multiply → 16x16 and Pack into Bytes

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Multiplication → Multiply → 16x16 and Pack into Bytes

16x16 and Pack into Bytes

16x16 and Pack into Bytes
Performs two multiplication and pack operations. Each source is 16-bit. each destination is 8-bit
and are packed into 20-bit or 16-bit determined by the vector register type.
Available Switches
      Number of atomic operations. An atomic operation is defined as two 16x16 multiply
DZNop and pack operations. Writes to one vector destination according to DZNop switch. 1op '
      DZNop ' 12op
            Number of atomic operations. An atomic operation is defined as two 16x16 multiply
Hop         and pack operations. Writes to one vector destination according to Hop switch. 1op ≤
            Hop ≤ 16op
            Number of atomic operations. An atomic operation is defined as two 16x16 multiply
Oop         and pack operations. Writes to one vector destination according to Hop switch. 1op ≤
            Oop ≤ 8op
            Number of atomic operations. An atomic operation is defined as two 16x16 multiply
Qop         and pack operations. Writes to one vector destination according to Hop switch. 1op ≤
            Oop ≤ 4op
bpsk        Each word in the vv[V]p source register is replicated according to modulation type:
qam64 Each word in the vv[V]p source register is replicated 6 times
            Each word in the vv[V]p source register is replicated according to QAM type defined-
qamX
            X is replaced with 256, 64 and 16 as follows:
qpsk        Each word in the vv[V]p source register is replicated according to modulation type:
vmpsX Selects the VMSNX and VPSX set within modv0 or modv2 mode registers.
Intrinsic Names
vmpybp_v32_v32_v32_bpsk

vmpybp_v32_v32_v32_bpsk_vmpsX
vmpybp_v32_v32_v32_qpsk
vmpybp_v32_v32_v32_qpsk_vmpsX
vmpybp_v32_v32_v32_v32_DZNop_qam64
vmpybp_v32_v32_v32_v32_DZNop_qam64_vmpsX
vmpybp_v32_v32_v32_v32_qam16
vmpybp_v32_v32_v32_v32_qam16_vmpsX
vmpybp_v32_v32_v32_v32_qam256
vmpybp_v32_v32_v32_v32_qam256_vmpsX
Instruction details in the instruction set specification
Intrinsic     vmpybp_v32_v32_v32_bpsk[_p]
name
Spec syntax   vmpybp {Qop, bpsk [,vmpsX]} vx[X]p, vv[V]p, vz[0], ?vprX

Return type   vec_t

              1    QOP            uint8     1..4            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0,4
                                                            Offset for the first DW used from operand
                                                            2

              4    IN1_PART       uint8     LOW,HIGH        Word part which is used for operand 2
              5    IN2_V32        vec_t                     Input vector operand
Operands
              6    IN2_OFST       uint8     0,4             Offset for the first DW used from operand
                                                            5

              7    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 5
                                                            Offset for the first DW used from the
              8    OUT_OFST       uint8     0,4
                                                            result operand
              9    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmpybp_v32_v32_v32_bpsk_p (4, vIn, 0, LOW, vIn2, 0, LOW, 0, vecPred);

                   IN_VPR last operand is relevant only for vmpybp_v32_v32_v32_bpsk_p
Comments      1.
                   version.


Main table → Multiplication → Multiply → 16x16 and Pack into Bytes
Intrinsic     vmpybp_v32_v32_v32_bpsk_vmpsX[_p]
name
Spec syntax   vmpybp {Qop, bpsk [,vmpsX]} vx[X]p, vv[V]p, vz[0], ?vprX

Return type   vec_t

              1    QOP            uint8     1..4            Number of atomic operations
                                                            Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1

modv0/modv2 mode registers
Operands      3    IN1_V32        vec_t                     Input vector operand

              4    IN1_OFST       uint8     0,4             Offset for the first DW used from operand
                                                            3

              5    IN1_PART       uint8     LOW,HIGH        Word part which is used for operand 3
             6    IN2_V32        vec_t                    Input vector operand

             7    IN2_OFST       uint8     0,4            Offset for the first DW used from operand
                                                          6

             8    IN2_PART       uint8     LOW,HIGH       Word part which is used for operand 6
                                                          Offset for the first DW used from the
             9    OUT_OFST       uint8     0,4
                                                          result operand
             10   IN_VPR         vprex_t                  Vector predicate operand
             vec_t vIn;
             vec_t vIn2;
             vec_t vRes;
C example    vprex_t vecPred;
             ...
             vRes = vmpybp_v32_v32_v32_bpsk_vmpsX_p (4, 1, vIn, 0, LOW, vIn2, 0, LOW, 0, vecPred);

                  IN_VPR last operand is relevant only for
Comments     1.
                  vmpybp_v32_v32_v32_bpsk_vmpsX_p version.


Main table → Multiplication → Multiply → 16x16 and Pack into Bytes
Intrinsic     vmpybp_v32_v32_v32_qpsk[_p]
name
Spec syntax   vmpybp {Oop, qpsk [,vmpsX]} vx[X]p, vv[V]p, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0,4
                                                            Offset for the first DW used from operand
                                                            2

              4    IN1_PART       uint8     LOW,HIGH        Word part which is used for operand 2
              5    IN2_V32        vec_t                     Input vector operand
Operands
              6    IN2_OFST       uint8     0,4             Offset for the first DW used from operand
                                                            5

              7    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 5

Offset for the first DW used from the
              8    OUT_OFST       uint8     0,4
                                                            result operand
              9    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmpybp_v32_v32_v32_qpsk_p (8, vIn, 0, LOW, vIn2, 0, LOW, 0, vecPred);

                   IN_VPR last operand is relevant only for vmpybp_v32_v32_v32_qpsk_p
Comments      1.
                   version.


Main table → Multiplication → Multiply → 16x16 and Pack into Bytes
Intrinsic     vmpybp_v32_v32_v32_qpsk_vmpsX[_p]
name
Spec syntax   vmpybp {Oop, qpsk [,vmpsX]} vx[X]p, vv[V]p, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
                                                            Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
Operands      3    IN1_V32        vec_t                     Input vector operand

              4    IN1_OFST       uint8     0,4             Offset for the first DW used from operand
                                                            3

              5    IN1_PART       uint8     LOW,HIGH        Word part which is used for operand 3
             6    IN2_V32        vec_t                    Input vector operand

             7    IN2_OFST       uint8     0,4            Offset for the first DW used from operand
                                                          6

             8    IN2_PART       uint8     LOW,HIGH       Word part which is used for operand 6
                                                          Offset for the first DW used from the
             9    OUT_OFST       uint8     0,4
                                                          result operand
             10   IN_VPR         vprex_t                  Vector predicate operand
             vec_t vIn;
             vec_t vIn2;
             vec_t vRes;
C example    vprex_t vecPred;
             ...
             vRes = vmpybp_v32_v32_v32_qpsk_vmpsX_p (8, 1, vIn, 0, LOW, vIn2, 0, LOW, 0, vecPred);

                  IN_VPR last operand is relevant only for
Comments     1.
                  vmpybp_v32_v32_v32_qpsk_vmpsX_p version.

Main table → Multiplication → Multiply → 16x16 and Pack into Bytes
Intrinsic     vmpybp_v32_v32_v32_v32_DZNop_qam64[_p]
name
Spec syntax   vmpybp {DZNop, qam64 [,vmpsX]} vx[X]p, vy[Y]p, vv[V]p, vz[0], ?vprX

Return type   vec_t

              1    DZNOP         uint8     1..12          Number of atomic operations
              2    IN1_V32       vec_t                    Input vector operand

              3    IN1_OFST      uint8     0,4
                                                          Offset for the first DW used from operand
                                                          2

              4    IN1_PART      uint8     LOW,HIGH       Word part which is used for operand 2
              5    IN2_V32       vec_t                    Input vector operand

Operands      6    IN2_OFST      uint8     0,4            Offset for the first DW used from operand
                                                          5

              7    IN2_PART      uint8     LOW,HIGH       Word part which is used for operand 5
              8    IN3_V32       vec_t                    Input vector operand

              9    IN3_OFST      uint8     0,4            Offset for the first DW used from operand
                                                          8

              10   IN3_PART      uint8     LOW,HIGH       Word part which is used for operand 8
              11   IN_VPR        vprex_t                  Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmpybp_v32_v32_v32_v32_DZNop_qam64_p (12, vIn, 0, LOW, vIn2, 0, LOW, vIn3, 0, LOW,
              vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmpybp_v32_v32_v32_v32_DZNop_qam64_p version.


Main table → Multiplication → Multiply → 16x16 and Pack into Bytes
Intrinsic     vmpybp_v32_v32_v32_v32_DZNop_qam64_vmpsX[_p]
name
Spec syntax   vmpybp {DZNop, qam64 [,vmpsX]} vx[X]p, vy[Y]p, vv[V]p, vz[0], ?vprX

Return type   vec_t

              1    DZNOP         uint8     1..12          Number of atomic operations
                                                          Selects the VMSNX and VPSX set within
Operands      2    VMPSX         uint8     0,1
                                                          modv0/modv2 mode registers

3    IN1_V32       vec_t                    Input vector operand
             4    IN1_OFST      uint8     0,4           Offset for the first DW used from operand
                                                        3

             5    IN1_PART      uint8     LOW,HIGH      Word part which is used for operand 3
             6    IN2_V32       vec_t                   Input vector operand

             7    IN2_OFST      uint8     0,4           Offset for the first DW used from operand
                                                        6

             8    IN2_PART      uint8     LOW,HIGH      Word part which is used for operand 6
             9    IN3_V32       vec_t                   Input vector operand

             10   IN3_OFST      uint8     0,4
                                                        Offset for the first DW used from operand
                                                        9

             11   IN3_PART      uint8     LOW,HIGH      Word part which is used for operand 9
             12   IN_VPR        vprex_t                 Vector predicate operand
             vec_t vIn;
             vec_t vIn2;
             vec_t vIn3;
             vec_t vRes;
C example    vprex_t vecPred;
             ...
             vRes = vmpybp_v32_v32_v32_v32_DZNop_qam64_vmpsX_p (12, 1, vIn, 0, LOW, vIn2, 0, LOW, vIn3,
             0, LOW, vecPred);

                  IN_VPR last operand is relevant only for
Comments     1.
                  vmpybp_v32_v32_v32_v32_DZNop_qam64_vmpsX_p version.


Main table → Multiplication → Multiply → 16x16 and Pack into Bytes
Intrinsic     vmpybp_v32_v32_v32_v32_qam16[_p]
name
Spec syntax   vmpybp {Hop, qam16 [,vmpsX]} vx[X]p, vy[Y]p, vv[V]p, vz[0], ?vprX

Return type   vec_t

              1    HOP            uint8     1..16          Number of atomic operations
              2    IN1_V32        vec_t                    Input vector operand

              3    IN1_OFST       uint8     0,4
                                                           Offset for the first DW used from operand
                                                           2

              4    IN1_PART       uint8     LOW,HIGH       Word part which is used for operand 2
              5    IN2_V32        vec_t                    Input vector operand

Operands      6    IN2_OFST       uint8     0,4            Offset for the first DW used from operand
                                                           5

7    IN2_PART       uint8     LOW,HIGH       Word part which is used for operand 5
              8    IN3_V32        vec_t                    Input vector operand

              9    IN3_OFST       uint8     0,4            Offset for the first DW used from operand
                                                           8

              10   IN3_PART       uint8     LOW,HIGH       Word part which is used for operand 8
              11   IN_VPR         vprex_t                  Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
C example     vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmpybp_v32_v32_v32_v32_qam16_p (16, vIn, 0, LOW, vIn2, 0, LOW, vIn3, 0, LOW, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmpybp_v32_v32_v32_v32_qam16_p version.


Main table → Multiplication → Multiply → 16x16 and Pack into Bytes
Intrinsic     vmpybp_v32_v32_v32_v32_qam16_vmpsX[_p]
name
Spec syntax   vmpybp {Hop, qam16 [,vmpsX]} vx[X]p, vy[Y]p, vv[V]p, vz[0], ?vprX

Return type   vec_t

              1    HOP            uint8     1..16          Number of atomic operations
                                                           Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
Operands                                                   modv0/modv2 mode registers
              3    IN1_V32        vec_t                    Input vector operand
              4    IN1_OFST       uint8     0,4            Offset for the first DW used from operand
                                                          3

              5    IN1_PART      uint8     LOW,HIGH       Word part which is used for operand 3
              6    IN2_V32       vec_t                    Input vector operand

              7    IN2_OFST      uint8     0,4            Offset for the first DW used from operand
                                                          6

              8    IN2_PART      uint8     LOW,HIGH       Word part which is used for operand 6
              9    IN3_V32       vec_t                    Input vector operand

              10   IN3_OFST      uint8     0,4
                                                          Offset for the first DW used from operand
                                                          9

11   IN3_PART      uint8     LOW,HIGH       Word part which is used for operand 9
              12   IN_VPR        vprex_t                  Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmpybp_v32_v32_v32_v32_qam16_vmpsX_p (16, 1, vIn, 0, LOW, vIn2, 0, LOW, vIn3, 0, LOW,
              vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmpybp_v32_v32_v32_v32_qam16_vmpsX_p version.


Main table → Multiplication → Multiply → 16x16 and Pack into Bytes
Intrinsic     vmpybp_v32_v32_v32_v32_qam256[_p]
name
Spec syntax   vmpybp {Hop, qam256 [,vmpsX]} vx[X]p, vy[Y]p, vv[V]p, vz[0], ?vprX

Return type   vec_t

              1    HOP           uint8     1..16          Number of atomic operations
              2    IN1_V32       vec_t                    Input vector operand

              3    IN1_OFST      uint8     0,4
                                                          Offset for the first DW used from operand
                                                          2

              4    IN1_PART      uint8     LOW,HIGH       Word part which is used for operand 2

Operands
              5    IN2_V32       vec_t                    Input vector operand

              6    IN2_OFST      uint8     0,4            Offset for the first DW used from operand
                                                          5

              7    IN2_PART      uint8     LOW,HIGH       Word part which is used for operand 5
              8    IN3_V32       vec_t                    Input vector operand

              9    IN3_OFST      uint8     0,4            Offset for the first DW used from operand
                                                          8
              10   IN3_PART       uint8     LOW,HIGH       Word part which is used for operand 8
              11   IN_VPR         vprex_t                  Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
C example     vec_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmpybp_v32_v32_v32_v32_qam256_p (16, vIn, 0, LOW, vIn2, 0, LOW, vIn3, 0, LOW, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmpybp_v32_v32_v32_v32_qam256_p version.

Main table → Multiplication → Multiply → 16x16 and Pack into Bytes
Intrinsic     vmpybp_v32_v32_v32_v32_qam256_vmpsX[_p]
name
Spec syntax   vmpybp {Hop, qam256 [,vmpsX]} vx[X]p, vy[Y]p, vv[V]p, vz[0], ?vprX

Return type   vec_t

              1    HOP            uint8     1..16          Number of atomic operations

              2
                                                           Selects the VMSNX and VPSX set within
                   VMPSX          uint8     0,1
                                                           modv0/modv2 mode registers
              3    IN1_V32        vec_t                    Input vector operand

              4    IN1_OFST       uint8     0,4
                                                           Offset for the first DW used from operand
                                                           3

              5    IN1_PART       uint8     LOW,HIGH       Word part which is used for operand 3
              6    IN2_V32        vec_t                    Input vector operand
Operands
              7    IN2_OFST       uint8     0,4            Offset for the first DW used from operand
                                                           6

              8    IN2_PART       uint8     LOW,HIGH       Word part which is used for operand 6
              9    IN3_V32        vec_t                    Input vector operand

              10   IN3_OFST       uint8     0,4            Offset for the first DW used from operand
                                                           9

              11   IN3_PART       uint8     LOW,HIGH       Word part which is used for operand 9
              12   IN_VPR         vprex_t                  Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmpybp_v32_v32_v32_v32_qam256_vmpsX_p (16, 1, vIn, 0, LOW, vIn2, 0, LOW, vIn3, 0, LOW,
              vecPred);
                  IN_VPR last operand is relevant only for
Comments     1.
                  vmpybp_v32_v32_v32_v32_qam256_vmpsX_p version.


Main table → Multiplication → Multiply → 16x16 and Pack into Bytes
