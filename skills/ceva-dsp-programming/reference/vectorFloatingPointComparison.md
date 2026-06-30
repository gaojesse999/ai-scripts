# Floating Point → Float Compare → Vector Floating Point Comparison

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Floating Point → Float Compare → Vector Floating Point Comparison

Vector Floating Point Comparison

Vector Floating Point Comparison
Performs comparison between two sources and set vector predicate bits accordingly. The sources
are 32-bit single precision floating-point numbers. The destination is 8-bit VPREX.
Available Switches
None
Intrinsic Names
vflpcmp_v32_v32_vpr
vflpcmp_v32_v32_vpr_eq
vflpcmp_v32_v32_vpr_eq_hi
vflpcmp_v32_v32_vpr_eq_hi_qsignal
vflpcmp_v32_v32_vpr_eq_low
vflpcmp_v32_v32_vpr_eq_low_qsignal
vflpcmp_v32_v32_vpr_eq_qsignal
vflpcmp_v32_v32_vpr_ge
vflpcmp_v32_v32_vpr_ge_hi
vflpcmp_v32_v32_vpr_ge_hi_qsignal
vflpcmp_v32_v32_vpr_ge_low
vflpcmp_v32_v32_vpr_ge_low_qsignal
vflpcmp_v32_v32_vpr_ge_qsignal
vflpcmp_v32_v32_vpr_gt
vflpcmp_v32_v32_vpr_gt_hi
vflpcmp_v32_v32_vpr_gt_hi_qsignal
vflpcmp_v32_v32_vpr_gt_low
vflpcmp_v32_v32_vpr_gt_low_qsignal
vflpcmp_v32_v32_vpr_gt_qsignal
vflpcmp_v32_v32_vpr_hi
vflpcmp_v32_v32_vpr_hi_qsignal
vflpcmp_v32_v32_vpr_le
vflpcmp_v32_v32_vpr_le_hi
vflpcmp_v32_v32_vpr_le_hi_qsignal
vflpcmp_v32_v32_vpr_le_low
vflpcmp_v32_v32_vpr_le_low_qsignal
vflpcmp_v32_v32_vpr_le_qsignal
vflpcmp_v32_v32_vpr_low
vflpcmp_v32_v32_vpr_low_qsignal
vflpcmp_v32_v32_vpr_lt
vflpcmp_v32_v32_vpr_lt_hi
vflpcmp_v32_v32_vpr_lt_hi_qsignal
vflpcmp_v32_v32_vpr_lt_low

