# Comparison And Predicates → Compare → Vector Compare Complex

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Comparison And Predicates → Compare → Vector Compare Complex

Vector Compare Complex

Vector Compare Complex
Performs comparison between two complex number sources and set vector predicate bits
accordingly. The sources are 32-bit wide. The destination is 8-bit VPREX.
Available Switches
      Number of atomic operations. An atomic operation is defined by as a single comparison
Qop
      operation. 1op ≤ Qop ≤ 4op
hi    When used, 'hi' switch is indicating that the result is written to the high VPREX[15:8].
      When used, 'low' switch is indicating that the result is written to the low VPREX[7:0]
low
      (default).
      When used, the sources represented by the 32-bits of the vector part are treated as
uu
      unsigned values (by default they are treated as signed values).
Intrinsic Names
vcmpx_v32_v32_vpr
vcmpx_v32_v32_vpr_eq
vcmpx_v32_v32_vpr_eq_hi
vcmpx_v32_v32_vpr_eq_low
vcmpx_v32_v32_vpr_eq_uu
vcmpx_v32_v32_vpr_eq_uu_hi
vcmpx_v32_v32_vpr_eq_uu_low
vcmpx_v32_v32_vpr_ge
vcmpx_v32_v32_vpr_ge_hi
vcmpx_v32_v32_vpr_ge_low
vcmpx_v32_v32_vpr_ge_uu
vcmpx_v32_v32_vpr_ge_uu_hi
vcmpx_v32_v32_vpr_ge_uu_low
vcmpx_v32_v32_vpr_gt
vcmpx_v32_v32_vpr_gt_hi
vcmpx_v32_v32_vpr_gt_low
vcmpx_v32_v32_vpr_gt_uu
vcmpx_v32_v32_vpr_gt_uu_hi
vcmpx_v32_v32_vpr_gt_uu_low
vcmpx_v32_v32_vpr_hi
vcmpx_v32_v32_vpr_le
vcmpx_v32_v32_vpr_le_hi
vcmpx_v32_v32_vpr_le_low
vcmpx_v32_v32_vpr_le_uu
vcmpx_v32_v32_vpr_le_uu_hi
vcmpx_v32_v32_vpr_le_uu_low
vcmpx_v32_v32_vpr_low
vcmpx_v32_v32_vpr_lt
vcmpx_v32_v32_vpr_lt_hi
vcmpx_v32_v32_vpr_lt_low
vcmpx_v32_v32_vpr_lt_uu
vcmpx_v32_v32_vpr_lt_uu_hi
vcmpx_v32_v32_vpr_lt_uu_low
vcmpx_v32_v32_vpr_neq
vcmpx_v32_v32_vpr_neq_hi
vcmpx_v32_v32_vpr_neq_low
vcmpx_v32_v32_vpr_neq_uu
vcmpx_v32_v32_vpr_neq_uu_hi
vcmpx_v32_v32_vpr_neq_uu_low
vcmpx_v32_v32_vpr_uu
vcmpx_v32_v32_vpr_uu_hi
vcmpx_v32_v32_vpr_uu_low
vcmpx_v32_v32_vpr_nrng
vcmpx_v32_v32_vpr_nrng_uu
vcmpx_v32_v32_vpr_rng
vcmpx_v32_v32_vpr_rng_uu
vcmpx_v32_c32_vpr
vcmpx_v32_c32_vpr_eq
vcmpx_v32_c32_vpr_eq_hi
vcmpx_v32_c32_vpr_eq_low
vcmpx_v32_c32_vpr_eq_uu
vcmpx_v32_c32_vpr_eq_uu_hi
vcmpx_v32_c32_vpr_eq_uu_low

