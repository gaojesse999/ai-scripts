# Memory Access → Store → Store extension bits

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Memory Access → Store → Store extension bits

Store extension bits

Store extension bits
Store extension bits
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
vstdw_v40ext_2dw
vstdw_v40ext_2dw_concat
vstdw_v40ext_2dw_vuX
Instruction details in the instruction set specification
Available addressing modes
Intrinsic Names:
vstdw_v40ext_2dw
vstdw_v40ext_direct_2dw
vstdw_v40ext_indexed_imm_2dw
vstdw_v40ext_indexed_rI_2dw
vstdw_v40ext_indexed_rI_pm_imm_2dw
vstdw_v40ext_indexed_rI_pm_ptr_2dw
vstdw_v40ext_indexed_rIp_2dw
vstdw_v40ext_indexed_rIp_pm_imm_2dw
vstdw_v40ext_indexed_rIp_pm_ptr_2dw
vstdw_v40ext_pm_imm_2dw
vstdw_v40ext_pm_ptr_2dw
Intrinsic     vstdw_v40ext_2dw
name
Spec syntax   vstdw {2dw [,concat]} vox[0]e, (pN)[+pm_x] [,?prSC]

Return type   void

              1      IN1_V40       vec40_t                   Output vector operand
Operands
              2      IN2_PTR       void *                    Pointer register (rN)
              void* ptr;
              vec40_t vIn;
C example     ...
              vstdw_v40ext_2dw (vIn, ptr);

Comments