vflpcmp_v32_v32_vpr_lt_low_qsignal
vflpcmp_v32_v32_vpr_lt_qsignal
vflpcmp_v32_v32_vpr_neq
vflpcmp_v32_v32_vpr_neq_hi
vflpcmp_v32_v32_vpr_neq_hi_qsignal
vflpcmp_v32_v32_vpr_neq_low
vflpcmp_v32_v32_vpr_neq_low_qsignal
vflpcmp_v32_v32_vpr_neq_qsignal
vflpcmp_v32_v32_vpr_qsignal
vflpcmp_v32_c32_vpr
vflpcmp_v32_c32_vpr_eq
vflpcmp_v32_c32_vpr_eq_hi
vflpcmp_v32_c32_vpr_eq_hi_qsignal
vflpcmp_v32_c32_vpr_eq_low
vflpcmp_v32_c32_vpr_eq_low_qsignal
vflpcmp_v32_c32_vpr_eq_qsignal
vflpcmp_v32_c32_vpr_ge
vflpcmp_v32_c32_vpr_ge_hi
vflpcmp_v32_c32_vpr_ge_hi_qsignal
vflpcmp_v32_c32_vpr_ge_low
vflpcmp_v32_c32_vpr_ge_low_qsignal
vflpcmp_v32_c32_vpr_ge_qsignal
vflpcmp_v32_c32_vpr_gt
vflpcmp_v32_c32_vpr_gt_hi
vflpcmp_v32_c32_vpr_gt_hi_qsignal
vflpcmp_v32_c32_vpr_gt_low
vflpcmp_v32_c32_vpr_gt_low_qsignal
vflpcmp_v32_c32_vpr_gt_qsignal
vflpcmp_v32_c32_vpr_hi
vflpcmp_v32_c32_vpr_hi_qsignal
vflpcmp_v32_c32_vpr_le
vflpcmp_v32_c32_vpr_le_hi
vflpcmp_v32_c32_vpr_le_hi_qsignal
vflpcmp_v32_c32_vpr_le_low
vflpcmp_v32_c32_vpr_le_low_qsignal
vflpcmp_v32_c32_vpr_le_qsignal
vflpcmp_v32_c32_vpr_low
vflpcmp_v32_c32_vpr_low_qsignal
vflpcmp_v32_c32_vpr_lt
vflpcmp_v32_c32_vpr_lt_hi
vflpcmp_v32_c32_vpr_lt_hi_qsignal
vflpcmp_v32_c32_vpr_lt_low
vflpcmp_v32_c32_vpr_lt_low_qsignal
vflpcmp_v32_c32_vpr_lt_qsignal
vflpcmp_v32_c32_vpr_neq
vflpcmp_v32_c32_vpr_neq_hi
vflpcmp_v32_c32_vpr_neq_hi_qsignal
vflpcmp_v32_c32_vpr_neq_low
vflpcmp_v32_c32_vpr_neq_low_qsignal
vflpcmp_v32_c32_vpr_neq_qsignal
vflpcmp_v32_c32_vpr_qsignal
Instruction details in the instruction set specification
Intrinsic     vflpcmp_v32_v32_vpr
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_v32_vpr (8, vIn, vIn2);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_v32_vpr_eq
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations

Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_v32_vpr_eq (8, vIn, vIn2);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_v32_vpr_eq_hi
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_v32_vpr_eq_hi (8, vIn, vIn2);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_v32_vpr_eq_hi_qsignal
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_v32_vpr_eq_hi_qsignal (8, vIn, vIn2);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_v32_vpr_eq_low
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_v32_vpr_eq_low (8, vIn, vIn2);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison

Intrinsic     vflpcmp_v32_v32_vpr_eq_low_qsignal
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP              uint8   1..8             Number of atomic operations
Operands      2    IN1_V32          vec_t                    Input vector operand
              3    IN2_V32          vec_t                    Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_v32_vpr_eq_low_qsignal (8, vIn, vIn2);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_v32_vpr_eq_qsignal
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP              uint8   1..8             Number of atomic operations
Operands      2    IN1_V32          vec_t                    Input vector operand
              3    IN2_V32          vec_t                    Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_v32_vpr_eq_qsignal (8, vIn, vIn2);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_v32_vpr_ge
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP              uint8   1..8             Number of atomic operations
Operands      2    IN1_V32          vec_t                    Input vector operand
              3    IN2_V32          vec_t                    Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_v32_vpr_ge (8, vIn, vIn2);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_v32_vpr_ge_hi
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;

vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_v32_vpr_ge_hi (8, vIn, vIn2);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_v32_vpr_ge_hi_qsignal
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_v32_vpr_ge_hi_qsignal (8, vIn, vIn2);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_v32_vpr_ge_low
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vy[0], VPREX

Return type   vprex_t
              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_v32_vpr_ge_low (8, vIn, vIn2);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_v32_vpr_ge_low_qsignal
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_v32_vpr_ge_low_qsignal (8, vIn, vIn2);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_v32_vpr_ge_qsignal
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vy[0], VPREX

Return type   vprex_t

1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_v32_vpr_ge_qsignal (8, vIn, vIn2);

Comments

Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_v32_vpr_gt
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_v32_vpr_gt (8, vIn, vIn2);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_v32_vpr_gt_hi
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_v32_vpr_gt_hi (8, vIn, vIn2);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_v32_vpr_gt_hi_qsignal
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands
              2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_v32_vpr_gt_hi_qsignal (8, vIn, vIn2);

