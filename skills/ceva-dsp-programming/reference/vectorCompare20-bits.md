# Comparison And Predicates → Compare → Vector Compare 20-bits

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Comparison And Predicates → Compare → Vector Compare 20-bits

Vector Compare 20-bits

Vector Compare 20-bits
Performs comparison between two sources and sets vector predicate registers accordingly. The
sources are 20-bit wide. The destination is 16-bit VPREX.
Available Switches
      Number of atomic operations. An atomic operation is defined by as a single comparison
Hop
      operation. 1op ≤ Hop ≤ 16op
      When used, each source which is represented by the 20-bits of the vector parts is treated as
uu
      an unsigned value (by default they are treated as signed values).
Intrinsic Names
vcmp20_v40_v40_vpr
vcmp20_v40_v40_vpr_eq
vcmp20_v40_v40_vpr_eq_uu
vcmp20_v40_v40_vpr_ge
vcmp20_v40_v40_vpr_ge_uu
vcmp20_v40_v40_vpr_gt
vcmp20_v40_v40_vpr_gt_uu
vcmp20_v40_v40_vpr_le
vcmp20_v40_v40_vpr_le_uu
vcmp20_v40_v40_vpr_lt
vcmp20_v40_v40_vpr_lt_uu
vcmp20_v40_v40_vpr_neq
vcmp20_v40_v40_vpr_neq_uu
vcmp20_v40_v40_vpr_uu
vcmp20_v40_c32_vpr

vcmp20_v40_c32_vpr_eq
vcmp20_v40_c32_vpr_eq_uu
vcmp20_v40_c32_vpr_ge
vcmp20_v40_c32_vpr_ge_uu
vcmp20_v40_c32_vpr_gt
vcmp20_v40_c32_vpr_gt_uu
vcmp20_v40_c32_vpr_le
vcmp20_v40_c32_vpr_le_uu
vcmp20_v40_c32_vpr_lt
vcmp20_v40_c32_vpr_lt_uu
vcmp20_v40_c32_vpr_neq
vcmp20_v40_c32_vpr_neq_uu
vcmp20_v40_c32_vpr_uu
vcmp20_v40_imm6_vpr
vcmp20_v40_imm6_vpr_eq
vcmp20_v40_imm6_vpr_eq_uu
vcmp20_v40_imm6_vpr_ge
vcmp20_v40_imm6_vpr_ge_uu
vcmp20_v40_imm6_vpr_gt
vcmp20_v40_imm6_vpr_gt_uu
vcmp20_v40_imm6_vpr_le
vcmp20_v40_imm6_vpr_le_uu
vcmp20_v40_imm6_vpr_lt
vcmp20_v40_imm6_vpr_lt_uu
vcmp20_v40_imm6_vpr_neq
vcmp20_v40_imm6_vpr_neq_uu
vcmp20_v40_imm6_vpr_uu
Instruction details in the instruction set specification
Intrinsic     vcmp20_v40_v40_vpr
name
Spec syntax   vcmp20 {Hop [,eq_neq_gt_ge_lt_le][,uu]} vox[0], voy[0],VPREX

Return type   vprex_t

              1    HOP            uint8     1..16           Number of atomic operations
