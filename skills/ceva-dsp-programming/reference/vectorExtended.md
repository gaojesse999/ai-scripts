# Load Configuration Fields → Store Pre-Shift Mode Bits → Vector Extended

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Load Configuration Fields → Store Pre-Shift Mode Bits → Vector Extended
Long Saturation and Store Pre-Shift

Vector Extended Long Saturation and Store Pre-Shift

Vector Extended Long Saturation and Store Pre-Shift
Sets the Vector Extended Long Saturation and Store Pre-Shift bit field.
Available Switches
None
Intrinsic Names
vlbf_uimm3_vstlset
lbfv_uimm3_vstlset
Instruction details in the instruction set specification
Intrinsic     vlbf_uimm3_vstlset[_p]
name
Spec syntax   vlbf #uimm3, vstlset, ?vprX

Return type   void

              1      IN1_UIMM3     uint8     0..7     3 bit unsigned immediate
Operands
              2      IN_VPR        vprex_t            Vector predicate operand
              vprex_t vecPred;
C example     ...
              vlbf_uimm3_vstlset_p(2, vecPred);

Comments      1.     IN_VPR last operand is relevant only for vlbf_uimm3_vstlset_p version.


Main table → Load Configuration Fields → Store Pre-Shift Mode Bits → Vector Extended
Long Saturation and Store Pre-Shift

Intrinsic     lbfv_uimm3_vstlset
name
Spec syntax   lbfv #uimm3, vstlset

Return type   void

Operands      1      IN1_UIMM3     uint8   0..7   3 bit unsigned immediate
              ...
C example     lbfv_uimm3_vstlset(2);

Comments


Main table → Load Configuration Fields → Store Pre-Shift Mode Bits → Vector Extended
Long Saturation and Store Pre-Shift

Main table → Load Configuration Fields → Store Pre-Shift Mode Bits → Vector Extended
Long Store Pre-Shift

Vector Extended Long Store Pre-Shift

Vector Extended Long Store Pre-Shift
Sets the Vector Extended Long Store Pre-Shift bit field.
Available Switches
None
Intrinsic Names
lbfv_uimm2_vshfl
vlbf_uimm2_vshfl
Instruction details in the instruction set specification
Intrinsic     lbfv_uimm2_vshfl
name
Spec syntax   lbfv #uimm2, vshfl

Return type   void

Operands      1      IN1_UIMM2       uint8   0..3   2 bit unsigned immediate
              ...
C example     lbfv_uimm2_vshfl(2);

Comments


Main table → Load Configuration Fields → Store Pre-Shift Mode Bits → Vector Extended
Long Store Pre-Shift
Intrinsic     vlbf_uimm2_vshfl[_p]
name
Spec syntax   vlbf #uimm2, vshfl, ?vprX

Return type   void

              1      IN1_UIMM2    uint8     0..3      2 bit unsigned immediate
Operands
              2      IN_VPR       vprex_t             Vector predicate operand
              vprex_t vecPred;
C example     ...
              vlbf_uimm2_vshfl_p(2, vecPred);

Comments      1.     IN_VPR last operand is relevant only for vlbf_uimm2_vshfl_p version.


Main table → Load Configuration Fields → Store Pre-Shift Mode Bits → Vector Extended
Long Store Pre-Shift
