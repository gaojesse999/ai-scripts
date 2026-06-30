# Load Configuration Fields → Rounding Mode Bits → Vector Automatic

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Load Configuration Fields → Rounding Mode Bits → Vector Automatic
Rounding

Vector Automatic Rounding

Vector Automatic Rounding
Sets the Vector Automatic Rounding bit field.
Available Switches
None
Intrinsic Names
vlbf_uimm1_vrnda
lbfv_uimm1_vrnda
Instruction details in the instruction set specification
Intrinsic     vlbf_uimm1_vrnda[_p]
name
Spec syntax   vlbf #uimm1, vrnda, ?vprX

Return type   void

              1      IN1_UIMM1    uint8     0..1      1 bit unsigned immediate
Operands
              2      IN_VPR       vprex_t             Vector predicate operand
              vprex_t vecPred;
C example     ...
              vlbf_uimm1_vrnda_p(2, vecPred);

Comments      1.     IN_VPR last operand is relevant only for vlbf_uimm1_vrnda_p version.


Main table → Load Configuration Fields → Rounding Mode Bits → Vector Automatic
Rounding
Intrinsic     lbfv_uimm1_vrnda
name
Spec syntax   lbfv #uimm1, vrnda

Return type   void

Operands      1      IN1_UIMM1       uint8   0..1   1 bit unsigned immediate
              ...
C example     lbfv_uimm1_vrnda(2);

Comments

Main table → Load Configuration Fields → Rounding Mode Bits → Vector Automatic
Rounding