Operands      2    IN1_V40        vec40_t                   Output vector operand
              3    IN2_V40        vec40_t                   Output vector operand
              vec40_t vIn;
              vec40_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp20_v40_v40_vpr (16, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare 20-bits
Intrinsic     vcmp20_v40_v40_vpr_eq
name
Spec syntax   vcmp20 {Hop [,eq_neq_gt_ge_lt_le][,uu]} vox[0], voy[0],VPREX

Return type   vprex_t

              1    HOP            uint8     1..16           Number of atomic operations
Operands      2    IN1_V40        vec40_t                   Output vector operand
              3    IN2_V40        vec40_t                   Output vector operand
              vec40_t vIn;
              vec40_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp20_v40_v40_vpr_eq (16, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare 20-bits
Intrinsic     vcmp20_v40_v40_vpr_eq_uu
name
Spec syntax   vcmp20 {Hop [,eq_neq_gt_ge_lt_le][,uu]} vox[0], voy[0],VPREX

Return type   vprex_t

              1    HOP            uint8     1..16           Number of atomic operations
Operands      2    IN1_V40        vec40_t                   Output vector operand
              3    IN2_V40        vec40_t                   Output vector operand
              vec40_t vIn;
              vec40_t vIn2;
C example     vprex_t vecPredRes;

...
              vecPredRes = vcmp20_v40_v40_vpr_eq_uu (16, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare 20-bits
Intrinsic     vcmp20_v40_v40_vpr_ge
name
Spec syntax   vcmp20 {Hop [,eq_neq_gt_ge_lt_le][,uu]} vox[0], voy[0],VPREX

Return type   vprex_t

              1    HOP            uint8     1..16           Number of atomic operations
Operands      2    IN1_V40        vec40_t                   Output vector operand
              3    IN2_V40        vec40_t                   Output vector operand
              vec40_t vIn;
              vec40_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp20_v40_v40_vpr_ge (16, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare 20-bits
Intrinsic     vcmp20_v40_v40_vpr_ge_uu
name
Spec syntax   vcmp20 {Hop [,eq_neq_gt_ge_lt_le][,uu]} vox[0], voy[0],VPREX

Return type   vprex_t

              1    HOP            uint8     1..16           Number of atomic operations
Operands      2    IN1_V40        vec40_t                   Output vector operand
              3    IN2_V40        vec40_t                   Output vector operand
              vec40_t vIn;
              vec40_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp20_v40_v40_vpr_ge_uu (16, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare 20-bits
Intrinsic     vcmp20_v40_v40_vpr_gt
name
Spec syntax   vcmp20 {Hop [,eq_neq_gt_ge_lt_le][,uu]} vox[0], voy[0],VPREX

Return type   vprex_t

              1    HOP              uint8     1..16         Number of atomic operations
Operands      2    IN1_V40          vec40_t                 Output vector operand
              3    IN2_V40          vec40_t                 Output vector operand
              vec40_t vIn;
              vec40_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp20_v40_v40_vpr_gt (16, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare 20-bits
Intrinsic     vcmp20_v40_v40_vpr_gt_uu
name
Spec syntax   vcmp20 {Hop [,eq_neq_gt_ge_lt_le][,uu]} vox[0], voy[0],VPREX

Return type   vprex_t

              1    HOP              uint8     1..16         Number of atomic operations
Operands      2    IN1_V40          vec40_t                 Output vector operand

3    IN2_V40          vec40_t                 Output vector operand
              vec40_t vIn;
              vec40_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp20_v40_v40_vpr_gt_uu (16, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare 20-bits
Intrinsic     vcmp20_v40_v40_vpr_le
name
Spec syntax   vcmp20 {Hop [,eq_neq_gt_ge_lt_le][,uu]} vox[0], voy[0],VPREX

Return type   vprex_t

              1    HOP              uint8     1..16         Number of atomic operations
Operands      2    IN1_V40          vec40_t                 Output vector operand
              3    IN2_V40          vec40_t                 Output vector operand
              vec40_t vIn;
              vec40_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp20_v40_v40_vpr_le (16, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare 20-bits
Intrinsic     vcmp20_v40_v40_vpr_le_uu
name
Spec syntax   vcmp20 {Hop [,eq_neq_gt_ge_lt_le][,uu]} vox[0], voy[0],VPREX

Return type   vprex_t

              1    HOP            uint8     1..16            Number of atomic operations
Operands      2    IN1_V40        vec40_t                    Output vector operand
              3    IN2_V40        vec40_t                    Output vector operand
              vec40_t vIn;
              vec40_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp20_v40_v40_vpr_le_uu (16, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare 20-bits
Intrinsic     vcmp20_v40_v40_vpr_lt
name
Spec syntax   vcmp20 {Hop [,eq_neq_gt_ge_lt_le][,uu]} vox[0], voy[0],VPREX

Return type   vprex_t

              1    HOP            uint8     1..16            Number of atomic operations
Operands      2    IN1_V40        vec40_t                    Output vector operand
              3    IN2_V40        vec40_t                    Output vector operand
              vec40_t vIn;
              vec40_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp20_v40_v40_vpr_lt (16, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare 20-bits
Intrinsic     vcmp20_v40_v40_vpr_lt_uu
name
Spec syntax   vcmp20 {Hop [,eq_neq_gt_ge_lt_le][,uu]} vox[0], voy[0],VPREX

Return type   vprex_t

1    HOP            uint8     1..16           Number of atomic operations
Operands      2    IN1_V40        vec40_t                   Output vector operand
              3    IN2_V40        vec40_t                   Output vector operand
              vec40_t vIn;
              vec40_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp20_v40_v40_vpr_lt_uu (16, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare 20-bits
Intrinsic     vcmp20_v40_v40_vpr_neq
name
Spec syntax   vcmp20 {Hop [,eq_neq_gt_ge_lt_le][,uu]} vox[0], voy[0],VPREX

Return type   vprex_t

              1    HOP            uint8     1..16           Number of atomic operations
Operands      2    IN1_V40        vec40_t                   Output vector operand
              3    IN2_V40        vec40_t                   Output vector operand
              vec40_t vIn;
              vec40_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp20_v40_v40_vpr_neq (16, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare 20-bits
Intrinsic     vcmp20_v40_v40_vpr_neq_uu
name
Spec syntax   vcmp20 {Hop [,eq_neq_gt_ge_lt_le][,uu]} vox[0], voy[0],VPREX

Return type   vprex_t

              1    HOP            uint8     1..16           Number of atomic operations
Operands      2    IN1_V40        vec40_t                   Output vector operand
              3    IN2_V40        vec40_t                   Output vector operand
              vec40_t vIn;
              vec40_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp20_v40_v40_vpr_neq_uu (16, vIn, vIn2);

Comments

Main table → Comparison And Predicates → Compare → Vector Compare 20-bits
Intrinsic     vcmp20_v40_v40_vpr_uu
name
Spec syntax   vcmp20 {Hop [,eq_neq_gt_ge_lt_le][,uu]} vox[0], voy[0],VPREX

Return type   vprex_t

              1    HOP            uint8     1..16           Number of atomic operations
Operands      2    IN1_V40        vec40_t                   Output vector operand
              3    IN2_V40        vec40_t                   Output vector operand
              vec40_t vIn;
              vec40_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp20_v40_v40_vpr_uu (16, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare 20-bits
Intrinsic     vcmp20_v40_c32_vpr
name

Spec syntax   vcmp20 {Hop [,eq_neq_gt_ge_lt_le][,uu]} vox[0], vcY,VPREX

Return type   vprex_t

              1    HOP            uint8     1..16            Number of atomic operations
Operands      2    IN1_V40        vec40_t                    Output vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec40_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp20_v40_c32_vpr (16, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare 20-bits
Intrinsic     vcmp20_v40_c32_vpr_eq
name
Spec syntax   vcmp20 {Hop [,eq_neq_gt_ge_lt_le][,uu]} vox[0], vcY,VPREX

Return type   vprex_t

              1    HOP            uint8     1..16            Number of atomic operations
Operands      2    IN1_V40        vec40_t                    Output vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec40_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp20_v40_c32_vpr_eq (16, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare 20-bits
Intrinsic     vcmp20_v40_c32_vpr_eq_uu
name
Spec syntax   vcmp20 {Hop [,eq_neq_gt_ge_lt_le][,uu]} vox[0], vcY,VPREX

Return type   vprex_t

              1    HOP            uint8     1..16            Number of atomic operations
Operands      2    IN1_V40        vec40_t                    Output vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec40_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp20_v40_c32_vpr_eq_uu (16, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare 20-bits
Intrinsic     vcmp20_v40_c32_vpr_ge
name
Spec syntax   vcmp20 {Hop [,eq_neq_gt_ge_lt_le][,uu]} vox[0], vcY,VPREX

Return type   vprex_t

              1    HOP            uint8     1..16            Number of atomic operations
Operands      2    IN1_V40        vec40_t                    Output vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec40_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp20_v40_c32_vpr_ge (16, vIn, vcoefIn);

Comments

Main table → Comparison And Predicates → Compare → Vector Compare 20-bits
Intrinsic     vcmp20_v40_c32_vpr_ge_uu
name
Spec syntax   vcmp20 {Hop [,eq_neq_gt_ge_lt_le][,uu]} vox[0], vcY,VPREX

Return type   vprex_t

              1    HOP            uint8     1..16            Number of atomic operations
Operands      2    IN1_V40        vec40_t                    Output vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec40_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp20_v40_c32_vpr_ge_uu (16, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare 20-bits
Intrinsic     vcmp20_v40_c32_vpr_gt
name
Spec syntax   vcmp20 {Hop [,eq_neq_gt_ge_lt_le][,uu]} vox[0], vcY,VPREX

Return type   vprex_t

              1    HOP              uint8     1..16          Number of atomic operations
Operands      2    IN1_V40          vec40_t                  Output vector operand
              3    IN2_C32          coef_t                   Coefficient operand
              vec40_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp20_v40_c32_vpr_gt (16, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare 20-bits
Intrinsic     vcmp20_v40_c32_vpr_gt_uu
name
Spec syntax   vcmp20 {Hop [,eq_neq_gt_ge_lt_le][,uu]} vox[0], vcY,VPREX

Return type   vprex_t

              1    HOP              uint8     1..16          Number of atomic operations
Operands      2    IN1_V40          vec40_t                  Output vector operand
              3    IN2_C32          coef_t                   Coefficient operand
              vec40_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp20_v40_c32_vpr_gt_uu (16, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare 20-bits
Intrinsic     vcmp20_v40_c32_vpr_le
name
Spec syntax   vcmp20 {Hop [,eq_neq_gt_ge_lt_le][,uu]} vox[0], vcY,VPREX

Return type   vprex_t

              1    HOP              uint8     1..16          Number of atomic operations
Operands      2    IN1_V40          vec40_t                  Output vector operand
              3    IN2_C32          coef_t                   Coefficient operand
              vec40_t vIn;
              coef_t vcoefIn;

C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp20_v40_c32_vpr_le (16, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare 20-bits
Intrinsic     vcmp20_v40_c32_vpr_le_uu
name
Spec syntax   vcmp20 {Hop [,eq_neq_gt_ge_lt_le][,uu]} vox[0], vcY,VPREX

Return type   vprex_t

              1    HOP            uint8     1..16            Number of atomic operations
Operands      2    IN1_V40        vec40_t                    Output vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec40_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp20_v40_c32_vpr_le_uu (16, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare 20-bits
Intrinsic     vcmp20_v40_c32_vpr_lt
name
Spec syntax   vcmp20 {Hop [,eq_neq_gt_ge_lt_le][,uu]} vox[0], vcY,VPREX

Return type   vprex_t

              1    HOP            uint8     1..16            Number of atomic operations
Operands      2    IN1_V40        vec40_t                    Output vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec40_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp20_v40_c32_vpr_lt (16, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare 20-bits
Intrinsic     vcmp20_v40_c32_vpr_lt_uu
name
Spec syntax   vcmp20 {Hop [,eq_neq_gt_ge_lt_le][,uu]} vox[0], vcY,VPREX

Return type   vprex_t
              1    HOP            uint8     1..16            Number of atomic operations
Operands      2    IN1_V40        vec40_t                    Output vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec40_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp20_v40_c32_vpr_lt_uu (16, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare 20-bits
Intrinsic     vcmp20_v40_c32_vpr_neq
name
Spec syntax   vcmp20 {Hop [,eq_neq_gt_ge_lt_le][,uu]} vox[0], vcY,VPREX

Return type   vprex_t

              1    HOP            uint8     1..16            Number of atomic operations
Operands      2    IN1_V40        vec40_t                    Output vector operand

3    IN2_C32        coef_t                     Coefficient operand
              vec40_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp20_v40_c32_vpr_neq (16, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare 20-bits
Intrinsic     vcmp20_v40_c32_vpr_neq_uu
name
Spec syntax   vcmp20 {Hop [,eq_neq_gt_ge_lt_le][,uu]} vox[0], vcY,VPREX

Return type   vprex_t

              1    HOP            uint8     1..16            Number of atomic operations
Operands      2    IN1_V40        vec40_t                    Output vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec40_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp20_v40_c32_vpr_neq_uu (16, vIn, vcoefIn);

Comments

Main table → Comparison And Predicates → Compare → Vector Compare 20-bits
Intrinsic     vcmp20_v40_c32_vpr_uu
name
Spec syntax   vcmp20 {Hop [,eq_neq_gt_ge_lt_le][,uu]} vox[0], vcY,VPREX

Return type   vprex_t

              1    HOP            uint8     1..16           Number of atomic operations
Operands      2    IN1_V40        vec40_t                   Output vector operand
              3    IN2_C32        coef_t                    Coefficient operand
              vec40_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp20_v40_c32_vpr_uu (16, vIn, vcoefIn);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare 20-bits
Intrinsic     vcmp20_v40_imm6_vpr
name
Spec syntax   vcmp20 {Hop [,eq_neq_gt_ge_lt_le][,uu]} vox[0], #imm6,VPREX

Return type   vprex_t

              1    HOP              uint8     1..16        Number of atomic operations
Operands      2    IN1_V40          vec40_t                Output vector operand
              3    IN2_IMM6         int16     -32..31      6 bit immediate
              vec40_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmp20_v40_imm6_vpr (16, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare 20-bits
Intrinsic     vcmp20_v40_imm6_vpr_eq
name
Spec syntax   vcmp20 {Hop [,eq_neq_gt_ge_lt_le][,uu]} vox[0], #imm6,VPREX

Return type   vprex_t

              1    HOP              uint8     1..16        Number of atomic operations

Operands      2    IN1_V40          vec40_t                Output vector operand
              3    IN2_IMM6         int16     -32..31      6 bit immediate
              vec40_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmp20_v40_imm6_vpr_eq (16, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare 20-bits
Intrinsic     vcmp20_v40_imm6_vpr_eq_uu
name
Spec syntax   vcmp20 {Hop [,eq_neq_gt_ge_lt_le][,uu]} vox[0], #imm6,VPREX

Return type   vprex_t

              1    HOP              uint8     1..16        Number of atomic operations
Operands      2    IN1_V40          vec40_t                Output vector operand
              3    IN2_IMM6         int16     -32..31      6 bit immediate
              vec40_t vIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmp20_v40_imm6_vpr_eq_uu (16, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare 20-bits
Intrinsic     vcmp20_v40_imm6_vpr_ge
name
Spec syntax   vcmp20 {Hop [,eq_neq_gt_ge_lt_le][,uu]} vox[0], #imm6,VPREX

Return type   vprex_t

              1   HOP            uint8     1..16           Number of atomic operations
Operands      2   IN1_V40        vec40_t                   Output vector operand
              3   IN2_IMM6       int16     -32..31         6 bit immediate
              vec40_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmp20_v40_imm6_vpr_ge (16, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare 20-bits
Intrinsic     vcmp20_v40_imm6_vpr_ge_uu
name
Spec syntax   vcmp20 {Hop [,eq_neq_gt_ge_lt_le][,uu]} vox[0], #imm6,VPREX

Return type   vprex_t

              1   HOP            uint8     1..16           Number of atomic operations
Operands      2   IN1_V40        vec40_t                   Output vector operand
              3   IN2_IMM6       int16     -32..31         6 bit immediate
              vec40_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmp20_v40_imm6_vpr_ge_uu (16, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare 20-bits
Intrinsic     vcmp20_v40_imm6_vpr_gt
name
Spec syntax   vcmp20 {Hop [,eq_neq_gt_ge_lt_le][,uu]} vox[0], #imm6,VPREX

Return type   vprex_t

Operands      1   HOP            uint8     1..16           Number of atomic operations

2    IN1_V40        vec40_t                   Output vector operand
              3    IN2_IMM6       int16     -32..31         6 bit immediate
              vec40_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmp20_v40_imm6_vpr_gt (16, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare 20-bits
Intrinsic     vcmp20_v40_imm6_vpr_gt_uu
name
Spec syntax   vcmp20 {Hop [,eq_neq_gt_ge_lt_le][,uu]} vox[0], #imm6,VPREX

Return type   vprex_t

              1    HOP            uint8     1..16           Number of atomic operations
Operands      2    IN1_V40        vec40_t                   Output vector operand
              3    IN2_IMM6       int16     -32..31         6 bit immediate
              vec40_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmp20_v40_imm6_vpr_gt_uu (16, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare 20-bits
Intrinsic     vcmp20_v40_imm6_vpr_le
name
Spec syntax   vcmp20 {Hop [,eq_neq_gt_ge_lt_le][,uu]} vox[0], #imm6,VPREX

Return type   vprex_t

              1    HOP            uint8     1..16           Number of atomic operations
Operands      2    IN1_V40        vec40_t                   Output vector operand
              3    IN2_IMM6       int16     -32..31         6 bit immediate
              vec40_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmp20_v40_imm6_vpr_le (16, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare 20-bits
Intrinsic     vcmp20_v40_imm6_vpr_le_uu
name
Spec syntax   vcmp20 {Hop [,eq_neq_gt_ge_lt_le][,uu]} vox[0], #imm6,VPREX

Return type   vprex_t

              1    HOP            uint8     1..16           Number of atomic operations
Operands      2    IN1_V40        vec40_t                   Output vector operand
              3    IN2_IMM6       int16     -32..31         6 bit immediate
              vec40_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmp20_v40_imm6_vpr_le_uu (16, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare 20-bits
Intrinsic     vcmp20_v40_imm6_vpr_lt
name
Spec syntax   vcmp20 {Hop [,eq_neq_gt_ge_lt_le][,uu]} vox[0], #imm6,VPREX

Return type   vprex_t

              1    HOP            uint8     1..16           Number of atomic operations

Operands      2    IN1_V40        vec40_t                   Output vector operand
              3    IN2_IMM6       int16     -32..31         6 bit immediate
              vec40_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmp20_v40_imm6_vpr_lt (16, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare 20-bits
Intrinsic     vcmp20_v40_imm6_vpr_lt_uu
name
Spec syntax   vcmp20 {Hop [,eq_neq_gt_ge_lt_le][,uu]} vox[0], #imm6,VPREX

Return type   vprex_t

              1    HOP            uint8     1..16           Number of atomic operations
Operands      2    IN1_V40        vec40_t                   Output vector operand
              3    IN2_IMM6       int16     -32..31         6 bit immediate
              vec40_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmp20_v40_imm6_vpr_lt_uu (16, vIn, 2);

Comments

Main table → Comparison And Predicates → Compare → Vector Compare 20-bits
Intrinsic     vcmp20_v40_imm6_vpr_neq
name
Spec syntax   vcmp20 {Hop [,eq_neq_gt_ge_lt_le][,uu]} vox[0], #imm6,VPREX

Return type   vprex_t

              1   HOP            uint8     1..16           Number of atomic operations
Operands      2   IN1_V40        vec40_t                   Output vector operand
              3   IN2_IMM6       int16     -32..31         6 bit immediate
              vec40_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmp20_v40_imm6_vpr_neq (16, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare 20-bits
Intrinsic     vcmp20_v40_imm6_vpr_neq_uu
name
Spec syntax   vcmp20 {Hop [,eq_neq_gt_ge_lt_le][,uu]} vox[0], #imm6,VPREX

Return type   vprex_t

              1   HOP            uint8     1..16           Number of atomic operations
Operands      2   IN1_V40        vec40_t                   Output vector operand
              3   IN2_IMM6       int16     -32..31         6 bit immediate
              vec40_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmp20_v40_imm6_vpr_neq_uu (16, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare 20-bits
Intrinsic     vcmp20_v40_imm6_vpr_uu
name
Spec syntax   vcmp20 {Hop [,eq_neq_gt_ge_lt_le][,uu]} vox[0], #imm6,VPREX

Return type   vprex_t

              1   HOP            uint8     1..16           Number of atomic operations

Operands      2   IN1_V40        vec40_t                   Output vector operand
              3   IN2_IMM6       int16     -32..31         6 bit immediate
            vec40_t vIn;
            vprex_t vecPredRes;
C example   ...
            vecPredRes = vcmp20_v40_imm6_vpr_uu (16, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare 20-bits
