# Special Algorithms → Generic Add Compare and Select → Vector Generic

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Special Algorithms → Generic Add Compare and Select → Vector Generic
Add Compare and Select

Vector Generic Add Compare and Select

Vector Generic Add Compare and Select
Performs configurable addition/subtraction compare and select between two sources using CISA.
The addends, operations and signs are user configured according to configuration register set.
Each source is 16-bit and the results are packed into 40-bit destination.
Available Switches
              Number of atomic operations. An atomic operation is defined as a four add compare
Qop
              and select operations.
              Configuration register. The instruction operands and signs are configured according to
cfgY          one of the vector registers: vi0, vi1...vi6,vi7. The Y is replaced with i0,i1...i6,i7. The
              default value is cfgi4 which selects the vi4 vector register.
signset2 Use second set of sign bits from cfgY[31:16]. The default is sign set1 cfgY[15:0]
Intrinsic Names
vgenacsw_v32_v32_v32_v32_c32
vgenacsw_v32_v32_v32_v32_c32_signset2
Instruction details in the instruction set specification
Intrinsic     vgenacsw_v32_v32_v32_v32_c32[_p]
name
Spec syntax   vgenacsw {Qop, b0b0 [,cfgX][,signset2]} vx[0], vy, vz1[0], vz2[0], vcZ1, vcZ2, ?vprX

Return type   coef_t

              1    QOP             uint8     1..4            Number of atomic operations
              2    IN_CFGX         vec_t                     Configuration register
              3    IN1_V32         vec_t                     Input vector operand
              4    IN2_V32         vec_t                     Input vector operand
Operands
              5    RES2_V32        vec_t                     Input vector result operand
              6    RES3_V32        vec_t                     Input vector result operand
              7    RES4_C32        coef_t                    Coefficient result operand
              8    IN_VPR          vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              coef_t vRes1;
              vec_t vRes2;
              vec_t vcfgIn;
C example     vec_t vcoefRes3;
              coef_t vcoefRes4;
              vprex_t vecPred;
              ...

vRes1 = vgenacsw_v32_v32_v32_v32_c32_p (4, vcfgIn, vIn, vIn2, vRes2, vcoefRes3, vcoefRes4, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vgenacsw_v32_v32_v32_v32_c32_p version.
Comments           This intrinsic returns more than one result. The first result variable should be
              2.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.


Main table → Special Algorithms → Generic Add Compare and Select → Vector Generic
Add Compare and Select
Intrinsic     vgenacsw_v32_v32_v32_v32_c32_signset2[_p]
name
Spec syntax   vgenacsw {Qop, b0b0 [,cfgX][,signset2]} vx[0], vy, vz1[0], vz2[0], vcZ1, vcZ2, ?vprX

Return type   coef_t

              1    QOP             uint8     1..4            Number of atomic operations
              2    IN_CFGX         vec_t                     Configuration register
Operands
              3    IN1_V32         vec_t                     Input vector operand
              4    IN2_V32         vec_t                     Input vector operand
            5    RES2_V32       vec_t                      Input vector result operand
            6    RES3_V32       vec_t                      Input vector result operand
            7    RES4_C32       coef_t                     Coefficient result operand
            8    IN_VPR         vprex_t                    Vector predicate operand
            vec_t vIn;
            vec_t vIn2;
            coef_t vRes1;
            vec_t vRes2;
            vec_t vcfgIn;
C example   vec_t vcoefRes3;
            coef_t vcoefRes4;
            vprex_t vecPred;
            ...
            vRes1 = vgenacsw_v32_v32_v32_v32_c32_signset2_p (4, vcfgIn, vIn, vIn2, vRes2, vcoefRes3, vcoefRes4,
            vecPred);

                 IN_VPR last operand is relevant only for
            1.
                 vgenacsw_v32_v32_v32_v32_c32_signset2_p version.
Comments         This intrinsic returns more than one result. The first result variable should be
            2.   placed to the left of the = sign (lvalue). Additional result variables should be
                 passed as parameters.


Main table → Special Algorithms → Generic Add Compare and Select → Vector Generic
Add Compare and Select
