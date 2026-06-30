# Load Configuration Fields → Overflow Mode Bits → Vector Sticky

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Load Configuration Fields → Overflow Mode Bits → Vector Sticky
Overflow Flag for VA unit

Vector Sticky Overflow Flag for VA unit

Vector Sticky Overflow Flag for VA unit
Sets the Vector Sticky Overflow Flag for VA unit bit field.
Available Switches
None
Intrinsic Names
vlbf_uimm1_vova
lbfv_uimm1_vova
Instruction details in the instruction set specification
Intrinsic     vlbf_uimm1_vova[_p]
name
Spec syntax   vlbf #uimm1, vova, ?vprX

Return type   void

              1      IN1_UIMM1    uint8     0..1     1 bit unsigned immediate
Operands

2      IN_VPR       vprex_t            Vector predicate operand
              vprex_t vecPred;
C example     ...
              vlbf_uimm1_vova_p(2, vecPred);

Comments      1.     IN_VPR last operand is relevant only for vlbf_uimm1_vova_p version.


Main table → Load Configuration Fields → Overflow Mode Bits → Vector Sticky
Overflow Flag for VA unit
Intrinsic     lbfv_uimm1_vova
name
Spec syntax   lbfv #uimm1, vova

Return type   void

Operands      1      IN1_UIMM1      uint8   0..1   1 bit unsigned immediate
              ...
C example     lbfv_uimm1_vova(2);

Comments


Main table → Load Configuration Fields → Overflow Mode Bits → Vector Sticky
Overflow Flag for VA unit

Main table → Load Configuration Fields → Overflow Mode Bits → Vector Sticky
Overflow Flag for VB unit

Vector Sticky Overflow Flag for VB unit

Vector Sticky Overflow Flag for VB unit
Sets the Vector Sticky Overflow Flag for VB unit bit field.
Available Switches
None
Intrinsic Names
lbfv_uimm1_vovb
vlbf_uimm1_vovb
Instruction details in the instruction set specification
Intrinsic     lbfv_uimm1_vovb
name
Spec syntax   lbfv #uimm1, vovb

Return type   void

Operands      1      IN1_UIMM1      uint8   0..1   1 bit unsigned immediate
              ...
C example     lbfv_uimm1_vovb(2);

Comments


Main table → Load Configuration Fields → Overflow Mode Bits → Vector Sticky
Overflow Flag for VB unit
Intrinsic     vlbf_uimm1_vovb[_p]
name
Spec syntax   vlbf #uimm1, vovb, ?vprX

Return type   void

              1      IN1_UIMM1    uint8     0..1     1 bit unsigned immediate
Operands
              2      IN_VPR       vprex_t            Vector predicate operand
              vprex_t vecPred;
C example     ...
              vlbf_uimm1_vovb_p(2, vecPred);

Comments      1.     IN_VPR last operand is relevant only for vlbf_uimm1_vovb_p version.


Main table → Load Configuration Fields → Overflow Mode Bits → Vector Sticky
Overflow Flag for VB unit
