# Comparison And Predicates → Compare → Vector Compare Word Parts

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Comparison And Predicates → Compare → Vector Compare Word Parts

Vector Compare Word Parts

Vector Compare Word Parts

Performs comparison between two sources and sets vector predicate registers accordingly. The
sources are 16-bit wide. The destination is 16-bit VPREX.
Available Switches
      Number of atomic operations. An atomic operation is defined by as a single 2-word
Oop
      comparison operation. 1op ≤ Oop ≤ 8op
dup The switch can be used only when Oop is 1op.
      When used, each source which is represented by the 16-bits of the vector parts is treated as
uu
      an unsigned value (by default they are treated as signed values).
Intrinsic Names
vcmpw_v32_imm16_6_vpr
vcmpw_v32_imm16_6_vpr_dup
vcmpw_v32_imm16_6_vpr_dup_uu
vcmpw_v32_imm16_6_vpr_eq
vcmpw_v32_imm16_6_vpr_eq_dup
vcmpw_v32_imm16_6_vpr_eq_dup_uu
vcmpw_v32_imm16_6_vpr_eq_uu
vcmpw_v32_imm16_6_vpr_ge
vcmpw_v32_imm16_6_vpr_ge_dup
vcmpw_v32_imm16_6_vpr_ge_dup_uu
vcmpw_v32_imm16_6_vpr_ge_uu
vcmpw_v32_imm16_6_vpr_gt
vcmpw_v32_imm16_6_vpr_gt_dup
vcmpw_v32_imm16_6_vpr_gt_dup_uu
vcmpw_v32_imm16_6_vpr_gt_uu
vcmpw_v32_imm16_6_vpr_le
vcmpw_v32_imm16_6_vpr_le_dup
vcmpw_v32_imm16_6_vpr_le_dup_uu
vcmpw_v32_imm16_6_vpr_le_uu
vcmpw_v32_imm16_6_vpr_lt
vcmpw_v32_imm16_6_vpr_lt_dup
vcmpw_v32_imm16_6_vpr_lt_dup_uu
vcmpw_v32_imm16_6_vpr_lt_uu
vcmpw_v32_imm16_6_vpr_neq
vcmpw_v32_imm16_6_vpr_neq_dup
vcmpw_v32_imm16_6_vpr_neq_dup_uu
vcmpw_v32_imm16_6_vpr_neq_uu
vcmpw_v32_imm16_6_vpr_uu
vcmpw_v32_v32_vpr
vcmpw_v32_v32_vpr_dup
vcmpw_v32_v32_vpr_dup_uu
vcmpw_v32_v32_vpr_eq
vcmpw_v32_v32_vpr_eq_dup
vcmpw_v32_v32_vpr_eq_dup_uu
vcmpw_v32_v32_vpr_eq_uu
vcmpw_v32_v32_vpr_ge
vcmpw_v32_v32_vpr_ge_dup
vcmpw_v32_v32_vpr_ge_dup_uu
vcmpw_v32_v32_vpr_ge_uu
vcmpw_v32_v32_vpr_gt
vcmpw_v32_v32_vpr_gt_dup
vcmpw_v32_v32_vpr_gt_dup_uu
vcmpw_v32_v32_vpr_gt_uu
vcmpw_v32_v32_vpr_le
vcmpw_v32_v32_vpr_le_dup
vcmpw_v32_v32_vpr_le_dup_uu
vcmpw_v32_v32_vpr_le_uu
vcmpw_v32_v32_vpr_lt
vcmpw_v32_v32_vpr_lt_dup
vcmpw_v32_v32_vpr_lt_dup_uu
vcmpw_v32_v32_vpr_lt_uu
vcmpw_v32_v32_vpr_neq
vcmpw_v32_v32_vpr_neq_dup
vcmpw_v32_v32_vpr_neq_dup_uu
vcmpw_v32_v32_vpr_neq_uu
vcmpw_v32_v32_vpr_uu
vcmpw_v32_c32_vpr
vcmpw_v32_c32_vpr_dup
vcmpw_v32_c32_vpr_dup_uu
vcmpw_v32_c32_vpr_eq
vcmpw_v32_c32_vpr_eq_dup
vcmpw_v32_c32_vpr_eq_dup_uu
vcmpw_v32_c32_vpr_eq_uu
vcmpw_v32_c32_vpr_ge
vcmpw_v32_c32_vpr_ge_dup
vcmpw_v32_c32_vpr_ge_dup_uu
vcmpw_v32_c32_vpr_ge_uu
vcmpw_v32_c32_vpr_gt
vcmpw_v32_c32_vpr_gt_dup
vcmpw_v32_c32_vpr_gt_dup_uu
vcmpw_v32_c32_vpr_gt_uu
vcmpw_v32_c32_vpr_le
vcmpw_v32_c32_vpr_le_dup
vcmpw_v32_c32_vpr_le_dup_uu
vcmpw_v32_c32_vpr_le_uu
vcmpw_v32_c32_vpr_lt

