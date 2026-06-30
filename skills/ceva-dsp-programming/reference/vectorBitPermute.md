# Bit Manipulation → Bit Permute → Vector Bit Permute

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Bit Manipulation → Bit Permute → Vector Bit Permute

Vector Bit Permute

Vector Bit Permute
Performs 32-bit permutation according to specified locations from a source into destination.
Available Switches
      When used, the vz[0]-vz[7] registers are cleared (excluding vz[Z] register) according to
clr
      vprX.
Intrinsic Names
vbpermute_v32_v32_v32_clr_p_5p
vbpermute_v32_v32_v32_p_5p
Instruction details in the instruction set specification
Intrinsic     vbpermute_v32_v32_v32_clr_p_5p
name

Spec syntax   vbpermute {[clr]} vx[0], vy[Y], vz[Z], ?vprX

Return type   vec_t

              1    IN1_V32        vec_t                      Input vector operand
              2    IN2_V32        vec_t                      Input vector operand

              3    IN2_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
Operands                                                     2

                                                             Offset for the first DW used from the
              4    OUT_OFST       uint8     0..7
                                                             result operand
              5    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vbpermute_v32_v32_v32_clr_p_5p (vIn, vIn2, 0, 0, vecPred);

Comments


Main table → Bit Manipulation → Bit Permute → Vector Bit Permute
Intrinsic     vbpermute_v32_v32_v32_p_5p
name
Spec syntax   vbpermute {[clr]} vx[0], vy[Y], vz[Z], ?vprX

Return type   vec_t

              1    IN1_V32        vec_t                      Input vector operand
              2    IN2_V32        vec_t                      Input vector operand

              3    IN2_OFST       uint8     0..7
                                                             Offset for the first DW used from operand
Operands                                                     2

              4
                                                             Offset for the first DW used from the
                   OUT_OFST       uint8     0..7
                                                             result operand
              5    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vbpermute_v32_v32_v32_p_5p (vIn, vIn2, 0, 0, vecPred);

Comments


Main table → Bit Manipulation → Bit Permute → Vector Bit Permute
