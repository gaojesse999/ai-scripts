# Generic → Generic Linear and Pack → Vector Generic Linear and Pack

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Generic → Generic Linear and Pack → Vector Generic Linear and Pack

Vector Generic Linear and Pack

Vector Generic Linear and Pack
Performs configurable linear and packing operation between three sources using CISA. The
multiplicands and addends are user configured according to the configuration register set. The
sources are 16-bit and 8-bit wide. The addition results are 16-bit wide and are packed into either
32-bit or 40-bit according to the register type.
Available Switches
               Number of atomic operations. An atomic operation is defined as four linear
Qop
               operations and packing the results into the destination. 1op ≤ Qop ≤ 4op
SHFL16 Pseudo-switch which is replaced by <
               Configuration register. The instruction operands are configured according to one of
cfgX           the vector registers. The X is replaced with i0,i1...i10,i11...o2,o3. The default value is
               cfgi4 which selects the vi4 vector register.

h              When used, bits [23:16] of the 24-bit result are packed instead of bits [15:8].
Intrinsic Names
vgenlinp_v32_v32Y_v32_SHFL16_h
vgenlinp_v32_v32Y_v32_SHFL16
vgenlinp_v32_v32Y_v32_h
vgenlinp_v32_v32Y_v32
vgenlinp_v32X_v32_v32_SHFL16_h
vgenlinp_v32X_v32_v32_SHFL16
vgenlinp_v32X_v32_v32_h
vgenlinp_v32X_v32_v32
Instruction details in the instruction set specification
Intrinsic     vgenlinp_v32_v32Y_v32_SHFL16_h[_p]
name
Spec syntax   vgenlinp {Qop [,SHFL16] [,cfgX][,h]} vx, vy[Y], vz[0], ?vprX

Return type   vec_t

              1    QOP            uint8     1..4             Number of atomic operations
              2    IN_CFGX        vec_t                      Configuration register
              3    IN1_V32        vec_t                      Input vector operand
