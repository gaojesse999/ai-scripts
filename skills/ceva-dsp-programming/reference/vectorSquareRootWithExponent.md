# Division → Square Root → Vector Square Root With Exponent

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Division → Square Root → Vector Square Root With Exponent

Vector Square Root With Exponent

Vector Square Root With Exponent
Produces a square root of the source. The second source is a 16-bit signed exponent value. The
destination is unsigned 16-bit number represented as U(16,8) where the 8 MSBs are the integer
part of the root and the 8 LSBs are the fraction part of the root.
Available Switches
None
Intrinsic Names
vsqrte_v32_v32_v32_v32
Instruction details in the instruction set specification
Intrinsic     vsqrte_v32_v32_v32_v32[_p]
name
Spec syntax   vsqrte vx[X]l, vy[Y]l, vz1[Z]l,vz2[Z]l, ?vprX

Return type   vec_t

              1    IN1_V32        vec_t                       Input vector operand

              2    IN1_OFST       uint8     0..7
                                                              Offset for the first DW used from operand
                                                              1

              3    IN1_PART       uint8     LOW,HIGH          Word part which is used for operand 1
              4    IN2_V32        vec_t                       Input vector operand

              5    IN2_OFST       uint8     0..7
                                                              Offset for the first DW used from operand
                                                              4
Operands      6    IN2_PART       uint8     LOW,HIGH          Word part which is used for operand 4
              7    RES2_V32       vec_t                       Input vector result operand
                                                              Offset for the first DW used from the first
              8    RES1_OFST      uint8     0..7
                                                              result operand

              9
                                                              Offset for the first DW used from the
                   RES2_OFST      uint8     0..7
                                                              second result operand
              10   IN_VPR         vprex_t                     Vector predicate operand

vec_t vExponentValue;
              vec_t vIn;
              vec_t vRes1;
C example     vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vsqrte_v32_v32_v32_v32_p (vIn, 0, LOW, vExponentValue, 0, LOW, vRes2, 0, 0, vecPred);

                   IN_VPR last operand is relevant only for vsqrte_v32_v32_v32_v32_p
              1.
                   version.
                   This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).
Comments
                   The vsqrte_v32_v32_v32_v32_p intrinsic has different latency in case the
                   Demapper block is installed/not installed on the HW. When Demapper is not
                   installed, 1/2 cycles are added after the generated vector instruction. The SDT
              3.
                   default is "Demapper installed". Therefore, for ensuring correct execution on
                   the HW, the -mno-demapper Compiler switch must be specified in case
                   Demapper is not installed.


Main table → Division → Square Root → Vector Square Root With Exponent
