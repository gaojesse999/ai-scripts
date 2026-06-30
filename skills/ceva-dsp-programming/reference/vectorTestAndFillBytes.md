# Bit Manipulation → Test and Fill → Vector Test and Fill Bytes

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Bit Manipulation → Test and Fill → Vector Test and Fill Bytes

Vector Test and Fill Bytes

Vector Test and Fill Bytes
Performs fill destination with two byte constant values from a common register source. The
destination is either 32-bit or 40-bit wide determined by the register type.
Available Switches
None
Intrinsic Names
vtstfillb_v32_c32_v32
Instruction details in the instruction set specification
Intrinsic     vtstfillb_v32_c32_v32[_p]
name
Spec syntax   vtstfillb vx[0], vcY, vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                       Input vector operand
Operands      2    IN2_C32         coef_t                      Coefficient operand
              3    IN_VPR          vprex_t                     Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vtstfillb_v32_c32_v32_p (vIn, vcoefIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vtstfillb_v32_c32_v32_p version.


Main table → Bit Manipulation → Test and Fill → Vector Test and Fill Bytes