vcmpw_v32_c32_vpr_lt_dup
vcmpw_v32_c32_vpr_lt_dup_uu
vcmpw_v32_c32_vpr_lt_uu
vcmpw_v32_c32_vpr_neq
vcmpw_v32_c32_vpr_neq_dup
vcmpw_v32_c32_vpr_neq_dup_uu
vcmpw_v32_c32_vpr_neq_uu
vcmpw_v32_c32_vpr_uu
Instruction details in the instruction set specification
Intrinsic     vcmpw_v32_imm16_6_vpr
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le] [,dup_sw][,uu]} vx[0], #imm16_6, VPREX

Return type   vprex_t

              1   OOP             uint8    1..8            Number of atomic operations
Operands      2   IN1_V32         vec_t                    Input vector operand
              3   IN2_IMM16_6 int16        -32768..32767   16 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpw_v32_imm16_6_vpr (8, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_imm16_6_vpr_dup
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le] [,dup_sw][,uu]} vx[0], #imm16_6, VPREX

Return type   vprex_t

              1   IN1_V32         vec_t                    Input vector operand
Operands
              2   IN2_IMM16_6 int16        -32768..32767   16 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpw_v32_imm16_6_vpr_dup (vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_imm16_6_vpr_dup_uu
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le] [,dup_sw][,uu]} vx[0], #imm16_6, VPREX

Return type   vprex_t

              1   IN1_V32         vec_t                    Input vector operand
Operands
              2   IN2_IMM16_6 int16        -32768..32767   16 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpw_v32_imm16_6_vpr_dup_uu (vIn, 2);

Comments

Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_imm16_6_vpr_eq
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le] [,dup_sw][,uu]} vx[0], #imm16_6, VPREX

Return type   vprex_t

              1   OOP            uint8     1..8            Number of atomic operations
Operands      2   IN1_V32        vec_t                     Input vector operand
              3   IN2_IMM16_6 int16        -32768..32767   16 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...

vecPredRes = vcmpw_v32_imm16_6_vpr_eq (8, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_imm16_6_vpr_eq_dup
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le] [,dup_sw][,uu]} vx[0], #imm16_6, VPREX

Return type   vprex_t

              1   IN1_V32        vec_t                     Input vector operand
Operands
              2   IN2_IMM16_6 int16        -32768..32767   16 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpw_v32_imm16_6_vpr_eq_dup (vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_imm16_6_vpr_eq_dup_uu
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le] [,dup_sw][,uu]} vx[0], #imm16_6, VPREX

Return type   vprex_t

              1   IN1_V32        vec_t                     Input vector operand
Operands
              2   IN2_IMM16_6 int16        -32768..32767   16 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpw_v32_imm16_6_vpr_eq_dup_uu (vIn, 2);
Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_imm16_6_vpr_eq_uu
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le] [,dup_sw][,uu]} vx[0], #imm16_6, VPREX

Return type   vprex_t

              1   OOP             uint8    1..8            Number of atomic operations
Operands      2   IN1_V32         vec_t                    Input vector operand
              3   IN2_IMM16_6 int16        -32768..32767   16 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpw_v32_imm16_6_vpr_eq_uu (8, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_imm16_6_vpr_ge
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le] [,dup_sw][,uu]} vx[0], #imm16_6, VPREX

Return type   vprex_t

              1   OOP             uint8    1..8            Number of atomic operations
Operands      2   IN1_V32         vec_t                    Input vector operand
              3   IN2_IMM16_6 int16        -32768..32767   16 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpw_v32_imm16_6_vpr_ge (8, vIn, 2);

Comments

Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_imm16_6_vpr_ge_dup
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le] [,dup_sw][,uu]} vx[0], #imm16_6, VPREX

