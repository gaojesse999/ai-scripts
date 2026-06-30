# Load Configuration Fields → Floating Point Mode Bits → Vector Masking

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Load Configuration Fields → Floating Point Mode Bits → Vector Masking
Bits for Inexact Floating Point Results

Vector Masking Bits for Inexact Floating Point Results

Vector Masking Bits for Inexact Floating Point Results
Sets the Vector Masking Bits for Inexact Floating Point Results bit field.
Available Switches
None
Intrinsic Names
lbfv_uimm2_vflpmask
vlbf_uimm2_vflpmask
Instruction details in the instruction set specification
Intrinsic     lbfv_uimm2_vflpmask
name
Spec syntax   lbfv #uimm2, vflpmask

Return type   void

Operands      1      IN1_UIMM2   uint8   0..3   2 bit unsigned immediate
              ...
C example     lbfv_uimm2_vflpmask(2);

Comments


Main table → Load Configuration Fields → Floating Point Mode Bits → Vector Masking
Bits for Inexact Floating Point Results
Intrinsic     vlbf_uimm2_vflpmask[_p]
name
Spec syntax   vlbf #uimm2, vflpmask, ?vprX

Return type   void

              1      IN1_UIMM2    uint8     0..3     2 bit unsigned immediate
Operands

2      IN_VPR       vprex_t            Vector predicate operand
              vprex_t vecPred;
C example     ...
              vlbf_uimm2_vflpmask_p(2, vecPred);

Comments      1.     IN_VPR last operand is relevant only for vlbf_uimm2_vflpmask_p version.


Main table → Load Configuration Fields → Floating Point Mode Bits → Vector Masking
Bits for Inexact Floating Point Results
