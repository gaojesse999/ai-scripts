# Division → Divide → Vector Divide Word

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Division → Divide → Vector Divide Word

Vector Divide Word

Vector Divide Word
Performs 2y divided by a source. The numerator 2y is determined by the 16-bit source value. The
source is unsigned number varies from zero to 65535. The destination is 16-bit wide signed or
unsigned depends on VSHFD mode bit.
Available Switches
b        When used, the shift-values are written into bytes
w        When used, the shift-values are written into words
Intrinsic Names
vdivw_v32_v32_v32_b
vdivw_v32_v32_v32_w
vdivw_v32_v32
Instruction details in the instruction set specification
Intrinsic     vdivw_v32_v32_v32_b[_p]
name
Spec syntax   vdivw {b} vx[X]l, vz1[Z]l,vz2[Z], ?vprX

Return type   vec_t

              1    IN1_V32        vec_t                      Input vector operand

              2    IN1_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             1

              3    IN2_V32        vec_t                      Input vector operand

Operands                                                     Offset for the first DW used from the first
              4    RES1_OFST      uint8     0..7
                                                             result operand
                                                             Offset for the first DW used from the
              5    RES2_OFST      uint8     0..7
                                                             second result operand
              6    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vExponentAndSrc;
              vec_t vRes1;
              vec_t vRes2;
C example     vprex_t vecPred;
              ...
              vRes1 = vdivw_v32_v32_v32_b_p (vExponentAndSrc, 0, vRes2, 0, 0, vecPred);

              1.   IN_VPR last operand is relevant only for vdivw_v32_v32_v32_b_p version.
                   This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_OFST).
Comments           The vdivw_v32_v32_v32_b_p intrinsic has different latency in case the
                   Demapper block is installed/not installed on the HW. When Demapper is not
              3.
                   installed, 1/2 cycles are added after the generated vector instruction. The SDT
                   default is "Demapper installed". Therefore, for ensuring correct execution on
                   the HW, the -mno-demapper Compiler switch must be specified in case
                   Demapper is not installed.


Main table → Division → Divide → Vector Divide Word
Intrinsic     vdivw_v32_v32_v32_w[_p]
name
Spec syntax   vdivw {w} vx[X]l, vz1[Z]l, vz2[Z]l, ?vprX

Return type   vec_t

              1    IN1_V32        vec_t                     Input vector operand

              2    IN1_OFST       uint8     0..7
                                                            Offset for the first DW used from operand
                                                            1

              3    IN2_V32        vec_t                     Input vector operand
Operands                                                    Offset for the first DW used from the first
              4    RES1_OFST      uint8     0..7
                                                            result operand

Offset for the first DW used from the
              5    RES2_OFST      uint8     0..7
                                                            second result operand
              6    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vExponentAndSrc;
              vec_t vRes1;
              vec_t vRes2;
C example     vprex_t vecPred;
              ...
              vRes1 = vdivw_v32_v32_v32_w_p (vExponentAndSrc, 0, vRes2, 0, 0, vecPred);

              1.   IN_VPR last operand is relevant only for vdivw_v32_v32_v32_w_p version.
                   This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_OFST).
Comments           The vdivw_v32_v32_v32_w_p intrinsic has different latency in case the
                   Demapper block is installed/not installed on the HW. When Demapper is not
              3.
                   installed, 1/2 cycles are added after the generated vector instruction. The SDT
                   default is "Demapper installed". Therefore, for ensuring correct execution on
                   the HW, the -mno-demapper Compiler switch must be specified in case
                   Demapper is not installed.


Main table → Division → Divide → Vector Divide Word
Intrinsic     vdivw_v32_v32[_p]
name
Spec syntax   vdivw vx[X]l, vz[Z]l, ?vprX

Return type   vec_t

              1    IN1_V32        vec_t                      Input vector operand

              2    IN1_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
                                                             1
Operands
                                                             Offset for the first DW used from the
              3    OUT_OFST       uint8     0..7
                                                             result operand
              4    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vExponentAndSrc;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vdivw_v32_v32_p (vExponentAndSrc, 0, 0, vecPred);

              1.   IN_VPR last operand is relevant only for vdivw_v32_v32_p version.
                   The vdivw_v32_v32_p intrinsic has different latency in case the Demapper

block is installed/not installed on the HW. When Demapper is not installed,
Comments           1/2 cycles are added after the generated vector instruction. The SDT default is
              2.
                   "Demapper installed". Therefore, for ensuring correct execution on the HW,
                   the -mno-demapper Compiler switch must be specified in case Demapper is
                   not installed.


Main table → Division → Divide → Vector Divide Word
