# Multiplication → Multiply-Subtract → Semi-Complex 16x32 with Exponent

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Multiplication → Multiply-Subtract → Semi-Complex 16x32 with Exponent

Semi-Complex 16x32 with Exponent

Semi-Complex 16x32 with Exponent
Performs semi-complex multiply-subtract with exponent between a complex number and a real
number. The complex source consists of real 16-bit part and imaginary 16-bit part. The real
source consists of real 32-bit part. Each of the real and the imaginary products are subtractd with
the 40-bit destination respectively.
Available Switches
           Number of atomic operations. An atomic operation is defined as a semi-complex
           multiply-subtract 16x32 with exponent operation.Used for two vector destinations,
Ohop
           while the first vector destination is always fully written, the second vector destination
           number of atomic operation is set by Ohop. 5op œ Ohop œ 8op
           Number of atomic operations. An atomic operation is defined as a semi-complex
Qop
           multiply-subtract 16x32 with exponent operation.
conj       conjugate complex operation
vmpsX Selects the VMSNX and VPSX set within modv0 or modv2 mode registers.
Intrinsic Names
vmsuwlxre_v32_v32_v32_v40_v40_conj
vmsuwlxre_v32_v32_v32_v40_v40_conj_vmpsX
vmsuwlxre_v32_v32_v32_v40_v40
vmsuwlxre_v32_v32_v32_v40_v40_vmpsX
vmsuwlxre_v32_v32_v32_v40_conj
vmsuwlxre_v32_v32_v32_v40_conj_vmpsX
vmsuwlxre_v32_v32_v32_v40
vmsuwlxre_v32_v32_v32_v40_vmpsX
Instruction details in the instruction set specification
Intrinsic     vmsuwlxre_v32_v32_v32_v40_v40_conj[_p]
name
Spec syntax   vmsuwlxre {Ohop [,conj][,vmpsX]} vx[X], vy[Y], vv[V]p, voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    OHOP           uint8     5..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             2

              4    IN2_V32        vec_t                      Input vector operand

5    IN2_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             4
Operands      6    IN3_V32        vec_t                      Input vector operand

              7    IN3_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             6

              8    IN3_PART       uint8     LOW,HIGH         Word part which is used for operand 6
              9    IN4_V40        vec40_t                    Output vector operand
              10   RES2_V40       vec40_t                    Output vector result operand
              11   IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec40_t vRes1;
C example     vec40_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vmsuwlxre_v32_v32_v32_v40_v40_conj_p (8, vIn, 0, vIn2, 0, vIn3, 0, LOW, vRes1, vRes2,
              vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vmsuwlxre_v32_v32_v32_v40_v40_conj_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).


Main table → Multiplication → Multiply-Subtract → Semi-Complex 16x32 with Exponent
Intrinsic     vmsuwlxre_v32_v32_v32_v40_v40_conj_vmpsX[_p]
name
Spec syntax   vmsuwlxre {Ohop [,conj][,vmpsX]} vx[X], vy[Y], vv[V]p, voz1[0], voz2[0], ?vprX

Return type   vec40_t

Operands      1    OHOP           uint8     5..8             Number of atomic operations
                                                            Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand

              4    IN1_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            3

              5    IN2_V32        vec_t                     Input vector operand

              6    IN2_OFST       uint8     0..7

Offset for the first DW used from operand
                                                            5

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
              vRes1 = vmsuwlxre_v32_v32_v32_v40_v40_conj_vmpsX_p (8, 1, vIn, 0, vIn2, 0, vIn3, 0, LOW, vRes1,
              vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vmsuwlxre_v32_v32_v32_v40_v40_conj_vmpsX_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).


Main table → Multiplication → Multiply-Subtract → Semi-Complex 16x32 with Exponent
Intrinsic     vmsuwlxre_v32_v32_v32_v40_v40[_p]
name
Spec syntax   vmsuwlxre {Ohop [,conj][,vmpsX]} vx[X], vy[Y], vv[V]p, voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    OHOP           uint8     5..8            Number of atomic operations

Operands
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0..7            Offset for the first DW used from operand
                                                            2
              4    IN2_V32        vec_t                      Input vector operand

              5    IN2_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             4

              6    IN3_V32        vec_t                      Input vector operand

7    IN3_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             6

              8    IN3_PART       uint8     LOW,HIGH         Word part which is used for operand 6
              9    IN4_V40        vec40_t                    Output vector operand
              10   RES2_V40       vec40_t                    Output vector result operand
              11   IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec40_t vRes1;
C example     vec40_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vmsuwlxre_v32_v32_v32_v40_v40_p (8, vIn, 0, vIn2, 0, vIn3, 0, LOW, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vmsuwlxre_v32_v32_v32_v40_v40_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).


Main table → Multiplication → Multiply-Subtract → Semi-Complex 16x32 with Exponent
Intrinsic     vmsuwlxre_v32_v32_v32_v40_v40_vmpsX[_p]
name
Spec syntax   vmsuwlxre {Ohop [,conj][,vmpsX]} vx[X], vy[Y], vv[V]p, voz1[0], voz2[0], ?vprX

Return type   vec40_t

              1    OHOP           uint8     5..8             Number of atomic operations
                                                             Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                             modv0/modv2 mode registers
              3    IN1_V32        vec_t                      Input vector operand

