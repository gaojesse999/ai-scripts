# Bit Manipulation → Copy → Vector Copy

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Bit Manipulation → Copy → Vector Copy

Vector Copy

Vector Copy
Performs copy of 16-bits source input into a vector predicate register.
Available Switches
None
Intrinsic Names
vcopy_imm16_8_vpr
vcopy_v32_vpr
Instruction details in the instruction set specification
Intrinsic     vcopy_imm16_8_vpr[_p]
name
Spec syntax   vcopy #imm16_8, VPREX, ?vprX

Return type   vprex_t

              1    IN1_IMM16_8 int16        -32768..32767   16 bit immediate
Operands
              2    IN_VPR         vprex_t                   Vector predicate operand
              vprex_t vecPred;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vcopy_imm16_8_vpr_p (2, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vcopy_imm16_8_vpr_p version.


Main table → Bit Manipulation → Copy → Vector Copy
Intrinsic     vcopy_v32_vpr[_p]
name
Spec syntax   vcopy vx[0], VPREX, ?vprX

Return type   vprex_t

              1    IN1_V32        vec_t                      Input vector operand
Operands
              2    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vprex_t vecPred;

C example     vprex_t vecPredRes;
              ...
              vecPredRes = vcopy_v32_vpr_p (vIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vcopy_v32_vpr_p version.


Main table → Bit Manipulation → Copy → Vector Copy
