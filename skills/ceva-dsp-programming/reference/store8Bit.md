# Memory Access → Store → Store 8 bit

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Memory Access → Store → Store 8 bit

Store 8 bit

Store 8 bit
Store 8 bit
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
vstb_v32_mw
vstb_v32_mw_concat
vstb_v32_mw_h
vstb_v32_mw_h_concat
vstb_v40_pb
vstb_v40_pb_concat
vstb_v40_mw_vuX
vstb_v40_mw_vuX_h
vstb_v40_mw
vstb_v40_mw_concat
vstb_v40_mw_h
vstb_v40_mw_h_concat
vstb_v32_pb
vstb_v32_pb_concat
vstb_v40_pb_vuX
vstb_v32_pb_vuX
vstb_v32_mw_vuX
vstb_v32_mw_vuX_h
Instruction details in the instruction set specification
Available addressing modes
Intrinsic Names:
vstb_v32_direct_mw
vstb_v32_indexed_imm_mw
vstb_v32_indexed_rI_mw
vstb_v32_indexed_rI_pm_imm_mw
vstb_v32_indexed_rI_pm_ptr_mw
vstb_v32_indexed_rIp_mw
vstb_v32_indexed_rIp_pm_imm_mw
vstb_v32_indexed_rIp_pm_ptr_mw
vstb_v32_mw
vstb_v32_pm_imm_mw
vstb_v32_pm_ptr_mw
Intrinsic     vstb_v32_direct_mw
name
Spec syntax   vstb {mw [,h][,concat]} vix[0], [#address] [,?prSC]

Return        void
type
                                                               Determines the element size and number
                                MW_options
              1      MW
                                enum                           of stored elements (see enum definition at
                                                               vec-mem-modes.h)
Operands

2      IN1_V32    vec_t                          Input vector operand
                                                    32
              3      IN2_ADDR   int32          0..2 -1         32 bit address
              vec_t vIn;
C example     ...
              vstb_v32_direct_mw (mw_8w, vIn, 2);

Comments



Intrinsic     vstb_v32_indexed_imm_mw
name
Spec          vstb {mw [,h][,concat]} vix[0], (gB+#imm16_6) [,?prSC]
syntax
Return        void
type
                                                               Determines the element size and number
                                 MW_options
              1 MW
                                 enum                          of stored elements (see enum definition
                                                               at vec-mem-modes.h)

Operands      2 IN1_V32          vec_t                         Input vector operand
              3 IN2_gB_BASE void *                             Pointer register (gB)

              4 IN3_IMM16_6
                                                -              16 bit immediate post modification in
                                 int16
                                                32768..32767   bytes
              void* ptrBase;
              vec_t vIn;
C example     ...
              vstb_v32_indexed_imm_mw (mw_8w, vIn, ptrBase, 2);

Comments



Intrinsic     vstb_v32_indexed_rI_mw
name
Spec          vstb {mw [,h][,concat]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                MW_options
            1 MW
                                enum                          of stored elements (see enum definition
                                                              at vec-mem-modes.h)

Operands    2 IN1_V32           vec_t                         Input vector operand
            3 IN2_gB_BASE       void *                        Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                              base pointer
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstb_v32_indexed_rI_mw (mw_8w, vIn, ptrBase, ptrModify);

Comments



Intrinsic   vstb_v32_indexed_rI_pm_imm_mw
name

Spec        vstb {mw [,h][,concat]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                MW_options
            1 MW
                                enum                          of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_V32           vec_t                         Input vector operand
Operands    3 IN2_gB_BASE       void *                        Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                              base pointer
                                                 31   31      32 bit immediate post modification in
            5 IN4_PM_IMM        int32          -2 ..2 -1
                                                              bytes
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstb_v32_indexed_rI_pm_imm_mw (mw_8w, vIn, ptrBase, ptrModify, 2);

Comments
Intrinsic   vstb_v32_indexed_rI_pm_ptr_mw
name
Spec        vstb {mw [,h][,concat]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                MW_options
            1 MW
                                enum                          of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_V32           vec_t                         Input vector operand
Operands    3 IN2_gB_BASE       void *                        Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                              base pointer
            5 IN4_PM_PTR        void*                         Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstb_v32_indexed_rI_pm_ptr_mw (mw_8w, vIn, ptrBase, ptrModify, ptr);

Comments



Intrinsic   vstb_v32_indexed_rIp_mw
name

Spec        vstb {mw [,h][,concat]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                MW_options
            1 MW
                                enum                          of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_V32           vec_t                         Input vector operand
Operands    3 IN2_gB_BASE       void *                        Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                              base pointer
            5 IN3_PART          uint8          LOW,HIGH       Word part which is used for operand 4
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstb_v32_indexed_rIp_mw (mw_8w, vIn, ptrBase, ptrModify, LOW);

Comments



Intrinsic   vstb_v32_indexed_rIp_pm_imm_mw
name
Spec        vstb {mw [,h][,concat]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                MW_options
            1 MW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
            2 IN1_V32           vec_t                        Input vector operand
            3 IN2_gB_BASE       void *                       Pointer register (gB)
Operands
                                                             Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                             base pointer
            5 IN3_PART          uint8         LOW,HIGH       Word part which is used for operand 4
                                                31   31      32 bit immediate post modification in
            6 IN4_PM_IMM        int32         -2 ..2 -1
                                                             bytes
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstb_v32_indexed_rIp_pm_imm_mw (mw_8w, vIn, ptrBase, ptrModify, LOW, 2);

Comments

Intrinsic   vstb_v32_indexed_rIp_pm_ptr_mw
name
Spec        vstb {mw [,h][,concat]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                MW_options                   Determines the element size and number
Operands    1 MW
                                enum                         of stored elements (see enum definition
                                                               at vec-mem-modes.h)
              2 IN1_V32           vec_t                        Input vector operand
              3 IN2_gB_BASE       void *                       Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the
              4 IN3_rI_OFFSET void *
                                                               base pointer
              5 IN3_PART          uint8          LOW,HIGH      Word part which is used for operand 4
              6 IN4_PM_PTR        void*                        Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec_t vIn;
              ...
              vstb_v32_indexed_rIp_pm_ptr_mw (mw_8w, vIn, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic     vstb_v32_mw
name
Spec syntax   vstb {mw [,h][,concat]} vix[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                              Determines the element size and number
                                MW_options
              1   MW
                                enum                          of stored elements (see enum definition at
                                                              vec-mem-modes.h)
Operands
              2   IN1_V32       vec_t                         Input vector operand
              3   IN2_PTR       void *                        Pointer register (rN)
              void* ptr;
              vec_t vIn;
C example     ...
              vstb_v32_mw (mw_8w, vIn, ptr);

Comments



Intrinsic     vstb_v32_pm_imm_mw
name
Spec          vstb {mw [,h][,concat]} vix[0], (pN)+#imm32_6 [,?prSC]
syntax
Return        void
type
                                                            Determines the element size and number
                                MW_options
             1   MW
                                enum                        of stored elements (see enum definition at

vec-mem-modes.h)

Operands     2   IN1_V32        vec_t                       Input vector operand
             3   IN2_PTR        void *                      Pointer register (rN)
                                                31   31     32 bit immediate post modification in
             4   IN3_IMM32_6 int32            -2 ..2 -1
                                                            bytes
             void* ptr;
             vec_t vIn;
C example    ...
             vstb_v32_pm_imm_mw (mw_8w, vIn, ptr, 2);

Comments



Intrinsic    vstb_v32_pm_ptr_mw
name
Spec         vstb {mw [,h][,concat]} vix[0], (pN)[+pm_x] [,?prSC]
syntax
Return       void
type
                                                            Determines the element size and number
                                MW_options
             1   MW
                                enum                        of stored elements (see enum definition at
                                                            vec-mem-modes.h)
Operands     2   IN1_V32        vec_t                       Input vector operand
             3   IN2_PTR        void *                      Pointer register (rN)
             4   IN3_PM_PTR void*                           Pointer register (rN)
             void* ptr;
             vec_t vIn;
C example    ...
             vstb_v32_pm_ptr_mw (mw_8w, vIn, ptr, ptr);

Comments


Main table → Memory Access → Store → Store 8 bit
Available addressing modes
Intrinsic Names:
vstb_v32_direct_mw_concat
vstb_v32_indexed_imm_mw_concat
vstb_v32_indexed_rI_mw_concat
vstb_v32_indexed_rI_pm_imm_mw_concat
vstb_v32_indexed_rI_pm_ptr_mw_concat
vstb_v32_indexed_rIp_mw_concat
vstb_v32_indexed_rIp_pm_imm_mw_concat
vstb_v32_indexed_rIp_pm_ptr_mw_concat
vstb_v32_mw_concat
vstb_v32_pm_imm_mw_concat
vstb_v32_pm_ptr_mw_concat
Intrinsic     vstb_v32_direct_mw_concat
name
Spec syntax   vstb {mw [,h][,concat]} vix[0], [#address] [,?prSC]

Return        void
type
                                                               Determines the element size and number
                                MW_options
              1      MW
                                enum                           of stored elements (see enum definition at
                                                               vec-mem-modes.h)
Operands
              2      IN1_V32    vec_t                          Input vector operand
                                                  32

3      IN2_ADDR   int32          0..2 -1         32 bit address
              vec_t vIn;
C example     ...
              vstb_v32_direct_mw_concat (mw_8w, vIn, 2);

Comments



Intrinsic     vstb_v32_indexed_imm_mw_concat
name
Spec          vstb {mw [,h][,concat]} vix[0], (gB+#imm16_6) [,?prSC]
syntax
Return        void
type
                                                               Determines the element size and number
                                 MW_options
              1 MW
                                 enum                          of stored elements (see enum definition
                                                               at vec-mem-modes.h)

Operands      2 IN1_V32          vec_t                         Input vector operand
              3 IN2_gB_BASE void *                             Pointer register (gB)

              4 IN3_IMM16_6
                                                -              16 bit immediate post modification in
                                 int16
                                                32768..32767   bytes
              void* ptrBase;
              vec_t vIn;
C example     ...
              vstb_v32_indexed_imm_mw_concat (mw_8w, vIn, ptrBase, 2);

Comments



Intrinsic     vstb_v32_indexed_rI_mw_concat
name
Spec          vstb {mw [,h][,concat]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                MW_options
            1 MW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)

Operands    2 IN1_V32           vec_t                        Input vector operand
            3 IN2_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                             base pointer
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstb_v32_indexed_rI_mw_concat (mw_8w, vIn, ptrBase, ptrModify);

Comments



Intrinsic   vstb_v32_indexed_rI_pm_imm_mw_concat
name
Spec        vstb {mw [,h][,concat]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type

Determines the element size and number
                                MW_options
            1 MW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
            2 IN1_V32           vec_t                        Input vector operand
Operands    3 IN2_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                             base pointer
                                                 31   31     32 bit immediate post modification in
            5 IN4_PM_IMM        int32          -2 ..2 -1
                                                             bytes
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstb_v32_indexed_rI_pm_imm_mw_concat (mw_8w, vIn, ptrBase, ptrModify, 2);

Comments
Intrinsic   vstb_v32_indexed_rI_pm_ptr_mw_concat
name
Spec        vstb {mw [,h][,concat]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                MW_options
            1 MW
                                enum                          of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_V32           vec_t                         Input vector operand
Operands    3 IN2_gB_BASE       void *                        Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                              base pointer
            5 IN4_PM_PTR        void*                         Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstb_v32_indexed_rI_pm_ptr_mw_concat (mw_8w, vIn, ptrBase, ptrModify, ptr);

Comments



Intrinsic   vstb_v32_indexed_rIp_mw_concat
name
Spec        vstb {mw [,h][,concat]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number

MW_options
            1 MW
                                enum                          of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_V32           vec_t                         Input vector operand
Operands    3 IN2_gB_BASE       void *                        Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                              base pointer
            5 IN3_PART          uint8          LOW,HIGH       Word part which is used for operand 4
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstb_v32_indexed_rIp_mw_concat (mw_8w, vIn, ptrBase, ptrModify, LOW);

Comments



Intrinsic   vstb_v32_indexed_rIp_pm_imm_mw_concat
name
Spec        vstb {mw [,h][,concat]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                            Determines the element size and number
                                MW_options
            1 MW
                                enum                        of stored elements (see enum definition
                                                            at vec-mem-modes.h)
            2 IN1_V32           vec_t                       Input vector operand
            3 IN2_gB_BASE       void *                      Pointer register (gB)
Operands
                                                            Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                            base pointer
            5 IN3_PART          uint8         LOW,HIGH      Word part which is used for operand 4
                                                31   31     32 bit immediate post modification in
            6 IN4_PM_IMM        int32         -2 ..2 -1
                                                            bytes
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstb_v32_indexed_rIp_pm_imm_mw_concat (mw_8w, vIn, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic   vstb_v32_indexed_rIp_pm_ptr_mw_concat
name
Spec        vstb {mw [,h][,concat]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type

MW_options                  Determines the element size and number
Operands    1 MW
                                enum                        of stored elements (see enum definition
                                                               at vec-mem-modes.h)
              2 IN1_V32           vec_t                        Input vector operand
              3 IN2_gB_BASE       void *                       Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the
              4 IN3_rI_OFFSET void *
                                                               base pointer
              5 IN3_PART          uint8          LOW,HIGH      Word part which is used for operand 4
              6 IN4_PM_PTR        void*                        Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec_t vIn;
              ...
              vstb_v32_indexed_rIp_pm_ptr_mw_concat (mw_8w, vIn, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic     vstb_v32_mw_concat
name
Spec syntax   vstb {mw [,h][,concat]} vix[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                              Determines the element size and number
                                MW_options
              1   MW
                                enum                          of stored elements (see enum definition at
                                                              vec-mem-modes.h)
Operands
              2   IN1_V32       vec_t                         Input vector operand
              3   IN2_PTR       void *                        Pointer register (rN)
              void* ptr;
              vec_t vIn;
C example     ...
              vstb_v32_mw_concat (mw_8w, vIn, ptr);

Comments



Intrinsic     vstb_v32_pm_imm_mw_concat
name
Spec          vstb {mw [,h][,concat]} vix[0], (pN)+#imm32_6 [,?prSC]
syntax
Return        void
type
                                                             Determines the element size and number
                                MW_options
             1   MW
                                enum                         of stored elements (see enum definition at
                                                             vec-mem-modes.h)

Operands     2   IN1_V32        vec_t                        Input vector operand

3   IN2_PTR        void *                       Pointer register (rN)
                                                31   31      32 bit immediate post modification in
             4   IN3_IMM32_6 int32            -2 ..2 -1
                                                             bytes
             void* ptr;
             vec_t vIn;
C example    ...
             vstb_v32_pm_imm_mw_concat (mw_8w, vIn, ptr, 2);

Comments



Intrinsic    vstb_v32_pm_ptr_mw_concat
name
Spec         vstb {mw [,h][,concat]} vix[0], (pN)[+pm_x] [,?prSC]
syntax
Return       void
type
                                                             Determines the element size and number
                               MW_options
             1   MW
                               enum                          of stored elements (see enum definition at
                                                             vec-mem-modes.h)
Operands     2   IN1_V32       vec_t                         Input vector operand
             3   IN2_PTR       void *                        Pointer register (rN)
             4   IN3_PM_PTR void*                            Pointer register (rN)
             void* ptr;
             vec_t vIn;
C example    ...
             vstb_v32_pm_ptr_mw_concat (mw_8w, vIn, ptr, ptr);

Comments


Main table → Memory Access → Store → Store 8 bit
Available addressing modes
Intrinsic Names:
vstb_v32_direct_mw_h
vstb_v32_indexed_imm_mw_h
vstb_v32_indexed_rI_mw_h
vstb_v32_indexed_rI_pm_imm_mw_h
vstb_v32_indexed_rI_pm_ptr_mw_h
vstb_v32_indexed_rIp_mw_h
vstb_v32_indexed_rIp_pm_imm_mw_h
vstb_v32_indexed_rIp_pm_ptr_mw_h
vstb_v32_mw_h
vstb_v32_pm_imm_mw_h
vstb_v32_pm_ptr_mw_h
Intrinsic     vstb_v32_direct_mw_h
name
Spec syntax   vstb {mw [,h][,concat]} vix[0], [#address] [,?prSC]

Return        void
type
                                                               Determines the element size and number
                                MW_options
              1      MW
                                enum                           of stored elements (see enum definition at
                                                               vec-mem-modes.h)
Operands
              2      IN1_V32    vec_t                          Input vector operand
                                                  32
              3      IN2_ADDR   int32          0..2 -1         32 bit address
              vec_t vIn;
C example     ...
              vstb_v32_direct_mw_h (mw_8w, vIn, 2);

Comments

Intrinsic     vstb_v32_indexed_imm_mw_h
name
Spec          vstb {mw [,h][,concat]} vix[0], (gB+#imm16_6) [,?prSC]
syntax
Return        void
type
                                                               Determines the element size and number
                                 MW_options
              1 MW
                                 enum                          of stored elements (see enum definition
                                                               at vec-mem-modes.h)

Operands      2 IN1_V32          vec_t                         Input vector operand
              3 IN2_gB_BASE void *                             Pointer register (gB)

              4 IN3_IMM16_6
                                                -              16 bit immediate post modification in
                                 int16
                                                32768..32767   bytes
              void* ptrBase;
              vec_t vIn;
C example     ...
              vstb_v32_indexed_imm_mw_h (mw_8w, vIn, ptrBase, 2);

Comments



Intrinsic     vstb_v32_indexed_rI_mw_h
name
Spec          vstb {mw [,h][,concat]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                MW_options
            1 MW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)

Operands    2 IN1_V32           vec_t                        Input vector operand
            3 IN2_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                             base pointer
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstb_v32_indexed_rI_mw_h (mw_8w, vIn, ptrBase, ptrModify);

Comments



Intrinsic   vstb_v32_indexed_rI_pm_imm_mw_h
name
Spec        vstb {mw [,h][,concat]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                MW_options
            1 MW

enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
            2 IN1_V32           vec_t                        Input vector operand
Operands    3 IN2_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                             base pointer
                                                 31   31     32 bit immediate post modification in
            5 IN4_PM_IMM        int32          -2 ..2 -1
                                                             bytes
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstb_v32_indexed_rI_pm_imm_mw_h (mw_8w, vIn, ptrBase, ptrModify, 2);

Comments
Intrinsic   vstb_v32_indexed_rI_pm_ptr_mw_h
name
Spec        vstb {mw [,h][,concat]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                MW_options
            1 MW
                                enum                          of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_V32           vec_t                         Input vector operand
Operands    3 IN2_gB_BASE       void *                        Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                              base pointer
            5 IN4_PM_PTR        void*                         Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstb_v32_indexed_rI_pm_ptr_mw_h (mw_8w, vIn, ptrBase, ptrModify, ptr);

Comments



Intrinsic   vstb_v32_indexed_rIp_mw_h
name
Spec        vstb {mw [,h][,concat]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                MW_options
            1 MW

enum                          of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_V32           vec_t                         Input vector operand
Operands    3 IN2_gB_BASE       void *                        Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                              base pointer
            5 IN3_PART          uint8          LOW,HIGH       Word part which is used for operand 4
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstb_v32_indexed_rIp_mw_h (mw_8w, vIn, ptrBase, ptrModify, LOW);

Comments



Intrinsic   vstb_v32_indexed_rIp_pm_imm_mw_h
name
Spec        vstb {mw [,h][,concat]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                            Determines the element size and number
                                MW_options
            1 MW
                                enum                        of stored elements (see enum definition
                                                            at vec-mem-modes.h)
            2 IN1_V32           vec_t                       Input vector operand
            3 IN2_gB_BASE       void *                      Pointer register (gB)
Operands
                                                            Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                            base pointer
            5 IN3_PART          uint8         LOW,HIGH      Word part which is used for operand 4
                                                31   31     32 bit immediate post modification in
            6 IN4_PM_IMM        int32         -2 ..2 -1
                                                            bytes
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstb_v32_indexed_rIp_pm_imm_mw_h (mw_8w, vIn, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic   vstb_v32_indexed_rIp_pm_ptr_mw_h
name
Spec        vstb {mw [,h][,concat]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                MW_options                  Determines the element size and number
Operands    1 MW

enum                        of stored elements (see enum definition
                                                               at vec-mem-modes.h)
              2 IN1_V32           vec_t                        Input vector operand
              3 IN2_gB_BASE       void *                       Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the
              4 IN3_rI_OFFSET void *
                                                               base pointer
              5 IN3_PART          uint8          LOW,HIGH      Word part which is used for operand 4
              6 IN4_PM_PTR        void*                        Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec_t vIn;
              ...
              vstb_v32_indexed_rIp_pm_ptr_mw_h (mw_8w, vIn, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic     vstb_v32_mw_h
name
Spec syntax   vstb {mw [,h][,concat]} vix[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                              Determines the element size and number
                                MW_options
              1   MW
                                enum                          of stored elements (see enum definition at
                                                              vec-mem-modes.h)
Operands
              2   IN1_V32       vec_t                         Input vector operand
              3   IN2_PTR       void *                        Pointer register (rN)
              void* ptr;
              vec_t vIn;
C example     ...
              vstb_v32_mw_h (mw_8w, vIn, ptr);

Comments



Intrinsic     vstb_v32_pm_imm_mw_h
name
Spec          vstb {mw [,h][,concat]} vix[0], (pN)+#imm32_6 [,?prSC]
syntax
Return        void
type
                                                            Determines the element size and number
                                MW_options
             1   MW
                                enum                        of stored elements (see enum definition at
                                                            vec-mem-modes.h)

Operands     2   IN1_V32        vec_t                       Input vector operand
             3   IN2_PTR        void *                      Pointer register (rN)
                                                31   31     32 bit immediate post modification in

4   IN3_IMM32_6 int32            -2 ..2 -1
                                                            bytes
             void* ptr;
             vec_t vIn;
C example    ...
             vstb_v32_pm_imm_mw_h (mw_8w, vIn, ptr, 2);

Comments



Intrinsic    vstb_v32_pm_ptr_mw_h
name
Spec         vstb {mw [,h][,concat]} vix[0], (pN)[+pm_x] [,?prSC]
syntax
Return       void
type
                                                            Determines the element size and number
                               MW_options
             1   MW
                               enum                         of stored elements (see enum definition at
                                                            vec-mem-modes.h)
Operands     2   IN1_V32       vec_t                        Input vector operand
             3   IN2_PTR       void *                       Pointer register (rN)
             4   IN3_PM_PTR void*                           Pointer register (rN)
             void* ptr;
             vec_t vIn;
C example    ...
             vstb_v32_pm_ptr_mw_h (mw_8w, vIn, ptr, ptr);

Comments


Main table → Memory Access → Store → Store 8 bit
Available addressing modes
Intrinsic Names:
vstb_v32_direct_mw_h_concat
vstb_v32_indexed_imm_mw_h_concat
vstb_v32_indexed_rI_mw_h_concat
vstb_v32_indexed_rI_pm_imm_mw_h_concat
vstb_v32_indexed_rI_pm_ptr_mw_h_concat
vstb_v32_indexed_rIp_mw_h_concat
vstb_v32_indexed_rIp_pm_imm_mw_h_concat
vstb_v32_indexed_rIp_pm_ptr_mw_h_concat
vstb_v32_mw_h_concat
vstb_v32_pm_imm_mw_h_concat
vstb_v32_pm_ptr_mw_h_concat
Intrinsic     vstb_v32_direct_mw_h_concat
name
Spec syntax   vstb {mw [,h][,concat]} vix[0], [#address] [,?prSC]

Return        void
type
                                                               Determines the element size and number
                                MW_options
              1      MW
                                enum                           of stored elements (see enum definition at
                                                               vec-mem-modes.h)
Operands
              2      IN1_V32    vec_t                          Input vector operand
                                                  32
              3      IN2_ADDR   int32          0..2 -1         32 bit address
              vec_t vIn;
C example     ...
              vstb_v32_direct_mw_h_concat (mw_8w, vIn, 2);

Comments



Intrinsic     vstb_v32_indexed_imm_mw_h_concat
name

Spec          vstb {mw [,h][,concat]} vix[0], (gB+#imm16_6) [,?prSC]
syntax
Return        void
type
                                                               Determines the element size and number
                                 MW_options
              1 MW
                                 enum                          of stored elements (see enum definition
                                                               at vec-mem-modes.h)

Operands      2 IN1_V32          vec_t                         Input vector operand
              3 IN2_gB_BASE void *                             Pointer register (gB)

              4 IN3_IMM16_6
                                                -              16 bit immediate post modification in
                                 int16
                                                32768..32767   bytes
              void* ptrBase;
              vec_t vIn;
C example     ...
              vstb_v32_indexed_imm_mw_h_concat (mw_8w, vIn, ptrBase, 2);

Comments



Intrinsic     vstb_v32_indexed_rI_mw_h_concat
name
Spec          vstb {mw [,h][,concat]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                MW_options
            1 MW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)

Operands    2 IN1_V32           vec_t                        Input vector operand
            3 IN2_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                             base pointer
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstb_v32_indexed_rI_mw_h_concat (mw_8w, vIn, ptrBase, ptrModify);

Comments



Intrinsic   vstb_v32_indexed_rI_pm_imm_mw_h_concat
name
Spec        vstb {mw [,h][,concat]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                MW_options
            1 MW
                                enum                         of stored elements (see enum definition

at vec-mem-modes.h)
            2 IN1_V32           vec_t                        Input vector operand
Operands    3 IN2_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                             base pointer
                                                 31   31     32 bit immediate post modification in
            5 IN4_PM_IMM        int32          -2 ..2 -1
                                                             bytes
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstb_v32_indexed_rI_pm_imm_mw_h_concat (mw_8w, vIn, ptrBase, ptrModify, 2);

Comments
Intrinsic   vstb_v32_indexed_rI_pm_ptr_mw_h_concat
name
Spec        vstb {mw [,h][,concat]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                MW_options
            1 MW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
            2 IN1_V32           vec_t                        Input vector operand
Operands    3 IN2_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                             base pointer
            5 IN4_PM_PTR        void*                        Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstb_v32_indexed_rI_pm_ptr_mw_h_concat (mw_8w, vIn, ptrBase, ptrModify, ptr);

Comments



Intrinsic   vstb_v32_indexed_rIp_mw_h_concat
name
Spec        vstb {mw [,h][,concat]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                MW_options
            1 MW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)

2 IN1_V32           vec_t                        Input vector operand
Operands    3 IN2_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                             base pointer
            5 IN3_PART          uint8          LOW,HIGH      Word part which is used for operand 4
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstb_v32_indexed_rIp_mw_h_concat (mw_8w, vIn, ptrBase, ptrModify, LOW);

Comments



Intrinsic   vstb_v32_indexed_rIp_pm_imm_mw_h_concat
name
Spec        vstb {mw [,h][,concat]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                            Determines the element size and number
                                MW_options
            1 MW
                                enum                        of stored elements (see enum definition
                                                            at vec-mem-modes.h)
            2 IN1_V32           vec_t                       Input vector operand
            3 IN2_gB_BASE       void *                      Pointer register (gB)
Operands
                                                            Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                            base pointer
            5 IN3_PART          uint8         LOW,HIGH      Word part which is used for operand 4
                                                31   31     32 bit immediate post modification in
            6 IN4_PM_IMM        int32         -2 ..2 -1
                                                            bytes
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstb_v32_indexed_rIp_pm_imm_mw_h_concat (mw_8w, vIn, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic   vstb_v32_indexed_rIp_pm_ptr_mw_h_concat
name
Spec        vstb {mw [,h][,concat]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                MW_options                  Determines the element size and number
Operands    1 MW
                                enum                        of stored elements (see enum definition

at vec-mem-modes.h)
              2 IN1_V32           vec_t                        Input vector operand
              3 IN2_gB_BASE       void *                       Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the
              4 IN3_rI_OFFSET void *
                                                               base pointer
              5 IN3_PART          uint8         LOW,HIGH       Word part which is used for operand 4
              6 IN4_PM_PTR        void*                        Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec_t vIn;
              ...
              vstb_v32_indexed_rIp_pm_ptr_mw_h_concat (mw_8w, vIn, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic     vstb_v32_mw_h_concat
name
Spec syntax   vstb {mw [,h][,concat]} vix[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                              Determines the element size and number
                                MW_options
              1   MW
                                enum                          of stored elements (see enum definition at
                                                              vec-mem-modes.h)
Operands
              2   IN1_V32       vec_t                         Input vector operand
              3   IN2_PTR       void *                        Pointer register (rN)
              void* ptr;
              vec_t vIn;
C example     ...
              vstb_v32_mw_h_concat (mw_8w, vIn, ptr);

Comments



Intrinsic     vstb_v32_pm_imm_mw_h_concat
name
Spec          vstb {mw [,h][,concat]} vix[0], (pN)+#imm32_6 [,?prSC]
syntax
Return        void
type
                                                            Determines the element size and number
                              MW_options
            1   MW
                              enum                          of stored elements (see enum definition at
                                                            vec-mem-modes.h)

Operands    2   IN1_V32       vec_t                         Input vector operand
            3   IN2_PTR       void *                        Pointer register (rN)
                                               31   31      32 bit immediate post modification in
            4   IN3_IMM32_6 int32            -2 ..2 -1
                                                            bytes

void* ptr;
            vec_t vIn;
C example   ...
            vstb_v32_pm_imm_mw_h_concat (mw_8w, vIn, ptr, 2);

Comments



Intrinsic   vstb_v32_pm_ptr_mw_h_concat
name
Spec        vstb {mw [,h][,concat]} vix[0], (pN)[+pm_x] [,?prSC]
syntax
Return      void
type
                                                            Determines the element size and number
                              MW_options
            1   MW
                              enum                          of stored elements (see enum definition at
                                                            vec-mem-modes.h)
Operands    2   IN1_V32       vec_t                         Input vector operand
            3   IN2_PTR       void *                        Pointer register (rN)
            4   IN3_PM_PTR void*                            Pointer register (rN)
            void* ptr;
            vec_t vIn;
C example   ...
            vstb_v32_pm_ptr_mw_h_concat (mw_8w, vIn, ptr, ptr);

Comments


Main table → Memory Access → Store → Store 8 bit
Available addressing modes
Intrinsic Names:
vstb_v40_direct_pb
vstb_v40_indexed_imm_pb
vstb_v40_indexed_rI_pb
vstb_v40_indexed_rI_pm_imm_pb
vstb_v40_indexed_rI_pm_ptr_pb
vstb_v40_indexed_rIp_pb
vstb_v40_indexed_rIp_pm_imm_pb
vstb_v40_indexed_rIp_pm_ptr_pb
vstb_v40_pb
vstb_v40_pm_imm_pb
vstb_v40_pm_ptr_pb
Intrinsic     vstb_v40_direct_pb
name
Spec syntax   vstb {pb [,concat]} vox[0], [#address] [,?prSC]

Return        void
type
                                                                 Determines the element size and number
                                 PB_options
              1      PB
                                 enum                            of stored elements (see enum definition at
                                                                 vec-mem-modes.h)
Operands      2      IN1_V40     vec40_t                         Output vector operand

              3      IN1_OFST    uint8          0,4
                                                                 Offset for the first DW used from operand
                                                                 2
                                                      32
              4      IN2_ADDR    int32          0..2 -1          32 bit address
              vec40_t vIn;
C example     ...
              vstb_v40_direct_pb (pb_16b, vIn, 0, 2);

Comments



Intrinsic     vstb_v40_indexed_imm_pb
name
Spec          vstb {pb [,concat]} vox[0], (gB+#imm16_6) [,?prSC]

syntax
Return        void
type
                                                                 Determines the element size and number
                                   PB_options
              1   PB
                                   enum                          of stored elements (see enum definition
                                                                 at vec-mem-modes.h)
              2   IN1_V40          vec40_t                       Output vector operand
Operands                                                         Offset for the first DW used from
              3   IN1_OFST         uint8          0,4
                                                                 operand 2
              4   IN2_gB_BASE void *                             Pointer register (gB)
                                                  -              16 bit immediate post modification in
              5   IN3_IMM16_6      int16
                                                  32768..32767   bytes
              void* ptrBase;
              vec40_t vIn;
C example     ...
              vstb_v40_indexed_imm_pb (pb_16b, vIn, 0, ptrBase, 2);

Comments
Intrinsic   vstb_v40_indexed_rI_pb
name
Spec        vstb {pb [,concat]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                                Determines the element size and number
                                  PB_options
            1 PB
                                  enum                          of stored elements (see enum definition
                                                                at vec-mem-modes.h)
            2 IN1_V40             vec40_t                       Output vector operand
Operands                                                        Offset for the first DW used from
            3 IN1_OFST            uint8         0,4
                                                                operand 2
            4 IN2_gB_BASE         void *                        Pointer register (gB)
                                                                Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                                base pointer
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstb_v40_indexed_rI_pb (pb_16b, vIn, 0, ptrBase, ptrModify);

Comments



Intrinsic   vstb_v40_indexed_rI_pm_imm_pb
name

Spec        vstb {pb [,concat]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                                Determines the element size and number
                                  PB_options
            1 PB
                                  enum                          of stored elements (see enum definition
                                                                at vec-mem-modes.h)
            2 IN1_V40             vec40_t                       Output vector operand
Operands
                                                                Offset for the first DW used from
            3 IN1_OFST            uint8         0,4
                                                                operand 2
            4 IN2_gB_BASE         void *                        Pointer register (gB)
            5 IN3_rI_OFFSET void *                              Pointer (rI) specifying the offset from the
                                                                base pointer
                                                  31   31       32 bit immediate post modification in
            6 IN4_PM_IMM          int32         -2 ..2 -1
                                                                bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstb_v40_indexed_rI_pm_imm_pb (pb_16b, vIn, 0, ptrBase, ptrModify, 2);

Comments



Intrinsic   vstb_v40_indexed_rI_pm_ptr_pb
name
Spec        vstb {pb [,concat]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                                Determines the element size and number
                                  PB_options
            1 PB
                                  enum                          of stored elements (see enum definition
                                                                at vec-mem-modes.h)
            2 IN1_V40             vec40_t                       Output vector operand
                                                                Offset for the first DW used from
Operands    3 IN1_OFST            uint8         0,4
                                                                operand 2
            4 IN2_gB_BASE         void *                        Pointer register (gB)
                                                                Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *

base pointer
            6 IN4_PM_PTR          void*                         Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstb_v40_indexed_rI_pm_ptr_pb (pb_16b, vIn, 0, ptrBase, ptrModify, ptr);

Comments



Intrinsic   vstb_v40_indexed_rIp_pb
name
Spec        vstb {pb [,concat]} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and number
                                 PB_options
            1 PB
                                 enum                          of stored elements (see enum definition
                                                               at vec-mem-modes.h)
            2 IN1_V40            vec40_t                       Output vector operand
                                                               Offset for the first DW used from
            3 IN1_OFST           uint8          0,4
Operands                                                       operand 2
            4 IN2_gB_BASE        void *                        Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                               base pointer
            6 IN3_PART           uint8          LOW,HIGH       Word part which is used for operand 5
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstb_v40_indexed_rIp_pb (pb_16b, vIn, 0, ptrBase, ptrModify, LOW);

Comments



Intrinsic   vstb_v40_indexed_rIp_pm_imm_pb
name
Spec        vstb {pb [,concat]} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and number
                                 PB_options
            1 PB
                                 enum                          of stored elements (see enum definition
                                                               at vec-mem-modes.h)
            2 IN1_V40            vec40_t                       Output vector operand
                                                               Offset for the first DW used from
            3 IN1_OFST           uint8          0,4
                                                               operand 2

Operands    4 IN2_gB_BASE        void *                        Pointer register (gB)

            5 IN3_rI_OFFSET void *
                                                               Pointer (rI) specifying the offset from the
                                                               base pointer
            6 IN3_PART           uint8          LOW,HIGH       Word part which is used for operand 5

            7 IN4_PM_IMM                          31   31      32 bit immediate post modification in
                                 int32          -2 ..2 -1
                                                               bytes
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;
              ...
              vstb_v40_indexed_rIp_pm_imm_pb (pb_16b, vIn, 0, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic     vstb_v40_indexed_rIp_pm_ptr_pb
name
Spec          vstb {pb [,concat]} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return        void
type
                                                                 Determines the element size and number
                                   PB_options
              1 PB
                                   enum                          of stored elements (see enum definition
                                                                 at vec-mem-modes.h)
              2 IN1_V40            vec40_t                       Output vector operand
                                                                 Offset for the first DW used from
              3 IN1_OFST           uint8         0,4
                                                                 operand 2
Operands
              4 IN2_gB_BASE        void *                        Pointer register (gB)
                                                                 Pointer (rI) specifying the offset from the
              5 IN3_rI_OFFSET void *
                                                                 base pointer
              6 IN3_PART           uint8         LOW,HIGH        Word part which is used for operand 5
              7 IN4_PM_PTR         void*                         Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;
              ...
              vstb_v40_indexed_rIp_pm_ptr_pb (pb_16b, vIn, 0, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic     vstb_v40_pb
name

Spec syntax   vstb {pb [,concat]} vox[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                 PB_options
Operands      1      PB
                                 enum                           Determines the element size and number
                                                             of stored elements (see enum definition at
                                                             vec-mem-modes.h)
            2   IN1_V40         vec40_t                      Output vector operand

            3   IN1_OFST        uint8            0,4         Offset for the first DW used from operand
                                                             2

            4   IN2_PTR         void *                       Pointer register (rN)
            void* ptr;
            vec40_t vIn;
C example   ...
            vstb_v40_pb (pb_16b, vIn, 0, ptr);

Comments



Intrinsic   vstb_v40_pm_imm_pb
name
Spec        vstb {pb [,concat]} vox[0], (pN)+#imm32_6 [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                 PB_options
            1   PB
                                 enum                        of stored elements (see enum definition at
                                                             vec-mem-modes.h)
            2   IN1_V40          vec40_t                     Output vector operand
Operands    3   IN1_OFST         uint8                       Offset for the first DW used from operand
                                                 0,4
                                                             2

            4   IN2_PTR          void *                      Pointer register (rN)
                                                   31   31   32 bit immediate post modification in
            5   IN3_IMM32_6 int32                -2 ..2 -1
                                                             bytes
            void* ptr;
            vec40_t vIn;
C example   ...
            vstb_v40_pm_imm_pb (pb_16b, vIn, 0, ptr, 2);

Comments



Intrinsic   vstb_v40_pm_ptr_pb
name
Spec        vstb {pb [,concat]} vox[0], (pN)[+pm_x] [,?prSC]
syntax
Return        void
type
                                                               Determines the element size and number
                                  PB_options
              1   PB

enum                         of stored elements (see enum definition at
                                                               vec-mem-modes.h)
              2   IN1_V40         vec40_t                      Output vector operand
Operands
              3   IN1_OFST        uint8          0,4
                                                               Offset for the first DW used from operand
                                                               2

              4   IN2_PTR         void *                       Pointer register (rN)
              5   IN3_PM_PTR void*                             Pointer register (rN)
              void* ptr;
              vec40_t vIn;
C example     ...
              vstb_v40_pm_ptr_pb (pb_16b, vIn, 0, ptr, ptr);

Comments


Main table → Memory Access → Store → Store 8 bit
Available addressing modes
Intrinsic Names:
vstb_v40_direct_pb_concat
vstb_v40_indexed_imm_pb_concat
vstb_v40_indexed_rI_pb_concat
vstb_v40_indexed_rI_pm_imm_pb_concat
vstb_v40_indexed_rI_pm_ptr_pb_concat
vstb_v40_indexed_rIp_pb_concat
vstb_v40_indexed_rIp_pm_imm_pb_concat
vstb_v40_indexed_rIp_pm_ptr_pb_concat
vstb_v40_pb_concat
vstb_v40_pm_imm_pb_concat
vstb_v40_pm_ptr_pb_concat
Intrinsic     vstb_v40_direct_pb_concat
name
Spec syntax   vstb {pb [,concat]} vox[0], [#address] [,?prSC]

Return        void
type
                                                                Determines the element size and number
                                 PB_options
              1      PB
                                 enum                           of stored elements (see enum definition at
                                                                vec-mem-modes.h)
Operands      2      IN1_V40     vec40_t                        Output vector operand

              3      IN1_OFST    uint8          0,4
                                                                Offset for the first DW used from operand
                                                                2
                                                      32
              4      IN2_ADDR    int32          0..2 -1         32 bit address
              vec40_t vIn;
C example     ...
              vstb_v40_direct_pb_concat (pb_16b, vIn, 0, 2);

Comments



Intrinsic     vstb_v40_indexed_imm_pb_concat
name
Spec          vstb {pb [,concat]} vox[0], (gB+#imm16_6) [,?prSC]
syntax
Return        void
type

Determines the element size and number
                                  PB_options
              1   PB
                                  enum                          of stored elements (see enum definition
                                                                at vec-mem-modes.h)
              2   IN1_V40         vec40_t                       Output vector operand
Operands                                                        Offset for the first DW used from
              3   IN1_OFST        uint8          0,4
                                                                operand 2
              4   IN2_gB_BASE void *                            Pointer register (gB)
                                                 -              16 bit immediate post modification in
              5   IN3_IMM16_6     int16
                                                 32768..32767   bytes
              void* ptrBase;
              vec40_t vIn;
C example     ...
              vstb_v40_indexed_imm_pb_concat (pb_16b, vIn, 0, ptrBase, 2);

Comments
Intrinsic   vstb_v40_indexed_rI_pb_concat
name
Spec        vstb {pb [,concat]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and number
                                  PB_options
            1 PB
                                  enum                         of stored elements (see enum definition
                                                               at vec-mem-modes.h)
            2 IN1_V40             vec40_t                      Output vector operand
Operands                                                       Offset for the first DW used from
            3 IN1_OFST            uint8         0,4
                                                               operand 2
            4 IN2_gB_BASE         void *                       Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                               base pointer
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstb_v40_indexed_rI_pb_concat (pb_16b, vIn, 0, ptrBase, ptrModify);

Comments



Intrinsic   vstb_v40_indexed_rI_pm_imm_pb_concat
name
Spec        vstb {pb [,concat]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type

Determines the element size and number
                                  PB_options
            1 PB
                                  enum                         of stored elements (see enum definition
                                                               at vec-mem-modes.h)
            2 IN1_V40             vec40_t                      Output vector operand
Operands
                                                               Offset for the first DW used from
            3 IN1_OFST            uint8         0,4
                                                               operand 2
            4 IN2_gB_BASE         void *                       Pointer register (gB)
            5 IN3_rI_OFFSET void *                             Pointer (rI) specifying the offset from the
                                                               base pointer
                                                  31   31      32 bit immediate post modification in
            6 IN4_PM_IMM         int32          -2 ..2 -1
                                                               bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstb_v40_indexed_rI_pm_imm_pb_concat (pb_16b, vIn, 0, ptrBase, ptrModify, 2);

Comments



Intrinsic   vstb_v40_indexed_rI_pm_ptr_pb_concat
name
Spec        vstb {pb [,concat]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and number
                                 PB_options
            1 PB
                                 enum                          of stored elements (see enum definition
                                                               at vec-mem-modes.h)
            2 IN1_V40            vec40_t                       Output vector operand
                                                               Offset for the first DW used from
Operands    3 IN1_OFST           uint8          0,4
                                                               operand 2
            4 IN2_gB_BASE        void *                        Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                               base pointer
            6 IN4_PM_PTR         void*                         Pointer register (rN)

void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstb_v40_indexed_rI_pm_ptr_pb_concat (pb_16b, vIn, 0, ptrBase, ptrModify, ptr);

Comments



Intrinsic   vstb_v40_indexed_rIp_pb_concat
name
Spec        vstb {pb [,concat]} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 PB_options
            1 PB
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_V40            vec40_t                      Output vector operand
                                                              Offset for the first DW used from
            3 IN1_OFST           uint8         0,4
Operands                                                      operand 2
            4 IN2_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                              base pointer
            6 IN3_PART           uint8         LOW,HIGH       Word part which is used for operand 5
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstb_v40_indexed_rIp_pb_concat (pb_16b, vIn, 0, ptrBase, ptrModify, LOW);

Comments



Intrinsic   vstb_v40_indexed_rIp_pm_imm_pb_concat
name
Spec        vstb {pb [,concat]} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 PB_options
            1 PB
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_V40            vec40_t                      Output vector operand
                                                              Offset for the first DW used from
            3 IN1_OFST           uint8         0,4
                                                              operand 2
Operands    4 IN2_gB_BASE        void *                       Pointer register (gB)

5 IN3_rI_OFFSET void *
                                                              Pointer (rI) specifying the offset from the
                                                              base pointer
            6 IN3_PART           uint8         LOW,HIGH       Word part which is used for operand 5

            7 IN4_PM_IMM                         31   31      32 bit immediate post modification in
                                 int32         -2 ..2 -1
                                                              bytes
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;
              ...
              vstb_v40_indexed_rIp_pm_imm_pb_concat (pb_16b, vIn, 0, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic     vstb_v40_indexed_rIp_pm_ptr_pb_concat
name
Spec          vstb {pb [,concat]} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return        void
type
                                                                Determines the element size and number
                                   PB_options
              1 PB
                                   enum                         of stored elements (see enum definition
                                                                at vec-mem-modes.h)
              2 IN1_V40            vec40_t                      Output vector operand
                                                                Offset for the first DW used from
              3 IN1_OFST           uint8         0,4
                                                                operand 2
Operands
              4 IN2_gB_BASE        void *                       Pointer register (gB)
                                                                Pointer (rI) specifying the offset from the
              5 IN3_rI_OFFSET void *
                                                                base pointer
              6 IN3_PART           uint8         LOW,HIGH       Word part which is used for operand 5
              7 IN4_PM_PTR         void*                        Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;
              ...
              vstb_v40_indexed_rIp_pm_ptr_pb_concat (pb_16b, vIn, 0, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic     vstb_v40_pb_concat
name
Spec syntax   vstb {pb [,concat]} vox[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                 PB_options

Operands      1      PB
                                 enum                          Determines the element size and number
                                                             of stored elements (see enum definition at
                                                             vec-mem-modes.h)
            2   IN1_V40        vec40_t                       Output vector operand

            3   IN1_OFST       uint8          0,4            Offset for the first DW used from operand
                                                             2

            4   IN2_PTR        void *                        Pointer register (rN)
            void* ptr;
            vec40_t vIn;
C example   ...
            vstb_v40_pb_concat (pb_16b, vIn, 0, ptr);

Comments



Intrinsic   vstb_v40_pm_imm_pb_concat
name
Spec        vstb {pb [,concat]} vox[0], (pN)+#imm32_6 [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                PB_options
            1   PB
                                enum                         of stored elements (see enum definition at
                                                             vec-mem-modes.h)
            2   IN1_V40         vec40_t                      Output vector operand
Operands    3   IN1_OFST        uint8                        Offset for the first DW used from operand
                                               0,4
                                                             2

            4   IN2_PTR         void *                       Pointer register (rN)
                                                 31     31   32 bit immediate post modification in
            5   IN3_IMM32_6 int32              -2 ..2 -1
                                                             bytes
            void* ptr;
            vec40_t vIn;
C example   ...
            vstb_v40_pm_imm_pb_concat (pb_16b, vIn, 0, ptr, 2);

Comments



Intrinsic   vstb_v40_pm_ptr_pb_concat
name
Spec        vstb {pb [,concat]} vox[0], (pN)[+pm_x] [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and number
                                PB_options
            1   PB
                                enum                           of stored elements (see enum definition at
                                                               vec-mem-modes.h)

2   IN1_V40         vec40_t                        Output vector operand
Operands
            3   IN1_OFST        uint8          0,4
                                                               Offset for the first DW used from operand
                                                               2

            4   IN2_PTR         void *                         Pointer register (rN)
            5   IN3_PM_PTR void*                               Pointer register (rN)
            void* ptr;
            vec40_t vIn;
C example   ...
            vstb_v40_pm_ptr_pb_concat (pb_16b, vIn, 0, ptr, ptr);

Comments


Main table → Memory Access → Store → Store 8 bit
Available addressing modes
Intrinsic Names:
vstb_v40_indexed_rI_mw_vuX
vstb_v40_indexed_rI_pm_imm_mw_vuX
vstb_v40_indexed_rI_pm_ptr_mw_vuX
vstb_v40_indexed_rIp_mw_vuX
vstb_v40_indexed_rIp_pm_imm_mw_vuX
vstb_v40_indexed_rIp_pm_ptr_mw_vuX
vstb_v40_mw_vuX
vstb_v40_pm_imm_mw_vuX
vstb_v40_pm_ptr_mw_vuX
Intrinsic   vstb_v40_indexed_rI_mw_vuX
name
Spec        vstb {mw, vuX [,h]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                MW_options
            1 MW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
            2 VUX               uint8          0..3          Determines the source VCU
Operands    3 IN1_V40           vec40_t                      Output vector operand
            4 IN2_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                             base pointer
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstb_v40_indexed_rI_mw_vuX (mw_8w, 1, vIn, ptrBase, ptrModify);

Comments



Intrinsic   vstb_v40_indexed_rI_pm_imm_mw_vuX
name
Spec        vstb {mw, vuX [,h]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                MW_options
            1 MW
                                enum                         of stored elements (see enum definition

at vec-mem-modes.h)
            2 VUX               uint8          0..3          Determines the source VCU
            3 IN1_V40           vec40_t                      Output vector operand
Operands
            4 IN2_gB_BASE       void *                       Pointer register (gB)

            5 IN3_rI_OFFSET void *
                                                             Pointer (rI) specifying the offset from the
                                                             base pointer

            6 IN4_PM_IMM                         31   31     32 bit immediate post modification in
                                int32          -2 ..2 -1
                                                             bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstb_v40_indexed_rI_pm_imm_mw_vuX (mw_8w, 1, vIn, ptrBase, ptrModify, 2);

Comments



Intrinsic   vstb_v40_indexed_rI_pm_ptr_mw_vuX
name
Spec        vstb {mw, vuX [,h]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                MW_options
            1 MW
                                enum                          of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 VUX               uint8          0..3           Determines the source VCU

Operands    3 IN1_V40           vec40_t                       Output vector operand
            4 IN2_gB_BASE       void *                        Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                              base pointer
            6 IN4_PM_PTR        void*                         Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstb_v40_indexed_rI_pm_ptr_mw_vuX (mw_8w, 1, vIn, ptrBase, ptrModify, ptr);

Comments



Intrinsic   vstb_v40_indexed_rIp_mw_vuX
name
Spec        vstb {mw,vuX [,h]} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                MW_options
Operands    1 MW

enum                          of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 VUX               uint8         0..3          Determines the source VCU
            3 IN1_V40           vec40_t                     Output vector operand
            4 IN2_gB_BASE       void *                      Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                            base pointer
            6 IN3_PART          uint8         LOW,HIGH      Word part which is used for operand 5
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstb_v40_indexed_rIp_mw_vuX (mw_8w, 1, vIn, ptrBase, ptrModify, LOW);

Comments



Intrinsic   vstb_v40_indexed_rIp_pm_imm_mw_vuX
name
Spec        vstb {mw,vuX [,h]} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                            Determines the element size and number
                                MW_options
            1 MW
                                enum                        of stored elements (see enum definition
                                                            at vec-mem-modes.h)
            2 VUX               uint8         0..3          Determines the source VCU
            3 IN1_V40           vec40_t                     Output vector operand
Operands    4 IN2_gB_BASE       void *                      Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                            base pointer
            6 IN3_PART          uint8         LOW,HIGH      Word part which is used for operand 5

            7 IN4_PM_IMM                        31   31     32 bit immediate post modification in
                                int32         -2 ..2 -1
                                                            bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstb_v40_indexed_rIp_pm_imm_mw_vuX (mw_8w, 1, vIn, ptrBase, ptrModify, LOW, 2);

Comments
Intrinsic     vstb_v40_indexed_rIp_pm_ptr_mw_vuX
name
Spec          vstb {mw,vuX [,h]} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax

Return        void
type
                                                               Determines the element size and number
                                  MW_options
              1 MW
                                  enum                         of stored elements (see enum definition
                                                               at vec-mem-modes.h)
              2 VUX               uint8          0..3          Determines the source VCU
              3 IN1_V40           vec40_t                      Output vector operand
Operands      4 IN2_gB_BASE       void *                       Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the
              5 IN3_rI_OFFSET void *
                                                               base pointer
              6 IN3_PART          uint8          LOW,HIGH      Word part which is used for operand 5
              7 IN4_PM_PTR        void*                        Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;
              ...
              vstb_v40_indexed_rIp_pm_ptr_mw_vuX (mw_8w, 1, vIn, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic     vstb_v40_mw_vuX
name
Spec syntax   vstb {mw, vuX [,h]} vox[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                              Determines the element size and number
                                MW_options
              1      MW
                                enum                          of stored elements (see enum definition at
                                                              vec-mem-modes.h)
Operands      2      VUX        uint8          0..3           Determines the source VCU
              3      IN1_V40    vec40_t                       Output vector operand
              4      IN2_PTR    void *                        Pointer register (rN)
              void* ptr;
C example     vec40_t vIn;
              ...
              vstb_v40_mw_vuX (mw_8w, 1, vIn, ptr);

Comments



Intrinsic     vstb_v40_pm_imm_mw_vuX
name
Spec syntax   vstb {mw, vuX [,h]} vox[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                            Determines the element size and number
                                MW_options
              1   MW

enum                        of stored elements (see enum definition at
                                                            vec-mem-modes.h)
              2   VUX           uint8          0..3         Determines the source VCU
Operands      3   IN1_V40       vec40_t                     Output vector operand
              4   IN2_PTR       void *                      Pointer register (rN)
                                                 31   31    32 bit immediate post modification in
              5   IN3_PM_IMM int32             -2 ..2 -1
                                                            bytes
              void* ptr;
              vec40_t vIn;
C example     ...
              vstb_v40_pm_imm_mw_vuX (mw_8w, 1, vIn, ptr, 2);

Comments



Intrinsic     vstb_v40_pm_ptr_mw_vuX
name
Spec          vstb {mw, vuX [,h]} vox[0], (pN)[+pm_x] [,?prSC]
syntax
Return        void
type
                                                            Determines the element size and number
                                MW_options
              1   MW
                                enum                        of stored elements (see enum definition at
                                                            vec-mem-modes.h)
              2   VUX           uint8          0..3         Determines the source VCU
Operands
              3   IN1_V40       vec40_t                     Output vector operand
              4   IN2_PTR       void *                      Pointer register (rN)
              5   IN3_PM_PTR void*                          Pointer register (rN)
             void* ptr;
             vec40_t vIn;
C example    ...
             vstb_v40_pm_ptr_mw_vuX (mw_8w, 1, vIn, ptr, ptr);

Comments


Main table → Memory Access → Store → Store 8 bit
Available addressing modes
Intrinsic Names:
vstb_v40_indexed_rI_mw_vuX_h
vstb_v40_indexed_rI_pm_imm_mw_vuX_h
vstb_v40_indexed_rI_pm_ptr_mw_vuX_h
vstb_v40_indexed_rIp_mw_vuX_h
vstb_v40_indexed_rIp_pm_imm_mw_vuX_h
vstb_v40_indexed_rIp_pm_ptr_mw_vuX_h
vstb_v40_mw_vuX_h
vstb_v40_pm_imm_mw_vuX_h
vstb_v40_pm_ptr_mw_vuX_h
Intrinsic   vstb_v40_indexed_rI_mw_vuX_h
name
Spec        vstb {mw, vuX [,h]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                MW_options
            1 MW
                                enum                         of stored elements (see enum definition

at vec-mem-modes.h)
            2 VUX               uint8          0..3          Determines the source VCU
Operands    3 IN1_V40           vec40_t                      Output vector operand
            4 IN2_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                             base pointer
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstb_v40_indexed_rI_mw_vuX_h (mw_8w, 1, vIn, ptrBase, ptrModify);

Comments



Intrinsic   vstb_v40_indexed_rI_pm_imm_mw_vuX_h
name
Spec        vstb {mw, vuX [,h]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                MW_options
            1 MW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
            2 VUX               uint8          0..3          Determines the source VCU
            3 IN1_V40           vec40_t                      Output vector operand
Operands
            4 IN2_gB_BASE       void *                       Pointer register (gB)

            5 IN3_rI_OFFSET void *
                                                             Pointer (rI) specifying the offset from the
                                                             base pointer

            6 IN4_PM_IMM                         31   31     32 bit immediate post modification in
                                int32          -2 ..2 -1
                                                             bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstb_v40_indexed_rI_pm_imm_mw_vuX_h (mw_8w, 1, vIn, ptrBase, ptrModify, 2);

Comments



Intrinsic   vstb_v40_indexed_rI_pm_ptr_mw_vuX_h
name
Spec        vstb {mw, vuX [,h]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                MW_options
            1 MW
                                enum                         of stored elements (see enum definition

at vec-mem-modes.h)
            2 VUX               uint8          0..3          Determines the source VCU

Operands    3 IN1_V40           vec40_t                      Output vector operand
            4 IN2_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                             base pointer
            6 IN4_PM_PTR        void*                        Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstb_v40_indexed_rI_pm_ptr_mw_vuX_h (mw_8w, 1, vIn, ptrBase, ptrModify, ptr);

Comments



Intrinsic   vstb_v40_indexed_rIp_mw_vuX_h
name
Spec        vstb {mw,vuX [,h]} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                MW_options
Operands    1 MW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
            2 VUX               uint8         0..3          Determines the source VCU
            3 IN1_V40           vec40_t                     Output vector operand
            4 IN2_gB_BASE       void *                      Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                            base pointer
            6 IN3_PART          uint8         LOW,HIGH      Word part which is used for operand 5
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstb_v40_indexed_rIp_mw_vuX_h (mw_8w, 1, vIn, ptrBase, ptrModify, LOW);

Comments



Intrinsic   vstb_v40_indexed_rIp_pm_imm_mw_vuX_h
name
Spec        vstb {mw,vuX [,h]} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                            Determines the element size and number
                                MW_options
            1 MW
                                enum                        of stored elements (see enum definition

at vec-mem-modes.h)
            2 VUX               uint8         0..3          Determines the source VCU
            3 IN1_V40           vec40_t                     Output vector operand
Operands    4 IN2_gB_BASE       void *                      Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                            base pointer
            6 IN3_PART          uint8         LOW,HIGH      Word part which is used for operand 5

            7 IN4_PM_IMM                        31   31     32 bit immediate post modification in
                                int32         -2 ..2 -1
                                                            bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstb_v40_indexed_rIp_pm_imm_mw_vuX_h (mw_8w, 1, vIn, ptrBase, ptrModify, LOW, 2);

Comments
Intrinsic     vstb_v40_indexed_rIp_pm_ptr_mw_vuX_h
name
Spec          vstb {mw,vuX [,h]} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return        void
type
                                                               Determines the element size and number
                                  MW_options
              1 MW
                                  enum                         of stored elements (see enum definition
                                                               at vec-mem-modes.h)
              2 VUX               uint8         0..3           Determines the source VCU
              3 IN1_V40           vec40_t                      Output vector operand
Operands      4 IN2_gB_BASE       void *                       Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the
              5 IN3_rI_OFFSET void *
                                                               base pointer
              6 IN3_PART          uint8         LOW,HIGH       Word part which is used for operand 5
              7 IN4_PM_PTR        void*                        Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;
              ...
              vstb_v40_indexed_rIp_pm_ptr_mw_vuX_h (mw_8w, 1, vIn, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic     vstb_v40_mw_vuX_h
name

Spec syntax   vstb {mw, vuX [,h]} vox[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                              Determines the element size and number
                                MW_options
              1      MW
                                enum                          of stored elements (see enum definition at
                                                              vec-mem-modes.h)
Operands      2      VUX        uint8          0..3           Determines the source VCU
              3      IN1_V40    vec40_t                       Output vector operand
              4      IN2_PTR    void *                        Pointer register (rN)
              void* ptr;
C example     vec40_t vIn;
              ...
              vstb_v40_mw_vuX_h (mw_8w, 1, vIn, ptr);

Comments



Intrinsic     vstb_v40_pm_imm_mw_vuX_h
name
Spec syntax   vstb {mw, vuX [,h]} vox[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                             Determines the element size and number
                                MW_options
              1   MW
                                enum                         of stored elements (see enum definition at
                                                             vec-mem-modes.h)
              2   VUX           uint8          0..3          Determines the source VCU
Operands      3   IN1_V40       vec40_t                      Output vector operand
              4   IN2_PTR       void *                       Pointer register (rN)
                                                 31     31   32 bit immediate post modification in
              5   IN3_PM_IMM int32             -2 ..2 -1
                                                             bytes
              void* ptr;
              vec40_t vIn;
C example     ...
              vstb_v40_pm_imm_mw_vuX_h (mw_8w, 1, vIn, ptr, 2);

Comments



Intrinsic     vstb_v40_pm_ptr_mw_vuX_h
name
Spec          vstb {mw, vuX [,h]} vox[0], (pN)[+pm_x] [,?prSC]
syntax
Return        void
type
                                                             Determines the element size and number
                                MW_options
              1   MW
                                enum                         of stored elements (see enum definition at
                                                             vec-mem-modes.h)

2   VUX           uint8         0..3           Determines the source VCU
Operands
              3   IN1_V40       vec40_t                      Output vector operand
              4   IN2_PTR       void *                       Pointer register (rN)
              5   IN3_PM_PTR void*                           Pointer register (rN)
            void* ptr;
            vec40_t vIn;
C example   ...
            vstb_v40_pm_ptr_mw_vuX_h (mw_8w, 1, vIn, ptr, ptr);

Comments


Main table → Memory Access → Store → Store 8 bit
Available addressing modes
Intrinsic Names:
vstb_v40_direct_mw
vstb_v40_indexed_imm_mw
vstb_v40_indexed_rI_mw
vstb_v40_indexed_rI_pm_imm_mw
vstb_v40_indexed_rI_pm_ptr_mw
vstb_v40_indexed_rIp_mw
vstb_v40_indexed_rIp_pm_imm_mw
vstb_v40_indexed_rIp_pm_ptr_mw
vstb_v40_mw
vstb_v40_pm_imm_mw
vstb_v40_pm_ptr_mw
Intrinsic     vstb_v40_direct_mw
name
Spec syntax   vstb {mw [,h][,concat]} vox[0], [#address] [,?prSC]

Return        void
type
                                                              Determines the element size and number
                                MW_options
              1      MW
                                enum                          of stored elements (see enum definition at
                                                              vec-mem-modes.h)
Operands
              2      IN1_V40    vec40_t                       Output vector operand
                                                    32
              3      IN2_ADDR   int32         0..2 -1         32 bit address
              vec40_t vIn;
C example     ...
              vstb_v40_direct_mw (mw_8w, vIn, 2);

Comments



Intrinsic     vstb_v40_indexed_imm_mw
name
Spec          vstb {mw [,h][,concat]} vox[0], (gB+#imm16_6) [,?prSC]
syntax
Return        void
type
                                                              Determines the element size and number
                                 MW_options
              1 MW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)

Operands      2 IN1_V40          vec40_t                      Output vector operand
              3 IN2_gB_BASE void *                            Pointer register (gB)

              4 IN3_IMM16_6
                                               -              16 bit immediate post modification in
                                 int16

32768..32767   bytes
              void* ptrBase;
              vec40_t vIn;
C example     ...
              vstb_v40_indexed_imm_mw (mw_8w, vIn, ptrBase, 2);

Comments



Intrinsic     vstb_v40_indexed_rI_mw
name
Spec          vstb {mw [,h][,concat]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                MW_options
            1 MW
                                enum                          of stored elements (see enum definition
                                                              at vec-mem-modes.h)

Operands    2 IN1_V40           vec40_t                       Output vector operand
            3 IN2_gB_BASE       void *                        Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                              base pointer
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstb_v40_indexed_rI_mw (mw_8w, vIn, ptrBase, ptrModify);

Comments



Intrinsic   vstb_v40_indexed_rI_pm_imm_mw
name
Spec        vstb {mw [,h][,concat]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                MW_options
            1 MW
                                enum                          of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_V40           vec40_t                       Output vector operand
Operands    3 IN2_gB_BASE       void *                        Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                              base pointer
                                                 31   31      32 bit immediate post modification in
            5 IN4_PM_IMM        int32          -2 ..2 -1
                                                              bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstb_v40_indexed_rI_pm_imm_mw (mw_8w, vIn, ptrBase, ptrModify, 2);

Comments
Intrinsic   vstb_v40_indexed_rI_pm_ptr_mw
name
Spec        vstb {mw [,h][,concat]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                MW_options
            1 MW
                                enum                          of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_V40           vec40_t                       Output vector operand
Operands    3 IN2_gB_BASE       void *                        Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                              base pointer
            5 IN4_PM_PTR        void*                         Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstb_v40_indexed_rI_pm_ptr_mw (mw_8w, vIn, ptrBase, ptrModify, ptr);

Comments



Intrinsic   vstb_v40_indexed_rIp_mw
name
Spec        vstb {mw [,h][,concat]} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                MW_options
            1 MW
                                enum                          of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_V40           vec40_t                       Output vector operand
Operands    3 IN2_gB_BASE       void *                        Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                              base pointer
            5 IN3_PART          uint8          LOW,HIGH       Word part which is used for operand 4
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstb_v40_indexed_rIp_mw (mw_8w, vIn, ptrBase, ptrModify, LOW);

Comments



Intrinsic   vstb_v40_indexed_rIp_pm_imm_mw
name
Spec        vstb {mw [,h][,concat]} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type

Determines the element size and number
                                MW_options
            1 MW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
            2 IN1_V40           vec40_t                      Output vector operand
            3 IN2_gB_BASE       void *                       Pointer register (gB)
Operands
                                                             Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                             base pointer
            5 IN3_PART          uint8         LOW,HIGH       Word part which is used for operand 4
                                                31   31      32 bit immediate post modification in
            6 IN4_PM_IMM        int32         -2 ..2 -1
                                                             bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstb_v40_indexed_rIp_pm_imm_mw (mw_8w, vIn, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic   vstb_v40_indexed_rIp_pm_ptr_mw
name
Spec        vstb {mw [,h][,concat]} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                MW_options                   Determines the element size and number
Operands    1 MW
                                enum                         of stored elements (see enum definition
                                                               at vec-mem-modes.h)
              2 IN1_V40           vec40_t                      Output vector operand
              3 IN2_gB_BASE       void *                       Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the
              4 IN3_rI_OFFSET void *
                                                               base pointer
              5 IN3_PART          uint8          LOW,HIGH      Word part which is used for operand 4
              6 IN4_PM_PTR        void*                        Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;
              ...
              vstb_v40_indexed_rIp_pm_ptr_mw (mw_8w, vIn, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic     vstb_v40_mw
name

Spec syntax   vstb {mw [,h][,concat]} vox[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                              Determines the element size and number
                                MW_options
              1   MW
                                enum                          of stored elements (see enum definition at
                                                              vec-mem-modes.h)
Operands
              2   IN1_V40       vec40_t                       Output vector operand
              3   IN2_PTR       void *                        Pointer register (rN)
              void* ptr;
              vec40_t vIn;
C example     ...
              vstb_v40_mw (mw_8w, vIn, ptr);

Comments



Intrinsic     vstb_v40_pm_imm_mw
name
Spec          vstb {mw [,h][,concat]} vox[0], (pN)+#imm32_6 [,?prSC]
syntax
Return        void
type
                                                           Determines the element size and number
                                MW_options
             1   MW
                                enum                       of stored elements (see enum definition at
                                                           vec-mem-modes.h)

Operands     2   IN1_V40        vec40_t                    Output vector operand
             3   IN2_PTR        void *                     Pointer register (rN)
                                                31   31    32 bit immediate post modification in
             4   IN3_IMM32_6 int32            -2 ..2 -1
                                                           bytes
             void* ptr;
             vec40_t vIn;
C example    ...
             vstb_v40_pm_imm_mw (mw_8w, vIn, ptr, 2);

Comments



Intrinsic    vstb_v40_pm_ptr_mw
name
Spec         vstb {mw [,h][,concat]} vox[0], (pN)[+pm_x] [,?prSC]
syntax
Return       void
type
                                                           Determines the element size and number
                                MW_options
             1   MW
                                enum                       of stored elements (see enum definition at
                                                           vec-mem-modes.h)
Operands     2   IN1_V40        vec40_t                    Output vector operand
             3   IN2_PTR        void *                     Pointer register (rN)
             4   IN3_PM_PTR void*                          Pointer register (rN)
             void* ptr;

vec40_t vIn;
C example    ...
             vstb_v40_pm_ptr_mw (mw_8w, vIn, ptr, ptr);

Comments


Main table → Memory Access → Store → Store 8 bit
Available addressing modes
Intrinsic Names:
vstb_v40_direct_mw_concat
vstb_v40_indexed_imm_mw_concat
vstb_v40_indexed_rI_mw_concat
vstb_v40_indexed_rI_pm_imm_mw_concat
vstb_v40_indexed_rI_pm_ptr_mw_concat
vstb_v40_indexed_rIp_mw_concat
vstb_v40_indexed_rIp_pm_imm_mw_concat
vstb_v40_indexed_rIp_pm_ptr_mw_concat
vstb_v40_mw_concat
vstb_v40_pm_imm_mw_concat
vstb_v40_pm_ptr_mw_concat
Intrinsic     vstb_v40_direct_mw_concat
name
Spec syntax   vstb {mw [,h][,concat]} vox[0], [#address] [,?prSC]

Return        void
type
                                                              Determines the element size and number
                                MW_options
              1      MW
                                enum                          of stored elements (see enum definition at
                                                              vec-mem-modes.h)
Operands
              2      IN1_V40    vec40_t                       Output vector operand
                                                  32
              3      IN2_ADDR   int32         0..2 -1         32 bit address
              vec40_t vIn;
C example     ...
              vstb_v40_direct_mw_concat (mw_8w, vIn, 2);

Comments



Intrinsic     vstb_v40_indexed_imm_mw_concat
name
Spec          vstb {mw [,h][,concat]} vox[0], (gB+#imm16_6) [,?prSC]
syntax
Return        void
type
                                                              Determines the element size and number
                                 MW_options
              1 MW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)

Operands      2 IN1_V40          vec40_t                      Output vector operand
              3 IN2_gB_BASE void *                            Pointer register (gB)

              4 IN3_IMM16_6
                                               -              16 bit immediate post modification in
                                 int16
                                               32768..32767   bytes
              void* ptrBase;
              vec40_t vIn;
C example     ...
              vstb_v40_indexed_imm_mw_concat (mw_8w, vIn, ptrBase, 2);

Comments



Intrinsic     vstb_v40_indexed_rI_mw_concat
name

Spec          vstb {mw [,h][,concat]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                MW_options
            1 MW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)

Operands    2 IN1_V40           vec40_t                      Output vector operand
            3 IN2_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                             base pointer
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstb_v40_indexed_rI_mw_concat (mw_8w, vIn, ptrBase, ptrModify);

Comments



Intrinsic   vstb_v40_indexed_rI_pm_imm_mw_concat
name
Spec        vstb {mw [,h][,concat]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                MW_options
            1 MW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
            2 IN1_V40           vec40_t                      Output vector operand
Operands    3 IN2_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                             base pointer
                                                 31   31     32 bit immediate post modification in
            5 IN4_PM_IMM        int32          -2 ..2 -1
                                                             bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstb_v40_indexed_rI_pm_imm_mw_concat (mw_8w, vIn, ptrBase, ptrModify, 2);

Comments
Intrinsic   vstb_v40_indexed_rI_pm_ptr_mw_concat
name
Spec        vstb {mw [,h][,concat]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type

Determines the element size and number
                                MW_options
            1 MW
                                enum                          of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_V40           vec40_t                       Output vector operand
Operands    3 IN2_gB_BASE       void *                        Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                              base pointer
            5 IN4_PM_PTR        void*                         Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstb_v40_indexed_rI_pm_ptr_mw_concat (mw_8w, vIn, ptrBase, ptrModify, ptr);

Comments



Intrinsic   vstb_v40_indexed_rIp_mw_concat
name
Spec        vstb {mw [,h][,concat]} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                MW_options
            1 MW
                                enum                          of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_V40           vec40_t                       Output vector operand
Operands    3 IN2_gB_BASE       void *                        Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                              base pointer
            5 IN3_PART          uint8          LOW,HIGH       Word part which is used for operand 4
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstb_v40_indexed_rIp_mw_concat (mw_8w, vIn, ptrBase, ptrModify, LOW);

Comments



Intrinsic   vstb_v40_indexed_rIp_pm_imm_mw_concat
name
Spec        vstb {mw [,h][,concat]} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                            Determines the element size and number
                                MW_options
            1 MW

enum                        of stored elements (see enum definition
                                                            at vec-mem-modes.h)
            2 IN1_V40           vec40_t                     Output vector operand
            3 IN2_gB_BASE       void *                      Pointer register (gB)
Operands
                                                            Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                            base pointer
            5 IN3_PART          uint8         LOW,HIGH      Word part which is used for operand 4
                                                31   31     32 bit immediate post modification in
            6 IN4_PM_IMM        int32         -2 ..2 -1
                                                            bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstb_v40_indexed_rIp_pm_imm_mw_concat (mw_8w, vIn, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic   vstb_v40_indexed_rIp_pm_ptr_mw_concat
name
Spec        vstb {mw [,h][,concat]} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                MW_options                  Determines the element size and number
Operands    1 MW
                                enum                        of stored elements (see enum definition
                                                               at vec-mem-modes.h)
              2 IN1_V40           vec40_t                      Output vector operand
              3 IN2_gB_BASE       void *                       Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the
              4 IN3_rI_OFFSET void *
                                                               base pointer
              5 IN3_PART          uint8          LOW,HIGH      Word part which is used for operand 4
              6 IN4_PM_PTR        void*                        Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;
              ...
              vstb_v40_indexed_rIp_pm_ptr_mw_concat (mw_8w, vIn, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic     vstb_v40_mw_concat
name
Spec syntax   vstb {mw [,h][,concat]} vox[0], (pN)[+pm_x] [,?prSC]

Return        void
type

Determines the element size and number
                                MW_options
              1   MW
                                enum                          of stored elements (see enum definition at
                                                              vec-mem-modes.h)
Operands
              2   IN1_V40       vec40_t                       Output vector operand
              3   IN2_PTR       void *                        Pointer register (rN)
              void* ptr;
              vec40_t vIn;
C example     ...
              vstb_v40_mw_concat (mw_8w, vIn, ptr);

Comments



Intrinsic     vstb_v40_pm_imm_mw_concat
name
Spec          vstb {mw [,h][,concat]} vox[0], (pN)+#imm32_6 [,?prSC]
syntax
Return        void
type
                                                             Determines the element size and number
                                MW_options
             1   MW
                                enum                         of stored elements (see enum definition at
                                                             vec-mem-modes.h)

Operands     2   IN1_V40        vec40_t                      Output vector operand
             3   IN2_PTR        void *                       Pointer register (rN)
                                                31   31      32 bit immediate post modification in
             4   IN3_IMM32_6 int32            -2 ..2 -1
                                                             bytes
             void* ptr;
             vec40_t vIn;
C example    ...
             vstb_v40_pm_imm_mw_concat (mw_8w, vIn, ptr, 2);

Comments



Intrinsic    vstb_v40_pm_ptr_mw_concat
name
Spec         vstb {mw [,h][,concat]} vox[0], (pN)[+pm_x] [,?prSC]
syntax
Return       void
type
                                                             Determines the element size and number
                               MW_options
             1   MW
                               enum                          of stored elements (see enum definition at
                                                             vec-mem-modes.h)
Operands     2   IN1_V40       vec40_t                       Output vector operand
             3   IN2_PTR       void *                        Pointer register (rN)
             4   IN3_PM_PTR void*                            Pointer register (rN)
             void* ptr;
             vec40_t vIn;
C example    ...
             vstb_v40_pm_ptr_mw_concat (mw_8w, vIn, ptr, ptr);

Comments

Main table → Memory Access → Store → Store 8 bit
Available addressing modes
Intrinsic Names:
vstb_v40_direct_mw_h
vstb_v40_indexed_imm_mw_h
vstb_v40_indexed_rI_mw_h
vstb_v40_indexed_rI_pm_imm_mw_h
vstb_v40_indexed_rI_pm_ptr_mw_h
vstb_v40_indexed_rIp_mw_h
vstb_v40_indexed_rIp_pm_imm_mw_h
vstb_v40_indexed_rIp_pm_ptr_mw_h
vstb_v40_mw_h
vstb_v40_pm_imm_mw_h
vstb_v40_pm_ptr_mw_h
Intrinsic     vstb_v40_direct_mw_h
name
Spec syntax   vstb {mw [,h][,concat]} vox[0], [#address] [,?prSC]

Return        void
type
                                                              Determines the element size and number
                                MW_options
              1      MW
                                enum                          of stored elements (see enum definition at
                                                              vec-mem-modes.h)
Operands
              2      IN1_V40    vec40_t                       Output vector operand
                                                  32
              3      IN2_ADDR   int32         0..2 -1         32 bit address
              vec40_t vIn;
C example     ...
              vstb_v40_direct_mw_h (mw_8w, vIn, 2);

Comments



Intrinsic     vstb_v40_indexed_imm_mw_h
name
Spec          vstb {mw [,h][,concat]} vox[0], (gB+#imm16_6) [,?prSC]
syntax
Return        void
type
                                                              Determines the element size and number
                                 MW_options
              1 MW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)

Operands      2 IN1_V40          vec40_t                      Output vector operand
              3 IN2_gB_BASE void *                            Pointer register (gB)

              4 IN3_IMM16_6
                                               -              16 bit immediate post modification in
                                 int16
                                               32768..32767   bytes
              void* ptrBase;
              vec40_t vIn;
C example     ...
              vstb_v40_indexed_imm_mw_h (mw_8w, vIn, ptrBase, 2);

Comments



Intrinsic     vstb_v40_indexed_rI_mw_h
name
Spec          vstb {mw [,h][,concat]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number

MW_options
            1 MW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)

Operands    2 IN1_V40           vec40_t                      Output vector operand
            3 IN2_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                             base pointer
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstb_v40_indexed_rI_mw_h (mw_8w, vIn, ptrBase, ptrModify);

Comments



Intrinsic   vstb_v40_indexed_rI_pm_imm_mw_h
name
Spec        vstb {mw [,h][,concat]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                MW_options
            1 MW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
            2 IN1_V40           vec40_t                      Output vector operand
Operands    3 IN2_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                             base pointer
                                                 31   31     32 bit immediate post modification in
            5 IN4_PM_IMM        int32          -2 ..2 -1
                                                             bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstb_v40_indexed_rI_pm_imm_mw_h (mw_8w, vIn, ptrBase, ptrModify, 2);

Comments
Intrinsic   vstb_v40_indexed_rI_pm_ptr_mw_h
name
Spec        vstb {mw [,h][,concat]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                MW_options
            1 MW
                                enum                          of stored elements (see enum definition

at vec-mem-modes.h)
            2 IN1_V40           vec40_t                       Output vector operand
Operands    3 IN2_gB_BASE       void *                        Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                              base pointer
            5 IN4_PM_PTR        void*                         Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstb_v40_indexed_rI_pm_ptr_mw_h (mw_8w, vIn, ptrBase, ptrModify, ptr);

Comments



Intrinsic   vstb_v40_indexed_rIp_mw_h
name
Spec        vstb {mw [,h][,concat]} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                MW_options
            1 MW
                                enum                          of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_V40           vec40_t                       Output vector operand
Operands    3 IN2_gB_BASE       void *                        Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                              base pointer
            5 IN3_PART          uint8          LOW,HIGH       Word part which is used for operand 4
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstb_v40_indexed_rIp_mw_h (mw_8w, vIn, ptrBase, ptrModify, LOW);

Comments



Intrinsic   vstb_v40_indexed_rIp_pm_imm_mw_h
name
Spec        vstb {mw [,h][,concat]} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                            Determines the element size and number
                                MW_options
            1 MW
                                enum                        of stored elements (see enum definition
                                                            at vec-mem-modes.h)
            2 IN1_V40           vec40_t                     Output vector operand

3 IN2_gB_BASE       void *                      Pointer register (gB)
Operands
                                                            Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                            base pointer
            5 IN3_PART          uint8         LOW,HIGH      Word part which is used for operand 4
                                                31   31     32 bit immediate post modification in
            6 IN4_PM_IMM        int32         -2 ..2 -1
                                                            bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstb_v40_indexed_rIp_pm_imm_mw_h (mw_8w, vIn, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic   vstb_v40_indexed_rIp_pm_ptr_mw_h
name
Spec        vstb {mw [,h][,concat]} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                MW_options                  Determines the element size and number
Operands    1 MW
                                enum                        of stored elements (see enum definition
                                                               at vec-mem-modes.h)
              2 IN1_V40           vec40_t                      Output vector operand
              3 IN2_gB_BASE       void *                       Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the
              4 IN3_rI_OFFSET void *
                                                               base pointer
              5 IN3_PART          uint8          LOW,HIGH      Word part which is used for operand 4
              6 IN4_PM_PTR        void*                        Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;
              ...
              vstb_v40_indexed_rIp_pm_ptr_mw_h (mw_8w, vIn, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic     vstb_v40_mw_h
name
Spec syntax   vstb {mw [,h][,concat]} vox[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                              Determines the element size and number
                                MW_options
              1   MW
                                enum                          of stored elements (see enum definition at

vec-mem-modes.h)
Operands
              2   IN1_V40       vec40_t                       Output vector operand
              3   IN2_PTR       void *                        Pointer register (rN)
              void* ptr;
              vec40_t vIn;
C example     ...
              vstb_v40_mw_h (mw_8w, vIn, ptr);

Comments



Intrinsic     vstb_v40_pm_imm_mw_h
name
Spec          vstb {mw [,h][,concat]} vox[0], (pN)+#imm32_6 [,?prSC]
syntax
Return        void
type
                                                            Determines the element size and number
                                MW_options
             1   MW
                                enum                        of stored elements (see enum definition at
                                                            vec-mem-modes.h)

Operands     2   IN1_V40        vec40_t                     Output vector operand
             3   IN2_PTR        void *                      Pointer register (rN)
                                                31   31     32 bit immediate post modification in
             4   IN3_IMM32_6 int32            -2 ..2 -1
                                                            bytes
             void* ptr;
             vec40_t vIn;
C example    ...
             vstb_v40_pm_imm_mw_h (mw_8w, vIn, ptr, 2);

Comments



Intrinsic    vstb_v40_pm_ptr_mw_h
name
Spec         vstb {mw [,h][,concat]} vox[0], (pN)[+pm_x] [,?prSC]
syntax
Return       void
type
                                                            Determines the element size and number
                               MW_options
             1   MW
                               enum                         of stored elements (see enum definition at
                                                            vec-mem-modes.h)
Operands     2   IN1_V40       vec40_t                      Output vector operand
             3   IN2_PTR       void *                       Pointer register (rN)
             4   IN3_PM_PTR void*                           Pointer register (rN)
             void* ptr;
             vec40_t vIn;
C example    ...
             vstb_v40_pm_ptr_mw_h (mw_8w, vIn, ptr, ptr);

Comments


Main table → Memory Access → Store → Store 8 bit
Available addressing modes
Intrinsic Names:
vstb_v40_direct_mw_h_concat
vstb_v40_indexed_imm_mw_h_concat
vstb_v40_indexed_rI_mw_h_concat
vstb_v40_indexed_rI_pm_imm_mw_h_concat
vstb_v40_indexed_rI_pm_ptr_mw_h_concat
vstb_v40_indexed_rIp_mw_h_concat

vstb_v40_indexed_rIp_pm_imm_mw_h_concat
vstb_v40_indexed_rIp_pm_ptr_mw_h_concat
vstb_v40_mw_h_concat
vstb_v40_pm_imm_mw_h_concat
vstb_v40_pm_ptr_mw_h_concat
Intrinsic     vstb_v40_direct_mw_h_concat
name
Spec syntax   vstb {mw [,h][,concat]} vox[0], [#address] [,?prSC]

Return        void
type
                                                              Determines the element size and number
                                MW_options
              1      MW
                                enum                          of stored elements (see enum definition at
                                                              vec-mem-modes.h)
Operands
              2      IN1_V40    vec40_t                       Output vector operand
                                                  32
              3      IN2_ADDR   int32         0..2 -1         32 bit address
              vec40_t vIn;
C example     ...
              vstb_v40_direct_mw_h_concat (mw_8w, vIn, 2);

Comments



Intrinsic     vstb_v40_indexed_imm_mw_h_concat
name
Spec          vstb {mw [,h][,concat]} vox[0], (gB+#imm16_6) [,?prSC]
syntax
Return        void
type
                                                              Determines the element size and number
                                 MW_options
              1 MW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)

Operands      2 IN1_V40          vec40_t                      Output vector operand
              3 IN2_gB_BASE void *                            Pointer register (gB)

              4 IN3_IMM16_6
                                               -              16 bit immediate post modification in
                                 int16
                                               32768..32767   bytes
              void* ptrBase;
              vec40_t vIn;
C example     ...
              vstb_v40_indexed_imm_mw_h_concat (mw_8w, vIn, ptrBase, 2);

Comments



Intrinsic     vstb_v40_indexed_rI_mw_h_concat
name
Spec          vstb {mw [,h][,concat]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                MW_options
            1 MW
                                enum                         of stored elements (see enum definition

at vec-mem-modes.h)

Operands    2 IN1_V40           vec40_t                      Output vector operand
            3 IN2_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                             base pointer
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstb_v40_indexed_rI_mw_h_concat (mw_8w, vIn, ptrBase, ptrModify);

Comments



Intrinsic   vstb_v40_indexed_rI_pm_imm_mw_h_concat
name
Spec        vstb {mw [,h][,concat]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                MW_options
            1 MW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
            2 IN1_V40           vec40_t                      Output vector operand
Operands    3 IN2_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                             base pointer
                                                 31   31     32 bit immediate post modification in
            5 IN4_PM_IMM        int32          -2 ..2 -1
                                                             bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstb_v40_indexed_rI_pm_imm_mw_h_concat (mw_8w, vIn, ptrBase, ptrModify, 2);

Comments
Intrinsic   vstb_v40_indexed_rI_pm_ptr_mw_h_concat
name
Spec        vstb {mw [,h][,concat]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                MW_options
            1 MW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
            2 IN1_V40           vec40_t                      Output vector operand

Operands    3 IN2_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                             base pointer
            5 IN4_PM_PTR        void*                        Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstb_v40_indexed_rI_pm_ptr_mw_h_concat (mw_8w, vIn, ptrBase, ptrModify, ptr);

Comments



Intrinsic   vstb_v40_indexed_rIp_mw_h_concat
name
Spec        vstb {mw [,h][,concat]} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                MW_options
            1 MW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
            2 IN1_V40           vec40_t                      Output vector operand
Operands    3 IN2_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                             base pointer
            5 IN3_PART          uint8          LOW,HIGH      Word part which is used for operand 4
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstb_v40_indexed_rIp_mw_h_concat (mw_8w, vIn, ptrBase, ptrModify, LOW);

Comments



Intrinsic   vstb_v40_indexed_rIp_pm_imm_mw_h_concat
name
Spec        vstb {mw [,h][,concat]} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                            Determines the element size and number
                                MW_options
            1 MW
                                enum                        of stored elements (see enum definition
                                                            at vec-mem-modes.h)
            2 IN1_V40           vec40_t                     Output vector operand
            3 IN2_gB_BASE       void *                      Pointer register (gB)
Operands

Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                            base pointer
            5 IN3_PART          uint8         LOW,HIGH      Word part which is used for operand 4
                                                31   31     32 bit immediate post modification in
            6 IN4_PM_IMM        int32         -2 ..2 -1
                                                            bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstb_v40_indexed_rIp_pm_imm_mw_h_concat (mw_8w, vIn, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic   vstb_v40_indexed_rIp_pm_ptr_mw_h_concat
name
Spec        vstb {mw [,h][,concat]} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                MW_options                  Determines the element size and number
Operands    1 MW
                                enum                        of stored elements (see enum definition
                                                               at vec-mem-modes.h)
              2 IN1_V40           vec40_t                      Output vector operand
              3 IN2_gB_BASE       void *                       Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the
              4 IN3_rI_OFFSET void *
                                                               base pointer
              5 IN3_PART          uint8         LOW,HIGH       Word part which is used for operand 4
              6 IN4_PM_PTR        void*                        Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;
              ...
              vstb_v40_indexed_rIp_pm_ptr_mw_h_concat (mw_8w, vIn, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic     vstb_v40_mw_h_concat
name
Spec syntax   vstb {mw [,h][,concat]} vox[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                              Determines the element size and number
                                MW_options
              1   MW
                                enum                          of stored elements (see enum definition at
                                                              vec-mem-modes.h)
Operands

2   IN1_V40       vec40_t                       Output vector operand
              3   IN2_PTR       void *                        Pointer register (rN)
              void* ptr;
              vec40_t vIn;
C example     ...
              vstb_v40_mw_h_concat (mw_8w, vIn, ptr);

Comments



Intrinsic     vstb_v40_pm_imm_mw_h_concat
name
Spec          vstb {mw [,h][,concat]} vox[0], (pN)+#imm32_6 [,?prSC]
syntax
Return        void
type
                                                            Determines the element size and number
                              MW_options
            1   MW
                              enum                          of stored elements (see enum definition at
                                                            vec-mem-modes.h)

Operands    2   IN1_V40       vec40_t                       Output vector operand
            3   IN2_PTR       void *                        Pointer register (rN)
                                               31   31      32 bit immediate post modification in
            4   IN3_IMM32_6 int32            -2 ..2 -1
                                                            bytes
            void* ptr;
            vec40_t vIn;
C example   ...
            vstb_v40_pm_imm_mw_h_concat (mw_8w, vIn, ptr, 2);

Comments



Intrinsic   vstb_v40_pm_ptr_mw_h_concat
name
Spec        vstb {mw [,h][,concat]} vox[0], (pN)[+pm_x] [,?prSC]
syntax
Return      void
type
                                                            Determines the element size and number
                              MW_options
            1   MW
                              enum                          of stored elements (see enum definition at
                                                            vec-mem-modes.h)
Operands    2   IN1_V40       vec40_t                       Output vector operand
            3   IN2_PTR       void *                        Pointer register (rN)
            4   IN3_PM_PTR void*                            Pointer register (rN)
            void* ptr;
            vec40_t vIn;
C example   ...
            vstb_v40_pm_ptr_mw_h_concat (mw_8w, vIn, ptr, ptr);

Comments


Main table → Memory Access → Store → Store 8 bit
Available addressing modes
Intrinsic Names:
vstb_v32_direct_pb
vstb_v32_indexed_imm_pb
vstb_v32_indexed_rI_pb
vstb_v32_indexed_rI_pm_imm_pb
vstb_v32_indexed_rI_pm_ptr_pb
vstb_v32_indexed_rIp_pb
vstb_v32_indexed_rIp_pm_imm_pb
vstb_v32_indexed_rIp_pm_ptr_pb
vstb_v32_pb

vstb_v32_pm_imm_pb
vstb_v32_pm_ptr_pb
Intrinsic     vstb_v32_direct_pb
name
Spec syntax   vstb {pb [,concat]} vix[0], [#address] [,?prSC]

Return        void
type
                                                                 Determines the element size and number
                                 PB_options
              1      PB
                                 enum                            of stored elements (see enum definition at
                                                                 vec-mem-modes.h)
Operands      2      IN1_V32     vec_t                           Input vector operand

              3      IN1_OFST    uint8          0,4
                                                                 Offset for the first DW used from operand
                                                                 2
                                                      32
              4      IN2_ADDR    int32          0..2 -1          32 bit address
              vec_t vIn;
C example     ...
              vstb_v32_direct_pb (pb_16b, vIn, 0, 2);

Comments



Intrinsic     vstb_v32_indexed_imm_pb
name
Spec          vstb {pb [,concat]} vix[0], (gB+#imm16_6) [,?prSC]
syntax
Return        void
type
                                                                 Determines the element size and number
                                   PB_options
              1   PB
                                   enum                          of stored elements (see enum definition
                                                                 at vec-mem-modes.h)
              2   IN1_V32          vec_t                         Input vector operand
Operands                                                         Offset for the first DW used from
              3   IN1_OFST         uint8          0,4
                                                                 operand 2
              4   IN2_gB_BASE void *                             Pointer register (gB)
                                                  -              16 bit immediate post modification in
              5   IN3_IMM16_6      int16
                                                  32768..32767   bytes
              void* ptrBase;
              vec_t vIn;
C example     ...
              vstb_v32_indexed_imm_pb (pb_16b, vIn, 0, ptrBase, 2);

Comments
Intrinsic   vstb_v32_indexed_rI_pb
name
Spec        vstb {pb [,concat]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type

Determines the element size and number
                                  PB_options
            1 PB
                                  enum                          of stored elements (see enum definition
                                                                at vec-mem-modes.h)
            2 IN1_V32             vec_t                         Input vector operand
Operands                                                        Offset for the first DW used from
            3 IN1_OFST            uint8         0,4
                                                                operand 2
            4 IN2_gB_BASE         void *                        Pointer register (gB)
                                                                Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                                base pointer
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstb_v32_indexed_rI_pb (pb_16b, vIn, 0, ptrBase, ptrModify);

Comments



Intrinsic   vstb_v32_indexed_rI_pm_imm_pb
name
Spec        vstb {pb [,concat]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                                Determines the element size and number
                                  PB_options
            1 PB
                                  enum                          of stored elements (see enum definition
                                                                at vec-mem-modes.h)
            2 IN1_V32             vec_t                         Input vector operand
Operands
                                                                Offset for the first DW used from
            3 IN1_OFST            uint8         0,4
                                                                operand 2
            4 IN2_gB_BASE         void *                        Pointer register (gB)
            5 IN3_rI_OFFSET void *                              Pointer (rI) specifying the offset from the
                                                                base pointer
                                                  31   31       32 bit immediate post modification in
            6 IN4_PM_IMM          int32         -2 ..2 -1
                                                                bytes
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...

vstb_v32_indexed_rI_pm_imm_pb (pb_16b, vIn, 0, ptrBase, ptrModify, 2);

Comments



Intrinsic   vstb_v32_indexed_rI_pm_ptr_pb
name
Spec        vstb {pb [,concat]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                                Determines the element size and number
                                  PB_options
            1 PB
                                  enum                          of stored elements (see enum definition
                                                                at vec-mem-modes.h)
            2 IN1_V32             vec_t                         Input vector operand
                                                                Offset for the first DW used from
Operands    3 IN1_OFST            uint8         0,4
                                                                operand 2
            4 IN2_gB_BASE         void *                        Pointer register (gB)
                                                                Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                                base pointer
            6 IN4_PM_PTR          void*                         Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstb_v32_indexed_rI_pm_ptr_pb (pb_16b, vIn, 0, ptrBase, ptrModify, ptr);

Comments



Intrinsic   vstb_v32_indexed_rIp_pb
name
Spec        vstb {pb [,concat]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and number
                                 PB_options
            1 PB
                                 enum                          of stored elements (see enum definition
                                                               at vec-mem-modes.h)
            2 IN1_V32            vec_t                         Input vector operand
                                                               Offset for the first DW used from
            3 IN1_OFST           uint8         0,4
Operands                                                       operand 2
            4 IN2_gB_BASE        void *                        Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the

5 IN3_rI_OFFSET void *
                                                               base pointer
            6 IN3_PART           uint8         LOW,HIGH        Word part which is used for operand 5
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstb_v32_indexed_rIp_pb (pb_16b, vIn, 0, ptrBase, ptrModify, LOW);

Comments



Intrinsic   vstb_v32_indexed_rIp_pm_imm_pb
name
Spec        vstb {pb [,concat]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and number
                                 PB_options
            1 PB
                                 enum                          of stored elements (see enum definition
                                                               at vec-mem-modes.h)
            2 IN1_V32            vec_t                         Input vector operand
                                                               Offset for the first DW used from
            3 IN1_OFST           uint8         0,4
                                                               operand 2
Operands    4 IN2_gB_BASE        void *                        Pointer register (gB)

            5 IN3_rI_OFFSET void *
                                                               Pointer (rI) specifying the offset from the
                                                               base pointer
            6 IN3_PART           uint8         LOW,HIGH        Word part which is used for operand 5

            7 IN4_PM_IMM                          31   31      32 bit immediate post modification in
                                 int32         -2 ..2 -1
                                                               bytes
              void* ptrBase;
              void* ptrModify;
C example     vec_t vIn;
              ...
              vstb_v32_indexed_rIp_pm_imm_pb (pb_16b, vIn, 0, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic     vstb_v32_indexed_rIp_pm_ptr_pb
name
Spec          vstb {pb [,concat]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return        void
type
                                                                 Determines the element size and number
                                   PB_options
              1 PB
                                   enum                          of stored elements (see enum definition

at vec-mem-modes.h)
              2 IN1_V32            vec_t                         Input vector operand
                                                                 Offset for the first DW used from
              3 IN1_OFST           uint8         0,4
                                                                 operand 2
Operands
              4 IN2_gB_BASE        void *                        Pointer register (gB)
                                                                 Pointer (rI) specifying the offset from the
              5 IN3_rI_OFFSET void *
                                                                 base pointer
              6 IN3_PART           uint8         LOW,HIGH        Word part which is used for operand 5
              7 IN4_PM_PTR         void*                         Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec_t vIn;
              ...
              vstb_v32_indexed_rIp_pm_ptr_pb (pb_16b, vIn, 0, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic     vstb_v32_pb
name
Spec syntax   vstb {pb [,concat]} vix[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                 PB_options
Operands      1      PB
                                 enum                           Determines the element size and number
                                                             of stored elements (see enum definition at
                                                             vec-mem-modes.h)
            2   IN1_V32         vec_t                        Input vector operand

            3   IN1_OFST        uint8            0,4         Offset for the first DW used from operand
                                                             2

            4   IN2_PTR         void *                       Pointer register (rN)
            void* ptr;
            vec_t vIn;
C example   ...
            vstb_v32_pb (pb_16b, vIn, 0, ptr);

Comments



Intrinsic   vstb_v32_pm_imm_pb
name
Spec        vstb {pb [,concat]} vix[0], (pN)+#imm32_6 [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                 PB_options
            1   PB
                                 enum                        of stored elements (see enum definition at
                                                             vec-mem-modes.h)

2   IN1_V32          vec_t                       Input vector operand
Operands    3   IN1_OFST         uint8                       Offset for the first DW used from operand
                                                 0,4
                                                             2

            4   IN2_PTR          void *                      Pointer register (rN)
                                                   31   31   32 bit immediate post modification in
            5   IN3_IMM32_6 int32                -2 ..2 -1
                                                             bytes
            void* ptr;
            vec_t vIn;
C example   ...
            vstb_v32_pm_imm_pb (pb_16b, vIn, 0, ptr, 2);

Comments



Intrinsic   vstb_v32_pm_ptr_pb
name
Spec        vstb {pb [,concat]} vix[0], (pN)[+pm_x] [,?prSC]
syntax
Return        void
type
                                                               Determines the element size and number
                                  PB_options
              1   PB
                                  enum                         of stored elements (see enum definition at
                                                               vec-mem-modes.h)
              2   IN1_V32         vec_t                        Input vector operand
Operands
              3   IN1_OFST        uint8          0,4
                                                               Offset for the first DW used from operand
                                                               2

              4   IN2_PTR         void *                       Pointer register (rN)
              5   IN3_PM_PTR void*                             Pointer register (rN)
              void* ptr;
              vec_t vIn;
C example     ...
              vstb_v32_pm_ptr_pb (pb_16b, vIn, 0, ptr, ptr);

Comments


Main table → Memory Access → Store → Store 8 bit
Available addressing modes
Intrinsic Names:
vstb_v32_direct_pb_concat
vstb_v32_indexed_imm_pb_concat
vstb_v32_indexed_rI_pb_concat
vstb_v32_indexed_rI_pm_imm_pb_concat
vstb_v32_indexed_rI_pm_ptr_pb_concat
vstb_v32_indexed_rIp_pb_concat
vstb_v32_indexed_rIp_pm_imm_pb_concat
vstb_v32_indexed_rIp_pm_ptr_pb_concat
vstb_v32_pb_concat
vstb_v32_pm_imm_pb_concat
vstb_v32_pm_ptr_pb_concat
Intrinsic     vstb_v32_direct_pb_concat
name
Spec syntax   vstb {pb [,concat]} vix[0], [#address] [,?prSC]

Return        void
type

Determines the element size and number
                                 PB_options
              1      PB
                                 enum                           of stored elements (see enum definition at
                                                                vec-mem-modes.h)
Operands      2      IN1_V32     vec_t                          Input vector operand

              3      IN1_OFST    uint8          0,4
                                                                Offset for the first DW used from operand
                                                                2
                                                      32
              4      IN2_ADDR    int32          0..2 -1         32 bit address
              vec_t vIn;
C example     ...
              vstb_v32_direct_pb_concat (pb_16b, vIn, 0, 2);

Comments



Intrinsic     vstb_v32_indexed_imm_pb_concat
name
Spec          vstb {pb [,concat]} vix[0], (gB+#imm16_6) [,?prSC]
syntax
Return        void
type
                                                                Determines the element size and number
                                  PB_options
              1   PB
                                  enum                          of stored elements (see enum definition
                                                                at vec-mem-modes.h)
              2   IN1_V32         vec_t                         Input vector operand
Operands                                                        Offset for the first DW used from
              3   IN1_OFST        uint8          0,4
                                                                operand 2
              4   IN2_gB_BASE void *                            Pointer register (gB)
                                                 -              16 bit immediate post modification in
              5   IN3_IMM16_6     int16
                                                 32768..32767   bytes
              void* ptrBase;
              vec_t vIn;
C example     ...
              vstb_v32_indexed_imm_pb_concat (pb_16b, vIn, 0, ptrBase, 2);

Comments
Intrinsic   vstb_v32_indexed_rI_pb_concat
name
Spec        vstb {pb [,concat]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                                Determines the element size and number
                                  PB_options
            1 PB

enum                          of stored elements (see enum definition
                                                                at vec-mem-modes.h)
            2 IN1_V32             vec_t                         Input vector operand
Operands                                                        Offset for the first DW used from
            3 IN1_OFST            uint8         0,4
                                                                operand 2
            4 IN2_gB_BASE         void *                        Pointer register (gB)
                                                                Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                                base pointer
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstb_v32_indexed_rI_pb_concat (pb_16b, vIn, 0, ptrBase, ptrModify);

Comments



Intrinsic   vstb_v32_indexed_rI_pm_imm_pb_concat
name
Spec        vstb {pb [,concat]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                                Determines the element size and number
                                  PB_options
            1 PB
                                  enum                          of stored elements (see enum definition
                                                                at vec-mem-modes.h)
            2 IN1_V32             vec_t                         Input vector operand
Operands
                                                                Offset for the first DW used from
            3 IN1_OFST            uint8         0,4
                                                                operand 2
            4 IN2_gB_BASE         void *                        Pointer register (gB)
            5 IN3_rI_OFFSET void *                              Pointer (rI) specifying the offset from the
                                                                base pointer
                                                  31   31       32 bit immediate post modification in
            6 IN4_PM_IMM         int32          -2 ..2 -1
                                                                bytes
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstb_v32_indexed_rI_pm_imm_pb_concat (pb_16b, vIn, 0, ptrBase, ptrModify, 2);

Comments

Intrinsic   vstb_v32_indexed_rI_pm_ptr_pb_concat
name
Spec        vstb {pb [,concat]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                                Determines the element size and number
                                 PB_options
            1 PB
                                 enum                           of stored elements (see enum definition
                                                                at vec-mem-modes.h)
            2 IN1_V32            vec_t                          Input vector operand
                                                                Offset for the first DW used from
Operands    3 IN1_OFST           uint8          0,4
                                                                operand 2
            4 IN2_gB_BASE        void *                         Pointer register (gB)
                                                                Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                                base pointer
            6 IN4_PM_PTR         void*                          Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstb_v32_indexed_rI_pm_ptr_pb_concat (pb_16b, vIn, 0, ptrBase, ptrModify, ptr);

Comments



Intrinsic   vstb_v32_indexed_rIp_pb_concat
name
Spec        vstb {pb [,concat]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 PB_options
            1 PB
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_V32            vec_t                        Input vector operand
                                                              Offset for the first DW used from
            3 IN1_OFST           uint8         0,4
Operands                                                      operand 2
            4 IN2_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *

base pointer
            6 IN3_PART           uint8         LOW,HIGH       Word part which is used for operand 5
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstb_v32_indexed_rIp_pb_concat (pb_16b, vIn, 0, ptrBase, ptrModify, LOW);

Comments



Intrinsic   vstb_v32_indexed_rIp_pm_imm_pb_concat
name
Spec        vstb {pb [,concat]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 PB_options
            1 PB
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_V32            vec_t                        Input vector operand
                                                              Offset for the first DW used from
            3 IN1_OFST           uint8         0,4
                                                              operand 2
Operands    4 IN2_gB_BASE        void *                       Pointer register (gB)

            5 IN3_rI_OFFSET void *
                                                              Pointer (rI) specifying the offset from the
                                                              base pointer
            6 IN3_PART           uint8         LOW,HIGH       Word part which is used for operand 5

            7 IN4_PM_IMM                         31   31      32 bit immediate post modification in
                                 int32         -2 ..2 -1
                                                              bytes
              void* ptrBase;
              void* ptrModify;
C example     vec_t vIn;
              ...
              vstb_v32_indexed_rIp_pm_imm_pb_concat (pb_16b, vIn, 0, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic     vstb_v32_indexed_rIp_pm_ptr_pb_concat
name
Spec          vstb {pb [,concat]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return        void
type
                                                                Determines the element size and number
                                   PB_options
              1 PB
                                   enum                         of stored elements (see enum definition
                                                                at vec-mem-modes.h)

2 IN1_V32            vec_t                        Input vector operand
                                                                Offset for the first DW used from
              3 IN1_OFST           uint8         0,4
                                                                operand 2
Operands
              4 IN2_gB_BASE        void *                       Pointer register (gB)
                                                                Pointer (rI) specifying the offset from the
              5 IN3_rI_OFFSET void *
                                                                base pointer
              6 IN3_PART           uint8         LOW,HIGH       Word part which is used for operand 5
              7 IN4_PM_PTR         void*                        Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec_t vIn;
              ...
              vstb_v32_indexed_rIp_pm_ptr_pb_concat (pb_16b, vIn, 0, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic     vstb_v32_pb_concat
name
Spec syntax   vstb {pb [,concat]} vix[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                 PB_options
Operands      1      PB
                                 enum                          Determines the element size and number
                                                             of stored elements (see enum definition at
                                                             vec-mem-modes.h)
            2   IN1_V32        vec_t                         Input vector operand

            3   IN1_OFST       uint8          0,4            Offset for the first DW used from operand
                                                             2

            4   IN2_PTR        void *                        Pointer register (rN)
            void* ptr;
            vec_t vIn;
C example   ...
            vstb_v32_pb_concat (pb_16b, vIn, 0, ptr);

Comments



Intrinsic   vstb_v32_pm_imm_pb_concat
name
Spec        vstb {pb [,concat]} vix[0], (pN)+#imm32_6 [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                PB_options
            1   PB
                                enum                         of stored elements (see enum definition at
                                                             vec-mem-modes.h)

2   IN1_V32         vec_t                        Input vector operand
Operands    3   IN1_OFST        uint8                        Offset for the first DW used from operand
                                               0,4
                                                             2

            4   IN2_PTR         void *                       Pointer register (rN)
                                                 31     31   32 bit immediate post modification in
            5   IN3_IMM32_6 int32              -2 ..2 -1
                                                             bytes
            void* ptr;
            vec_t vIn;
C example   ...
            vstb_v32_pm_imm_pb_concat (pb_16b, vIn, 0, ptr, 2);

Comments



Intrinsic   vstb_v32_pm_ptr_pb_concat
name
Spec        vstb {pb [,concat]} vix[0], (pN)[+pm_x] [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and number
                                PB_options
            1   PB
                                enum                           of stored elements (see enum definition at
                                                               vec-mem-modes.h)
            2   IN1_V32         vec_t                          Input vector operand
Operands
            3   IN1_OFST        uint8          0,4
                                                               Offset for the first DW used from operand
                                                               2

            4   IN2_PTR         void *                         Pointer register (rN)
            5   IN3_PM_PTR void*                               Pointer register (rN)
            void* ptr;
            vec_t vIn;
C example   ...
            vstb_v32_pm_ptr_pb_concat (pb_16b, vIn, 0, ptr, ptr);

Comments


Main table → Memory Access → Store → Store 8 bit
Available addressing modes
Intrinsic Names:
vstb_v40_indexed_rI_pb_vuX
vstb_v40_indexed_rI_pm_imm_pb_vuX
vstb_v40_indexed_rI_pm_ptr_pb_vuX
vstb_v40_indexed_rIp_pb_vuX
vstb_v40_indexed_rIp_pm_imm_pb_vuX
vstb_v40_indexed_rIp_pm_ptr_pb_vuX
vstb_v40_pb_vuX
vstb_v40_pm_imm_pb_vuX
vstb_v40_pm_ptr_pb_vuX
Intrinsic   vstb_v40_indexed_rI_pb_vuX
name
Spec        vstb {pb, vuX} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                                Determines the element size and number
                                  PB_options
            1 PB

enum                          of stored elements (see enum definition
                                                                at vec-mem-modes.h)
            2 VUX                 uint8         0..3            Determines the source VCU
            3 IN1_V40             vec40_t                       Output vector operand
Operands
                                                                Offset for the first DW used from
            4 IN1_OFST            uint8         0,4
                                                                operand 3
            5 IN2_gB_BASE         void *                        Pointer register (gB)

            6 IN3_rI_OFFSET void *
                                                                Pointer (rI) specifying the offset from the
                                                                base pointer
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstb_v40_indexed_rI_pb_vuX (pb_16b, 1, vIn, 0, ptrBase, ptrModify);

Comments



Intrinsic   vstb_v40_indexed_rI_pm_imm_pb_vuX
name
Spec        vstb {pb, vuX} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                                Determines the element size and number
                                  PB_options
            1 PB
                                  enum                          of stored elements (see enum definition
                                                                at vec-mem-modes.h)
            2 VUX                 uint8         0..3            Determines the source VCU
Operands    3 IN1_V40             vec40_t                       Output vector operand

            4 IN1_OFST
                                                                Offset for the first DW used from
                                  uint8         0,4
                                                                operand 3
            5 IN2_gB_BASE         void *                        Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the
            6 IN3_rI_OFFSET void *
                                                               base pointer
                                                  31   31      32 bit immediate post modification in
            7 IN4_PM_IMM         int32          -2 ..2 -1

bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstb_v40_indexed_rI_pm_imm_pb_vuX (pb_16b, 1, vIn, 0, ptrBase, ptrModify, 2);

Comments



Intrinsic   vstb_v40_indexed_rI_pm_ptr_pb_vuX
name
Spec        vstb {pb, vuX} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and number
                                 PB_options
            1 PB
                                 enum                          of stored elements (see enum definition
                                                               at vec-mem-modes.h)
            2 VUX                uint8          0..3           Determines the source VCU
            3 IN1_V40            vec40_t                       Output vector operand
Operands                                                       Offset for the first DW used from
            4 IN1_OFST           uint8          0,4
                                                               operand 3
            5 IN2_gB_BASE        void *                        Pointer register (gB)

            6 IN3_rI_OFFSET void *
                                                               Pointer (rI) specifying the offset from the
                                                               base pointer
            7 IN4_PM_PTR         void*                         Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstb_v40_indexed_rI_pm_ptr_pb_vuX (pb_16b, 1, vIn, 0, ptrBase, ptrModify, ptr);

Comments



Intrinsic   vstb_v40_indexed_rIp_pb_vuX
name
Spec        vstb {pb,vuX} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 PB_options
            1 PB
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 VUX                uint8         0..3           Determines the source VCU
            3 IN1_V40            vec40_t                      Output vector operand
Operands                                                      Offset for the first DW used from
            4 IN1_OFST           uint8         0,4

operand 3
            5 IN2_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            6 IN3_rI_OFFSET void *
                                                              base pointer
            7 IN3_PART           uint8         LOW,HIGH       Word part which is used for operand 6
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstb_v40_indexed_rIp_pb_vuX (pb_16b, 1, vIn, 0, ptrBase, ptrModify, LOW);

Comments



Intrinsic   vstb_v40_indexed_rIp_pm_imm_pb_vuX
name
Spec        vstb {pb,vuX} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 PB_options
            1 PB
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 VUX                uint8         0..3           Determines the source VCU

Operands    3 IN1_V40            vec40_t                      Output vector operand
                                                              Offset for the first DW used from
            4 IN1_OFST           uint8         0,4
                                                              operand 3
            5 IN2_gB_BASE        void *                       Pointer register (gB)
            6 IN3_rI_OFFSET void *                            Pointer (rI) specifying the offset from the
                                                              base pointer
            7 IN3_PART           uint8         LOW,HIGH       Word part which is used for operand 6

            8 IN4_PM_IMM                         31   31      32 bit immediate post modification in
                                 int32         -2 ..2 -1
                                                              bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstb_v40_indexed_rIp_pm_imm_pb_vuX (pb_16b, 1, vIn, 0, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic   vstb_v40_indexed_rIp_pm_ptr_pb_vuX
name
Spec        vstb {pb,vuX} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type

Determines the element size and number
                                 PB_options
            1 PB
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 VUX                uint8         0..3           Determines the source VCU
            3 IN1_V40            vec40_t                      Output vector operand
                                                              Offset for the first DW used from
            4 IN1_OFST           uint8         0,4
Operands                                                      operand 3
            5 IN2_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            6 IN3_rI_OFFSET void *
                                                              base pointer
            7 IN3_PART           uint8         LOW,HIGH       Word part which is used for operand 6
            8 IN4_PM_PTR         void*                        Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstb_v40_indexed_rIp_pm_ptr_pb_vuX (pb_16b, 1, vIn, 0, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic   vstb_v40_pb_vuX
name
Spec syntax   vstb {pb, vuX} vox[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                               Determines the element size and number
                                 PB_options
              1   PB
                                 enum                          of stored elements (see enum definition at
                                                               vec-mem-modes.h)
              2   VUX            uint8          0..3           Determines the source VCU
Operands
              3   IN1_V40        vec40_t                       Output vector operand

              4   IN1_OFST       uint8          0,4            Offset for the first DW used from operand
                                                               3

              5   IN2_PTR        void *                        Pointer register (rN)
              void* ptr;
              vec40_t vIn;
C example     ...
              vstb_v40_pb_vuX (pb_16b, 1, vIn, 0, ptr);

Comments



Intrinsic     vstb_v40_pm_imm_pb_vuX
name

Spec syntax   vstb {pb, vuX} vox[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                               Determines the element size and number
                                  PB_options
              1   PB
                                  enum                         of stored elements (see enum definition at
                                                               vec-mem-modes.h)
              2   VUX             uint8          0..3          Determines the source VCU
              3   IN1_V40         vec40_t                      Output vector operand
Operands
              4   IN1_OFST        uint8          0,4           Offset for the first DW used from operand
                                                               3

              5   IN2_PTR         void *                       Pointer register (rN)
                                                   31     31   32 bit immediate post modification in
              6   IN3_PM_IMM int32               -2 ..2 -1
                                                               bytes
              void* ptr;
              vec40_t vIn;
C example     ...
              vstb_v40_pm_imm_pb_vuX (pb_16b, 1, vIn, 0, ptr, 2);
Comments



Intrinsic   vstb_v40_pm_ptr_pb_vuX
name
Spec        vstb {pb, vuX} vox[0], (pN)[+pm_x] [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and number
                                PB_options
            1   PB
                                enum                           of stored elements (see enum definition at
                                                               vec-mem-modes.h)
            2   VUX             uint8          0..3            Determines the source VCU
Operands    3   IN1_V40         vec40_t                        Output vector operand

            4   IN1_OFST        uint8          0,4             Offset for the first DW used from operand
                                                               3

            5   IN2_PTR         void *                         Pointer register (rN)
            6   IN3_PM_PTR void*                               Pointer register (rN)
            void* ptr;
            vec40_t vIn;
C example   ...
            vstb_v40_pm_ptr_pb_vuX (pb_16b, 1, vIn, 0, ptr, ptr);

Comments


Main table → Memory Access → Store → Store 8 bit
Available addressing modes
Intrinsic Names:

vstb_v32_indexed_rI_pb_vuX
vstb_v32_indexed_rI_pm_imm_pb_vuX
vstb_v32_indexed_rI_pm_ptr_pb_vuX
vstb_v32_indexed_rIp_pb_vuX
vstb_v32_indexed_rIp_pm_imm_pb_vuX
vstb_v32_indexed_rIp_pm_ptr_pb_vuX
vstb_v32_pb_vuX
vstb_v32_pm_imm_pb_vuX
vstb_v32_pm_ptr_pb_vuX
Intrinsic   vstb_v32_indexed_rI_pb_vuX
name
Spec        vstb {pb, vuX} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                                Determines the element size and number
                                  PB_options
            1 PB
                                  enum                          of stored elements (see enum definition
                                                                at vec-mem-modes.h)
            2 VUX                 uint8         0..3            Determines the source VCU
            3 IN1_V32             vec_t                         Input vector operand
Operands
                                                                Offset for the first DW used from
            4 IN1_OFST            uint8         0,4
                                                                operand 3
            5 IN2_gB_BASE         void *                        Pointer register (gB)

            6 IN3_rI_OFFSET void *
                                                                Pointer (rI) specifying the offset from the
                                                                base pointer
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstb_v32_indexed_rI_pb_vuX (pb_16b, 1, vIn, 0, ptrBase, ptrModify);

Comments



Intrinsic   vstb_v32_indexed_rI_pm_imm_pb_vuX
name
Spec        vstb {pb, vuX} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                                Determines the element size and number
                                  PB_options
            1 PB
                                  enum                          of stored elements (see enum definition
                                                                at vec-mem-modes.h)
            2 VUX                 uint8         0..3            Determines the source VCU
Operands    3 IN1_V32             vec_t                         Input vector operand

            4 IN1_OFST
                                                                Offset for the first DW used from
                                  uint8         0,4

operand 3
            5 IN2_gB_BASE         void *                        Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the
            6 IN3_rI_OFFSET void *
                                                               base pointer
                                                  31   31      32 bit immediate post modification in
            7 IN4_PM_IMM         int32          -2 ..2 -1
                                                               bytes
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstb_v32_indexed_rI_pm_imm_pb_vuX (pb_16b, 1, vIn, 0, ptrBase, ptrModify, 2);

Comments



Intrinsic   vstb_v32_indexed_rI_pm_ptr_pb_vuX
name
Spec        vstb {pb, vuX} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and number
                                 PB_options
            1 PB
                                 enum                          of stored elements (see enum definition
                                                               at vec-mem-modes.h)
            2 VUX                uint8          0..3           Determines the source VCU
            3 IN1_V32            vec_t                         Input vector operand
Operands                                                       Offset for the first DW used from
            4 IN1_OFST           uint8          0,4
                                                               operand 3
            5 IN2_gB_BASE        void *                        Pointer register (gB)

            6 IN3_rI_OFFSET void *
                                                               Pointer (rI) specifying the offset from the
                                                               base pointer
            7 IN4_PM_PTR         void*                         Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstb_v32_indexed_rI_pm_ptr_pb_vuX (pb_16b, 1, vIn, 0, ptrBase, ptrModify, ptr);

Comments



Intrinsic   vstb_v32_indexed_rIp_pb_vuX
name
Spec        vstb {pb,vuX} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number

PB_options
            1 PB
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 VUX                uint8         0..3           Determines the source VCU
            3 IN1_V32            vec_t                        Input vector operand
Operands                                                      Offset for the first DW used from
            4 IN1_OFST           uint8         0,4
                                                              operand 3
            5 IN2_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            6 IN3_rI_OFFSET void *
                                                              base pointer
            7 IN3_PART           uint8         LOW,HIGH       Word part which is used for operand 6
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstb_v32_indexed_rIp_pb_vuX (pb_16b, 1, vIn, 0, ptrBase, ptrModify, LOW);

Comments



Intrinsic   vstb_v32_indexed_rIp_pm_imm_pb_vuX
name
Spec        vstb {pb,vuX} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 PB_options
            1 PB
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 VUX                uint8         0..3           Determines the source VCU

Operands    3 IN1_V32            vec_t                        Input vector operand
                                                              Offset for the first DW used from
            4 IN1_OFST           uint8         0,4
                                                              operand 3
            5 IN2_gB_BASE        void *                       Pointer register (gB)
            6 IN3_rI_OFFSET void *                            Pointer (rI) specifying the offset from the
                                                              base pointer
            7 IN3_PART           uint8         LOW,HIGH       Word part which is used for operand 6

8 IN4_PM_IMM                         31   31      32 bit immediate post modification in
                                 int32         -2 ..2 -1
                                                              bytes
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstb_v32_indexed_rIp_pm_imm_pb_vuX (pb_16b, 1, vIn, 0, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic   vstb_v32_indexed_rIp_pm_ptr_pb_vuX
name
Spec        vstb {pb,vuX} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 PB_options
            1 PB
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 VUX                uint8         0..3           Determines the source VCU
            3 IN1_V32            vec_t                        Input vector operand
                                                              Offset for the first DW used from
            4 IN1_OFST           uint8         0,4
Operands                                                      operand 3
            5 IN2_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            6 IN3_rI_OFFSET void *
                                                              base pointer
            7 IN3_PART           uint8         LOW,HIGH       Word part which is used for operand 6
            8 IN4_PM_PTR         void*                        Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstb_v32_indexed_rIp_pm_ptr_pb_vuX (pb_16b, 1, vIn, 0, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic   vstb_v32_pb_vuX
name
Spec syntax   vstb {pb, vuX} vix[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                               Determines the element size and number
                                 PB_options
              1   PB
                                 enum                          of stored elements (see enum definition at
                                                               vec-mem-modes.h)

2   VUX            uint8          0..3           Determines the source VCU
Operands
              3   IN1_V32        vec_t                         Input vector operand

              4   IN1_OFST       uint8          0,4            Offset for the first DW used from operand
                                                               3

              5   IN2_PTR        void *                        Pointer register (rN)
              void* ptr;
              vec_t vIn;
C example     ...
              vstb_v32_pb_vuX (pb_16b, 1, vIn, 0, ptr);

Comments



Intrinsic     vstb_v32_pm_imm_pb_vuX
name
Spec syntax   vstb {pb, vuX} vix[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                               Determines the element size and number
                                  PB_options
              1   PB
                                  enum                         of stored elements (see enum definition at
                                                               vec-mem-modes.h)
              2   VUX             uint8          0..3          Determines the source VCU
              3   IN1_V32         vec_t                        Input vector operand
Operands
              4   IN1_OFST        uint8          0,4           Offset for the first DW used from operand
                                                               3

              5   IN2_PTR         void *                       Pointer register (rN)
                                                   31     31   32 bit immediate post modification in
              6   IN3_PM_IMM int32               -2 ..2 -1
                                                               bytes
              void* ptr;
              vec_t vIn;
C example     ...
              vstb_v32_pm_imm_pb_vuX (pb_16b, 1, vIn, 0, ptr, 2);
Comments



Intrinsic   vstb_v32_pm_ptr_pb_vuX
name
Spec        vstb {pb, vuX} vix[0], (pN)[+pm_x] [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and number
                                PB_options
            1   PB
                                enum                           of stored elements (see enum definition at
                                                               vec-mem-modes.h)
            2   VUX             uint8          0..3            Determines the source VCU

Operands    3   IN1_V32         vec_t                          Input vector operand

            4   IN1_OFST        uint8          0,4             Offset for the first DW used from operand
                                                               3

            5   IN2_PTR         void *                         Pointer register (rN)
            6   IN3_PM_PTR void*                               Pointer register (rN)
            void* ptr;
            vec_t vIn;
C example   ...
            vstb_v32_pm_ptr_pb_vuX (pb_16b, 1, vIn, 0, ptr, ptr);

Comments


Main table → Memory Access → Store → Store 8 bit
Available addressing modes
Intrinsic Names:
vstb_v32_indexed_rI_mw_vuX
vstb_v32_indexed_rI_pm_imm_mw_vuX
vstb_v32_indexed_rI_pm_ptr_mw_vuX
vstb_v32_indexed_rIp_mw_vuX
vstb_v32_indexed_rIp_pm_imm_mw_vuX
vstb_v32_indexed_rIp_pm_ptr_mw_vuX
vstb_v32_mw_vuX
vstb_v32_pm_imm_mw_vuX
vstb_v32_pm_ptr_mw_vuX
Intrinsic   vstb_v32_indexed_rI_mw_vuX
name
Spec        vstb {mw, vuX [,h]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                                Determines the element size and number
                                MW_options
            1 MW
                                enum                            of stored elements (see enum definition
                                                                at vec-mem-modes.h)
            2 VUX               uint8          0..3             Determines the source VCU
Operands    3 IN1_V32           vec_t                           Input vector operand
            4 IN2_gB_BASE       void *                          Pointer register (gB)
                                                                Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                                base pointer
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstb_v32_indexed_rI_mw_vuX (mw_8w, 1, vIn, ptrBase, ptrModify);

Comments



Intrinsic   vstb_v32_indexed_rI_pm_imm_mw_vuX
name
Spec        vstb {mw, vuX [,h]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                                Determines the element size and number
                                MW_options
            1 MW
                                enum                            of stored elements (see enum definition

at vec-mem-modes.h)
            2 VUX               uint8          0..3             Determines the source VCU
            3 IN1_V32           vec_t                           Input vector operand
Operands
            4 IN2_gB_BASE       void *                          Pointer register (gB)

            5 IN3_rI_OFFSET void *
                                                                Pointer (rI) specifying the offset from the
                                                                base pointer

            6 IN4_PM_IMM                         31   31        32 bit immediate post modification in
                                int32          -2 ..2 -1
                                                                bytes
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstb_v32_indexed_rI_pm_imm_mw_vuX (mw_8w, 1, vIn, ptrBase, ptrModify, 2);

Comments



Intrinsic   vstb_v32_indexed_rI_pm_ptr_mw_vuX
name
Spec        vstb {mw, vuX [,h]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                                Determines the element size and number
                                MW_options
            1 MW
                                enum                            of stored elements (see enum definition
                                                                at vec-mem-modes.h)
            2 VUX               uint8          0..3             Determines the source VCU

Operands    3 IN1_V32           vec_t                           Input vector operand
            4 IN2_gB_BASE       void *                          Pointer register (gB)
                                                                Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                                base pointer
            6 IN4_PM_PTR        void*                           Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstb_v32_indexed_rI_pm_ptr_mw_vuX (mw_8w, 1, vIn, ptrBase, ptrModify, ptr);

Comments



Intrinsic   vstb_v32_indexed_rIp_mw_vuX
name
Spec        vstb {mw,vuX [,h]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                                Determines the element size and number
                                MW_options

Operands    1 MW
                                enum                            of stored elements (see enum definition
                                                                at vec-mem-modes.h)
            2 VUX               uint8         0..3          Determines the source VCU
            3 IN1_V32           vec_t                       Input vector operand
            4 IN2_gB_BASE       void *                      Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                            base pointer
            6 IN3_PART          uint8         LOW,HIGH      Word part which is used for operand 5
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstb_v32_indexed_rIp_mw_vuX (mw_8w, 1, vIn, ptrBase, ptrModify, LOW);

Comments



Intrinsic   vstb_v32_indexed_rIp_pm_imm_mw_vuX
name
Spec        vstb {mw,vuX [,h]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                            Determines the element size and number
                                MW_options
            1 MW
                                enum                        of stored elements (see enum definition
                                                            at vec-mem-modes.h)
            2 VUX               uint8         0..3          Determines the source VCU
            3 IN1_V32           vec_t                       Input vector operand
Operands    4 IN2_gB_BASE       void *                      Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                            base pointer
            6 IN3_PART          uint8         LOW,HIGH      Word part which is used for operand 5

            7 IN4_PM_IMM                        31   31     32 bit immediate post modification in
                                int32         -2 ..2 -1
                                                            bytes
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstb_v32_indexed_rIp_pm_imm_mw_vuX (mw_8w, 1, vIn, ptrBase, ptrModify, LOW, 2);

Comments
Intrinsic     vstb_v32_indexed_rIp_pm_ptr_mw_vuX
name

Spec          vstb {mw,vuX [,h]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return        void
type
                                                               Determines the element size and number
                                  MW_options
              1 MW
                                  enum                         of stored elements (see enum definition
                                                               at vec-mem-modes.h)
              2 VUX               uint8          0..3          Determines the source VCU
              3 IN1_V32           vec_t                        Input vector operand
Operands      4 IN2_gB_BASE       void *                       Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the
              5 IN3_rI_OFFSET void *
                                                               base pointer
              6 IN3_PART          uint8          LOW,HIGH      Word part which is used for operand 5
              7 IN4_PM_PTR        void*                        Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec_t vIn;
              ...
              vstb_v32_indexed_rIp_pm_ptr_mw_vuX (mw_8w, 1, vIn, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic     vstb_v32_mw_vuX
name
Spec syntax   vstb {mw, vuX [,h]} vix[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                              Determines the element size and number
                                MW_options
              1      MW
                                enum                          of stored elements (see enum definition at
                                                              vec-mem-modes.h)
Operands      2      VUX        uint8          0..3           Determines the source VCU
              3      IN1_V32    vec_t                         Input vector operand
              4      IN2_PTR    void *                        Pointer register (rN)
              void* ptr;
C example     vec_t vIn;
              ...
              vstb_v32_mw_vuX (mw_8w, 1, vIn, ptr);

Comments



Intrinsic     vstb_v32_pm_imm_mw_vuX
name
Spec syntax   vstb {mw, vuX [,h]} vix[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                            Determines the element size and number
                                MW_options

1   MW
                                enum                        of stored elements (see enum definition at
                                                            vec-mem-modes.h)
              2   VUX           uint8          0..3         Determines the source VCU
Operands      3   IN1_V32       vec_t                       Input vector operand
              4   IN2_PTR       void *                      Pointer register (rN)
                                                 31   31    32 bit immediate post modification in
              5   IN3_PM_IMM int32             -2 ..2 -1
                                                            bytes
              void* ptr;
              vec_t vIn;
C example     ...
              vstb_v32_pm_imm_mw_vuX (mw_8w, 1, vIn, ptr, 2);

Comments



Intrinsic     vstb_v32_pm_ptr_mw_vuX
name
Spec          vstb {mw, vuX [,h]} vix[0], (pN)[+pm_x] [,?prSC]
syntax
Return        void
type
                                                             Determines the element size and number
                                MW_options
              1   MW
                                enum                         of stored elements (see enum definition at
                                                             vec-mem-modes.h)
              2   VUX           uint8          0..3          Determines the source VCU
Operands
              3   IN1_V32       vec_t                        Input vector operand
              4   IN2_PTR       void *                       Pointer register (rN)
              5   IN3_PM_PTR void*                           Pointer register (rN)
             void* ptr;
             vec_t vIn;
C example    ...
             vstb_v32_pm_ptr_mw_vuX (mw_8w, 1, vIn, ptr, ptr);

Comments


Main table → Memory Access → Store → Store 8 bit
Available addressing modes
Intrinsic Names:
vstb_v32_indexed_rI_mw_vuX_h
vstb_v32_indexed_rI_pm_imm_mw_vuX_h
vstb_v32_indexed_rI_pm_ptr_mw_vuX_h
vstb_v32_indexed_rIp_mw_vuX_h
vstb_v32_indexed_rIp_pm_imm_mw_vuX_h
vstb_v32_indexed_rIp_pm_ptr_mw_vuX_h
vstb_v32_mw_vuX_h
vstb_v32_pm_imm_mw_vuX_h
vstb_v32_pm_ptr_mw_vuX_h
Intrinsic   vstb_v32_indexed_rI_mw_vuX_h
name
Spec        vstb {mw, vuX [,h]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                                Determines the element size and number
                                MW_options
            1 MW

enum                            of stored elements (see enum definition
                                                                at vec-mem-modes.h)
            2 VUX               uint8          0..3             Determines the source VCU
Operands    3 IN1_V32           vec_t                           Input vector operand
            4 IN2_gB_BASE       void *                          Pointer register (gB)
                                                                Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                                base pointer
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstb_v32_indexed_rI_mw_vuX_h (mw_8w, 1, vIn, ptrBase, ptrModify);

Comments



Intrinsic   vstb_v32_indexed_rI_pm_imm_mw_vuX_h
name
Spec        vstb {mw, vuX [,h]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                                Determines the element size and number
                                MW_options
            1 MW
                                enum                            of stored elements (see enum definition
                                                                at vec-mem-modes.h)
            2 VUX               uint8          0..3             Determines the source VCU
            3 IN1_V32           vec_t                           Input vector operand
Operands
            4 IN2_gB_BASE       void *                          Pointer register (gB)

            5 IN3_rI_OFFSET void *
                                                                Pointer (rI) specifying the offset from the
                                                                base pointer

            6 IN4_PM_IMM                         31   31        32 bit immediate post modification in
                                int32          -2 ..2 -1
                                                                bytes
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstb_v32_indexed_rI_pm_imm_mw_vuX_h (mw_8w, 1, vIn, ptrBase, ptrModify, 2);

Comments



Intrinsic   vstb_v32_indexed_rI_pm_ptr_mw_vuX_h
name
Spec        vstb {mw, vuX [,h]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                                Determines the element size and number

MW_options
            1 MW
                                enum                            of stored elements (see enum definition
                                                                at vec-mem-modes.h)
            2 VUX               uint8          0..3             Determines the source VCU

Operands    3 IN1_V32           vec_t                           Input vector operand
            4 IN2_gB_BASE       void *                          Pointer register (gB)
                                                                Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                                base pointer
            6 IN4_PM_PTR        void*                           Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstb_v32_indexed_rI_pm_ptr_mw_vuX_h (mw_8w, 1, vIn, ptrBase, ptrModify, ptr);

Comments



Intrinsic   vstb_v32_indexed_rIp_mw_vuX_h
name
Spec        vstb {mw,vuX [,h]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                                Determines the element size and number
                                MW_options
Operands    1 MW
                                enum                            of stored elements (see enum definition
                                                                at vec-mem-modes.h)
            2 VUX               uint8         0..3          Determines the source VCU
            3 IN1_V32           vec_t                       Input vector operand
            4 IN2_gB_BASE       void *                      Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                            base pointer
            6 IN3_PART          uint8         LOW,HIGH      Word part which is used for operand 5
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstb_v32_indexed_rIp_mw_vuX_h (mw_8w, 1, vIn, ptrBase, ptrModify, LOW);

Comments



Intrinsic   vstb_v32_indexed_rIp_pm_imm_mw_vuX_h
name
Spec        vstb {mw,vuX [,h]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                            Determines the element size and number

MW_options
            1 MW
                                enum                        of stored elements (see enum definition
                                                            at vec-mem-modes.h)
            2 VUX               uint8         0..3          Determines the source VCU
            3 IN1_V32           vec_t                       Input vector operand
Operands    4 IN2_gB_BASE       void *                      Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                            base pointer
            6 IN3_PART          uint8         LOW,HIGH      Word part which is used for operand 5

            7 IN4_PM_IMM                        31   31     32 bit immediate post modification in
                                int32         -2 ..2 -1
                                                            bytes
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstb_v32_indexed_rIp_pm_imm_mw_vuX_h (mw_8w, 1, vIn, ptrBase, ptrModify, LOW, 2);

Comments
Intrinsic     vstb_v32_indexed_rIp_pm_ptr_mw_vuX_h
name
Spec          vstb {mw,vuX [,h]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return        void
type
                                                               Determines the element size and number
                                  MW_options
              1 MW
                                  enum                         of stored elements (see enum definition
                                                               at vec-mem-modes.h)
              2 VUX               uint8         0..3           Determines the source VCU
              3 IN1_V32           vec_t                        Input vector operand
Operands      4 IN2_gB_BASE       void *                       Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the
              5 IN3_rI_OFFSET void *
                                                               base pointer
              6 IN3_PART          uint8         LOW,HIGH       Word part which is used for operand 5
              7 IN4_PM_PTR        void*                        Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec_t vIn;
              ...

vstb_v32_indexed_rIp_pm_ptr_mw_vuX_h (mw_8w, 1, vIn, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic     vstb_v32_mw_vuX_h
name
Spec syntax   vstb {mw, vuX [,h]} vix[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                              Determines the element size and number
                                MW_options
              1      MW
                                enum                          of stored elements (see enum definition at
                                                              vec-mem-modes.h)
Operands      2      VUX        uint8          0..3           Determines the source VCU
              3      IN1_V32    vec_t                         Input vector operand
              4      IN2_PTR    void *                        Pointer register (rN)
              void* ptr;
C example     vec_t vIn;
              ...
              vstb_v32_mw_vuX_h (mw_8w, 1, vIn, ptr);

Comments



Intrinsic     vstb_v32_pm_imm_mw_vuX_h
name
Spec syntax   vstb {mw, vuX [,h]} vix[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                             Determines the element size and number
                                MW_options
              1   MW
                                enum                         of stored elements (see enum definition at
                                                             vec-mem-modes.h)
              2   VUX           uint8          0..3          Determines the source VCU
Operands      3   IN1_V32       vec_t                        Input vector operand
              4   IN2_PTR       void *                       Pointer register (rN)
                                                 31     31   32 bit immediate post modification in
              5   IN3_PM_IMM int32             -2 ..2 -1
                                                             bytes
              void* ptr;
              vec_t vIn;
C example     ...
              vstb_v32_pm_imm_mw_vuX_h (mw_8w, 1, vIn, ptr, 2);

Comments



Intrinsic     vstb_v32_pm_ptr_mw_vuX_h
name
Spec          vstb {mw, vuX [,h]} vix[0], (pN)[+pm_x] [,?prSC]
syntax
Return        void
type
                                                             Determines the element size and number
                                MW_options
              1   MW
                                enum                         of stored elements (see enum definition at

vec-mem-modes.h)
              2   VUX           uint8         0..3           Determines the source VCU
Operands
              3   IN1_V32       vec_t                        Input vector operand
              4   IN2_PTR       void *                       Pointer register (rN)
              5   IN3_PM_PTR void*                           Pointer register (rN)
            void* ptr;
            vec_t vIn;
C example   ...
            vstb_v32_pm_ptr_mw_vuX_h (mw_8w, 1, vIn, ptr, ptr);

Comments


Main table → Memory Access → Store → Store 8 bit