vcmpx_v32_c32_vpr_ge
vcmpx_v32_c32_vpr_ge_hi
vcmpx_v32_c32_vpr_ge_low
vcmpx_v32_c32_vpr_ge_uu
vcmpx_v32_c32_vpr_ge_uu_hi
vcmpx_v32_c32_vpr_ge_uu_low
vcmpx_v32_c32_vpr_gt
vcmpx_v32_c32_vpr_gt_hi
vcmpx_v32_c32_vpr_gt_low
vcmpx_v32_c32_vpr_gt_uu
vcmpx_v32_c32_vpr_gt_uu_hi
vcmpx_v32_c32_vpr_gt_uu_low
vcmpx_v32_c32_vpr_hi
vcmpx_v32_c32_vpr_le
vcmpx_v32_c32_vpr_le_hi
vcmpx_v32_c32_vpr_le_low
vcmpx_v32_c32_vpr_le_uu
vcmpx_v32_c32_vpr_le_uu_hi
vcmpx_v32_c32_vpr_le_uu_low
vcmpx_v32_c32_vpr_low
vcmpx_v32_c32_vpr_lt
vcmpx_v32_c32_vpr_lt_hi
vcmpx_v32_c32_vpr_lt_low
vcmpx_v32_c32_vpr_lt_uu
vcmpx_v32_c32_vpr_lt_uu_hi
vcmpx_v32_c32_vpr_lt_uu_low
vcmpx_v32_c32_vpr_neq
vcmpx_v32_c32_vpr_neq_hi
vcmpx_v32_c32_vpr_neq_low
vcmpx_v32_c32_vpr_neq_uu
vcmpx_v32_c32_vpr_neq_uu_hi
vcmpx_v32_c32_vpr_neq_uu_low
vcmpx_v32_c32_vpr_uu
vcmpx_v32_c32_vpr_uu_hi
vcmpx_v32_c32_vpr_uu_low
vcmpx_v32_imm32_6_vpr
vcmpx_v32_imm32_6_vpr_eq
vcmpx_v32_imm32_6_vpr_eq_uu
vcmpx_v32_imm32_6_vpr_ge
vcmpx_v32_imm32_6_vpr_ge_uu
vcmpx_v32_imm32_6_vpr_gt
vcmpx_v32_imm32_6_vpr_gt_uu
vcmpx_v32_imm32_6_vpr_le
vcmpx_v32_imm32_6_vpr_le_uu
vcmpx_v32_imm32_6_vpr_lt
vcmpx_v32_imm32_6_vpr_lt_uu
vcmpx_v32_imm32_6_vpr_neq
vcmpx_v32_imm32_6_vpr_neq_uu
vcmpx_v32_imm32_6_vpr_uu
Instruction details in the instruction set specification
Intrinsic     vcmpx_v32_v32_vpr
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4               Number of atomic operations
Operands      2    IN1_V32        vec_t                        Input vector operand
              3    IN2_V32        vec_t                        Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_v32_vpr (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_v32_vpr_eq
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4               Number of atomic operations
Operands      2    IN1_V32        vec_t                        Input vector operand
              3    IN2_V32        vec_t                        Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...

vecPredRes = vcmpx_v32_v32_vpr_eq (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_v32_vpr_eq_hi
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4               Number of atomic operations
Operands      2    IN1_V32        vec_t                        Input vector operand
              3    IN2_V32        vec_t                        Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_v32_vpr_eq_hi (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_v32_vpr_eq_low
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_v32_vpr_eq_low (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_v32_vpr_eq_uu
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_v32_vpr_eq_uu (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_v32_vpr_eq_uu_hi
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP              uint8   1..4            Number of atomic operations
Operands      2    IN1_V32          vec_t                   Input vector operand

3    IN2_V32          vec_t                   Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_v32_vpr_eq_uu_hi (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_v32_vpr_eq_uu_low
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP              uint8   1..4            Number of atomic operations
Operands      2    IN1_V32          vec_t                   Input vector operand
              3    IN2_V32          vec_t                   Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_v32_vpr_eq_uu_low (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_v32_vpr_ge
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP              uint8   1..4            Number of atomic operations
Operands      2    IN1_V32          vec_t                   Input vector operand
              3    IN2_V32          vec_t                   Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_v32_vpr_ge (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_v32_vpr_ge_hi
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_v32_vpr_ge_hi (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_v32_vpr_ge_low
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

1    QOP            uint8     1..4            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_v32_vpr_ge_low (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_v32_vpr_ge_uu
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t
              1    QOP            uint8    1..4             Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_v32_vpr_ge_uu (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_v32_vpr_ge_uu_hi
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8    1..4             Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_v32_vpr_ge_uu_hi (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_v32_vpr_ge_uu_low
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8    1..4             Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_v32_vpr_ge_uu_low (4, vIn, vIn2);

Comments

Main table → Comparison And Predicates → Compare → Vector Compare Complex

Intrinsic     vcmpx_v32_v32_vpr_gt
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_v32_vpr_gt (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_v32_vpr_gt_hi
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_v32_vpr_gt_hi (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_v32_vpr_gt_low
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4             Number of atomic operations
Operands
              2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_v32_vpr_gt_low (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_v32_vpr_gt_uu
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...

vecPredRes = vcmpx_v32_v32_vpr_gt_uu (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_v32_vpr_gt_uu_hi
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_v32_vpr_gt_uu_hi (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_v32_vpr_gt_uu_low
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_v32_vpr_gt_uu_low (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_v32_vpr_hi
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_v32_vpr_hi (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_v32_vpr_le
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand

3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
C example     vec_t vIn2;
              vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_v32_vpr_le (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_v32_vpr_le_hi
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_v32_vpr_le_hi (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_v32_vpr_le_low
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_v32_vpr_le_low (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_v32_vpr_le_uu
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vy[0], VPREX
Return type   vprex_t

              1    QOP            uint8     1..4            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_v32_vpr_le_uu (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_v32_vpr_le_uu_hi
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

1    QOP            uint8     1..4            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_v32_vpr_le_uu_hi (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_v32_vpr_le_uu_low
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_v32_vpr_le_uu_low (4, vIn, vIn2);
Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_v32_vpr_low
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_v32_vpr_low (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_v32_vpr_lt
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_v32_vpr_lt (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_v32_vpr_lt_hi

name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

Operands      1    QOP            uint8     1..4             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_v32_vpr_lt_hi (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_v32_vpr_lt_low
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_v32_vpr_lt_low (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_v32_vpr_lt_uu
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_v32_vpr_lt_uu (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_v32_vpr_lt_uu_hi
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...

vecPredRes = vcmpx_v32_v32_vpr_lt_uu_hi (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_v32_vpr_lt_uu_low
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_v32_vpr_lt_uu_low (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_v32_vpr_neq
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_v32_vpr_neq (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_v32_vpr_neq_hi
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_v32_vpr_neq_hi (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_v32_vpr_neq_low
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand

3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_v32_vpr_neq_low (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_v32_vpr_neq_uu
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP              uint8   1..4            Number of atomic operations
Operands      2    IN1_V32          vec_t                   Input vector operand
              3    IN2_V32          vec_t                   Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_v32_vpr_neq_uu (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_v32_vpr_neq_uu_hi
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP              uint8   1..4            Number of atomic operations
Operands      2    IN1_V32          vec_t                   Input vector operand
              3    IN2_V32          vec_t                   Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_v32_vpr_neq_uu_hi (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_v32_vpr_neq_uu_low
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP              uint8   1..4            Number of atomic operations
Operands      2    IN1_V32          vec_t                   Input vector operand
              3    IN2_V32          vec_t                   Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_v32_vpr_neq_uu_low (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_v32_vpr_uu
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

1    QOP            uint8     1..4            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_v32_vpr_uu (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_v32_vpr_uu_hi
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_v32_vpr_uu_hi (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_v32_vpr_uu_low
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vy[0], VPREX

Return type   vprex_t
            1    QOP            uint8    1..4             Number of atomic operations
Operands    2    IN1_V32        vec_t                     Input vector operand
            3    IN2_V32        vec_t                     Input vector operand
            vec_t vIn;
            vec_t vIn2;
C example   vprex_t vecPredRes;
            ...
            vecPredRes = vcmpx_v32_v32_vpr_uu_low (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_v32_vpr_nrng
name
Spec syntax   vcmpx {Qop, rng_nrng [,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_v32_vpr_nrng (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_v32_vpr_nrng_uu
name

Spec syntax   vcmpx {Qop, rng_nrng [,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_v32_vpr_nrng_uu (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_v32_vpr_rng
name
Spec syntax   vcmpx {Qop, rng_nrng [,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_v32_vpr_rng (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_v32_vpr_rng_uu
name
Spec syntax   vcmpx {Qop, rng_nrng [,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_v32_vpr_rng_uu (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_c32_vpr
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP            uint8     1..4             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_c32_vpr (4, vIn, vcoefIn);

Comments

Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_c32_vpr_eq
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP            uint8     1..4             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_c32_vpr_eq (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_c32_vpr_eq_hi
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP            uint8     1..4             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_c32_vpr_eq_hi (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_c32_vpr_eq_low
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP            uint8     1..4             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_c32_vpr_eq_low (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_c32_vpr_eq_uu
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP            uint8     1..4             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;

coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_c32_vpr_eq_uu (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_c32_vpr_eq_uu_hi
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP              uint8    1..4           Number of atomic operations
Operands      2    IN1_V32          vec_t                   Input vector operand
              3    IN2_C32          coef_t                  Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_c32_vpr_eq_uu_hi (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_c32_vpr_eq_uu_low
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP              uint8    1..4           Number of atomic operations
Operands      2    IN1_V32          vec_t                   Input vector operand
              3    IN2_C32          coef_t                  Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_c32_vpr_eq_uu_low (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_c32_vpr_ge
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP              uint8    1..4           Number of atomic operations
Operands      2    IN1_V32          vec_t                   Input vector operand
              3    IN2_C32          coef_t                  Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_c32_vpr_ge (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_c32_vpr_ge_hi
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP            uint8     1..4             Number of atomic operations

Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_c32_vpr_ge_hi (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_c32_vpr_ge_low
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP            uint8     1..4             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_c32_vpr_ge_low (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_c32_vpr_ge_uu
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t
              1    QOP            uint8     1..4            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_C32        coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_c32_vpr_ge_uu (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_c32_vpr_ge_uu_hi
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP            uint8     1..4            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_C32        coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_c32_vpr_ge_uu_hi (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_c32_vpr_ge_uu_low
name

Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP            uint8     1..4            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_C32        coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_c32_vpr_ge_uu_low (4, vIn, vcoefIn);

Comments

Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_c32_vpr_gt
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP            uint8     1..4             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_c32_vpr_gt (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_c32_vpr_gt_hi
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP            uint8     1..4             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_c32_vpr_gt_hi (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_c32_vpr_gt_low
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP            uint8     1..4             Number of atomic operations
Operands
              2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...

vecPredRes = vcmpx_v32_c32_vpr_gt_low (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_c32_vpr_gt_uu
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP            uint8     1..4             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_c32_vpr_gt_uu (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_c32_vpr_gt_uu_hi
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP            uint8     1..4             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_c32_vpr_gt_uu_hi (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_c32_vpr_gt_uu_low
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP            uint8     1..4             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_c32_vpr_gt_uu_low (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_c32_vpr_hi
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP            uint8     1..4             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand

3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_c32_vpr_hi (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_c32_vpr_le
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP            uint8     1..4             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
C example     coef_t vcoefIn;
              vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_c32_vpr_le (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_c32_vpr_le_hi
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP            uint8     1..4             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_c32_vpr_le_hi (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_c32_vpr_le_low
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP            uint8     1..4             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_c32_vpr_le_low (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_c32_vpr_le_uu
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vcY, VPREX
Return type   vprex_t

1    QOP            uint8     1..4             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_c32_vpr_le_uu (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_c32_vpr_le_uu_hi
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP            uint8     1..4             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_c32_vpr_le_uu_hi (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_c32_vpr_le_uu_low
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP            uint8     1..4             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_c32_vpr_le_uu_low (4, vIn, vcoefIn);
Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_c32_vpr_low
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP             uint8     1..4            Number of atomic operations
Operands      2    IN1_V32         vec_t                     Input vector operand
              3    IN2_C32         coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_c32_vpr_low (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex

Intrinsic     vcmpx_v32_c32_vpr_lt
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP             uint8     1..4            Number of atomic operations
Operands      2    IN1_V32         vec_t                     Input vector operand
              3    IN2_C32         coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_c32_vpr_lt (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_c32_vpr_lt_hi
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

Operands      1    QOP             uint8     1..4            Number of atomic operations
              2    IN1_V32         vec_t                     Input vector operand
              3    IN2_C32         coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_c32_vpr_lt_hi (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_c32_vpr_lt_low
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP             uint8    1..4             Number of atomic operations
Operands      2    IN1_V32         vec_t                     Input vector operand
              3    IN2_C32         coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_c32_vpr_lt_low (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_c32_vpr_lt_uu
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP             uint8    1..4             Number of atomic operations
Operands      2    IN1_V32         vec_t                     Input vector operand
              3    IN2_C32         coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...

vecPredRes = vcmpx_v32_c32_vpr_lt_uu (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_c32_vpr_lt_uu_hi
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP            uint8     1..4             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_c32_vpr_lt_uu_hi (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_c32_vpr_lt_uu_low
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP            uint8     1..4             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_c32_vpr_lt_uu_low (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_c32_vpr_neq
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP            uint8     1..4             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_c32_vpr_neq (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_c32_vpr_neq_hi
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP            uint8     1..4            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand

3    IN2_C32        coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_c32_vpr_neq_hi (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_c32_vpr_neq_low
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP            uint8     1..4            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_C32        coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_c32_vpr_neq_low (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_c32_vpr_neq_uu
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP              uint8    1..4           Number of atomic operations
Operands      2    IN1_V32          vec_t                   Input vector operand
              3    IN2_C32          coef_t                  Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_c32_vpr_neq_uu (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_c32_vpr_neq_uu_hi
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP              uint8    1..4           Number of atomic operations
Operands      2    IN1_V32          vec_t                   Input vector operand
              3    IN2_C32          coef_t                  Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_c32_vpr_neq_uu_hi (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_c32_vpr_neq_uu_low
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

1    QOP              uint8    1..4           Number of atomic operations
Operands      2    IN1_V32          vec_t                   Input vector operand
              3    IN2_C32          coef_t                  Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_c32_vpr_neq_uu_low (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_c32_vpr_uu
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP            uint8     1..4            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_C32        coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_c32_vpr_uu (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_c32_vpr_uu_hi
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP            uint8     1..4            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_C32        coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_c32_vpr_uu_hi (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_c32_vpr_uu_low
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu][,low_hi]} vx[0], vcY, VPREX

Return type   vprex_t
            1    QOP            uint8     1..4            Number of atomic operations
Operands    2    IN1_V32        vec_t                     Input vector operand
            3    IN2_C32        coef_t                    Coefficient operand
            vec_t vIn;
            coef_t vcoefIn;
C example   vprex_t vecPredRes;
            ...
            vecPredRes = vcmpx_v32_c32_vpr_uu_low (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_imm32_6_vpr
name

Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1    QOP              uint8   1..4           Number of atomic operations
Operands      2    IN1_V32          vec_t                  Input vector operand
                                              31   31
              3    IN2_IMM32_6 int32        -2 ..2 -1      32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpx_v32_imm32_6_vpr (4, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_imm32_6_vpr_eq
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1    QOP              uint8   1..4           Number of atomic operations
Operands      2    IN1_V32          vec_t                  Input vector operand
                                              31   31
              3    IN2_IMM32_6 int32        -2 ..2 -1      32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpx_v32_imm32_6_vpr_eq (4, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_imm32_6_vpr_eq_uu
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1    QOP              uint8   1..4           Number of atomic operations
Operands      2    IN1_V32          vec_t                  Input vector operand
                                              31   31
              3    IN2_IMM32_6 int32        -2 ..2 -1      32 bit immediate
              vec_t vIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpx_v32_imm32_6_vpr_eq_uu (4, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_imm32_6_vpr_ge
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1   QOP             uint8    1..4            Number of atomic operations
Operands      2   IN1_V32         vec_t                    Input vector operand
                                             31   31
              3   IN2_IMM32_6 int32        -2 ..2 -1       32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...

vecPredRes = vcmpx_v32_imm32_6_vpr_ge (4, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_imm32_6_vpr_ge_uu
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1   QOP             uint8    1..4            Number of atomic operations
Operands      2   IN1_V32         vec_t                    Input vector operand
                                             31   31
              3   IN2_IMM32_6 int32        -2 ..2 -1       32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpx_v32_imm32_6_vpr_ge_uu (4, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_imm32_6_vpr_gt
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

Operands      1   QOP             uint8    1..4            Number of atomic operations
              2   IN1_V32         vec_t                     Input vector operand
                                             31   31
              3   IN2_IMM32_6 int32        -2 ..2 -1        32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpx_v32_imm32_6_vpr_gt (4, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_imm32_6_vpr_gt_uu
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1   QOP             uint8    1..4             Number of atomic operations
Operands      2   IN1_V32         vec_t                     Input vector operand
                                             31   31
              3   IN2_IMM32_6 int32        -2 ..2 -1        32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpx_v32_imm32_6_vpr_gt_uu (4, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_imm32_6_vpr_le
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1   QOP             uint8    1..4             Number of atomic operations
Operands      2   IN1_V32         vec_t                     Input vector operand

31   31
              3   IN2_IMM32_6 int32        -2 ..2 -1        32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpx_v32_imm32_6_vpr_le (4, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_imm32_6_vpr_le_uu
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1    QOP            uint8     1..4            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
                                              31   31
              3    IN2_IMM32_6 int32        -2 ..2 -1       32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpx_v32_imm32_6_vpr_le_uu (4, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_imm32_6_vpr_lt
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1    QOP            uint8     1..4            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
                                              31   31
              3    IN2_IMM32_6 int32        -2 ..2 -1       32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpx_v32_imm32_6_vpr_lt (4, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_imm32_6_vpr_lt_uu
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1    QOP            uint8     1..4            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
                                              31   31
              3    IN2_IMM32_6 int32        -2 ..2 -1       32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpx_v32_imm32_6_vpr_lt_uu (4, vIn, 2);

Comments

Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_imm32_6_vpr_neq
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

1   QOP             uint8    1..4            Number of atomic operations
Operands      2   IN1_V32         vec_t                    Input vector operand
                                             31   31
              3   IN2_IMM32_6 int32        -2 ..2 -1       32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpx_v32_imm32_6_vpr_neq (4, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_imm32_6_vpr_neq_uu
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1   QOP             uint8    1..4            Number of atomic operations
Operands      2   IN1_V32         vec_t                    Input vector operand
                                             31   31
              3   IN2_IMM32_6 int32        -2 ..2 -1       32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpx_v32_imm32_6_vpr_neq_uu (4, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Intrinsic     vcmpx_v32_imm32_6_vpr_uu
name
Spec syntax   vcmpx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1   QOP             uint8    1..4            Number of atomic operations
Operands      2   IN1_V32         vec_t                    Input vector operand
                                             31   31
              3   IN2_IMM32_6 int32        -2 ..2 -1       32 bit immediate
            vec_t vIn;
            vprex_t vecPredRes;
C example   ...
            vecPredRes = vcmpx_v32_imm32_6_vpr_uu (4, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex

Main table → Comparison And Predicates → Compare → Vector Compare Complex
Word Parts

Vector Compare Complex Word Parts

Vector Compare Complex Word Parts
Performs comparison between two sources and sets vector predicate registers accordingly. The
sources are 16-bit wide. The destination is 16-bit VPREX.
Available Switches
      Number of atomic operations. An atomic operation is defined by as a single 2-word
Qop
      comparison operation. 1op ≤ Qop ≤ 4op
      When used, each source which is represented by the 16-bits of the vector parts is treated as
uu

an unsigned value (by default they are treated as signed values).
Intrinsic Names
vcmpwx_v32_v32_vpr
vcmpwx_v32_v32_vpr_eq
vcmpwx_v32_v32_vpr_eq_uu
vcmpwx_v32_v32_vpr_ge
vcmpwx_v32_v32_vpr_ge_uu
vcmpwx_v32_v32_vpr_gt
vcmpwx_v32_v32_vpr_gt_uu
vcmpwx_v32_v32_vpr_le
vcmpwx_v32_v32_vpr_le_uu
vcmpwx_v32_v32_vpr_lt
vcmpwx_v32_v32_vpr_lt_uu
vcmpwx_v32_v32_vpr_neq
vcmpwx_v32_v32_vpr_neq_uu
vcmpwx_v32_v32_vpr_uu
vcmpwx_v32_imm16_6_vpr
vcmpwx_v32_imm16_6_vpr_eq
vcmpwx_v32_imm16_6_vpr_eq_uu
vcmpwx_v32_imm16_6_vpr_ge
vcmpwx_v32_imm16_6_vpr_ge_uu
vcmpwx_v32_imm16_6_vpr_gt
vcmpwx_v32_imm16_6_vpr_gt_uu
vcmpwx_v32_imm16_6_vpr_le
vcmpwx_v32_imm16_6_vpr_le_uu
vcmpwx_v32_imm16_6_vpr_lt
vcmpwx_v32_imm16_6_vpr_lt_uu
vcmpwx_v32_imm16_6_vpr_neq
vcmpwx_v32_imm16_6_vpr_neq_uu
vcmpwx_v32_imm16_6_vpr_uu
vcmpwx_v32_c32_vpr
vcmpwx_v32_c32_vpr_eq
vcmpwx_v32_c32_vpr_eq_uu
vcmpwx_v32_c32_vpr_ge
vcmpwx_v32_c32_vpr_ge_uu
vcmpwx_v32_c32_vpr_gt
vcmpwx_v32_c32_vpr_gt_uu
vcmpwx_v32_c32_vpr_le
vcmpwx_v32_c32_vpr_le_uu
vcmpwx_v32_c32_vpr_lt
vcmpwx_v32_c32_vpr_lt_uu
vcmpwx_v32_c32_vpr_neq
vcmpwx_v32_c32_vpr_neq_uu
vcmpwx_v32_c32_vpr_uu
Instruction details in the instruction set specification
Intrinsic     vcmpwx_v32_v32_vpr
name
Spec syntax   vcmpwx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpwx_v32_v32_vpr (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Word Parts
Intrinsic     vcmpwx_v32_v32_vpr_eq
name
Spec syntax   vcmpwx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpwx_v32_v32_vpr_eq (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Word Parts

Intrinsic     vcmpwx_v32_v32_vpr_eq_uu
name
Spec syntax   vcmpwx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4            Number of atomic operations
Operands
              2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpwx_v32_v32_vpr_eq_uu (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Word Parts
Intrinsic     vcmpwx_v32_v32_vpr_ge
name
Spec syntax   vcmpwx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8    1..4             Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpwx_v32_v32_vpr_ge (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Word Parts
Intrinsic     vcmpwx_v32_v32_vpr_ge_uu
name
Spec syntax   vcmpwx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8    1..4             Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpwx_v32_v32_vpr_ge_uu (4, vIn, vIn2);

Comments

Main table → Comparison And Predicates → Compare → Vector Compare Complex
Word Parts
Intrinsic     vcmpwx_v32_v32_vpr_gt
name
Spec syntax   vcmpwx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...

vecPredRes = vcmpwx_v32_v32_vpr_gt (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Word Parts
Intrinsic     vcmpwx_v32_v32_vpr_gt_uu
name
Spec syntax   vcmpwx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpwx_v32_v32_vpr_gt_uu (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Word Parts
Intrinsic     vcmpwx_v32_v32_vpr_le
name
Spec syntax   vcmpwx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t
              1    QOP            uint8     1..4            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpwx_v32_v32_vpr_le (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Word Parts
Intrinsic     vcmpwx_v32_v32_vpr_le_uu
name
Spec syntax   vcmpwx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpwx_v32_v32_vpr_le_uu (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Word Parts
Intrinsic     vcmpwx_v32_v32_vpr_lt
name
Spec syntax   vcmpwx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand

3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpwx_v32_v32_vpr_lt (4, vIn, vIn2);
Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Word Parts
Intrinsic     vcmpwx_v32_v32_vpr_lt_uu
name
Spec syntax   vcmpwx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpwx_v32_v32_vpr_lt_uu (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Word Parts
Intrinsic     vcmpwx_v32_v32_vpr_neq
name
Spec syntax   vcmpwx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpwx_v32_v32_vpr_neq (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Word Parts
Intrinsic     vcmpwx_v32_v32_vpr_neq_uu
name
Spec syntax   vcmpwx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vy[0], VPREX
Return type   vprex_t

              1    QOP            uint8    1..4            Number of atomic operations
Operands      2    IN1_V32        vec_t                    Input vector operand
              3    IN2_V32        vec_t                    Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpwx_v32_v32_vpr_neq_uu (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Word Parts
Intrinsic     vcmpwx_v32_v32_vpr_uu
name
Spec syntax   vcmpwx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

1    QOP            uint8    1..4            Number of atomic operations
Operands      2    IN1_V32        vec_t                    Input vector operand
              3    IN2_V32        vec_t                    Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpwx_v32_v32_vpr_uu (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Word Parts
Intrinsic     vcmpwx_v32_imm16_6_vpr
name
Spec syntax   vcmpwx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], #imm16_6, VPREX

Return type   vprex_t

              1   QOP             uint8    1..4            Number of atomic operations
Operands      2   IN1_V32         vec_t                    Input vector operand
              3   IN2_IMM16_6 int16        -32768..32767   16 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpwx_v32_imm16_6_vpr (4, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Word Parts
Intrinsic     vcmpwx_v32_imm16_6_vpr_eq
name
Spec syntax   vcmpwx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], #imm16_6, VPREX

Return type   vprex_t

              1   QOP             uint8    1..4            Number of atomic operations
Operands      2   IN1_V32         vec_t                    Input vector operand
              3   IN2_IMM16_6 int16        -32768..32767   16 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpwx_v32_imm16_6_vpr_eq (4, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Word Parts
Intrinsic     vcmpwx_v32_imm16_6_vpr_eq_uu
name
Spec syntax   vcmpwx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], #imm16_6, VPREX

Return type   vprex_t

              1   QOP             uint8    1..4            Number of atomic operations
Operands      2   IN1_V32         vec_t                    Input vector operand
              3   IN2_IMM16_6 int16        -32768..32767   16 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpwx_v32_imm16_6_vpr_eq_uu (4, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Word Parts
Intrinsic     vcmpwx_v32_imm16_6_vpr_ge
name

Spec syntax   vcmpwx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], #imm16_6, VPREX

Return type   vprex_t

              1   QOP            uint8     1..4            Number of atomic operations
Operands      2   IN1_V32        vec_t                     Input vector operand
              3   IN2_IMM16_6 int16        -32768..32767   16 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpwx_v32_imm16_6_vpr_ge (4, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Word Parts
Intrinsic     vcmpwx_v32_imm16_6_vpr_ge_uu
name
Spec syntax   vcmpwx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], #imm16_6, VPREX

Return type   vprex_t

              1   QOP            uint8     1..4            Number of atomic operations
Operands      2   IN1_V32        vec_t                     Input vector operand
              3   IN2_IMM16_6 int16        -32768..32767   16 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpwx_v32_imm16_6_vpr_ge_uu (4, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Word Parts
Intrinsic     vcmpwx_v32_imm16_6_vpr_gt
name
Spec syntax   vcmpwx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], #imm16_6, VPREX

Return type   vprex_t

              1    QOP              uint8   1..4            Number of atomic operations
Operands      2    IN1_V32          vec_t                   Input vector operand
              3    IN2_IMM16_6 int16        -32768..32767   16 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpwx_v32_imm16_6_vpr_gt (4, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Word Parts
Intrinsic     vcmpwx_v32_imm16_6_vpr_gt_uu
name
Spec syntax   vcmpwx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], #imm16_6, VPREX

Return type   vprex_t

              1    QOP              uint8   1..4            Number of atomic operations
Operands      2    IN1_V32          vec_t                   Input vector operand
              3    IN2_IMM16_6 int16        -32768..32767   16 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpwx_v32_imm16_6_vpr_gt_uu (4, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Word Parts

Intrinsic     vcmpwx_v32_imm16_6_vpr_le
name
Spec syntax   vcmpwx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], #imm16_6, VPREX

Return type   vprex_t

              1    QOP              uint8   1..4            Number of atomic operations
Operands      2    IN1_V32          vec_t                   Input vector operand
              3    IN2_IMM16_6 int16        -32768..32767   16 bit immediate
              vec_t vIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpwx_v32_imm16_6_vpr_le (4, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Word Parts
Intrinsic     vcmpwx_v32_imm16_6_vpr_le_uu
name
Spec syntax   vcmpwx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], #imm16_6, VPREX

Return type   vprex_t

              1   QOP             uint8    1..4            Number of atomic operations
Operands      2   IN1_V32         vec_t                    Input vector operand
              3   IN2_IMM16_6 int16        -32768..32767   16 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpwx_v32_imm16_6_vpr_le_uu (4, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Word Parts
Intrinsic     vcmpwx_v32_imm16_6_vpr_lt
name
Spec syntax   vcmpwx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], #imm16_6, VPREX

Return type   vprex_t

              1   QOP             uint8    1..4            Number of atomic operations
Operands      2   IN1_V32         vec_t                    Input vector operand
              3   IN2_IMM16_6 int16        -32768..32767   16 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpwx_v32_imm16_6_vpr_lt (4, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Word Parts
Intrinsic     vcmpwx_v32_imm16_6_vpr_lt_uu
name
Spec syntax   vcmpwx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], #imm16_6, VPREX
Return type   vprex_t

              1   QOP             uint8    1..4            Number of atomic operations
Operands      2   IN1_V32         vec_t                    Input vector operand
              3   IN2_IMM16_6 int16        -32768..32767   16 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpwx_v32_imm16_6_vpr_lt_uu (4, vIn, 2);

Comments

Main table → Comparison And Predicates → Compare → Vector Compare Complex
Word Parts
Intrinsic     vcmpwx_v32_imm16_6_vpr_neq
name
Spec syntax   vcmpwx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], #imm16_6, VPREX

Return type   vprex_t

              1   QOP             uint8    1..4            Number of atomic operations
Operands      2   IN1_V32         vec_t                    Input vector operand
              3   IN2_IMM16_6 int16        -32768..32767   16 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpwx_v32_imm16_6_vpr_neq (4, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Word Parts
Intrinsic     vcmpwx_v32_imm16_6_vpr_neq_uu
name
Spec syntax   vcmpwx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], #imm16_6, VPREX

Return type   vprex_t

              1   QOP             uint8    1..4            Number of atomic operations
Operands      2   IN1_V32         vec_t                    Input vector operand
              3   IN2_IMM16_6 int16        -32768..32767   16 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpwx_v32_imm16_6_vpr_neq_uu (4, vIn, 2);
Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Word Parts
Intrinsic     vcmpwx_v32_imm16_6_vpr_uu
name
Spec syntax   vcmpwx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], #imm16_6, VPREX

Return type   vprex_t

              1   QOP            uint8     1..4            Number of atomic operations
Operands      2   IN1_V32        vec_t                     Input vector operand
              3   IN2_IMM16_6 int16        -32768..32767   16 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpwx_v32_imm16_6_vpr_uu (4, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Word Parts
Intrinsic     vcmpwx_v32_c32_vpr
name
Spec syntax   vcmpwx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vcYp, VPREX

Return type   vprex_t

              1    QOP            uint8    1..4            Number of atomic operations
              2    IN1_V32        vec_t                    Input vector operand
Operands
              3    IN2_C32        coef_t                   Coefficient operand
              4    IN2_PART       uint8    LOW,HIGH        Word part which is used for operand 3
              vec_t vIn;

coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpwx_v32_c32_vpr (4, vIn, vcoefIn, LOW);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Word Parts
Intrinsic     vcmpwx_v32_c32_vpr_eq
name
Spec syntax   vcmpwx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vcYp, VPREX

Return type   vprex_t

              1    QOP            uint8    1..4            Number of atomic operations
              2    IN1_V32        vec_t                    Input vector operand
Operands
              3    IN2_C32        coef_t                   Coefficient operand
              4    IN2_PART       uint8    LOW,HIGH        Word part which is used for operand 3
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpwx_v32_c32_vpr_eq (4, vIn, vcoefIn, LOW);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Word Parts
Intrinsic     vcmpwx_v32_c32_vpr_eq_uu
name
Spec syntax   vcmpwx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vcYp, VPREX

Return type   vprex_t
              1    QOP            uint8    1..4            Number of atomic operations
              2    IN1_V32        vec_t                    Input vector operand
Operands
              3    IN2_C32        coef_t                   Coefficient operand
              4    IN2_PART       uint8    LOW,HIGH        Word part which is used for operand 3
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpwx_v32_c32_vpr_eq_uu (4, vIn, vcoefIn, LOW);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Word Parts
Intrinsic     vcmpwx_v32_c32_vpr_ge
name
Spec syntax   vcmpwx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vcYp, VPREX

Return type   vprex_t

              1    QOP            uint8    1..4            Number of atomic operations
              2    IN1_V32        vec_t                    Input vector operand
Operands
              3    IN2_C32        coef_t                   Coefficient operand
              4    IN2_PART       uint8    LOW,HIGH        Word part which is used for operand 3
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpwx_v32_c32_vpr_ge (4, vIn, vcoefIn, LOW);

Comments

Main table → Comparison And Predicates → Compare → Vector Compare Complex
Word Parts
Intrinsic     vcmpwx_v32_c32_vpr_ge_uu
name
Spec syntax   vcmpwx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vcYp, VPREX

Return type   vprex_t

              1    QOP            uint8    1..4            Number of atomic operations
              2    IN1_V32        vec_t                    Input vector operand
Operands
              3    IN2_C32        coef_t                   Coefficient operand
              4    IN2_PART       uint8    LOW,HIGH        Word part which is used for operand 3
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpwx_v32_c32_vpr_ge_uu (4, vIn, vcoefIn, LOW);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Word Parts
Intrinsic     vcmpwx_v32_c32_vpr_gt
name
Spec syntax   vcmpwx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vcYp, VPREX

Return type   vprex_t

              1    QOP            uint8    1..4            Number of atomic operations
              2    IN1_V32        vec_t                    Input vector operand
Operands
              3    IN2_C32        coef_t                   Coefficient operand
              4    IN2_PART       uint8    LOW,HIGH        Word part which is used for operand 3
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpwx_v32_c32_vpr_gt (4, vIn, vcoefIn, LOW);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Word Parts
Intrinsic     vcmpwx_v32_c32_vpr_gt_uu
name
Spec syntax   vcmpwx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vcYp, VPREX

Return type   vprex_t

              1    QOP            uint8    1..4            Number of atomic operations
              2    IN1_V32        vec_t                    Input vector operand
Operands
              3    IN2_C32        coef_t                   Coefficient operand
              4    IN2_PART       uint8    LOW,HIGH        Word part which is used for operand 3
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpwx_v32_c32_vpr_gt_uu (4, vIn, vcoefIn, LOW);

Comments

Main table → Comparison And Predicates → Compare → Vector Compare Complex
Word Parts
Intrinsic     vcmpwx_v32_c32_vpr_le
name

Spec syntax   vcmpwx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vcYp, VPREX

Return type   vprex_t

              1    QOP            uint8    1..4             Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand
Operands
              3    IN2_C32        coef_t                    Coefficient operand
              4    IN2_PART       uint8    LOW,HIGH         Word part which is used for operand 3
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpwx_v32_c32_vpr_le (4, vIn, vcoefIn, LOW);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Word Parts
Intrinsic     vcmpwx_v32_c32_vpr_le_uu
name
Spec syntax   vcmpwx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vcYp, VPREX

Return type   vprex_t

              1    QOP            uint8    1..4             Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand
Operands
              3    IN2_C32        coef_t                    Coefficient operand
              4    IN2_PART       uint8    LOW,HIGH         Word part which is used for operand 3
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpwx_v32_c32_vpr_le_uu (4, vIn, vcoefIn, LOW);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Word Parts
Intrinsic     vcmpwx_v32_c32_vpr_lt
name
Spec syntax   vcmpwx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vcYp, VPREX

Return type   vprex_t

              1    QOP            uint8    1..4             Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand
Operands
              3    IN2_C32        coef_t                    Coefficient operand
              4    IN2_PART       uint8    LOW,HIGH         Word part which is used for operand 3
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpwx_v32_c32_vpr_lt (4, vIn, vcoefIn, LOW);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Word Parts
Intrinsic     vcmpwx_v32_c32_vpr_lt_uu
name
Spec syntax   vcmpwx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vcYp, VPREX

Return type   vprex_t

1    QOP            uint8    1..4             Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand
Operands
              3    IN2_C32        coef_t                    Coefficient operand
              4    IN2_PART       uint8    LOW,HIGH         Word part which is used for operand 3
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpwx_v32_c32_vpr_lt_uu (4, vIn, vcoefIn, LOW);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Word Parts
Intrinsic     vcmpwx_v32_c32_vpr_neq
name
Spec syntax   vcmpwx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vcYp, VPREX

Return type   vprex_t

              1    QOP            uint8    1..4             Number of atomic operations
Operands
              2    IN1_V32        vec_t                     Input vector operand
              3    IN2_C32          coef_t                 Coefficient operand
              4    IN2_PART         uint8    LOW,HIGH      Word part which is used for operand 3
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpwx_v32_c32_vpr_neq (4, vIn, vcoefIn, LOW);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Word Parts
Intrinsic     vcmpwx_v32_c32_vpr_neq_uu
name
Spec syntax   vcmpwx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vcYp, VPREX

Return type   vprex_t

              1    QOP              uint8    1..4          Number of atomic operations
              2    IN1_V32          vec_t                  Input vector operand
Operands
              3    IN2_C32          coef_t                 Coefficient operand
              4    IN2_PART         uint8    LOW,HIGH      Word part which is used for operand 3
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpwx_v32_c32_vpr_neq_uu (4, vIn, vcoefIn, LOW);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Word Parts
Intrinsic     vcmpwx_v32_c32_vpr_uu
name
Spec syntax   vcmpwx {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vcYp, VPREX

Return type   vprex_t

              1    QOP              uint8    1..4          Number of atomic operations
              2    IN1_V32          vec_t                  Input vector operand
Operands

3    IN2_C32          coef_t                 Coefficient operand
              4    IN2_PART         uint8    LOW,HIGH      Word part which is used for operand 3
              vec_t vIn;
C example     coef_t vcoefIn;
              vprex_t vecPredRes;
           ...
           vecPredRes = vcmpwx_v32_c32_vpr_uu (4, vIn, vcoefIn, LOW);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Complex
Word Parts