Comments

Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_v32_vpr_gt_low
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_v32_vpr_gt_low (8, vIn, vIn2);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_v32_vpr_gt_low_qsignal
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_v32_vpr_gt_low_qsignal (8, vIn, vIn2);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_v32_vpr_gt_qsignal
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_v32_vpr_gt_qsignal (8, vIn, vIn2);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_v32_vpr_hi
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand

3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_v32_vpr_hi (8, vIn, vIn2);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_v32_vpr_hi_qsignal
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
C example     vec_t vIn2;
              vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_v32_vpr_hi_qsignal (8, vIn, vIn2);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_v32_vpr_le
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP             uint8    1..8             Number of atomic operations
Operands      2    IN1_V32         vec_t                     Input vector operand
              3    IN2_V32         vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_v32_vpr_le (8, vIn, vIn2);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_v32_vpr_le_hi
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP             uint8    1..8             Number of atomic operations
Operands      2    IN1_V32         vec_t                     Input vector operand
              3    IN2_V32         vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_v32_vpr_le_hi (8, vIn, vIn2);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_v32_vpr_le_hi_qsignal
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_v32_vpr_le_hi_qsignal (8, vIn, vIn2);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_v32_vpr_le_low
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_v32_vpr_le_low (8, vIn, vIn2);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_v32_vpr_le_low_qsignal
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_v32_vpr_le_low_qsignal (8, vIn, vIn2);
Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_v32_vpr_le_qsignal
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...

vecPredRes = vflpcmp_v32_v32_vpr_le_qsignal (8, vIn, vIn2);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_v32_vpr_low
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_v32_vpr_low (8, vIn, vIn2);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_v32_vpr_low_qsignal
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vy[0], VPREX

Return type   vprex_t

Operands      1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand
              3    IN2_V32         vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_v32_vpr_low_qsignal (8, vIn, vIn2);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_v32_vpr_lt
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP             uint8     1..8             Number of atomic operations
Operands      2    IN1_V32         vec_t                      Input vector operand
              3    IN2_V32         vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_v32_vpr_lt (8, vIn, vIn2);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_v32_vpr_lt_hi
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP             uint8     1..8             Number of atomic operations

Operands      2    IN1_V32         vec_t                      Input vector operand
              3    IN2_V32         vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_v32_vpr_lt_hi (8, vIn, vIn2);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_v32_vpr_lt_hi_qsignal
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP             uint8    1..8             Number of atomic operations
Operands      2    IN1_V32         vec_t                     Input vector operand
              3    IN2_V32         vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_v32_vpr_lt_hi_qsignal (8, vIn, vIn2);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_v32_vpr_lt_low
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP             uint8    1..8             Number of atomic operations
Operands      2    IN1_V32         vec_t                     Input vector operand
              3    IN2_V32         vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_v32_vpr_lt_low (8, vIn, vIn2);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_v32_vpr_lt_low_qsignal
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP             uint8    1..8             Number of atomic operations
Operands      2    IN1_V32         vec_t                     Input vector operand
              3    IN2_V32         vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_v32_vpr_lt_low_qsignal (8, vIn, vIn2);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison

Intrinsic     vflpcmp_v32_v32_vpr_lt_qsignal
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP             uint8    1..8             Number of atomic operations
Operands      2    IN1_V32         vec_t                     Input vector operand
              3    IN2_V32         vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_v32_vpr_lt_qsignal (8, vIn, vIn2);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_v32_vpr_neq
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP             uint8    1..8             Number of atomic operations
Operands      2    IN1_V32         vec_t                     Input vector operand
              3    IN2_V32         vec_t                     Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_v32_vpr_neq (8, vIn, vIn2);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_v32_vpr_neq_hi
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP              uint8   1..8             Number of atomic operations
Operands      2    IN1_V32          vec_t                    Input vector operand
              3    IN2_V32          vec_t                    Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_v32_vpr_neq_hi (8, vIn, vIn2);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_v32_vpr_neq_hi_qsignal
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP              uint8   1..8             Number of atomic operations
Operands      2    IN1_V32          vec_t                    Input vector operand
              3    IN2_V32          vec_t                    Input vector operand
              vec_t vIn;
              vec_t vIn2;

