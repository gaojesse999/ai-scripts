# Memory Access → Store → Store predicate register

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Memory Access → Store → Store predicate register

Store predicate register

Store predicate register
Store predicate register
Available Switches
2dw       Store two double-words
8dw       Store eight double-words
concat Data concatenation
mdw       Number of double-word stores. 1dw ≤ mdw ≤ 8dw
ndw       Number of double-word stores. 1dw ≤ ndw ≤ 4dw
          The store operation ignores the mode-bits behavior on the vector store operation (i.e. the
vspill
          vshfdw, vsatsdw, vshfl and vsatsl mode-bits are ignored - the stride is 8dw by default)

vuX       Determines the source VCU of the instruction. voz[0] ≤ vuX ≤ voz[3]
Intrinsic Names
vstdw_vpr_dw
vstdw_vpr_dw_concat
vstdw_vpr_dw_vuX
Instruction details in the instruction set specification
Available addressing modes
Intrinsic Names:
vstdw_vpr_direct_dw
vstdw_vpr_dw
vstdw_vpr_indexed_imm_dw
vstdw_vpr_indexed_rI_dw
vstdw_vpr_indexed_rI_pm_imm_dw
vstdw_vpr_indexed_rI_pm_ptr_dw
vstdw_vpr_indexed_rIp_dw
vstdw_vpr_indexed_rIp_pm_imm_dw
vstdw_vpr_indexed_rIp_pm_ptr_dw
vstdw_vpr_pm_imm_dw
vstdw_vpr_pm_ptr_dw
Intrinsic     vstdw_vpr_direct_dw
name
Spec syntax   vstdw {dw [,concat]} VPREX, [#address] [,?prSC]

Return type   void

              1      IN1_VPR       vprex_t                      Vector predicate operand
Operands                                          32
              2      IN2_ADDR      int32     0..2 -1            32 bit address
              vprex_t vecPredRes;
C example     ...
              vstdw_vpr_direct_dw (vecPredRes, 2);

Comments



Intrinsic     vstdw_vpr_dw
name
Spec syntax   vstdw {dw [,concat]} VPREX, (pN)[+pm_x] [,?prSC]

Return type   void

              1      IN1_VPR       vprex_t                      Vector predicate operand
Operands
              2      IN2_PTR       void *                       Pointer register (rN)
              void* ptr;
              vprex_t vecPredRes;
C example     ...
              vstdw_vpr_dw (vecPredRes, ptr);

Comments



Intrinsic     vstdw_vpr_indexed_imm_dw
name
Spec syntax   vstdw {dw [,concat]} VPREX, (gB+#imm16_6) [,?prSC]

Return type   void

              1      IN1_VPR       vprex_t                      Vector predicate operand
              2      IN2_gB_BASE void *                         Pointer register (gB)
Operands
                                                                16 bit immediate post modification in
              3      IN3_IMM16_6   int16        -32768..32767
                                                                bytes
              void* ptrBase;
              vprex_t vecPredRes;
C example     ...
              vstdw_vpr_indexed_imm_dw (vecPredRes, ptrBase, 2);

Comments
Intrinsic     vstdw_vpr_indexed_rI_dw
name
Spec syntax   vstdw {dw [,concat]} VPREX, (gB+rI)[+pm] [,?prSC]

Return type   void

              1      IN1_VPR        vprex_t                  Vector predicate operand
              2      IN2_gB_BASE    void *                   Pointer register (gB)
Operands

Pointer (rI) specifying the offset from the
              3      IN3_rI_OFFSET void *
                                                             base pointer
              void* ptrBase;
              void* ptrModify;
C example     vprex_t vecPredRes;
              ...
              vstdw_vpr_indexed_rI_dw (vecPredRes, ptrBase, ptrModify);

Comments



Intrinsic     vstdw_vpr_indexed_rI_pm_imm_dw
name
Spec syntax   vstdw {dw [,concat]} VPREX, (gB+rI)[+pm] [,?prSC]

Return type   void

              1      IN1_VPR        vprex_t                  Vector predicate operand
              2      IN2_gB_BASE    void *                   Pointer register (gB)

Operands                                                     Pointer (rI) specifying the offset from the
              3      IN3_rI_OFFSET void *
                                                             base pointer
                                                31   31      32 bit immediate post modification in
              4      IN4_PM_IMM     int32     -2 ..2 -1
                                                             bytes
              void* ptrBase;
              void* ptrModify;
C example     vprex_t vecPredRes;
              ...
              vstdw_vpr_indexed_rI_pm_imm_dw (vecPredRes, ptrBase, ptrModify, 2);

Comments



Intrinsic     vstdw_vpr_indexed_rI_pm_ptr_dw
name
Spec syntax   vstdw {dw [,concat]} VPREX, (gB+rI)[+pm] [,?prSC]
Return type   void

              1      IN1_VPR        vprex_t                  Vector predicate operand
              2      IN2_gB_BASE    void *                   Pointer register (gB)
Operands                                                     Pointer (rI) specifying the offset from the
              3      IN3_rI_OFFSET void *
                                                             base pointer
              4      IN4_PM_PTR     void*                    Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vprex_t vecPredRes;
              ...
              vstdw_vpr_indexed_rI_pm_ptr_dw (vecPredRes, ptrBase, ptrModify, ptr);

Comments



Intrinsic     vstdw_vpr_indexed_rIp_dw
name
Spec syntax   vstdw {dw [,concat]} VPREX, (gB+rIp)[+pm] [,?prSC]

Return type   void

              1      IN1_VPR        vprex_t                  Vector predicate operand
              2      IN2_gB_BASE    void *                   Pointer register (gB)

Operands                                                     Pointer (rI) specifying the offset from the
              3      IN3_rI_OFFSET void *
                                                             base pointer
              4      IN3_PART       uint8     LOW,HIGH       Word part which is used for operand 3
              void* ptrBase;
              void* ptrModify;
C example     vprex_t vecPredRes;
              ...
              vstdw_vpr_indexed_rIp_dw (vecPredRes, ptrBase, ptrModify, LOW);

Comments



Intrinsic     vstdw_vpr_indexed_rIp_pm_imm_dw
name
Spec syntax   vstdw {dw [,concat]} VPREX, (gB+rIp)[+pm] [,?prSC]

Return type   void

              1      IN1_VPR        vprex_t                  Vector predicate operand
Operands
              2      IN2_gB_BASE    void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              3      IN3_rI_OFFSET void *
                                                             base pointer
              4      IN3_PART       uint8      LOW,HIGH      Word part which is used for operand 3

              5                                  31    31    32 bit immediate post modification in
                     IN4_PM_IMM     int32      -2 ..2 -1
                                                             bytes
              void* ptrBase;
              void* ptrModify;
C example     vprex_t vecPredRes;
              ...
              vstdw_vpr_indexed_rIp_pm_imm_dw (vecPredRes, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic     vstdw_vpr_indexed_rIp_pm_ptr_dw
name
Spec syntax   vstdw {dw [,concat]} VPREX, (gB+rIp)[+pm] [,?prSC]

Return type   void

              1      IN1_VPR        vprex_t                  Vector predicate operand
              2      IN2_gB_BASE    void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
Operands      3      IN3_rI_OFFSET void *
                                                             base pointer
              4      IN3_PART       uint8      LOW,HIGH      Word part which is used for operand 3
              5      IN4_PM_PTR     void*                    Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vprex_t vecPredRes;
              ...

vstdw_vpr_indexed_rIp_pm_ptr_dw (vecPredRes, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic     vstdw_vpr_pm_imm_dw
name
Spec syntax   vstdw {dw [,concat]} VPREX, (pN)+#imm32_6 [,?prSC]

Return type   void

              1      IN1_VPR       vprex_t                  Vector predicate operand
Operands      2      IN2_PTR       void *                   Pointer register (rN)
                                               31     31
              3      IN3_IMM32_6 int32        -2 ..2 -1     32 bit immediate post modification in
                                                             bytes
               void* ptr;
               vprex_t vecPredRes;
C example      ...
               vstdw_vpr_pm_imm_dw (vecPredRes, ptr, 2);

Comments



Intrinsic      vstdw_vpr_pm_ptr_dw
name
Spec syntax    vstdw {dw [,concat]} VPREX, (pN)[+pm_x] [,?prSC]

Return type    void

               1      IN1_VPR      vprex_t                   Vector predicate operand
Operands       2      IN2_PTR      void *                    Pointer register (rN)
               3      IN3_PM_PTR void*                       Pointer register (rN)
               void* ptr;
               vprex_t vecPredRes;
C example      ...
               vstdw_vpr_pm_ptr_dw (vecPredRes, ptr, ptr);

Comments


Main table → Memory Access → Store → Store predicate register
Available addressing modes
Intrinsic Names:
vstdw_vpr_direct_dw_concat
vstdw_vpr_dw_concat
vstdw_vpr_indexed_imm_dw_concat
vstdw_vpr_indexed_rI_dw_concat
vstdw_vpr_indexed_rI_pm_imm_dw_concat
vstdw_vpr_indexed_rI_pm_ptr_dw_concat
vstdw_vpr_indexed_rIp_dw_concat
vstdw_vpr_indexed_rIp_pm_imm_dw_concat
vstdw_vpr_indexed_rIp_pm_ptr_dw_concat
vstdw_vpr_pm_imm_dw_concat
vstdw_vpr_pm_ptr_dw_concat
Intrinsic     vstdw_vpr_direct_dw_concat
name
Spec syntax   vstdw {dw [,concat]} VPREX, [#address] [,?prSC]

Return type   void

              1      IN1_VPR       vprex_t                   Vector predicate operand
Operands                                        32
              2      IN2_ADDR      int32     0..2 -1         32 bit address
              vprex_t vecPredRes;
C example     ...
              vstdw_vpr_direct_dw_concat (vecPredRes, 2);

Comments



Intrinsic     vstdw_vpr_dw_concat
name
Spec syntax   vstdw {dw [,concat]} VPREX, (pN)[+pm_x] [,?prSC]

Return type   void

              1      IN1_VPR       vprex_t                   Vector predicate operand
Operands

2      IN2_PTR       void *                    Pointer register (rN)
              void* ptr;
              vprex_t vecPredRes;
C example     ...
              vstdw_vpr_dw_concat (vecPredRes, ptr);

Comments



Intrinsic     vstdw_vpr_indexed_imm_dw_concat
name
Spec syntax   vstdw {dw [,concat]} VPREX, (gB+#imm16_6) [,?prSC]

Return type   void

              1      IN1_VPR       vprex_t                   Vector predicate operand
              2      IN2_gB_BASE void *                      Pointer register (gB)
Operands
                                                             16 bit immediate post modification in
              3      IN3_IMM16_6   int16     -32768..32767
                                                             bytes
              void* ptrBase;
              vprex_t vecPredRes;
C example     ...
              vstdw_vpr_indexed_imm_dw_concat (vecPredRes, ptrBase, 2);

Comments
Intrinsic     vstdw_vpr_indexed_rI_dw_concat
name
Spec syntax   vstdw {dw [,concat]} VPREX, (gB+rI)[+pm] [,?prSC]

Return type   void

              1      IN1_VPR        vprex_t                  Vector predicate operand
              2      IN2_gB_BASE    void *                   Pointer register (gB)
Operands
                                                             Pointer (rI) specifying the offset from the
              3      IN3_rI_OFFSET void *
                                                             base pointer
              void* ptrBase;
              void* ptrModify;
C example     vprex_t vecPredRes;
              ...
              vstdw_vpr_indexed_rI_dw_concat (vecPredRes, ptrBase, ptrModify);

Comments



Intrinsic     vstdw_vpr_indexed_rI_pm_imm_dw_concat
name
Spec syntax   vstdw {dw [,concat]} VPREX, (gB+rI)[+pm] [,?prSC]

Return type   void

              1      IN1_VPR        vprex_t                  Vector predicate operand
              2      IN2_gB_BASE    void *                   Pointer register (gB)

Operands                                                     Pointer (rI) specifying the offset from the
              3      IN3_rI_OFFSET void *
                                                             base pointer
                                                31   31      32 bit immediate post modification in
              4      IN4_PM_IMM     int32     -2 ..2 -1
                                                             bytes
              void* ptrBase;
              void* ptrModify;

C example     vprex_t vecPredRes;
              ...
              vstdw_vpr_indexed_rI_pm_imm_dw_concat (vecPredRes, ptrBase, ptrModify, 2);

Comments



Intrinsic     vstdw_vpr_indexed_rI_pm_ptr_dw_concat
name
Spec syntax   vstdw {dw [,concat]} VPREX, (gB+rI)[+pm] [,?prSC]
Return type   void

              1      IN1_VPR        vprex_t                  Vector predicate operand
              2      IN2_gB_BASE    void *                   Pointer register (gB)
Operands                                                     Pointer (rI) specifying the offset from the
              3      IN3_rI_OFFSET void *
                                                             base pointer
              4      IN4_PM_PTR     void*                    Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vprex_t vecPredRes;
              ...
              vstdw_vpr_indexed_rI_pm_ptr_dw_concat (vecPredRes, ptrBase, ptrModify, ptr);

Comments



Intrinsic     vstdw_vpr_indexed_rIp_dw_concat
name
Spec syntax   vstdw {dw [,concat]} VPREX, (gB+rIp)[+pm] [,?prSC]

Return type   void

              1      IN1_VPR        vprex_t                  Vector predicate operand
              2      IN2_gB_BASE    void *                   Pointer register (gB)
Operands                                                     Pointer (rI) specifying the offset from the
              3      IN3_rI_OFFSET void *
                                                             base pointer
              4      IN3_PART       uint8     LOW,HIGH       Word part which is used for operand 3
              void* ptrBase;
              void* ptrModify;
C example     vprex_t vecPredRes;
              ...
              vstdw_vpr_indexed_rIp_dw_concat (vecPredRes, ptrBase, ptrModify, LOW);

Comments



Intrinsic     vstdw_vpr_indexed_rIp_pm_imm_dw_concat
name
Spec syntax   vstdw {dw [,concat]} VPREX, (gB+rIp)[+pm] [,?prSC]

Return type   void

              1      IN1_VPR        vprex_t                  Vector predicate operand
Operands
              2      IN2_gB_BASE    void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              3      IN3_rI_OFFSET void *
                                                            base pointer
              4      IN3_PART       uint8      LOW,HIGH     Word part which is used for operand 3

5                                  31    31   32 bit immediate post modification in
                     IN4_PM_IMM     int32      -2 ..2 -1
                                                            bytes
              void* ptrBase;
              void* ptrModify;
C example     vprex_t vecPredRes;
              ...
              vstdw_vpr_indexed_rIp_pm_imm_dw_concat (vecPredRes, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic     vstdw_vpr_indexed_rIp_pm_ptr_dw_concat
name
Spec syntax   vstdw {dw [,concat]} VPREX, (gB+rIp)[+pm] [,?prSC]

Return type   void

              1      IN1_VPR        vprex_t                 Vector predicate operand
              2      IN2_gB_BASE    void *                  Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
Operands      3      IN3_rI_OFFSET void *
                                                            base pointer
              4      IN3_PART       uint8      LOW,HIGH     Word part which is used for operand 3
              5      IN4_PM_PTR     void*                   Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vprex_t vecPredRes;
              ...
              vstdw_vpr_indexed_rIp_pm_ptr_dw_concat (vecPredRes, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic     vstdw_vpr_pm_imm_dw_concat
name
Spec syntax   vstdw {dw [,concat]} VPREX, (pN)+#imm32_6 [,?prSC]

Return type   void

              1      IN1_VPR       vprex_t                  Vector predicate operand
Operands      2      IN2_PTR       void *                   Pointer register (rN)
                                               31     31
              3      IN3_IMM32_6 int32        -2 ..2 -1     32 bit immediate post modification in
                                                            bytes
              void* ptr;
              vprex_t vecPredRes;
C example     ...
              vstdw_vpr_pm_imm_dw_concat (vecPredRes, ptr, 2);

Comments



Intrinsic     vstdw_vpr_pm_ptr_dw_concat
name
Spec syntax   vstdw {dw [,concat]} VPREX, (pN)[+pm_x] [,?prSC]

Return type   void

              1      IN1_VPR      vprex_t                   Vector predicate operand
Operands      2      IN2_PTR      void *                    Pointer register (rN)
              3      IN3_PM_PTR void*                       Pointer register (rN)
              void* ptr;
              vprex_t vecPredRes;

C example     ...
              vstdw_vpr_pm_ptr_dw_concat (vecPredRes, ptr, ptr);

Comments


Main table → Memory Access → Store → Store predicate register
Available addressing modes
Intrinsic Names:
vstdw_vpr_dw_vuX
vstdw_vpr_indexed_rI_dw_vuX
vstdw_vpr_indexed_rI_pm_imm_dw_vuX
vstdw_vpr_indexed_rI_pm_ptr_dw_vuX
vstdw_vpr_indexed_rIp_dw_vuX
vstdw_vpr_indexed_rIp_pm_imm_dw_vuX
vstdw_vpr_indexed_rIp_pm_ptr_dw_vuX
vstdw_vpr_pm_imm_dw_vuX
vstdw_vpr_pm_ptr_dw_vuX
Intrinsic     vstdw_vpr_dw_vuX
name
Spec syntax   vstdw {dw, vuX} VPREX, (pN)[+pm_x] [,?prSC]

Return type   void

              1      VUX           uint8      0..3           Determines the source VCU
Operands      2      IN1_VPR       vprex_t                   Vector predicate operand
              3      IN2_PTR       void *                    Pointer register (rN)
              void* ptr;
              vprex_t vecPredRes;
C example     ...
              vstdw_vpr_dw_vuX (1, vecPredRes, ptr);

Comments



Intrinsic     vstdw_vpr_indexed_rI_dw_vuX
name
Spec syntax   vstdw {dw, vuX} VPREX, (gB+rI)[+pm] [,?prSC]

Return type   void

              1      VUX            uint8      0..3          Determines the source VCU
              2      IN1_VPR        vprex_t                  Vector predicate operand
Operands      3      IN2_gB_BASE    void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              4      IN3_rI_OFFSET void *
                                                             base pointer
              void* ptrBase;
              void* ptrModify;
C example     vprex_t vecPredRes;
              ...
              vstdw_vpr_indexed_rI_dw_vuX (1, vecPredRes, ptrBase, ptrModify);

Comments



Intrinsic     vstdw_vpr_indexed_rI_pm_imm_dw_vuX
name
Spec syntax   vstdw {dw, vuX} VPREX, (gB+rI)[+pm] [,?prSC]

Return type   void

              1      VUX            uint8      0..3          Determines the source VCU
Operands
              2      IN1_VPR        vprex_t                  Vector predicate operand
              3      IN2_gB_BASE    void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              4      IN3_rI_OFFSET void *
                                                             base pointer

5                                 31   31      32 bit immediate post modification in
                     IN4_PM_IMM     int32     -2 ..2 -1
                                                             bytes
              void* ptrBase;
              void* ptrModify;
C example     vprex_t vecPredRes;
              ...
              vstdw_vpr_indexed_rI_pm_imm_dw_vuX (1, vecPredRes, ptrBase, ptrModify, 2);

Comments



Intrinsic     vstdw_vpr_indexed_rI_pm_ptr_dw_vuX
name
Spec syntax   vstdw {dw, vuX} VPREX, (gB+rI)[+pm] [,?prSC]

Return type   void

              1      VUX            uint8     0..3           Determines the source VCU
              2      IN1_VPR        vprex_t                  Vector predicate operand
              3      IN2_gB_BASE    void *                   Pointer register (gB)
Operands
                                                             Pointer (rI) specifying the offset from the
              4      IN3_rI_OFFSET void *
                                                             base pointer
              5      IN4_PM_PTR     void*                    Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vprex_t vecPredRes;
              ...
              vstdw_vpr_indexed_rI_pm_ptr_dw_vuX (1, vecPredRes, ptrBase, ptrModify, ptr);

Comments



Intrinsic     vstdw_vpr_indexed_rIp_dw_vuX
name
Spec syntax   vstdw {dw,vuX} VPREX, (gB+rIp)[+pm] [,?prSC]

Return type   void

              1      VUX            uint8     0..3           Determines the source VCU
Operands      2      IN1_VPR        vprex_t                  Vector predicate operand
              3      IN2_gB_BASE    void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              4      IN3_rI_OFFSET void *
                                                            base pointer
              5      IN3_PART       uint8     LOW,HIGH      Word part which is used for operand 4
              void* ptrBase;
              void* ptrModify;
C example     vprex_t vecPredRes;
              ...
              vstdw_vpr_indexed_rIp_dw_vuX (1, vecPredRes, ptrBase, ptrModify, LOW);

Comments



Intrinsic     vstdw_vpr_indexed_rIp_pm_imm_dw_vuX
name
Spec syntax   vstdw {dw,vuX} VPREX, (gB+rIp)[+pm] [,?prSC]

Return type   void

              1      VUX            uint8     0..3          Determines the source VCU

2      IN1_VPR        vprex_t                 Vector predicate operand
              3      IN2_gB_BASE    void *                  Pointer register (gB)

Operands                                                    Pointer (rI) specifying the offset from the
              4      IN3_rI_OFFSET void *
                                                            base pointer
              5      IN3_PART       uint8     LOW,HIGH      Word part which is used for operand 4
                                                31   31     32 bit immediate post modification in
              6      IN4_PM_IMM     int32     -2 ..2 -1
                                                            bytes
              void* ptrBase;
              void* ptrModify;
C example     vprex_t vecPredRes;
              ...
              vstdw_vpr_indexed_rIp_pm_imm_dw_vuX (1, vecPredRes, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic     vstdw_vpr_indexed_rIp_pm_ptr_dw_vuX
name
Spec syntax   vstdw {dw,vuX} VPREX, (gB+rIp)[+pm] [,?prSC]

Return type   void

              1      VUX            uint8     0..3          Determines the source VCU
Operands      2      IN1_VPR        vprex_t                 Vector predicate operand
              3      IN2_gB_BASE    void *                  Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              4   IN3_rI_OFFSET void *
                                                            base pointer
              5   IN3_PART          uint8    LOW,HIGH       Word part which is used for operand 4
              6   IN4_PM_PTR        void*                   Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vprex_t vecPredRes;
              ...
              vstdw_vpr_indexed_rIp_pm_ptr_dw_vuX (1, vecPredRes, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic     vstdw_vpr_pm_imm_dw_vuX
name
Spec syntax   vstdw {dw, vuX} VPREX, (pN)[+pm_x] [,?prSC]

Return type   void

              1      VUX          uint8     0..3            Determines the source VCU
              2      IN1_VPR      vprex_t                   Vector predicate operand
Operands      3      IN2_PTR      void *                    Pointer register (rN)
                                              31   31       32 bit immediate post modification in
              4      IN3_PM_IMM int32       -2 ..2 -1

bytes
              void* ptr;
              vprex_t vecPredRes;
C example     ...
              vstdw_vpr_pm_imm_dw_vuX (1, vecPredRes, ptr, 2);

Comments



Intrinsic     vstdw_vpr_pm_ptr_dw_vuX
name
Spec syntax   vstdw {dw, vuX} VPREX, (pN)[+pm_x] [,?prSC]

Return type   void

              1      VUX          uint8     0..3            Determines the source VCU
              2      IN1_VPR      vprex_t                   Vector predicate operand
Operands
              3      IN2_PTR      void *                    Pointer register (rN)
              4      IN3_PM_PTR void*                       Pointer register (rN)
C example     void* ptr;
            vprex_t vecPredRes;
            ...
            vstdw_vpr_pm_ptr_dw_vuX (1, vecPredRes, ptr, ptr);

Comments


Main table → Memory Access → Store → Store predicate register
