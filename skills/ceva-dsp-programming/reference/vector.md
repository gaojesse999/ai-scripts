# Load Configuration Fields → Multiplication Mode Bits → Vector

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Load Configuration Fields → Multiplication Mode Bits → Vector
Multiplication Product Post-Shift (Set 0)

Vector Multiplication Product Post-Shift (Set 0)

Vector Multiplication Product Post-Shift (Set 0)
Sets the Vector Multiplication Product Post-Shift (Set 0) bit field.
Available Switches
None
Intrinsic Names
vlbf_uimm5_vps0
lbfv_uimm5_vps0
Instruction details in the instruction set specification
Intrinsic     vlbf_uimm5_vps0[_p]
name
Spec syntax   vlbf #uimm5, vps0, ?vprX

Return type   void

              1      IN1_UIMM5    uint16       0..31   5 bit unsigned immediate
Operands
              2      IN_VPR       vprex_t              Vector predicate operand
              vprex_t vecPred;
C example     ...
              vlbf_uimm5_vps0_p(2, vecPred);

Comments      1.     IN_VPR last operand is relevant only for vlbf_uimm5_vps0_p version.


Main table → Load Configuration Fields → Multiplication Mode Bits → Vector
Multiplication Product Post-Shift (Set 0)
Intrinsic     lbfv_uimm5_vps0
name
Spec syntax   lbfv #uimm5, vps0

Return type   void

Operands      1      IN1_UIMM5      uint16   0..31   5 bit unsigned immediate
              ...
C example     lbfv_uimm5_vps0(2);

Comments


Main table → Load Configuration Fields → Multiplication Mode Bits → Vector
Multiplication Product Post-Shift (Set 0)

Main table → Load Configuration Fields → Multiplication Mode Bits → Vector
Multiplication Product Post-Shift (Set 1)

Vector Multiplication Product Post-Shift (Set 1)

Vector Multiplication Product Post-Shift (Set 1)
Sets the Vector Multiplication Product Post-Shift (Set 1) bit field.
Available Switches
None
Intrinsic Names
vlbf_uimm5_vps1
lbfv_uimm5_vps1
Instruction details in the instruction set specification
Intrinsic     vlbf_uimm5_vps1[_p]
name
Spec syntax   vlbf #uimm5, vps1, ?vprX

Return type   void

              1      IN1_UIMM5    uint16       0..31   5 bit unsigned immediate
Operands
              2      IN_VPR       vprex_t              Vector predicate operand
              vprex_t vecPred;
C example     ...
              vlbf_uimm5_vps1_p(2, vecPred);

Comments      1.     IN_VPR last operand is relevant only for vlbf_uimm5_vps1_p version.


Main table → Load Configuration Fields → Multiplication Mode Bits → Vector
Multiplication Product Post-Shift (Set 1)
Intrinsic     lbfv_uimm5_vps1
name
Spec syntax   lbfv #uimm5, vps1

Return type   void

Operands      1      IN1_UIMM5      uint16   0..31   5 bit unsigned immediate
              ...
C example     lbfv_uimm5_vps1(2);

Comments


Main table → Load Configuration Fields → Multiplication Mode Bits → Vector
Multiplication Product Post-Shift (Set 1)

Main table → Load Configuration Fields → Multiplication Mode Bits → Vector
Multiplication Product Post-Shift and Sign (Set 0)

Vector Multiplication Product Post-Shift and Sign (Set 0)

Vector Multiplication Product Post-Shift and Sign (Set 0)
Sets the Vector Multiplication Product Post-Shift and Sign (Set 0) bit field.
Available Switches
None
Intrinsic Names
vlbf_uimm7_vmpset0
lbfv_uimm7_vmpset0
Instruction details in the instruction set specification
Intrinsic     vlbf_uimm7_vmpset0[_p]
name
Spec syntax   vlbf #uimm7, vmpset0, ?vprX

Return type   void

              1      IN1_UIMM7    uint8     0..127   7 bit unsigned immediate
Operands
              2      IN_VPR       vprex_t            Vector predicate operand
              vprex_t vecPred;
C example     ...
              vlbf_uimm7_vmpset0_p(2, vecPred);

Comments      1.     IN_VPR last operand is relevant only for vlbf_uimm7_vmpset0_p version.


Main table → Load Configuration Fields → Multiplication Mode Bits → Vector
Multiplication Product Post-Shift and Sign (Set 0)
Intrinsic     lbfv_uimm7_vmpset0
name
Spec syntax   lbfv #uimm7, vmpset0

Return type   void

Operands      1      IN1_UIMM7   uint8   0..127   7 bit unsigned immediate
              ...
C example     lbfv_uimm7_vmpset0(2);

Comments