Return type   vprex_t

              1   IN1_V32         vec_t                    Input vector operand
Operands
              2   IN2_IMM16_6 int16        -32768..32767   16 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpw_v32_imm16_6_vpr_ge_dup (vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_imm16_6_vpr_ge_dup_uu
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le] [,dup_sw][,uu]} vx[0], #imm16_6, VPREX

Return type   vprex_t

              1   IN1_V32        vec_t                     Input vector operand
Operands
              2   IN2_IMM16_6 int16        -32768..32767   16 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpw_v32_imm16_6_vpr_ge_dup_uu (vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_imm16_6_vpr_ge_uu
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le] [,dup_sw][,uu]} vx[0], #imm16_6, VPREX

Return type   vprex_t

              1   OOP            uint8     1..8            Number of atomic operations
Operands      2   IN1_V32        vec_t                     Input vector operand
              3   IN2_IMM16_6 int16        -32768..32767   16 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpw_v32_imm16_6_vpr_ge_uu (8, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_imm16_6_vpr_gt
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le] [,dup_sw][,uu]} vx[0], #imm16_6, VPREX

Return type   vprex_t

Operands      1   OOP            uint8     1..8            Number of atomic operations
              2   IN1_V32         vec_t                    Input vector operand
              3   IN2_IMM16_6 int16        -32768..32767   16 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpw_v32_imm16_6_vpr_gt (8, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_imm16_6_vpr_gt_dup

name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le] [,dup_sw][,uu]} vx[0], #imm16_6, VPREX

Return type   vprex_t

              1   IN1_V32         vec_t                    Input vector operand
Operands
              2   IN2_IMM16_6 int16        -32768..32767   16 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpw_v32_imm16_6_vpr_gt_dup (vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_imm16_6_vpr_gt_dup_uu
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le] [,dup_sw][,uu]} vx[0], #imm16_6, VPREX

Return type   vprex_t

              1   IN1_V32         vec_t                    Input vector operand
Operands
              2   IN2_IMM16_6 int16        -32768..32767   16 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpw_v32_imm16_6_vpr_gt_dup_uu (vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_imm16_6_vpr_gt_uu
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le] [,dup_sw][,uu]} vx[0], #imm16_6, VPREX

Return type   vprex_t
              1   OOP             uint8    1..8            Number of atomic operations
Operands      2   IN1_V32         vec_t                    Input vector operand
              3   IN2_IMM16_6 int16        -32768..32767   16 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpw_v32_imm16_6_vpr_gt_uu (8, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_imm16_6_vpr_le
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le] [,dup_sw][,uu]} vx[0], #imm16_6, VPREX

Return type   vprex_t

              1   OOP             uint8    1..8            Number of atomic operations
Operands      2   IN1_V32         vec_t                    Input vector operand
              3   IN2_IMM16_6 int16        -32768..32767   16 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpw_v32_imm16_6_vpr_le (8, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_imm16_6_vpr_le_dup
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le] [,dup_sw][,uu]} vx[0], #imm16_6, VPREX

Return type   vprex_t

1   IN1_V32         vec_t                    Input vector operand
Operands
              2   IN2_IMM16_6 int16        -32768..32767   16 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpw_v32_imm16_6_vpr_le_dup (vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_imm16_6_vpr_le_dup_uu
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le] [,dup_sw][,uu]} vx[0], #imm16_6, VPREX

Return type   vprex_t

              1   IN1_V32         vec_t                    Input vector operand
Operands
              2   IN2_IMM16_6 int16        -32768..32767   16 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpw_v32_imm16_6_vpr_le_dup_uu (vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_imm16_6_vpr_le_uu
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le] [,dup_sw][,uu]} vx[0], #imm16_6, VPREX

Return type   vprex_t

              1   OOP             uint8    1..8            Number of atomic operations
Operands      2   IN1_V32         vec_t                    Input vector operand
              3   IN2_IMM16_6 int16        -32768..32767   16 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpw_v32_imm16_6_vpr_le_uu (8, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_imm16_6_vpr_lt
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le] [,dup_sw][,uu]} vx[0], #imm16_6, VPREX

Return type   vprex_t

              1   OOP             uint8    1..8            Number of atomic operations
Operands      2   IN1_V32         vec_t                    Input vector operand
              3   IN2_IMM16_6 int16        -32768..32767   16 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpw_v32_imm16_6_vpr_lt (8, vIn, 2);

