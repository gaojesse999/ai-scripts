# Load Configuration Fields → Saturation Mode Bits → Vector Double Word

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Load Configuration Fields → Saturation Mode Bits → Vector Double Word
Saturation and Store Pre-Shift

Vector Double Word Saturation and Store Pre-Shift

Vector Double Word Saturation and Store Pre-Shift
Sets the Vector Double Word Saturation and Store Pre-Shift bit field.
Available Switches
None
Intrinsic Names
lbfv_uimm3_vstdwset
vlbf_uimm3_vstdwset
Instruction details in the instruction set specification
Intrinsic     lbfv_uimm3_vstdwset
name
Spec syntax   lbfv #uimm3, vstdwset

Return type   void

Operands      1      IN1_UIMM3    uint8   0..7   3 bit unsigned immediate
              ...
C example     lbfv_uimm3_vstdwset(2);

Comments


Main table → Load Configuration Fields → Saturation Mode Bits → Vector Double Word
Saturation and Store Pre-Shift
Intrinsic     vlbf_uimm3_vstdwset[_p]
name
Spec syntax   vlbf #uimm3, vstdwset, ?vprX

Return type   void

              1      IN1_UIMM3    uint8     0..7      3 bit unsigned immediate
Operands
              2      IN_VPR       vprex_t             Vector predicate operand
              vprex_t vecPred;
C example     ...
              vlbf_uimm3_vstdwset_p(2, vecPred);

Comments      1.     IN_VPR last operand is relevant only for vlbf_uimm3_vstdwset_p version.


Main table → Load Configuration Fields → Saturation Mode Bits → Vector Double Word
Saturation and Store Pre-Shift