C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_v32_vpr_neq_hi_qsignal (8, vIn, vIn2);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_v32_vpr_neq_low
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP              uint8   1..8             Number of atomic operations
Operands      2    IN1_V32          vec_t                    Input vector operand
              3    IN2_V32          vec_t                    Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_v32_vpr_neq_low (8, vIn, vIn2);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_v32_vpr_neq_low_qsignal
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_v32_vpr_neq_low_qsignal (8, vIn, vIn2);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_v32_vpr_neq_qsignal
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vy[0], VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
              vec_t vIn;
              vec_t vIn2;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_v32_vpr_neq_qsignal (8, vIn, vIn2);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_v32_vpr_qsignal
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vy[0], VPREX

Return type   vprex_t

1    OOP            uint8     1..8             Number of atomic operations
Operands    2    IN1_V32        vec_t                      Input vector operand
            3    IN2_V32        vec_t                      Input vector operand
            vec_t vIn;
            vec_t vIn2;
C example   vprex_t vecPredRes;
            ...
            vecPredRes = vflpcmp_v32_v32_vpr_qsignal (8, vIn, vIn2);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_c32_vpr
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP             uint8     1..8            Number of atomic operations
Operands      2    IN1_V32         vec_t                     Input vector operand
              3    IN2_C32         coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_c32_vpr (8, vIn, vcoefIn);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_c32_vpr_eq
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP             uint8     1..8            Number of atomic operations
Operands      2    IN1_V32         vec_t                     Input vector operand
              3    IN2_C32         coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_c32_vpr_eq (8, vIn, vcoefIn);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_c32_vpr_eq_hi
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP             uint8     1..8            Number of atomic operations
Operands      2    IN1_V32         vec_t                     Input vector operand
              3    IN2_C32         coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_c32_vpr_eq_hi (8, vIn, vcoefIn);

Comments

Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_c32_vpr_eq_hi_qsignal
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_c32_vpr_eq_hi_qsignal (8, vIn, vcoefIn);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_c32_vpr_eq_low
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_c32_vpr_eq_low (8, vIn, vcoefIn);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_c32_vpr_eq_low_qsignal
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP              uint8    1..8            Number of atomic operations
Operands      2    IN1_V32          vec_t                    Input vector operand
              3    IN2_C32          coef_t                   Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_c32_vpr_eq_low_qsignal (8, vIn, vcoefIn);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_c32_vpr_eq_qsignal
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP              uint8    1..8            Number of atomic operations
Operands      2    IN1_V32          vec_t                    Input vector operand

3    IN2_C32          coef_t                   Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_c32_vpr_eq_qsignal (8, vIn, vcoefIn);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_c32_vpr_ge
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP              uint8    1..8            Number of atomic operations
Operands      2    IN1_V32          vec_t                    Input vector operand
              3    IN2_C32          coef_t                   Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_c32_vpr_ge (8, vIn, vcoefIn);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_c32_vpr_ge_hi
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_c32_vpr_ge_hi (8, vIn, vcoefIn);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_c32_vpr_ge_hi_qsignal
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_c32_vpr_ge_hi_qsignal (8, vIn, vcoefIn);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_c32_vpr_ge_low
name

Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vcY, VPREX

Return type   vprex_t
              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_c32_vpr_ge_low (8, vIn, vcoefIn);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_c32_vpr_ge_low_qsignal
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_c32_vpr_ge_low_qsignal (8, vIn, vcoefIn);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_c32_vpr_ge_qsignal
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_c32_vpr_ge_qsignal (8, vIn, vcoefIn);

Comments

Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_c32_vpr_gt
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP             uint8    1..8             Number of atomic operations
Operands      2    IN1_V32         vec_t                     Input vector operand
              3    IN2_C32         coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;

