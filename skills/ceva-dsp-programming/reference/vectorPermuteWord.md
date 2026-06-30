# Data Reordering → Permute → Vector Permute Word

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Data Reordering → Permute → Vector Permute Word

Vector Permute Word

Vector Permute Word
Performs vector permutation on one or two source vector according to specified locations from
using a configuration register set into destination vector.
Available Switches
        Number of atomic operations. An atomic operation is defined as a word permutation
Hop
        operation. 1op ≤ Hop ≤ 16op
        Number of atomic operations. An atomic operation is defined as two permutation
Oop
        operations. 1op ≤ Oop ≤ 8op
     Configuration register. The instruction operands and signs are configured according to one
     of the vector registers. The X is replaced with i0,i1...i10,i11...o2,o3. The default value is
cfgX
     cfgi4 which selects the vi4 vector register. cfgX0 and cfgX1 are used as the configuration
     registers.
        When used, configuration register cfgX5 is valid. The default value for cfgX5 register is
clr
        ignored.
u       When used, the destination is zero-extended. The default is sign-extention.
Intrinsic Names
vpermutew_v32_v32_v32_clr
vpermutew_v32_v32_v32_clr_u
vpermutew_v32_v32_v32
vpermutew_v32_v32_v32_u
vpermutew_v32_v32_clr
vpermutew_v32_v32_clr_u
vpermutew_v32_v32
vpermutew_v32_v32_u
Instruction details in the instruction set specification
Intrinsic     vpermutew_v32_v32_v32_clr[_p]
name
Spec syntax   vpermutew {Hop [,cfgX][,clr][,u]} vx, vy, vz[0], ?vprX

Return type   vec_t

              1    HOP             uint8     1..16           Number of atomic operations
              2    IN_CFGX         vec_t                     Configuration register
Operands      3    IN1_V32         vec_t                     Input vector operand
              4    IN2_V32         vec_t                     Input vector operand
              5    IN_VPR          vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vec_t vcfgIn;
              vprex_t vecPred;
              ...
              vRes = vpermutew_v32_v32_v32_clr_p (16, vcfgIn, vIn, vIn2, vecPred);

                   IN_VPR last operand is relevant only for vpermutew_v32_v32_v32_clr_p
Comments      1.
                   version.

Main table → Data Reordering → Permute → Vector Permute Word
Intrinsic     vpermutew_v32_v32_v32_clr_u[_p]
name
Spec syntax   vpermutew {Hop [,cfgX][,clr][,u]} vx, vy, vz[0], ?vprX

Return type   vec_t

              1    HOP             uint8     1..16           Number of atomic operations
              2    IN_CFGX         vec_t                     Configuration register
Operands      3    IN1_V32         vec_t                     Input vector operand
              4    IN2_V32         vec_t                     Input vector operand
              5    IN_VPR          vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vec_t vcfgIn;
              vprex_t vecPred;
              ...
              vRes = vpermutew_v32_v32_v32_clr_u_p (16, vcfgIn, vIn, vIn2, vecPred);

                   IN_VPR last operand is relevant only for vpermutew_v32_v32_v32_clr_u_p
Comments      1.
                   version.


Main table → Data Reordering → Permute → Vector Permute Word
Intrinsic     vpermutew_v32_v32_v32[_p]
name
Spec syntax   vpermutew {Hop [,cfgX][,clr][,u]} vx, vy, vz[0], ?vprX

Return type   vec_t

              1    HOP            uint8     1..16            Number of atomic operations
              2    IN_CFGX        vec_t                      Configuration register
Operands      3    IN1_V32        vec_t                      Input vector operand
              4    IN2_V32        vec_t                      Input vector operand
              5    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vec_t vcfgIn;
              vprex_t vecPred;
              ...
              vRes = vpermutew_v32_v32_v32_p (16, vcfgIn, vIn, vIn2, vecPred);

                   IN_VPR last operand is relevant only for vpermutew_v32_v32_v32_p
Comments      1.
                   version.


Main table → Data Reordering → Permute → Vector Permute Word
Intrinsic     vpermutew_v32_v32_v32_u[_p]
name
Spec syntax   vpermutew {Hop [,cfgX][,clr][,u]} vx, vy, vz[0], ?vprX

Return type   vec_t

              1    HOP            uint8     1..16            Number of atomic operations
              2    IN_CFGX        vec_t                      Configuration register
Operands      3    IN1_V32        vec_t                      Input vector operand

4    IN2_V32        vec_t                      Input vector operand
              5    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vec_t vcfgIn;
              vprex_t vecPred;
              ...
              vRes = vpermutew_v32_v32_v32_u_p (16, vcfgIn, vIn, vIn2, vecPred);

                   IN_VPR last operand is relevant only for vpermutew_v32_v32_v32_u_p
Comments      1.
                   version.


Main table → Data Reordering → Permute → Vector Permute Word
Intrinsic     vpermutew_v32_v32_clr[_p]
name
Spec syntax   vpermutew {Oop [,cfgX][,clr][,u]} vx, vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8            Number of atomic operations
              2    IN_CFGX         vec_t                     Configuration register
Operands
              3    IN1_V32         vec_t                     Input vector operand
              4    IN_VPR          vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              vec_t vcfgIn;
C example     vprex_t vecPred;
              ...
              vRes = vpermutew_v32_v32_clr_p (8, vcfgIn, vIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vpermutew_v32_v32_clr_p version.


Main table → Data Reordering → Permute → Vector Permute Word
Intrinsic     vpermutew_v32_v32_clr_u[_p]
name
Spec syntax   vpermutew {Oop [,cfgX][,clr][,u]} vx, vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8            Number of atomic operations
              2    IN_CFGX         vec_t                     Configuration register
Operands
              3    IN1_V32         vec_t                     Input vector operand
              4    IN_VPR          vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              vec_t vcfgIn;
C example     vprex_t vecPred;
              ...
              vRes = vpermutew_v32_v32_clr_u_p (8, vcfgIn, vIn, vecPred);

                   IN_VPR last operand is relevant only for vpermutew_v32_v32_clr_u_p
Comments      1.
                   version.


Main table → Data Reordering → Permute → Vector Permute Word
Intrinsic     vpermutew_v32_v32[_p]
name
Spec syntax   vpermutew {Oop [,cfgX][,clr][,u]} vx, vz[0], ?vprX

Return type   vec_t

1    OOP            uint8     1..8             Number of atomic operations
              2    IN_CFGX        vec_t                      Configuration register
Operands
              3    IN1_V32        vec_t                      Input vector operand
              4    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              vec_t vcfgIn;
C example     vprex_t vecPred;
              ...
              vRes = vpermutew_v32_v32_p (8, vcfgIn, vIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vpermutew_v32_v32_p version.


Main table → Data Reordering → Permute → Vector Permute Word
Intrinsic     vpermutew_v32_v32_u[_p]
name
Spec syntax   vpermutew {Oop [,cfgX][,clr][,u]} vx, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN_CFGX        vec_t                      Configuration register
Operands
              3    IN1_V32        vec_t                      Input vector operand
              4    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              vec_t vcfgIn;
C example     vprex_t vecPred;
              ...
              vRes = vpermutew_v32_v32_u_p (8, vcfgIn, vIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vpermutew_v32_v32_u_p version.


Main table → Data Reordering → Permute → Vector Permute Word
