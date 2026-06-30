# Load Configuration Fields → Saturation Mode Bits → Vector Word/Double-

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Load Configuration Fields → Saturation Mode Bits → Vector Word/Double-
Word Saturation

Vector Word/Double-Word Saturation

Vector Word/Double-Word Saturation
Sets the Vector Word/Double-Word Saturation bit field.
Available Switches
None
Intrinsic Names
lbfv_uimm4_vsatmod
lbfv_uimm4_vsatmode
vlbf_uimm4_vsatmode
vlbf_uimm4_vsatmod
Instruction details in the instruction set specification
Intrinsic     lbfv_uimm4_vsatmod
name
Spec syntax   lbfv #uimm4, vsatmod

Return type   void

Operands      1      IN1_UIMM4   uint8   0..15   4 bit unsigned immediate
              ...
C example     lbfv_uimm4_vsatmod(2);

Comments


Main table → Load Configuration Fields → Saturation Mode Bits → Vector Word/Double-
Word Saturation
Intrinsic     lbfv_uimm4_vsatmode
name
Spec syntax   lbfv #uimm4, vsatmode

Return type   void

Operands      1      IN1_UIMM4   uint8   0..15   4 bit unsigned immediate
              ...
C example     lbfv_uimm4_vsatmode(2);

Comments


Main table → Load Configuration Fields → Saturation Mode Bits → Vector Word/Double-
Word Saturation
Intrinsic     vlbf_uimm4_vsatmode[_p]
name
Spec syntax   vlbf #uimm4, vsatmode, ?vprX

Return type   void

              1      IN1_UIMM4    uint8     0..15    4 bit unsigned immediate
Operands
              2      IN_VPR       vprex_t            Vector predicate operand
              vprex_t vecPred;
C example     ...
              vlbf_uimm4_vsatmode_p(2, vecPred);

Comments      1.     IN_VPR last operand is relevant only for vlbf_uimm4_vsatmode_p version.


Main table → Load Configuration Fields → Saturation Mode Bits → Vector Word/Double-
Word Saturation
Intrinsic     vlbf_uimm4_vsatmod[_p]
name
Spec syntax   vlbf #uimm4, vsatmod, ?vprX

Return type   void

1      IN1_UIMM4    uint8     0..15    4 bit unsigned immediate
Operands
              2      IN_VPR       vprex_t            Vector predicate operand
              vprex_t vecPred;
C example     ...
              vlbf_uimm4_vsatmod_p(2, vecPred);

Comments      1.     IN_VPR last operand is relevant only for vlbf_uimm4_vsatmod_p version.


Main table → Load Configuration Fields → Saturation Mode Bits → Vector Word/Double-
Word Saturation