C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_c32_vpr_gt (8, vIn, vcoefIn);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_c32_vpr_gt_hi
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP             uint8    1..8             Number of atomic operations
Operands      2    IN1_V32         vec_t                     Input vector operand
              3    IN2_C32         coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_c32_vpr_gt_hi (8, vIn, vcoefIn);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_c32_vpr_gt_hi_qsignal
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP             uint8    1..8             Number of atomic operations
Operands
              2    IN1_V32         vec_t                     Input vector operand
              3    IN2_C32         coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_c32_vpr_gt_hi_qsignal (8, vIn, vcoefIn);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_c32_vpr_gt_low
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP             uint8    1..8             Number of atomic operations
Operands      2    IN1_V32         vec_t                     Input vector operand
              3    IN2_C32         coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_c32_vpr_gt_low (8, vIn, vcoefIn);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_c32_vpr_gt_low_qsignal
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vcY, VPREX

Return type   vprex_t

1    OOP             uint8    1..8             Number of atomic operations
Operands      2    IN1_V32         vec_t                     Input vector operand
              3    IN2_C32         coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_c32_vpr_gt_low_qsignal (8, vIn, vcoefIn);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_c32_vpr_gt_qsignal
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP             uint8    1..8             Number of atomic operations
Operands      2    IN1_V32         vec_t                     Input vector operand
              3    IN2_C32         coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_c32_vpr_gt_qsignal (8, vIn, vcoefIn);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_c32_vpr_hi
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP             uint8    1..8             Number of atomic operations
Operands      2    IN1_V32         vec_t                     Input vector operand
              3    IN2_C32         coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_c32_vpr_hi (8, vIn, vcoefIn);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_c32_vpr_hi_qsignal
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP             uint8    1..8             Number of atomic operations
Operands      2    IN1_V32         vec_t                     Input vector operand
              3    IN2_C32         coef_t                    Coefficient operand
              vec_t vIn;
C example     coef_t vcoefIn;
              vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_c32_vpr_hi_qsignal (8, vIn, vcoefIn);

Comments

Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_c32_vpr_le
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP             uint8     1..8             Number of atomic operations
Operands      2    IN1_V32         vec_t                      Input vector operand
              3    IN2_C32         coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_c32_vpr_le (8, vIn, vcoefIn);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_c32_vpr_le_hi
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP             uint8     1..8             Number of atomic operations
Operands      2    IN1_V32         vec_t                      Input vector operand
              3    IN2_C32         coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_c32_vpr_le_hi (8, vIn, vcoefIn);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_c32_vpr_le_hi_qsignal
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vcY, VPREX
Return type   vprex_t

              1    OOP             uint8     1..8            Number of atomic operations
Operands      2    IN1_V32         vec_t                     Input vector operand
              3    IN2_C32         coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_c32_vpr_le_hi_qsignal (8, vIn, vcoefIn);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_c32_vpr_le_low
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP             uint8     1..8            Number of atomic operations
Operands      2    IN1_V32         vec_t                     Input vector operand

3    IN2_C32         coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_c32_vpr_le_low (8, vIn, vcoefIn);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_c32_vpr_le_low_qsignal
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP             uint8     1..8            Number of atomic operations
Operands      2    IN1_V32         vec_t                     Input vector operand
              3    IN2_C32         coef_t                    Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_c32_vpr_le_low_qsignal (8, vIn, vcoefIn);
Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_c32_vpr_le_qsignal
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP             uint8     1..8             Number of atomic operations
Operands      2    IN1_V32         vec_t                      Input vector operand
              3    IN2_C32         coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_c32_vpr_le_qsignal (8, vIn, vcoefIn);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_c32_vpr_low
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP             uint8     1..8             Number of atomic operations
Operands      2    IN1_V32         vec_t                      Input vector operand
              3    IN2_C32         coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_c32_vpr_low (8, vIn, vcoefIn);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_c32_vpr_low_qsignal
name

Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vcY, VPREX

