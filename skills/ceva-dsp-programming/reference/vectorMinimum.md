# Comparison And Predicates → Minimum → Vector Minimum

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Comparison And Predicates → Minimum → Vector Minimum

Vector Minimum

Vector Minimum

Performs minimum operation between two sources. Each source is 32-bit wide. The destination
is 32-bit and the VPREX bit is updated accordingly.
Available Switches
       Number of atomic operations. An atomic operation is defined by a single comparison. 1op
Oop
       ≤ Oop ≤ 8op
       When used, the sources represented by the 32-bits of the vector part are treated as unsigned
uu
       values (by default they are treated as signed values).
Intrinsic Names
vmin_v32_v32_v32
vmin_v32_v32_v32_uu
vmin_v32_v32_v32_vpr
vmin_v32_v32_v32_vpr_uu
Instruction details in the instruction set specification
Intrinsic     vmin_v32_v32_v32[_p]
name
Spec syntax   vmin {Oop [,uu]} vx[0], vy[0], vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8            Number of atomic operations
              2    IN1_V32         vec_t                     Input vector operand
Operands
              3    IN2_V32         vec_t                     Input vector operand
              4    IN_VPR          vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmin_v32_v32_v32_p (8, vIn, vIn2, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmin_v32_v32_v32_p version.


Main table → Comparison And Predicates → Minimum → Vector Minimum
Intrinsic     vmin_v32_v32_v32_uu[_p]
name
Spec syntax   vmin {Oop [,uu]} vx[0], vy[0], vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8            Number of atomic operations
              2    IN1_V32         vec_t                     Input vector operand
Operands
              3    IN2_V32         vec_t                     Input vector operand
              4    IN_VPR          vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmin_v32_v32_v32_uu_p (8, vIn, vIn2, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmin_v32_v32_v32_uu_p version.


Main table → Comparison And Predicates → Minimum → Vector Minimum
Intrinsic     vmin_v32_v32_v32_vpr[_p]
name
Spec syntax   vmin {Oop [,uu]} vx[0], vy[0], vz[0], VPREX, ?vprX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations

2    IN1_V32        vec_t                      Input vector operand
Operands      3    IN2_V32        vec_t                      Input vector operand
              4    RES_V32        vec_t                      Input vector result operand
              5    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vprex_t vRes;
C example     vprex_t vecPred;
              vec_t vecPredRes;
              ...
              vRes = vmin_v32_v32_v32_vpr_p (8, vIn, vIn2, vecPredRes, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmin_v32_v32_v32_vpr_p version.


Main table → Comparison And Predicates → Minimum → Vector Minimum
Intrinsic     vmin_v32_v32_v32_vpr_uu[_p]
name
Spec syntax   vmin {Oop [,uu]} vx[0], vy[0], vz[0], VPREX, ?vprX

Return type   vprex_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand
Operands      3    IN2_V32        vec_t                      Input vector operand
              4    RES_V32        vec_t                      Input vector result operand
              5    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vprex_t vRes;
C example     vprex_t vecPred;
              vec_t vecPredRes;
              ...
              vRes = vmin_v32_v32_v32_vpr_uu_p (8, vIn, vIn2, vecPredRes, vecPred);

                   IN_VPR last operand is relevant only for vmin_v32_v32_v32_vpr_uu_p
Comments      1.
                   version.


Main table → Comparison And Predicates → Minimum → Vector Minimum
