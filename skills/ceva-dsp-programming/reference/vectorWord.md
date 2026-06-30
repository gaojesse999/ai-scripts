# Load Configuration Fields → Store Pre-Shift Mode Bits → Vector Word

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Load Configuration Fields → Store Pre-Shift Mode Bits → Vector Word
Saturation and Store Pre-Shift

Vector Word Saturation and Store Pre-Shift

Vector Word Saturation and Store Pre-Shift
Sets the Vector Word Saturation and Store Pre-Shift bit field.
Available Switches
None
Intrinsic Names
lbfv_uimm3_vstwset
vlbf_uimm3_vstwset
Instruction details in the instruction set specification
Intrinsic     lbfv_uimm3_vstwset
name
Spec syntax   lbfv #uimm3, vstwset

Return type   void

Operands      1      IN1_UIMM3    uint8   0..7   3 bit unsigned immediate
              ...
C example     lbfv_uimm3_vstwset(2);

Comments


Main table → Load Configuration Fields → Store Pre-Shift Mode Bits → Vector Word
Saturation and Store Pre-Shift
Intrinsic     vlbf_uimm3_vstwset[_p]
name
Spec syntax   vlbf #uimm3, vstwset, ?vprX

Return type   void

1      IN1_UIMM3    uint8     0..7      3 bit unsigned immediate
Operands
              2      IN_VPR       vprex_t             Vector predicate operand
              vprex_t vecPred;
C example     ...
              vlbf_uimm3_vstwset_p(2, vecPred);

Comments      1.     IN_VPR last operand is relevant only for vlbf_uimm3_vstwset_p version.


Main table → Load Configuration Fields → Store Pre-Shift Mode Bits → Vector Word
Saturation and Store Pre-Shift

Main table → Load Configuration Fields → Store Pre-Shift Mode Bits → Vector Word
Store Pre-Shift

Vector Word Store Pre-Shift

Vector Word Store Pre-Shift
Sets the Vector Word Store Pre-Shift bit field.
Available Switches
None
Intrinsic Names
lbfv_uimm2_vshfw
vlbf_uimm2_vshfw
Instruction details in the instruction set specification
Intrinsic     lbfv_uimm2_vshfw
name
Spec syntax   lbfv #uimm2, vshfw

Return type   void

Operands      1      IN1_UIMM2     uint8   0..3   2 bit unsigned immediate
              ...
C example     lbfv_uimm2_vshfw(2);

Comments


Main table → Load Configuration Fields → Store Pre-Shift Mode Bits → Vector Word
Store Pre-Shift
Intrinsic     vlbf_uimm2_vshfw[_p]
name
Spec syntax   vlbf #uimm2, vshfw, ?vprX

Return type   void

              1      IN1_UIMM2    uint8     0..3     2 bit unsigned immediate
Operands
              2      IN_VPR       vprex_t            Vector predicate operand
              vprex_t vecPred;
C example     ...
              vlbf_uimm2_vshfw_p(2, vecPred);

Comments      1.     IN_VPR last operand is relevant only for vlbf_uimm2_vshfw_p version.


Main table → Load Configuration Fields → Store Pre-Shift Mode Bits → Vector Word
Store Pre-Shift
