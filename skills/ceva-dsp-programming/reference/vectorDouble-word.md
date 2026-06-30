# Load Configuration Fields → Rounding Mode Bits → Vector Double-Word

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Load Configuration Fields → Rounding Mode Bits → Vector Double-Word
Multiplication Product Rounding - Rounding Constant Shift Value

Vector Double-Word Multiplication Product Rounding - Rounding Constant Shift Value

Vector Double-Word Multiplication Product Rounding - Rounding Constant Shift Value
Sets the Rounding Constant Shift Value for Vector Double-Word Multiplication Product
Rounding.
Available Switches
None
Intrinsic Names
vlbf_uimm6_vrndxl
vlbf_uimm5_vrndx
lbfv_uimm6_vrndxl
lbfv_uimm5_vrndx
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


Main table → Load Configuration Fields → Rounding Mode Bits → Vector Double-Word
Multiplication Product Rounding - Rounding Constant Shift Value
Intrinsic     vlbf_uimm5_vrndx[_p]
name
Spec syntax   vlbf #uimm5, vrndx, ?vprX

Return type   void

              1      IN1_UIMM5    uint16    0..31    5 bit unsigned immediate
Operands
              2      IN_VPR       vprex_t            Vector predicate operand
              vprex_t vecPred;
C example     ...
              vlbf_uimm5_vrndx_p(2, vecPred);

Comments      1.     IN_VPR last operand is relevant only for vlbf_uimm5_vrndx_p version.


Main table → Load Configuration Fields → Rounding Mode Bits → Vector Double-Word
Multiplication Product Rounding - Rounding Constant Shift Value
Intrinsic     lbfv_uimm6_vrndxl
name
Spec syntax   lbfv #uimm6, vrndxl

Return type   void

Operands      1      IN1_UIMM6    uint8   0..63   6 bit unsigned immediate
              ...
C example     lbfv_uimm6_vrndxl(2);

Comments


Main table → Load Configuration Fields → Rounding Mode Bits → Vector Double-Word
Multiplication Product Rounding - Rounding Constant Shift Value
Intrinsic     lbfv_uimm5_vrndx
name
Spec syntax   lbfv #uimm5, vrndx

Return type   void

Operands      1      IN1_UIMM5     uint16   0..31   5 bit unsigned immediate
              ...
C example     lbfv_uimm5_vrndx(2);

Comments

Main table → Load Configuration Fields → Rounding Mode Bits → Vector Double-Word
Multiplication Product Rounding - Rounding Constant Shift Value

Main table → Load Configuration Fields → Rounding Mode Bits → Vector Double-Word
Multiplication Product Rounding - Rounding Set

Vector Double-Word Multiplication Product Rounding - Rounding Set

Vector Double-Word Multiplication Product Rounding - Rounding Set
Sets the Rounding Set bits for Vector Double-Word Multiplication Product Rounding.
Available Switches
None
Intrinsic Names
vlbf_uimm6_vrndset
lbfv_uimm6_vrndset
Instruction details in the instruction set specification
Intrinsic     vlbf_uimm6_vrndset[_p]
name
Spec syntax   vlbf #uimm6, vrndset, ?vprX

Return type   void

              1      IN1_UIMM6    uint8     0..63     6 bit unsigned immediate
Operands
              2      IN_VPR       vprex_t             Vector predicate operand
              vprex_t vecPred;
C example     ...
              vlbf_uimm6_vrndset_p(2, vecPred);

Comments      1.     IN_VPR last operand is relevant only for vlbf_uimm6_vrndset_p version.


Main table → Load Configuration Fields → Rounding Mode Bits → Vector Double-Word
Multiplication Product Rounding - Rounding Set
Intrinsic     lbfv_uimm6_vrndset
name
Spec syntax   lbfv #uimm6, vrndset

Return type   void

Operands      1      IN1_UIMM6    uint8   0..63   6 bit unsigned immediate
              ...
C example     lbfv_uimm6_vrndset(2);

Comments


Main table → Load Configuration Fields → Rounding Mode Bits → Vector Double-Word
Multiplication Product Rounding - Rounding Set

Main table → Load Configuration Fields → Rounding Mode Bits → Vector Double-Word
Multiplication Product Rounding - Valid Bit

Vector Double-Word Multiplication Product Rounding - Valid Bit

Vector Double-Word Multiplication Product Rounding - Valid Bit
Sets the valid bit for Vector Double-Word Multiplication Product Rounding.
Available Switches
None
Intrinsic Names
lbfv_uimm1_vrndv
vlbf_uimm1_vrndv
Instruction details in the instruction set specification
Intrinsic     lbfv_uimm1_vrndv
name
Spec syntax   lbfv #uimm1, vrndv

Return type   void

Operands      1      IN1_UIMM1     uint8   0..1   1 bit unsigned immediate
              ...
C example     lbfv_uimm1_vrndv(2);

Comments


Main table → Load Configuration Fields → Rounding Mode Bits → Vector Double-Word
Multiplication Product Rounding - Valid Bit
Intrinsic     vlbf_uimm1_vrndv[_p]
name
Spec syntax   vlbf #uimm1, vrndv, ?vprX

Return type   void

1      IN1_UIMM1    uint8     0..1     1 bit unsigned immediate
Operands
              2      IN_VPR       vprex_t            Vector predicate operand
              vprex_t vecPred;
C example     ...
              vlbf_uimm1_vrndv_p(2, vecPred);

Comments      1.     IN_VPR last operand is relevant only for vlbf_uimm1_vrndv_p version.


Main table → Load Configuration Fields → Rounding Mode Bits → Vector Double-Word
Multiplication Product Rounding - Valid Bit
