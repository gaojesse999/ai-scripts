# Comparison And Predicates → Compare → Vector Compare

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Comparison And Predicates → Compare → Vector Compare

Vector Compare

Vector Compare
Performs comparison between two sources and set vector predicate bits accordingly. The sources
are 32-bit wide. The destination is 8-bit VPREX.
Available Switches
      Number of atomic operations. An atomic operation is defined by as a single comparison
Oop
      operation. 1op ≤ Oop ≤ 8op
dup The switch can be used only when Oop is 1op.
hi    When used, 'hi' switch is indicating that the result is written to the high VPREX[15:8].
      When used, 'low' switch is indicating that the result is written to the low VPREX[7:0]
low
      (default).
      When used, the sources represented by the 32-bits of the vector parts are treated as
uu
      unsigned values (by default they are treated as signed values).
Intrinsic Names
vcmp_v32_c32_vpr
vcmp_v32_c32_vpr_dup
vcmp_v32_c32_vpr_dup_hi
vcmp_v32_c32_vpr_dup_low
vcmp_v32_c32_vpr_dup_uu
vcmp_v32_c32_vpr_dup_uu_hi
vcmp_v32_c32_vpr_dup_uu_low
vcmp_v32_c32_vpr_eq
vcmp_v32_c32_vpr_eq_dup
vcmp_v32_c32_vpr_eq_dup_hi
vcmp_v32_c32_vpr_eq_dup_low
vcmp_v32_c32_vpr_eq_dup_uu
vcmp_v32_c32_vpr_eq_dup_uu_hi
vcmp_v32_c32_vpr_eq_dup_uu_low
vcmp_v32_c32_vpr_eq_hi
vcmp_v32_c32_vpr_eq_low
vcmp_v32_c32_vpr_eq_uu
vcmp_v32_c32_vpr_eq_uu_hi
vcmp_v32_c32_vpr_eq_uu_low
vcmp_v32_c32_vpr_ge
vcmp_v32_c32_vpr_ge_dup
vcmp_v32_c32_vpr_ge_dup_hi
vcmp_v32_c32_vpr_ge_dup_low
vcmp_v32_c32_vpr_ge_dup_uu
vcmp_v32_c32_vpr_ge_dup_uu_hi
vcmp_v32_c32_vpr_ge_dup_uu_low
vcmp_v32_c32_vpr_ge_hi
vcmp_v32_c32_vpr_ge_low
vcmp_v32_c32_vpr_ge_uu
vcmp_v32_c32_vpr_ge_uu_hi
vcmp_v32_c32_vpr_ge_uu_low
vcmp_v32_c32_vpr_gt
vcmp_v32_c32_vpr_gt_dup
vcmp_v32_c32_vpr_gt_dup_hi
vcmp_v32_c32_vpr_gt_dup_low
vcmp_v32_c32_vpr_gt_dup_uu
vcmp_v32_c32_vpr_gt_dup_uu_hi
vcmp_v32_c32_vpr_gt_dup_uu_low
vcmp_v32_c32_vpr_gt_hi
vcmp_v32_c32_vpr_gt_low
vcmp_v32_c32_vpr_gt_uu
vcmp_v32_c32_vpr_gt_uu_hi
vcmp_v32_c32_vpr_gt_uu_low
vcmp_v32_c32_vpr_hi
vcmp_v32_c32_vpr_le
vcmp_v32_c32_vpr_le_dup
vcmp_v32_c32_vpr_le_dup_hi
vcmp_v32_c32_vpr_le_dup_low
vcmp_v32_c32_vpr_le_dup_uu
vcmp_v32_c32_vpr_le_dup_uu_hi
vcmp_v32_c32_vpr_le_dup_uu_low
vcmp_v32_c32_vpr_le_hi
vcmp_v32_c32_vpr_le_low
vcmp_v32_c32_vpr_le_uu