Return type   vprex_t

Operands      1    OOP             uint8     1..8             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand
              3    IN2_C32         coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_c32_vpr_low_qsignal (8, vIn, vcoefIn);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_c32_vpr_lt
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP             uint8     1..8             Number of atomic operations
Operands      2    IN1_V32         vec_t                      Input vector operand
              3    IN2_C32         coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_c32_vpr_lt (8, vIn, vcoefIn);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_c32_vpr_lt_hi
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP             uint8     1..8             Number of atomic operations
Operands      2    IN1_V32         vec_t                      Input vector operand
              3    IN2_C32         coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_c32_vpr_lt_hi (8, vIn, vcoefIn);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_c32_vpr_lt_hi_qsignal
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP             uint8     1..8             Number of atomic operations
Operands      2    IN1_V32         vec_t                      Input vector operand
              3    IN2_C32         coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;

C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_c32_vpr_lt_hi_qsignal (8, vIn, vcoefIn);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_c32_vpr_lt_low
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP             uint8     1..8             Number of atomic operations
Operands      2    IN1_V32         vec_t                      Input vector operand
              3    IN2_C32         coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_c32_vpr_lt_low (8, vIn, vcoefIn);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_c32_vpr_lt_low_qsignal
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP             uint8     1..8             Number of atomic operations
Operands      2    IN1_V32         vec_t                      Input vector operand
              3    IN2_C32         coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_c32_vpr_lt_low_qsignal (8, vIn, vcoefIn);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_c32_vpr_lt_qsignal
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP             uint8     1..8             Number of atomic operations
Operands      2    IN1_V32         vec_t                      Input vector operand
              3    IN2_C32         coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_c32_vpr_lt_qsignal (8, vIn, vcoefIn);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_c32_vpr_neq
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vcY, VPREX

Return type   vprex_t

1    OOP             uint8     1..8             Number of atomic operations
Operands      2    IN1_V32         vec_t                      Input vector operand
              3    IN2_C32         coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_c32_vpr_neq (8, vIn, vcoefIn);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_c32_vpr_neq_hi
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP              uint8    1..8            Number of atomic operations
Operands      2    IN1_V32          vec_t                    Input vector operand
              3    IN2_C32          coef_t                   Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_c32_vpr_neq_hi (8, vIn, vcoefIn);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_c32_vpr_neq_hi_qsignal
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP              uint8    1..8            Number of atomic operations
Operands      2    IN1_V32          vec_t                    Input vector operand
              3    IN2_C32          coef_t                   Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_c32_vpr_neq_hi_qsignal (8, vIn, vcoefIn);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_c32_vpr_neq_low
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP              uint8    1..8            Number of atomic operations
Operands      2    IN1_V32          vec_t                    Input vector operand
              3    IN2_C32          coef_t                   Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_c32_vpr_neq_low (8, vIn, vcoefIn);

Comments

Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_c32_vpr_neq_low_qsignal
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_c32_vpr_neq_low_qsignal (8, vIn, vcoefIn);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_c32_vpr_neq_qsignal
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vcY, VPREX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
              vec_t vIn;
              coef_t vcoefIn;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vflpcmp_v32_c32_vpr_neq_qsignal (8, vIn, vcoefIn);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
Intrinsic     vflpcmp_v32_c32_vpr_qsignal
name
Spec syntax   vflpcmp {Oop [,eq_neq_gt_ge_lt_le][,low_hi][,qsignal]} vx[0], vcY, VPREX

Return type   vprex_t
            1    OOP             uint8    1..8             Number of atomic operations
Operands    2    IN1_V32         vec_t                     Input vector operand
            3    IN2_C32         coef_t                    Coefficient operand
            vec_t vIn;
            coef_t vcoefIn;
C example   vprex_t vecPredRes;
            ...
            vecPredRes = vflpcmp_v32_c32_vpr_qsignal (8, vIn, vcoefIn);

Comments


Main table → Floating Point → Float Compare → Vector Floating Point Comparison