Comments

Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_imm16_6_vpr_lt_dup
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le] [,dup_sw][,uu]} vx[0], #imm16_6, VPREX

Return type   vprex_t

              1   IN1_V32         vec_t                    Input vector operand
Operands

2   IN2_IMM16_6 int16        -32768..32767   16 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpw_v32_imm16_6_vpr_lt_dup (vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_imm16_6_vpr_lt_dup_uu
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le] [,dup_sw][,uu]} vx[0], #imm16_6, VPREX

Return type   vprex_t

              1   IN1_V32         vec_t                    Input vector operand
Operands
              2   IN2_IMM16_6 int16        -32768..32767   16 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpw_v32_imm16_6_vpr_lt_dup_uu (vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_imm16_6_vpr_lt_uu
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le] [,dup_sw][,uu]} vx[0], #imm16_6, VPREX

Return type   vprex_t

              1   OOP             uint8    1..8            Number of atomic operations
Operands      2   IN1_V32         vec_t                    Input vector operand
              3   IN2_IMM16_6 int16        -32768..32767   16 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpw_v32_imm16_6_vpr_lt_uu (8, vIn, 2);
Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_imm16_6_vpr_neq
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le] [,dup_sw][,uu]} vx[0], #imm16_6, VPREX

Return type   vprex_t

              1    OOP              uint8   1..8            Number of atomic operations
Operands      2    IN1_V32          vec_t                   Input vector operand
              3    IN2_IMM16_6 int16        -32768..32767   16 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpw_v32_imm16_6_vpr_neq (8, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_imm16_6_vpr_neq_dup
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le] [,dup_sw][,uu]} vx[0], #imm16_6, VPREX

Return type   vprex_t

              1    IN1_V32          vec_t                   Input vector operand
Operands
              2    IN2_IMM16_6 int16        -32768..32767   16 bit immediate
              vec_t vIn;

vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpw_v32_imm16_6_vpr_neq_dup (vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_imm16_6_vpr_neq_dup_uu
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le] [,dup_sw][,uu]} vx[0], #imm16_6, VPREX

Return type   vprex_t

              1    IN1_V32          vec_t                   Input vector operand
Operands
              2    IN2_IMM16_6 int16        -32768..32767   16 bit immediate
              vec_t vIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_imm16_6_vpr_neq_dup_uu (vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_imm16_6_vpr_neq_uu
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le] [,dup_sw][,uu]} vx[0], #imm16_6, VPREX

Return type   vprex_t

              1   OOP            uint8     1..8            Number of atomic operations
Operands      2   IN1_V32        vec_t                     Input vector operand
              3   IN2_IMM16_6 int16        -32768..32767   16 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpw_v32_imm16_6_vpr_neq_uu (8, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_imm16_6_vpr_uu
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le] [,dup_sw][,uu]} vx[0], #imm16_6, VPREX

Return type   vprex_t

              1   OOP            uint8     1..8            Number of atomic operations
