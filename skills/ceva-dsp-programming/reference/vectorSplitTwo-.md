# Load Configuration Fields → Rounding Mode Bits → Vector Split Two-

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Load Configuration Fields → Rounding Mode Bits → Vector Split Two-
Word Multiplication Product Rounding - Rounding Constant Shift Value

Vector Split Two-Word Multiplication Product Rounding - Rounding Constant Shift Value

Vector Split Two-Word Multiplication Product Rounding - Rounding Constant Shift Value
Sets the Rounding Constant Shift Value for Vector Split Two-Word Multiplication Product
Rounding.
Available Switches
None
Intrinsic Names
lbfv_uimm4_vrndx2w
vlbf_uimm4_vrndx2w
Instruction details in the instruction set specification
Intrinsic     lbfv_uimm4_vrndx2w
name
Spec syntax   lbfv #uimm4, vrndx2w

Return type   void

Operands      1      IN1_UIMM4   uint8   0..15   4 bit unsigned immediate
              ...
C example     lbfv_uimm4_vrndx2w(2);

Comments


Main table → Load Configuration Fields → Rounding Mode Bits → Vector Split Two-
Word Multiplication Product Rounding - Rounding Constant Shift Value
Intrinsic     vlbf_uimm4_vrndx2w[_p]
name
Spec syntax   vlbf #uimm4, vrndx2w, ?vprX

Return type   void

              1      IN1_UIMM4    uint8     0..15    4 bit unsigned immediate
Operands
              2      IN_VPR       vprex_t            Vector predicate operand
              vprex_t vecPred;
C example     ...
              vlbf_uimm4_vrndx2w_p(2, vecPred);

Comments      1.     IN_VPR last operand is relevant only for vlbf_uimm4_vrndx2w_p version.


Main table → Load Configuration Fields → Rounding Mode Bits → Vector Split Two-
Word Multiplication Product Rounding - Rounding Constant Shift Value

Main table → Load Configuration Fields → Rounding Mode Bits → Vector Split Two-
Word Multiplication Product Rounding - Rounding Set

Vector Split Two-Word Multiplication Product Rounding - Rounding Set

Vector Split Two-Word Multiplication Product Rounding - Rounding Set
Sets the Rounding Set bits for Vector Split Two-Word Multiplication Product Rounding.
Available Switches
None
Intrinsic Names
lbfv_uimm5_vrndset2w
vlbf_uimm5_vrndset2w
Instruction details in the instruction set specification
Intrinsic     lbfv_uimm5_vrndset2w
name
Spec syntax   lbfv #uimm5, vrndset2w

Return type   void

Operands      1      IN1_UIMM5    uint16   0..31   5 bit unsigned immediate
              ...
C example     lbfv_uimm5_vrndset2w(2);

Comments


Main table → Load Configuration Fields → Rounding Mode Bits → Vector Split Two-
Word Multiplication Product Rounding - Rounding Set
Intrinsic     vlbf_uimm5_vrndset2w[_p]
name

Spec syntax   vlbf #uimm5, vrndset2w, ?vprX

Return type   void

              1      IN1_UIMM5    uint16    0..31    5 bit unsigned immediate
Operands
              2      IN_VPR       vprex_t            Vector predicate operand
              vprex_t vecPred;
C example     ...
              vlbf_uimm5_vrndset2w_p(2, vecPred);

Comments      1.     IN_VPR last operand is relevant only for vlbf_uimm5_vrndset2w_p version.


Main table → Load Configuration Fields → Rounding Mode Bits → Vector Split Two-
Word Multiplication Product Rounding - Rounding Set

Main table → Load Configuration Fields → Rounding Mode Bits → Vector Split Two-
Word Multiplication Product Rounding - Valid Bit

Vector Split Two-Word Multiplication Product Rounding - Valid Bit

Vector Split Two-Word Multiplication Product Rounding - Valid Bit
Sets the valid bit for Vector Split Two-Word Multiplication Product Rounding.
Available Switches
None
Intrinsic Names
vlbf_uimm1_vrndv2w
lbfv_uimm1_vrndv2w
Instruction details in the instruction set specification
Intrinsic     vlbf_uimm1_vrndv2w[_p]
name
Spec syntax   vlbf #uimm1, vrndv2w, ?vprX

Return type   void

              1      IN1_UIMM1    uint8     0..1     1 bit unsigned immediate
Operands
              2      IN_VPR       vprex_t            Vector predicate operand
              vprex_t vecPred;
C example     ...
              vlbf_uimm1_vrndv2w_p(2, vecPred);

Comments      1.     IN_VPR last operand is relevant only for vlbf_uimm1_vrndv2w_p version.


Main table → Load Configuration Fields → Rounding Mode Bits → Vector Split Two-
Word Multiplication Product Rounding - Valid Bit
Intrinsic     lbfv_uimm1_vrndv2w
name
Spec syntax   lbfv #uimm1, vrndv2w

Return type   void

Operands      1      IN1_UIMM1   uint8   0..1   1 bit unsigned immediate
              ...
C example     lbfv_uimm1_vrndv2w(2);

Comments


Main table → Load Configuration Fields → Rounding Mode Bits → Vector Split Two-
Word Multiplication Product Rounding - Valid Bit
