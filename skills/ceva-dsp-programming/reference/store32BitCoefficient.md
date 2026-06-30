# Memory Access → Store → Store 32 bit coefficient

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Memory Access → Store → Store 32 bit coefficient

Store 32 bit coefficient

Store 32 bit coefficient
Store 32 bit coefficient
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
vstdw_c32_dw
vstdw_c32_dw_concat
vstdw_c32_2dw
vstdw_c32_2dw_concat
vstdw_c32_2dw_vuX
vstdw_c32_dw_vuX
Instruction details in the instruction set specification
Available addressing modes
Intrinsic Names:
vstdw_c32_direct_dw
vstdw_c32_dw
vstdw_c32_indexed_imm_dw
vstdw_c32_indexed_rI_dw
vstdw_c32_indexed_rI_pm_imm_dw
vstdw_c32_indexed_rI_pm_ptr_dw
vstdw_c32_indexed_rIp_dw
vstdw_c32_indexed_rIp_pm_imm_dw
vstdw_c32_indexed_rIp_pm_ptr_dw
vstdw_c32_pm_imm_dw
vstdw_c32_pm_ptr_dw
Intrinsic     vstdw_c32_direct_dw
name
Spec syntax   vstdw {dw [,concat]} vcX, [#address] [,?prSC]

Return type   void

              1      IN1_C32       coef_t                    Coefficient operand
Operands                                          32

2      IN2_ADDR      int32     0..2 -1         32 bit address
              coef_t vcoefIn;
C example     ...
              vstdw_c32_direct_dw (vcoefIn, 2);

Comments



Intrinsic     vstdw_c32_dw
name
Spec syntax   vstdw {dw [,concat]} vcX, (pN)[+pm_x] [,?prSC]

Return type   void

              1      IN1_C32       coef_t                    Coefficient operand
Operands
              2      IN2_PTR       void *                    Pointer register (rN)
              void* ptr;
              coef_t vcoefIn;
C example     ...
              vstdw_c32_dw (vcoefIn, ptr);

Comments



Intrinsic     vstdw_c32_indexed_imm_dw
name
Spec syntax   vstdw {dw [,concat]} vcX, (gB+#imm16_6) [,?prSC]

Return type   void

              1      IN1_C32        coef_t                   Coefficient operand
              2      IN2_gB_BASE void *                      Pointer register (gB)
Operands
                                                             16 bit immediate post modification in
              3      IN3_IMM16_6    int16    -32768..32767
                                                             bytes
              void* ptrBase;
              coef_t vcoefIn;
C example     ...
              vstdw_c32_indexed_imm_dw (vcoefIn, ptrBase, 2);

Comments
Intrinsic     vstdw_c32_indexed_rI_dw
name
Spec syntax   vstdw {dw [,concat]} vcX, (gB+rI)[+pm] [,?prSC]

Return type   void

              1      IN1_C32        coef_t                    Coefficient operand
              2      IN2_gB_BASE    void *                    Pointer register (gB)
Operands
                                                              Pointer (rI) specifying the offset from the
              3      IN3_rI_OFFSET void *
                                                              base pointer
              void* ptrBase;
              void* ptrModify;
C example     coef_t vcoefIn;
              ...
              vstdw_c32_indexed_rI_dw (vcoefIn, ptrBase, ptrModify);

Comments



Intrinsic     vstdw_c32_indexed_rI_pm_imm_dw
name
Spec syntax   vstdw {dw [,concat]} vcX, (gB+rI)[+pm] [,?prSC]

Return type   void

              1      IN1_C32        coef_t                    Coefficient operand
              2      IN2_gB_BASE    void *                    Pointer register (gB)

Operands                                                      Pointer (rI) specifying the offset from the
              3      IN3_rI_OFFSET void *
                                                              base pointer

31   31       32 bit immediate post modification in
              4      IN4_PM_IMM     int32     -2 ..2 -1
                                                              bytes
              void* ptrBase;
              void* ptrModify;
C example     coef_t vcoefIn;
              ...
              vstdw_c32_indexed_rI_pm_imm_dw (vcoefIn, ptrBase, ptrModify, 2);

Comments



Intrinsic     vstdw_c32_indexed_rI_pm_ptr_dw
name
Spec syntax   vstdw {dw [,concat]} vcX, (gB+rI)[+pm] [,?prSC]
Return type   void

              1      IN1_C32        coef_t                    Coefficient operand
              2      IN2_gB_BASE    void *                    Pointer register (gB)
Operands                                                      Pointer (rI) specifying the offset from the
              3      IN3_rI_OFFSET void *
                                                              base pointer
              4      IN4_PM_PTR     void*                     Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     coef_t vcoefIn;
              ...
              vstdw_c32_indexed_rI_pm_ptr_dw (vcoefIn, ptrBase, ptrModify, ptr);

Comments



Intrinsic     vstdw_c32_indexed_rIp_dw
name
Spec syntax   vstdw {dw [,concat]} vcX, (gB+rIp)[+pm] [,?prSC]

Return type   void

              1      IN1_C32        coef_t                    Coefficient operand
              2      IN2_gB_BASE    void *                    Pointer register (gB)
Operands                                                      Pointer (rI) specifying the offset from the
              3      IN3_rI_OFFSET void *
                                                              base pointer
              4      IN3_PART       uint8     LOW,HIGH        Word part which is used for operand 3
              void* ptrBase;
              void* ptrModify;
C example     coef_t vcoefIn;
              ...
              vstdw_c32_indexed_rIp_dw (vcoefIn, ptrBase, ptrModify, LOW);

Comments



Intrinsic     vstdw_c32_indexed_rIp_pm_imm_dw
name
Spec syntax   vstdw {dw [,concat]} vcX, (gB+rIp)[+pm] [,?prSC]

Return type   void

              1      IN1_C32        coef_t                    Coefficient operand
Operands
              2      IN2_gB_BASE    void *                    Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              3      IN3_rI_OFFSET void *

base pointer
              4      IN3_PART       uint8    LOW,HIGH        Word part which is used for operand 3

              5                                31    31      32 bit immediate post modification in
                     IN4_PM_IMM     int32    -2 ..2 -1
                                                             bytes
              void* ptrBase;
              void* ptrModify;
C example     coef_t vcoefIn;
              ...
              vstdw_c32_indexed_rIp_pm_imm_dw (vcoefIn, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic     vstdw_c32_indexed_rIp_pm_ptr_dw
name
Spec syntax   vstdw {dw [,concat]} vcX, (gB+rIp)[+pm] [,?prSC]

Return type   void

              1      IN1_C32        coef_t                   Coefficient operand
              2      IN2_gB_BASE    void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
Operands      3      IN3_rI_OFFSET void *
                                                             base pointer
              4      IN3_PART       uint8    LOW,HIGH        Word part which is used for operand 3
              5      IN4_PM_PTR     void*                    Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     coef_t vcoefIn;
              ...
              vstdw_c32_indexed_rIp_pm_ptr_dw (vcoefIn, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic     vstdw_c32_pm_imm_dw
name
Spec syntax   vstdw {dw [,concat]} vcX, (pN)+#imm32_6 [,?prSC]

Return type   void

              1      IN1_C32       coef_t                    Coefficient operand
Operands      2      IN2_PTR       void *                    Pointer register (rN)
                                              31    31
              3      IN3_IMM32_6 int32       -2 ..2 -1       32 bit immediate post modification in
                                                         bytes
              void* ptr;
              coef_t vcoefIn;
C example     ...
              vstdw_c32_pm_imm_dw (vcoefIn, ptr, 2);

Comments



Intrinsic     vstdw_c32_pm_ptr_dw
name
Spec syntax   vstdw {dw [,concat]} vcX, (pN)[+pm_x] [,?prSC]

Return type   void

              1      IN1_C32       coef_t                Coefficient operand
Operands      2      IN2_PTR       void *                Pointer register (rN)
              3      IN3_PM_PTR void*                    Pointer register (rN)
              void* ptr;

coef_t vcoefIn;
C example     ...
              vstdw_c32_pm_ptr_dw (vcoefIn, ptr, ptr);

Comments


Main table → Memory Access → Store → Store 32 bit coefficient
Available addressing modes
Intrinsic Names:
vstdw_c32_direct_dw_concat
vstdw_c32_dw_concat
vstdw_c32_indexed_imm_dw_concat
vstdw_c32_indexed_rI_dw_concat
vstdw_c32_indexed_rI_pm_imm_dw_concat
vstdw_c32_indexed_rI_pm_ptr_dw_concat
vstdw_c32_indexed_rIp_dw_concat
vstdw_c32_indexed_rIp_pm_imm_dw_concat
vstdw_c32_indexed_rIp_pm_ptr_dw_concat
vstdw_c32_pm_imm_dw_concat
vstdw_c32_pm_ptr_dw_concat
Intrinsic     vstdw_c32_direct_dw_concat
name
Spec syntax   vstdw {dw [,concat]} vcX, [#address] [,?prSC]

Return type   void

              1      IN1_C32       coef_t                    Coefficient operand
Operands                                        32
              2      IN2_ADDR      int32    0..2 -1          32 bit address
              coef_t vcoefIn;
C example     ...
              vstdw_c32_direct_dw_concat (vcoefIn, 2);

Comments



Intrinsic     vstdw_c32_dw_concat
name
Spec syntax   vstdw {dw [,concat]} vcX, (pN)[+pm_x] [,?prSC]

Return type   void

              1      IN1_C32       coef_t                    Coefficient operand
Operands
              2      IN2_PTR       void *                    Pointer register (rN)
              void* ptr;
              coef_t vcoefIn;
C example     ...
              vstdw_c32_dw_concat (vcoefIn, ptr);

Comments



Intrinsic     vstdw_c32_indexed_imm_dw_concat
name
Spec syntax   vstdw {dw [,concat]} vcX, (gB+#imm16_6) [,?prSC]

Return type   void

              1      IN1_C32       coef_t                    Coefficient operand
              2      IN2_gB_BASE void *                      Pointer register (gB)
Operands
                                                             16 bit immediate post modification in
              3      IN3_IMM16_6   int16     -32768..32767
                                                             bytes
              void* ptrBase;
              coef_t vcoefIn;
C example     ...
              vstdw_c32_indexed_imm_dw_concat (vcoefIn, ptrBase, 2);

Comments
Intrinsic     vstdw_c32_indexed_rI_dw_concat
name
Spec syntax   vstdw {dw [,concat]} vcX, (gB+rI)[+pm] [,?prSC]

Return type   void

              1      IN1_C32        coef_t                    Coefficient operand
              2      IN2_gB_BASE    void *                    Pointer register (gB)
Operands

Pointer (rI) specifying the offset from the
              3      IN3_rI_OFFSET void *
                                                              base pointer
              void* ptrBase;
              void* ptrModify;
C example     coef_t vcoefIn;
              ...
              vstdw_c32_indexed_rI_dw_concat (vcoefIn, ptrBase, ptrModify);

Comments



Intrinsic     vstdw_c32_indexed_rI_pm_imm_dw_concat
name
Spec syntax   vstdw {dw [,concat]} vcX, (gB+rI)[+pm] [,?prSC]

Return type   void

              1      IN1_C32        coef_t                    Coefficient operand
              2      IN2_gB_BASE    void *                    Pointer register (gB)

Operands                                                      Pointer (rI) specifying the offset from the
              3      IN3_rI_OFFSET void *
                                                              base pointer
                                                31   31       32 bit immediate post modification in
              4      IN4_PM_IMM     int32     -2 ..2 -1
                                                              bytes
              void* ptrBase;
              void* ptrModify;
C example     coef_t vcoefIn;
              ...
              vstdw_c32_indexed_rI_pm_imm_dw_concat (vcoefIn, ptrBase, ptrModify, 2);

Comments



Intrinsic     vstdw_c32_indexed_rI_pm_ptr_dw_concat
name
Spec syntax   vstdw {dw [,concat]} vcX, (gB+rI)[+pm] [,?prSC]
Return type   void

              1      IN1_C32        coef_t                    Coefficient operand
              2      IN2_gB_BASE    void *                    Pointer register (gB)
Operands                                                      Pointer (rI) specifying the offset from the
              3      IN3_rI_OFFSET void *
                                                              base pointer
              4      IN4_PM_PTR     void*                     Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     coef_t vcoefIn;
              ...
              vstdw_c32_indexed_rI_pm_ptr_dw_concat (vcoefIn, ptrBase, ptrModify, ptr);

Comments



Intrinsic     vstdw_c32_indexed_rIp_dw_concat
name
Spec syntax   vstdw {dw [,concat]} vcX, (gB+rIp)[+pm] [,?prSC]

Return type   void

              1      IN1_C32        coef_t                    Coefficient operand
              2      IN2_gB_BASE    void *                    Pointer register (gB)

Operands                                                      Pointer (rI) specifying the offset from the
              3      IN3_rI_OFFSET void *
                                                              base pointer
              4      IN3_PART       uint8     LOW,HIGH        Word part which is used for operand 3
              void* ptrBase;
              void* ptrModify;
C example     coef_t vcoefIn;
              ...
              vstdw_c32_indexed_rIp_dw_concat (vcoefIn, ptrBase, ptrModify, LOW);

Comments



Intrinsic     vstdw_c32_indexed_rIp_pm_imm_dw_concat
name
Spec syntax   vstdw {dw [,concat]} vcX, (gB+rIp)[+pm] [,?prSC]

Return type   void

              1      IN1_C32        coef_t                    Coefficient operand
Operands
              2      IN2_gB_BASE    void *                    Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              3      IN3_rI_OFFSET void *
                                                             base pointer
              4      IN3_PART       uint8    LOW,HIGH        Word part which is used for operand 3

              5                                31    31      32 bit immediate post modification in
                     IN4_PM_IMM     int32    -2 ..2 -1
                                                             bytes
              void* ptrBase;
              void* ptrModify;
C example     coef_t vcoefIn;
              ...
              vstdw_c32_indexed_rIp_pm_imm_dw_concat (vcoefIn, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic     vstdw_c32_indexed_rIp_pm_ptr_dw_concat
name
Spec syntax   vstdw {dw [,concat]} vcX, (gB+rIp)[+pm] [,?prSC]

Return type   void

              1      IN1_C32        coef_t                   Coefficient operand
              2      IN2_gB_BASE    void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
Operands      3      IN3_rI_OFFSET void *
                                                             base pointer
              4      IN3_PART       uint8    LOW,HIGH        Word part which is used for operand 3
              5      IN4_PM_PTR     void*                    Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     coef_t vcoefIn;
              ...

vstdw_c32_indexed_rIp_pm_ptr_dw_concat (vcoefIn, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic     vstdw_c32_pm_imm_dw_concat
name
Spec syntax   vstdw {dw [,concat]} vcX, (pN)+#imm32_6 [,?prSC]

Return type   void

              1      IN1_C32       coef_t                   Coefficient operand
Operands      2      IN2_PTR       void *                   Pointer register (rN)
                                              31    31
              3      IN3_IMM32_6 int32       -2 ..2 -1      32 bit immediate post modification in
                                                                bytes
              void* ptr;
              coef_t vcoefIn;
C example     ...
              vstdw_c32_pm_imm_dw_concat (vcoefIn, ptr, 2);

Comments



Intrinsic     vstdw_c32_pm_ptr_dw_concat
name
Spec syntax   vstdw {dw [,concat]} vcX, (pN)[+pm_x] [,?prSC]

Return type   void

              1      IN1_C32      coef_t                        Coefficient operand
Operands      2      IN2_PTR      void *                        Pointer register (rN)
              3      IN3_PM_PTR void*                           Pointer register (rN)
              void* ptr;
              coef_t vcoefIn;
C example     ...
              vstdw_c32_pm_ptr_dw_concat (vcoefIn, ptr, ptr);

Comments


Main table → Memory Access → Store → Store 32 bit coefficient
Available addressing modes
Intrinsic Names:
vstdw_c32_2dw
vstdw_c32_direct_2dw
vstdw_c32_indexed_imm_2dw
vstdw_c32_indexed_rI_2dw
vstdw_c32_indexed_rI_pm_imm_2dw
vstdw_c32_indexed_rI_pm_ptr_2dw
vstdw_c32_indexed_rIp_2dw
vstdw_c32_indexed_rIp_pm_imm_2dw
vstdw_c32_indexed_rIp_pm_ptr_2dw
vstdw_c32_pm_imm_2dw
vstdw_c32_pm_ptr_2dw
Intrinsic     vstdw_c32_2dw
name
Spec syntax   vstdw {2dw [,concat]} vc1X, vc2X, (pN)[+pm_x] [,?prSC]

Return type   void


              1
                                                             Coefficient operand (register vc1 is
                     IN1_VC1       coef_t
                                                             expected)
Operands                                                     Coefficient operand (register vc2 is
              2      IN2_VC2       coef_t
                                                             expected)
              3      IN3_PTR       void *                    Pointer register (rN)
              void* ptr;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              ...
              vstdw_c32_2dw (vcoefIn, vcoefIn2, ptr);

Comments

Intrinsic     vstdw_c32_direct_2dw
name
Spec syntax   vstdw {2dw [,concat]} vc1X, vc2X, [#address] [,?prSC]

Return type   void

                                                             Coefficient operand (register vc1 is
              1      IN1_VC1       coef_t
                                                             expected)
Operands                                                     Coefficient operand (register vc2 is
              2      IN2_VC2       coef_t
                                                             expected)
                                                 32
              3      IN3_ADDR      int32     0..2 -1         32 bit address
              coef_t vcoefIn;
              coef_t vcoefIn2;
C example     ...
              vstdw_c32_direct_2dw (vcoefIn, vcoefIn2, 2);

Comments



Intrinsic     vstdw_c32_indexed_imm_2dw
name
Spec syntax   vstdw {2dw [,concat]} vc1X, vc2X, (gB+#imm16_6) [,?prSC]

Return type   void

                                                             Coefficient operand (register vc1 is
Operands      1      IN1_VC1        coef_t
                                                             expected)
                                                              Coefficient operand (register vc2 is
              2      IN2_VC2        coef_t
                                                              expected)
              3      IN3_gB_BASE void *                       Pointer register (gB)

              4
                                                              16 bit immediate post modification in
                     IN4_IMM16_6    int16     -32768..32767
                                                              bytes
              void* ptrBase;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              ...
              vstdw_c32_indexed_imm_2dw (vcoefIn, vcoefIn2, ptrBase, 2);

Comments



Intrinsic     vstdw_c32_indexed_rI_2dw
name
Spec syntax   vstdw {2dw [,concat]} vc1X, vc2X, (gB+rI)[+pm] [,?prSC]

Return type   void

                                                               Coefficient operand (register vc1 is
              1      IN1_VC1         coef_t
                                                               expected)
                                                               Coefficient operand (register vc2 is
              2      IN2_VC2         coef_t
Operands                                                       expected)

3      IN3_gB_BASE     void *                    Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the
              4      IN4_rI_OFFSET void *
                                                               base pointer
              void* ptrBase;
              void* ptrModify;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              ...
              vstdw_c32_indexed_rI_2dw (vcoefIn, vcoefIn2, ptrBase, ptrModify);

Comments



Intrinsic     vstdw_c32_indexed_rI_pm_imm_2dw
name
Spec syntax   vstdw {2dw [,concat]} vc1X, vc2X, (gB+rI)[+pm] [,?prSC]

Return type   void

                                                               Coefficient operand (register vc1 is
              1      IN1_VC1         coef_t
Operands                                                       expected)
              2      IN2_VC2         coef_t                    Coefficient operand (register vc2 is
                                                               expected)
              3      IN3_gB_BASE     void *                    Pointer register (gB)

              4
                                                               Pointer (rI) specifying the offset from the
                     IN4_rI_OFFSET void *
                                                               base pointer
                                                31   31        32 bit immediate post modification in
              5      IN5_PM_IMM      int32    -2 ..2 -1
                                                               bytes
              void* ptrBase;
              void* ptrModify;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              ...
              vstdw_c32_indexed_rI_pm_imm_2dw (vcoefIn, vcoefIn2, ptrBase, ptrModify, 2);

Comments



Intrinsic     vstdw_c32_indexed_rI_pm_ptr_2dw
name
Spec syntax   vstdw {2dw [,concat]} vc1X, vc2X, (gB+rI)[+pm] [,?prSC]

Return type   void

                                                               Coefficient operand (register vc1 is
              1      IN1_VC1         coef_t
                                                               expected)
                                                               Coefficient operand (register vc2 is
              2      IN2_VC2         coef_t
                                                               expected)

Operands      3      IN3_gB_BASE     void *                    Pointer register (gB)

              4
                                                               Pointer (rI) specifying the offset from the
                     IN4_rI_OFFSET void *
                                                               base pointer
              5      IN5_PM_PTR      void*                     Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     coef_t vcoefIn;
              coef_t vcoefIn2;
              ...
              vstdw_c32_indexed_rI_pm_ptr_2dw (vcoefIn, vcoefIn2, ptrBase, ptrModify, ptr);

Comments



Intrinsic     vstdw_c32_indexed_rIp_2dw
name
Spec syntax   vstdw {2dw [,concat]} vc1X, vc2X, (gB+rIp)[+pm] [,?prSC]
Return type   void

                                                              Coefficient operand (register vc1 is
              1      IN1_VC1        coef_t
                                                              expected)

              2
                                                              Coefficient operand (register vc2 is
                     IN2_VC2        coef_t
                                                              expected)
Operands      3      IN3_gB_BASE    void *                    Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
              4      IN4_rI_OFFSET void *
                                                              base pointer
              5      IN4_PART       uint8    LOW,HIGH         Word part which is used for operand 4
              void* ptrBase;
              void* ptrModify;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              ...
              vstdw_c32_indexed_rIp_2dw (vcoefIn, vcoefIn2, ptrBase, ptrModify, LOW);

Comments



Intrinsic     vstdw_c32_indexed_rIp_pm_imm_2dw
name
Spec syntax   vstdw {2dw [,concat]} vc1X, vc2X, (gB+rIp)[+pm] [,?prSC]

Return type   void

                                                              Coefficient operand (register vc1 is
              1      IN1_VC1        coef_t
                                                              expected)

              2
                                                              Coefficient operand (register vc2 is
                     IN2_VC2        coef_t
                                                              expected)

3      IN3_gB_BASE    void *                    Pointer register (gB)
Operands
              4
                                                              Pointer (rI) specifying the offset from the
                     IN4_rI_OFFSET void *
                                                              base pointer
              5      IN4_PART       uint8    LOW,HIGH         Word part which is used for operand 4
                                               31   31        32 bit immediate post modification in
              6      IN5_PM_IMM     int32    -2 ..2 -1
                                                              bytes
              void* ptrBase;
              void* ptrModify;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              ...
              vstdw_c32_indexed_rIp_pm_imm_2dw (vcoefIn, vcoefIn2, ptrBase, ptrModify, LOW, 2);

Comments
Intrinsic     vstdw_c32_indexed_rIp_pm_ptr_2dw
name
Spec syntax   vstdw {2dw [,concat]} vc1X, vc2X, (gB+rIp)[+pm] [,?prSC]

Return type   void


              1
                                                              Coefficient operand (register vc1 is
                     IN1_VC1        coef_t
                                                              expected)
                                                              Coefficient operand (register vc2 is
              2      IN2_VC2        coef_t
                                                              expected)

Operands      3      IN3_gB_BASE    void *                    Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
              4      IN4_rI_OFFSET void *
                                                              base pointer
              5      IN4_PART       uint8    LOW,HIGH         Word part which is used for operand 4
              6      IN5_PM_PTR     void*                     Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     coef_t vcoefIn;
              coef_t vcoefIn2;
              ...
              vstdw_c32_indexed_rIp_pm_ptr_2dw (vcoefIn, vcoefIn2, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic     vstdw_c32_pm_imm_2dw
name
Spec syntax   vstdw {2dw [,concat]} vc1X, vc2X, (pN)+#imm32_6 [,?prSC]

Return type   void


              1
                                                             Coefficient operand (register vc1 is

IN1_VC1       coef_t
                                                             expected)
                                                             Coefficient operand (register vc2 is
              2      IN2_VC2       coef_t
Operands                                                     expected)
              3      IN3_PTR       void *                    Pointer register (rN)
                                               31   31       32 bit immediate post modification in
              4      IN4_IMM32_6 int32       -2 ..2 -1
                                                             bytes
              void* ptr;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              ...
              vstdw_c32_pm_imm_2dw (vcoefIn, vcoefIn2, ptr, 2);

Comments



Intrinsic     vstdw_c32_pm_ptr_2dw
name
Spec syntax   vstdw {2dw [,concat]} vc1X, vc2X, (pN)[+pm_x] [,?prSC]

Return type   void


              1
                                                              Coefficient operand (register vc1 is
                     IN1_VC1       coef_t
                                                              expected)
                                                              Coefficient operand (register vc2 is
              2      IN2_VC2       coef_t
Operands                                                      expected)
              3      IN3_PTR       void *                     Pointer register (rN)
              4      IN4_PM_PTR void*                         Pointer register (rN)
              void* ptr;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              ...
              vstdw_c32_pm_ptr_2dw (vcoefIn, vcoefIn2, ptr, ptr);

Comments


Main table → Memory Access → Store → Store 32 bit coefficient
Available addressing modes
Intrinsic Names:
vstdw_c32_2dw_concat
vstdw_c32_direct_2dw_concat
vstdw_c32_indexed_imm_2dw_concat
vstdw_c32_indexed_rI_2dw_concat
vstdw_c32_indexed_rI_pm_imm_2dw_concat
vstdw_c32_indexed_rI_pm_ptr_2dw_concat
vstdw_c32_indexed_rIp_2dw_concat
vstdw_c32_indexed_rIp_pm_imm_2dw_concat
vstdw_c32_indexed_rIp_pm_ptr_2dw_concat
vstdw_c32_pm_imm_2dw_concat
vstdw_c32_pm_ptr_2dw_concat
Intrinsic     vstdw_c32_2dw_concat
name
Spec syntax   vstdw {2dw [,concat]} vc1X, vc2X, (pN)[+pm_x] [,?prSC]

Return type   void


              1
                                                               Coefficient operand (register vc1 is
                     IN1_VC1       coef_t

expected)
Operands                                                       Coefficient operand (register vc2 is
              2      IN2_VC2       coef_t
                                                               expected)
              3      IN3_PTR       void *                      Pointer register (rN)
              void* ptr;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              ...
              vstdw_c32_2dw_concat (vcoefIn, vcoefIn2, ptr);

Comments



Intrinsic     vstdw_c32_direct_2dw_concat
name
Spec syntax   vstdw {2dw [,concat]} vc1X, vc2X, [#address] [,?prSC]

Return type   void

                                                               Coefficient operand (register vc1 is
              1      IN1_VC1       coef_t
                                                               expected)
Operands                                                       Coefficient operand (register vc2 is
              2      IN2_VC2       coef_t
                                                               expected)
                                                 32
              3      IN3_ADDR      int32     0..2 -1           32 bit address
              coef_t vcoefIn;
              coef_t vcoefIn2;
C example     ...
              vstdw_c32_direct_2dw_concat (vcoefIn, vcoefIn2, 2);

Comments



Intrinsic     vstdw_c32_indexed_imm_2dw_concat
name
Spec syntax   vstdw {2dw [,concat]} vc1X, vc2X, (gB+#imm16_6) [,?prSC]

Return type   void

                                                               Coefficient operand (register vc1 is
Operands      1      IN1_VC1        coef_t
                                                               expected)
                                                              Coefficient operand (register vc2 is
              2      IN2_VC2        coef_t
                                                              expected)
              3      IN3_gB_BASE void *                       Pointer register (gB)

              4
                                                              16 bit immediate post modification in
                     IN4_IMM16_6    int16     -32768..32767
                                                              bytes
              void* ptrBase;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              ...
              vstdw_c32_indexed_imm_2dw_concat (vcoefIn, vcoefIn2, ptrBase, 2);

Comments



Intrinsic     vstdw_c32_indexed_rI_2dw_concat
name

Spec syntax   vstdw {2dw [,concat]} vc1X, vc2X, (gB+rI)[+pm] [,?prSC]

Return type   void

                                                              Coefficient operand (register vc1 is
              1      IN1_VC1         coef_t
                                                              expected)
                                                              Coefficient operand (register vc2 is
              2      IN2_VC2         coef_t
Operands                                                      expected)
              3      IN3_gB_BASE     void *                   Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
              4      IN4_rI_OFFSET void *
                                                              base pointer
              void* ptrBase;
              void* ptrModify;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              ...
              vstdw_c32_indexed_rI_2dw_concat (vcoefIn, vcoefIn2, ptrBase, ptrModify);

Comments



Intrinsic     vstdw_c32_indexed_rI_pm_imm_2dw_concat
name
Spec syntax   vstdw {2dw [,concat]} vc1X, vc2X, (gB+rI)[+pm] [,?prSC]

Return type   void

                                                              Coefficient operand (register vc1 is
              1      IN1_VC1         coef_t
Operands                                                      expected)
              2      IN2_VC2         coef_t                   Coefficient operand (register vc2 is
                                                              expected)
              3      IN3_gB_BASE    void *                    Pointer register (gB)

              4
                                                              Pointer (rI) specifying the offset from the
                     IN4_rI_OFFSET void *
                                                              base pointer
                                                31   31       32 bit immediate post modification in
              5      IN5_PM_IMM     int32     -2 ..2 -1
                                                              bytes
              void* ptrBase;
              void* ptrModify;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              ...
              vstdw_c32_indexed_rI_pm_imm_2dw_concat (vcoefIn, vcoefIn2, ptrBase, ptrModify, 2);

Comments



Intrinsic     vstdw_c32_indexed_rI_pm_ptr_2dw_concat
name

Spec syntax   vstdw {2dw [,concat]} vc1X, vc2X, (gB+rI)[+pm] [,?prSC]

Return type   void

                                                              Coefficient operand (register vc1 is
              1      IN1_VC1        coef_t
                                                              expected)
                                                              Coefficient operand (register vc2 is
              2      IN2_VC2        coef_t
                                                              expected)
Operands      3      IN3_gB_BASE    void *                    Pointer register (gB)

              4
                                                              Pointer (rI) specifying the offset from the
                     IN4_rI_OFFSET void *
                                                              base pointer
              5      IN5_PM_PTR     void*                     Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     coef_t vcoefIn;
              coef_t vcoefIn2;
              ...
              vstdw_c32_indexed_rI_pm_ptr_2dw_concat (vcoefIn, vcoefIn2, ptrBase, ptrModify, ptr);

Comments



Intrinsic     vstdw_c32_indexed_rIp_2dw_concat
name
Spec syntax   vstdw {2dw [,concat]} vc1X, vc2X, (gB+rIp)[+pm] [,?prSC]
Return type   void

                                                             Coefficient operand (register vc1 is
              1      IN1_VC1        coef_t
                                                             expected)

              2
                                                             Coefficient operand (register vc2 is
                     IN2_VC2        coef_t
                                                             expected)
Operands      3      IN3_gB_BASE    void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              4      IN4_rI_OFFSET void *
                                                             base pointer
              5      IN4_PART       uint8    LOW,HIGH        Word part which is used for operand 4
              void* ptrBase;
              void* ptrModify;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              ...
              vstdw_c32_indexed_rIp_2dw_concat (vcoefIn, vcoefIn2, ptrBase, ptrModify, LOW);

Comments



Intrinsic     vstdw_c32_indexed_rIp_pm_imm_2dw_concat
name

Spec syntax   vstdw {2dw [,concat]} vc1X, vc2X, (gB+rIp)[+pm] [,?prSC]

Return type   void

                                                             Coefficient operand (register vc1 is
              1      IN1_VC1        coef_t
                                                             expected)

              2
                                                             Coefficient operand (register vc2 is
                     IN2_VC2        coef_t
                                                             expected)
              3      IN3_gB_BASE    void *                   Pointer register (gB)
Operands
              4
                                                             Pointer (rI) specifying the offset from the
                     IN4_rI_OFFSET void *
                                                             base pointer
              5      IN4_PART       uint8    LOW,HIGH        Word part which is used for operand 4
                                               31   31       32 bit immediate post modification in
              6      IN5_PM_IMM     int32    -2 ..2 -1
                                                             bytes
              void* ptrBase;
              void* ptrModify;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              ...
              vstdw_c32_indexed_rIp_pm_imm_2dw_concat (vcoefIn, vcoefIn2, ptrBase, ptrModify, LOW, 2);

Comments
Intrinsic     vstdw_c32_indexed_rIp_pm_ptr_2dw_concat
name
Spec syntax   vstdw {2dw [,concat]} vc1X, vc2X, (gB+rIp)[+pm] [,?prSC]

Return type   void


              1
                                                             Coefficient operand (register vc1 is
                     IN1_VC1        coef_t
                                                             expected)
                                                             Coefficient operand (register vc2 is
              2      IN2_VC2        coef_t
                                                             expected)

Operands      3      IN3_gB_BASE    void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              4      IN4_rI_OFFSET void *
                                                             base pointer
              5      IN4_PART       uint8    LOW,HIGH        Word part which is used for operand 4

6      IN5_PM_PTR     void*                    Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     coef_t vcoefIn;
              coef_t vcoefIn2;
              ...
              vstdw_c32_indexed_rIp_pm_ptr_2dw_concat (vcoefIn, vcoefIn2, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic     vstdw_c32_pm_imm_2dw_concat
name
Spec syntax   vstdw {2dw [,concat]} vc1X, vc2X, (pN)+#imm32_6 [,?prSC]

Return type   void


              1
                                                             Coefficient operand (register vc1 is
                     IN1_VC1       coef_t
                                                             expected)
                                                             Coefficient operand (register vc2 is
              2      IN2_VC2       coef_t
Operands                                                     expected)
              3      IN3_PTR       void *                    Pointer register (rN)
                                              31   31        32 bit immediate post modification in
              4      IN4_IMM32_6 int32       -2 ..2 -1
                                                             bytes
              void* ptr;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              ...
              vstdw_c32_pm_imm_2dw_concat (vcoefIn, vcoefIn2, ptr, 2);

Comments



Intrinsic     vstdw_c32_pm_ptr_2dw_concat
name
Spec syntax   vstdw {2dw [,concat]} vc1X, vc2X, (pN)[+pm_x] [,?prSC]

Return type   void


              1
                                                              Coefficient operand (register vc1 is
                     IN1_VC1       coef_t
                                                              expected)
                                                              Coefficient operand (register vc2 is
              2      IN2_VC2       coef_t
Operands                                                      expected)
              3      IN3_PTR       void *                     Pointer register (rN)
              4      IN4_PM_PTR void*                         Pointer register (rN)
              void* ptr;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              ...
              vstdw_c32_pm_ptr_2dw_concat (vcoefIn, vcoefIn2, ptr, ptr);

Comments


Main table → Memory Access → Store → Store 32 bit coefficient
Available addressing modes
Intrinsic Names:
vstdw_c32_2dw_vuX

vstdw_c32_indexed_rI_2dw_vuX
vstdw_c32_indexed_rI_pm_imm_2dw_vuX
vstdw_c32_indexed_rI_pm_ptr_2dw_vuX
vstdw_c32_indexed_rIp_2dw_vuX
vstdw_c32_indexed_rIp_pm_imm_2dw_vuX
vstdw_c32_indexed_rIp_pm_ptr_2dw_vuX
vstdw_c32_pm_imm_2dw_vuX
vstdw_c32_pm_ptr_2dw_vuX
Intrinsic     vstdw_c32_2dw_vuX
name
Spec syntax   vstdw {2dw, vuX} vc1X, vc2X, (pN)[+pm_x] [,?prSC]

Return type   void

              1      VUX           uint8      0..3             Determines the source VCU
                                                               Coefficient operand (register vc1 is
              2      IN1_VC1       coef_t
                                                               expected)
Operands
                                                               Coefficient operand (register vc2 is
              3      IN2_VC2       coef_t
                                                               expected)
              4      IN3_PTR       void *                      Pointer register (rN)
              void* ptr;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              ...
              vstdw_c32_2dw_vuX (1, vcoefIn, vcoefIn2, ptr);

Comments



Intrinsic     vstdw_c32_indexed_rI_2dw_vuX
name
Spec syntax   vstdw {2dw, vuX} vc1X, vc2X, (gB+rI)[+pm] [,?prSC]

Return type   void

              1      VUX             uint8     0..3            Determines the source VCU
                                                               Coefficient operand (register vc1 is
              2      IN1_VC1         coef_t
                                                               expected)
                                                               Coefficient operand (register vc2 is
Operands      3      IN2_VC2         coef_t
                                                               expected)
              4      IN3_gB_BASE     void *                    Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the
              5      IN4_rI_OFFSET void *
                                                               base pointer
              void* ptrBase;
              void* ptrModify;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              ...
              vstdw_c32_indexed_rI_2dw_vuX (1, vcoefIn, vcoefIn2, ptrBase, ptrModify);

Comments
Intrinsic     vstdw_c32_indexed_rI_pm_imm_2dw_vuX
name
Spec syntax   vstdw {2dw, vuX} vc1X, vc2X, (gB+rI)[+pm] [,?prSC]

Return type   void

              1      VUX            uint8    0..3            Determines the source VCU
                                                             Coefficient operand (register vc1 is
              2      IN1_VC1        coef_t
                                                             expected)
                                                             Coefficient operand (register vc2 is
              3      IN2_VC2        coef_t
                                                             expected)
Operands
              4      IN3_gB_BASE    void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              5      IN4_rI_OFFSET void *
                                                             base pointer
                                               31   31       32 bit immediate post modification in
              6      IN5_PM_IMM     int32    -2 ..2 -1
                                                             bytes
              void* ptrBase;
              void* ptrModify;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              ...
              vstdw_c32_indexed_rI_pm_imm_2dw_vuX (1, vcoefIn, vcoefIn2, ptrBase, ptrModify, 2);

Comments



Intrinsic     vstdw_c32_indexed_rI_pm_ptr_2dw_vuX
name
Spec syntax   vstdw {2dw, vuX} vc1X, vc2X, (gB+rI)[+pm] [,?prSC]

Return type   void

              1      VUX            uint8    0..3            Determines the source VCU
                                                             Coefficient operand (register vc1 is
              2      IN1_VC1        coef_t
                                                             expected)
                                                             Coefficient operand (register vc2 is
              3      IN2_VC2        coef_t
Operands                                                     expected)
              4      IN3_gB_BASE    void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              5      IN4_rI_OFFSET void *
                                                             base pointer
              6      IN5_PM_PTR     void*                    Pointer register (rN)
              void* ptr;
C example     void* ptrBase;
              void* ptrModify;
              coef_t vcoefIn;
              coef_t vcoefIn2;

...
              vstdw_c32_indexed_rI_pm_ptr_2dw_vuX (1, vcoefIn, vcoefIn2, ptrBase, ptrModify, ptr);

Comments



Intrinsic     vstdw_c32_indexed_rIp_2dw_vuX
name
Spec syntax   vstdw {2dw, vuX} vc1X, vc2X, (gB+rIp)[+pm] [,?prSC]

Return type   void

              1      VUX            uint8     0..3            Determines the source VCU
                                                              Coefficient operand (register vc1 is
              2      IN1_VC1        coef_t
                                                              expected)
                                                              Coefficient operand (register vc2 is
              3      IN2_VC2        coef_t
Operands                                                      expected)
              4      IN3_gB_BASE    void *                    Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
              5      IN4_rI_OFFSET void *
                                                              base pointer
              6      IN4_PART       uint8     LOW,HIGH        Word part which is used for operand 5
              void* ptrBase;
              void* ptrModify;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              ...
              vstdw_c32_indexed_rIp_2dw_vuX (1, vcoefIn, vcoefIn2, ptrBase, ptrModify, LOW);

Comments



Intrinsic     vstdw_c32_indexed_rIp_pm_imm_2dw_vuX
name
Spec syntax   vstdw {2dw, vuX} vc1X, vc2X, (gB+rIp)[+pm] [,?prSC]

Return type   void

              1      VUX            uint8     0..3            Determines the source VCU
                                                              Coefficient operand (register vc1 is
              2      IN1_VC1        coef_t
Operands                                                      expected)
                                                              Coefficient operand (register vc2 is
              3      IN2_VC2        coef_t
                                                              expected)
              4      IN3_gB_BASE    void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              5      IN4_rI_OFFSET void *
                                                             base pointer
              6      IN4_PART       uint8    LOW,HIGH        Word part which is used for operand 5

31   31       32 bit immediate post modification in
              7      IN5_PM_IMM     int32    -2 ..2 -1
                                                             bytes
              void* ptrBase;
              void* ptrModify;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              ...
              vstdw_c32_indexed_rIp_pm_imm_2dw_vuX (1, vcoefIn, vcoefIn2, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic     vstdw_c32_indexed_rIp_pm_ptr_2dw_vuX
name
Spec syntax   vstdw {2dw, vuX} vc1X, vc2X, (gB+rIp)[+pm] [,?prSC]

Return type   void

              1      VUX            uint8    0..3            Determines the source VCU
                                                             Coefficient operand (register vc1 is
              2      IN1_VC1        coef_t
                                                             expected)
                                                             Coefficient operand (register vc2 is
              3      IN2_VC2        coef_t
                                                             expected)
Operands      4      IN3_gB_BASE    void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              5      IN4_rI_OFFSET void *
                                                             base pointer
              6      IN4_PART       uint8    LOW,HIGH        Word part which is used for operand 5
              7      IN5_PM_PTR     void*                    Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     coef_t vcoefIn;
              coef_t vcoefIn2;
              ...
              vstdw_c32_indexed_rIp_pm_ptr_2dw_vuX (1, vcoefIn, vcoefIn2, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic     vstdw_c32_pm_imm_2dw_vuX
name
Spec syntax   vstdw {2dw, vuX} vc1X, vc2X, (pN)[+pm_x] [,?prSC]

Return type   void

              1      VUX           uint8     0..3             Determines the source VCU
                                                              Coefficient operand (register vc1 is
              2      IN1_VC1       coef_t
                                                              expected)
                                                              Coefficient operand (register vc2 is
Operands      3      IN2_VC2       coef_t
                                                              expected)

4      IN3_PTR       void *                     Pointer register (rN)
                                               31   31        32 bit immediate post modification in
              5      IN4_PM_IMM int32        -2 ..2 -1
                                                              bytes
              void* ptr;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              ...
              vstdw_c32_pm_imm_2dw_vuX (1, vcoefIn, vcoefIn2, ptr, 2);

Comments



Intrinsic     vstdw_c32_pm_ptr_2dw_vuX
name
Spec syntax   vstdw {2dw, vuX} vc1X, vc2X, (pN)[+pm_x] [,?prSC]

Return type   void

              1      VUX           uint8     0..3             Determines the source VCU
                                                              Coefficient operand (register vc1 is
              2      IN1_VC1       coef_t
                                                              expected)
Operands                                                      Coefficient operand (register vc2 is
              3      IN2_VC2       coef_t
                                                              expected)
              4      IN3_PTR       void *                     Pointer register (rN)
              5      IN4_PM_PTR void*                         Pointer register (rN)
              void* ptr;
              coef_t vcoefIn;
C example     coef_t vcoefIn2;
              ...
              vstdw_c32_pm_ptr_2dw_vuX (1, vcoefIn, vcoefIn2, ptr, ptr);

Comments


Main table → Memory Access → Store → Store 32 bit coefficient
Available addressing modes
Intrinsic Names:
vstdw_c32_dw_vuX
vstdw_c32_indexed_rI_dw_vuX
vstdw_c32_indexed_rI_pm_imm_dw_vuX
vstdw_c32_indexed_rI_pm_ptr_dw_vuX
vstdw_c32_indexed_rIp_dw_vuX
vstdw_c32_indexed_rIp_pm_imm_dw_vuX
vstdw_c32_indexed_rIp_pm_ptr_dw_vuX
vstdw_c32_pm_imm_dw_vuX
vstdw_c32_pm_ptr_dw_vuX
Intrinsic     vstdw_c32_dw_vuX
name
Spec syntax   vstdw {dw, vuX} vcX, (pN)[+pm_x] [,?prSC]

Return type   void

              1      VUX           uint8     0..3            Determines the source VCU
Operands      2      IN1_C32       coef_t                    Coefficient operand
              3      IN2_PTR       void *                    Pointer register (rN)
              void* ptr;
              coef_t vcoefIn;
C example     ...
              vstdw_c32_dw_vuX (1, vcoefIn, ptr);

Comments



Intrinsic     vstdw_c32_indexed_rI_dw_vuX
name
Spec syntax   vstdw {dw, vuX} vcX, (gB+rI)[+pm] [,?prSC]

Return type   void

1      VUX            uint8     0..3            Determines the source VCU
              2      IN1_C32        coef_t                    Coefficient operand
Operands      3      IN2_gB_BASE    void *                    Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
              4      IN3_rI_OFFSET void *
                                                              base pointer
              void* ptrBase;
              void* ptrModify;
C example     coef_t vcoefIn;
              ...
              vstdw_c32_indexed_rI_dw_vuX (1, vcoefIn, ptrBase, ptrModify);

Comments



Intrinsic     vstdw_c32_indexed_rI_pm_imm_dw_vuX
name
Spec syntax   vstdw {dw, vuX} vcX, (gB+rI)[+pm] [,?prSC]

Return type   void

              1      VUX            uint8     0..3            Determines the source VCU
Operands
              2      IN1_C32        coef_t                    Coefficient operand
              3      IN2_gB_BASE    void *                    Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
              4      IN3_rI_OFFSET void *
                                                              base pointer

              5                                 31   31       32 bit immediate post modification in
                     IN4_PM_IMM     int32     -2 ..2 -1
                                                              bytes
              void* ptrBase;
              void* ptrModify;
C example     coef_t vcoefIn;
              ...
              vstdw_c32_indexed_rI_pm_imm_dw_vuX (1, vcoefIn, ptrBase, ptrModify, 2);

Comments



Intrinsic     vstdw_c32_indexed_rI_pm_ptr_dw_vuX
name
Spec syntax   vstdw {dw, vuX} vcX, (gB+rI)[+pm] [,?prSC]

Return type   void

              1      VUX            uint8     0..3            Determines the source VCU
              2      IN1_C32        coef_t                    Coefficient operand
              3      IN2_gB_BASE    void *                    Pointer register (gB)
Operands
                                                              Pointer (rI) specifying the offset from the
              4      IN3_rI_OFFSET void *
                                                              base pointer
              5      IN4_PM_PTR     void*                     Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;

C example     coef_t vcoefIn;
              ...
              vstdw_c32_indexed_rI_pm_ptr_dw_vuX (1, vcoefIn, ptrBase, ptrModify, ptr);

Comments



Intrinsic     vstdw_c32_indexed_rIp_dw_vuX
name
Spec syntax   vstdw {dw, vuX} vcX, (gB+rIp)[+pm] [,?prSC]

Return type   void

              1      VUX            uint8     0..3            Determines the source VCU
Operands      2      IN1_C32        coef_t                    Coefficient operand
              3      IN2_gB_BASE    void *                    Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              4      IN3_rI_OFFSET void *
                                                             base pointer
              5      IN3_PART       uint8    LOW,HIGH        Word part which is used for operand 4
              void* ptrBase;
              void* ptrModify;
C example     coef_t vcoefIn;
              ...
              vstdw_c32_indexed_rIp_dw_vuX (1, vcoefIn, ptrBase, ptrModify, LOW);

Comments



Intrinsic     vstdw_c32_indexed_rIp_pm_imm_dw_vuX
name
Spec syntax   vstdw {dw, vuX} vcX, (gB+rIp)[+pm] [,?prSC]

Return type   void

              1      VUX            uint8    0..3            Determines the source VCU
              2      IN1_C32        coef_t                   Coefficient operand
              3      IN2_gB_BASE    void *                   Pointer register (gB)

Operands                                                     Pointer (rI) specifying the offset from the
              4      IN3_rI_OFFSET void *
                                                             base pointer
              5      IN3_PART       uint8    LOW,HIGH        Word part which is used for operand 4
                                               31   31       32 bit immediate post modification in
              6      IN4_PM_IMM     int32    -2 ..2 -1
                                                             bytes
              void* ptrBase;
              void* ptrModify;
C example     coef_t vcoefIn;
              ...
              vstdw_c32_indexed_rIp_pm_imm_dw_vuX (1, vcoefIn, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic     vstdw_c32_indexed_rIp_pm_ptr_dw_vuX
name
Spec syntax   vstdw {dw, vuX} vcX, (gB+rIp)[+pm] [,?prSC]

Return type   void

              1      VUX            uint8    0..3            Determines the source VCU
Operands      2      IN1_C32        coef_t                   Coefficient operand

3      IN2_gB_BASE    void *                   Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
              4   IN3_rI_OFFSET void *
                                                              base pointer
              5   IN3_PART          uint8    LOW,HIGH         Word part which is used for operand 4
              6   IN4_PM_PTR        void*                     Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     coef_t vcoefIn;
              ...
              vstdw_c32_indexed_rIp_pm_ptr_dw_vuX (1, vcoefIn, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic     vstdw_c32_pm_imm_dw_vuX
name
Spec syntax   vstdw {dw, vuX} vcX, (pN)[+pm_x] [,?prSC]

Return type   void

              1      VUX          uint8     0..3              Determines the source VCU
              2      IN1_C32      coef_t                      Coefficient operand
Operands      3      IN2_PTR      void *                      Pointer register (rN)
                                              31   31         32 bit immediate post modification in
              4      IN3_PM_IMM int32       -2 ..2 -1
                                                              bytes
              void* ptr;
              coef_t vcoefIn;
C example     ...
              vstdw_c32_pm_imm_dw_vuX (1, vcoefIn, ptr, 2);

Comments



Intrinsic     vstdw_c32_pm_ptr_dw_vuX
name
Spec syntax   vstdw {dw, vuX} vcX, (pN)[+pm_x] [,?prSC]

Return type   void

              1      VUX          uint8     0..3              Determines the source VCU
              2      IN1_C32      coef_t                      Coefficient operand
Operands
              3      IN2_PTR      void *                      Pointer register (rN)
              4      IN3_PM_PTR void*                         Pointer register (rN)
C example     void* ptr;
             coef_t vcoefIn;
             ...
             vstdw_c32_pm_ptr_dw_vuX (1, vcoefIn, ptr, ptr);

Comments


Main table → Memory Access → Store → Store 32 bit coefficient