Operands      4    IN1_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             3

              5    IN2_V32        vec_t                      Input vector operand

              6    IN2_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             5

              7    IN3_V32        vec_t                      Input vector operand
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
C example   vec40_t vRes2;
            vprex_t vecPred;
            ...
            vRes1 = vmsuwlxre_v32_v32_v32_v40_v40_vmpsX_p (8, 1, vIn, 0, vIn2, 0, vIn3, 0, LOW, vRes1, vRes2,
            vecPred);

                 IN_VPR last operand is relevant only for
            1.
                 vmsuwlxre_v32_v32_v32_v40_v40_vmpsX_p version.
Comments         This intrinsic returns two results. The first result variable should be placed to
            2.   the left of the = sign (lvalue). The second result variable should be passed as
                 an additional parameter (RES2_V40).


Main table → Multiplication → Multiply-Subtract → Semi-Complex 16x32 with Exponent
Intrinsic     vmsuwlxre_v32_v32_v32_v40_conj[_p]
name
Spec syntax   vmsuwlxre {Qop [,conj][,vmpsX]} vx[X], vy[Y], vv[V]p, voz[0], ?vprX

Return type   vec40_t

              1    QOP             uint8     1..4             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand

              3    IN1_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
                                                              2

              4    IN2_V32         vec_t                      Input vector operand

              5    IN2_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
                                                              4
Operands
              6    IN3_V32         vec_t                      Input vector operand

              7    IN3_OFST        uint8     0..7             Offset for the first DW used from operand
                                                              6

              8    IN3_PART        uint8     LOW,HIGH         Word part which is used for operand 6
              9    IN4_V40         vec40_t                    Output vector operand

10   IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
C example     vec40_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmsuwlxre_v32_v32_v32_v40_conj_p (4, vIn, 0, vIn2, 0, vIn3, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsuwlxre_v32_v32_v32_v40_conj_p version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 16x32 with Exponent
Intrinsic     vmsuwlxre_v32_v32_v32_v40_conj_vmpsX[_p]
name
Spec syntax   vmsuwlxre {Qop [,conj][,vmpsX]} vx[X], vy[Y], vv[V]p, voz[0], ?vprX

Return type   vec40_t

              1    QOP             uint8     1..4             Number of atomic operations
                                                              Selects the VMSNX and VPSX set within
              2    VMPSX           uint8     0,1
                                                              modv0/modv2 mode registers
Operands
              3    IN1_V32         vec_t                      Input vector operand

              4    IN1_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
                                                              3
              5    IN2_V32        vec_t                      Input vector operand

              6    IN2_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             5

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
              vRes = vmsuwlxre_v32_v32_v32_v40_conj_vmpsX_p (4, 1, vIn, 0, vIn2, 0, vIn3, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.

vmsuwlxre_v32_v32_v32_v40_conj_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 16x32 with Exponent
Intrinsic     vmsuwlxre_v32_v32_v32_v40[_p]
name
Spec syntax   vmsuwlxre {Qop [,conj][,vmpsX]} vx[X], vy[Y], vv[V]p, voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             2

              4    IN2_V32        vec_t                      Input vector operand

              5    IN2_OFST       uint8     0..7             Offset for the first DW used from operand
Operands                                                     4

              6    IN3_V32        vec_t                      Input vector operand

              7    IN3_OFST       uint8     0..7             Offset for the first DW used from operand
                                                             6

              8    IN3_PART       uint8     LOW,HIGH         Word part which is used for operand 6
              9    IN4_V40        vec40_t                    Output vector operand
              10   IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
C example     vec_t vIn2;
              vec_t vIn3;
              vec40_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmsuwlxre_v32_v32_v32_v40_p (4, vIn, 0, vIn2, 0, vIn3, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for vmsuwlxre_v32_v32_v32_v40_p
Comments      1.
                   version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 16x32 with Exponent
Intrinsic     vmsuwlxre_v32_v32_v32_v40_vmpsX[_p]
name
Spec syntax   vmsuwlxre {Qop [,conj][,vmpsX]} vx[X], vy[Y], vv[V]p, voz[0], ?vprX

Return type   vec40_t

              1    QOP             uint8     1..4             Number of atomic operations
                                                              Selects the VMSNX and VPSX set within
              2    VMPSX           uint8     0,1
                                                              modv0/modv2 mode registers
              3    IN1_V32         vec_t                      Input vector operand

              4    IN1_OFST        uint8     0..7

Offset for the first DW used from operand
                                                              3

              5    IN2_V32         vec_t                      Input vector operand
Operands      6    IN2_OFST        uint8     0..7             Offset for the first DW used from operand
                                                              5

              7    IN3_V32         vec_t                      Input vector operand

              8    IN3_OFST        uint8     0..7             Offset for the first DW used from operand
                                                              7

              9    IN3_PART        uint8     LOW,HIGH         Word part which is used for operand 7
              10   IN4_V40         vec40_t                    Output vector operand
              11   IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
C example     vec40_t vRes;
              vprex_t vecPred;
              ...
              vRes = vmsuwlxre_v32_v32_v32_v40_vmpsX_p (4, 1, vIn, 0, vIn2, 0, vIn3, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsuwlxre_v32_v32_v32_v40_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Semi-Complex 16x32 with Exponent