vcmp_v32_c32_vpr_le_uu_hi
vcmp_v32_c32_vpr_le_uu_low
vcmp_v32_c32_vpr_low
vcmp_v32_c32_vpr_lt
vcmp_v32_c32_vpr_lt_dup
vcmp_v32_c32_vpr_lt_dup_hi
vcmp_v32_c32_vpr_lt_dup_low
vcmp_v32_c32_vpr_lt_dup_uu
vcmp_v32_c32_vpr_lt_dup_uu_hi
vcmp_v32_c32_vpr_lt_dup_uu_low
vcmp_v32_c32_vpr_lt_hi
vcmp_v32_c32_vpr_lt_low
vcmp_v32_c32_vpr_lt_uu
vcmp_v32_c32_vpr_lt_uu_hi
vcmp_v32_c32_vpr_lt_uu_low
vcmp_v32_c32_vpr_neq
vcmp_v32_c32_vpr_neq_dup
vcmp_v32_c32_vpr_neq_dup_hi
vcmp_v32_c32_vpr_neq_dup_low
vcmp_v32_c32_vpr_neq_dup_uu
vcmp_v32_c32_vpr_neq_dup_uu_hi
vcmp_v32_c32_vpr_neq_dup_uu_low
vcmp_v32_c32_vpr_neq_hi
vcmp_v32_c32_vpr_neq_low
vcmp_v32_c32_vpr_neq_uu
vcmp_v32_c32_vpr_neq_uu_hi
vcmp_v32_c32_vpr_neq_uu_low
vcmp_v32_c32_vpr_uu
vcmp_v32_c32_vpr_uu_hi
vcmp_v32_c32_vpr_uu_low
vcmp_v32_v32_vpr_nrng
vcmp_v32_v32_vpr_nrng_dup
vcmp_v32_v32_vpr_nrng_dup_uu
vcmp_v32_v32_vpr_nrng_uu
vcmp_v32_v32_vpr_rng
vcmp_v32_v32_vpr_rng_dup
vcmp_v32_v32_vpr_rng_dup_uu
vcmp_v32_v32_vpr_rng_uu
vcmp_v32_v32_vpr
vcmp_v32_v32_vpr_dup
vcmp_v32_v32_vpr_dup_hi
vcmp_v32_v32_vpr_dup_low
vcmp_v32_v32_vpr_dup_uu
vcmp_v32_v32_vpr_dup_uu_hi
vcmp_v32_v32_vpr_dup_uu_low
vcmp_v32_v32_vpr_eq
vcmp_v32_v32_vpr_eq_dup
vcmp_v32_v32_vpr_eq_dup_hi
vcmp_v32_v32_vpr_eq_dup_low
vcmp_v32_v32_vpr_eq_dup_uu
vcmp_v32_v32_vpr_eq_dup_uu_hi
vcmp_v32_v32_vpr_eq_dup_uu_low
vcmp_v32_v32_vpr_eq_hi
vcmp_v32_v32_vpr_eq_low
vcmp_v32_v32_vpr_eq_uu
vcmp_v32_v32_vpr_eq_uu_hi
vcmp_v32_v32_vpr_eq_uu_low
vcmp_v32_v32_vpr_ge
vcmp_v32_v32_vpr_ge_dup
vcmp_v32_v32_vpr_ge_dup_hi
vcmp_v32_v32_vpr_ge_dup_low
vcmp_v32_v32_vpr_ge_dup_uu
vcmp_v32_v32_vpr_ge_dup_uu_hi
vcmp_v32_v32_vpr_ge_dup_uu_low
vcmp_v32_v32_vpr_ge_hi
vcmp_v32_v32_vpr_ge_low
vcmp_v32_v32_vpr_ge_uu
vcmp_v32_v32_vpr_ge_uu_hi
vcmp_v32_v32_vpr_ge_uu_low
vcmp_v32_v32_vpr_gt
vcmp_v32_v32_vpr_gt_dup
vcmp_v32_v32_vpr_gt_dup_hi
vcmp_v32_v32_vpr_gt_dup_low
vcmp_v32_v32_vpr_gt_dup_uu
vcmp_v32_v32_vpr_gt_dup_uu_hi
vcmp_v32_v32_vpr_gt_dup_uu_low
vcmp_v32_v32_vpr_gt_hi
vcmp_v32_v32_vpr_gt_low
vcmp_v32_v32_vpr_gt_uu
vcmp_v32_v32_vpr_gt_uu_hi
vcmp_v32_v32_vpr_gt_uu_low
vcmp_v32_v32_vpr_hi
vcmp_v32_v32_vpr_le
vcmp_v32_v32_vpr_le_dup
vcmp_v32_v32_vpr_le_dup_hi
vcmp_v32_v32_vpr_le_dup_low
vcmp_v32_v32_vpr_le_dup_uu
vcmp_v32_v32_vpr_le_dup_uu_hi
vcmp_v32_v32_vpr_le_dup_uu_low
vcmp_v32_v32_vpr_le_hi
vcmp_v32_v32_vpr_le_low
vcmp_v32_v32_vpr_le_uu
vcmp_v32_v32_vpr_le_uu_hi
vcmp_v32_v32_vpr_le_uu_low
vcmp_v32_v32_vpr_low
vcmp_v32_v32_vpr_lt
vcmp_v32_v32_vpr_lt_dup
vcmp_v32_v32_vpr_lt_dup_hi

