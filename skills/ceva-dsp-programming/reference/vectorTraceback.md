# Special Algorithms → Traceback → Vector traceback

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Special Algorithms → Traceback → Vector traceback

Vector traceback

Vector traceback
Performs vector traceback operation on 32-bit source. The destination is 32-bit wide.
Available Switches
kX          k value, X holds values of 7 or 9.
Intrinsic Names
vtracback_v32_v32_k7
vtracback_v32_v32_k9
vtracback_v32_v32_k5
Instruction details in the instruction set specification
Intrinsic     vtracback_v32_v32_k7[_p]
name
Spec syntax   vtracback {k7|k9} vx[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32        vec_t                      Input vector operand
Operands      2    IN2_V32        vec_t                      Input vector operand
              3    IN_VPR         vprex_t                    Vector predicate operand

vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vtracback_v32_v32_k7_p (vIn, vRes, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vtracback_v32_v32_k7_p version.


Main table → Special Algorithms → Traceback → Vector traceback
Intrinsic     vtracback_v32_v32_k9[_p]
name
Spec syntax   vtracback {k7|k9} vx[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32        vec_t                      Input vector operand
Operands      2    IN2_V32        vec_t                      Input vector operand
              3    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vtracback_v32_v32_k9_p (vIn, vRes, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vtracback_v32_v32_k9_p version.


Main table → Special Algorithms → Traceback → Vector traceback
Intrinsic     vtracback_v32_v32_k5[_p]
name
Spec syntax   vtracback {k5} vx[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32        vec_t                      Input vector operand
Operands      2    IN2_V32        vec_t                      Input vector operand
              3    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vtracback_v32_v32_k5_p (vIn, vRes, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vtracback_v32_v32_k5_p version.


Main table → Special Algorithms → Traceback → Vector traceback
