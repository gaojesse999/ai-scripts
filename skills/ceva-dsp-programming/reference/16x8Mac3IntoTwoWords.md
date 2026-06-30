# Generic → Generic Multiply-Accumulate → 16x8 MAC3 into Two Words

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Generic → Generic Multiply-Accumulate → 16x8 MAC3 into Two Words

16x8 MAC3 into Two Words

16x8 MAC3 into Two Words
Performs configurable multiplication between four sources and accumulation using two products
by using CISA. The multiplicands, products signs and accumulation operations are user
configured according to the configuration regsiter set. The sources are 16-bit and 8-bit wide. The
accumulation results are 20-bit wide each and are packed into 40-bit destination.
Available Switches
         Number of atomic operations. An atomic operation is defined as two multiply/multiply-
Oop
         accumulate/subtract operations.
     Configuration register. The instruction operands and signs are configured according to
cfgX one of the vector registers. The X is replaced with i0,i1...i10,i11...o2,o3. The default value
     is cfgi4 which selects the vi4 vector register.
         When used, the 20 LSBs of the products are taken (instead of the high parts). The default
low
         behavior is the high parts.
Intrinsic Names
vgenmacwb3_v32_v32_v40_low

vgenmacwb3_v32_v32_v40
vgenmacwb3_v32_v32_c32_v40_low
vgenmacwb3_v32_v32_c32_v40
Instruction details in the instruction set specification
Intrinsic     vgenmacwb3_v32_v32_v40_low[_p]
name
Spec syntax   vgenmacwb3 {Oop [,low][,cfgX]} vx, vy, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN_CFGX        vec_t                      Configuration register
              3    IN1_V32        vec_t                      Input vector operand
Operands
              4    IN2_V32        vec_t                      Input vector operand
              5    IN3_V40        vec40_t                    Output vector operand
              6    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vec_t vcfgIn;
              vprex_t vecPred;
              ...
              vRes = vgenmacwb3_v32_v32_v40_low_p (8, vcfgIn, vIn, vIn2, vRes, vecPred);

                   IN_VPR last operand is relevant only for vgenmacwb3_v32_v32_v40_low_p
Comments      1.
                   version.


Main table → Generic → Generic Multiply-Accumulate → 16x8 MAC3 into Two Words
Intrinsic     vgenmacwb3_v32_v32_v40[_p]
name
Spec syntax   vgenmacwb3 {Oop [,low][,cfgX]} vx, vy, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN_CFGX        vec_t                      Configuration register
              3    IN1_V32        vec_t                      Input vector operand
Operands
              4    IN2_V32        vec_t                      Input vector operand
              5    IN3_V40        vec40_t                    Output vector operand
              6    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vec_t vcfgIn;
              vprex_t vecPred;
              ...
              vRes = vgenmacwb3_v32_v32_v40_p (8, vcfgIn, vIn, vIn2, vRes, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vgenmacwb3_v32_v32_v40_p
               version.


Main table → Generic → Generic Multiply-Accumulate → 16x8 MAC3 into Two Words
Intrinsic     vgenmacwb3_v32_v32_c32_v40_low[_p]
name
Spec syntax   vgenmacwb3 {Oop [,low][,cfgX]} vx, vy, vcWp, voz[0], ?vprX

Return type   vec40_t

1    OOP            uint8     1..8             Number of atomic operations
              2    IN_CFGX        vec_t                      Configuration register
              3    IN1_V32        vec_t                      Input vector operand
              4    IN2_V32        vec_t                      Input vector operand
Operands
              5    IN3_C32        coef_t                     Coefficient operand
              6    IN3_PART       uint8     LOW,HIGH         Word part which is used for operand 5
              7    IN4_V40        vec40_t                    Output vector operand
              8    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec40_t vRes;
              vec_t vcfgIn;
C example     coef_t vcoefIn;
              vprex_t vecPred;
              ...
              vRes = vgenmacwb3_v32_v32_c32_v40_low_p (8, vcfgIn, vIn, vIn2, vcoefIn, LOW, vRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vgenmacwb3_v32_v32_c32_v40_low_p version.


Main table → Generic → Generic Multiply-Accumulate → 16x8 MAC3 into Two Words
Intrinsic     vgenmacwb3_v32_v32_c32_v40[_p]
name
Spec syntax   vgenmacwb3 {Oop [,low][,cfgX]} vx, vy, vcWp, voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN_CFGX        vec_t                      Configuration register
              3    IN1_V32        vec_t                      Input vector operand
              4    IN2_V32        vec_t                      Input vector operand
Operands
              5    IN3_C32        coef_t                     Coefficient operand
              6    IN3_PART       uint8     LOW,HIGH         Word part which is used for operand 5
              7    IN4_V40        vec40_t                    Output vector operand
              8    IN_VPR         vprex_t                    Vector predicate operand
            vec_t vIn;
            vec_t vIn2;
            vec40_t vRes;
            vec_t vcfgIn;
C example   coef_t vcoefIn;
            vprex_t vecPred;
            ...
            vRes = vgenmacwb3_v32_v32_c32_v40_p (8, vcfgIn, vIn, vIn2, vcoefIn, LOW, vRes, vecPred);

                 IN_VPR last operand is relevant only for vgenmacwb3_v32_v32_c32_v40_p
Comments    1.
                 version.

Main table → Generic → Generic Multiply-Accumulate → 16x8 MAC3 into Two Words