Operands      4    IN2_V32        vec_t                      Input vector operand

              5    IN2_OFST       uint8     0,4              Offset for the first DW used from operand
                                                             4

              6    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vec_t vcfgIn;
              vprex_t vecPred;
              ...
              vRes = vgenlinp_v32_v32Y_v32_SHFL16_h_p (4, vcfgIn, vIn, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vgenlinp_v32_v32Y_v32_SHFL16_h_p version.


Main table → Generic → Generic Linear and Pack → Vector Generic Linear and Pack
Intrinsic     vgenlinp_v32_v32Y_v32_SHFL16[_p]
name
Spec syntax   vgenlinp {Qop [,SHFL16] [,cfgX][,h]} vx, vy[Y], vz[0], ?vprX

Return type   vec_t

              1    QOP            uint8     1..4             Number of atomic operations
              2    IN_CFGX        vec_t                      Configuration register
              3    IN1_V32        vec_t                      Input vector operand
Operands      4    IN2_V32        vec_t                      Input vector operand

              5    IN2_OFST       uint8     0,4
                                                             Offset for the first DW used from operand
                                                             4

              6    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vec_t vcfgIn;

vprex_t vecPred;
              ...
              vRes = vgenlinp_v32_v32Y_v32_SHFL16_p (4, vcfgIn, vIn, vIn2, 0, vecPred);
                   IN_VPR last operand is relevant only for
Comments      1.
                   vgenlinp_v32_v32Y_v32_SHFL16_p version.


Main table → Generic → Generic Linear and Pack → Vector Generic Linear and Pack
Intrinsic     vgenlinp_v32_v32Y_v32_h[_p]
name
Spec syntax   vgenlinp {Qop [,SHFL16] [,cfgX][,h]} vx, vy[Y], vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4             Number of atomic operations
              2    IN_CFGX         vec_t                      Configuration register
              3    IN1_V32         vec_t                      Input vector operand
Operands      4    IN2_V32         vec_t                      Input vector operand

              5    IN2_OFST        uint8     0,4              Offset for the first DW used from operand
                                                              4

              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vec_t vcfgIn;
              vprex_t vecPred;
              ...
              vRes = vgenlinp_v32_v32Y_v32_h_p (4, vcfgIn, vIn, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for vgenlinp_v32_v32Y_v32_h_p
Comments      1.
                   version.


Main table → Generic → Generic Linear and Pack → Vector Generic Linear and Pack
Intrinsic     vgenlinp_v32_v32Y_v32[_p]
name
Spec syntax   vgenlinp {Qop [,SHFL16] [,cfgX][,h]} vx, vy[Y], vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4             Number of atomic operations
              2    IN_CFGX         vec_t                      Configuration register
              3    IN1_V32         vec_t                      Input vector operand
Operands      4    IN2_V32         vec_t                      Input vector operand

              5    IN2_OFST        uint8     0,4
                                                              Offset for the first DW used from operand
                                                              4

              6    IN_VPR          vprex_t                    Vector predicate operand
C example     vec_t vIn;
            vec_t vIn2;
            vec_t vRes;
            vec_t vcfgIn;
            vprex_t vecPred;
            ...

vRes = vgenlinp_v32_v32Y_v32_p (4, vcfgIn, vIn, vIn2, 0, vecPred);

                 IN_VPR last operand is relevant only for vgenlinp_v32_v32Y_v32_p
Comments    1.
                 version.


Main table → Generic → Generic Linear and Pack → Vector Generic Linear and Pack
Intrinsic     vgenlinp_v32X_v32_v32_SHFL16_h[_p]
name
Spec syntax   vgenlinp {Qop [,SHFL16] [,cfgX][,h]} vx[X], vy, vz[0], ?vprX

Return type   vec_t

              1    QOP            uint8     1..4             Number of atomic operations
              2    IN_CFGX        vec_t                      Configuration register
              3    IN1_V32        vec_t                      Input vector operand
Operands                                                     Offset for the first DW used from operand
              4    IN1_OFST       uint8     0,4
                                                             3

              5    IN2_V32        vec_t                      Input vector operand
              6    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vec_t vcfgIn;
              vprex_t vecPred;
              ...
              vRes = vgenlinp_v32X_v32_v32_SHFL16_h_p (4, vcfgIn, vIn, 0, vIn2, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vgenlinp_v32X_v32_v32_SHFL16_h_p version.


Main table → Generic → Generic Linear and Pack → Vector Generic Linear and Pack
Intrinsic     vgenlinp_v32X_v32_v32_SHFL16[_p]
name
Spec syntax   vgenlinp {Qop [,SHFL16] [,cfgX][,h]} vx[X], vy, vz[0], ?vprX

Return type   vec_t

              1    QOP            uint8     1..4             Number of atomic operations
              2    IN_CFGX        vec_t                      Configuration register
              3    IN1_V32        vec_t                      Input vector operand
Operands                                                     Offset for the first DW used from operand
              4    IN1_OFST       uint8     0,4
                                                             3

              5    IN2_V32        vec_t                      Input vector operand
              6    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vec_t vcfgIn;
              vprex_t vecPred;
              ...

vRes = vgenlinp_v32X_v32_v32_SHFL16_p (4, vcfgIn, vIn, 0, vIn2, vecPred);
                   IN_VPR last operand is relevant only for
Comments      1.
                   vgenlinp_v32X_v32_v32_SHFL16_p version.


Main table → Generic → Generic Linear and Pack → Vector Generic Linear and Pack
Intrinsic     vgenlinp_v32X_v32_v32_h[_p]
name
Spec syntax   vgenlinp {Qop [,SHFL16] [,cfgX][,h]} vx[X], vy, vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4             Number of atomic operations
              2    IN_CFGX         vec_t                      Configuration register
              3    IN1_V32         vec_t                      Input vector operand
Operands                                                      Offset for the first DW used from operand
              4    IN1_OFST        uint8     0,4
                                                              3

              5    IN2_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vec_t vcfgIn;
              vprex_t vecPred;
              ...
              vRes = vgenlinp_v32X_v32_v32_h_p (4, vcfgIn, vIn, 0, vIn2, vecPred);

                   IN_VPR last operand is relevant only for vgenlinp_v32X_v32_v32_h_p
Comments      1.
                   version.


Main table → Generic → Generic Linear and Pack → Vector Generic Linear and Pack
Intrinsic     vgenlinp_v32X_v32_v32[_p]
name
Spec syntax   vgenlinp {Qop [,SHFL16] [,cfgX][,h]} vx[X], vy, vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4             Number of atomic operations
              2    IN_CFGX         vec_t                      Configuration register
              3    IN1_V32         vec_t                      Input vector operand
Operands                                                      Offset for the first DW used from operand
              4    IN1_OFST        uint8     0,4
                                                              3

              5    IN2_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
C example     vec_t vIn;
            vec_t vIn2;
            vec_t vRes;
            vec_t vcfgIn;
            vprex_t vecPred;
            ...

vRes = vgenlinp_v32X_v32_v32_p (4, vcfgIn, vIn, 0, vIn2, vecPred);

                 IN_VPR last operand is relevant only for vgenlinp_v32X_v32_v32_p
Comments    1.
                 version.


Main table → Generic → Generic Linear and Pack → Vector Generic Linear and Pack
