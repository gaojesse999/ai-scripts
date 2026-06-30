# Comparison And Predicates → Maximum → Vector Maximum

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Comparison And Predicates → Maximum → Vector Maximum

Vector Maximum

Vector Maximum
Performs maximum operation between two sources. Each source is 32-bit wide. The destination
is 32-bit and the VPREX bit is updated accordingly.
Available Switches
               Number of atomic operations. An atomic operation is defined by a single comparison.
Oop
               1op ≤ Oop ≤ 8op
        When used, the MSB bit of both sources is masked when comparison between the
maskmsb two sources is performed.The MSB bit of the result is not masked.(By default both
        sources they are treated as signed values).
               When used, the sources represented by the 32-bits of the vector part are treated as
uu
               unsigned values (by default they are treated as signed values).
Intrinsic Names
vmax_v32_v32_v32_vpr_maskmsb
vmax_v32_v32_v32_vpr
vmax_v32_v32_v32_vpr_uu
vmax_v32_v32_v32
vmax_v32_v32_v32_uu
Instruction details in the instruction set specification
Intrinsic     vmax_v32_v32_v32_vpr_maskmsb[_p]
name
Spec syntax   vmax {Oop [,uu_maskmsb]} vx[0], vy[0], vz[0], VPREX, ?vprX

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
              vRes = vmax_v32_v32_v32_vpr_maskmsb_p (8, vIn, vIn2, vecPredRes, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vmax_v32_v32_v32_vpr_maskmsb_p version.


Main table → Comparison And Predicates → Maximum → Vector Maximum
Intrinsic     vmax_v32_v32_v32_vpr[_p]
name
Spec syntax   vmax {Oop [,uu_maskmsb]} vx[0], vy[0], vz[0], VPREX, ?vprX

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
              vRes = vmax_v32_v32_v32_vpr_p (8, vIn, vIn2, vecPredRes, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmax_v32_v32_v32_vpr_p version.


Main table → Comparison And Predicates → Maximum → Vector Maximum
Intrinsic     vmax_v32_v32_v32_vpr_uu[_p]
name
Spec syntax   vmax {Oop [,uu_maskmsb]} vx[0], vy[0], vz[0], VPREX, ?vprX

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
              vRes = vmax_v32_v32_v32_vpr_uu_p (8, vIn, vIn2, vecPredRes, vecPred);

                   IN_VPR last operand is relevant only for vmax_v32_v32_v32_vpr_uu_p
Comments      1.
                   version.


Main table → Comparison And Predicates → Maximum → Vector Maximum
Intrinsic     vmax_v32_v32_v32[_p]
name
Spec syntax   vmax {Oop [,uu]} vx[0], vy[0], vz[0], ?vprX

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
              vRes = vmax_v32_v32_v32_p (8, vIn, vIn2, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmax_v32_v32_v32_p version.


Main table → Comparison And Predicates → Maximum → Vector Maximum
Intrinsic     vmax_v32_v32_v32_uu[_p]
name
Spec syntax   vmax {Oop [,uu]} vx[0], vy[0], vz[0], ?vprX

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
              vRes = vmax_v32_v32_v32_uu_p (8, vIn, vIn2, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmax_v32_v32_v32_uu_p version.


Main table → Comparison And Predicates → Maximum → Vector Maximum
