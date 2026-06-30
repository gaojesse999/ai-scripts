# Comparison And Predicates → Maximum → Vector Maximum Word Parts

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Comparison And Predicates → Maximum → Vector Maximum Word Parts

Vector Maximum Word Parts

Vector Maximum Word Parts
Performs two maximum operations between two sources. Each source is 16-bit wide. The results
are packed into 32-bit destination and the VPREX bit is updated accordingly.
Available Switches
        Number of atomic operations. An atomic operation is defined two comparisons. 1op ≤
Oop
        Oop ≤ 8op
        When used, the sources represented by the 16-bits of the vector part are treated as
uu
        unsigned values (by default they are treated as signed values).
Intrinsic Names
vmaxw_v32_v32_v32
vmaxw_v32_v32_v32_uu
vmaxw_v32_v32_v32_vpr
vmaxw_v32_v32_v32_vpr_uu
Instruction details in the instruction set specification
Intrinsic     vmaxw_v32_v32_v32[_p]
name
Spec syntax   vmaxw {Oop [,uu]} vx[0], vy[0], vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand
Operands
              3    IN2_V32        vec_t                      Input vector operand
              4    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmaxw_v32_v32_v32_p (8, vIn, vIn2, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmaxw_v32_v32_v32_p version.


Main table → Comparison And Predicates → Maximum → Vector Maximum Word Parts
Intrinsic     vmaxw_v32_v32_v32_uu[_p]
name
Spec syntax   vmaxw {Oop [,uu]} vx[0], vy[0], vz[0], ?vprX

Return type   vec_t

1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand
Operands
              3    IN2_V32        vec_t                      Input vector operand
              4    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmaxw_v32_v32_v32_uu_p (8, vIn, vIn2, vecPred);

                   IN_VPR last operand is relevant only for vmaxw_v32_v32_v32_uu_p
Comments      1.
                   version.


Main table → Comparison And Predicates → Maximum → Vector Maximum Word Parts
Intrinsic     vmaxw_v32_v32_v32_vpr[_p]
name
Spec syntax   vmaxw {Oop [,uu]} vx[0], vy[0], vz[0], VPREX, ?vprX

Return type   vprex_t

              1    OOP            uint8     1..8            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand
Operands      3    IN2_V32        vec_t                     Input vector operand
              4    RES_V32        vec_t                     Input vector result operand
              5    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vprex_t vRes;
C example     vprex_t vecPred;
              vec_t vecPredRes;
              ...
              vRes = vmaxw_v32_v32_v32_vpr_p (8, vIn, vIn2, vecPredRes, vecPred);

                   IN_VPR last operand is relevant only for vmaxw_v32_v32_v32_vpr_p
Comments      1.
                   version.


Main table → Comparison And Predicates → Maximum → Vector Maximum Word Parts
Intrinsic     vmaxw_v32_v32_v32_vpr_uu[_p]
name
Spec syntax   vmaxw {Oop [,uu]} vx[0], vy[0], vz[0], VPREX, ?vprX

Return type   vprex_t

              1    OOP            uint8     1..8            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand
Operands      3    IN2_V32        vec_t                     Input vector operand
              4    RES_V32        vec_t                     Input vector result operand
              5    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vprex_t vRes;
C example     vprex_t vecPred;
              vec_t vecPredRes;
              ...

vRes = vmaxw_v32_v32_v32_vpr_uu_p (8, vIn, vIn2, vecPredRes, vecPred);

                   IN_VPR last operand is relevant only for vmaxw_v32_v32_v32_vpr_uu_p
Comments      1.
                   version.


Main table → Comparison And Predicates → Maximum → Vector Maximum Word Parts
