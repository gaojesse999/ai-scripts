# Division → Square Root → Vector Square Root

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Division → Square Root → Vector Square Root

Vector Square Root

Vector Square Root
Performs square-root on a source. The source is unsigned 16-bit number varies from zero to
65535. The destination is positive signed 16-bit number.
Available Switches
None
Intrinsic Names
vsqrt_v32_v32
Instruction details in the instruction set specification
Intrinsic     vsqrt_v32_v32[_p]
name
Spec syntax   vsqrt vx[X]l, vz[Z]l, ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                     Input vector operand

              2    IN1_OFST        uint8      0..7
                                                             Offset for the first DW used from operand
                                                             1
Operands
                                                             Offset for the first DW used from the
              3    OUT_OFST        uint8      0..7
                                                             result operand
              4    IN_VPR          vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vsqrt_v32_v32_p (vIn, 0, 0, vecPred);

              1.   IN_VPR last operand is relevant only for vsqrt_v32_v32_p version.
                   The vsqrt_v32_v32_p intrinsic has different latency in case the Demapper
                   block is installed/not installed on the HW. When Demapper is not installed,

Comments           1/2 cycles are added after the generated vector instruction. The SDT default is
              2.
                   "Demapper installed". Therefore, for ensuring correct execution on the HW,
                   the -mno-demapper Compiler switch must be specified in case Demapper is
                   not installed.


Main table → Division → Square Root → Vector Square Root
