# Comparison And Predicates → Compare → Vector Compare Long

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Comparison And Predicates → Compare → Vector Compare Long

Vector Compare Long

Vector Compare Long
Performs comparison between two long number sources and set vector predicate bits
accordingly. The sources are 64-bit wide. The destination is 4-bit VPREX.
Available Switches
      Number of atomic operations. An atomic operation is defined by a single comparison
Qop
      operation. 1op ≤ Qop ≤ 4op
      When used, the sources represented by the 64-bits of the vector part are treated as
uu
      unsigned values (by default they are treated as signed values).
Intrinsic Names
vcmpl_v32_v32_vpr_nrng
vcmpl_v32_v32_vpr_nrng_uu
vcmpl_v32_v32_vpr_rng
vcmpl_v32_v32_vpr_rng_uu
vcmpl_v32_v32_vpr
vcmpl_v32_v32_vpr_eq
vcmpl_v32_v32_vpr_eq_uu
vcmpl_v32_v32_vpr_ge
vcmpl_v32_v32_vpr_ge_uu
vcmpl_v32_v32_vpr_gt
vcmpl_v32_v32_vpr_gt_uu
vcmpl_v32_v32_vpr_le
vcmpl_v32_v32_vpr_le_uu
vcmpl_v32_v32_vpr_lt
vcmpl_v32_v32_vpr_lt_uu
vcmpl_v32_v32_vpr_neq
vcmpl_v32_v32_vpr_neq_uu
vcmpl_v32_v32_vpr_uu
vcmpl_v32_c32_vpr
vcmpl_v32_c32_vpr_eq
vcmpl_v32_c32_vpr_eq_uu
vcmpl_v32_c32_vpr_ge
vcmpl_v32_c32_vpr_ge_uu
vcmpl_v32_c32_vpr_gt
vcmpl_v32_c32_vpr_gt_uu
vcmpl_v32_c32_vpr_le
vcmpl_v32_c32_vpr_le_uu
vcmpl_v32_c32_vpr_lt
vcmpl_v32_c32_vpr_lt_uu
vcmpl_v32_c32_vpr_neq
vcmpl_v32_c32_vpr_neq_uu
vcmpl_v32_c32_vpr_uu
vcmpl_v32_imm32_6_vpr
vcmpl_v32_imm32_6_vpr_eq
vcmpl_v32_imm32_6_vpr_eq_uu
vcmpl_v32_imm32_6_vpr_ge
vcmpl_v32_imm32_6_vpr_ge_uu
vcmpl_v32_imm32_6_vpr_gt
vcmpl_v32_imm32_6_vpr_gt_uu
vcmpl_v32_imm32_6_vpr_le
vcmpl_v32_imm32_6_vpr_le_uu
vcmpl_v32_imm32_6_vpr_lt
vcmpl_v32_imm32_6_vpr_lt_uu
vcmpl_v32_imm32_6_vpr_neq
vcmpl_v32_imm32_6_vpr_neq_uu
vcmpl_v32_imm32_6_vpr_uu
Instruction details in the instruction set specification
Intrinsic     vcmpl_v32_v32_vpr_nrng
name
Spec syntax   vcmpl {Qop, rng_nrng [,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand

3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpl_v32_v32_vpr_nrng (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Long
Intrinsic     vcmpl_v32_v32_vpr_nrng_uu
name
Spec syntax   vcmpl {Qop, rng_nrng [,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpl_v32_v32_vpr_nrng_uu (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Long
Intrinsic     vcmpl_v32_v32_vpr_rng
name
Spec syntax   vcmpl {Qop, rng_nrng [,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpl_v32_v32_vpr_rng (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Long
Intrinsic     vcmpl_v32_v32_vpr_rng_uu
name
Spec syntax   vcmpl {Qop, rng_nrng [,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpl_v32_v32_vpr_rng_uu (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Long
Intrinsic     vcmpl_v32_v32_vpr
name
Spec syntax   vcmpl {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4               Number of atomic operations

Operands      2    IN1_V32        vec_t                        Input vector operand
              3    IN2_V32        vec_t                        Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpl_v32_v32_vpr (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Long
Intrinsic     vcmpl_v32_v32_vpr_eq
name
Spec syntax   vcmpl {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4               Number of atomic operations
Operands      2    IN1_V32        vec_t                        Input vector operand
              3    IN2_V32        vec_t                        Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpl_v32_v32_vpr_eq (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Long
Intrinsic     vcmpl_v32_v32_vpr_eq_uu
name
Spec syntax   vcmpl {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4               Number of atomic operations
Operands      2    IN1_V32        vec_t                        Input vector operand
              3    IN2_V32        vec_t                        Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpl_v32_v32_vpr_eq_uu (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Long
Intrinsic     vcmpl_v32_v32_vpr_ge
name
Spec syntax   vcmpl {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpl_v32_v32_vpr_ge (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Long
Intrinsic     vcmpl_v32_v32_vpr_ge_uu
name
Spec syntax   vcmpl {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

1    QOP            uint8     1..4             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpl_v32_v32_vpr_ge_uu (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Long
Intrinsic     vcmpl_v32_v32_vpr_gt
name
Spec syntax   vcmpl {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP              uint8   1..4             Number of atomic operations
Operands      2    IN1_V32          vec_t                    Input vector operand
              3    IN2_V32          vec_t                    Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpl_v32_v32_vpr_gt (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Long
Intrinsic     vcmpl_v32_v32_vpr_gt_uu
name
Spec syntax   vcmpl {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP              uint8   1..4             Number of atomic operations
Operands      2    IN1_V32          vec_t                    Input vector operand
              3    IN2_V32          vec_t                    Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpl_v32_v32_vpr_gt_uu (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Long
Intrinsic     vcmpl_v32_v32_vpr_le
name
Spec syntax   vcmpl {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP              uint8   1..4             Number of atomic operations
Operands      2    IN1_V32          vec_t                    Input vector operand
              3    IN2_V32          vec_t                    Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpl_v32_v32_vpr_le (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Long
Intrinsic     vcmpl_v32_v32_vpr_le_uu
name

Spec syntax   vcmpl {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP             uint8     1..4             Number of atomic operations
Operands      2    IN1_V32         vec_t                      Input vector operand
              3    IN2_V32         vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpl_v32_v32_vpr_le_uu (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Long
Intrinsic     vcmpl_v32_v32_vpr_lt
name
Spec syntax   vcmpl {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP             uint8     1..4             Number of atomic operations
Operands      2    IN1_V32         vec_t                      Input vector operand
              3    IN2_V32         vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpl_v32_v32_vpr_lt (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Long
Intrinsic     vcmpl_v32_v32_vpr_lt_uu
name
Spec syntax   vcmpl {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t
              1    QOP            uint8     1..4             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpl_v32_v32_vpr_lt_uu (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Long
Intrinsic     vcmpl_v32_v32_vpr_neq
name
Spec syntax   vcmpl {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpl_v32_v32_vpr_neq (4, vIn, vIn2);

Comments

Main table → Comparison And Predicates → Compare → Vector Compare Long
Intrinsic     vcmpl_v32_v32_vpr_neq_uu
name
Spec syntax   vcmpl {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpl_v32_v32_vpr_neq_uu (4, vIn, vIn2);

Comments

Main table → Comparison And Predicates → Compare → Vector Compare Long
Intrinsic     vcmpl_v32_v32_vpr_uu
name
Spec syntax   vcmpl {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    QOP            uint8     1..4            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpl_v32_v32_vpr_uu (4, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Long
Intrinsic     vcmpl_v32_c32_vpr
name
Spec syntax   vcmpl {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP             uint8     1..4            Number of atomic operations
Operands      2    IN1_V32         vec_t                     Input vector operand
              3    IN2_C32         coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpl_v32_c32_vpr (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Long
Intrinsic     vcmpl_v32_c32_vpr_eq
name
Spec syntax   vcmpl {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP             uint8     1..4            Number of atomic operations
Operands      2    IN1_V32         vec_t                     Input vector operand
              3    IN2_C32         coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...

vecPredRes = vcmpl_v32_c32_vpr_eq (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Long
Intrinsic     vcmpl_v32_c32_vpr_eq_uu
name
Spec syntax   vcmpl {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP             uint8     1..4            Number of atomic operations
Operands      2    IN1_V32         vec_t                     Input vector operand
              3    IN2_C32         coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpl_v32_c32_vpr_eq_uu (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Long
Intrinsic     vcmpl_v32_c32_vpr_ge
name
Spec syntax   vcmpl {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP            uint8     1..4             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpl_v32_c32_vpr_ge (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Long
Intrinsic     vcmpl_v32_c32_vpr_ge_uu
name
Spec syntax   vcmpl {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP            uint8     1..4             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpl_v32_c32_vpr_ge_uu (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Long
Intrinsic     vcmpl_v32_c32_vpr_gt
name
Spec syntax   vcmpl {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP              uint8    1..4            Number of atomic operations
Operands      2    IN1_V32          vec_t                    Input vector operand
              3    IN2_C32          coef_t                   Coefficient operand
              vec_t vIn;

coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpl_v32_c32_vpr_gt (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Long
Intrinsic     vcmpl_v32_c32_vpr_gt_uu
name
Spec syntax   vcmpl {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP              uint8    1..4            Number of atomic operations
Operands      2    IN1_V32          vec_t                    Input vector operand
              3    IN2_C32          coef_t                   Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpl_v32_c32_vpr_gt_uu (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Long
Intrinsic     vcmpl_v32_c32_vpr_le
name
Spec syntax   vcmpl {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP              uint8    1..4            Number of atomic operations
Operands      2    IN1_V32          vec_t                    Input vector operand
              3    IN2_C32          coef_t                   Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpl_v32_c32_vpr_le (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Long
Intrinsic     vcmpl_v32_c32_vpr_le_uu
name
Spec syntax   vcmpl {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP             uint8     1..4             Number of atomic operations
Operands      2    IN1_V32         vec_t                      Input vector operand
              3    IN2_C32         coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpl_v32_c32_vpr_le_uu (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Long
Intrinsic     vcmpl_v32_c32_vpr_lt
name
Spec syntax   vcmpl {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP             uint8     1..4             Number of atomic operations
Operands      2    IN1_V32         vec_t                      Input vector operand

3    IN2_C32         coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpl_v32_c32_vpr_lt (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Long
Intrinsic     vcmpl_v32_c32_vpr_lt_uu
name
Spec syntax   vcmpl {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vcY, VPREX

Return type   vprex_t
              1    QOP             uint8    1..4             Number of atomic operations
Operands      2    IN1_V32         vec_t                     Input vector operand
              3    IN2_C32         coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpl_v32_c32_vpr_lt_uu (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Long
Intrinsic     vcmpl_v32_c32_vpr_neq
name
Spec syntax   vcmpl {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP             uint8    1..4             Number of atomic operations
Operands      2    IN1_V32         vec_t                     Input vector operand
              3    IN2_C32         coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpl_v32_c32_vpr_neq (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Long
Intrinsic     vcmpl_v32_c32_vpr_neq_uu
name
Spec syntax   vcmpl {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP             uint8    1..4             Number of atomic operations
Operands      2    IN1_V32         vec_t                     Input vector operand
              3    IN2_C32         coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpl_v32_c32_vpr_neq_uu (4, vIn, vcoefIn);

Comments

Main table → Comparison And Predicates → Compare → Vector Compare Long
Intrinsic     vcmpl_v32_c32_vpr_uu
name
Spec syntax   vcmpl {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], vcY, VPREX

Return type   vprex_t

              1    QOP            uint8     1..4             Number of atomic operations

Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpl_v32_c32_vpr_uu (4, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Long
Intrinsic     vcmpl_v32_imm32_6_vpr
name
Spec syntax   vcmpl {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1    QOP              uint8   1..4            Number of atomic operations
Operands      2    IN1_V32          vec_t                   Input vector operand
                                              31   31
              3    IN2_IMM32_6 int32        -2 ..2 -1       32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpl_v32_imm32_6_vpr (4, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Long
Intrinsic     vcmpl_v32_imm32_6_vpr_eq
name
Spec syntax   vcmpl {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1    QOP              uint8   1..4            Number of atomic operations
Operands      2    IN1_V32          vec_t                   Input vector operand
                                              31   31
              3    IN2_IMM32_6 int32        -2 ..2 -1       32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpl_v32_imm32_6_vpr_eq (4, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Long
Intrinsic     vcmpl_v32_imm32_6_vpr_eq_uu
name
Spec syntax   vcmpl {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1    QOP              uint8   1..4            Number of atomic operations
Operands      2    IN1_V32          vec_t                   Input vector operand
                                              31   31
              3    IN2_IMM32_6 int32        -2 ..2 -1       32 bit immediate
              vec_t vIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpl_v32_imm32_6_vpr_eq_uu (4, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Long
Intrinsic     vcmpl_v32_imm32_6_vpr_ge
name

Spec syntax   vcmpl {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1   QOP             uint8    1..4             Number of atomic operations
Operands      2   IN1_V32         vec_t                     Input vector operand
                                             31   31
              3   IN2_IMM32_6 int32        -2 ..2 -1        32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpl_v32_imm32_6_vpr_ge (4, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Long
Intrinsic     vcmpl_v32_imm32_6_vpr_ge_uu
name
Spec syntax   vcmpl {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1   QOP             uint8    1..4             Number of atomic operations
Operands      2   IN1_V32         vec_t                     Input vector operand
                                             31   31
              3   IN2_IMM32_6 int32        -2 ..2 -1        32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpl_v32_imm32_6_vpr_ge_uu (4, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Long
Intrinsic     vcmpl_v32_imm32_6_vpr_gt
name
Spec syntax   vcmpl {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

Operands      1   QOP             uint8    1..4             Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand
                                              31   31
              3    IN2_IMM32_6 int32        -2 ..2 -1       32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpl_v32_imm32_6_vpr_gt (4, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Long
Intrinsic     vcmpl_v32_imm32_6_vpr_gt_uu
name
Spec syntax   vcmpl {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1    QOP            uint8     1..4            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
                                              31   31
              3    IN2_IMM32_6 int32        -2 ..2 -1       32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...

vecPredRes = vcmpl_v32_imm32_6_vpr_gt_uu (4, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Long
Intrinsic     vcmpl_v32_imm32_6_vpr_le
name
Spec syntax   vcmpl {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1    QOP            uint8     1..4            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
                                              31   31
              3    IN2_IMM32_6 int32        -2 ..2 -1       32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpl_v32_imm32_6_vpr_le (4, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Long
Intrinsic     vcmpl_v32_imm32_6_vpr_le_uu
name
Spec syntax   vcmpl {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1    QOP            uint8     1..4            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
                                              31   31
              3    IN2_IMM32_6 int32        -2 ..2 -1       32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpl_v32_imm32_6_vpr_le_uu (4, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Long
Intrinsic     vcmpl_v32_imm32_6_vpr_lt
name
Spec syntax   vcmpl {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1    QOP            uint8     1..4            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
                                              31   31
              3    IN2_IMM32_6 int32        -2 ..2 -1       32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpl_v32_imm32_6_vpr_lt (4, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Long
Intrinsic     vcmpl_v32_imm32_6_vpr_lt_uu
name
Spec syntax   vcmpl {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1    QOP            uint8     1..4            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand

31   31
              3    IN2_IMM32_6 int32        -2 ..2 -1       32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpl_v32_imm32_6_vpr_lt_uu (4, vIn, 2);

Comments

Main table → Comparison And Predicates → Compare → Vector Compare Long
Intrinsic     vcmpl_v32_imm32_6_vpr_neq
name
Spec syntax   vcmpl {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1   QOP             uint8    1..4            Number of atomic operations
Operands      2   IN1_V32         vec_t                    Input vector operand
                                             31   31
              3   IN2_IMM32_6 int32        -2 ..2 -1       32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpl_v32_imm32_6_vpr_neq (4, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Long
Intrinsic     vcmpl_v32_imm32_6_vpr_neq_uu
name
Spec syntax   vcmpl {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1   QOP             uint8    1..4            Number of atomic operations
Operands      2   IN1_V32         vec_t                    Input vector operand
                                             31   31
              3   IN2_IMM32_6 int32        -2 ..2 -1       32 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpl_v32_imm32_6_vpr_neq_uu (4, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Long
Intrinsic     vcmpl_v32_imm32_6_vpr_uu
name
Spec syntax   vcmpl {Qop [,eq_neq_gt_ge_lt_le][,uu]} vx[0], #imm32_6, VPREX

Return type   vprex_t

              1   QOP             uint8    1..4            Number of atomic operations
Operands      2   IN1_V32         vec_t                    Input vector operand
                                             31   31
              3   IN2_IMM32_6 int32        -2 ..2 -1       32 bit immediate
            vec_t vIn;
            vprex_t vecPredRes;
C example   ...
            vecPredRes = vcmpl_v32_imm32_6_vpr_uu (4, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Long
