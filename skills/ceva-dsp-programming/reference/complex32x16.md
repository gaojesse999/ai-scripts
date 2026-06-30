# Multiplication → Multiply-Subtract → Complex 32x16

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Multiplication → Multiply-Subtract → Complex 32x16

Complex 32x16

Complex 32x16
Performs complex multiply-subtract between two complex numbers. The first complex source
consists of real 32-bit part and imaginary 32-bit part. The second complex source consists of real
16-bit part and imaginary 16-bit part. Each of the real and the imaginary products are
accumulated with the 40-bit destination respectively.
Available Switches
           Number of atomic operations. An atomic operation is defined as a complex multiply-
Qop
           subtract double precision operation. 1op ≤ Qop ≤ 4op
SHX        SHX is a pseudo-switch which is replaced by either >>8 or <
Switch     Effect
conj       conjugate complex operation on 16-bit complex source
conj32     conjugate complex operation on 32-bit complex source
prt        Indicates partial vmsulwx operation
           Swap between real and image second source complex multiplication behavior. When
sx         used, vy part represent now the imaginary part. The default is vy as real part
           multiplied by two vx[X] double-words.
vmpsX      Selects the VMSNX and VPSX set within modv0 or modv2 mode registers.
Intrinsic Names
vmsulwx_v32_v32_v40_prt_SHFL16_conj
vmsulwx_v32_v32_v40_prt_SHFL16
vmsulwx_v32_v32_v40_prt_SHFL16_sx_conj
vmsulwx_v32_v32_v40_prt_SHFL16_sx
vmsulwx_v32_v32_v40_prt_SHFR8_conj
vmsulwx_v32_v32_v40_prt_SHFR8
vmsulwx_v32_v32_v40_prt_SHFR8_sx_conj
vmsulwx_v32_v32_v40_prt_SHFR8_sx
vmsulwx_v32_v32_v40_conj32
vmsulwx_v32_v32_v40_conj32_vmpsX
vmsulwx_v32_v32_v40_conj
vmsulwx_v32_v32_v40_conj_vmpsX
vmsulwx_v32_v32_v40
vmsulwx_v32_v32_v40_vmpsX
vmsulwx_v32_v32_v40_prt_conj
vmsulwx_v32_v32_v40_prt
vmsulwx_v32_v32_v40_prt_sx_conj
vmsulwx_v32_v32_v40_prt_sx
vmsulwx_v32_v32_v40_SHFL16_conj32
vmsulwx_v32_v32_v40_SHFL16_conj32_vmpsX
vmsulwx_v32_v32_v40_SHFL16_conj
vmsulwx_v32_v32_v40_SHFL16_conj_vmpsX
vmsulwx_v32_v32_v40_SHFL16
vmsulwx_v32_v32_v40_SHFL16_vmpsX
vmsulwx_v32_v32_v40_SHFR8_conj32

vmsulwx_v32_v32_v40_SHFR8_conj32_vmpsX
vmsulwx_v32_v32_v40_SHFR8_conj
vmsulwx_v32_v32_v40_SHFR8_conj_vmpsX
vmsulwx_v32_v32_v40_SHFR8
vmsulwx_v32_v32_v40_SHFR8_vmpsX
Instruction details in the instruction set specification
Intrinsic     vmsulwx_v32_v32_v40_prt_SHFL16_conj[_p]
name
Spec syntax   vmsulwx {Qop ,prt, SHFR8|SHFL16 [,sx][,conj]} vx[X], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0,4
                                                            Offset for the first DW used from operand
                                                            2

              4    IN2_V32        vec_t                     Input vector operand
