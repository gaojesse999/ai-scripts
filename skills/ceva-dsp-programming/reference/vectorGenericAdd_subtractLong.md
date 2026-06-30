# Generic → Generic Add/Subtract → Vector Generic Add/Subtract Long

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Generic → Generic Add/Subtract → Vector Generic Add/Subtract Long

Vector Generic Add/Subtract Long

Vector Generic Add/Subtract Long
Performs configurable addition/subtraction between two sources using CISA. The addends,

operations and signs are user configured according to configuration register set. Each source is
either 64-bit or 72-bit according to the register type. The destination is 72-bit.
Available Switches
Out The out switch notify that first source is treated as 72-bit operands.
        Number of atomic operations. An atomic operation is defined as a single addition. 1op ≤
Qop
        Qop ≤ 4op
     Configuration register. The instruction operands and signs are configured according to one
cfgX of the vector registers. The X is replaced with i0,i1...i10,i11...o2,o3. The default value is
     cfgi4 which selects the vi4 vector register.
Intrinsic Names
vgenasul_v32_v32_v32
vgenasul_v40_v32_v40_out
Instruction details in the instruction set specification
Intrinsic     vgenasul_v32_v32_v32[_p]
name
Spec syntax   vgenasul {Qop [,cfgX]} vx, vy, vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4             Number of atomic operations
              2    IN_CFGX         vec_t                      Configuration register
Operands      3    IN1_V32         vec_t                      Input vector operand
              4    IN2_V32         vec_t                      Input vector operand
              5    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vec_t vcfgIn;
              vprex_t vecPred;
              ...
              vRes = vgenasul_v32_v32_v32_p (4, vcfgIn, vIn, vIn2, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vgenasul_v32_v32_v32_p version.


Main table → Generic → Generic Add/Subtract → Vector Generic Add/Subtract Long
Intrinsic     vgenasul_v40_v32_v40_out[_p]
name
Spec syntax   vgenasul {Qop, out [,cfgX]} vox[0], vy, voz[0], ?vprX

Return type   vec40_t

              1    QOP             uint8     1..4             Number of atomic operations
              2    IN_CFGX         vec_t                      Configuration register
Operands      3    IN1_V40         vec40_t                    Output vector operand
              4    IN2_V32         vec_t                      Input vector operand
              5    IN_VPR          vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vec_t vcfgIn;
              vprex_t vecPred;
              ...

vRes = vgenasul_v40_v32_v40_out_p (4, vcfgIn, vIn, vIn2, vecPred);

                   IN_VPR last operand is relevant only for vgenasul_v40_v32_v40_out_p
Comments      1.
                   version.


Main table → Generic → Generic Add/Subtract → Vector Generic Add/Subtract Long