Operands      2   IN1_V32        vec_t                     Input vector operand
              3   IN2_IMM16_6 int16        -32768..32767   16 bit immediate
              vec_t vIn;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcmpw_v32_imm16_6_vpr_uu (8, vIn, 2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_v32_vpr
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8               Number of atomic operations
Operands      2    IN1_V32        vec_t                        Input vector operand
              3    IN2_V32        vec_t                        Input vector operand
              vec_t vIn;
              vec_t vIn2;

C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_v32_vpr (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_v32_vpr_dup
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                        Input vector operand
Operands
              2    IN2_V32        vec_t                        Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_v32_vpr_dup (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_v32_vpr_dup_uu
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                        Input vector operand
Operands
              2    IN2_V32        vec_t                        Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_v32_vpr_dup_uu (vIn, vIn2);
Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_v32_vpr_eq
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8    1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_v32_vpr_eq (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_v32_vpr_eq_dup
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                     Input vector operand
Operands
              2    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...

vecPredRes = vcmpw_v32_v32_vpr_eq_dup (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_v32_vpr_eq_dup_uu
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                     Input vector operand
Operands
              2    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_v32_vpr_eq_dup_uu (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_v32_vpr_eq_uu
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_v32_vpr_eq_uu (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_v32_vpr_ge
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_v32_vpr_ge (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_v32_vpr_ge_dup
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                    Input vector operand
Operands
              2    IN2_V32        vec_t                    Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...

vecPredRes = vcmpw_v32_v32_vpr_ge_dup (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_v32_vpr_ge_dup_uu
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                    Input vector operand
Operands
              2    IN2_V32        vec_t                    Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_v32_vpr_ge_dup_uu (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_v32_vpr_ge_uu
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8    1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                    Input vector operand
              3    IN2_V32        vec_t                    Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_v32_vpr_ge_uu (8, vIn, vIn2);

Comments

Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_v32_vpr_gt
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_v32_vpr_gt (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_v32_vpr_gt_dup
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                     Input vector operand
Operands
              2    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...

vecPredRes = vcmpw_v32_v32_vpr_gt_dup (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_v32_vpr_gt_dup_uu
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                     Input vector operand
Operands
              2    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
C example     vec_t vIn2;
              vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_v32_vpr_gt_dup_uu (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_v32_vpr_gt_uu
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_v32_vpr_gt_uu (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_v32_vpr_le
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_v32_vpr_le (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_v32_vpr_le_dup
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vy[0], VPREX
Return type   vprex_t

              1    IN1_V32        vec_t                     Input vector operand
Operands
              2    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...

vecPredRes = vcmpw_v32_v32_vpr_le_dup (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_v32_vpr_le_dup_uu
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                     Input vector operand
Operands
              2    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_v32_vpr_le_dup_uu (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_v32_vpr_le_uu
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8    1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_v32_vpr_le_uu (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_v32_vpr_lt
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_v32_vpr_lt (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_v32_vpr_lt_dup
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                      Input vector operand
Operands
              2    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...

vecPredRes = vcmpw_v32_v32_vpr_lt_dup (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_v32_vpr_lt_dup_uu
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                      Input vector operand
Operands
              2    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_v32_vpr_lt_dup_uu (vIn, vIn2);
Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_v32_vpr_lt_uu
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_v32_vpr_lt_uu (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_v32_vpr_neq
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_v32_vpr_neq (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_v32_vpr_neq_dup
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

Operands      1    IN1_V32        vec_t                     Input vector operand
              2    IN2_V32        vec_t                    Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...

vecPredRes = vcmpw_v32_v32_vpr_neq_dup (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_v32_vpr_neq_dup_uu
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                    Input vector operand
Operands
              2    IN2_V32        vec_t                    Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_v32_vpr_neq_dup_uu (vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_v32_vpr_neq_uu
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8    1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                    Input vector operand
              3    IN2_V32        vec_t                    Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_v32_vpr_neq_uu (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_v32_vpr_uu
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8    1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN2_V32        vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_v32_vpr_uu (8, vIn, vIn2);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_c32_vpr
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vcYp, VPREX

Return type   vprex_t

              1    OOP            uint8    1..8             Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand
Operands
              3    IN2_C32        coef_t                    Coefficient operand

4    IN2_PART       uint8    LOW,HIGH         Word part which is used for operand 3
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_c32_vpr (8, vIn, vcoefIn, LOW);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_c32_vpr_dup
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vcYp, VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                     Input vector operand
Operands      2    IN2_C32        coef_t                    Coefficient operand
              3    IN2_PART       uint8    LOW,HIGH         Word part which is used for operand 2
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_c32_vpr_dup (vIn, vcoefIn, LOW);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_c32_vpr_dup_uu
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vcYp, VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                     Input vector operand
Operands
              2    IN2_C32        coef_t                    Coefficient operand
              3    IN2_PART       uint8    LOW,HIGH        Word part which is used for operand 2
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_c32_vpr_dup_uu (vIn, vcoefIn, LOW);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_c32_vpr_eq
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vcYp, VPREX

Return type   vprex_t

              1    OOP            uint8    1..8            Number of atomic operations
              2    IN1_V32        vec_t                    Input vector operand
Operands
              3    IN2_C32        coef_t                   Coefficient operand
              4    IN2_PART       uint8    LOW,HIGH        Word part which is used for operand 3
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_c32_vpr_eq (8, vIn, vcoefIn, LOW);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts

Intrinsic     vcmpw_v32_c32_vpr_eq_dup
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vcYp, VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                    Input vector operand
Operands      2    IN2_C32        coef_t                   Coefficient operand
              3    IN2_PART       uint8    LOW,HIGH        Word part which is used for operand 2
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_c32_vpr_eq_dup (vIn, vcoefIn, LOW);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_c32_vpr_eq_dup_uu
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vcYp, VPREX

Return type   vprex_t

              1   IN1_V32        vec_t                     Input vector operand
Operands      2   IN2_C32        coef_t                    Coefficient operand
              3   IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 2
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_c32_vpr_eq_dup_uu (vIn, vcoefIn, LOW);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_c32_vpr_eq_uu
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vcYp, VPREX

Return type   vprex_t

              1   OOP            uint8     1..8            Number of atomic operations
              2   IN1_V32        vec_t                     Input vector operand
Operands
              3   IN2_C32        coef_t                    Coefficient operand
              4   IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 3
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_c32_vpr_eq_uu (8, vIn, vcoefIn, LOW);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_c32_vpr_ge
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vcYp, VPREX

Return type   vprex_t

              1   OOP            uint8     1..8            Number of atomic operations
Operands
              2   IN1_V32        vec_t                     Input vector operand

3    IN2_C32        coef_t                   Coefficient operand
              4    IN2_PART       uint8    LOW,HIGH        Word part which is used for operand 3
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_c32_vpr_ge (8, vIn, vcoefIn, LOW);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_c32_vpr_ge_dup
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vcYp, VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                    Input vector operand
Operands      2    IN2_C32        coef_t                   Coefficient operand
              3    IN2_PART       uint8    LOW,HIGH        Word part which is used for operand 2
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_c32_vpr_ge_dup (vIn, vcoefIn, LOW);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_c32_vpr_ge_dup_uu
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vcYp, VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                    Input vector operand
Operands      2    IN2_C32        coef_t                   Coefficient operand
              3    IN2_PART       uint8    LOW,HIGH        Word part which is used for operand 2
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_c32_vpr_ge_dup_uu (vIn, vcoefIn, LOW);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_c32_vpr_ge_uu
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vcYp, VPREX

Return type   vprex_t

              1    OOP            uint8    1..8             Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand
Operands
              3    IN2_C32        coef_t                    Coefficient operand
              4    IN2_PART       uint8    LOW,HIGH         Word part which is used for operand 3
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_c32_vpr_ge_uu (8, vIn, vcoefIn, LOW);

Comments

Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_c32_vpr_gt
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vcYp, VPREX

Return type   vprex_t

              1    OOP            uint8    1..8             Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand
Operands
              3    IN2_C32        coef_t                    Coefficient operand
              4    IN2_PART       uint8    LOW,HIGH         Word part which is used for operand 3
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_c32_vpr_gt (8, vIn, vcoefIn, LOW);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_c32_vpr_gt_dup
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vcYp, VPREX

Return type   vprex_t

Operands      1    IN1_V32        vec_t                     Input vector operand
              2    IN2_C32        coef_t                   Coefficient operand
              3    IN2_PART       uint8    LOW,HIGH        Word part which is used for operand 2
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_c32_vpr_gt_dup (vIn, vcoefIn, LOW);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_c32_vpr_gt_dup_uu
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vcYp, VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                    Input vector operand
Operands      2    IN2_C32        coef_t                   Coefficient operand
              3    IN2_PART       uint8    LOW,HIGH        Word part which is used for operand 2
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_c32_vpr_gt_dup_uu (vIn, vcoefIn, LOW);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_c32_vpr_gt_uu
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vcYp, VPREX

Return type   vprex_t

              1    OOP            uint8    1..8            Number of atomic operations

2    IN1_V32        vec_t                    Input vector operand
Operands
              3    IN2_C32        coef_t                   Coefficient operand
              4    IN2_PART       uint8    LOW,HIGH        Word part which is used for operand 3
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_c32_vpr_gt_uu (8, vIn, vcoefIn, LOW);

Comments

Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_c32_vpr_le
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vcYp, VPREX

Return type   vprex_t

              1    OOP            uint8    1..8             Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand
Operands
              3    IN2_C32        coef_t                    Coefficient operand
              4    IN2_PART       uint8    LOW,HIGH         Word part which is used for operand 3
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_c32_vpr_le (8, vIn, vcoefIn, LOW);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_c32_vpr_le_dup
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vcYp, VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                     Input vector operand
Operands      2    IN2_C32        coef_t                    Coefficient operand
              3    IN2_PART       uint8    LOW,HIGH         Word part which is used for operand 2
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_c32_vpr_le_dup (vIn, vcoefIn, LOW);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_c32_vpr_le_dup_uu
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vcYp, VPREX

Return type   vprex_t

Operands      1    IN1_V32        vec_t                     Input vector operand
              2    IN2_C32        coef_t                    Coefficient operand
              3    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 2
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...

vecPredRes = vcmpw_v32_c32_vpr_le_dup_uu (vIn, vcoefIn, LOW);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_c32_vpr_le_uu
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vcYp, VPREX

Return type   vprex_t

              1    OOP            uint8     1..8            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand
Operands
              3    IN2_C32        coef_t                    Coefficient operand
              4    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 3
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_c32_vpr_le_uu (8, vIn, vcoefIn, LOW);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_c32_vpr_lt
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vcYp, VPREX

Return type   vprex_t

              1    OOP            uint8     1..8            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand
Operands
              3    IN2_C32        coef_t                    Coefficient operand
              4    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 3
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_c32_vpr_lt (8, vIn, vcoefIn, LOW);
Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_c32_vpr_lt_dup
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vcYp, VPREX

Return type   vprex_t

              1   IN1_V32        vec_t                     Input vector operand
Operands      2   IN2_C32        coef_t                    Coefficient operand
              3   IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 2
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_c32_vpr_lt_dup (vIn, vcoefIn, LOW);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_c32_vpr_lt_dup_uu
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vcYp, VPREX

Return type   vprex_t

              1   IN1_V32        vec_t                     Input vector operand
Operands      2   IN2_C32        coef_t                    Coefficient operand
              3   IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 2
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_c32_vpr_lt_dup_uu (vIn, vcoefIn, LOW);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_c32_vpr_lt_uu
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vcYp, VPREX

Return type   vprex_t

Operands      1   OOP            uint8     1..8            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand
              3    IN2_C32        coef_t                    Coefficient operand
              4    IN2_PART       uint8    LOW,HIGH         Word part which is used for operand 3
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_c32_vpr_lt_uu (8, vIn, vcoefIn, LOW);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_c32_vpr_neq
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vcYp, VPREX

Return type   vprex_t

              1    OOP            uint8    1..8             Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand
Operands
              3    IN2_C32        coef_t                    Coefficient operand
              4    IN2_PART       uint8    LOW,HIGH         Word part which is used for operand 3
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_c32_vpr_neq (8, vIn, vcoefIn, LOW);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_c32_vpr_neq_dup
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vcYp, VPREX

Return type   vprex_t

              1    IN1_V32        vec_t                     Input vector operand
Operands      2    IN2_C32        coef_t                    Coefficient operand
              3    IN2_PART       uint8    LOW,HIGH         Word part which is used for operand 2

vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_c32_vpr_neq_dup (vIn, vcoefIn, LOW);
Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_c32_vpr_neq_dup_uu
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vcYp, VPREX

Return type   vprex_t

              1   IN1_V32        vec_t                     Input vector operand
Operands      2   IN2_C32        coef_t                    Coefficient operand
              3   IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 2
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_c32_vpr_neq_dup_uu (vIn, vcoefIn, LOW);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_c32_vpr_neq_uu
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vcYp, VPREX

Return type   vprex_t

              1   OOP            uint8     1..8            Number of atomic operations
              2   IN1_V32        vec_t                     Input vector operand
Operands
              3   IN2_C32        coef_t                    Coefficient operand
              4   IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 3
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcmpw_v32_c32_vpr_neq_uu (8, vIn, vcoefIn, LOW);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
Intrinsic     vcmpw_v32_c32_vpr_uu
name
Spec syntax   vcmpw {Oop [,eq_neq_gt_ge_lt_le][,dup_sw][,uu]} vx[0], vcYp, VPREX

Return type   vprex_t
            1    OOP            uint8    1..8            Number of atomic operations
            2    IN1_V32        vec_t                    Input vector operand
Operands
            3    IN2_C32        coef_t                   Coefficient operand
            4    IN2_PART       uint8    LOW,HIGH        Word part which is used for operand 3
            vec_t vIn;
            coef_t vcoefIn;
C example   vprex_t vecPredRes;
            ...
            vecPredRes = vcmpw_v32_c32_vpr_uu (8, vIn, vcoefIn, LOW);

Comments


Main table → Comparison And Predicates → Compare → Vector Compare Word Parts