Operands
              5    IN2_OFST       uint8     0,4
                                                            Offset for the first DW used from operand
                                                            4

              6    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 4
              7    IN3_V40        vec40_t                   Output vector operand
              8    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsulwx_v32_v32_v40_prt_SHFL16_conj_p (4, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsulwx_v32_v32_v40_prt_SHFL16_conj_p version.


Main table → Multiplication → Multiply-Subtract → Complex 32x16
Intrinsic     vmsulwx_v32_v32_v40_prt_SHFL16[_p]
name
Spec syntax   vmsulwx {Qop ,prt, SHFR8|SHFL16 [,sx][,conj]} vx[X], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0,4
                                                            Offset for the first DW used from operand
                                                            2

Operands      4    IN2_V32        vec_t                     Input vector operand

              5    IN2_OFST       uint8     0,4

Offset for the first DW used from operand
                                                            4

              6    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 4
              7    IN3_V40        vec40_t                   Output vector operand
              8    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsulwx_v32_v32_v40_prt_SHFL16_p (4, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsulwx_v32_v32_v40_prt_SHFL16_p version.


Main table → Multiplication → Multiply-Subtract → Complex 32x16
Intrinsic     vmsulwx_v32_v32_v40_prt_SHFL16_sx_conj[_p]
name
Spec syntax   vmsulwx {Qop ,prt, SHFR8|SHFL16 [,sx][,conj]} vx[X], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0,4
                                                            Offset for the first DW used from operand
                                                            2

              4    IN2_V32        vec_t                     Input vector operand
Operands
              5    IN2_OFST       uint8     0,4
                                                            Offset for the first DW used from operand
                                                            4

              6    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 4
              7    IN3_V40        vec40_t                   Output vector operand
              8    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsulwx_v32_v32_v40_prt_SHFL16_sx_conj_p (4, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsulwx_v32_v32_v40_prt_SHFL16_sx_conj_p version.


Main table → Multiplication → Multiply-Subtract → Complex 32x16
Intrinsic     vmsulwx_v32_v32_v40_prt_SHFL16_sx[_p]
name

Spec syntax   vmsulwx {Qop ,prt, SHFR8|SHFL16 [,sx][,conj]} vx[X], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

Operands      1    QOP            uint8     1..4            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0,4             Offset for the first DW used from operand
                                                            2

              4    IN2_V32        vec_t                     Input vector operand

              5    IN2_OFST       uint8     0,4             Offset for the first DW used from operand
                                                            4

              6    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 4
              7    IN3_V40        vec40_t                   Output vector operand
              8    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsulwx_v32_v32_v40_prt_SHFL16_sx_p (4, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsulwx_v32_v32_v40_prt_SHFL16_sx_p version.


Main table → Multiplication → Multiply-Subtract → Complex 32x16
Intrinsic     vmsulwx_v32_v32_v40_prt_SHFR8_conj[_p]
name
Spec syntax   vmsulwx {Qop ,prt, SHFR8|SHFL16 [,sx][,conj]} vx[X], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0,4             Offset for the first DW used from operand
                                                            2

              4    IN2_V32        vec_t                     Input vector operand
Operands
              5    IN2_OFST       uint8     0,4             Offset for the first DW used from operand
                                                            4

              6    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 4
              7    IN3_V40        vec40_t                   Output vector operand
              8    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;

C example     vprex_t vecPred;
              ...
              vRes = vmsulwx_v32_v32_v40_prt_SHFR8_conj_p (4, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

Comments      1.   IN_VPR last operand is relevant only for
                   vmsulwx_v32_v32_v40_prt_SHFR8_conj_p version.


Main table → Multiplication → Multiply-Subtract → Complex 32x16
Intrinsic     vmsulwx_v32_v32_v40_prt_SHFR8[_p]
name
Spec syntax   vmsulwx {Qop ,prt, SHFR8|SHFL16 [,sx][,conj]} vx[X], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0,4
                                                            Offset for the first DW used from operand
                                                            2

              4    IN2_V32        vec_t                     Input vector operand
Operands
              5    IN2_OFST       uint8     0,4
                                                            Offset for the first DW used from operand
                                                            4

              6    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 4
              7    IN3_V40        vec40_t                   Output vector operand
              8    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsulwx_v32_v32_v40_prt_SHFR8_p (4, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsulwx_v32_v32_v40_prt_SHFR8_p version.


Main table → Multiplication → Multiply-Subtract → Complex 32x16
Intrinsic     vmsulwx_v32_v32_v40_prt_SHFR8_sx_conj[_p]
name
Spec syntax   vmsulwx {Qop ,prt, SHFR8|SHFL16 [,sx][,conj]} vx[X], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0,4
                                                            Offset for the first DW used from operand
Operands                                                    2

4    IN2_V32        vec_t                     Input vector operand

              5    IN2_OFST       uint8     0,4
                                                            Offset for the first DW used from operand
                                                            4
              6    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 4
              7    IN3_V40        vec40_t                   Output vector operand
              8    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsulwx_v32_v32_v40_prt_SHFR8_sx_conj_p (4, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsulwx_v32_v32_v40_prt_SHFR8_sx_conj_p version.


Main table → Multiplication → Multiply-Subtract → Complex 32x16
Intrinsic     vmsulwx_v32_v32_v40_prt_SHFR8_sx[_p]
name
Spec syntax   vmsulwx {Qop ,prt, SHFR8|SHFL16 [,sx][,conj]} vx[X], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0,4             Offset for the first DW used from operand
                                                            2

              4    IN2_V32        vec_t                     Input vector operand
Operands
              5    IN2_OFST       uint8     0,4             Offset for the first DW used from operand
                                                            4

              6    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 4
              7    IN3_V40        vec40_t                   Output vector operand
              8    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsulwx_v32_v32_v40_prt_SHFR8_sx_p (4, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsulwx_v32_v32_v40_prt_SHFR8_sx_p version.


Main table → Multiplication → Multiply-Subtract → Complex 32x16
Intrinsic     vmsulwx_v32_v32_v40_conj32[_p]
name

Spec syntax   vmsulwx {Qop [,conj_conj32][,vmpsX]} vx[Xe], vy[Y], voz[0], ?vprX

Return type   vec40_t

              1    QOP             uint8     1..4             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand

              3    IN1_OFST        uint8     0,4
                                                              Offset for the first DW used from operand
                                                              2

Operands      4    IN2_V32         vec_t                      Input vector operand

              5    IN2_OFST        uint8     0,4
                                                              Offset for the first DW used from operand
                                                              4

              6    IN3_V40         vec40_t                    Output vector operand
              7    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsulwx_v32_v32_v40_conj32_p (4, vIn, 0, vIn2, 0, vRes, vecPred);

                   IN_VPR last operand is relevant only for vmsulwx_v32_v32_v40_conj32_p
Comments      1.
                   version.


Main table → Multiplication → Multiply-Subtract → Complex 32x16
Intrinsic     vmsulwx_v32_v32_v40_conj32_vmpsX[_p]
name
Spec syntax   vmsulwx {Qop [,conj_conj32][,vmpsX]} vx[Xe], vy[Y], voz[0], ?vprX

Return type   vec40_t

              1    QOP             uint8     1..4             Number of atomic operations

              2
                                                              Selects the VMSNX and VPSX set within
                   VMPSX           uint8     0,1
                                                              modv0/modv2 mode registers
              3    IN1_V32         vec_t                      Input vector operand

              4    IN1_OFST        uint8     0,4
                                                              Offset for the first DW used from operand
Operands                                                      3

              5    IN2_V32         vec_t                      Input vector operand

              6    IN2_OFST        uint8     0,4
                                                              Offset for the first DW used from operand
                                                              5

7    IN3_V40         vec40_t                    Output vector operand
              8    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsulwx_v32_v32_v40_conj32_vmpsX_p (4, 1, vIn, 0, vIn2, 0, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsulwx_v32_v32_v40_conj32_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Complex 32x16
Intrinsic     vmsulwx_v32_v32_v40_conj[_p]
name
Spec syntax   vmsulwx {Qop [,conj_conj32][,vmpsX]} vx[Xe], vy[Y], voz[0], ?vprX

Return type   vec40_t

              1    QOP             uint8     1..4             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand

              3    IN1_OFST        uint8     0,4
                                                              Offset for the first DW used from operand
                                                              2

Operands      4    IN2_V32         vec_t                      Input vector operand

              5    IN2_OFST        uint8     0,4
                                                              Offset for the first DW used from operand
                                                              4

              6    IN3_V40         vec40_t                    Output vector operand
              7    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsulwx_v32_v32_v40_conj_p (4, vIn, 0, vIn2, 0, vRes, vecPred);

                   IN_VPR last operand is relevant only for vmsulwx_v32_v32_v40_conj_p
Comments      1.
                   version.


Main table → Multiplication → Multiply-Subtract → Complex 32x16
Intrinsic     vmsulwx_v32_v32_v40_conj_vmpsX[_p]
name
Spec syntax   vmsulwx {Qop [,conj_conj32][,vmpsX]} vx[Xe], vy[Y], voz[0], ?vprX

Return type   vec40_t

              1    QOP             uint8     1..4             Number of atomic operations
Operands                                                      Selects the VMSNX and VPSX set within
              2    VMPSX           uint8     0,1

modv0/modv2 mode registers
              3    IN1_V32         vec_t                      Input vector operand

              4    IN1_OFST        uint8     0,4              Offset for the first DW used from operand
                                                              3

              5    IN2_V32         vec_t                      Input vector operand

              6    IN2_OFST        uint8     0,4              Offset for the first DW used from operand
                                                              5

              7    IN3_V40         vec40_t                    Output vector operand
              8    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsulwx_v32_v32_v40_conj_vmpsX_p (4, 1, vIn, 0, vIn2, 0, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsulwx_v32_v32_v40_conj_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Complex 32x16
Intrinsic     vmsulwx_v32_v32_v40[_p]
name
Spec syntax   vmsulwx {Qop [,conj_conj32][,vmpsX]} vx[Xe], vy[Y], voz[0], ?vprX

Return type   vec40_t

              1    QOP             uint8     1..4             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand

              3    IN1_OFST        uint8     0,4              Offset for the first DW used from operand
                                                              2

Operands      4    IN2_V32         vec_t                      Input vector operand

              5    IN2_OFST        uint8     0,4              Offset for the first DW used from operand
                                                              4

              6    IN3_V40         vec40_t                    Output vector operand
              7    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsulwx_v32_v32_v40_p (4, vIn, 0, vIn2, 0, vRes, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmsulwx_v32_v32_v40_p version.


Main table → Multiplication → Multiply-Subtract → Complex 32x16
Intrinsic     vmsulwx_v32_v32_v40_vmpsX[_p]
name

Spec syntax   vmsulwx {Qop [,conj_conj32][,vmpsX]} vx[Xe], vy[Y], voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4             Number of atomic operations
                                                             Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                             modv0/modv2 mode registers
              3    IN1_V32        vec_t                      Input vector operand

              4    IN1_OFST       uint8     0,4
                                                             Offset for the first DW used from operand
Operands                                                     3

              5    IN2_V32        vec_t                      Input vector operand

              6    IN2_OFST       uint8     0,4              Offset for the first DW used from operand
                                                             5

              7    IN3_V40        vec40_t                    Output vector operand
              8    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsulwx_v32_v32_v40_vmpsX_p (4, 1, vIn, 0, vIn2, 0, vRes, vecPred);

                   IN_VPR last operand is relevant only for vmsulwx_v32_v32_v40_vmpsX_p
Comments      1.
                   version.


Main table → Multiplication → Multiply-Subtract → Complex 32x16
Intrinsic     vmsulwx_v32_v32_v40_prt_conj[_p]
name
Spec syntax   vmsulwx {Qop ,prt [,sx][,conj]} vx[X], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4             Number of atomic operations
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
              vRes = vmsulwx_v32_v32_v40_prt_conj_p (4, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for vmsulwx_v32_v32_v40_prt_conj_p
Comments      1.
                   version.


Main table → Multiplication → Multiply-Subtract → Complex 32x16
Intrinsic     vmsulwx_v32_v32_v40_prt[_p]
name
Spec syntax   vmsulwx {Qop ,prt [,sx][,conj]} vx[X], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0,4
                                                             Offset for the first DW used from operand
                                                             2

Operands      4    IN2_V32        vec_t                      Input vector operand

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
              vRes = vmsulwx_v32_v32_v40_prt_p (4, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for vmsulwx_v32_v32_v40_prt_p
Comments      1.
                   version.


Main table → Multiplication → Multiply-Subtract → Complex 32x16
Intrinsic     vmsulwx_v32_v32_v40_prt_sx_conj[_p]
name
Spec syntax   vmsulwx {Qop ,prt [,sx][,conj]} vx[X], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4             Number of atomic operations

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
              vRes = vmsulwx_v32_v32_v40_prt_sx_conj_p (4, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsulwx_v32_v32_v40_prt_sx_conj_p version.


Main table → Multiplication → Multiply-Subtract → Complex 32x16
Intrinsic     vmsulwx_v32_v32_v40_prt_sx[_p]
name
Spec syntax   vmsulwx {Qop ,prt [,sx][,conj]} vx[X], vy[Y]p, voz[0], ?vprX

Return type   vec40_t

Operands      1    QOP            uint8     1..4             Number of atomic operations
            2    IN1_V32        vec_t                      Input vector operand

            3    IN1_OFST       uint8     0,4              Offset for the first DW used from operand
                                                           2

            4    IN2_V32        vec_t                      Input vector operand

            5    IN2_OFST       uint8     0,4              Offset for the first DW used from operand
                                                           4

            6    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 4
            7    IN3_V40        vec40_t                    Output vector operand
            8    IN_VPR         vprex_t                    Vector predicate operand
            vec_t vIn;
            vec_t vIn2;
            vec40_t vRes;
C example   vprex_t vecPred;
            ...
            vRes = vmsulwx_v32_v32_v40_prt_sx_p (4, vIn, 0, vIn2, 0, LOW, vRes, vecPred);

IN_VPR last operand is relevant only for vmsulwx_v32_v32_v40_prt_sx_p
Comments    1.
                 version.


Main table → Multiplication → Multiply-Subtract → Complex 32x16
Intrinsic     vmsulwx_v32_v32_v40_SHFL16_conj32[_p]
name
Spec syntax   vmsulwx {Qop ,SHFR8|SHFL16 [,conj_conj32][,vmpsX]} vx[Xe], vy[Y], voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0,4
                                                            Offset for the first DW used from operand
                                                            2

Operands      4    IN2_V32        vec_t                     Input vector operand

              5    IN2_OFST       uint8     0,4
                                                            Offset for the first DW used from operand
                                                            4

              6    IN3_V40        vec40_t                   Output vector operand
              7    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsulwx_v32_v32_v40_SHFL16_conj32_p (4, vIn, 0, vIn2, 0, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsulwx_v32_v32_v40_SHFL16_conj32_p version.


Main table → Multiplication → Multiply-Subtract → Complex 32x16
Intrinsic     vmsulwx_v32_v32_v40_SHFL16_conj32_vmpsX[_p]
name
Spec syntax   vmsulwx {Qop ,SHFR8|SHFL16 [,conj_conj32][,vmpsX]} vx[Xe], vy[Y], voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4            Number of atomic operations

              2
                                                            Selects the VMSNX and VPSX set within
                   VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand

              4    IN1_OFST       uint8     0,4
                                                            Offset for the first DW used from operand
Operands                                                    3

5    IN2_V32        vec_t                     Input vector operand

              6    IN2_OFST       uint8     0,4
                                                            Offset for the first DW used from operand
                                                            5

              7    IN3_V40        vec40_t                   Output vector operand
              8    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsulwx_v32_v32_v40_SHFL16_conj32_vmpsX_p (4, 1, vIn, 0, vIn2, 0, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsulwx_v32_v32_v40_SHFL16_conj32_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Complex 32x16
Intrinsic     vmsulwx_v32_v32_v40_SHFL16_conj[_p]
name
Spec syntax   vmsulwx {Qop ,SHFR8|SHFL16 [,conj_conj32][,vmpsX]} vx[Xe], vy[Y], voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0,4
                                                            Offset for the first DW used from operand
                                                            2

Operands      4    IN2_V32        vec_t                     Input vector operand

              5    IN2_OFST       uint8     0,4
                                                            Offset for the first DW used from operand
                                                            4

              6    IN3_V40        vec40_t                   Output vector operand
              7    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsulwx_v32_v32_v40_SHFL16_conj_p (4, vIn, 0, vIn2, 0, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsulwx_v32_v32_v40_SHFL16_conj_p version.


Main table → Multiplication → Multiply-Subtract → Complex 32x16
Intrinsic     vmsulwx_v32_v32_v40_SHFL16_conj_vmpsX[_p]
name
Spec syntax   vmsulwx {Qop ,SHFR8|SHFL16 [,conj_conj32][,vmpsX]} vx[Xe], vy[Y], voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4            Number of atomic operations
Operands                                                    Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32        vec_t                      Input vector operand

              4    IN1_OFST       uint8     0,4              Offset for the first DW used from operand
                                                             3

              5    IN2_V32        vec_t                      Input vector operand

              6    IN2_OFST       uint8     0,4              Offset for the first DW used from operand
                                                             5

              7    IN3_V40        vec40_t                    Output vector operand
              8    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsulwx_v32_v32_v40_SHFL16_conj_vmpsX_p (4, 1, vIn, 0, vIn2, 0, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsulwx_v32_v32_v40_SHFL16_conj_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Complex 32x16
Intrinsic     vmsulwx_v32_v32_v40_SHFL16[_p]
name
Spec syntax   vmsulwx {Qop ,SHFR8|SHFL16 [,conj_conj32][,vmpsX]} vx[Xe], vy[Y], voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0,4              Offset for the first DW used from operand
                                                             2

Operands      4    IN2_V32        vec_t                      Input vector operand

              5    IN2_OFST       uint8     0,4              Offset for the first DW used from operand
                                                             4

              6    IN3_V40        vec40_t                    Output vector operand
              7    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;

...
              vRes = vmsulwx_v32_v32_v40_SHFL16_p (4, vIn, 0, vIn2, 0, vRes, vecPred);

                   IN_VPR last operand is relevant only for vmsulwx_v32_v32_v40_SHFL16_p
Comments      1.
                   version.


Main table → Multiplication → Multiply-Subtract → Complex 32x16
Intrinsic     vmsulwx_v32_v32_v40_SHFL16_vmpsX[_p]
name
Spec syntax   vmsulwx {Qop ,SHFR8|SHFL16 [,conj_conj32][,vmpsX]} vx[Xe], vy[Y], voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4            Number of atomic operations
                                                            Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand

              4    IN1_OFST       uint8     0,4
                                                            Offset for the first DW used from operand
Operands                                                    3

              5    IN2_V32        vec_t                     Input vector operand

              6    IN2_OFST       uint8     0,4             Offset for the first DW used from operand
                                                            5

              7    IN3_V40        vec40_t                   Output vector operand
              8    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsulwx_v32_v32_v40_SHFL16_vmpsX_p (4, 1, vIn, 0, vIn2, 0, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsulwx_v32_v32_v40_SHFL16_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Complex 32x16
Intrinsic     vmsulwx_v32_v32_v40_SHFR8_conj32[_p]
name
Spec syntax   vmsulwx {Qop ,SHFR8|SHFL16 [,conj_conj32][,vmpsX]} vx[Xe], vy[Y], voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0,4
                                                            Offset for the first DW used from operand
                                                            2

Operands      4    IN2_V32        vec_t                     Input vector operand

              5    IN2_OFST       uint8     0,4
                                                            Offset for the first DW used from operand
                                                            4

              6    IN3_V40        vec40_t                   Output vector operand
              7    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsulwx_v32_v32_v40_SHFR8_conj32_p (4, vIn, 0, vIn2, 0, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsulwx_v32_v32_v40_SHFR8_conj32_p version.


Main table → Multiplication → Multiply-Subtract → Complex 32x16
Intrinsic     vmsulwx_v32_v32_v40_SHFR8_conj32_vmpsX[_p]
name
Spec syntax   vmsulwx {Qop ,SHFR8|SHFL16 [,conj_conj32][,vmpsX]} vx[Xe], vy[Y], voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4            Number of atomic operations

              2
                                                            Selects the VMSNX and VPSX set within
                   VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand

              4    IN1_OFST       uint8     0,4
                                                            Offset for the first DW used from operand
Operands                                                    3

              5    IN2_V32        vec_t                     Input vector operand

              6    IN2_OFST       uint8     0,4
                                                            Offset for the first DW used from operand
                                                            5

              7    IN3_V40        vec40_t                   Output vector operand
              8    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsulwx_v32_v32_v40_SHFR8_conj32_vmpsX_p (4, 1, vIn, 0, vIn2, 0, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.

vmsulwx_v32_v32_v40_SHFR8_conj32_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Complex 32x16
Intrinsic     vmsulwx_v32_v32_v40_SHFR8_conj[_p]
name
Spec syntax   vmsulwx {Qop ,SHFR8|SHFL16 [,conj_conj32][,vmpsX]} vx[Xe], vy[Y], voz[0], ?vprX

Return type   vec40_t

Operands      1    QOP            uint8     1..4            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

              3    IN1_OFST       uint8     0,4             Offset for the first DW used from operand
                                                            2

              4    IN2_V32        vec_t                     Input vector operand

              5    IN2_OFST       uint8     0,4             Offset for the first DW used from operand
                                                            4

              6    IN3_V40        vec40_t                   Output vector operand
              7    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsulwx_v32_v32_v40_SHFR8_conj_p (4, vIn, 0, vIn2, 0, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmsulwx_v32_v32_v40_SHFR8_conj_p version.


Main table → Multiplication → Multiply-Subtract → Complex 32x16
Intrinsic     vmsulwx_v32_v32_v40_SHFR8_conj_vmpsX[_p]
name
Spec syntax   vmsulwx {Qop ,SHFR8|SHFL16 [,conj_conj32][,vmpsX]} vx[Xe], vy[Y], voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4            Number of atomic operations
                                                            Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1
                                                            modv0/modv2 mode registers
              3    IN1_V32        vec_t                     Input vector operand

              4    IN1_OFST       uint8     0,4             Offset for the first DW used from operand
Operands                                                    3

              5    IN2_V32        vec_t                     Input vector operand

              6    IN2_OFST       uint8     0,4             Offset for the first DW used from operand
                                                            5

7    IN3_V40        vec40_t                   Output vector operand
              8    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsulwx_v32_v32_v40_SHFR8_conj_vmpsX_p (4, 1, vIn, 0, vIn2, 0, vRes, vecPred);

Comments      1.   IN_VPR last operand is relevant only for
                   vmsulwx_v32_v32_v40_SHFR8_conj_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Complex 32x16
Intrinsic     vmsulwx_v32_v32_v40_SHFR8[_p]
name
Spec syntax   vmsulwx {Qop ,SHFR8|SHFL16 [,conj_conj32][,vmpsX]} vx[Xe], vy[Y], voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0,4
                                                             Offset for the first DW used from operand
                                                             2

Operands      4    IN2_V32        vec_t                      Input vector operand

              5    IN2_OFST       uint8     0,4
                                                             Offset for the first DW used from operand
                                                             4

              6    IN3_V40        vec40_t                    Output vector operand
              7    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmsulwx_v32_v32_v40_SHFR8_p (4, vIn, 0, vIn2, 0, vRes, vecPred);

                   IN_VPR last operand is relevant only for vmsulwx_v32_v32_v40_SHFR8_p
Comments      1.
                   version.


Main table → Multiplication → Multiply-Subtract → Complex 32x16
Intrinsic     vmsulwx_v32_v32_v40_SHFR8_vmpsX[_p]
name
Spec syntax   vmsulwx {Qop ,SHFR8|SHFL16 [,conj_conj32][,vmpsX]} vx[Xe], vy[Y], voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4             Number of atomic operations
                                                             Selects the VMSNX and VPSX set within
              2    VMPSX          uint8     0,1

modv0/modv2 mode registers
              3    IN1_V32        vec_t                      Input vector operand
Operands
              4    IN1_OFST       uint8     0,4
                                                             Offset for the first DW used from operand
                                                             3

              5    IN2_V32        vec_t                      Input vector operand
              6    IN2_OFST       uint8     0,4              Offset for the first DW used from operand
                                                          5

            7    IN3_V40        vec40_t                   Output vector operand
            8    IN_VPR         vprex_t                   Vector predicate operand
            vec_t vIn;
            vec_t vIn2;
            vec40_t vRes;
C example   vprex_t vecPred;
            ...
            vRes = vmsulwx_v32_v32_v40_SHFR8_vmpsX_p (4, 1, vIn, 0, vIn2, 0, vRes, vecPred);

                 IN_VPR last operand is relevant only for
Comments    1.
                 vmsulwx_v32_v32_v40_SHFR8_vmpsX_p version.


Main table → Multiplication → Multiply-Subtract → Complex 32x16
