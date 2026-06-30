# Division → Divide → Vector Divide With Exponent

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Division → Divide → Vector Divide With Exponent

Vector Divide With Exponent

Vector Divide With Exponent
Produces a inverse square root on the first source. The numerator 216-k is determined by the first
16-bit source unsigned number varies from zero to 216-1. The second source is a 16-bit signed
exponent value. The destinations are 16-bit unsigned mantissa and 16-bit signed exponent
results.
Available Switches
None
Intrinsic Names
vdive_v32_v32_v32_v32
Instruction details in the instruction set specification
Intrinsic     vdive_v32_v32_v32_v32[_p]
name
Spec syntax   vdive vx[X]l, vy[Y]l, vz1[Z]l,vz2[Z]l, ?vprX

Return type   vec_t

              1    IN1_V32        vec_t                      Input vector operand

              2    IN1_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             1

              3    IN1_PART       uint8     LOW,HIGH         Word part which is used for operand 1
              4    IN2_V32        vec_t                      Input vector operand

              5    IN2_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             4
Operands      6    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 4
              7    RES2_V32       vec_t                      Input vector result operand
                                                             Offset for the first DW used from the first
              8    RES1_OFST      uint8     0..7
                                                             result operand

              9
                                                             Offset for the first DW used from the
                   RES2_OFST      uint8     0..7

second result operand
              10   IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes1;
C example     vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vdive_v32_v32_v32_v32_p (vIn, 0, LOW, vIn2, 0, LOW, vRes2, 0, 0, vecPred);

                   IN_VPR last operand is relevant only for vdive_v32_v32_v32_v32_p
              1.
                   version.
                   This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).
Comments
                   The vdive_v32_v32_v32_v32_p intrinsic has different latency in case the
                   Demapper block is installed/not installed on the HW. When Demapper is not
                   installed, 1/2 cycles are added after the generated vector instruction. The SDT
              3.
                   default is "Demapper installed". Therefore, for ensuring correct execution on
                   the HW, the -mno-demapper Compiler switch must be specified in case
                   Demapper is not installed.


Main table → Division → Divide → Vector Divide With Exponent
