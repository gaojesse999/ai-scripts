# Load Configuration Fields → Division Mode Bits → Vector Division Shift

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Load Configuration Fields → Division Mode Bits → Vector Division Shift
Bit

Vector Division Shift Bit

Vector Division Shift Bit
Sets the Vector Division Shift Bit field.
Available Switches
None
Intrinsic Names
vlbf_uimm1_vshfd
lbfv_uimm1_vshfd
vlbf_uimm2_vshfdw
lbfv_uimm2_vshfdw
Instruction details in the instruction set specification
Intrinsic     vlbf_uimm1_vshfd[_p]
name
Spec syntax   vlbf #uimm1, vshfd, ?vprX

Return type   void

              1      IN1_UIMM1    uint8     0..1      1 bit unsigned immediate
Operands
              2      IN_VPR       vprex_t             Vector predicate operand
              vprex_t vecPred;
C example     ...
              vlbf_uimm1_vshfd_p(2, vecPred);

Comments      1.     IN_VPR last operand is relevant only for vlbf_uimm1_vshfd_p version.


Main table → Load Configuration Fields → Division Mode Bits → Vector Division Shift
Bit
Intrinsic     lbfv_uimm1_vshfd
name
Spec syntax   lbfv #uimm1, vshfd

Return type   void

Operands      1      IN1_UIMM1       uint8   0..1   1 bit unsigned immediate
              ...
C example     lbfv_uimm1_vshfd(2);

Comments


Main table → Load Configuration Fields → Division Mode Bits → Vector Division Shift
Bit
Intrinsic     vlbf_uimm2_vshfdw[_p]
name
Spec syntax   vlbf #uimm2, vshfdw, ?vprX

Return type   void

              1      IN1_UIMM2    uint8     0..3     2 bit unsigned immediate
Operands
              2      IN_VPR       vprex_t            Vector predicate operand
              vprex_t vecPred;
C example     ...
              vlbf_uimm2_vshfdw_p(2, vecPred);

Comments      1.     IN_VPR last operand is relevant only for vlbf_uimm2_vshfdw_p version.


Main table → Load Configuration Fields → Division Mode Bits → Vector Division Shift
Bit
Intrinsic     lbfv_uimm2_vshfdw

name
Spec syntax   lbfv #uimm2, vshfdw

Return type   void

Operands      1      IN1_UIMM2   uint8   0..3   2 bit unsigned immediate
              ...
C example     lbfv_uimm2_vshfdw(2);

Comments


Main table → Load Configuration Fields → Division Mode Bits → Vector Division Shift
Bit