Main table → Load Configuration Fields → Multiplication Mode Bits → Vector
Multiplication Product Post-Shift and Sign (Set 0)

Main table → Load Configuration Fields → Multiplication Mode Bits → Vector
Multiplication Product Post-Shift and Sign (Set 1)

Vector Multiplication Product Post-Shift and Sign (Set 1)

Vector Multiplication Product Post-Shift and Sign (Set 1)
Sets the Vector Multiplication Product Post-Shift and Sign (Set 1) bit field.
Available Switches
None
Intrinsic Names
vlbf_uimm7_vmpset1
lbfv_uimm7_vmpset1
Instruction details in the instruction set specification
Intrinsic     vlbf_uimm7_vmpset1[_p]
name
Spec syntax   vlbf #uimm7, vmpset1, ?vprX

Return type   void

              1      IN1_UIMM7    uint8     0..127   7 bit unsigned immediate
Operands
              2      IN_VPR       vprex_t            Vector predicate operand
              vprex_t vecPred;
C example     ...
              vlbf_uimm7_vmpset1_p(2, vecPred);

Comments      1.     IN_VPR last operand is relevant only for vlbf_uimm7_vmpset1_p version.


Main table → Load Configuration Fields → Multiplication Mode Bits → Vector
Multiplication Product Post-Shift and Sign (Set 1)
Intrinsic     lbfv_uimm7_vmpset1
name
Spec syntax   lbfv #uimm7, vmpset1

Return type   void

Operands      1      IN1_UIMM7   uint8   0..127   7 bit unsigned immediate
              ...
C example     lbfv_uimm7_vmpset1(2);

Comments


Main table → Load Configuration Fields → Multiplication Mode Bits → Vector
Multiplication Product Post-Shift and Sign (Set 1)

Main table → Load Configuration Fields → Multiplication Mode Bits → Vector
Multiplication Sign (Set 0)

Vector Multiplication Sign (Set 0)

Vector Multiplication Sign (Set 0)
Sets the Vector Multiplication Sign (Set 0) bit field.
Available Switches
None
Intrinsic Names
lbfv_uimm2_vmsn0
vlbf_uimm2_vmsn0
Instruction details in the instruction set specification
Intrinsic     lbfv_uimm2_vmsn0
name
Spec syntax   lbfv #uimm2, vmsn0

Return type   void

Operands      1      IN1_UIMM2   uint8   0..3   2 bit unsigned immediate
              ...
C example     lbfv_uimm2_vmsn0(2);

Comments


Main table → Load Configuration Fields → Multiplication Mode Bits → Vector
Multiplication Sign (Set 0)
Intrinsic     vlbf_uimm2_vmsn0[_p]
name
Spec syntax   vlbf #uimm2, vmsn0, ?vprX

Return type   void

              1      IN1_UIMM2    uint8     0..3     2 bit unsigned immediate
Operands
              2      IN_VPR       vprex_t            Vector predicate operand
              vprex_t vecPred;
C example     ...
              vlbf_uimm2_vmsn0_p(2, vecPred);

Comments      1.     IN_VPR last operand is relevant only for vlbf_uimm2_vmsn0_p version.


Main table → Load Configuration Fields → Multiplication Mode Bits → Vector
Multiplication Sign (Set 0)

Main table → Load Configuration Fields → Multiplication Mode Bits → Vector
Multiplication Sign (Set 1)

Vector Multiplication Sign (Set 1)

Vector Multiplication Sign (Set 1)
Sets the Vector Multiplication Sign (Set 1) bit field.
Available Switches
None
Intrinsic Names
lbfv_uimm2_vmsn1
vlbf_uimm2_vmsn1
Instruction details in the instruction set specification
Intrinsic     lbfv_uimm2_vmsn1
name
Spec syntax   lbfv #uimm2, vmsn1

Return type   void

Operands      1      IN1_UIMM2   uint8   0..3   2 bit unsigned immediate
              ...
C example     lbfv_uimm2_vmsn1(2);

Comments


Main table → Load Configuration Fields → Multiplication Mode Bits → Vector
Multiplication Sign (Set 1)
Intrinsic     vlbf_uimm2_vmsn1[_p]
name
Spec syntax   vlbf #uimm2, vmsn1, ?vprX

Return type   void

              1      IN1_UIMM2    uint8     0..3     2 bit unsigned immediate
Operands
              2      IN_VPR       vprex_t            Vector predicate operand
              vprex_t vecPred;
C example     ...
              vlbf_uimm2_vmsn1_p(2, vecPred);

Comments      1.     IN_VPR last operand is relevant only for vlbf_uimm2_vmsn1_p version.


Main table → Load Configuration Fields → Multiplication Mode Bits → Vector
Multiplication Sign (Set 1)
