# Generic → Generic Linear → Vector Generic Linear

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Generic → Generic Linear → Vector Generic Linear

Vector Generic Linear

Vector Generic Linear
Performs configurable linear operation between three sources using CISA. The multiplicands and
addends are user configured according to the configuration regsiter set. The sources are 16-bit
and 8-bit wide. The addition results are 16-bit wide and are packed into either 32-bit or 40-bit
destination according to the register type.
Available Switches
               Number of atomic operations. An atomic operation is defined as a pair of two linear
Oop
               operations. 1op ≤ Oop ≤ 8op
SHFL16 Pseudo-switch which is replaced by <
               Configuration register. The instruction operands are configured according to one of
cfgX           the vector registers. The X is replaced with i0,i1...i10,i11...o2,o3. The default value is
               cfgi4 which selects the vi4 vector register.
Intrinsic Names
vgenlinwb_v32X_v32_v32_SHFL16
vgenlinwb_v32X_v32_v32
vgenlinwb_v32_v32Y_v32_SHFL16
vgenlinwb_v32_v32Y_v32
Instruction details in the instruction set specification
Intrinsic     vgenlinwb_v32X_v32_v32_SHFL16[_p]
name
Spec syntax   vgenlinwb {Oop [,SHFL16] [,cfgX]} vx[X], vy, vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8             Number of atomic operations
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
              vRes = vgenlinwb_v32X_v32_v32_SHFL16_p (8, vcfgIn, vIn, 0, vIn2, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vgenlinwb_v32X_v32_v32_SHFL16_p version.


Main table → Generic → Generic Linear → Vector Generic Linear
Intrinsic     vgenlinwb_v32X_v32_v32[_p]
name
Spec syntax   vgenlinwb {Oop [,SHFL16] [,cfgX]} vx[X], vy, vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8             Number of atomic operations
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
              vRes = vgenlinwb_v32X_v32_v32_p (8, vcfgIn, vIn, 0, vIn2, vecPred);
                 IN_VPR last operand is relevant only for vgenlinwb_v32X_v32_v32_p
Comments    1.
                 version.


Main table → Generic → Generic Linear → Vector Generic Linear
Intrinsic     vgenlinwb_v32_v32Y_v32_SHFL16[_p]
name
Spec syntax   vgenlinwb {Oop [,SHFL16] [,cfgX]} vx, vy[Y], vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8             Number of atomic operations
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
              vRes = vgenlinwb_v32_v32Y_v32_SHFL16_p (8, vcfgIn, vIn, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vgenlinwb_v32_v32Y_v32_SHFL16_p version.


Main table → Generic → Generic Linear → Vector Generic Linear
Intrinsic     vgenlinwb_v32_v32Y_v32[_p]
name
Spec syntax   vgenlinwb {Oop [,SHFL16] [,cfgX]} vx, vy[Y], vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8             Number of atomic operations
              2    IN_CFGX         vec_t                      Configuration register
              3    IN1_V32         vec_t                      Input vector operand
Operands      4    IN2_V32         vec_t                      Input vector operand

              5    IN2_OFST        uint8     0,4
                                                              Offset for the first DW used from operand
                                                              4

              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vec_t vcfgIn;
              vprex_t vecPred;
              ...
              vRes = vgenlinwb_v32_v32Y_v32_p (8, vcfgIn, vIn, vIn2, 0, vecPred);
                 IN_VPR last operand is relevant only for vgenlinwb_v32_v32Y_v32_p
Comments    1.
                 version.


Main table → Generic → Generic Linear → Vector Generic Linear
