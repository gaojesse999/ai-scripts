# Load Configuration Fields → Floating Point Mode Bits → Vector Floating

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Load Configuration Fields → Floating Point Mode Bits → Vector Floating
Point Flags

Vector Floating Point Flags

Vector Floating Point Flags
Sets the Vector Floating Point Flags bit field.
Available Switches
None
Intrinsic Names
lbfv_uimm11_vflpflags
vlbf_uimm11_vflpflags
Instruction details in the instruction set specification
Intrinsic     lbfv_uimm11_vflpflags
name
Spec syntax   lbfv #uimm11, vflpflags

Return type   void

Operands      1      IN1_UIMM11    uint16   0..2047   11 bit unsigned immediate
              ...
C example     lbfv_uimm11_vflpflags(2);

Comments


Main table → Load Configuration Fields → Floating Point Mode Bits → Vector Floating
Point Flags
Intrinsic     vlbf_uimm11_vflpflags[_p]
name
Spec syntax   vlbf #uimm11, vflpflags, ?vprX

Return type   void

              1      IN1_UIMM11    uint16    0..2047   11 bit unsigned immediate
Operands
              2      IN_VPR        vprex_t             Vector predicate operand
              vprex_t vecPred;
C example     ...
              vlbf_uimm11_vflpflags_p(2, vecPred);

Comments      1.     IN_VPR last operand is relevant only for vlbf_uimm11_vflpflags_p version.


Main table → Load Configuration Fields → Floating Point Mode Bits → Vector Floating
Point Flags

Main table → Load Configuration Fields → Floating Point Mode Bits → Vector Floating
Point Rounding

Vector Floating Point Rounding

Vector Floating Point Rounding
Sets the Vector Floating Point Rounding bit field.
Available Switches
None
Intrinsic Names
lbfv_uimm3_vflprnd
vlbf_uimm3_vflprnd
Instruction details in the instruction set specification
Intrinsic     lbfv_uimm3_vflprnd
name
Spec syntax   lbfv #uimm3, vflprnd

Return type   void

Operands      1      IN1_UIMM3    uint8   0..7   3 bit unsigned immediate
              ...
C example     lbfv_uimm3_vflprnd(2);

Comments


Main table → Load Configuration Fields → Floating Point Mode Bits → Vector Floating
Point Rounding
Intrinsic     vlbf_uimm3_vflprnd[_p]
name
Spec syntax   vlbf #uimm3, vflprnd, ?vprX

Return type   void

              1      IN1_UIMM3    uint8     0..7      3 bit unsigned immediate
Operands
              2      IN_VPR       vprex_t             Vector predicate operand
              vprex_t vecPred;
C example     ...
              vlbf_uimm3_vflprnd_p(2, vecPred);

Comments      1.     IN_VPR last operand is relevant only for vlbf_uimm3_vflprnd_p version.


Main table → Load Configuration Fields → Floating Point Mode Bits → Vector Floating
Point Rounding
