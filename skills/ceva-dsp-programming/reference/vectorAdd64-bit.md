# Arithmetic → Addition → Vector Add 64-bit

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Arithmetic → Addition → Vector Add 64-bit

Vector Add 64-bit

Vector Add 64-bit
Performs addition between two sources into destinations. The sources are 64-bit vector register
type and the destination is 72-bit vector register type.
Available Switches
Qop        Number of atomic operations. An atomic operation is defined as a single addition.
Intrinsic Names
vadd64_v32_v32_v32
Instruction details in the instruction set specification
Intrinsic     vadd64_v32_v32_v32[_p]
name

Spec syntax   vadd64 {Qop} vx[0], vy[0], vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4            Number of atomic operations
              2    IN1_V32         vec_t                     Input vector operand
Operands
              3    IN2_V32         vec_t                     Input vector operand
              4    IN_VPR          vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vadd64_v32_v32_v32_p (4, vIn, vIn2, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vadd64_v32_v32_v32_p version.


Main table → Arithmetic → Addition → Vector Add 64-bit
