# Data Reordering → Permute → Vector Permute Byte

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Data Reordering → Permute → Vector Permute Byte

Vector Permute Byte

Vector Permute Byte
Performs vector permutation on a source vector according to specified locations from using a
configuration register set into destination vector.
Available Switches
        Number of atomic operations. An atomic operation is defined as two byte permutation
Hop
        operations. 1op ≤ Hop ≤ 16op
     Configuration register. The instruction operands and signs are configured according to one
cfgX of the vector registers. The X is replaced with i0,i1...i10,i11...o2,o3. The default value is
     cfgi4 which selects the vi4 vector register.
        When used, configuration register cfgX5 is valid. The default value for cfgX5 register is
clr
        ignored.
Intrinsic Names
vpermuteb_v32_v32_clr
vpermuteb_v32_v32
Instruction details in the instruction set specification
Intrinsic     vpermuteb_v32_v32_clr[_p]
name
Spec syntax   vpermuteb {Hop [,cfgX][,clr]} vx, vz[0], ?vprX

Return type   vec_t

              1    HOP             uint8     1..16            Number of atomic operations
              2    IN_CFGX         vec_t                      Configuration register
Operands
              3    IN1_V32         vec_t                      Input vector operand
              4    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              vec_t vcfgIn;
C example     vprex_t vecPred;
              ...
              vRes = vpermuteb_v32_v32_clr_p (16, vcfgIn, vIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vpermuteb_v32_v32_clr_p version.


Main table → Data Reordering → Permute → Vector Permute Byte
Intrinsic     vpermuteb_v32_v32[_p]
name
Spec syntax   vpermuteb {Hop [,cfgX][,clr]} vx, vz[0], ?vprX

Return type   vec_t

              1    HOP             uint8     1..16            Number of atomic operations
              2    IN_CFGX         vec_t                      Configuration register
Operands
              3    IN1_V32         vec_t                      Input vector operand
              4    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              vec_t vcfgIn;
C example     vprex_t vecPred;
              ...

vRes = vpermuteb_v32_v32_p (16, vcfgIn, vIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vpermuteb_v32_v32_p version.


Main table → Data Reordering → Permute → Vector Permute Byte