Intrinsic     vstdw_v40ext_direct_2dw
name
Spec syntax   vstdw {2dw [,concat]} vox[0]e, [#address] [,?prSC]

Return type   void

              1      IN1_V40       vec40_t                   Output vector operand
Operands                                          32
              2      IN2_ADDR      int32     0..2 -1         32 bit address
              vec40_t vIn;
C example     ...

vstdw_v40ext_direct_2dw (vIn, 2);

Comments



Intrinsic     vstdw_v40ext_indexed_imm_2dw
name
Spec syntax   vstdw {2dw [,concat]} vox[0]e, (gB+#imm16_6) [,?prSC]

Return type   void

              1      IN1_V40       vec40_t                   Output vector operand
              2      IN2_gB_BASE void *                      Pointer register (gB)
Operands
                                                             16 bit immediate post modification in
              3      IN3_IMM16_6   int16     -32768..32767
                                                             bytes
              void* ptrBase;
              vec40_t vIn;
C example     ...
              vstdw_v40ext_indexed_imm_2dw (vIn, ptrBase, 2);

Comments
Intrinsic     vstdw_v40ext_indexed_rI_2dw
name
Spec syntax   vstdw {2dw [,concat]} vox[0]e, (gB+rI)[+pm] [,?prSC]

Return type   void

              1   IN1_V40           vec40_t                   Output vector operand
              2   IN2_gB_BASE       void *                    Pointer register (gB)
Operands
                                                              Pointer (rI) specifying the offset from the
              3   IN3_rI_OFFSET void *
                                                              base pointer
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;
              ...
              vstdw_v40ext_indexed_rI_2dw (vIn, ptrBase, ptrModify);

Comments



Intrinsic     vstdw_v40ext_indexed_rI_pm_imm_2dw
name
Spec syntax   vstdw {2dw [,concat]} vox[0]e, (gB+rI)[+pm] [,?prSC]

Return type   void

              1   IN1_V40           vec40_t                   Output vector operand
              2   IN2_gB_BASE       void *                    Pointer register (gB)

Operands                                                      Pointer (rI) specifying the offset from the
              3   IN3_rI_OFFSET void *
                                                              base pointer
                                                31   31       32 bit immediate post modification in
              4   IN4_PM_IMM        int32     -2 ..2 -1
                                                              bytes
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;
              ...
              vstdw_v40ext_indexed_rI_pm_imm_2dw (vIn, ptrBase, ptrModify, 2);

Comments



Intrinsic     vstdw_v40ext_indexed_rI_pm_ptr_2dw
name

Spec syntax   vstdw {2dw [,concat]} vox[0]e, (gB+rI)[+pm] [,?prSC]
Return type   void

              1   IN1_V40           vec40_t                   Output vector operand
              2   IN2_gB_BASE       void *                    Pointer register (gB)
Operands                                                      Pointer (rI) specifying the offset from the
              3   IN3_rI_OFFSET void *
                                                              base pointer
              4   IN4_PM_PTR        void*                     Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;
              ...
              vstdw_v40ext_indexed_rI_pm_ptr_2dw (vIn, ptrBase, ptrModify, ptr);

Comments



Intrinsic     vstdw_v40ext_indexed_rIp_2dw
name
Spec syntax   vstdw {2dw [,concat]} vox[0]e, (gB+rIp)[+pm] [,?prSC]

Return type   void

              1   IN1_V40           vec40_t                   Output vector operand
              2   IN2_gB_BASE       void *                    Pointer register (gB)
Operands                                                      Pointer (rI) specifying the offset from the
              3   IN3_rI_OFFSET void *
                                                              base pointer
              4   IN3_PART          uint8     LOW,HIGH        Word part which is used for operand 3
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;
              ...
              vstdw_v40ext_indexed_rIp_2dw (vIn, ptrBase, ptrModify, LOW);

Comments



Intrinsic     vstdw_v40ext_indexed_rIp_pm_imm_2dw
name
Spec syntax   vstdw {2dw [,concat]} vox[0]e, (gB+rIp)[+pm] [,?prSC]

Return type   void

              1   IN1_V40           vec40_t                   Output vector operand
Operands
              2   IN2_gB_BASE       void *                    Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              3   IN3_rI_OFFSET void *
                                                             base pointer
              4   IN3_PART          uint8      LOW,HIGH      Word part which is used for operand 3

              5                                 31    31     32 bit immediate post modification in
                  IN4_PM_IMM        int32      -2 ..2 -1
                                                             bytes
              void* ptrBase;

void* ptrModify;
C example     vec40_t vIn;
              ...
              vstdw_v40ext_indexed_rIp_pm_imm_2dw (vIn, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic     vstdw_v40ext_indexed_rIp_pm_ptr_2dw
name
Spec syntax   vstdw {2dw [,concat]} vox[0]e, (gB+rIp)[+pm] [,?prSC]

Return type   void

              1   IN1_V40           vec40_t                  Output vector operand
              2   IN2_gB_BASE       void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
Operands      3   IN3_rI_OFFSET void *
                                                             base pointer
              4   IN3_PART          uint8      LOW,HIGH      Word part which is used for operand 3
              5   IN4_PM_PTR        void*                    Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;
              ...
              vstdw_v40ext_indexed_rIp_pm_ptr_2dw (vIn, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic     vstdw_v40ext_pm_imm_2dw
name
Spec syntax   vstdw {2dw [,concat]} vox[0]e, (pN)+#imm32_6 [,?prSC]

Return type   void

              1      IN1_V40       vec40_t                   Output vector operand
Operands      2      IN2_PTR       void *                    Pointer register (rN)
                                               31    31
              3      IN3_IMM32_6 int32        -2 ..2 -1      32 bit immediate post modification in
                                                          bytes
              void* ptr;
              vec40_t vIn;
C example     ...
              vstdw_v40ext_pm_imm_2dw (vIn, ptr, 2);

Comments



Intrinsic      vstdw_v40ext_pm_ptr_2dw
name
Spec syntax    vstdw {2dw [,concat]} vox[0]e, (pN)[+pm_x] [,?prSC]

Return type    void

               1      IN1_V40      vec40_t                Output vector operand
Operands       2      IN2_PTR      void *                 Pointer register (rN)
               3      IN3_PM_PTR void*                    Pointer register (rN)
               void* ptr;
               vec40_t vIn;
C example      ...
               vstdw_v40ext_pm_ptr_2dw (vIn, ptr, ptr);

Comments


Main table → Memory Access → Store → Store extension bits
Available addressing modes
Intrinsic Names:
vstdw_v40ext_2dw_concat
vstdw_v40ext_direct_2dw_concat
vstdw_v40ext_indexed_imm_2dw_concat
vstdw_v40ext_indexed_rI_2dw_concat

vstdw_v40ext_indexed_rI_pm_imm_2dw_concat
vstdw_v40ext_indexed_rI_pm_ptr_2dw_concat
vstdw_v40ext_indexed_rIp_2dw_concat
vstdw_v40ext_indexed_rIp_pm_imm_2dw_concat
vstdw_v40ext_indexed_rIp_pm_ptr_2dw_concat
vstdw_v40ext_pm_imm_2dw_concat
vstdw_v40ext_pm_ptr_2dw_concat
Intrinsic     vstdw_v40ext_2dw_concat
name
Spec syntax   vstdw {2dw [,concat]} vox[0]e, (pN)[+pm_x] [,?prSC]

Return type   void

              1      IN1_V40       vec40_t                   Output vector operand
Operands
              2      IN2_PTR       void *                    Pointer register (rN)
              void* ptr;
              vec40_t vIn;
C example     ...
              vstdw_v40ext_2dw_concat (vIn, ptr);

Comments



Intrinsic     vstdw_v40ext_direct_2dw_concat
name
Spec syntax   vstdw {2dw [,concat]} vox[0]e, [#address] [,?prSC]

Return type   void

              1      IN1_V40       vec40_t                   Output vector operand
Operands                                        32
              2      IN2_ADDR      int32     0..2 -1         32 bit address
              vec40_t vIn;
C example     ...
              vstdw_v40ext_direct_2dw_concat (vIn, 2);

Comments



Intrinsic     vstdw_v40ext_indexed_imm_2dw_concat
name
Spec syntax   vstdw {2dw [,concat]} vox[0]e, (gB+#imm16_6) [,?prSC]

Return type   void

              1      IN1_V40       vec40_t                   Output vector operand
              2      IN2_gB_BASE void *                      Pointer register (gB)
Operands
                                                             16 bit immediate post modification in
              3      IN3_IMM16_6   int16     -32768..32767
                                                             bytes
              void* ptrBase;
              vec40_t vIn;
C example     ...
              vstdw_v40ext_indexed_imm_2dw_concat (vIn, ptrBase, 2);

Comments
Intrinsic     vstdw_v40ext_indexed_rI_2dw_concat
name
Spec syntax   vstdw {2dw [,concat]} vox[0]e, (gB+rI)[+pm] [,?prSC]

Return type   void

              1   IN1_V40           vec40_t                   Output vector operand
              2   IN2_gB_BASE       void *                    Pointer register (gB)
Operands
                                                              Pointer (rI) specifying the offset from the
              3   IN3_rI_OFFSET void *
                                                              base pointer
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;

...
              vstdw_v40ext_indexed_rI_2dw_concat (vIn, ptrBase, ptrModify);

Comments



Intrinsic     vstdw_v40ext_indexed_rI_pm_imm_2dw_concat
name
Spec syntax   vstdw {2dw [,concat]} vox[0]e, (gB+rI)[+pm] [,?prSC]

Return type   void

              1   IN1_V40           vec40_t                   Output vector operand
              2   IN2_gB_BASE       void *                    Pointer register (gB)

Operands                                                      Pointer (rI) specifying the offset from the
              3   IN3_rI_OFFSET void *
                                                              base pointer
                                                31   31       32 bit immediate post modification in
              4   IN4_PM_IMM        int32     -2 ..2 -1
                                                              bytes
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;
              ...
              vstdw_v40ext_indexed_rI_pm_imm_2dw_concat (vIn, ptrBase, ptrModify, 2);

Comments



Intrinsic     vstdw_v40ext_indexed_rI_pm_ptr_2dw_concat
name
Spec syntax   vstdw {2dw [,concat]} vox[0]e, (gB+rI)[+pm] [,?prSC]
Return type   void

              1   IN1_V40           vec40_t                   Output vector operand
              2   IN2_gB_BASE       void *                    Pointer register (gB)
Operands                                                      Pointer (rI) specifying the offset from the
              3   IN3_rI_OFFSET void *
                                                              base pointer
              4   IN4_PM_PTR        void*                     Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;
              ...
              vstdw_v40ext_indexed_rI_pm_ptr_2dw_concat (vIn, ptrBase, ptrModify, ptr);

Comments



Intrinsic     vstdw_v40ext_indexed_rIp_2dw_concat
name
Spec syntax   vstdw {2dw [,concat]} vox[0]e, (gB+rIp)[+pm] [,?prSC]

Return type   void

              1   IN1_V40           vec40_t                   Output vector operand
              2   IN2_gB_BASE       void *                    Pointer register (gB)
Operands                                                      Pointer (rI) specifying the offset from the
              3   IN3_rI_OFFSET void *
                                                              base pointer

4   IN3_PART          uint8     LOW,HIGH        Word part which is used for operand 3
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;
              ...
              vstdw_v40ext_indexed_rIp_2dw_concat (vIn, ptrBase, ptrModify, LOW);

Comments



Intrinsic     vstdw_v40ext_indexed_rIp_pm_imm_2dw_concat
name
Spec syntax   vstdw {2dw [,concat]} vox[0]e, (gB+rIp)[+pm] [,?prSC]

Return type   void

              1   IN1_V40           vec40_t                   Output vector operand
Operands
              2   IN2_gB_BASE       void *                    Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              3   IN3_rI_OFFSET void *
                                                             base pointer
              4   IN3_PART          uint8      LOW,HIGH      Word part which is used for operand 3

              5                                 31    31     32 bit immediate post modification in
                  IN4_PM_IMM        int32      -2 ..2 -1
                                                             bytes
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;
              ...
              vstdw_v40ext_indexed_rIp_pm_imm_2dw_concat (vIn, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic     vstdw_v40ext_indexed_rIp_pm_ptr_2dw_concat
name
Spec syntax   vstdw {2dw [,concat]} vox[0]e, (gB+rIp)[+pm] [,?prSC]

Return type   void

              1   IN1_V40           vec40_t                  Output vector operand
              2   IN2_gB_BASE       void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
Operands      3   IN3_rI_OFFSET void *
                                                             base pointer
              4   IN3_PART          uint8      LOW,HIGH      Word part which is used for operand 3
              5   IN4_PM_PTR        void*                    Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;
              ...
              vstdw_v40ext_indexed_rIp_pm_ptr_2dw_concat (vIn, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic     vstdw_v40ext_pm_imm_2dw_concat
name
Spec syntax   vstdw {2dw [,concat]} vox[0]e, (pN)+#imm32_6 [,?prSC]

Return type   void

1      IN1_V40      vec40_t                   Output vector operand
Operands      2      IN2_PTR      void *                    Pointer register (rN)
                                               31    31
              3      IN3_IMM32_6 int32        -2 ..2 -1     32 bit immediate post modification in
                                                                bytes
              void* ptr;
              vec40_t vIn;
C example     ...
              vstdw_v40ext_pm_imm_2dw_concat (vIn, ptr, 2);

Comments



Intrinsic     vstdw_v40ext_pm_ptr_2dw_concat
name
Spec syntax   vstdw {2dw [,concat]} vox[0]e, (pN)[+pm_x] [,?prSC]

Return type   void

              1      IN1_V40      vec40_t                       Output vector operand
Operands      2      IN2_PTR      void *                        Pointer register (rN)
              3      IN3_PM_PTR void*                           Pointer register (rN)
              void* ptr;
              vec40_t vIn;
C example     ...
              vstdw_v40ext_pm_ptr_2dw_concat (vIn, ptr, ptr);

Comments


Main table → Memory Access → Store → Store extension bits
Available addressing modes
Intrinsic Names:
vstdw_v40ext_2dw_vuX
vstdw_v40ext_indexed_rI_2dw_vuX
vstdw_v40ext_indexed_rI_pm_imm_2dw_vuX
vstdw_v40ext_indexed_rI_pm_ptr_2dw_vuX
vstdw_v40ext_indexed_rIp_2dw_vuX
vstdw_v40ext_indexed_rIp_pm_imm_2dw_vuX
vstdw_v40ext_indexed_rIp_pm_ptr_2dw_vuX
vstdw_v40ext_pm_imm_2dw_vuX
vstdw_v40ext_pm_ptr_2dw_vuX
Intrinsic     vstdw_v40ext_2dw_vuX
name
Spec syntax   vstdw {2dw, vuX} vox[0]e, (pN)[+pm_x] [,?prSC]

Return type   void

              1      VUX           uint8      0..3           Determines the source VCU
Operands      2      IN1_V40       vec40_t                   Output vector operand
              3      IN2_PTR       void *                    Pointer register (rN)
              void* ptr;
              vec40_t vIn;
C example     ...
              vstdw_v40ext_2dw_vuX (1, vIn, ptr);

Comments



Intrinsic     vstdw_v40ext_indexed_rI_2dw_vuX
name
Spec syntax   vstdw {2dw, vuX} vox[0]e, (gB+rI)[+pm] [,?prSC]

Return type   void

              1   VUX               uint8      0..3           Determines the source VCU
              2   IN1_V40           vec40_t                   Output vector operand
Operands      3   IN2_gB_BASE       void *                    Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the

4   IN3_rI_OFFSET void *
                                                              base pointer
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;
              ...
              vstdw_v40ext_indexed_rI_2dw_vuX (1, vIn, ptrBase, ptrModify);

Comments



Intrinsic     vstdw_v40ext_indexed_rI_pm_imm_2dw_vuX
name
Spec syntax   vstdw {2dw, vuX} vox[0]e, (gB+rI)[+pm] [,?prSC]

Return type   void

              1   VUX               uint8      0..3           Determines the source VCU
Operands
              2   IN1_V40           vec40_t                   Output vector operand
              3   IN2_gB_BASE       void *                    Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
              4   IN3_rI_OFFSET void *
                                                              base pointer

              5                                 31   31       32 bit immediate post modification in
                  IN4_PM_IMM        int32     -2 ..2 -1
                                                              bytes
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;
              ...
              vstdw_v40ext_indexed_rI_pm_imm_2dw_vuX (1, vIn, ptrBase, ptrModify, 2);

Comments



Intrinsic     vstdw_v40ext_indexed_rI_pm_ptr_2dw_vuX
name
Spec syntax   vstdw {2dw, vuX} vox[0]e, (gB+rI)[+pm] [,?prSC]

Return type   void

              1   VUX               uint8     0..3            Determines the source VCU
              2   IN1_V40           vec40_t                   Output vector operand
              3   IN2_gB_BASE       void *                    Pointer register (gB)
Operands
                                                              Pointer (rI) specifying the offset from the
              4   IN3_rI_OFFSET void *
                                                              base pointer
              5   IN4_PM_PTR        void*                     Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;
              ...
              vstdw_v40ext_indexed_rI_pm_ptr_2dw_vuX (1, vIn, ptrBase, ptrModify, ptr);

Comments



Intrinsic     vstdw_v40ext_indexed_rIp_2dw_vuX
name
Spec syntax   vstdw {2dw, vuX} vox[0]e, (gB+rIp)[+pm] [,?prSC]

Return type   void

1   VUX               uint8     0..3            Determines the source VCU
Operands      2   IN1_V40           vec40_t                   Output vector operand
              3   IN2_gB_BASE       void *                    Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              4   IN3_rI_OFFSET void *
                                                             base pointer
              5   IN3_PART          uint8     LOW,HIGH       Word part which is used for operand 4
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;
              ...
              vstdw_v40ext_indexed_rIp_2dw_vuX (1, vIn, ptrBase, ptrModify, LOW);

Comments



Intrinsic     vstdw_v40ext_indexed_rIp_pm_imm_2dw_vuX
name
Spec syntax   vstdw {2dw, vuX} vox[0]e, (gB+rIp)[+pm] [,?prSC]

Return type   void

              1   VUX               uint8     0..3           Determines the source VCU
              2   IN1_V40           vec40_t                  Output vector operand
              3   IN2_gB_BASE       void *                   Pointer register (gB)

Operands                                                     Pointer (rI) specifying the offset from the
              4   IN3_rI_OFFSET void *
                                                             base pointer
              5   IN3_PART          uint8     LOW,HIGH       Word part which is used for operand 4
                                                31   31      32 bit immediate post modification in
              6   IN4_PM_IMM        int32     -2 ..2 -1
                                                             bytes
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;
              ...
              vstdw_v40ext_indexed_rIp_pm_imm_2dw_vuX (1, vIn, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic     vstdw_v40ext_indexed_rIp_pm_ptr_2dw_vuX
name
Spec syntax   vstdw {2dw, vuX} vox[0]e, (gB+rIp)[+pm] [,?prSC]

Return type   void

              1   VUX               uint8     0..3           Determines the source VCU
Operands      2   IN1_V40           vec40_t                  Output vector operand
              3   IN2_gB_BASE       void *                   Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
              4   IN3_rI_OFFSET void *

base pointer
              5   IN3_PART          uint8    LOW,HIGH         Word part which is used for operand 4
              6   IN4_PM_PTR        void*                     Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;
              ...
              vstdw_v40ext_indexed_rIp_pm_ptr_2dw_vuX (1, vIn, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic     vstdw_v40ext_pm_imm_2dw_vuX
name
Spec syntax   vstdw {2dw, vuX} vox[0]e, (pN)[+pm_x] [,?prSC]

Return type   void

              1      VUX          uint8     0..3              Determines the source VCU
              2      IN1_V40      vec40_t                     Output vector operand
Operands      3      IN2_PTR      void *                      Pointer register (rN)
                                              31   31         32 bit immediate post modification in
              4      IN3_PM_IMM int32       -2 ..2 -1
                                                              bytes
              void* ptr;
              vec40_t vIn;
C example     ...
              vstdw_v40ext_pm_imm_2dw_vuX (1, vIn, ptr, 2);

Comments



Intrinsic     vstdw_v40ext_pm_ptr_2dw_vuX
name
Spec syntax   vstdw {2dw, vuX} vox[0]e, (pN)[+pm_x] [,?prSC]

Return type   void

              1      VUX          uint8     0..3              Determines the source VCU
              2      IN1_V40      vec40_t                     Output vector operand
Operands
              3      IN2_PTR      void *                      Pointer register (rN)
              4      IN3_PM_PTR void*                         Pointer register (rN)
C example     void* ptr;
            vec40_t vIn;
            ...
            vstdw_v40ext_pm_ptr_2dw_vuX (1, vIn, ptr, ptr);

Comments


Main table → Memory Access → Store → Store extension bits