vcmp_v32_v32_vpr_lt_dup_low
vcmp_v32_v32_vpr_lt_dup_uu
vcmp_v32_v32_vpr_lt_dup_uu_hi
vcmp_v32_v32_vpr_lt_dup_uu_low
vcmp_v32_v32_vpr_lt_hi
vcmp_v32_v32_vpr_lt_low
vcmp_v32_v32_vpr_lt_uu
vcmp_v32_v32_vpr_lt_uu_hi
vcmp_v32_v32_vpr_lt_uu_low
vcmp_v32_v32_vpr_neq
vcmp_v32_v32_vpr_neq_dup
vcmp_v32_v32_vpr_neq_dup_hi
vcmp_v32_v32_vpr_neq_dup_low
vcmp_v32_v32_vpr_neq_dup_uu
vcmp_v32_v32_vpr_neq_dup_uu_hi
vcmp_v32_v32_vpr_neq_dup_uu_low
vcmp_v32_v32_vpr_neq_hi
vcmp_v32_v32_vpr_neq_low
vcmp_v32_v32_vpr_neq_uu
vcmp_v32_v32_vpr_neq_uu_hi
vcmp_v32_v32_vpr_neq_uu_low
vcmp_v32_v32_vpr_uu
vcmp_v32_v32_vpr_uu_hi
vcmp_v32_v32_vpr_uu_low
vcmp_v32_imm32_6_vpr
vcmp_v32_imm32_6_vpr_dup
vcmp_v32_imm32_6_vpr_dup_uu
vcmp_v32_imm32_6_vpr_eq
vcmp_v32_imm32_6_vpr_eq_dup
vcmp_v32_imm32_6_vpr_eq_dup_uu
vcmp_v32_imm32_6_vpr_eq_uu
vcmp_v32_imm32_6_vpr_ge
vcmp_v32_imm32_6_vpr_ge_dup
vcmp_v32_imm32_6_vpr_ge_dup_uu
vcmp_v32_imm32_6_vpr_ge_uu
vcmp_v32_imm32_6_vpr_gt
vcmp_v32_imm32_6_vpr_gt_dup
vcmp_v32_imm32_6_vpr_gt_dup_uu
vcmp_v32_imm32_6_vpr_gt_uu
vcmp_v32_imm32_6_vpr_le
vcmp_v32_imm32_6_vpr_le_dup
vcmp_v32_imm32_6_vpr_le_dup_uu
vcmp_v32_imm32_6_vpr_le_uu
vcmp_v32_imm32_6_vpr_lt
vcmp_v32_imm32_6_vpr_lt_dup
vcmp_v32_imm32_6_vpr_lt_dup_uu
vcmp_v32_imm32_6_vpr_lt_uu
vcmp_v32_imm32_6_vpr_neq
vcmp_v32_imm32_6_vpr_neq_dup
vcmp_v32_imm32_6_vpr_neq_dup_uu
vcmp_v32_imm32_6_vpr_neq_uu
vcmp_v32_imm32_6_vpr_uu
Instruction details in the instruction set specification
Intrinsic     vcmp_v32_c32_vpr
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr (8, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_dup
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                      Input vector operand
Operands
              2    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;

C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_dup (vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_dup_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                      Input vector operand
Operands
              2    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_dup_hi (vIn, vcoefIn);
Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_dup_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                    Input vector operand
Operands
              2    IN2_C32        coef_t                   Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_dup_low (vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_dup_uu
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                    Input vector operand
Operands
              2    IN2_C32        coef_t                   Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_dup_uu (vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_dup_uu_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                    Input vector operand
Operands
              2    IN2_C32        coef_t                   Coefficient operand
              vec_t vIn;
C example     coef_t vcoefIn;
              vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_dup_uu_hi (vIn, vcoefIn);

Comments

Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_dup_uu_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                      Input vector operand
Operands
              2    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_dup_uu_low (vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_eq
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_eq (8, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_eq_dup
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t
              1    IN1_V32        vec_t                    Input vector operand
Operands
              2    IN2_C32        coef_t                   Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_eq_dup (vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_eq_dup_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                    Input vector operand
Operands
              2    IN2_C32        coef_t                   Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_eq_dup_hi (vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare

Intrinsic     vcmp_v32_c32_vpr_eq_dup_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                    Input vector operand
Operands
              2    IN2_C32        coef_t                   Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_eq_dup_low (vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_eq_dup_uu
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    IN1_V32       vec_t                     Input vector operand
Operands
              2    IN2_C32       coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_eq_dup_uu (vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_eq_dup_uu_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    IN1_V32       vec_t                     Input vector operand
Operands
              2    IN2_C32       coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_eq_dup_uu_hi (vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_eq_dup_uu_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    IN1_V32       vec_t                     Input vector operand
Operands
              2    IN2_C32       coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_eq_dup_uu_low (vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_eq_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_eq_hi (8, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_eq_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_eq_low (8, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_eq_uu
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_eq_uu (8, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_eq_uu_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_C32        coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_eq_uu_hi (8, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare

Intrinsic     vcmp_v32_c32_vpr_eq_uu_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_C32        coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_eq_uu_low (8, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_ge
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_ge (8, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_ge_dup
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                      Input vector operand
Operands
              2    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_ge_dup (vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_ge_dup_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                      Input vector operand
Operands
              2    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_ge_dup_hi (vIn, vcoefIn);

Comments

Main table → Comparison And Predicates → Compare → Vector Compare

Intrinsic     vcmp_v32_c32_vpr_ge_dup_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    IN1_V32          vec_t                  Input vector operand
Operands
              2    IN2_C32          coef_t                 Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_ge_dup_low (vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_ge_dup_uu
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    IN1_V32          vec_t                  Input vector operand
Operands
              2    IN2_C32          coef_t                 Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_ge_dup_uu (vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_ge_dup_uu_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    IN1_V32          vec_t                  Input vector operand
Operands
              2    IN2_C32          coef_t                 Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_ge_dup_uu_hi (vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_ge_dup_uu_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                      Input vector operand
Operands
              2    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_ge_dup_uu_low (vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_ge_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_ge_hi (8, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_ge_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

Operands      1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand
              3    IN2_C32        coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_ge_low (8, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_ge_uu
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_C32        coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_ge_uu (8, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_ge_uu_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_C32        coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_ge_uu_hi (8, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare

Intrinsic     vcmp_v32_c32_vpr_ge_uu_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP              uint8    1..8            Number of atomic operations
Operands      2    IN1_V32          vec_t                    Input vector operand
              3    IN2_C32          coef_t                   Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_ge_uu_low (8, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_gt
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP              uint8    1..8            Number of atomic operations
Operands      2    IN1_V32          vec_t                    Input vector operand
              3    IN2_C32          coef_t                   Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_gt (8, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_gt_dup
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    IN1_V32          vec_t                    Input vector operand
Operands
              2    IN2_C32          coef_t                   Coefficient operand
              vec_t vIn;
C example     coef_t vcoefIn;
              vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_gt_dup (vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_gt_dup_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                     Input vector operand
Operands
              2    IN2_C32        coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_gt_dup_hi (vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare

Intrinsic     vcmp_v32_c32_vpr_gt_dup_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                     Input vector operand
Operands
              2    IN2_C32        coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_gt_dup_low (vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_gt_dup_uu
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                     Input vector operand
Operands
              2    IN2_C32        coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_gt_dup_uu (vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_gt_dup_uu_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                    Input vector operand
Operands
              2    IN2_C32        coef_t                   Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_gt_dup_uu_hi (vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_gt_dup_uu_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                    Input vector operand
Operands
              2    IN2_C32        coef_t                   Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_gt_dup_uu_low (vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_gt_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_gt_hi (8, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_gt_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_gt_low (8, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_gt_uu
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_gt_uu (8, vIn, vcoefIn);

Comments

Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_gt_uu_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_gt_uu_hi (8, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare

Intrinsic     vcmp_v32_c32_vpr_gt_uu_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_gt_uu_low (8, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands
              2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32         coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_hi (8, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_le
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP             uint8    1..8             Number of atomic operations
Operands      2    IN1_V32         vec_t                     Input vector operand
              3    IN2_C32         coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_le (8, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_le_dup
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    IN1_V32         vec_t                     Input vector operand
Operands
              2    IN2_C32         coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_le_dup (vIn, vcoefIn);

Comments

Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_le_dup_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                     Input vector operand
Operands
              2    IN2_C32        coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_le_dup_hi (vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_le_dup_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                     Input vector operand
Operands
              2    IN2_C32        coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_le_dup_low (vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_le_dup_uu
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                     Input vector operand
Operands
              2    IN2_C32        coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_le_dup_uu (vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_le_dup_uu_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    IN1_V32         vec_t                     Input vector operand
Operands
              2    IN2_C32         coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_le_dup_uu_hi (vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_le_dup_uu_low
name

Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    IN1_V32         vec_t                     Input vector operand
Operands
              2    IN2_C32         coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_le_dup_uu_low (vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_le_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP             uint8    1..8             Number of atomic operations
Operands      2    IN1_V32         vec_t                     Input vector operand
              3    IN2_C32         coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_le_hi (8, vIn, vcoefIn);
Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_le_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_le_low (8, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_le_uu
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_le_uu (8, vIn, vcoefIn);

Comments

Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_le_uu_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

Operands      1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_le_uu_hi (8, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_le_uu_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_le_uu_low (8, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_low (8, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_lt
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP             uint8     1..8             Number of atomic operations
Operands      2    IN1_V32         vec_t                      Input vector operand
              3    IN2_C32         coef_t                     Coefficient operand
              vec_t vIn;

coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_lt (8, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_lt_dup
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    IN1_V32         vec_t                      Input vector operand
Operands
              2    IN2_C32         coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_lt_dup (vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_lt_dup_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    IN1_V32         vec_t                      Input vector operand
Operands
              2    IN2_C32         coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_lt_dup_hi (vIn, vcoefIn);
Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_lt_dup_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                     Input vector operand
Operands
              2    IN2_C32        coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_lt_dup_low (vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_lt_dup_uu
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                     Input vector operand
Operands
              2    IN2_C32        coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_lt_dup_uu (vIn, vcoefIn);

Comments

Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_lt_dup_uu_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                     Input vector operand
Operands
              2    IN2_C32        coef_t                    Coefficient operand
              vec_t vIn;
C example     coef_t vcoefIn;
              vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_lt_dup_uu_hi (vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_lt_dup_uu_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    IN1_V32         vec_t                      Input vector operand
Operands
              2    IN2_C32         coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_lt_dup_uu_low (vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_lt_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP             uint8     1..8             Number of atomic operations
Operands      2    IN1_V32         vec_t                      Input vector operand
              3    IN2_C32         coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_lt_hi (8, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_lt_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t
              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_lt_low (8, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_lt_uu
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_lt_uu (8, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_lt_uu_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_lt_uu_hi (8, vIn, vcoefIn);

Comments

Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_lt_uu_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_lt_uu_low (8, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_neq
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;

coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_neq (8, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_neq_dup
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                      Input vector operand
Operands
              2    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_neq_dup (vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_neq_dup_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                    Input vector operand
Operands
              2    IN2_C32        coef_t                   Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_neq_dup_hi (vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_neq_dup_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                    Input vector operand
Operands
              2    IN2_C32        coef_t                   Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_neq_dup_low (vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_neq_dup_uu
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t
              1   IN1_V32        vec_t                     Input vector operand
Operands
              2   IN2_C32        coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_neq_dup_uu (vIn, vcoefIn);

Comments

Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_neq_dup_uu_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1   IN1_V32        vec_t                     Input vector operand
Operands
              2   IN2_C32        coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_neq_dup_uu_hi (vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_neq_dup_uu_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1   IN1_V32        vec_t                     Input vector operand
Operands
              2   IN2_C32        coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_neq_dup_uu_low (vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_neq_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP              uint8    1..8            Number of atomic operations
Operands      2    IN1_V32          vec_t                    Input vector operand
              3    IN2_C32          coef_t                   Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_neq_hi (8, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_neq_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP              uint8    1..8            Number of atomic operations
Operands      2    IN1_V32          vec_t                    Input vector operand
              3    IN2_C32          coef_t                   Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_neq_low (8, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_neq_uu
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP              uint8    1..8            Number of atomic operations
Operands      2    IN1_V32          vec_t                    Input vector operand
              3    IN2_C32          coef_t                   Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_neq_uu (8, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_neq_uu_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_C32        coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_neq_uu_hi (8, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_neq_uu_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_C32        coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_neq_uu_low (8, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_uu
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t
              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;

coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_uu (8, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_uu_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_uu_hi (8, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_c32_vpr_uu_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_c32_vpr_uu_low (8, vIn, vcoefIn);

Comments

Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_nrng
name
Spec syntax   vcmp {Oop, rng_nrng [,dup_sw][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_nrng (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_nrng_dup
name
Spec syntax   vcmp {Oop, rng_nrng [,dup_sw][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                     Input vector operand
Operands
              2    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;

vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_nrng_dup (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_nrng_dup_uu
name
Spec syntax   vcmp {Oop, rng_nrng [,dup_sw][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                     Input vector operand
Operands
              2    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_nrng_dup_uu (vIn, vIn2);
Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_nrng_uu
name
Spec syntax   vcmp {Oop, rng_nrng [,dup_sw][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_nrng_uu (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_rng
name
Spec syntax   vcmp {Oop, rng_nrng [,dup_sw][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_rng (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_rng_dup
name
Spec syntax   vcmp {Oop, rng_nrng [,dup_sw][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

Operands      1    IN1_V32        vec_t                     Input vector operand
              2    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...

vecPredRes = vcmp_v32_v32_vpr_rng_dup (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_rng_dup_uu
name
Spec syntax   vcmp {Oop, rng_nrng [,dup_sw][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                     Input vector operand
Operands
              2    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_rng_dup_uu (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_rng_uu
name
Spec syntax   vcmp {Oop, rng_nrng [,dup_sw][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8    1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_rng_uu (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8              Number of atomic operations
Operands      2    IN1_V32        vec_t                       Input vector operand
              3    IN2_V32        vec_t                       Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_dup
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                       Input vector operand
Operands
              2    IN2_V32        vec_t                       Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_dup (vIn, vIn2);

Comments

Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_dup_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                       Input vector operand
Operands
              2    IN2_V32        vec_t                       Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_dup_hi (vIn, vIn2);
Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_dup_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    IN1_V32       vec_t                     Input vector operand
Operands
              2    IN2_V32       vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_dup_low (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_dup_uu
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    IN1_V32       vec_t                     Input vector operand
Operands
              2    IN2_V32       vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_dup_uu (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_dup_uu_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    IN1_V32       vec_t                     Input vector operand
Operands
              2    IN2_V32       vec_t                     Input vector operand
              vec_t vIn;
C example     vec_t vIn2;
              vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_dup_uu_hi (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_dup_uu_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                     Input vector operand
Operands
              2    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_dup_uu_low (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_eq
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_eq (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_eq_dup
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t
              1    IN1_V32       vec_t                     Input vector operand
Operands
              2    IN2_V32       vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_eq_dup (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_eq_dup_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    IN1_V32       vec_t                     Input vector operand
Operands
              2    IN2_V32       vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_eq_dup_hi (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_eq_dup_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    IN1_V32       vec_t                     Input vector operand
Operands

2    IN2_V32       vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_eq_dup_low (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_eq_dup_uu
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1   IN1_V32        vec_t                     Input vector operand
Operands
              2   IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_eq_dup_uu (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_eq_dup_uu_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1   IN1_V32        vec_t                     Input vector operand
Operands
              2   IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_eq_dup_uu_hi (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_eq_dup_uu_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1   IN1_V32        vec_t                     Input vector operand
Operands
              2   IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_eq_dup_uu_low (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_eq_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;

vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_eq_hi (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_eq_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_eq_low (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_eq_uu
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_eq_uu (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_eq_uu_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8    1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_eq_uu_hi (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_eq_uu_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8    1..8             Number of atomic operations

Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_eq_uu_low (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_ge
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_ge (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_ge_dup
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                     Input vector operand
Operands
              2    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_ge_dup (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_ge_dup_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                     Input vector operand
Operands
              2    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_ge_dup_hi (vIn, vIn2);

Comments

Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_ge_dup_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    IN1_V32          vec_t                  Input vector operand
Operands

2    IN2_V32          vec_t                  Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_ge_dup_low (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_ge_dup_uu
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    IN1_V32          vec_t                  Input vector operand
Operands
              2    IN2_V32          vec_t                  Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_ge_dup_uu (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_ge_dup_uu_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    IN1_V32          vec_t                  Input vector operand
Operands
              2    IN2_V32          vec_t                  Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_ge_dup_uu_hi (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_ge_dup_uu_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                     Input vector operand
Operands
              2    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_ge_dup_uu_low (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_ge_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;

vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_ge_hi (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_ge_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

Operands      1    OOP            uint8     1..8            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_ge_low (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_ge_uu
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_ge_uu (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_ge_uu_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_ge_uu_hi (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_ge_uu_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP              uint8   1..8             Number of atomic operations

Operands      2    IN1_V32          vec_t                    Input vector operand
              3    IN2_V32          vec_t                    Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_ge_uu_low (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_gt
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP              uint8   1..8             Number of atomic operations
Operands      2    IN1_V32          vec_t                    Input vector operand
              3    IN2_V32          vec_t                    Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_gt (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_gt_dup
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    IN1_V32          vec_t                    Input vector operand
Operands
              2    IN2_V32          vec_t                    Input vector operand
              vec_t vIn;
C example     vec_t vIn2;
              vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_gt_dup (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_gt_dup_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                    Input vector operand
Operands
              2    IN2_V32        vec_t                    Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_gt_dup_hi (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_gt_dup_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                    Input vector operand
Operands

2    IN2_V32        vec_t                    Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_gt_dup_low (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_gt_dup_uu
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                    Input vector operand
Operands
              2    IN2_V32        vec_t                    Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_gt_dup_uu (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_gt_dup_uu_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1   IN1_V32        vec_t                     Input vector operand
Operands
              2   IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_gt_dup_uu_hi (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_gt_dup_uu_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1   IN1_V32        vec_t                     Input vector operand
Operands
              2   IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_gt_dup_uu_low (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_gt_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t
              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;

vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_gt_hi (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_gt_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_gt_low (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_gt_uu
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_gt_uu (8, vIn, vIn2);

Comments

Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_gt_uu_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_gt_uu_hi (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_gt_uu_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8            Number of atomic operations

Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_gt_uu_low (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands
              2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_hi (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_le
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_le (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_le_dup
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                      Input vector operand
Operands
              2    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_le_dup (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_le_dup_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

1    IN1_V32        vec_t                    Input vector operand
Operands
              2    IN2_V32        vec_t                    Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_le_dup_hi (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_le_dup_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                    Input vector operand
Operands
              2    IN2_V32        vec_t                    Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_le_dup_low (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_le_dup_uu
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                    Input vector operand
Operands
              2    IN2_V32        vec_t                    Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_le_dup_uu (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_le_dup_uu_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                      Input vector operand
Operands
              2    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_le_dup_uu_hi (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_le_dup_uu_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                      Input vector operand
Operands
              2    IN2_V32        vec_t                      Input vector operand

vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_le_dup_uu_low (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_le_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_le_hi (8, vIn, vIn2);
Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_le_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_le_low (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_le_uu
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_le_uu (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_le_uu_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

Operands      1    OOP            uint8     1..8             Number of atomic operations

2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_le_uu_hi (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_le_uu_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_le_uu_low (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_low (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_lt
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_lt (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_lt_dup
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                      Input vector operand
Operands
              2    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_lt_dup (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_lt_dup_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                      Input vector operand
Operands
              2    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_lt_dup_hi (vIn, vIn2);
Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_lt_dup_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                    Input vector operand
Operands
              2    IN2_V32        vec_t                    Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_lt_dup_low (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_lt_dup_uu
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                    Input vector operand
Operands
              2    IN2_V32        vec_t                    Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_lt_dup_uu (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_lt_dup_uu_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                    Input vector operand
Operands

2    IN2_V32        vec_t                    Input vector operand
              vec_t vIn;
C example     vec_t vIn2;
              vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_lt_dup_uu_hi (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_lt_dup_uu_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                      Input vector operand
Operands
              2    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_lt_dup_uu_low (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_lt_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_lt_hi (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_lt_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t
              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_lt_low (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_lt_uu
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations

Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_lt_uu (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_lt_uu_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_lt_uu_hi (8, vIn, vIn2);

Comments

Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_lt_uu_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_lt_uu_low (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_neq
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_neq (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_neq_dup
name

Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                     Input vector operand
Operands
              2    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_neq_dup (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_neq_dup_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1   IN1_V32        vec_t                     Input vector operand
Operands
              2   IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_neq_dup_hi (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_neq_dup_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1   IN1_V32        vec_t                     Input vector operand
Operands
              2   IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_neq_dup_low (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_neq_dup_uu
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t
              1   IN1_V32        vec_t                    Input vector operand
Operands
              2   IN2_V32        vec_t                    Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_neq_dup_uu (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_neq_dup_uu_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

1   IN1_V32        vec_t                    Input vector operand
Operands
              2   IN2_V32        vec_t                    Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_neq_dup_uu_hi (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_neq_dup_uu_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1   IN1_V32        vec_t                    Input vector operand
Operands
              2   IN2_V32        vec_t                    Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_neq_dup_uu_low (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_neq_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP              uint8   1..8            Number of atomic operations
Operands      2    IN1_V32          vec_t                   Input vector operand
              3    IN2_V32          vec_t                   Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_neq_hi (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_neq_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP              uint8   1..8            Number of atomic operations
Operands      2    IN1_V32          vec_t                   Input vector operand
              3    IN2_V32          vec_t                   Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_neq_low (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_neq_uu
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

1    OOP              uint8   1..8            Number of atomic operations
Operands      2    IN1_V32          vec_t                   Input vector operand
              3    IN2_V32          vec_t                   Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_neq_uu (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_neq_uu_hi
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8    1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_neq_uu_hi (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_neq_uu_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8    1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_neq_uu_low (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_uu
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t
              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_uu (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_uu_hi
name

Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_uu_hi (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_v32_vpr_uu_low
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_v32_vpr_uu_low (8, vIn, vIn2);

Comments

Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_imm32_6_vpr
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1   OOP             uint8    1..8            Number of atomic operations
Operands      2   IN1_V32         vec_t                    Input vector operand
                                             31   31
              3   IN2_IMM32_6 int32        -2 ..2 -1       32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmp_v32_imm32_6_vpr (8, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_imm32_6_vpr_dup
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1   IN1_V32         vec_t                    Input vector operand
Operands                                     31   31
              2   IN2_IMM32_6 int32        -2 ..2 -1       32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmp_v32_imm32_6_vpr_dup (vIn, 2);

Comments

Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_imm32_6_vpr_dup_uu
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1   IN1_V32         vec_t                    Input vector operand
Operands                                     31   31
              2   IN2_IMM32_6 int32        -2 ..2 -1       32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmp_v32_imm32_6_vpr_dup_uu (vIn, 2);

Comments

Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_imm32_6_vpr_eq
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1   OOP             uint8    1..8            Number of atomic operations
Operands      2   IN1_V32         vec_t                    Input vector operand
                                             31   31
              3   IN2_IMM32_6 int32        -2 ..2 -1       32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmp_v32_imm32_6_vpr_eq (8, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_imm32_6_vpr_eq_dup
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1   IN1_V32         vec_t                    Input vector operand
Operands                                     31   31
              2   IN2_IMM32_6 int32        -2 ..2 -1       32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmp_v32_imm32_6_vpr_eq_dup (vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_imm32_6_vpr_eq_dup_uu
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1   IN1_V32         vec_t                    Input vector operand
Operands                                     31   31
              2   IN2_IMM32_6 int32        -2 ..2 -1       32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmp_v32_imm32_6_vpr_eq_dup_uu (vIn, 2);
Comments


Main table → Comparison And Predicates → Compare → Vector Compare

Intrinsic     vcmp_v32_imm32_6_vpr_eq_uu
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1   OOP             uint8    1..8            Number of atomic operations
Operands      2   IN1_V32         vec_t                    Input vector operand
                                             31   31
              3   IN2_IMM32_6 int32        -2 ..2 -1       32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmp_v32_imm32_6_vpr_eq_uu (8, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_imm32_6_vpr_ge
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1   OOP             uint8    1..8            Number of atomic operations
Operands      2   IN1_V32         vec_t                    Input vector operand
                                             31   31
              3   IN2_IMM32_6 int32        -2 ..2 -1       32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmp_v32_imm32_6_vpr_ge (8, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_imm32_6_vpr_ge_dup
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1   IN1_V32         vec_t                    Input vector operand
Operands                                     31   31
              2   IN2_IMM32_6 int32        -2 ..2 -1       32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmp_v32_imm32_6_vpr_ge_dup (vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_imm32_6_vpr_ge_dup_uu
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1   IN1_V32         vec_t                    Input vector operand
Operands                                     31   31
              2   IN2_IMM32_6 int32        -2 ..2 -1       32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmp_v32_imm32_6_vpr_ge_dup_uu (vIn, 2);

Comments

Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_imm32_6_vpr_ge_uu
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1   OOP             uint8    1..8            Number of atomic operations
Operands      2   IN1_V32         vec_t                    Input vector operand
                                             31   31
              3   IN2_IMM32_6 int32        -2 ..2 -1       32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmp_v32_imm32_6_vpr_ge_uu (8, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_imm32_6_vpr_gt
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

Operands      1   OOP             uint8    1..8            Number of atomic operations
              2   IN1_V32         vec_t                    Input vector operand
                                             31   31
              3   IN2_IMM32_6 int32        -2 ..2 -1       32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmp_v32_imm32_6_vpr_gt (8, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_imm32_6_vpr_gt_dup
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1   IN1_V32         vec_t                    Input vector operand
Operands                                     31   31
              2   IN2_IMM32_6 int32        -2 ..2 -1       32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmp_v32_imm32_6_vpr_gt_dup (vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_imm32_6_vpr_gt_dup_uu
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1   IN1_V32         vec_t                    Input vector operand
Operands                                     31   31
              2   IN2_IMM32_6 int32        -2 ..2 -1       32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmp_v32_imm32_6_vpr_gt_dup_uu (vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_imm32_6_vpr_gt_uu
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t
              1    OOP            uint8    1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
                                             31   31
              3    IN2_IMM32_6 int32       -2 ..2 -1        32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmp_v32_imm32_6_vpr_gt_uu (8, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_imm32_6_vpr_le
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1    OOP            uint8    1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
                                             31   31
              3    IN2_IMM32_6 int32       -2 ..2 -1        32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmp_v32_imm32_6_vpr_le (8, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_imm32_6_vpr_le_dup
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                     Input vector operand
Operands                                     31   31
              2    IN2_IMM32_6 int32       -2 ..2 -1        32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmp_v32_imm32_6_vpr_le_dup (vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_imm32_6_vpr_le_dup_uu
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                     Input vector operand
Operands                                      31   31
              2    IN2_IMM32_6 int32        -2 ..2 -1       32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...

vecPredRes = vcmp_v32_imm32_6_vpr_le_dup_uu (vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_imm32_6_vpr_le_uu
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
                                              31   31
              3    IN2_IMM32_6 int32        -2 ..2 -1       32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmp_v32_imm32_6_vpr_le_uu (8, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_imm32_6_vpr_lt
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
                                              31   31
              3    IN2_IMM32_6 int32        -2 ..2 -1       32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmp_v32_imm32_6_vpr_lt (8, vIn, 2);

Comments

Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_imm32_6_vpr_lt_dup
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1   IN1_V32         vec_t                    Input vector operand
Operands                                     31   31
              2   IN2_IMM32_6 int32        -2 ..2 -1       32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmp_v32_imm32_6_vpr_lt_dup (vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_imm32_6_vpr_lt_dup_uu
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1   IN1_V32         vec_t                    Input vector operand
Operands                                     31   31
              2   IN2_IMM32_6 int32        -2 ..2 -1       32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;

C example     ...
              vecPredRes = vcmp_v32_imm32_6_vpr_lt_dup_uu (vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_imm32_6_vpr_lt_uu
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1   OOP             uint8    1..8            Number of atomic operations
Operands      2   IN1_V32         vec_t                    Input vector operand
                                             31   31
              3   IN2_IMM32_6 int32        -2 ..2 -1       32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmp_v32_imm32_6_vpr_lt_uu (8, vIn, 2);
Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_imm32_6_vpr_neq
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1    OOP              uint8   1..8           Number of atomic operations
Operands      2    IN1_V32          vec_t                  Input vector operand
                                              31   31
              3    IN2_IMM32_6 int32        -2 ..2 -1      32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmp_v32_imm32_6_vpr_neq (8, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_imm32_6_vpr_neq_dup
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1    IN1_V32          vec_t                  Input vector operand
Operands                                      31   31
              2    IN2_IMM32_6 int32        -2 ..2 -1      32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmp_v32_imm32_6_vpr_neq_dup (vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_imm32_6_vpr_neq_dup_uu
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1    IN1_V32          vec_t                  Input vector operand
Operands                                      31   31
              2    IN2_IMM32_6 int32        -2 ..2 -1      32 bit immediate
              vec_t vIn;

C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp_v32_imm32_6_vpr_neq_dup_uu (vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_imm32_6_vpr_neq_uu
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1   OOP             uint8    1..8            Number of atomic operations
Operands      2   IN1_V32         vec_t                    Input vector operand
                                             31   31
              3   IN2_IMM32_6 int32        -2 ..2 -1       32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmp_v32_imm32_6_vpr_neq_uu (8, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
Intrinsic     vcmp_v32_imm32_6_vpr_uu
name
Spec syntax   vcmp {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1   OOP             uint8    1..8            Number of atomic operations
Operands      2   IN1_V32         vec_t                    Input vector operand
                                             31   31
              3   IN2_IMM32_6 int32        -2 ..2 -1       32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmp_v32_imm32_6_vpr_uu (8, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare
