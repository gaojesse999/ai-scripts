# Load Configuration Fields → Rounding Mode Bits → Vector Long Double-

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Load Configuration Fields → Rounding Mode Bits → Vector Long Double-
Word Multiplication Product Rounding - Rounding Constant Shift Value

Vector Long Double-Word Multiplication Product Rounding - Rounding Constant Shift
Value

Vector Long Double-Word Multiplication Product Rounding - Rounding Constant Shift
Value
Sets the Rounding Constant Shift Value for Vector Long Double-Word Multiplication Product
Rounding.
Available Switches
None
Intrinsic Names
vlbf_uimm6_vrndxl
lbfv_uimm6_vrndxl
Instruction details in the instruction set specification
Intrinsic     vlbf_uimm6_vrndxl[_p]
name
Spec syntax   vlbf #uimm6, vrndxl, ?vprX

Return type   void

              1      IN1_UIMM6    uint8     0..63     6 bit unsigned immediate
Operands
              2      IN_VPR       vprex_t             Vector predicate operand
              vprex_t vecPred;
C example     ...
              vlbf_uimm6_vrndxl_p(2, vecPred);

Comments      1.     IN_VPR last operand is relevant only for vlbf_uimm6_vrndxl_p version.


Main table → Load Configuration Fields → Rounding Mode Bits → Vector Long Double-
Word Multiplication Product Rounding - Rounding Constant Shift Value
Intrinsic     lbfv_uimm6_vrndxl
name
Spec syntax   lbfv #uimm6, vrndxl

Return type   void

Operands      1      IN1_UIMM6    uint8   0..63   6 bit unsigned immediate
              ...
C example     lbfv_uimm6_vrndxl(2);

Comments


Main table → Load Configuration Fields → Rounding Mode Bits → Vector Long Double-
Word Multiplication Product Rounding - Rounding Constant Shift Value

Main table → Load Configuration Fields → Rounding Mode Bits → Vector Long Double-
Word Multiplication Product Rounding - Rounding Set

Vector Long Double-Word Multiplication Product Rounding - Rounding Set

Vector Long Double-Word Multiplication Product Rounding - Rounding Set
Sets the Rounding Set bits for Vector Long Double-Word Multiplication Product Rounding.
Available Switches
None
Intrinsic Names
vlbf_uimm7_vrndlset
lbfv_uimm7_vrndlset

Instruction details in the instruction set specification
Intrinsic     vlbf_uimm7_vrndlset[_p]
name
Spec syntax   vlbf #uimm7, vrndlset, ?vprX

Return type   void

              1      IN1_UIMM7     uint8     0..127   7 bit unsigned immediate
Operands
              2      IN_VPR        vprex_t            Vector predicate operand
              vprex_t vecPred;
C example     ...
              vlbf_uimm7_vrndlset_p(2, vecPred);

Comments      1.     IN_VPR last operand is relevant only for vlbf_uimm7_vrndlset_p version.


Main table → Load Configuration Fields → Rounding Mode Bits → Vector Long Double-
Word Multiplication Product Rounding - Rounding Set
Intrinsic     lbfv_uimm7_vrndlset
name
Spec syntax   lbfv #uimm7, vrndlset

Return type   void

Operands      1      IN1_UIMM7    uint8   0..127   7 bit unsigned immediate
              ...
C example     lbfv_uimm7_vrndlset(2);

Comments


Main table → Load Configuration Fields → Rounding Mode Bits → Vector Long Double-
Word Multiplication Product Rounding - Rounding Set

Main table → Load Configuration Fields → Rounding Mode Bits → Vector Long Double-
Word Multiplication Product Rounding - Valid Bit

Vector Long Double-Word Multiplication Product Rounding - Valid Bit

Vector Long Double-Word Multiplication Product Rounding - Valid Bit
Sets the valid bit for Vector Long Double-Word Multiplication Product Rounding.
Available Switches
None
Intrinsic Names
vlbf_uimm1_vrndlv
lbfv_uimm1_vrndlv
Instruction details in the instruction set specification
Intrinsic     vlbf_uimm1_vrndlv[_p]
name
Spec syntax   vlbf #uimm1, vrndlv, ?vprX

Return type   void

              1      IN1_UIMM1    uint8     0..1      1 bit unsigned immediate
Operands
              2      IN_VPR       vprex_t             Vector predicate operand
              vprex_t vecPred;
C example     ...
              vlbf_uimm1_vrndlv_p(2, vecPred);

Comments      1.     IN_VPR last operand is relevant only for vlbf_uimm1_vrndlv_p version.


Main table → Load Configuration Fields → Rounding Mode Bits → Vector Long Double-
Word Multiplication Product Rounding - Valid Bit
Intrinsic     lbfv_uimm1_vrndlv
name
Spec syntax   lbfv #uimm1, vrndlv

Return type   void

Operands      1      IN1_UIMM1    uint8   0..1   1 bit unsigned immediate
              ...
C example     lbfv_uimm1_vrndlv(2);

Comments


Main table → Load Configuration Fields → Rounding Mode Bits → Vector Long Double-
Word Multiplication Product Rounding - Valid Bit
