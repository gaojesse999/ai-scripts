# Memory Access → Load → Load predicate

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Memory Access → Load → Load predicate

Load predicate

Load predicate
Load predicate register
Available Switches
2dw        Load two double words
int2dw When used 2dw are interleaved. The default is 4dw are interleaved.
mdw        Number of double-word loads. 1dw ≤ mdw ≤ 8dw
ndw        Number of double-word loads. 1dw ≤ ndw ≤ 4dw
           When row stride mechanism enabled - the row stride values are taken from ROWSTR0
rowstr
           or ROWSTR1 located under mod4 mode register under the following conditions:
strX       Selects the STR, PMSTR set within mod1 register and ROWSTR at mod4 register.
u          When using vozZ as destination, each vozZ which is written is zero-extended instead of
           The load operation ignores the mode-bits behavior on the vector load operation (i.e. the
vspill
           stride0/1, pmstr0/1, rowstr0/1 mode-bits are ignored - the stride is 8dw by default)
vuX        Determines the destination VCU of the instruction. X is replaced by 0 or 1.
Intrinsic Names
vlddw_vpr_dw
vlddw_vpr_clone_dw
vlddw_vpr_dw_vuX
Instruction details in the instruction set specification
Available addressing modes
Intrinsic Names:
vlddw_direct_vpr_dw
vlddw_indexed_imm_vpr_dw
vlddw_indexed_rI_pm_imm_vpr_dw
vlddw_indexed_rI_pm_ptr_vpr_dw
vlddw_indexed_rI_vpr_dw
vlddw_indexed_rIp_pm_imm_vpr_dw
vlddw_indexed_rIp_pm_ptr_vpr_dw
vlddw_indexed_rIp_vpr_dw
vlddw_pm_imm_vpr_dw
vlddw_pm_ptr_vpr_dw
vlddw_vpr_dw
Intrinsic     vlddw_direct_vpr_dw
name
Spec syntax   vlddw {dw [,strX]} [#address],VPREX [,?prSC]

Return type   vprex_t
                                               32

Operands      1    IN1_ADDR       int32     0..2 -1         32 bit address
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vlddw_direct_vpr_dw (2);

Comments



Intrinsic     vlddw_indexed_imm_vpr_dw
name
Spec syntax   vlddw {dw [,strX]} (gB+#imm16_6), VPREX [,?prSC]

Return type   vprex_t

              1   IN1_gB_BASE void *                        Pointer register (gB)
Operands                                                    16 bit immediate post modification in
              2   IN2_IMM16_6      int16    -32768..32767
                                                            bytes
              void* ptrBase;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vlddw_indexed_imm_vpr_dw (ptrBase, 2);

Comments



Intrinsic     vlddw_indexed_rI_pm_imm_vpr_dw
name
Spec syntax   vlddw {dw [,strX]} (gB+rI)[+pm],VPREX [,?prSC]

Return type   vprex_t

              1   IN1_gB_BASE      void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
Operands                                                    base pointer
                                              31    31      32 bit immediate post modification in
              3   IN3_PM_IMM       int32    -2 ..2 -1
                                                            bytes
              void* ptrBase;
              void* ptrModify;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vlddw_indexed_rI_pm_imm_vpr_dw (ptrBase, ptrModify, 2);
Comments



Intrinsic     vlddw_indexed_rI_pm_ptr_vpr_dw
name
Spec syntax   vlddw {dw [,strX]} (gB+rI)[+pm],VPREX [,?prSC]

Return type   vprex_t

              1   IN1_gB_BASE       void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
Operands      2   IN2_rI_OFFSET void *
                                                             base pointer
              3   IN3_PM_PTR        void*                    Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vlddw_indexed_rI_pm_ptr_vpr_dw (ptrBase, ptrModify, ptr);

Comments



Intrinsic     vlddw_indexed_rI_vpr_dw
name

Spec syntax   vlddw {dw [,strX]} (gB+rI)[+pm],VPREX [,?prSC]

Return type   vprex_t

              1   IN1_gB_BASE       void *                   Pointer register (gB)
Operands                                                     Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
                                                             base pointer
              void* ptrBase;
              void* ptrModify;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vlddw_indexed_rI_vpr_dw (ptrBase, ptrModify);

Comments



Intrinsic     vlddw_indexed_rIp_pm_imm_vpr_dw
name
Spec syntax   vlddw {dw [,strX]} (gB+rIp)[+pm],VPREX [,?prSC]

Return type   vprex_t
              1   IN1_gB_BASE       void *                  Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
                                                            base pointer
Operands
              3   IN2_PART          uint8    LOW,HIGH       Word part which is used for operand 2
                                              31   31       32 bit immediate post modification in
              4   IN3_PM_IMM        int32    -2 ..2 -1
                                                            bytes
              void* ptrBase;
              void* ptrModify;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vlddw_indexed_rIp_pm_imm_vpr_dw (ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic     vlddw_indexed_rIp_pm_ptr_vpr_dw
name
Spec syntax   vlddw {dw [,strX]} (gB+rIp)[+pm],VPREX [,?prSC]

Return type   vprex_t

              1   IN1_gB_BASE       void *                  Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
Operands                                                    base pointer
              3   IN2_PART          uint8    LOW,HIGH       Word part which is used for operand 2
              4   IN3_PM_PTR        void*                   Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vlddw_indexed_rIp_pm_ptr_vpr_dw (ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic     vlddw_indexed_rIp_vpr_dw
name

Spec syntax   vlddw {dw [,strX]} (gB+rIp)[+pm],VPREX [,?prSC]

Return type   vprex_t

              1   IN1_gB_BASE       void *                  Pointer register (gB)
Operands                                                    Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
                                                            base pointer
              3   IN2_PART         uint8     LOW,HIGH        Word part which is used for operand 2
              void* ptrBase;
              void* ptrModify;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vlddw_indexed_rIp_vpr_dw (ptrBase, ptrModify, LOW);

Comments



Intrinsic     vlddw_pm_imm_vpr_dw
name
Spec syntax   vlddw {dw [,strX]} (pN)+#imm32_6,VPREX [,?prSC]

Return type   vprex_t

              1    IN1_PTR        void *                     Pointer register (rN)
Operands                                      31   31        32 bit immediate post modification in
              2    IN2_IMM32_6 int32        -2 ..2 -1
                                                             bytes
              void* ptr;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vlddw_pm_imm_vpr_dw (ptr, 2);

Comments



Intrinsic     vlddw_pm_ptr_vpr_dw
name
Spec syntax   vlddw {dw [,strX]} (pN)[+pm_x], VPREX [,?prSC]

Return type   vprex_t

              1    IN1_PTR        void *                     Pointer register (rN)
Operands
              2    IN2_PM_PTR void*                          Pointer register (rN)
              void* ptr;
              void* vecPredRes;
C example     ...
              ptr = vlddw_pm_ptr_vpr_dw (ptr, vecPredRes);

Comments



Intrinsic     vlddw_vpr_dw
name
Spec syntax   vlddw {dw [,strX]} (pN)[+pm_x], VPREX [,?prSC]

Return type   vprex_t
Operands       1    IN1_PTR        void *         Pointer register (rN)
               void* ptr;
               vprex_t vecPredRes;
C example      ...
               vecPredRes = vlddw_vpr_dw (ptr);

Comments


Main table → Memory Access → Load → Load predicate
Available addressing modes
Intrinsic Names:
vlddw_direct_vpr_clone_dw
vlddw_indexed_imm_vpr_clone_dw
vlddw_indexed_rI_pm_imm_vpr_clone_dw
vlddw_indexed_rI_pm_ptr_vpr_clone_dw
vlddw_indexed_rI_vpr_clone_dw
vlddw_indexed_rIp_pm_imm_vpr_clone_dw
vlddw_indexed_rIp_pm_ptr_vpr_clone_dw
vlddw_indexed_rIp_vpr_clone_dw
vlddw_pm_imm_vpr_clone_dw
vlddw_pm_ptr_vpr_clone_dw
vlddw_vpr_clone_dw

Intrinsic     vlddw_direct_vpr_clone_dw
name          vlddw_direct_vpr_str1_dw

Spec syntax   vlddw {dw [,strX]} [#address],VPREX [,?prSC]

Return type   vprex_t
                                                 32
Operands      1    IN1_ADDR         int32     0..2 -1         32 bit address
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vlddw_direct_vpr_clone_dw (2);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_indexed_imm_vpr_clone_dw
name          vlddw_indexed_imm_vpr_str1_dw

Spec syntax   vlddw {dw [,strX]} (gB+#imm16_6), VPREX [,?prSC]

Return type   vprex_t

              1    IN1_gB_BASE void *                         Pointer register (gB)
Operands                                                      16 bit immediate post modification in
              2    IN2_IMM16_6      int16     -32768..32767
                                                              bytes
              void* ptrBase;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vlddw_indexed_imm_vpr_clone_dw (ptrBase, 2);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_indexed_rI_pm_imm_vpr_clone_dw
name          vlddw_indexed_rI_pm_imm_vpr_str1_dw

Spec syntax   vlddw {dw [,strX]} (gB+rI)[+pm],VPREX [,?prSC]

Return type   vprex_t

              1    IN1_gB_BASE       void *                   Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
Operands                                                      base pointer
                                                31    31      32 bit immediate post modification in
              3    IN3_PM_IMM        int32    -2 ..2 -1
                                                              bytes
              void* ptrBase;
C example     void* ptrModify;
              vprex_t vecPredRes;
              ...
              vecPredRes = vlddw_indexed_rI_pm_imm_vpr_clone_dw (ptrBase, ptrModify, 2);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_indexed_rI_pm_ptr_vpr_clone_dw

name          vlddw_indexed_rI_pm_ptr_vpr_str1_dw

Spec syntax   vlddw {dw [,strX]} (gB+rI)[+pm],VPREX [,?prSC]

Return type   vprex_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
Operands      2    IN2_rI_OFFSET void *
                                                             base pointer
              3    IN3_PM_PTR       void*                    Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vlddw_indexed_rI_pm_ptr_vpr_clone_dw (ptrBase, ptrModify, ptr);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_indexed_rI_vpr_clone_dw
name          vlddw_indexed_rI_vpr_str1_dw

Spec syntax   vlddw {dw [,strX]} (gB+rI)[+pm],VPREX [,?prSC]

Return type   vprex_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
Operands                                                     Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
              void* ptrBase;
              void* ptrModify;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vlddw_indexed_rI_vpr_clone_dw (ptrBase, ptrModify);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).
Intrinsic     vlddw_indexed_rIp_pm_imm_vpr_clone_dw
name          vlddw_indexed_rIp_pm_imm_vpr_str1_dw

Spec syntax   vlddw {dw [,strX]} (gB+rIp)[+pm],VPREX [,?prSC]

Return type   vprex_t

              1    IN1_gB_BASE      void *                  Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                            base pointer
Operands
              3    IN2_PART         uint8    LOW,HIGH       Word part which is used for operand 2
                                              31   31       32 bit immediate post modification in
              4    IN3_PM_IMM       int32    -2 ..2 -1

bytes
              void* ptrBase;
              void* ptrModify;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vlddw_indexed_rIp_pm_imm_vpr_clone_dw (ptrBase, ptrModify, LOW, 2);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_indexed_rIp_pm_ptr_vpr_clone_dw
name          vlddw_indexed_rIp_pm_ptr_vpr_str1_dw

Spec syntax   vlddw {dw [,strX]} (gB+rIp)[+pm],VPREX [,?prSC]

Return type   vprex_t

              1    IN1_gB_BASE      void *                  Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
Operands                                                    base pointer
              3    IN2_PART         uint8    LOW,HIGH       Word part which is used for operand 2
              4    IN3_PM_PTR       void*                   Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vlddw_indexed_rIp_pm_ptr_vpr_clone_dw (ptrBase, ptrModify, LOW, ptr);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_indexed_rIp_vpr_clone_dw
name          vlddw_indexed_rIp_vpr_str1_dw
Spec syntax   vlddw {dw [,strX]} (gB+rIp)[+pm],VPREX [,?prSC]

Return type   vprex_t

              1    IN1_gB_BASE     void *                    Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
Operands      2    IN2_rI_OFFSET void *
                                                             base pointer
              3    IN2_PART        uint8     LOW,HIGH        Word part which is used for operand 2
              void* ptrBase;
              void* ptrModify;
C example     vprex_t vecPredRes;
              ...
              vecPredRes = vlddw_indexed_rIp_vpr_clone_dw (ptrBase, ptrModify, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_pm_imm_vpr_clone_dw
name          vlddw_pm_imm_vpr_str1_dw

Spec syntax   vlddw {dw [,strX]} (pN)+#imm32_6,VPREX [,?prSC]

Return type   vprex_t

1    IN1_PTR        void *                    Pointer register (rN)
Operands                                      31   31       32 bit immediate post modification in
              2    IN2_IMM32_6 int32        -2 ..2 -1
                                                            bytes
              void* ptr;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vlddw_pm_imm_vpr_clone_dw (ptr, 2);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_pm_ptr_vpr_clone_dw
name          vlddw_pm_ptr_vpr_str1_dw

Spec syntax   vlddw {dw [,strX]} (pN)[+pm_x], VPREX [,?prSC]

Return type   vprex_t

              1    IN1_PTR        void *                    Pointer register (rN)
Operands
              2    IN2_PM_PTR void*                         Pointer register (rN)
              void* ptr;
              void* vecPredRes;
C example     ...
              ptr = vlddw_pm_ptr_vpr_clone_dw (ptr, vecPredRes);
                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_vpr_clone_dw
name          vlddw_vpr_str1_dw

Spec syntax   vlddw {dw [,strX]} (pN)[+pm_x], VPREX [,?prSC]

Return type   vprex_t

Operands      1    IN1_PTR        void *                Pointer register (rN)
              void* ptr;
              vprex_t vecPredRes;
C example     ...
              vecPredRes = vlddw_vpr_clone_dw (ptr);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).


Main table → Memory Access → Load → Load predicate
Available addressing modes
Intrinsic Names:
vlddw_pm_imm_vpr_dw_vuX
vlddw_pm_ptr_vpr_dw_vuX
vlddw_vpr_dw_vuX
Intrinsic     vlddw_pm_imm_vpr_dw_vuX
name
Spec syntax   vlddw {dw, vuX} (pN)[+pm_x], VPREX [,?prSC]

Return type   vprex_t

              1    VUX              uint8    0..3           Determines the destination VCU
              2    IN1_PTR          void *                  Pointer register (rN)
Operands
                                               31   31      32 bit immediate post modification in
              3    IN2_PM_IMM int32          -2 ..2 -1
                                                            bytes
              vprex_t 2;
              void* ptr;
C example     ...

2 = vlddw_pm_imm_vpr_dw_vuX (1, ptr, vecPredRes);

Comments



Intrinsic     vlddw_pm_ptr_vpr_dw_vuX
name
Spec syntax   vlddw {dw, vuX} (pN)[+pm_x], VPREX [,?prSC]

Return type   vprex_t

              1    VUX              uint8    0..3           Determines the destination VCU
Operands      2    IN1_PTR          void *                  Pointer register (rN)
              3    IN2_PM_PTR void*                         Pointer register (rN)
              void* ptr;
              void* vecPredRes;
C example     ...
              ptr = vlddw_pm_ptr_vpr_dw_vuX (1, ptr, vecPredRes);

Comments



Intrinsic     vlddw_vpr_dw_vuX
name
Spec syntax   vlddw {dw, vuX} (pN)[+pm_x], VPREX [,?prSC]

Return type   vprex_t

              1    VUX              uint8    0..3           Determines the destination VCU
Operands
              2    IN1_PTR          void *                  Pointer register (rN)
              void* ptr;
C example     vprex_t vecPredRes;
              ...
            vecPredRes = vlddw_vpr_dw_vuX (1, ptr);

Comments


Main table → Memory Access → Load → Load predicate
