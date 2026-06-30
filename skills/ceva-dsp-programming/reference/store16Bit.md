# Memory Access → Store → Store 16 bit

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Memory Access → Store → Store 16 bit

Store 16 bit

Store 16 bit
Store 16 bit word
Available Switches
concat Data concatenation
hp        When used, the high parts are stored in the memory (voxXh, voxX~h,...)
lp        When used, the low parts are stored in the memory (voxXl, voxX~l,...)
mw        Number of word stores. 1w ≤ mw ≤ 8w
pw        Number of word stores. 9w ≤ pw ≤ 16w
vuX       Determines the source VCU of the instruction. voz[0] ≤ vuX ≤ voz[3]
Intrinsic Names
vstw_v32_pw
vstw_v40_vuX
vstw_v40_vuX_hp
vstw_v40_vuX_lp
vstw_v32_pw_vuX
vstw_v40_v40_hp
vstw_v40_v40_hp_concat
vstw_v40_v40_lp
vstw_v40_pw_vuX
vstw_v40_v40_vuX_hp
vstw_v40_v40_vuX_lp
vstw_v32_vuX
vstw_v32_vuX_hp
vstw_v32_vuX_lp
vstw_v40
vstw_v40_concat
vstw_v40_hp
vstw_v40_hp_concat
vstw_v40_lp
vstw_v40_lp_concat
vstw_v32
vstw_v32_concat
vstw_v32_hp
vstw_v32_hp_concat
vstw_v32_lp
vstw_v32_lp_concat
vstw_v40_pw
Instruction details in the instruction set specification
Available addressing modes
Intrinsic Names:
vstw_v32_direct_pw
vstw_v32_indexed_imm_pw
vstw_v32_indexed_rI_pm_imm_pw
vstw_v32_indexed_rI_pm_ptr_pw
vstw_v32_indexed_rI_pw
vstw_v32_indexed_rIp_pm_imm_pw
vstw_v32_indexed_rIp_pm_ptr_pw
vstw_v32_indexed_rIp_pw
vstw_v32_pm_imm_pw
vstw_v32_pm_ptr_pw
vstw_v32_pw
Intrinsic     vstw_v32_direct_pw
name
Spec syntax   vstw {pw} vix[0], [#address] [,?prSC]

Return        void
type
                                                               Determines the element size and number
                                PW_options
              1      PW
                                enum                           of stored elements (see enum definition at
                                                               vec-mem-modes.h)
Operands

2      IN1_V32    vec_t                          Input vector operand
                                                     32
              3      IN2_ADDR   int32          0..2 -1         32 bit address
              vec_t vIn;
C example     ...
              vstw_v32_direct_pw (pw_16w, vIn, 2);

Comments



Intrinsic     vstw_v32_indexed_imm_pw
name
Spec          vstw {pw} vix[0], (gB+#imm16_6) [,?prSC]
syntax
Return        void
type
                                                               Determines the element size and number
                                 PW_options
              1   PW
                                 enum                          of stored elements (see enum definition
                                                               at vec-mem-modes.h)

Operands      2   IN1_V32        vec_t                         Input vector operand
              3   IN2_gB_BASE void *                           Pointer register (gB)

              4
                                                -              16 bit immediate post modification in
                  IN3_IMM16_6    int16
                                                32768..32767   bytes
              void* ptrBase;
              vec_t vIn;
C example     ...
              vstw_v32_indexed_imm_pw (pw_16w, vIn, ptrBase, 2);

Comments



Intrinsic     vstw_v32_indexed_rI_pm_imm_pw
name
Spec          vstw {pw} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 PW_options
            1 PW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_V32            vec_t                        Input vector operand
Operands    3 IN2_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                              base pointer
                                                 31   31      32 bit immediate post modification in
            5 IN4_PM_IMM         int32         -2 ..2 -1
                                                              bytes
            void* ptrBase;
            void* ptrModify;

C example   vec_t vIn;
            ...
            vstw_v32_indexed_rI_pm_imm_pw (pw_16w, vIn, ptrBase, ptrModify, 2);

Comments



Intrinsic   vstw_v32_indexed_rI_pm_ptr_pw
name
Spec        vstw {pw} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 PW_options
            1 PW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_V32            vec_t                        Input vector operand
Operands    3 IN2_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                              base pointer
            5 IN4_PM_PTR         void*                        Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rI_pm_ptr_pw (pw_16w, vIn, ptrBase, ptrModify, ptr);
Comments



Intrinsic   vstw_v32_indexed_rI_pw
name
Spec        vstw {pw} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 PW_options
            1 PW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)

Operands    2 IN1_V32            vec_t                        Input vector operand
            3 IN2_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                              base pointer
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rI_pw (pw_16w, vIn, ptrBase, ptrModify);

Comments



Intrinsic   vstw_v32_indexed_rIp_pm_imm_pw
name
Spec        vstw {pw} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type

Determines the element size and number
                                 PW_options
            1 PW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_V32            vec_t                        Input vector operand
Operands    3 IN2_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                              base pointer
            5 IN3_PART           uint8         LOW,HIGH       Word part which is used for operand 4
                                                 31   31     32 bit immediate post modification in
            6 IN4_PM_IMM        int32          -2 ..2 -1
                                                             bytes
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rIp_pm_imm_pw (pw_16w, vIn, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic   vstw_v32_indexed_rIp_pm_ptr_pw
name
Spec        vstw {pw} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                PW_options
            1 PW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
            2 IN1_V32           vec_t                        Input vector operand

Operands    3 IN2_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                             base pointer
            5 IN3_PART          uint8          LOW,HIGH      Word part which is used for operand 4
            6 IN4_PM_PTR        void*                        Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rIp_pm_ptr_pw (pw_16w, vIn, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic   vstw_v32_indexed_rIp_pw
name

Spec        vstw {pw} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                PW_options
            1 PW
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
            vstw_v32_indexed_rIp_pw (pw_16w, vIn, ptrBase, ptrModify, LOW);

Comments



Intrinsic   vstw_v32_pm_imm_pw
name
Spec        vstw {pw} vix[0], (pN)+#imm32_6 [,?prSC]
syntax
Return      void
type
                                                            Determines the element size and number
                               PW_options
            1   PW
                               enum                         of stored elements (see enum definition at
                                                            vec-mem-modes.h)

Operands    2   IN1_V32        vec_t                        Input vector operand
            3   IN2_PTR        void *                       Pointer register (rN)
                                               31   31      32 bit immediate post modification in
            4   IN3_IMM32_6 int32            -2 ..2 -1
                                                            bytes
            void* ptr;
            vec_t vIn;
C example   ...
            vstw_v32_pm_imm_pw (pw_16w, vIn, ptr, 2);

Comments



Intrinsic   vstw_v32_pm_ptr_pw
name
Spec        vstw {pw} vix[0], (pN)[+pm_x] [,?prSC]
syntax
Return        void
type
                                                            Determines the element size and number
                                 PW_options
              1   PW
                                 enum                       of stored elements (see enum definition at

vec-mem-modes.h)
Operands      2   IN1_V32        vec_t                      Input vector operand
              3   IN2_PTR        void *                     Pointer register (rN)
              4   IN3_PM_PTR void*                          Pointer register (rN)
              void* ptr;
              vec_t vIn;
C example     ...
              vstw_v32_pm_ptr_pw (pw_16w, vIn, ptr, ptr);

Comments



Intrinsic     vstw_v32_pw
name
Spec syntax   vstw {pw} vix[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                            Determines the element size and number
                                 PW_options
              1   PW
                                 enum                       of stored elements (see enum definition at
                                                            vec-mem-modes.h)
Operands
              2   IN1_V32        vec_t                      Input vector operand
              3   IN2_PTR        void *                     Pointer register (rN)
              void* ptr;
              vec_t vIn;
C example     ...
              vstw_v32_pw (pw_16w, vIn, ptr);

Comments


Main table → Memory Access → Store → Store 16 bit
Available addressing modes
Intrinsic Names:
vstw_v40_indexed_rI_pm_imm_vuX
vstw_v40_indexed_rI_pm_ptr_vuX
vstw_v40_indexed_rI_vuX
vstw_v40_indexed_rIp_pm_imm_vuX
vstw_v40_indexed_rIp_pm_ptr_vuX
vstw_v40_indexed_rIp_vuX
vstw_v40_pm_imm_vuX
vstw_v40_pm_ptr_vuX
vstw_v40_vuX
Intrinsic   vstw_v40_indexed_rI_pm_imm_vuX
name
Spec        vstw {mw, vuX [,lp|hp]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                MW_options
            1 MW
                                enum                          of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 VUX               uint8          0..3           Determines the source VCU
            3 IN1_V40           vec40_t                       Output vector operand
                                                              Offset for the first DW used from
Operands    4 IN1_OFST          uint8          0,4
                                                              operand 3
            5 IN2_gB_BASE       void *                        Pointer register (gB)

            6 IN3_rI_OFFSET void *

Pointer (rI) specifying the offset from the
                                                              base pointer
                                                 31   31      32 bit immediate post modification in
            7 IN4_PM_IMM        int32          -2 ..2 -1
                                                              bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rI_pm_imm_vuX (mw_8w, 1, vIn, 0, ptrBase, ptrModify, 2);

Comments



Intrinsic   vstw_v40_indexed_rI_pm_ptr_vuX
name
Spec        vstw {mw, vuX [,lp|hp]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                MW_options
            1 MW
                                enum                          of stored elements (see enum definition
                                                              at vec-mem-modes.h)
Operands    2 VUX               uint8          0..3           Determines the source VCU
            3 IN1_V40           vec40_t                       Output vector operand
            4 IN1_OFST          uint8          0,4            Offset for the first DW used from
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
            vstw_v40_indexed_rI_pm_ptr_vuX (mw_8w, 1, vIn, 0, ptrBase, ptrModify, ptr);

Comments



Intrinsic   vstw_v40_indexed_rI_vuX
name
Spec        vstw {mw, vuX [,lp|hp]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and number
                                 MW_options
            1 MW
                                 enum                          of stored elements (see enum definition
                                                               at vec-mem-modes.h)

2 VUX                uint8          0..3           Determines the source VCU
            3 IN1_V40            vec40_t                       Output vector operand
Operands
            4 IN1_OFST
                                                               Offset for the first DW used from
                                 uint8          0,4
                                                               operand 3
            5 IN2_gB_BASE        void *                        Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the
            6 IN3_rI_OFFSET void *
                                                               base pointer
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rI_vuX (mw_8w, 1, vIn, 0, ptrBase, ptrModify);

Comments



Intrinsic   vstw_v40_indexed_rIp_pm_imm_vuX
name
Spec        vstw {mw,vuX [,lp|hp]} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                MW_options
            1 MW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
            2 VUX               uint8         0..3           Determines the source VCU
            3 IN1_V40           vec40_t                      Output vector operand
                                                             Offset for the first DW used from
            4 IN1_OFST          uint8         0,4
Operands                                                     operand 3
            5 IN2_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            6 IN3_rI_OFFSET void *
                                                             base pointer
            7 IN3_PART          uint8         LOW,HIGH       Word part which is used for operand 6
                                                31   31      32 bit immediate post modification in
            8 IN4_PM_IMM        int32         -2 ..2 -1
                                                             bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...

vstw_v40_indexed_rIp_pm_imm_vuX (mw_8w, 1, vIn, 0, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic   vstw_v40_indexed_rIp_pm_ptr_vuX
name
Spec        vstw {mw,vuX [,lp|hp]} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                MW_options
            1 MW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)

Operands    2 VUX               uint8         0..3           Determines the source VCU
            3 IN1_V40           vec40_t                      Output vector operand

            4 IN1_OFST
                                                             Offset for the first DW used from
                                uint8         0,4
                                                             operand 3
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
            vstw_v40_indexed_rIp_pm_ptr_vuX (mw_8w, 1, vIn, 0, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic   vstw_v40_indexed_rIp_vuX
name
Spec        vstw {mw,vuX [,lp|hp]} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 MW_options
            1 MW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 VUX                uint8         0..3           Determines the source VCU
            3 IN1_V40            vec40_t                      Output vector operand
Operands    4 IN1_OFST
                                                              Offset for the first DW used from

uint8         0,4
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
            vstw_v40_indexed_rIp_vuX (mw_8w, 1, vIn, 0, ptrBase, ptrModify, LOW);

Comments



Intrinsic   vstw_v40_pm_imm_vuX
name
Spec syntax   vstw {mw, vuX [,lp|hp]} vox[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                                Determines the element size and number
                                 MW_options
              1   MW
                                 enum                           of stored elements (see enum definition at
                                                                vec-mem-modes.h)
              2   VUX            uint8         0..3             Determines the source VCU
              3   IN1_V40        vec40_t                        Output vector operand
Operands
              4   IN1_OFST       uint8         0,4              Offset for the first DW used from operand
                                                                3

              5   IN2_PTR        void *                         Pointer register (rN)
                                                 31   31        32 bit immediate post modification in
              6   IN3_PM_IMM int32             -2 ..2 -1
                                                                bytes
              void* ptr;
              vec40_t vIn;
C example     ...
              vstw_v40_pm_imm_vuX (mw_8w, 1, vIn, 0, ptr, 2);

Comments



Intrinsic     vstw_v40_pm_ptr_vuX
name
Spec          vstw {mw, vuX [,lp|hp]} vox[0], (pN)[+pm_x] [,?prSC]
syntax
Return        void
type
                                                                Determines the element size and number
                                MW_options
              1   MW
                                enum                            of stored elements (see enum definition at
                                                                vec-mem-modes.h)

2   VUX           uint8          0..3             Determines the source VCU

Operands      3   IN1_V40       vec40_t                         Output vector operand

              4
                                                                Offset for the first DW used from
                  IN1_OFST      uint8          0,4
                                                                operand 3
              5   IN2_PTR       void *                          Pointer register (rN)
              6   IN3_PM_PTR void*                              Pointer register (rN)
              void* ptr;
C example     vec40_t vIn;
              ...
              vstw_v40_pm_ptr_vuX (mw_8w, 1, vIn, 0, ptr, ptr);

Comments



Intrinsic     vstw_v40_vuX
name
Spec syntax   vstw {mw, vuX [,lp|hp]} vox[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                                  Determines the element size and number
                                 MW_options
              1   MW
                                 enum                             of stored elements (see enum definition at
                                                                  vec-mem-modes.h)
              2   VUX            uint8          0..3              Determines the source VCU
Operands
              3   IN1_V40        vec40_t                          Output vector operand

              4   IN1_OFST       uint8          0,4
                                                                  Offset for the first DW used from operand
                                                                  3

              5   IN2_PTR        void *                           Pointer register (rN)
              void* ptr;
              vec40_t vIn;
C example     ...
              vstw_v40_vuX (mw_8w, 1, vIn, 0, ptr);

Comments


Main table → Memory Access → Store → Store 16 bit
Available addressing modes
Intrinsic Names:
vstw_v40_indexed_rI_pm_imm_vuX_hp
vstw_v40_indexed_rI_pm_ptr_vuX_hp
vstw_v40_indexed_rI_vuX_hp
vstw_v40_indexed_rIp_pm_imm_vuX_hp
vstw_v40_indexed_rIp_pm_ptr_vuX_hp
vstw_v40_indexed_rIp_vuX_hp
vstw_v40_pm_imm_vuX_hp
vstw_v40_pm_ptr_vuX_hp
vstw_v40_vuX_hp
Intrinsic   vstw_v40_indexed_rI_pm_imm_vuX_hp
name
Spec        vstw {mw, vuX [,lp|hp]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                MW_options

1 MW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
            2 VUX               uint8         0..3           Determines the source VCU
            3 IN1_V40           vec40_t                      Output vector operand
Operands
            4 IN2_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                             base pointer

            6 IN4_PM_IMM                        31   31      32 bit immediate post modification in
                                int32         -2 ..2 -1
                                                             bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rI_pm_imm_vuX_hp (mw_8w, 1, vIn, ptrBase, ptrModify, 2);

Comments



Intrinsic   vstw_v40_indexed_rI_pm_ptr_vuX_hp
name
Spec        vstw {mw, vuX [,lp|hp]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                MW_options
            1 MW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
            2 VUX               uint8         0..3           Determines the source VCU
Operands    3 IN1_V40           vec40_t                      Output vector operand
            4 IN2_gB_BASE       void *                       Pointer register (gB)

            5 IN3_rI_OFFSET void *
                                                             Pointer (rI) specifying the offset from the
                                                             base pointer
            6 IN4_PM_PTR         void*                        Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rI_pm_ptr_vuX_hp (mw_8w, 1, vIn, ptrBase, ptrModify, ptr);

Comments



Intrinsic   vstw_v40_indexed_rI_vuX_hp
name
Spec        vstw {mw, vuX [,lp|hp]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type

Determines the element size and number
                                 MW_options
            1 MW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 VUX                uint8         0..3           Determines the source VCU
Operands    3 IN1_V40            vec40_t                      Output vector operand
            4 IN2_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                              base pointer
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rI_vuX_hp (mw_8w, 1, vIn, ptrBase, ptrModify);

Comments



Intrinsic   vstw_v40_indexed_rIp_pm_imm_vuX_hp
name
Spec        vstw {mw,vuX [,lp|hp]} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 MW_options
Operands    1 MW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 VUX               uint8          0..3          Determines the source VCU
            3 IN1_V40           vec40_t                      Output vector operand
            4 IN2_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                             base pointer
            6 IN3_PART          uint8          LOW,HIGH      Word part which is used for operand 5
                                                 31   31     32 bit immediate post modification in
            7 IN4_PM_IMM        int32          -2 ..2 -1
                                                             bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rIp_pm_imm_vuX_hp (mw_8w, 1, vIn, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic   vstw_v40_indexed_rIp_pm_ptr_vuX_hp
name

Spec        vstw {mw,vuX [,lp|hp]} vox[0], (gB+rIp)[+pm] [,?prSC]
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
Operands    4 IN2_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                             base pointer
            6 IN3_PART          uint8          LOW,HIGH      Word part which is used for operand 5
            7 IN4_PM_PTR        void*                        Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rIp_pm_ptr_vuX_hp (mw_8w, 1, vIn, ptrBase, ptrModify, LOW, ptr);

Comments
Intrinsic     vstw_v40_indexed_rIp_vuX_hp
name
Spec          vstw {mw,vuX [,lp|hp]} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return        void
type
                                                               Determines the element size and number
                                  MW_options
              1 MW
                                  enum                         of stored elements (see enum definition
                                                               at vec-mem-modes.h)
              2 VUX               uint8          0..3          Determines the source VCU

Operands      3 IN1_V40           vec40_t                      Output vector operand
              4 IN2_gB_BASE       void *                       Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the
              5 IN3_rI_OFFSET void *
                                                               base pointer
              6 IN3_PART          uint8          LOW,HIGH      Word part which is used for operand 5
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;
              ...

vstw_v40_indexed_rIp_vuX_hp (mw_8w, 1, vIn, ptrBase, ptrModify, LOW);

Comments



Intrinsic     vstw_v40_pm_imm_vuX_hp
name
Spec syntax   vstw {mw, vuX [,lp|hp]} vox[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                              Determines the element size and number
                                 MW_options
              1      MW
                                 enum                         of stored elements (see enum definition at
                                                              vec-mem-modes.h)
              2      VUX         uint8          0..3          Determines the source VCU
Operands      3      IN1_V40     vec40_t                      Output vector operand
              4      IN2_PTR     void *                       Pointer register (rN)

              5                                   31    31    32 bit immediate post modification in
                     IN3_PM_IMM int32           -2 ..2 -1
                                                              bytes
              void* ptr;
              vec40_t vIn;
C example     ...
              vstw_v40_pm_imm_vuX_hp (mw_8w, 1, vIn, ptr, 2);

Comments



Intrinsic     vstw_v40_pm_ptr_vuX_hp
name
Spec          vstw {mw, vuX [,lp|hp]} vox[0], (pN)[+pm_x] [,?prSC]
syntax
Return        void
type
                                                                  Determines the element size and number
                                 MW_options
              1   MW
                                 enum                             of stored elements (see enum definition at
                                                                  vec-mem-modes.h)
              2   VUX            uint8          0..3              Determines the source VCU
Operands
              3   IN1_V40        vec40_t                          Output vector operand
              4   IN2_PTR        void *                           Pointer register (rN)
              5   IN3_PM_PTR void*                                Pointer register (rN)
              void* ptr;
              vec40_t vIn;
C example     ...
              vstw_v40_pm_ptr_vuX_hp (mw_8w, 1, vIn, ptr, ptr);

Comments



Intrinsic     vstw_v40_vuX_hp
name
Spec syntax   vstw {mw, vuX [,lp|hp]} vox[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                                  Determines the element size and number
                                MW_options

1   MW
                                enum                              of stored elements (see enum definition at
                                                                  vec-mem-modes.h)
Operands      2   VUX           uint8          0..3               Determines the source VCU
              3   IN1_V40       vec40_t                           Output vector operand
              4   IN2_PTR       void *                            Pointer register (rN)
              void* ptr;
              vec40_t vIn;
C example     ...
              vstw_v40_vuX_hp (mw_8w, 1, vIn, ptr);

Comments


Main table → Memory Access → Store → Store 16 bit
Available addressing modes
Intrinsic Names:
vstw_v40_indexed_rI_pm_imm_vuX_lp
vstw_v40_indexed_rI_pm_ptr_vuX_lp
vstw_v40_indexed_rI_vuX_lp
vstw_v40_indexed_rIp_pm_imm_vuX_lp
vstw_v40_indexed_rIp_pm_ptr_vuX_lp
vstw_v40_indexed_rIp_vuX_lp
vstw_v40_pm_imm_vuX_lp
vstw_v40_pm_ptr_vuX_lp
vstw_v40_vuX_lp
Intrinsic   vstw_v40_indexed_rI_pm_imm_vuX_lp
name
Spec        vstw {mw, vuX [,lp|hp]} vox[0], (gB+rI)[+pm] [,?prSC]
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
                                                             Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                             base pointer

            6 IN4_PM_IMM                         31   31     32 bit immediate post modification in
                                int32          -2 ..2 -1
                                                             bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rI_pm_imm_vuX_lp (mw_8w, 1, vIn, ptrBase, ptrModify, 2);

Comments



Intrinsic   vstw_v40_indexed_rI_pm_ptr_vuX_lp
name
Spec        vstw {mw, vuX [,lp|hp]} vox[0], (gB+rI)[+pm] [,?prSC]
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

            5 IN3_rI_OFFSET void *
                                                             Pointer (rI) specifying the offset from the
                                                             base pointer
            6 IN4_PM_PTR         void*                        Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rI_pm_ptr_vuX_lp (mw_8w, 1, vIn, ptrBase, ptrModify, ptr);

Comments



Intrinsic   vstw_v40_indexed_rI_vuX_lp
name
Spec        vstw {mw, vuX [,lp|hp]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 MW_options
            1 MW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 VUX                uint8          0..3          Determines the source VCU
Operands    3 IN1_V40            vec40_t                      Output vector operand
            4 IN2_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                              base pointer
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rI_vuX_lp (mw_8w, 1, vIn, ptrBase, ptrModify);

Comments



Intrinsic   vstw_v40_indexed_rIp_pm_imm_vuX_lp
name
Spec        vstw {mw,vuX [,lp|hp]} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 MW_options

Operands    1 MW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 VUX               uint8          0..3           Determines the source VCU
            3 IN1_V40           vec40_t                       Output vector operand
            4 IN2_gB_BASE       void *                        Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                              base pointer
            6 IN3_PART          uint8          LOW,HIGH       Word part which is used for operand 5
                                                 31   31      32 bit immediate post modification in
            7 IN4_PM_IMM        int32          -2 ..2 -1
                                                              bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rIp_pm_imm_vuX_lp (mw_8w, 1, vIn, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic   vstw_v40_indexed_rIp_pm_ptr_vuX_lp
name
Spec        vstw {mw,vuX [,lp|hp]} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                MW_options
            1 MW
                                enum                          of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 VUX               uint8          0..3           Determines the source VCU
            3 IN1_V40           vec40_t                       Output vector operand
Operands    4 IN2_gB_BASE       void *                        Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                              base pointer
            6 IN3_PART          uint8          LOW,HIGH       Word part which is used for operand 5
            7 IN4_PM_PTR        void*                         Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...

vstw_v40_indexed_rIp_pm_ptr_vuX_lp (mw_8w, 1, vIn, ptrBase, ptrModify, LOW, ptr);

Comments
Intrinsic     vstw_v40_indexed_rIp_vuX_lp
name
Spec          vstw {mw,vuX [,lp|hp]} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return        void
type
                                                               Determines the element size and number
                                  MW_options
              1 MW
                                  enum                         of stored elements (see enum definition
                                                               at vec-mem-modes.h)
              2 VUX               uint8          0..3          Determines the source VCU

Operands      3 IN1_V40           vec40_t                      Output vector operand
              4 IN2_gB_BASE       void *                       Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the
              5 IN3_rI_OFFSET void *
                                                               base pointer
              6 IN3_PART          uint8          LOW,HIGH      Word part which is used for operand 5
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;
              ...
              vstw_v40_indexed_rIp_vuX_lp (mw_8w, 1, vIn, ptrBase, ptrModify, LOW);

Comments



Intrinsic     vstw_v40_pm_imm_vuX_lp
name
Spec syntax   vstw {mw, vuX [,lp|hp]} vox[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                              Determines the element size and number
                                 MW_options
              1      MW
                                 enum                         of stored elements (see enum definition at
                                                              vec-mem-modes.h)
              2      VUX         uint8          0..3          Determines the source VCU
Operands      3      IN1_V40     vec40_t                      Output vector operand
              4      IN2_PTR     void *                       Pointer register (rN)

              5                                   31    31    32 bit immediate post modification in
                     IN3_PM_IMM int32           -2 ..2 -1
                                                              bytes
              void* ptr;
              vec40_t vIn;
C example     ...
              vstw_v40_pm_imm_vuX_lp (mw_8w, 1, vIn, ptr, 2);

Comments

Intrinsic     vstw_v40_pm_ptr_vuX_lp
name
Spec          vstw {mw, vuX [,lp|hp]} vox[0], (pN)[+pm_x] [,?prSC]
syntax
Return        void
type
                                                                  Determines the element size and number
                                 MW_options
              1   MW
                                 enum                             of stored elements (see enum definition at
                                                                  vec-mem-modes.h)
              2   VUX            uint8          0..3              Determines the source VCU
Operands
              3   IN1_V40        vec40_t                          Output vector operand
              4   IN2_PTR        void *                           Pointer register (rN)
              5   IN3_PM_PTR void*                                Pointer register (rN)
              void* ptr;
              vec40_t vIn;
C example     ...
              vstw_v40_pm_ptr_vuX_lp (mw_8w, 1, vIn, ptr, ptr);

Comments



Intrinsic     vstw_v40_vuX_lp
name
Spec syntax   vstw {mw, vuX [,lp|hp]} vox[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                                  Determines the element size and number
                                MW_options
              1   MW
                                enum                              of stored elements (see enum definition at
                                                                  vec-mem-modes.h)
Operands      2   VUX           uint8          0..3               Determines the source VCU
              3   IN1_V40       vec40_t                           Output vector operand
              4   IN2_PTR       void *                            Pointer register (rN)
            void* ptr;
            vec40_t vIn;
C example   ...
            vstw_v40_vuX_lp (mw_8w, 1, vIn, ptr);

Comments


Main table → Memory Access → Store → Store 16 bit
Available addressing modes
Intrinsic Names:
vstw_v32_indexed_rI_pm_imm_pw_vuX
vstw_v32_indexed_rI_pm_ptr_pw_vuX
vstw_v32_indexed_rI_pw_vuX
vstw_v32_indexed_rIp_pm_imm_pw_vuX
vstw_v32_indexed_rIp_pm_ptr_pw_vuX
vstw_v32_indexed_rIp_pw_vuX
vstw_v32_pm_imm_pw_vuX
vstw_v32_pm_ptr_pw_vuX
vstw_v32_pw_vuX
Intrinsic   vstw_v32_indexed_rI_pm_imm_pw_vuX
name
Spec        vstw {pw, vuX} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number

PW_options
            1 PW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
            2 VUX               uint8         0..3           Determines the source VCU
            3 IN1_V32           vec_t                        Input vector operand
Operands
            4 IN2_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                             base pointer

            6 IN4_PM_IMM                        31   31      32 bit immediate post modification in
                                int32         -2 ..2 -1
                                                             bytes
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rI_pm_imm_pw_vuX (pw_16w, 1, vIn, ptrBase, ptrModify, 2);

Comments



Intrinsic   vstw_v32_indexed_rI_pm_ptr_pw_vuX
name
Spec        vstw {pw, vuX} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                PW_options
            1 PW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
            2 VUX               uint8         0..3           Determines the source VCU
Operands    3 IN1_V32           vec_t                        Input vector operand
            4 IN2_gB_BASE       void *                       Pointer register (gB)

            5 IN3_rI_OFFSET void *
                                                             Pointer (rI) specifying the offset from the
                                                             base pointer
            6 IN4_PM_PTR         void*                        Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rI_pm_ptr_pw_vuX (pw_16w, 1, vIn, ptrBase, ptrModify, ptr);

Comments



Intrinsic   vstw_v32_indexed_rI_pw_vuX
name
Spec        vstw {pw, vuX} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type

Determines the element size and number
                                 PW_options
            1 PW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 VUX                uint8         0..3           Determines the source VCU
Operands    3 IN1_V32            vec_t                        Input vector operand
            4 IN2_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                              base pointer
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rI_pw_vuX (pw_16w, 1, vIn, ptrBase, ptrModify);

Comments



Intrinsic   vstw_v32_indexed_rIp_pm_imm_pw_vuX
name
Spec        vstw {pw,vuX} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 PW_options
Operands    1 PW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 VUX               uint8          0..3          Determines the source VCU
            3 IN1_V32           vec_t                        Input vector operand
            4 IN2_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                             base pointer
            6 IN3_PART          uint8          LOW,HIGH      Word part which is used for operand 5
                                                 31   31     32 bit immediate post modification in
            7 IN4_PM_IMM        int32          -2 ..2 -1
                                                             bytes
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rIp_pm_imm_pw_vuX (pw_16w, 1, vIn, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic   vstw_v32_indexed_rIp_pm_ptr_pw_vuX
name

Spec        vstw {pw,vuX} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                PW_options
            1 PW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
            2 VUX               uint8          0..3          Determines the source VCU
            3 IN1_V32           vec_t                        Input vector operand
Operands    4 IN2_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                             base pointer
            6 IN3_PART          uint8          LOW,HIGH      Word part which is used for operand 5
            7 IN4_PM_PTR        void*                        Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rIp_pm_ptr_pw_vuX (pw_16w, 1, vIn, ptrBase, ptrModify, LOW, ptr);

Comments
Intrinsic     vstw_v32_indexed_rIp_pw_vuX
name
Spec          vstw {pw,vuX} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return        void
type
                                                               Determines the element size and number
                                  PW_options
              1 PW
                                  enum                         of stored elements (see enum definition
                                                               at vec-mem-modes.h)
              2 VUX               uint8         0..3           Determines the source VCU

Operands      3 IN1_V32           vec_t                        Input vector operand
              4 IN2_gB_BASE       void *                       Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the
              5 IN3_rI_OFFSET void *
                                                               base pointer
              6 IN3_PART          uint8         LOW,HIGH       Word part which is used for operand 5
              void* ptrBase;
              void* ptrModify;
C example     vec_t vIn;
              ...

vstw_v32_indexed_rIp_pw_vuX (pw_16w, 1, vIn, ptrBase, ptrModify, LOW);

Comments



Intrinsic     vstw_v32_pm_imm_pw_vuX
name
Spec syntax   vstw {pw, vuX} vix[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                              Determines the element size and number
                                 PW_options
              1      PW
                                 enum                         of stored elements (see enum definition at
                                                              vec-mem-modes.h)
              2      VUX         uint8          0..3          Determines the source VCU
Operands      3      IN1_V32     vec_t                        Input vector operand
              4      IN2_PTR     void *                       Pointer register (rN)

              5                                   31   31     32 bit immediate post modification in
                     IN3_PM_IMM int32           -2 ..2 -1
                                                              bytes
              void* ptr;
              vec_t vIn;
C example     ...
              vstw_v32_pm_imm_pw_vuX (pw_16w, 1, vIn, ptr, 2);

Comments



Intrinsic     vstw_v32_pm_ptr_pw_vuX
name
Spec          vstw {pw, vuX} vix[0], (pN)[+pm_x] [,?prSC]
syntax
Return        void
type
                                                               Determines the element size and number
                                 PW_options
              1   PW
                                 enum                          of stored elements (see enum definition at
                                                               vec-mem-modes.h)
              2   VUX            uint8         0..3            Determines the source VCU
Operands
              3   IN1_V32        vec_t                         Input vector operand
              4   IN2_PTR        void *                        Pointer register (rN)
              5   IN3_PM_PTR void*                             Pointer register (rN)
              void* ptr;
              vec_t vIn;
C example     ...
              vstw_v32_pm_ptr_pw_vuX (pw_16w, 1, vIn, ptr, ptr);

Comments



Intrinsic     vstw_v32_pw_vuX
name
Spec syntax   vstw {pw, vuX} vix[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                              Determines the element size and number
                                PW_options
              1   PW

enum                          of stored elements (see enum definition at
                                                              vec-mem-modes.h)
Operands      2   VUX           uint8          0..3           Determines the source VCU
              3   IN1_V32       vec_t                         Input vector operand
              4   IN2_PTR       void *                        Pointer register (rN)
            void* ptr;
            vec_t vIn;
C example   ...
            vstw_v32_pw_vuX (pw_16w, 1, vIn, ptr);

Comments


Main table → Memory Access → Store → Store 16 bit
Available addressing modes
Intrinsic Names:
vstw_v40_v40_direct_hp
vstw_v40_v40_hp
vstw_v40_v40_indexed_imm_hp
vstw_v40_v40_indexed_rI_hp
vstw_v40_v40_indexed_rI_pm_imm_hp
vstw_v40_v40_indexed_rI_pm_ptr_hp
vstw_v40_v40_indexed_rIp_hp
vstw_v40_v40_indexed_rIp_pm_imm_hp
vstw_v40_v40_indexed_rIp_pm_ptr_hp
vstw_v40_v40_pm_imm_hp
vstw_v40_v40_pm_ptr_hp
Intrinsic     vstw_v40_v40_direct_hp
name
Spec syntax   vstw {pw, hp [,concat]} vox[0], voy[0], [#address] [,?prSC]

Return        void
type
                                                               Determines the element size and number
                                 PW_options
              1   PW
                                 enum                          of stored elements (see enum definition at
                                                               vec-mem-modes.h)
Operands      2   IN1_V40        vec40_t                       Output vector operand
              3   IN2_V40        vec40_t                       Output vector operand
                                                   32
              4   IN3_ADDR       int32         0..2 -1         32 bit address
              vec40_t vIn;
              vec40_t vIn2;
C example     ...
              vstw_v40_v40_direct_hp (pw_16w, vIn, vIn2, 2);

Comments



Intrinsic     vstw_v40_v40_hp
name
Spec syntax   vstw {pw ,hp [,concat]} vox[0], voy[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                               Determines the element size and number
                                 PW_options
              1   PW
                                 enum                          of stored elements (see enum definition at
                                                               vec-mem-modes.h)
Operands      2   IN1_V40        vec40_t                       Output vector operand

3   IN2_V40        vec40_t                       Output vector operand
              4   IN3_PTR        void *                        Pointer register (rN)
              void* ptr;
              vec40_t vIn;
C example     vec40_t vIn2;
              ...
              vstw_v40_v40_hp (pw_16w, vIn, vIn2, ptr);

Comments



Intrinsic     vstw_v40_v40_indexed_imm_hp
name
Spec        vstw {pw, hp [,concat]} vox[0], voy[0], (gB+#imm16_6) [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and number
                                PW_options
            1   PW
                                enum                           of stored elements (see enum definition
                                                               at vec-mem-modes.h)
            2   IN1_V40         vec40_t                        Output vector operand
Operands    3   IN2_V40         vec40_t                        Output vector operand
            4   IN3_gB_BASE void *                             Pointer register (gB)
                                               -               16 bit immediate post modification in
            5   IN4_IMM16_6     int16
                                               32768..32767    bytes
            void* ptrBase;
            vec40_t vIn;
C example   vec40_t vIn2;
            ...
            vstw_v40_v40_indexed_imm_hp (pw_16w, vIn, vIn2, ptrBase, 2);

Comments



Intrinsic   vstw_v40_v40_indexed_rI_hp
name
Spec        vstw {pw, hp [,concat]} vox[0], voy[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and number
                                 PW_options
            1 PW
                                 enum                          of stored elements (see enum definition
                                                               at vec-mem-modes.h)
            2 IN1_V40            vec40_t                       Output vector operand
Operands    3 IN2_V40            vec40_t                       Output vector operand
            4 IN3_gB_BASE        void *                        Pointer register (gB)

            5 IN4_rI_OFFSET void *
                                                               Pointer (rI) specifying the offset from the
                                                               base pointer
            void* ptrBase;
            void* ptrModify;

vec40_t vIn;
C example   vec40_t vIn2;
            ...
            vstw_v40_v40_indexed_rI_hp (pw_16w, vIn, vIn2, ptrBase, ptrModify);
Comments



Intrinsic   vstw_v40_v40_indexed_rI_pm_imm_hp
name
Spec        vstw {pw, hp [,concat]} vox[0], voy[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                PW_options
            1 PW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
            2 IN1_V40           vec40_t                      Output vector operand
            3 IN2_V40           vec40_t                      Output vector operand
Operands
            4 IN3_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            5 IN4_rI_OFFSET void *
                                                             base pointer

            6 IN5_PM_IMM                         31   31     32 bit immediate post modification in
                                int32          -2 ..2 -1
                                                             bytes
            void* ptrBase;
            void* ptrModify;
            vec40_t vIn;
C example   vec40_t vIn2;
            ...
            vstw_v40_v40_indexed_rI_pm_imm_hp (pw_16w, vIn, vIn2, ptrBase, ptrModify, 2);

Comments



Intrinsic   vstw_v40_v40_indexed_rI_pm_ptr_hp
name
Spec        vstw {pw, hp [,concat]} vox[0], voy[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                PW_options
            1 PW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
Operands
            2 IN1_V40           vec40_t                      Output vector operand
            3 IN2_V40           vec40_t                      Output vector operand
            4 IN3_gB_BASE        void *                        Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the
            5 IN4_rI_OFFSET void *

base pointer
            6 IN5_PM_PTR         void*                         Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            vec40_t vIn2;
            ...
            vstw_v40_v40_indexed_rI_pm_ptr_hp (pw_16w, vIn, vIn2, ptrBase, ptrModify, ptr);

Comments



Intrinsic   vstw_v40_v40_indexed_rIp_hp
name
Spec        vstw {pw, hp [,concat]} vox[0], voy[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and number
                                 PW_options
            1 PW
                                 enum                          of stored elements (see enum definition
                                                               at vec-mem-modes.h)
            2 IN1_V40            vec40_t                       Output vector operand

Operands    3 IN2_V40            vec40_t                       Output vector operand
            4 IN3_gB_BASE        void *                        Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the
            5 IN4_rI_OFFSET void *
                                                               base pointer
            6 IN4_PART           uint8          LOW,HIGH       Word part which is used for operand 5
            void* ptrBase;
            void* ptrModify;
            vec40_t vIn;
C example   vec40_t vIn2;
            ...
            vstw_v40_v40_indexed_rIp_hp (pw_16w, vIn, vIn2, ptrBase, ptrModify, LOW);

Comments



Intrinsic   vstw_v40_v40_indexed_rIp_pm_imm_hp
name
Spec        vstw {pw, hp [,concat]} vox[0], voy[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                            Determines the element size and number
                                PW_options
            1 PW
                                enum                        of stored elements (see enum definition
                                                            at vec-mem-modes.h)
            2 IN1_V40           vec40_t                     Output vector operand
            3 IN2_V40           vec40_t                     Output vector operand
Operands    4 IN3_gB_BASE       void *                      Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the

5 IN4_rI_OFFSET void *
                                                            base pointer
            6 IN4_PART          uint8         LOW,HIGH      Word part which is used for operand 5
                                                31   31     32 bit immediate post modification in
            7 IN5_PM_IMM        int32         -2 ..2 -1
                                                            bytes
            void* ptrBase;
            void* ptrModify;
            vec40_t vIn;
C example   vec40_t vIn2;
            ...
            vstw_v40_v40_indexed_rIp_pm_imm_hp (pw_16w, vIn, vIn2, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic   vstw_v40_v40_indexed_rIp_pm_ptr_hp
name
Spec        vstw {pw, hp [,concat]} vox[0], voy[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                            Determines the element size and number
                                PW_options
            1 PW
                                enum                        of stored elements (see enum definition
                                                            at vec-mem-modes.h)
            2 IN1_V40           vec40_t                     Output vector operand

Operands    3 IN2_V40           vec40_t                     Output vector operand
            4 IN3_gB_BASE       void *                      Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
            5 IN4_rI_OFFSET void *
                                                            base pointer
            6 IN4_PART          uint8         LOW,HIGH      Word part which is used for operand 5
            7 IN5_PM_PTR         void*                        Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            vec40_t vIn2;
            ...
            vstw_v40_v40_indexed_rIp_pm_ptr_hp (pw_16w, vIn, vIn2, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic   vstw_v40_v40_pm_imm_hp
name
Spec        vstw {pw, hp [,concat]} vox[0], voy[0], (pN)+#imm32_6 [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                               PW_options
            1   PW
                               enum                          of stored elements (see enum definition at

vec-mem-modes.h)
            2   IN1_V40        vec40_t                       Output vector operand
Operands    3   IN2_V40        vec40_t                       Output vector operand
            4   IN3_PTR        void *                        Pointer register (rN)
                                                31   31      32 bit immediate post modification in
            5   IN4_IMM32_6 int32             -2 ..2 -1
                                                             bytes
            void* ptr;
            vec40_t vIn;
C example   vec40_t vIn2;
            ...
            vstw_v40_v40_pm_imm_hp (pw_16w, vIn, vIn2, ptr, 2);

Comments



Intrinsic   vstw_v40_v40_pm_ptr_hp
name
Spec        vstw {pw ,hp [,concat]} vox[0], voy[0], (pN)[+pm_x] [,?prSC]
syntax
Return      void
type
                               PW_options                    Determines the element size and number
Operands    1   PW
                               enum                          of stored elements (see enum definition at
                                                               vec-mem-modes.h)
             2   IN1_V40        vec40_t                        Output vector operand
             3   IN2_V40        vec40_t                        Output vector operand
             4   IN3_PTR        void *                         Pointer register (rN)
             5   IN4_PM_PTR void*                              Pointer register (rN)
             void* ptr;
             vec40_t vIn;
C example    vec40_t vIn2;
             ...
             vstw_v40_v40_pm_ptr_hp (pw_16w, vIn, vIn2, ptr, ptr);

Comments


Main table → Memory Access → Store → Store 16 bit
Available addressing modes
Intrinsic Names:
vstw_v40_v40_direct_hp_concat
vstw_v40_v40_hp_concat
vstw_v40_v40_indexed_imm_hp_concat
vstw_v40_v40_indexed_rI_hp_concat
vstw_v40_v40_indexed_rI_pm_imm_hp_concat
vstw_v40_v40_indexed_rI_pm_ptr_hp_concat
vstw_v40_v40_indexed_rIp_hp_concat
vstw_v40_v40_indexed_rIp_pm_imm_hp_concat
vstw_v40_v40_indexed_rIp_pm_ptr_hp_concat
vstw_v40_v40_pm_imm_hp_concat
vstw_v40_v40_pm_ptr_hp_concat
Intrinsic     vstw_v40_v40_direct_hp_concat
name
Spec syntax   vstw {pw, hp [,concat]} vox[0], voy[0], [#address] [,?prSC]

Return        void
type
                                                                 Determines the element size and number
                                PW_options
              1   PW

enum                             of stored elements (see enum definition at
                                                                 vec-mem-modes.h)
Operands      2   IN1_V40       vec40_t                          Output vector operand
              3   IN2_V40       vec40_t                          Output vector operand
                                                   32
              4   IN3_ADDR      int32          0..2 -1           32 bit address
              vec40_t vIn;
              vec40_t vIn2;
C example     ...
              vstw_v40_v40_direct_hp_concat (pw_16w, vIn, vIn2, 2);

Comments



Intrinsic     vstw_v40_v40_hp_concat
name
Spec syntax   vstw {pw ,hp [,concat]} vox[0], voy[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                                 Determines the element size and number
                                PW_options
              1   PW
                                enum                             of stored elements (see enum definition at
                                                                 vec-mem-modes.h)
Operands      2   IN1_V40       vec40_t                          Output vector operand
              3   IN2_V40       vec40_t                          Output vector operand
              4   IN3_PTR       void *                           Pointer register (rN)
              void* ptr;
              vec40_t vIn;
C example     vec40_t vIn2;
              ...
              vstw_v40_v40_hp_concat (pw_16w, vIn, vIn2, ptr);

Comments



Intrinsic     vstw_v40_v40_indexed_imm_hp_concat
name
Spec        vstw {pw, hp [,concat]} vox[0], voy[0], (gB+#imm16_6) [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                PW_options
            1   PW
                                enum                          of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2   IN1_V40         vec40_t                       Output vector operand
Operands    3   IN2_V40         vec40_t                       Output vector operand
            4   IN3_gB_BASE void *                            Pointer register (gB)
                                               -              16 bit immediate post modification in
            5   IN4_IMM16_6     int16

32768..32767   bytes
            void* ptrBase;
            vec40_t vIn;
C example   vec40_t vIn2;
            ...
            vstw_v40_v40_indexed_imm_hp_concat (pw_16w, vIn, vIn2, ptrBase, 2);

Comments



Intrinsic   vstw_v40_v40_indexed_rI_hp_concat
name
Spec        vstw {pw, hp [,concat]} vox[0], voy[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 PW_options
            1 PW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_V40            vec40_t                      Output vector operand
Operands    3 IN2_V40            vec40_t                      Output vector operand
            4 IN3_gB_BASE        void *                       Pointer register (gB)

            5 IN4_rI_OFFSET void *
                                                              Pointer (rI) specifying the offset from the
                                                              base pointer
            void* ptrBase;
            void* ptrModify;
            vec40_t vIn;
C example   vec40_t vIn2;
            ...
            vstw_v40_v40_indexed_rI_hp_concat (pw_16w, vIn, vIn2, ptrBase, ptrModify);
Comments



Intrinsic   vstw_v40_v40_indexed_rI_pm_imm_hp_concat
name
Spec        vstw {pw, hp [,concat]} vox[0], voy[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                PW_options
            1 PW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
            2 IN1_V40           vec40_t                      Output vector operand
            3 IN2_V40           vec40_t                      Output vector operand
Operands
            4 IN3_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            5 IN4_rI_OFFSET void *
                                                             base pointer

            6 IN5_PM_IMM                         31   31     32 bit immediate post modification in

int32          -2 ..2 -1
                                                             bytes
            void* ptrBase;
            void* ptrModify;
            vec40_t vIn;
C example   vec40_t vIn2;
            ...
            vstw_v40_v40_indexed_rI_pm_imm_hp_concat (pw_16w, vIn, vIn2, ptrBase, ptrModify, 2);

Comments



Intrinsic   vstw_v40_v40_indexed_rI_pm_ptr_hp_concat
name
Spec        vstw {pw, hp [,concat]} vox[0], voy[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                PW_options
            1 PW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
Operands
            2 IN1_V40           vec40_t                      Output vector operand
            3 IN2_V40           vec40_t                      Output vector operand
            4 IN3_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            5 IN4_rI_OFFSET void *
                                                              base pointer
            6 IN5_PM_PTR         void*                        Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            vec40_t vIn2;
            ...
            vstw_v40_v40_indexed_rI_pm_ptr_hp_concat (pw_16w, vIn, vIn2, ptrBase, ptrModify, ptr);

Comments



Intrinsic   vstw_v40_v40_indexed_rIp_hp_concat
name
Spec        vstw {pw, hp [,concat]} vox[0], voy[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 PW_options
            1 PW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_V40            vec40_t                      Output vector operand

Operands    3 IN2_V40            vec40_t                      Output vector operand
            4 IN3_gB_BASE        void *                       Pointer register (gB)

Pointer (rI) specifying the offset from the
            5 IN4_rI_OFFSET void *
                                                              base pointer
            6 IN4_PART           uint8         LOW,HIGH       Word part which is used for operand 5
            void* ptrBase;
            void* ptrModify;
            vec40_t vIn;
C example   vec40_t vIn2;
            ...
            vstw_v40_v40_indexed_rIp_hp_concat (pw_16w, vIn, vIn2, ptrBase, ptrModify, LOW);

Comments



Intrinsic   vstw_v40_v40_indexed_rIp_pm_imm_hp_concat
name
Spec        vstw {pw, hp [,concat]} vox[0], voy[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                            Determines the element size and number
                                PW_options
            1 PW
                                enum                        of stored elements (see enum definition
                                                            at vec-mem-modes.h)
            2 IN1_V40           vec40_t                     Output vector operand
            3 IN2_V40           vec40_t                     Output vector operand
Operands    4 IN3_gB_BASE       void *                      Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
            5 IN4_rI_OFFSET void *
                                                            base pointer
            6 IN4_PART          uint8         LOW,HIGH      Word part which is used for operand 5
                                                31   31     32 bit immediate post modification in
            7 IN5_PM_IMM        int32         -2 ..2 -1
                                                            bytes
            void* ptrBase;
            void* ptrModify;
            vec40_t vIn;
C example   vec40_t vIn2;
            ...
            vstw_v40_v40_indexed_rIp_pm_imm_hp_concat (pw_16w, vIn, vIn2, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic   vstw_v40_v40_indexed_rIp_pm_ptr_hp_concat
name
Spec        vstw {pw, hp [,concat]} vox[0], voy[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                            Determines the element size and number
                                PW_options
            1 PW
                                enum                        of stored elements (see enum definition

at vec-mem-modes.h)
            2 IN1_V40           vec40_t                     Output vector operand

Operands    3 IN2_V40           vec40_t                     Output vector operand
            4 IN3_gB_BASE       void *                      Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
            5 IN4_rI_OFFSET void *
                                                            base pointer
            6 IN4_PART          uint8         LOW,HIGH      Word part which is used for operand 5
            7 IN5_PM_PTR         void*                        Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            vec40_t vIn2;
            ...
            vstw_v40_v40_indexed_rIp_pm_ptr_hp_concat (pw_16w, vIn, vIn2, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic   vstw_v40_v40_pm_imm_hp_concat
name
Spec        vstw {pw, hp [,concat]} vox[0], voy[0], (pN)+#imm32_6 [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                               PW_options
            1   PW
                               enum                          of stored elements (see enum definition at
                                                             vec-mem-modes.h)
            2   IN1_V40        vec40_t                       Output vector operand
Operands    3   IN2_V40        vec40_t                       Output vector operand
            4   IN3_PTR        void *                        Pointer register (rN)
                                                31   31      32 bit immediate post modification in
            5   IN4_IMM32_6 int32             -2 ..2 -1
                                                             bytes
            void* ptr;
            vec40_t vIn;
C example   vec40_t vIn2;
            ...
            vstw_v40_v40_pm_imm_hp_concat (pw_16w, vIn, vIn2, ptr, 2);

Comments



Intrinsic   vstw_v40_v40_pm_ptr_hp_concat
name
Spec        vstw {pw ,hp [,concat]} vox[0], voy[0], (pN)[+pm_x] [,?prSC]
syntax
Return      void
type
                               PW_options                    Determines the element size and number
Operands    1   PW
                               enum                          of stored elements (see enum definition at

vec-mem-modes.h)
            2   IN1_V40        vec40_t                       Output vector operand
            3   IN2_V40        vec40_t                       Output vector operand
            4   IN3_PTR        void *                        Pointer register (rN)
            5   IN4_PM_PTR void*                             Pointer register (rN)
            void* ptr;
            vec40_t vIn;
C example   vec40_t vIn2;
            ...
            vstw_v40_v40_pm_ptr_hp_concat (pw_16w, vIn, vIn2, ptr, ptr);

Comments


Main table → Memory Access → Store → Store 16 bit
Available addressing modes
Intrinsic Names:
vstw_v40_v40_direct_lp
vstw_v40_v40_indexed_imm_lp
vstw_v40_v40_indexed_rI_lp
vstw_v40_v40_indexed_rI_pm_imm_lp
vstw_v40_v40_indexed_rI_pm_ptr_lp
vstw_v40_v40_indexed_rIp_lp
vstw_v40_v40_indexed_rIp_pm_imm_lp
vstw_v40_v40_indexed_rIp_pm_ptr_lp
vstw_v40_v40_lp
vstw_v40_v40_pm_imm_lp
vstw_v40_v40_pm_ptr_lp
Intrinsic     vstw_v40_v40_direct_lp
name
Spec syntax   vstw {pw, lp} vox[0], voy[0], [#address] [,?prSC]

Return        void
type
                                                                Determines the element size and number
                                 PW_options
              1      PW
                                 enum                           of stored elements (see enum definition at
                                                                vec-mem-modes.h)
Operands      2      IN1_V40     vec40_t                        Output vector operand
              3      IN2_V40     vec40_t                        Output vector operand
                                                   32
              4      IN3_ADDR    int32          0..2 -1         32 bit address
              vec40_t vIn;
              vec40_t vIn2;
C example     ...
              vstw_v40_v40_direct_lp (pw_16w, vIn, vIn2, 2);

Comments



Intrinsic     vstw_v40_v40_indexed_imm_lp
name
Spec          vstw {pw, lp} vox[0], voy[0], (gB+#imm16_6) [,?prSC]
syntax
Return        void
type
                                                                Determines the element size and number
                                  PW_options
              1   PW
                                  enum                          of stored elements (see enum definition
                                                                at vec-mem-modes.h)
              2   IN1_V40         vec40_t                       Output vector operand

Operands      3   IN2_V40         vec40_t                       Output vector operand
              4   IN3_gB_BASE void *                            Pointer register (gB)
                                                 -              16 bit immediate post modification in
              5   IN4_IMM16_6     int16
                                                 32768..32767   bytes
              void* ptrBase;
              vec40_t vIn;
C example     vec40_t vIn2;
              ...
              vstw_v40_v40_indexed_imm_lp (pw_16w, vIn, vIn2, ptrBase, 2);

Comments
Intrinsic   vstw_v40_v40_indexed_rI_lp
name
Spec        vstw {pw, lp} vox[0], voy[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and number
                                 PW_options
            1 PW
                                 enum                          of stored elements (see enum definition
                                                               at vec-mem-modes.h)
            2 IN1_V40            vec40_t                       Output vector operand
Operands    3 IN2_V40            vec40_t                       Output vector operand
            4 IN3_gB_BASE        void *                        Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the
            5 IN4_rI_OFFSET void *
                                                               base pointer
            void* ptrBase;
            void* ptrModify;
            vec40_t vIn;
C example   vec40_t vIn2;
            ...
            vstw_v40_v40_indexed_rI_lp (pw_16w, vIn, vIn2, ptrBase, ptrModify);

Comments



Intrinsic   vstw_v40_v40_indexed_rI_pm_imm_lp
name
Spec        vstw {pw, lp} vox[0], voy[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and number
                                 PW_options
            1 PW
                                 enum                          of stored elements (see enum definition
                                                               at vec-mem-modes.h)
            2 IN1_V40            vec40_t                       Output vector operand
Operands    3 IN2_V40            vec40_t                       Output vector operand
            4 IN3_gB_BASE        void *                        Pointer register (gB)

Pointer (rI) specifying the offset from the
            5 IN4_rI_OFFSET void *
                                                               base pointer
                                                  31   31      32 bit immediate post modification in
            6 IN5_PM_IMM         int32          -2 ..2 -1
                                                               bytes
            void* ptrBase;
            void* ptrModify;
            vec40_t vIn;
C example   vec40_t vIn2;
            ...
            vstw_v40_v40_indexed_rI_pm_imm_lp (pw_16w, vIn, vIn2, ptrBase, ptrModify, 2);

Comments



Intrinsic   vstw_v40_v40_indexed_rI_pm_ptr_lp
name
Spec        vstw {pw, lp} vox[0], voy[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and number
                                 PW_options
            1 PW
                                 enum                          of stored elements (see enum definition
                                                               at vec-mem-modes.h)
            2 IN1_V40            vec40_t                       Output vector operand

Operands    3 IN2_V40            vec40_t                       Output vector operand
            4 IN3_gB_BASE        void *                        Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the
            5 IN4_rI_OFFSET void *
                                                               base pointer
            6 IN5_PM_PTR         void*                         Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            vec40_t vIn2;
            ...
            vstw_v40_v40_indexed_rI_pm_ptr_lp (pw_16w, vIn, vIn2, ptrBase, ptrModify, ptr);

Comments



Intrinsic   vstw_v40_v40_indexed_rIp_lp
name
Spec        vstw {pw, lp} vox[0], voy[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 PW_options
            1 PW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_V40            vec40_t                      Output vector operand

Operands    3 IN2_V40            vec40_t                      Output vector operand
            4 IN3_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            5 IN4_rI_OFFSET void *
                                                              base pointer
            6 IN4_PART           uint8         LOW,HIGH       Word part which is used for operand 5
            void* ptrBase;
            void* ptrModify;
            vec40_t vIn;
C example   vec40_t vIn2;
            ...
            vstw_v40_v40_indexed_rIp_lp (pw_16w, vIn, vIn2, ptrBase, ptrModify, LOW);

Comments



Intrinsic   vstw_v40_v40_indexed_rIp_pm_imm_lp
name
Spec        vstw {pw, lp} vox[0], voy[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 PW_options
            1 PW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_V40            vec40_t                      Output vector operand
            3 IN2_V40            vec40_t                      Output vector operand
Operands    4 IN3_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            5 IN4_rI_OFFSET void *
                                                              base pointer
            6 IN4_PART           uint8         LOW,HIGH       Word part which is used for operand 5
                                                 31   31      32 bit immediate post modification in
            7 IN5_PM_IMM         int32         -2 ..2 -1
                                                              bytes
            void* ptrBase;
C example   void* ptrModify;
            vec40_t vIn;
              vec40_t vIn2;
              ...
              vstw_v40_v40_indexed_rIp_pm_imm_lp (pw_16w, vIn, vIn2, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic     vstw_v40_v40_indexed_rIp_pm_ptr_lp
name
Spec          vstw {pw, lp} vox[0], voy[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return        void
type
                                                                Determines the element size and number

PW_options
              1 PW
                                   enum                         of stored elements (see enum definition
                                                                at vec-mem-modes.h)
              2 IN1_V40            vec40_t                      Output vector operand
              3 IN2_V40            vec40_t                      Output vector operand
Operands      4 IN3_gB_BASE        void *                       Pointer register (gB)
                                                                Pointer (rI) specifying the offset from the
              5 IN4_rI_OFFSET void *
                                                                base pointer
              6 IN4_PART           uint8         LOW,HIGH       Word part which is used for operand 5
              7 IN5_PM_PTR         void*                        Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;
              vec40_t vIn2;
              ...
              vstw_v40_v40_indexed_rIp_pm_ptr_lp (pw_16w, vIn, vIn2, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic     vstw_v40_v40_lp
name
Spec syntax   vstw {pw ,lp} vox[0], voy[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                               Determines the element size and number
                                 PW_options
Operands      1      PW
                                 enum                          of stored elements (see enum definition at
                                                               vec-mem-modes.h)
            2   IN1_V40        vec40_t                       Output vector operand
            3   IN2_V40        vec40_t                       Output vector operand
            4   IN3_PTR        void *                        Pointer register (rN)
            void* ptr;
            vec40_t vIn;
C example   vec40_t vIn2;
            ...
            vstw_v40_v40_lp (pw_16w, vIn, vIn2, ptr);

Comments



Intrinsic   vstw_v40_v40_pm_imm_lp
name
Spec        vstw {pw, lp} vox[0], voy[0], (pN)+#imm32_6 [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                               PW_options
            1   PW
                               enum                          of stored elements (see enum definition at

vec-mem-modes.h)
            2   IN1_V40        vec40_t                       Output vector operand
Operands    3   IN2_V40        vec40_t                       Output vector operand
            4   IN3_PTR        void *                        Pointer register (rN)
                                                 31     31   32 bit immediate post modification in
            5   IN4_IMM32_6 int32              -2 ..2 -1
                                                             bytes
            void* ptr;
            vec40_t vIn;
C example   vec40_t vIn2;
            ...
            vstw_v40_v40_pm_imm_lp (pw_16w, vIn, vIn2, ptr, 2);

Comments



Intrinsic   vstw_v40_v40_pm_ptr_lp
name
Spec        vstw {pw ,lp} vox[0], voy[0], (pN)[+pm_x] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                               PW_options
            1   PW
                               enum                           of stored elements (see enum definition at
                                                              vec-mem-modes.h)
            2   IN1_V40        vec40_t                        Output vector operand
Operands
            3   IN2_V40        vec40_t                        Output vector operand
            4   IN3_PTR        void *                         Pointer register (rN)
            5   IN4_PM_PTR void*                              Pointer register (rN)
            void* ptr;
            vec40_t vIn;
C example   vec40_t vIn2;
            ...
            vstw_v40_v40_pm_ptr_lp (pw_16w, vIn, vIn2, ptr, ptr);

Comments


Main table → Memory Access → Store → Store 16 bit
Available addressing modes
Intrinsic Names:
vstw_v40_indexed_rI_pm_imm_pw_vuX
vstw_v40_indexed_rI_pm_ptr_pw_vuX
vstw_v40_indexed_rI_pw_vuX
vstw_v40_indexed_rIp_pm_imm_pw_vuX
vstw_v40_indexed_rIp_pm_ptr_pw_vuX
vstw_v40_indexed_rIp_pw_vuX
vstw_v40_pm_imm_pw_vuX
vstw_v40_pm_ptr_pw_vuX
vstw_v40_pw_vuX
Intrinsic   vstw_v40_indexed_rI_pm_imm_pw_vuX
name
Spec        vstw {pw, vuX} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                PW_options
            1 PW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)

2 VUX               uint8         0..3           Determines the source VCU
            3 IN1_V40           vec40_t                      Output vector operand
Operands
            4 IN2_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                             base pointer

            6 IN4_PM_IMM                        31   31      32 bit immediate post modification in
                                int32         -2 ..2 -1
                                                             bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rI_pm_imm_pw_vuX (pw_16w, 1, vIn, ptrBase, ptrModify, 2);

Comments



Intrinsic   vstw_v40_indexed_rI_pm_ptr_pw_vuX
name
Spec        vstw {pw, vuX} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                PW_options
            1 PW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
            2 VUX               uint8         0..3           Determines the source VCU
Operands    3 IN1_V40           vec40_t                      Output vector operand
            4 IN2_gB_BASE       void *                       Pointer register (gB)

            5 IN3_rI_OFFSET void *
                                                             Pointer (rI) specifying the offset from the
                                                             base pointer
            6 IN4_PM_PTR         void*                        Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rI_pm_ptr_pw_vuX (pw_16w, 1, vIn, ptrBase, ptrModify, ptr);

Comments



Intrinsic   vstw_v40_indexed_rI_pw_vuX
name
Spec        vstw {pw, vuX} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 PW_options
            1 PW

enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 VUX                uint8         0..3           Determines the source VCU
Operands    3 IN1_V40            vec40_t                      Output vector operand
            4 IN2_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                              base pointer
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rI_pw_vuX (pw_16w, 1, vIn, ptrBase, ptrModify);

Comments



Intrinsic   vstw_v40_indexed_rIp_pm_imm_pw_vuX
name
Spec        vstw {pw,vuX} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 PW_options
Operands    1 PW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 VUX               uint8          0..3          Determines the source VCU
            3 IN1_V40           vec40_t                      Output vector operand
            4 IN2_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                             base pointer
            6 IN3_PART          uint8          LOW,HIGH      Word part which is used for operand 5
                                                 31   31     32 bit immediate post modification in
            7 IN4_PM_IMM        int32          -2 ..2 -1
                                                             bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rIp_pm_imm_pw_vuX (pw_16w, 1, vIn, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic   vstw_v40_indexed_rIp_pm_ptr_pw_vuX
name
Spec        vstw {pw,vuX} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type

Determines the element size and number
                                PW_options
            1 PW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
            2 VUX               uint8          0..3          Determines the source VCU
            3 IN1_V40           vec40_t                      Output vector operand
Operands    4 IN2_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                             base pointer
            6 IN3_PART          uint8          LOW,HIGH      Word part which is used for operand 5
            7 IN4_PM_PTR        void*                        Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rIp_pm_ptr_pw_vuX (pw_16w, 1, vIn, ptrBase, ptrModify, LOW, ptr);

Comments
Intrinsic     vstw_v40_indexed_rIp_pw_vuX
name
Spec          vstw {pw,vuX} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return        void
type
                                                               Determines the element size and number
                                  PW_options
              1 PW
                                  enum                         of stored elements (see enum definition
                                                               at vec-mem-modes.h)
              2 VUX               uint8         0..3           Determines the source VCU

Operands      3 IN1_V40           vec40_t                      Output vector operand
              4 IN2_gB_BASE       void *                       Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the
              5 IN3_rI_OFFSET void *
                                                               base pointer
              6 IN3_PART          uint8         LOW,HIGH       Word part which is used for operand 5
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;
              ...
              vstw_v40_indexed_rIp_pw_vuX (pw_16w, 1, vIn, ptrBase, ptrModify, LOW);

Comments



Intrinsic     vstw_v40_pm_imm_pw_vuX
name

Spec syntax   vstw {pw, vuX} vox[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                              Determines the element size and number
                                 PW_options
              1      PW
                                 enum                         of stored elements (see enum definition at
                                                              vec-mem-modes.h)
              2      VUX         uint8          0..3          Determines the source VCU
Operands      3      IN1_V40     vec40_t                      Output vector operand
              4      IN2_PTR     void *                       Pointer register (rN)

              5                                   31   31     32 bit immediate post modification in
                     IN3_PM_IMM int32           -2 ..2 -1
                                                              bytes
              void* ptr;
              vec40_t vIn;
C example     ...
              vstw_v40_pm_imm_pw_vuX (pw_16w, 1, vIn, ptr, 2);

Comments



Intrinsic     vstw_v40_pm_ptr_pw_vuX
name
Spec          vstw {pw, vuX} vox[0], (pN)[+pm_x] [,?prSC]
syntax
Return        void
type
                                                               Determines the element size and number
                                 PW_options
              1   PW
                                 enum                          of stored elements (see enum definition at
                                                               vec-mem-modes.h)
              2   VUX            uint8         0..3            Determines the source VCU
Operands
              3   IN1_V40        vec40_t                       Output vector operand
              4   IN2_PTR        void *                        Pointer register (rN)
              5   IN3_PM_PTR void*                             Pointer register (rN)
              void* ptr;
              vec40_t vIn;
C example     ...
              vstw_v40_pm_ptr_pw_vuX (pw_16w, 1, vIn, ptr, ptr);

Comments



Intrinsic     vstw_v40_pw_vuX
name
Spec syntax   vstw {pw, vuX} vox[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                              Determines the element size and number
                                PW_options
              1   PW
                                enum                          of stored elements (see enum definition at

vec-mem-modes.h)
Operands      2   VUX           uint8          0..3           Determines the source VCU
              3   IN1_V40       vec40_t                       Output vector operand
              4   IN2_PTR       void *                        Pointer register (rN)
            void* ptr;
            vec40_t vIn;
C example   ...
            vstw_v40_pw_vuX (pw_16w, 1, vIn, ptr);

Comments


Main table → Memory Access → Store → Store 16 bit
Available addressing modes
Intrinsic Names:
vstw_v40_v40_indexed_rI_pm_imm_vuX_hp
vstw_v40_v40_indexed_rI_pm_ptr_vuX_hp
vstw_v40_v40_indexed_rI_vuX_hp
vstw_v40_v40_indexed_rIp_pm_imm_vuX_hp
vstw_v40_v40_indexed_rIp_pm_ptr_vuX_hp
vstw_v40_v40_indexed_rIp_vuX_hp
vstw_v40_v40_pm_imm_vuX_hp
vstw_v40_v40_pm_ptr_vuX_hp
vstw_v40_v40_vuX_hp
Intrinsic   vstw_v40_v40_indexed_rI_pm_imm_vuX_hp
name
Spec        vstw {pw, vuX, hp} vox[0], voy[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                PW_options
            1 PW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
            2 VUX               uint8          0..3          Determines the source VCU
            3 IN1_V40           vec40_t                      Output vector operand
Operands    4 IN2_V40           vec40_t                      Output vector operand
            5 IN3_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            6 IN4_rI_OFFSET void *
                                                             base pointer
                                                 31   31     32 bit immediate post modification in
            7 IN5_PM_IMM        int32          -2 ..2 -1
                                                             bytes
            void* ptrBase;
            void* ptrModify;
            vec40_t vIn;
C example   vec40_t vIn2;
            ...
            vstw_v40_v40_indexed_rI_pm_imm_vuX_hp (pw_16w, 1, vIn, vIn2, ptrBase, ptrModify, 2);

Comments



Intrinsic   vstw_v40_v40_indexed_rI_pm_ptr_vuX_hp
name
Spec        vstw {pw, vuX, hp} vox[0], voy[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type

Determines the element size and number
                                PW_options
            1 PW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
Operands    2 VUX               uint8          0..3          Determines the source VCU
            3 IN1_V40           vec40_t                      Output vector operand
            4 IN2_V40           vec40_t                      Output vector operand
            5 IN3_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            6 IN4_rI_OFFSET void *
                                                              base pointer
            7 IN5_PM_PTR         void*                        Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            vec40_t vIn2;
            ...
            vstw_v40_v40_indexed_rI_pm_ptr_vuX_hp (pw_16w, 1, vIn, vIn2, ptrBase, ptrModify, ptr);

Comments



Intrinsic   vstw_v40_v40_indexed_rI_vuX_hp
name
Spec        vstw {pw, vuX, hp} vox[0], voy[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 PW_options
            1 PW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 VUX                uint8          0..3          Determines the source VCU

Operands    3 IN1_V40            vec40_t                      Output vector operand
            4 IN2_V40            vec40_t                      Output vector operand
            5 IN3_gB_BASE        void *                       Pointer register (gB)

            6 IN4_rI_OFFSET void *
                                                              Pointer (rI) specifying the offset from the
                                                              base pointer
            void* ptrBase;
            void* ptrModify;
            vec40_t vIn;
C example   vec40_t vIn2;
            ...
            vstw_v40_v40_indexed_rI_vuX_hp (pw_16w, 1, vIn, vIn2, ptrBase, ptrModify);

Comments

Intrinsic   vstw_v40_v40_indexed_rIp_pm_imm_vuX_hp
name
Spec        vstw {pw,vuX, hp} vox[0], voy[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                            Determines the element size and number
                                PW_options
            1 PW
                                enum                        of stored elements (see enum definition
                                                            at vec-mem-modes.h)
            2 VUX               uint8         0..3          Determines the source VCU
            3 IN1_V40           vec40_t                     Output vector operand
            4 IN2_V40           vec40_t                     Output vector operand
Operands
            5 IN3_gB_BASE       void *                      Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
            6 IN4_rI_OFFSET void *
                                                            base pointer
            7 IN4_PART          uint8         LOW,HIGH      Word part which is used for operand 6
                                                31   31     32 bit immediate post modification in
            8 IN5_PM_IMM        int32         -2 ..2 -1
                                                            bytes
            void* ptrBase;
            void* ptrModify;
            vec40_t vIn;
C example   vec40_t vIn2;
            ...
            vstw_v40_v40_indexed_rIp_pm_imm_vuX_hp (pw_16w, 1, vIn, vIn2, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic   vstw_v40_v40_indexed_rIp_pm_ptr_vuX_hp
name
Spec        vstw {pw,vuX, hp} vox[0], voy[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                            Determines the element size and number
                                PW_options
            1 PW
                                enum                        of stored elements (see enum definition
                                                            at vec-mem-modes.h)
            2 VUX               uint8         0..3          Determines the source VCU
Operands    3 IN1_V40           vec40_t                     Output vector operand
            4 IN2_V40           vec40_t                     Output vector operand
            5 IN3_gB_BASE       void *                      Pointer register (gB)

6 IN4_rI_OFFSET void *                          Pointer (rI) specifying the offset from the
                                                              base pointer
            7 IN4_PART           uint8         LOW,HIGH       Word part which is used for operand 6
            8 IN5_PM_PTR         void*                        Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            vec40_t vIn2;
            ...
            vstw_v40_v40_indexed_rIp_pm_ptr_vuX_hp (pw_16w, 1, vIn, vIn2, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic   vstw_v40_v40_indexed_rIp_vuX_hp
name
Spec        vstw {pw,vuX, hp} vox[0], voy[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 PW_options
            1 PW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 VUX                uint8         0..3           Determines the source VCU
            3 IN1_V40            vec40_t                      Output vector operand
Operands    4 IN2_V40            vec40_t                      Output vector operand
            5 IN3_gB_BASE        void *                       Pointer register (gB)

            6 IN4_rI_OFFSET void *
                                                              Pointer (rI) specifying the offset from the
                                                              base pointer
            7 IN4_PART           uint8         LOW,HIGH       Word part which is used for operand 6
            void* ptrBase;
            void* ptrModify;
            vec40_t vIn;
C example   vec40_t vIn2;
            ...
            vstw_v40_v40_indexed_rIp_vuX_hp (pw_16w, 1, vIn, vIn2, ptrBase, ptrModify, LOW);

Comments



Intrinsic   vstw_v40_v40_pm_imm_vuX_hp
name
Spec syntax   vstw {pw,vuX, hp} vox[0], voy[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                               Determines the element size and number
                                 PW_options
              1   PW
                                 enum                          of stored elements (see enum definition at
                                                               vec-mem-modes.h)

2   VUX            uint8          0..3           Determines the source VCU

Operands      3   IN1_V40        vec40_t                       Output vector operand
              4   IN2_V40        vec40_t                       Output vector operand
              5   IN3_PTR        void *                        Pointer register (rN)
                                                  31   31      32 bit immediate post modification in
              6   IN4_PM_IMM int32              -2 ..2 -1
                                                               bytes
              void* ptr;
              vec40_t vIn;
C example     vec40_t vIn2;
              ...
              vstw_v40_v40_pm_imm_vuX_hp (pw_16w, 1, vIn, vIn2, ptr, 2);

Comments



Intrinsic     vstw_v40_v40_pm_ptr_vuX_hp
name
Spec          vstw {pw,vuX, hp} vox[0], voy[0], (pN)[+pm_x] [,?prSC]
syntax
Return        void
type
                                                               Determines the element size and number
                                 PW_options
              1   PW
                                 enum                          of stored elements (see enum definition at
                                                               vec-mem-modes.h)
              2   VUX            uint8          0..3           Determines the source VCU
Operands      3   IN1_V40        vec40_t                       Output vector operand
              4   IN2_V40        vec40_t                       Output vector operand
              5   IN3_PTR        void *                        Pointer register (rN)
              6   IN4_PM_PTR void*                             Pointer register (rN)
              void* ptr;
              vec40_t vIn;
C example     vec40_t vIn2;
              ...
              vstw_v40_v40_pm_ptr_vuX_hp (pw_16w, 1, vIn, vIn2, ptr, ptr);
Comments



Intrinsic     vstw_v40_v40_vuX_hp
name
Spec syntax   vstw {pw,vuX, hp} vox[0], voy[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                                 Determines the element size and number
                                PW_options
              1   PW
                                enum                             of stored elements (see enum definition at
                                                                 vec-mem-modes.h)
              2   VUX           uint8          0..3              Determines the source VCU
Operands

3   IN1_V40       vec40_t                          Output vector operand
              4   IN2_V40       vec40_t                          Output vector operand
              5   IN3_PTR       void *                           Pointer register (rN)
              void* ptr;
              vec40_t vIn;
C example     vec40_t vIn2;
              ...
              vstw_v40_v40_vuX_hp (pw_16w, 1, vIn, vIn2, ptr);

Comments


Main table → Memory Access → Store → Store 16 bit
Available addressing modes
Intrinsic Names:
vstw_v40_v40_indexed_rI_pm_imm_vuX_lp
vstw_v40_v40_indexed_rI_pm_ptr_vuX_lp
vstw_v40_v40_indexed_rI_vuX_lp
vstw_v40_v40_indexed_rIp_pm_imm_vuX_lp
vstw_v40_v40_indexed_rIp_pm_ptr_vuX_lp
vstw_v40_v40_indexed_rIp_vuX_lp
vstw_v40_v40_pm_imm_vuX_lp
vstw_v40_v40_pm_ptr_vuX_lp
vstw_v40_v40_vuX_lp
Intrinsic   vstw_v40_v40_indexed_rI_pm_imm_vuX_lp
name
Spec        vstw {pw, vuX, lp} vox[0], voy[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 PW_options
            1 PW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 VUX                uint8         0..3           Determines the source VCU
            3 IN1_V40            vec40_t                      Output vector operand
Operands    4 IN2_V40            vec40_t                      Output vector operand
            5 IN3_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            6 IN4_rI_OFFSET void *
                                                              base pointer
                                                 31   31      32 bit immediate post modification in
            7 IN5_PM_IMM         int32         -2 ..2 -1
                                                              bytes
            void* ptrBase;
            void* ptrModify;
            vec40_t vIn;
C example   vec40_t vIn2;
            ...
            vstw_v40_v40_indexed_rI_pm_imm_vuX_lp (pw_16w, 1, vIn, vIn2, ptrBase, ptrModify, 2);

Comments



Intrinsic   vstw_v40_v40_indexed_rI_pm_ptr_vuX_lp
name
Spec        vstw {pw, vuX, lp} vox[0], voy[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type

Determines the element size and number
                                 PW_options
            1 PW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
Operands    2 VUX                uint8         0..3           Determines the source VCU
            3 IN1_V40            vec40_t                      Output vector operand
            4 IN2_V40            vec40_t                      Output vector operand
            5 IN3_gB_BASE        void *                        Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the
            6 IN4_rI_OFFSET void *
                                                               base pointer
            7 IN5_PM_PTR         void*                         Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            vec40_t vIn2;
            ...
            vstw_v40_v40_indexed_rI_pm_ptr_vuX_lp (pw_16w, 1, vIn, vIn2, ptrBase, ptrModify, ptr);

Comments



Intrinsic   vstw_v40_v40_indexed_rI_vuX_lp
name
Spec        vstw {pw, vuX, lp} vox[0], voy[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and number
                                 PW_options
            1 PW
                                 enum                          of stored elements (see enum definition
                                                               at vec-mem-modes.h)
            2 VUX                uint8          0..3           Determines the source VCU

Operands    3 IN1_V40            vec40_t                       Output vector operand
            4 IN2_V40            vec40_t                       Output vector operand
            5 IN3_gB_BASE        void *                        Pointer register (gB)

            6 IN4_rI_OFFSET void *
                                                               Pointer (rI) specifying the offset from the
                                                               base pointer
            void* ptrBase;
            void* ptrModify;
            vec40_t vIn;
C example   vec40_t vIn2;
            ...
            vstw_v40_v40_indexed_rI_vuX_lp (pw_16w, 1, vIn, vIn2, ptrBase, ptrModify);

Comments

Intrinsic   vstw_v40_v40_indexed_rIp_pm_imm_vuX_lp
name
Spec        vstw {pw,vuX, lp} vox[0], voy[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                PW_options
            1 PW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
            2 VUX               uint8         0..3           Determines the source VCU
            3 IN1_V40           vec40_t                      Output vector operand
            4 IN2_V40           vec40_t                      Output vector operand
Operands
            5 IN3_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            6 IN4_rI_OFFSET void *
                                                             base pointer
            7 IN4_PART          uint8         LOW,HIGH       Word part which is used for operand 6
                                                31   31      32 bit immediate post modification in
            8 IN5_PM_IMM        int32         -2 ..2 -1
                                                             bytes
            void* ptrBase;
            void* ptrModify;
            vec40_t vIn;
C example   vec40_t vIn2;
            ...
            vstw_v40_v40_indexed_rIp_pm_imm_vuX_lp (pw_16w, 1, vIn, vIn2, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic   vstw_v40_v40_indexed_rIp_pm_ptr_vuX_lp
name
Spec        vstw {pw,vuX, lp} vox[0], voy[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                PW_options
            1 PW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
            2 VUX               uint8         0..3           Determines the source VCU
Operands    3 IN1_V40           vec40_t                      Output vector operand
            4 IN2_V40           vec40_t                      Output vector operand
            5 IN3_gB_BASE       void *                       Pointer register (gB)

6 IN4_rI_OFFSET void *                           Pointer (rI) specifying the offset from the
                                                              base pointer
            7 IN4_PART           uint8         LOW,HIGH       Word part which is used for operand 6
            8 IN5_PM_PTR         void*                        Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            vec40_t vIn2;
            ...
            vstw_v40_v40_indexed_rIp_pm_ptr_vuX_lp (pw_16w, 1, vIn, vIn2, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic   vstw_v40_v40_indexed_rIp_vuX_lp
name
Spec        vstw {pw,vuX, lp} vox[0], voy[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 PW_options
            1 PW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 VUX                uint8         0..3           Determines the source VCU
            3 IN1_V40            vec40_t                      Output vector operand
Operands    4 IN2_V40            vec40_t                      Output vector operand
            5 IN3_gB_BASE        void *                       Pointer register (gB)

            6 IN4_rI_OFFSET void *
                                                              Pointer (rI) specifying the offset from the
                                                              base pointer
            7 IN4_PART           uint8         LOW,HIGH       Word part which is used for operand 6
            void* ptrBase;
            void* ptrModify;
            vec40_t vIn;
C example   vec40_t vIn2;
            ...
            vstw_v40_v40_indexed_rIp_vuX_lp (pw_16w, 1, vIn, vIn2, ptrBase, ptrModify, LOW);

Comments



Intrinsic   vstw_v40_v40_pm_imm_vuX_lp
name
Spec syntax   vstw {pw,vuX, lp} vox[0], voy[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                                Determines the element size and number
                                  PW_options
              1   PW
                                  enum                          of stored elements (see enum definition at
                                                                vec-mem-modes.h)

2   VUX             uint8          0..3           Determines the source VCU

Operands      3   IN1_V40         vec40_t                       Output vector operand
              4   IN2_V40         vec40_t                       Output vector operand
              5   IN3_PTR         void *                        Pointer register (rN)
                                                   31   31      32 bit immediate post modification in
              6   IN4_PM_IMM int32               -2 ..2 -1
                                                                bytes
              void* ptr;
              vec40_t vIn;
C example     vec40_t vIn2;
              ...
              vstw_v40_v40_pm_imm_vuX_lp (pw_16w, 1, vIn, vIn2, ptr, 2);

Comments



Intrinsic     vstw_v40_v40_pm_ptr_vuX_lp
name
Spec          vstw {pw,vuX, lp} vox[0], voy[0], (pN)[+pm_x] [,?prSC]
syntax
Return        void
type
                                                                Determines the element size and number
                                 PW_options
              1   PW
                                 enum                           of stored elements (see enum definition at
                                                                vec-mem-modes.h)
              2   VUX            uint8          0..3            Determines the source VCU
Operands      3   IN1_V40        vec40_t                        Output vector operand
              4   IN2_V40        vec40_t                        Output vector operand
              5   IN3_PTR        void *                         Pointer register (rN)
              6   IN4_PM_PTR void*                              Pointer register (rN)
              void* ptr;
              vec40_t vIn;
C example     vec40_t vIn2;
              ...
              vstw_v40_v40_pm_ptr_vuX_lp (pw_16w, 1, vIn, vIn2, ptr, ptr);
Comments



Intrinsic     vstw_v40_v40_vuX_lp
name
Spec syntax   vstw {pw,vuX, lp} vox[0], voy[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                                 Determines the element size and number
                                 PW_options
              1   PW
                                 enum                            of stored elements (see enum definition at
                                                                 vec-mem-modes.h)
              2   VUX            uint8         0..3              Determines the source VCU
Operands

3   IN1_V40        vec40_t                         Output vector operand
              4   IN2_V40        vec40_t                         Output vector operand
              5   IN3_PTR        void *                          Pointer register (rN)
              void* ptr;
              vec40_t vIn;
C example     vec40_t vIn2;
              ...
              vstw_v40_v40_vuX_lp (pw_16w, 1, vIn, vIn2, ptr);

Comments


Main table → Memory Access → Store → Store 16 bit
Available addressing modes
Intrinsic Names:
vstw_v32_indexed_rI_pm_imm_vuX
vstw_v32_indexed_rI_pm_ptr_vuX
vstw_v32_indexed_rI_vuX
vstw_v32_indexed_rIp_pm_imm_vuX
vstw_v32_indexed_rIp_pm_ptr_vuX
vstw_v32_indexed_rIp_vuX
vstw_v32_pm_imm_vuX
vstw_v32_pm_ptr_vuX
vstw_v32_vuX
Intrinsic   vstw_v32_indexed_rI_pm_imm_vuX
name
Spec        vstw {mw, vuX [,lp|hp]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                MW_options
            1 MW
                                enum                          of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 VUX               uint8          0..3           Determines the source VCU
            3 IN1_V32           vec_t                         Input vector operand
                                                              Offset for the first DW used from
Operands    4 IN1_OFST          uint8          0,4
                                                              operand 3
            5 IN2_gB_BASE       void *                        Pointer register (gB)

            6 IN3_rI_OFFSET void *
                                                              Pointer (rI) specifying the offset from the
                                                              base pointer
                                                 31   31      32 bit immediate post modification in
            7 IN4_PM_IMM        int32          -2 ..2 -1
                                                              bytes
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rI_pm_imm_vuX (mw_8w, 1, vIn, 0, ptrBase, ptrModify, 2);

Comments



Intrinsic   vstw_v32_indexed_rI_pm_ptr_vuX
name
Spec        vstw {mw, vuX [,lp|hp]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type

Determines the element size and number
                                MW_options
            1 MW
                                enum                          of stored elements (see enum definition
                                                              at vec-mem-modes.h)
Operands    2 VUX               uint8          0..3           Determines the source VCU
            3 IN1_V32           vec_t                         Input vector operand
            4 IN1_OFST          uint8          0,4            Offset for the first DW used from
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
            vstw_v32_indexed_rI_pm_ptr_vuX (mw_8w, 1, vIn, 0, ptrBase, ptrModify, ptr);

Comments



Intrinsic   vstw_v32_indexed_rI_vuX
name
Spec        vstw {mw, vuX [,lp|hp]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and number
                                 MW_options
            1 MW
                                 enum                          of stored elements (see enum definition
                                                               at vec-mem-modes.h)
            2 VUX                uint8          0..3           Determines the source VCU
            3 IN1_V32            vec_t                         Input vector operand
Operands
            4 IN1_OFST
                                                               Offset for the first DW used from
                                 uint8          0,4
                                                               operand 3
            5 IN2_gB_BASE        void *                        Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the
            6 IN3_rI_OFFSET void *
                                                               base pointer
            void* ptrBase;

void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rI_vuX (mw_8w, 1, vIn, 0, ptrBase, ptrModify);

Comments



Intrinsic   vstw_v32_indexed_rIp_pm_imm_vuX
name
Spec        vstw {mw,vuX [,lp|hp]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                MW_options
            1 MW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
            2 VUX               uint8         0..3           Determines the source VCU
            3 IN1_V32           vec_t                        Input vector operand
                                                             Offset for the first DW used from
            4 IN1_OFST          uint8         0,4
Operands                                                     operand 3
            5 IN2_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            6 IN3_rI_OFFSET void *
                                                             base pointer
            7 IN3_PART          uint8         LOW,HIGH       Word part which is used for operand 6
                                                31   31      32 bit immediate post modification in
            8 IN4_PM_IMM        int32         -2 ..2 -1
                                                             bytes
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rIp_pm_imm_vuX (mw_8w, 1, vIn, 0, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic   vstw_v32_indexed_rIp_pm_ptr_vuX
name
Spec        vstw {mw,vuX [,lp|hp]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                MW_options
            1 MW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)

Operands    2 VUX               uint8         0..3           Determines the source VCU
            3 IN1_V32           vec_t                        Input vector operand

4 IN1_OFST
                                                             Offset for the first DW used from
                                uint8         0,4
                                                             operand 3
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
            vstw_v32_indexed_rIp_pm_ptr_vuX (mw_8w, 1, vIn, 0, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic   vstw_v32_indexed_rIp_vuX
name
Spec        vstw {mw,vuX [,lp|hp]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 MW_options
            1 MW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 VUX                uint8         0..3           Determines the source VCU
            3 IN1_V32            vec_t                        Input vector operand
Operands    4 IN1_OFST
                                                              Offset for the first DW used from
                                 uint8         0,4
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
            vstw_v32_indexed_rIp_vuX (mw_8w, 1, vIn, 0, ptrBase, ptrModify, LOW);

Comments



Intrinsic   vstw_v32_pm_imm_vuX
name

Spec syntax   vstw {mw, vuX [,lp|hp]} vix[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                                Determines the element size and number
                                 MW_options
              1   MW
                                 enum                           of stored elements (see enum definition at
                                                                vec-mem-modes.h)
              2   VUX            uint8         0..3             Determines the source VCU
              3   IN1_V32        vec_t                          Input vector operand
Operands
              4   IN1_OFST       uint8         0,4              Offset for the first DW used from operand
                                                                3

              5   IN2_PTR        void *                         Pointer register (rN)
                                                 31   31        32 bit immediate post modification in
              6   IN3_PM_IMM int32             -2 ..2 -1
                                                                bytes
              void* ptr;
              vec_t vIn;
C example     ...
              vstw_v32_pm_imm_vuX (mw_8w, 1, vIn, 0, ptr, 2);

Comments



Intrinsic     vstw_v32_pm_ptr_vuX
name
Spec          vstw {mw, vuX [,lp|hp]} vix[0], (pN)[+pm_x] [,?prSC]
syntax
Return        void
type
                                                                Determines the element size and number
                                MW_options
              1   MW
                                enum                            of stored elements (see enum definition at
                                                                vec-mem-modes.h)
              2   VUX           uint8          0..3             Determines the source VCU

Operands      3   IN1_V32       vec_t                           Input vector operand

              4
                                                                Offset for the first DW used from
                  IN1_OFST      uint8          0,4
                                                                operand 3
              5   IN2_PTR       void *                          Pointer register (rN)
              6   IN3_PM_PTR void*                              Pointer register (rN)
              void* ptr;
C example     vec_t vIn;
              ...
              vstw_v32_pm_ptr_vuX (mw_8w, 1, vIn, 0, ptr, ptr);

Comments

Intrinsic     vstw_v32_vuX
name
Spec syntax   vstw {mw, vuX [,lp|hp]} vix[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                                  Determines the element size and number
                                 MW_options
              1   MW
                                 enum                             of stored elements (see enum definition at
                                                                  vec-mem-modes.h)
              2   VUX            uint8          0..3              Determines the source VCU
Operands
              3   IN1_V32        vec_t                            Input vector operand

              4   IN1_OFST       uint8          0,4
                                                                  Offset for the first DW used from operand
                                                                  3

              5   IN2_PTR        void *                           Pointer register (rN)
              void* ptr;
              vec_t vIn;
C example     ...
              vstw_v32_vuX (mw_8w, 1, vIn, 0, ptr);

Comments


Main table → Memory Access → Store → Store 16 bit
Available addressing modes
Intrinsic Names:
vstw_v32_indexed_rI_pm_imm_vuX_hp
vstw_v32_indexed_rI_pm_ptr_vuX_hp
vstw_v32_indexed_rI_vuX_hp
vstw_v32_indexed_rIp_pm_imm_vuX_hp
vstw_v32_indexed_rIp_pm_ptr_vuX_hp
vstw_v32_indexed_rIp_vuX_hp
vstw_v32_pm_imm_vuX_hp
vstw_v32_pm_ptr_vuX_hp
vstw_v32_vuX_hp
Intrinsic   vstw_v32_indexed_rI_pm_imm_vuX_hp
name
Spec        vstw {mw, vuX [,lp|hp]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                MW_options
            1 MW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
            2 VUX               uint8         0..3           Determines the source VCU
            3 IN1_V32           vec_t                        Input vector operand
Operands
            4 IN2_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                             base pointer

6 IN4_PM_IMM                        31   31      32 bit immediate post modification in
                                int32         -2 ..2 -1
                                                             bytes
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rI_pm_imm_vuX_hp (mw_8w, 1, vIn, ptrBase, ptrModify, 2);

Comments



Intrinsic   vstw_v32_indexed_rI_pm_ptr_vuX_hp
name
Spec        vstw {mw, vuX [,lp|hp]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                MW_options
            1 MW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
            2 VUX               uint8         0..3           Determines the source VCU
Operands    3 IN1_V32           vec_t                        Input vector operand
            4 IN2_gB_BASE       void *                       Pointer register (gB)

            5 IN3_rI_OFFSET void *
                                                             Pointer (rI) specifying the offset from the
                                                             base pointer
            6 IN4_PM_PTR         void*                        Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rI_pm_ptr_vuX_hp (mw_8w, 1, vIn, ptrBase, ptrModify, ptr);

Comments



Intrinsic   vstw_v32_indexed_rI_vuX_hp
name
Spec        vstw {mw, vuX [,lp|hp]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 MW_options
            1 MW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 VUX                uint8         0..3           Determines the source VCU
Operands    3 IN1_V32            vec_t                        Input vector operand
            4 IN2_gB_BASE        void *                       Pointer register (gB)

Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                              base pointer
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rI_vuX_hp (mw_8w, 1, vIn, ptrBase, ptrModify);

Comments



Intrinsic   vstw_v32_indexed_rIp_pm_imm_vuX_hp
name
Spec        vstw {mw,vuX [,lp|hp]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 MW_options
Operands    1 MW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 VUX               uint8          0..3          Determines the source VCU
            3 IN1_V32           vec_t                        Input vector operand
            4 IN2_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                             base pointer
            6 IN3_PART          uint8          LOW,HIGH      Word part which is used for operand 5
                                                 31   31     32 bit immediate post modification in
            7 IN4_PM_IMM        int32          -2 ..2 -1
                                                             bytes
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rIp_pm_imm_vuX_hp (mw_8w, 1, vIn, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic   vstw_v32_indexed_rIp_pm_ptr_vuX_hp
name
Spec        vstw {mw,vuX [,lp|hp]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                MW_options
            1 MW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
            2 VUX               uint8          0..3          Determines the source VCU
            3 IN1_V32           vec_t                        Input vector operand

Operands    4 IN2_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                             base pointer
            6 IN3_PART          uint8          LOW,HIGH      Word part which is used for operand 5
            7 IN4_PM_PTR        void*                        Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rIp_pm_ptr_vuX_hp (mw_8w, 1, vIn, ptrBase, ptrModify, LOW, ptr);

Comments
Intrinsic     vstw_v32_indexed_rIp_vuX_hp
name
Spec          vstw {mw,vuX [,lp|hp]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return        void
type
                                                               Determines the element size and number
                                  MW_options
              1 MW
                                  enum                         of stored elements (see enum definition
                                                               at vec-mem-modes.h)
              2 VUX               uint8          0..3          Determines the source VCU

Operands      3 IN1_V32           vec_t                        Input vector operand
              4 IN2_gB_BASE       void *                       Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the
              5 IN3_rI_OFFSET void *
                                                               base pointer
              6 IN3_PART          uint8          LOW,HIGH      Word part which is used for operand 5
              void* ptrBase;
              void* ptrModify;
C example     vec_t vIn;
              ...
              vstw_v32_indexed_rIp_vuX_hp (mw_8w, 1, vIn, ptrBase, ptrModify, LOW);

Comments



Intrinsic     vstw_v32_pm_imm_vuX_hp
name
Spec syntax   vstw {mw, vuX [,lp|hp]} vix[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                              Determines the element size and number
                                 MW_options
              1      MW
                                 enum                         of stored elements (see enum definition at
                                                              vec-mem-modes.h)

2      VUX         uint8          0..3          Determines the source VCU
Operands      3      IN1_V32     vec_t                        Input vector operand
              4      IN2_PTR     void *                       Pointer register (rN)

              5                                   31    31    32 bit immediate post modification in
                     IN3_PM_IMM int32           -2 ..2 -1
                                                              bytes
              void* ptr;
              vec_t vIn;
C example     ...
              vstw_v32_pm_imm_vuX_hp (mw_8w, 1, vIn, ptr, 2);

Comments



Intrinsic     vstw_v32_pm_ptr_vuX_hp
name
Spec          vstw {mw, vuX [,lp|hp]} vix[0], (pN)[+pm_x] [,?prSC]
syntax
Return        void
type
                                                                  Determines the element size and number
                                 MW_options
              1   MW
                                 enum                             of stored elements (see enum definition at
                                                                  vec-mem-modes.h)
              2   VUX            uint8          0..3              Determines the source VCU
Operands
              3   IN1_V32        vec_t                            Input vector operand
              4   IN2_PTR        void *                           Pointer register (rN)
              5   IN3_PM_PTR void*                                Pointer register (rN)
              void* ptr;
              vec_t vIn;
C example     ...
              vstw_v32_pm_ptr_vuX_hp (mw_8w, 1, vIn, ptr, ptr);

Comments



Intrinsic     vstw_v32_vuX_hp
name
Spec syntax   vstw {mw, vuX [,lp|hp]} vix[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                              Determines the element size and number
                                MW_options
              1   MW
                                enum                          of stored elements (see enum definition at
                                                              vec-mem-modes.h)
Operands      2   VUX           uint8          0..3           Determines the source VCU
              3   IN1_V32       vec_t                         Input vector operand
              4   IN2_PTR       void *                        Pointer register (rN)
              void* ptr;
              vec_t vIn;
C example     ...
              vstw_v32_vuX_hp (mw_8w, 1, vIn, ptr);

Comments

Main table → Memory Access → Store → Store 16 bit
Available addressing modes
Intrinsic Names:
vstw_v32_indexed_rI_pm_imm_vuX_lp
vstw_v32_indexed_rI_pm_ptr_vuX_lp
vstw_v32_indexed_rI_vuX_lp
vstw_v32_indexed_rIp_pm_imm_vuX_lp
vstw_v32_indexed_rIp_pm_ptr_vuX_lp
vstw_v32_indexed_rIp_vuX_lp
vstw_v32_pm_imm_vuX_lp
vstw_v32_pm_ptr_vuX_lp
vstw_v32_vuX_lp
Intrinsic   vstw_v32_indexed_rI_pm_imm_vuX_lp
name
Spec        vstw {mw, vuX [,lp|hp]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                MW_options
            1 MW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
            2 VUX               uint8          0..3          Determines the source VCU
            3 IN1_V32           vec_t                        Input vector operand
Operands
            4 IN2_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                             base pointer

            6 IN4_PM_IMM                         31   31     32 bit immediate post modification in
                                int32          -2 ..2 -1
                                                             bytes
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rI_pm_imm_vuX_lp (mw_8w, 1, vIn, ptrBase, ptrModify, 2);

Comments



Intrinsic   vstw_v32_indexed_rI_pm_ptr_vuX_lp
name
Spec        vstw {mw, vuX [,lp|hp]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                MW_options
            1 MW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
            2 VUX               uint8          0..3          Determines the source VCU
Operands    3 IN1_V32           vec_t                        Input vector operand
            4 IN2_gB_BASE       void *                       Pointer register (gB)

5 IN3_rI_OFFSET void *
                                                             Pointer (rI) specifying the offset from the
                                                             base pointer
            6 IN4_PM_PTR         void*                        Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rI_pm_ptr_vuX_lp (mw_8w, 1, vIn, ptrBase, ptrModify, ptr);

Comments



Intrinsic   vstw_v32_indexed_rI_vuX_lp
name
Spec        vstw {mw, vuX [,lp|hp]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 MW_options
            1 MW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 VUX                uint8          0..3          Determines the source VCU
Operands    3 IN1_V32            vec_t                        Input vector operand
            4 IN2_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                              base pointer
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rI_vuX_lp (mw_8w, 1, vIn, ptrBase, ptrModify);

Comments



Intrinsic   vstw_v32_indexed_rIp_pm_imm_vuX_lp
name
Spec        vstw {mw,vuX [,lp|hp]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 MW_options
Operands    1 MW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 VUX               uint8          0..3           Determines the source VCU
            3 IN1_V32           vec_t                         Input vector operand
            4 IN2_gB_BASE       void *                        Pointer register (gB)

Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                              base pointer
            6 IN3_PART          uint8          LOW,HIGH       Word part which is used for operand 5
                                                 31   31      32 bit immediate post modification in
            7 IN4_PM_IMM        int32          -2 ..2 -1
                                                              bytes
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rIp_pm_imm_vuX_lp (mw_8w, 1, vIn, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic   vstw_v32_indexed_rIp_pm_ptr_vuX_lp
name
Spec        vstw {mw,vuX [,lp|hp]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                MW_options
            1 MW
                                enum                          of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 VUX               uint8          0..3           Determines the source VCU
            3 IN1_V32           vec_t                         Input vector operand
Operands    4 IN2_gB_BASE       void *                        Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                              base pointer
            6 IN3_PART          uint8          LOW,HIGH       Word part which is used for operand 5
            7 IN4_PM_PTR        void*                         Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rIp_pm_ptr_vuX_lp (mw_8w, 1, vIn, ptrBase, ptrModify, LOW, ptr);

Comments
Intrinsic     vstw_v32_indexed_rIp_vuX_lp
name
Spec          vstw {mw,vuX [,lp|hp]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return        void
type
                                                               Determines the element size and number
                                  MW_options
              1 MW
                                  enum                         of stored elements (see enum definition

at vec-mem-modes.h)
              2 VUX               uint8          0..3          Determines the source VCU

Operands      3 IN1_V32           vec_t                        Input vector operand
              4 IN2_gB_BASE       void *                       Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the
              5 IN3_rI_OFFSET void *
                                                               base pointer
              6 IN3_PART          uint8          LOW,HIGH      Word part which is used for operand 5
              void* ptrBase;
              void* ptrModify;
C example     vec_t vIn;
              ...
              vstw_v32_indexed_rIp_vuX_lp (mw_8w, 1, vIn, ptrBase, ptrModify, LOW);

Comments



Intrinsic     vstw_v32_pm_imm_vuX_lp
name
Spec syntax   vstw {mw, vuX [,lp|hp]} vix[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                              Determines the element size and number
                                 MW_options
              1      MW
                                 enum                         of stored elements (see enum definition at
                                                              vec-mem-modes.h)
              2      VUX         uint8          0..3          Determines the source VCU
Operands      3      IN1_V32     vec_t                        Input vector operand
              4      IN2_PTR     void *                       Pointer register (rN)

              5                                   31    31    32 bit immediate post modification in
                     IN3_PM_IMM int32           -2 ..2 -1
                                                              bytes
              void* ptr;
              vec_t vIn;
C example     ...
              vstw_v32_pm_imm_vuX_lp (mw_8w, 1, vIn, ptr, 2);

Comments



Intrinsic     vstw_v32_pm_ptr_vuX_lp
name
Spec          vstw {mw, vuX [,lp|hp]} vix[0], (pN)[+pm_x] [,?prSC]
syntax
Return        void
type
                                                                  Determines the element size and number
                                 MW_options
              1   MW
                                 enum                             of stored elements (see enum definition at
                                                                  vec-mem-modes.h)

2   VUX            uint8          0..3              Determines the source VCU
Operands
              3   IN1_V32        vec_t                            Input vector operand
              4   IN2_PTR        void *                           Pointer register (rN)
              5   IN3_PM_PTR void*                                Pointer register (rN)
              void* ptr;
              vec_t vIn;
C example     ...
              vstw_v32_pm_ptr_vuX_lp (mw_8w, 1, vIn, ptr, ptr);

Comments



Intrinsic     vstw_v32_vuX_lp
name
Spec syntax   vstw {mw, vuX [,lp|hp]} vix[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                                  Determines the element size and number
                                MW_options
              1   MW
                                enum                              of stored elements (see enum definition at
                                                                  vec-mem-modes.h)
Operands      2   VUX           uint8          0..3               Determines the source VCU
              3   IN1_V32       vec_t                             Input vector operand
              4   IN2_PTR       void *                            Pointer register (rN)
            void* ptr;
            vec_t vIn;
C example   ...
            vstw_v32_vuX_lp (mw_8w, 1, vIn, ptr);

Comments


Main table → Memory Access → Store → Store 16 bit
Available addressing modes
Intrinsic Names:
vstw_v40
vstw_v40_direct
vstw_v40_indexed_imm
vstw_v40_indexed_rI
vstw_v40_indexed_rI_pm_imm
vstw_v40_indexed_rI_pm_ptr
vstw_v40_indexed_rIp
vstw_v40_indexed_rIp_pm_imm
vstw_v40_indexed_rIp_pm_ptr
vstw_v40_pm_imm
vstw_v40_pm_ptr
Intrinsic     vstw_v40
name
Spec syntax   vstw {mw [,lp|hp][,concat]} vox[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                            Determines the element size and number
                                 MW_options
              1   MW
                                 enum                       of stored elements (see enum definition at
                                                            vec-mem-modes.h)
Operands      2   IN1_V40        vec40_t                    Output vector operand

              3   IN1_OFST       uint8          0,4
                                                            Offset for the first DW used from operand
                                                            2

4   IN2_PTR        void *                     Pointer register (rN)
              void* ptr;
              vec40_t vIn;
C example     ...
              vstw_v40 (mw_8w, vIn, 0, ptr);

Comments



Intrinsic     vstw_v40_direct
name
Spec syntax   vstw {mw [,lp|hp][,concat]} vox[0], [#address] [,?prSC]

Return        void
type
                                                            Determines the element size and number
                                 MW_options
              1   MW
                                 enum                       of stored elements (see enum definition at
                                                            vec-mem-modes.h)
Operands      2   IN1_V40        vec40_t                    Output vector operand

              3   IN1_OFST       uint8          0,4
                                                            Offset for the first DW used from operand
                                                            2
                                                      32
              4   IN2_ADDR       int32          0..2 -1     32 bit address
              vec40_t vIn;
C example     ...
              vstw_v40_direct (mw_8w, vIn, 0, 2);

Comments



Intrinsic     vstw_v40_indexed_imm
name
Spec        vstw {mw [,lp|hp][,concat]} vox[0], (gB+#imm16_6) [,?prSC]
syntax
Return      void
type
                                                                Determines the element size and number
                                 MW_options
            1 MW
                                 enum                           of stored elements (see enum definition
                                                                at vec-mem-modes.h)
            2 IN1_V40            vec40_t                        Output vector operand
Operands                                                        Offset for the first DW used from
            3 IN1_OFST           uint8          0,4
                                                                operand 2
            4 IN2_gB_BASE void *                                Pointer register (gB)
                                                -               16 bit immediate post modification in
            5 IN3_IMM16_6        int16
                                                32768..32767    bytes
            void* ptrBase;
            vec40_t vIn;
C example   ...
            vstw_v40_indexed_imm (mw_8w, vIn, 0, ptrBase, 2);

Comments



Intrinsic   vstw_v40_indexed_rI
name

Spec        vstw {mw [,lp|hp][,concat]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                                Determines the element size and number
                                 MW_options
            1 MW
                                 enum                           of stored elements (see enum definition
                                                                at vec-mem-modes.h)
            2 IN1_V40            vec40_t                        Output vector operand
Operands                                                        Offset for the first DW used from
            3 IN1_OFST           uint8          0,4
                                                                operand 2
            4 IN2_gB_BASE        void *                         Pointer register (gB)
                                                                Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                                base pointer
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rI (mw_8w, vIn, 0, ptrBase, ptrModify);
Comments



Intrinsic   vstw_v40_indexed_rI_pm_imm
name
Spec        vstw {mw [,lp|hp][,concat]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                MW_options
            1 MW
                                enum                          of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_V40           vec40_t                       Output vector operand
                                                              Offset for the first DW used from
            3 IN1_OFST          uint8          0,4
Operands                                                      operand 2
            4 IN2_gB_BASE       void *                        Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                              base pointer

            6 IN4_PM_IMM                         31   31      32 bit immediate post modification in
                                int32          -2 ..2 -1

bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rI_pm_imm (mw_8w, vIn, 0, ptrBase, ptrModify, 2);

Comments



Intrinsic   vstw_v40_indexed_rI_pm_ptr
name
Spec        vstw {mw [,lp|hp][,concat]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                MW_options
            1 MW
                                enum                          of stored elements (see enum definition
                                                              at vec-mem-modes.h)
Operands
            2 IN1_V40           vec40_t                       Output vector operand
            3 IN1_OFST          uint8          0,4            Offset for the first DW used from
                                                               operand 2
            4 IN2_gB_BASE        void *                        Pointer register (gB)

            5 IN3_rI_OFFSET void *
                                                               Pointer (rI) specifying the offset from the
                                                               base pointer
            6 IN4_PM_PTR         void*                         Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rI_pm_ptr (mw_8w, vIn, 0, ptrBase, ptrModify, ptr);

Comments



Intrinsic   vstw_v40_indexed_rIp
name
Spec        vstw {mw [,lp|hp][,concat]} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and number
                                 MW_options
            1 MW
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
            6 IN3_PART           uint8          LOW,HIGH       Word part which is used for operand 5
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rIp (mw_8w, vIn, 0, ptrBase, ptrModify, LOW);

Comments



Intrinsic   vstw_v40_indexed_rIp_pm_imm
name
Spec        vstw {mw [,lp|hp][,concat]} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                MW_options
            1 MW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
            2 IN1_V40           vec40_t                      Output vector operand
                                                             Offset for the first DW used from
            3 IN1_OFST          uint8          0,4
                                                             operand 2
Operands    4 IN2_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                             base pointer
            6 IN3_PART          uint8          LOW,HIGH      Word part which is used for operand 5
                                                31   31      32 bit immediate post modification in
            7 IN4_PM_IMM        int32          -2 ..2 -1
                                                             bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rIp_pm_imm (mw_8w, vIn, 0, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic   vstw_v40_indexed_rIp_pm_ptr
name
Spec        vstw {mw [,lp|hp][,concat]} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                MW_options
            1 MW
                                enum                         of stored elements (see enum definition

at vec-mem-modes.h)
            2 IN1_V40           vec40_t                      Output vector operand
Operands
            3 IN1_OFST
                                                             Offset for the first DW used from
                                uint8          0,4
                                                             operand 2
            4 IN2_gB_BASE       void *                       Pointer register (gB)
            5 IN3_rI_OFFSET void *                           Pointer (rI) specifying the offset from the
                                                              base pointer
            6 IN3_PART           uint8          LOW,HIGH      Word part which is used for operand 5
            7 IN4_PM_PTR         void*                        Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rIp_pm_ptr (mw_8w, vIn, 0, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic   vstw_v40_pm_imm
name
Spec        vstw {mw [,lp|hp][,concat]} vox[0], (pN)+#imm32_6 [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                               MW_options
            1   MW
                               enum                           of stored elements (see enum definition at
                                                              vec-mem-modes.h)
            2   IN1_V40        vec40_t                        Output vector operand
Operands                                                      Offset for the first DW used from
            3   IN1_OFST       uint8          0,4
                                                              operand 2
            4   IN2_PTR        void *                         Pointer register (rN)

            5                                   31     31     32 bit immediate post modification in
                IN3_IMM32_6 int32             -2 ..2 -1
                                                              bytes
            void* ptr;
            vec40_t vIn;
C example   ...
            vstw_v40_pm_imm (mw_8w, vIn, 0, ptr, 2);

Comments



Intrinsic   vstw_v40_pm_ptr
name
Spec        vstw {mw [,lp|hp][,concat]} vox[0], (pN)[+pm_x] [,?prSC]
syntax
Return      void
type
                                                           Determines the element size and number

MW_options
              1   MW
                                 enum                      of stored elements (see enum definition at
                                                           vec-mem-modes.h)
              2   IN1_V40        vec40_t                   Output vector operand
Operands
              3
                                                           Offset for the first DW used from
                  IN1_OFST       uint8           0,4
                                                           operand 2
              4   IN2_PTR        void *                    Pointer register (rN)
              5   IN3_PM_PTR void*                         Pointer register (rN)
              void* ptr;
              vec40_t vIn;
C example     ...
              vstw_v40_pm_ptr (mw_8w, vIn, 0, ptr, ptr);

Comments


Main table → Memory Access → Store → Store 16 bit
Available addressing modes
Intrinsic Names:
vstw_v40_concat
vstw_v40_direct_concat
vstw_v40_indexed_imm_concat
vstw_v40_indexed_rI_concat
vstw_v40_indexed_rI_pm_imm_concat
vstw_v40_indexed_rI_pm_ptr_concat
vstw_v40_indexed_rIp_concat
vstw_v40_indexed_rIp_pm_imm_concat
vstw_v40_indexed_rIp_pm_ptr_concat
vstw_v40_pm_imm_concat
vstw_v40_pm_ptr_concat
Intrinsic     vstw_v40_concat
name
Spec syntax   vstw {mw [,lp|hp][,concat]} vox[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                            Determines the element size and number
                                 MW_options
              1   MW
                                 enum                       of stored elements (see enum definition at
                                                            vec-mem-modes.h)
Operands      2   IN1_V40        vec40_t                    Output vector operand

              3   IN1_OFST       uint8          0,4
                                                            Offset for the first DW used from operand
                                                            2

              4   IN2_PTR        void *                     Pointer register (rN)
              void* ptr;
              vec40_t vIn;
C example     ...
              vstw_v40_concat (mw_8w, vIn, 0, ptr);

Comments



Intrinsic     vstw_v40_direct_concat
name
Spec syntax   vstw {mw [,lp|hp][,concat]} vox[0], [#address] [,?prSC]

Return        void
type
                                                            Determines the element size and number

MW_options
              1   MW
                                 enum                       of stored elements (see enum definition at
                                                            vec-mem-modes.h)
Operands      2   IN1_V40        vec40_t                    Output vector operand

              3   IN1_OFST       uint8          0,4
                                                            Offset for the first DW used from operand
                                                            2
                                                      32
              4   IN2_ADDR       int32          0..2 -1     32 bit address
              vec40_t vIn;
C example     ...
              vstw_v40_direct_concat (mw_8w, vIn, 0, 2);

Comments



Intrinsic     vstw_v40_indexed_imm_concat
name
Spec        vstw {mw [,lp|hp][,concat]} vox[0], (gB+#imm16_6) [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and number
                                MW_options
            1 MW
                                enum                           of stored elements (see enum definition
                                                               at vec-mem-modes.h)
            2 IN1_V40           vec40_t                        Output vector operand
Operands                                                       Offset for the first DW used from
            3 IN1_OFST          uint8           0,4
                                                               operand 2
            4 IN2_gB_BASE void *                               Pointer register (gB)
                                                -              16 bit immediate post modification in
            5 IN3_IMM16_6       int16
                                                32768..32767   bytes
            void* ptrBase;
            vec40_t vIn;
C example   ...
            vstw_v40_indexed_imm_concat (mw_8w, vIn, 0, ptrBase, 2);

Comments



Intrinsic   vstw_v40_indexed_rI_concat
name
Spec        vstw {mw [,lp|hp][,concat]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and number
                                 MW_options
            1 MW
                                 enum                          of stored elements (see enum definition
                                                               at vec-mem-modes.h)

2 IN1_V40            vec40_t                       Output vector operand
Operands                                                       Offset for the first DW used from
            3 IN1_OFST           uint8          0,4
                                                               operand 2
            4 IN2_gB_BASE        void *                        Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                               base pointer
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rI_concat (mw_8w, vIn, 0, ptrBase, ptrModify);
Comments



Intrinsic   vstw_v40_indexed_rI_pm_imm_concat
name
Spec        vstw {mw [,lp|hp][,concat]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                MW_options
            1 MW
                                enum                          of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_V40           vec40_t                       Output vector operand
                                                              Offset for the first DW used from
            3 IN1_OFST          uint8          0,4
Operands                                                      operand 2
            4 IN2_gB_BASE       void *                        Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                              base pointer

            6 IN4_PM_IMM                         31   31      32 bit immediate post modification in
                                int32          -2 ..2 -1
                                                              bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rI_pm_imm_concat (mw_8w, vIn, 0, ptrBase, ptrModify, 2);

Comments



Intrinsic   vstw_v40_indexed_rI_pm_ptr_concat
name
Spec        vstw {mw [,lp|hp][,concat]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type

Determines the element size and number
                                MW_options
            1 MW
                                enum                          of stored elements (see enum definition
                                                              at vec-mem-modes.h)
Operands
            2 IN1_V40           vec40_t                       Output vector operand
            3 IN1_OFST          uint8          0,4            Offset for the first DW used from
                                                               operand 2
            4 IN2_gB_BASE        void *                        Pointer register (gB)

            5 IN3_rI_OFFSET void *
                                                               Pointer (rI) specifying the offset from the
                                                               base pointer
            6 IN4_PM_PTR         void*                         Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rI_pm_ptr_concat (mw_8w, vIn, 0, ptrBase, ptrModify, ptr);

Comments



Intrinsic   vstw_v40_indexed_rIp_concat
name
Spec        vstw {mw [,lp|hp][,concat]} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and number
                                 MW_options
            1 MW
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
            6 IN3_PART           uint8          LOW,HIGH       Word part which is used for operand 5
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...

vstw_v40_indexed_rIp_concat (mw_8w, vIn, 0, ptrBase, ptrModify, LOW);

Comments



Intrinsic   vstw_v40_indexed_rIp_pm_imm_concat
name
Spec        vstw {mw [,lp|hp][,concat]} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                MW_options
            1 MW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
            2 IN1_V40           vec40_t                      Output vector operand
                                                             Offset for the first DW used from
            3 IN1_OFST          uint8         0,4
                                                             operand 2
Operands    4 IN2_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                             base pointer
            6 IN3_PART          uint8         LOW,HIGH       Word part which is used for operand 5
                                                31   31      32 bit immediate post modification in
            7 IN4_PM_IMM        int32         -2 ..2 -1
                                                             bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rIp_pm_imm_concat (mw_8w, vIn, 0, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic   vstw_v40_indexed_rIp_pm_ptr_concat
name
Spec        vstw {mw [,lp|hp][,concat]} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                MW_options
            1 MW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
            2 IN1_V40           vec40_t                      Output vector operand
Operands
            3 IN1_OFST
                                                             Offset for the first DW used from
                                uint8         0,4

operand 2
            4 IN2_gB_BASE       void *                       Pointer register (gB)
            5 IN3_rI_OFFSET void *                           Pointer (rI) specifying the offset from the
                                                              base pointer
            6 IN3_PART           uint8         LOW,HIGH       Word part which is used for operand 5
            7 IN4_PM_PTR         void*                        Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rIp_pm_ptr_concat (mw_8w, vIn, 0, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic   vstw_v40_pm_imm_concat
name
Spec        vstw {mw [,lp|hp][,concat]} vox[0], (pN)+#imm32_6 [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                               MW_options
            1   MW
                               enum                           of stored elements (see enum definition at
                                                              vec-mem-modes.h)
            2   IN1_V40        vec40_t                        Output vector operand
Operands                                                      Offset for the first DW used from
            3   IN1_OFST       uint8          0,4
                                                              operand 2
            4   IN2_PTR        void *                         Pointer register (rN)

            5                                   31   31       32 bit immediate post modification in
                IN3_IMM32_6 int32             -2 ..2 -1
                                                              bytes
            void* ptr;
            vec40_t vIn;
C example   ...
            vstw_v40_pm_imm_concat (mw_8w, vIn, 0, ptr, 2);

Comments



Intrinsic   vstw_v40_pm_ptr_concat
name
Spec        vstw {mw [,lp|hp][,concat]} vox[0], (pN)[+pm_x] [,?prSC]
syntax
Return      void
type
                                                                 Determines the element size and number
                                MW_options
             1   MW
                                enum                             of stored elements (see enum definition at
                                                                 vec-mem-modes.h)

2   IN1_V40        vec40_t                          Output vector operand
Operands
             3
                                                                 Offset for the first DW used from
                 IN1_OFST       uint8           0,4
                                                                 operand 2
             4   IN2_PTR        void *                           Pointer register (rN)
             5   IN3_PM_PTR void*                                Pointer register (rN)
             void* ptr;
             vec40_t vIn;
C example    ...
             vstw_v40_pm_ptr_concat (mw_8w, vIn, 0, ptr, ptr);

Comments


Main table → Memory Access → Store → Store 16 bit
Available addressing modes
Intrinsic Names:
vstw_v40_direct_hp
vstw_v40_hp
vstw_v40_indexed_imm_hp
vstw_v40_indexed_rI_hp
vstw_v40_indexed_rI_pm_imm_hp
vstw_v40_indexed_rI_pm_ptr_hp
vstw_v40_indexed_rIp_hp
vstw_v40_indexed_rIp_pm_imm_hp
vstw_v40_indexed_rIp_pm_ptr_hp
vstw_v40_pm_imm_hp
vstw_v40_pm_ptr_hp
Intrinsic     vstw_v40_direct_hp
name
Spec syntax   vstw {mw [,lp|hp][,concat]} vox[0], [#address] [,?prSC]

Return        void
type
                                                            Determines the element size and number
                                MW_options
              1      MW
                                enum                        of stored elements (see enum definition at
                                                            vec-mem-modes.h)
Operands
              2      IN1_V40    vec40_t                     Output vector operand
                                                    32
              3      IN2_ADDR   int32          0..2 -1      32 bit address
              vec40_t vIn;
C example     ...
              vstw_v40_direct_hp (mw_8w, vIn, 2);

Comments



Intrinsic     vstw_v40_hp
name
Spec syntax   vstw {mw [,lp|hp][,concat]} vox[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                            Determines the element size and number
                                MW_options
              1      MW
                                enum                        of stored elements (see enum definition at
                                                            vec-mem-modes.h)
Operands
              2      IN1_V40    vec40_t                     Output vector operand
              3      IN2_PTR    void *                      Pointer register (rN)
              void* ptr;

vec40_t vIn;
C example     ...
              vstw_v40_hp (mw_8w, vIn, ptr);

Comments



Intrinsic     vstw_v40_indexed_imm_hp
name
Spec          vstw {mw [,lp|hp][,concat]} vox[0], (gB+#imm16_6) [,?prSC]
syntax
Return        void
type
                                                              Determines the element size and number
                                MW_options
            1 MW
                                enum                          of stored elements (see enum definition
                                                              at vec-mem-modes.h)

Operands    2 IN1_V40           vec40_t                       Output vector operand
            3 IN2_gB_BASE void *                              Pointer register (gB)
                                               -              16 bit immediate post modification in
            4 IN3_IMM16_6       int16
                                               32768..32767   bytes
            void* ptrBase;
            vec40_t vIn;
C example   ...
            vstw_v40_indexed_imm_hp (mw_8w, vIn, ptrBase, 2);

Comments



Intrinsic   vstw_v40_indexed_rI_hp
name
Spec        vstw {mw [,lp|hp][,concat]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 MW_options
            1 MW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)

Operands    2 IN1_V40            vec40_t                      Output vector operand
            3 IN2_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                              base pointer
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rI_hp (mw_8w, vIn, ptrBase, ptrModify);

Comments



Intrinsic   vstw_v40_indexed_rI_pm_imm_hp
name
Spec        vstw {mw [,lp|hp][,concat]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 MW_options
            1 MW

enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_V40            vec40_t                      Output vector operand
Operands    3 IN2_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                              base pointer
                                                  31   31     32 bit immediate post modification in
            5 IN4_PM_IMM         int32          -2 ..2 -1
                                                              bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rI_pm_imm_hp (mw_8w, vIn, ptrBase, ptrModify, 2);

Comments



Intrinsic   vstw_v40_indexed_rI_pm_ptr_hp
name
Spec        vstw {mw [,lp|hp][,concat]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 MW_options
            1 MW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_V40            vec40_t                      Output vector operand
Operands    3 IN2_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                              base pointer
            5 IN4_PM_PTR         void*                        Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rI_pm_ptr_hp (mw_8w, vIn, ptrBase, ptrModify, ptr);

Comments
Intrinsic   vstw_v40_indexed_rIp_hp
name
Spec        vstw {mw [,lp|hp][,concat]} vox[0], (gB+rIp)[+pm] [,?prSC]
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
            vstw_v40_indexed_rIp_hp (mw_8w, vIn, ptrBase, ptrModify, LOW);

Comments



Intrinsic   vstw_v40_indexed_rIp_pm_imm_hp
name
Spec        vstw {mw [,lp|hp][,concat]} vox[0], (gB+rIp)[+pm] [,?prSC]
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
                                                 31   31     32 bit immediate post modification in
            6 IN4_PM_IMM        int32          -2 ..2 -1
                                                             bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rIp_pm_imm_hp (mw_8w, vIn, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic   vstw_v40_indexed_rIp_pm_ptr_hp
name
Spec        vstw {mw [,lp|hp][,concat]} vox[0], (gB+rIp)[+pm] [,?prSC]
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
            6 IN4_PM_PTR        void*                        Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rIp_pm_ptr_hp (mw_8w, vIn, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic   vstw_v40_pm_imm_hp
name
Spec        vstw {mw [,lp|hp][,concat]} vox[0], (pN)+#imm32_6 [,?prSC]
syntax
Return      void
type
                                                           Determines the element size and number
                                MW_options
             1   MW
                                enum                       of stored elements (see enum definition at
                                                           vec-mem-modes.h)

Operands     2   IN1_V40        vec40_t                    Output vector operand
             3   IN2_PTR        void *                     Pointer register (rN)
                                                 31   31   32 bit immediate post modification in
             4   IN3_IMM32_6 int32             -2 ..2 -1
                                                           bytes
             void* ptr;
             vec40_t vIn;
C example    ...
             vstw_v40_pm_imm_hp (mw_8w, vIn, ptr, 2);

Comments



Intrinsic    vstw_v40_pm_ptr_hp
name
Spec         vstw {mw [,lp|hp][,concat]} vox[0], (pN)[+pm_x] [,?prSC]
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
             vstw_v40_pm_ptr_hp (mw_8w, vIn, ptr, ptr);

Comments


Main table → Memory Access → Store → Store 16 bit
Available addressing modes
Intrinsic Names:
vstw_v40_direct_hp_concat
vstw_v40_hp_concat
vstw_v40_indexed_imm_hp_concat
vstw_v40_indexed_rI_hp_concat
vstw_v40_indexed_rI_pm_imm_hp_concat
vstw_v40_indexed_rI_pm_ptr_hp_concat
vstw_v40_indexed_rIp_hp_concat
vstw_v40_indexed_rIp_pm_imm_hp_concat
vstw_v40_indexed_rIp_pm_ptr_hp_concat
vstw_v40_pm_imm_hp_concat
vstw_v40_pm_ptr_hp_concat
Intrinsic     vstw_v40_direct_hp_concat
name
Spec syntax   vstw {mw [,lp|hp][,concat]} vox[0], [#address] [,?prSC]

Return        void
type
                                                            Determines the element size and number
                                MW_options
              1      MW
                                enum                        of stored elements (see enum definition at
                                                            vec-mem-modes.h)
Operands
              2      IN1_V40    vec40_t                     Output vector operand
                                                  32
              3      IN2_ADDR   int32          0..2 -1      32 bit address
              vec40_t vIn;
C example     ...
              vstw_v40_direct_hp_concat (mw_8w, vIn, 2);

Comments



Intrinsic     vstw_v40_hp_concat
name
Spec syntax   vstw {mw [,lp|hp][,concat]} vox[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                            Determines the element size and number
                                MW_options
              1      MW
                                enum                        of stored elements (see enum definition at
                                                            vec-mem-modes.h)
Operands
              2      IN1_V40    vec40_t                     Output vector operand
              3      IN2_PTR    void *                      Pointer register (rN)
              void* ptr;
              vec40_t vIn;
C example     ...
              vstw_v40_hp_concat (mw_8w, vIn, ptr);

Comments



Intrinsic     vstw_v40_indexed_imm_hp_concat
name

Spec          vstw {mw [,lp|hp][,concat]} vox[0], (gB+#imm16_6) [,?prSC]
syntax
Return        void
type
                                                              Determines the element size and number
                                MW_options
            1 MW
                                enum                          of stored elements (see enum definition
                                                              at vec-mem-modes.h)

Operands    2 IN1_V40           vec40_t                       Output vector operand
            3 IN2_gB_BASE void *                              Pointer register (gB)
                                               -              16 bit immediate post modification in
            4 IN3_IMM16_6       int16
                                               32768..32767   bytes
            void* ptrBase;
            vec40_t vIn;
C example   ...
            vstw_v40_indexed_imm_hp_concat (mw_8w, vIn, ptrBase, 2);

Comments



Intrinsic   vstw_v40_indexed_rI_hp_concat
name
Spec        vstw {mw [,lp|hp][,concat]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 MW_options
            1 MW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)

Operands    2 IN1_V40            vec40_t                      Output vector operand
            3 IN2_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                              base pointer
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rI_hp_concat (mw_8w, vIn, ptrBase, ptrModify);

Comments



Intrinsic   vstw_v40_indexed_rI_pm_imm_hp_concat
name
Spec        vstw {mw [,lp|hp][,concat]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 MW_options
            1 MW
                                 enum                         of stored elements (see enum definition

at vec-mem-modes.h)
            2 IN1_V40            vec40_t                      Output vector operand
Operands    3 IN2_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                              base pointer
                                                 31   31      32 bit immediate post modification in
            5 IN4_PM_IMM         int32         -2 ..2 -1
                                                              bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rI_pm_imm_hp_concat (mw_8w, vIn, ptrBase, ptrModify, 2);

Comments



Intrinsic   vstw_v40_indexed_rI_pm_ptr_hp_concat
name
Spec        vstw {mw [,lp|hp][,concat]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 MW_options
            1 MW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_V40            vec40_t                      Output vector operand
Operands    3 IN2_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                              base pointer
            5 IN4_PM_PTR         void*                        Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rI_pm_ptr_hp_concat (mw_8w, vIn, ptrBase, ptrModify, ptr);

Comments
Intrinsic   vstw_v40_indexed_rIp_hp_concat
name
Spec        vstw {mw [,lp|hp][,concat]} vox[0], (gB+rIp)[+pm] [,?prSC]
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
            vstw_v40_indexed_rIp_hp_concat (mw_8w, vIn, ptrBase, ptrModify, LOW);

Comments



Intrinsic   vstw_v40_indexed_rIp_pm_imm_hp_concat
name
Spec        vstw {mw [,lp|hp][,concat]} vox[0], (gB+rIp)[+pm] [,?prSC]
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
                                                 31   31     32 bit immediate post modification in
            6 IN4_PM_IMM        int32          -2 ..2 -1
                                                             bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rIp_pm_imm_hp_concat (mw_8w, vIn, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic   vstw_v40_indexed_rIp_pm_ptr_hp_concat
name
Spec        vstw {mw [,lp|hp][,concat]} vox[0], (gB+rIp)[+pm] [,?prSC]
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
            6 IN4_PM_PTR        void*                        Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rIp_pm_ptr_hp_concat (mw_8w, vIn, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic   vstw_v40_pm_imm_hp_concat
name
Spec        vstw {mw [,lp|hp][,concat]} vox[0], (pN)+#imm32_6 [,?prSC]
syntax
Return      void
type
                                                                  Determines the element size and number
                                 MW_options
              1   MW
                                 enum                             of stored elements (see enum definition at
                                                                  vec-mem-modes.h)

Operands      2   IN1_V40        vec40_t                          Output vector operand
              3   IN2_PTR        void *                           Pointer register (rN)
                                                  31   31         32 bit immediate post modification in
              4   IN3_IMM32_6 int32             -2 ..2 -1
                                                                  bytes
              void* ptr;
              vec40_t vIn;
C example     ...
              vstw_v40_pm_imm_hp_concat (mw_8w, vIn, ptr, 2);

Comments



Intrinsic     vstw_v40_pm_ptr_hp_concat
name
Spec          vstw {mw [,lp|hp][,concat]} vox[0], (pN)[+pm_x] [,?prSC]
syntax
Return        void
type
                                                                  Determines the element size and number
                                 MW_options
              1   MW
                                 enum                             of stored elements (see enum definition at

vec-mem-modes.h)
Operands      2   IN1_V40        vec40_t                          Output vector operand
              3   IN2_PTR        void *                           Pointer register (rN)
              4   IN3_PM_PTR void*                                Pointer register (rN)
              void* ptr;
              vec40_t vIn;
C example     ...
              vstw_v40_pm_ptr_hp_concat (mw_8w, vIn, ptr, ptr);

Comments


Main table → Memory Access → Store → Store 16 bit
Available addressing modes
Intrinsic Names:
vstw_v40_direct_lp
vstw_v40_indexed_imm_lp
vstw_v40_indexed_rI_lp
vstw_v40_indexed_rI_pm_imm_lp
vstw_v40_indexed_rI_pm_ptr_lp
vstw_v40_indexed_rIp_lp
vstw_v40_indexed_rIp_pm_imm_lp
vstw_v40_indexed_rIp_pm_ptr_lp
vstw_v40_lp
vstw_v40_pm_imm_lp
vstw_v40_pm_ptr_lp
Intrinsic     vstw_v40_direct_lp
name
Spec syntax   vstw {mw [,lp|hp][,concat]} vox[0], [#address] [,?prSC]

Return        void
type
                                                               Determines the element size and number
                                MW_options
              1      MW
                                enum                           of stored elements (see enum definition at
                                                               vec-mem-modes.h)
Operands
              2      IN1_V40    vec40_t                        Output vector operand
                                                    32
              3      IN2_ADDR   int32          0..2 -1         32 bit address
              vec40_t vIn;
C example     ...
              vstw_v40_direct_lp (mw_8w, vIn, 2);

Comments



Intrinsic     vstw_v40_indexed_imm_lp
name
Spec          vstw {mw [,lp|hp][,concat]} vox[0], (gB+#imm16_6) [,?prSC]
syntax
Return        void
type
                                                                  Determines the element size and number
                                 MW_options
              1 MW
                                 enum                             of stored elements (see enum definition
                                                                  at vec-mem-modes.h)

Operands      2 IN1_V40          vec40_t                          Output vector operand
              3 IN2_gB_BASE void *                                Pointer register (gB)

              4 IN3_IMM16_6
                                                -                 16 bit immediate post modification in
                                 int16

32768..32767      bytes
              void* ptrBase;
              vec40_t vIn;
C example     ...
              vstw_v40_indexed_imm_lp (mw_8w, vIn, ptrBase, 2);

Comments



Intrinsic     vstw_v40_indexed_rI_lp
name
Spec          vstw {mw [,lp|hp][,concat]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and number
                                 MW_options
            1 MW
                                 enum                          of stored elements (see enum definition
                                                               at vec-mem-modes.h)

Operands    2 IN1_V40            vec40_t                       Output vector operand
            3 IN2_gB_BASE        void *                        Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                               base pointer
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rI_lp (mw_8w, vIn, ptrBase, ptrModify);

Comments



Intrinsic   vstw_v40_indexed_rI_pm_imm_lp
name
Spec        vstw {mw [,lp|hp][,concat]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and number
                                 MW_options
            1 MW
                                 enum                          of stored elements (see enum definition
                                                               at vec-mem-modes.h)
            2 IN1_V40            vec40_t                       Output vector operand
Operands    3 IN2_gB_BASE        void *                        Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                               base pointer
                                                  31   31      32 bit immediate post modification in
            5 IN4_PM_IMM         int32          -2 ..2 -1
                                                               bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...

vstw_v40_indexed_rI_pm_imm_lp (mw_8w, vIn, ptrBase, ptrModify, 2);

Comments
Intrinsic   vstw_v40_indexed_rI_pm_ptr_lp
name
Spec        vstw {mw [,lp|hp][,concat]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and number
                                 MW_options
            1 MW
                                 enum                          of stored elements (see enum definition
                                                               at vec-mem-modes.h)
            2 IN1_V40            vec40_t                       Output vector operand
Operands    3 IN2_gB_BASE        void *                        Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                               base pointer
            5 IN4_PM_PTR         void*                         Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rI_pm_ptr_lp (mw_8w, vIn, ptrBase, ptrModify, ptr);

Comments



Intrinsic   vstw_v40_indexed_rIp_lp
name
Spec        vstw {mw [,lp|hp][,concat]} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and number
                                 MW_options
            1 MW
                                 enum                          of stored elements (see enum definition
                                                               at vec-mem-modes.h)
            2 IN1_V40            vec40_t                       Output vector operand
Operands    3 IN2_gB_BASE        void *                        Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                               base pointer
            5 IN3_PART           uint8          LOW,HIGH       Word part which is used for operand 4
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rIp_lp (mw_8w, vIn, ptrBase, ptrModify, LOW);

Comments



Intrinsic   vstw_v40_indexed_rIp_pm_imm_lp
name

Spec        vstw {mw [,lp|hp][,concat]} vox[0], (gB+rIp)[+pm] [,?prSC]
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
            5 IN3_PART          uint8          LOW,HIGH      Word part which is used for operand 4
                                                 31   31     32 bit immediate post modification in
            6 IN4_PM_IMM        int32          -2 ..2 -1
                                                             bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rIp_pm_imm_lp (mw_8w, vIn, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic   vstw_v40_indexed_rIp_pm_ptr_lp
name
Spec        vstw {mw [,lp|hp][,concat]} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                MW_options                   Determines the element size and number
Operands    1 MW
                                enum                         of stored elements (see enum definition
                                                                at vec-mem-modes.h)
              2 IN1_V40           vec40_t                       Output vector operand
              3 IN2_gB_BASE       void *                        Pointer register (gB)
                                                                Pointer (rI) specifying the offset from the
              4 IN3_rI_OFFSET void *
                                                                base pointer
              5 IN3_PART          uint8          LOW,HIGH       Word part which is used for operand 4
              6 IN4_PM_PTR        void*                         Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;

...
              vstw_v40_indexed_rIp_pm_ptr_lp (mw_8w, vIn, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic     vstw_v40_lp
name
Spec syntax   vstw {mw [,lp|hp][,concat]} vox[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                               Determines the element size and number
                                 MW_options
              1   MW
                                 enum                          of stored elements (see enum definition at
                                                               vec-mem-modes.h)
Operands
              2   IN1_V40        vec40_t                       Output vector operand
              3   IN2_PTR        void *                        Pointer register (rN)
              void* ptr;
              vec40_t vIn;
C example     ...
              vstw_v40_lp (mw_8w, vIn, ptr);

Comments



Intrinsic     vstw_v40_pm_imm_lp
name
Spec          vstw {mw [,lp|hp][,concat]} vox[0], (pN)+#imm32_6 [,?prSC]
syntax
Return        void
type
                                                            Determines the element size and number
                                 MW_options
              1   MW
                                 enum                       of stored elements (see enum definition at
                                                            vec-mem-modes.h)

Operands      2   IN1_V40        vec40_t                    Output vector operand
              3   IN2_PTR        void *                     Pointer register (rN)
                                                  31   31   32 bit immediate post modification in
              4   IN3_IMM32_6 int32             -2 ..2 -1
                                                            bytes
              void* ptr;
              vec40_t vIn;
C example     ...
              vstw_v40_pm_imm_lp (mw_8w, vIn, ptr, 2);

Comments



Intrinsic     vstw_v40_pm_ptr_lp
name
Spec          vstw {mw [,lp|hp][,concat]} vox[0], (pN)[+pm_x] [,?prSC]
syntax
Return        void
type
                                                            Determines the element size and number
                                 MW_options
              1   MW
                                 enum                       of stored elements (see enum definition at
                                                            vec-mem-modes.h)
Operands      2   IN1_V40        vec40_t                    Output vector operand

3   IN2_PTR        void *                     Pointer register (rN)
              4   IN3_PM_PTR void*                          Pointer register (rN)
              void* ptr;
              vec40_t vIn;
C example     ...
              vstw_v40_pm_ptr_lp (mw_8w, vIn, ptr, ptr);

Comments


Main table → Memory Access → Store → Store 16 bit
Available addressing modes
Intrinsic Names:
vstw_v40_direct_lp_concat
vstw_v40_indexed_imm_lp_concat
vstw_v40_indexed_rI_lp_concat
vstw_v40_indexed_rI_pm_imm_lp_concat
vstw_v40_indexed_rI_pm_ptr_lp_concat
vstw_v40_indexed_rIp_lp_concat
vstw_v40_indexed_rIp_pm_imm_lp_concat
vstw_v40_indexed_rIp_pm_ptr_lp_concat
vstw_v40_lp_concat
vstw_v40_pm_imm_lp_concat
vstw_v40_pm_ptr_lp_concat
Intrinsic     vstw_v40_direct_lp_concat
name
Spec syntax   vstw {mw [,lp|hp][,concat]} vox[0], [#address] [,?prSC]

Return        void
type
                                                               Determines the element size and number
                                MW_options
              1      MW
                                enum                           of stored elements (see enum definition at
                                                               vec-mem-modes.h)
Operands
              2      IN1_V40    vec40_t                        Output vector operand
                                                   32
              3      IN2_ADDR   int32          0..2 -1         32 bit address
              vec40_t vIn;
C example     ...
              vstw_v40_direct_lp_concat (mw_8w, vIn, 2);

Comments



Intrinsic     vstw_v40_indexed_imm_lp_concat
name
Spec          vstw {mw [,lp|hp][,concat]} vox[0], (gB+#imm16_6) [,?prSC]
syntax
Return        void
type
                                                               Determines the element size and number
                                 MW_options
              1 MW
                                 enum                          of stored elements (see enum definition
                                                               at vec-mem-modes.h)

Operands      2 IN1_V40          vec40_t                       Output vector operand
              3 IN2_gB_BASE void *                             Pointer register (gB)

              4 IN3_IMM16_6
                                                -              16 bit immediate post modification in
                                 int16
                                                32768..32767   bytes

void* ptrBase;
              vec40_t vIn;
C example     ...
              vstw_v40_indexed_imm_lp_concat (mw_8w, vIn, ptrBase, 2);

Comments



Intrinsic     vstw_v40_indexed_rI_lp_concat
name
Spec          vstw {mw [,lp|hp][,concat]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 MW_options
            1 MW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)

Operands    2 IN1_V40            vec40_t                      Output vector operand
            3 IN2_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                              base pointer
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rI_lp_concat (mw_8w, vIn, ptrBase, ptrModify);

Comments



Intrinsic   vstw_v40_indexed_rI_pm_imm_lp_concat
name
Spec        vstw {mw [,lp|hp][,concat]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 MW_options
            1 MW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_V40            vec40_t                      Output vector operand
Operands    3 IN2_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                              base pointer
                                                  31   31     32 bit immediate post modification in
            5 IN4_PM_IMM         int32          -2 ..2 -1
                                                              bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...

vstw_v40_indexed_rI_pm_imm_lp_concat (mw_8w, vIn, ptrBase, ptrModify, 2);

Comments
Intrinsic   vstw_v40_indexed_rI_pm_ptr_lp_concat
name
Spec        vstw {mw [,lp|hp][,concat]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 MW_options
            1 MW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_V40            vec40_t                      Output vector operand
Operands    3 IN2_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                              base pointer
            5 IN4_PM_PTR         void*                        Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rI_pm_ptr_lp_concat (mw_8w, vIn, ptrBase, ptrModify, ptr);

Comments



Intrinsic   vstw_v40_indexed_rIp_lp_concat
name
Spec        vstw {mw [,lp|hp][,concat]} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 MW_options
            1 MW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_V40            vec40_t                      Output vector operand
Operands    3 IN2_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                              base pointer
            5 IN3_PART           uint8          LOW,HIGH      Word part which is used for operand 4
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rIp_lp_concat (mw_8w, vIn, ptrBase, ptrModify, LOW);

Comments



Intrinsic   vstw_v40_indexed_rIp_pm_imm_lp_concat
name

Spec        vstw {mw [,lp|hp][,concat]} vox[0], (gB+rIp)[+pm] [,?prSC]
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
            5 IN3_PART          uint8          LOW,HIGH      Word part which is used for operand 4
                                                 31   31     32 bit immediate post modification in
            6 IN4_PM_IMM        int32          -2 ..2 -1
                                                             bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rIp_pm_imm_lp_concat (mw_8w, vIn, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic   vstw_v40_indexed_rIp_pm_ptr_lp_concat
name
Spec        vstw {mw [,lp|hp][,concat]} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                MW_options                   Determines the element size and number
Operands    1 MW
                                enum                         of stored elements (see enum definition
                                                                at vec-mem-modes.h)
              2 IN1_V40           vec40_t                       Output vector operand
              3 IN2_gB_BASE       void *                        Pointer register (gB)
                                                                Pointer (rI) specifying the offset from the
              4 IN3_rI_OFFSET void *
                                                                base pointer
              5 IN3_PART          uint8          LOW,HIGH       Word part which is used for operand 4
              6 IN4_PM_PTR        void*                         Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;

C example     vec40_t vIn;
              ...
              vstw_v40_indexed_rIp_pm_ptr_lp_concat (mw_8w, vIn, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic     vstw_v40_lp_concat
name
Spec syntax   vstw {mw [,lp|hp][,concat]} vox[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                               Determines the element size and number
                                 MW_options
              1   MW
                                 enum                          of stored elements (see enum definition at
                                                               vec-mem-modes.h)
Operands
              2   IN1_V40        vec40_t                       Output vector operand
              3   IN2_PTR        void *                        Pointer register (rN)
              void* ptr;
              vec40_t vIn;
C example     ...
              vstw_v40_lp_concat (mw_8w, vIn, ptr);

Comments



Intrinsic     vstw_v40_pm_imm_lp_concat
name
Spec          vstw {mw [,lp|hp][,concat]} vox[0], (pN)+#imm32_6 [,?prSC]
syntax
Return        void
type
                                                                Determines the element size and number
                               MW_options
            1   MW
                               enum                             of stored elements (see enum definition at
                                                                vec-mem-modes.h)

Operands    2   IN1_V40        vec40_t                          Output vector operand
            3   IN2_PTR        void *                           Pointer register (rN)
                                                31   31         32 bit immediate post modification in
            4   IN3_IMM32_6 int32             -2 ..2 -1
                                                                bytes
            void* ptr;
            vec40_t vIn;
C example   ...
            vstw_v40_pm_imm_lp_concat (mw_8w, vIn, ptr, 2);

Comments



Intrinsic   vstw_v40_pm_ptr_lp_concat
name
Spec        vstw {mw [,lp|hp][,concat]} vox[0], (pN)[+pm_x] [,?prSC]
syntax
Return      void
type
                                                                Determines the element size and number
                               MW_options
            1   MW
                               enum                             of stored elements (see enum definition at
                                                                vec-mem-modes.h)

Operands    2   IN1_V40        vec40_t                          Output vector operand
            3   IN2_PTR        void *                           Pointer register (rN)
            4   IN3_PM_PTR void*                                Pointer register (rN)
            void* ptr;
            vec40_t vIn;
C example   ...
            vstw_v40_pm_ptr_lp_concat (mw_8w, vIn, ptr, ptr);

Comments


Main table → Memory Access → Store → Store 16 bit
Available addressing modes
Intrinsic Names:
vstw_v32
vstw_v32_direct
vstw_v32_indexed_imm
vstw_v32_indexed_rI
vstw_v32_indexed_rI_pm_imm
vstw_v32_indexed_rI_pm_ptr
vstw_v32_indexed_rIp
vstw_v32_indexed_rIp_pm_imm
vstw_v32_indexed_rIp_pm_ptr
vstw_v32_pm_imm
vstw_v32_pm_ptr
Intrinsic     vstw_v32
name
Spec syntax   vstw {mw [,lp|hp][,concat]} vix[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                             Determines the element size and number
                                 MW_options
              1   MW
                                 enum                        of stored elements (see enum definition at
                                                             vec-mem-modes.h)
Operands      2   IN1_V32        vec_t                       Input vector operand

              3   IN1_OFST       uint8          0,4
                                                             Offset for the first DW used from operand
                                                             2

              4   IN2_PTR        void *                      Pointer register (rN)
              void* ptr;
              vec_t vIn;
C example     ...
              vstw_v32 (mw_8w, vIn, 0, ptr);

Comments



Intrinsic     vstw_v32_direct
name
Spec syntax   vstw {mw [,lp|hp][,concat]} vix[0], [#address] [,?prSC]

Return        void
type
                                                             Determines the element size and number
                                 MW_options
              1   MW
                                 enum                        of stored elements (see enum definition at
                                                             vec-mem-modes.h)
Operands      2   IN1_V32        vec_t                       Input vector operand

              3   IN1_OFST       uint8          0,4
                                                             Offset for the first DW used from operand
                                                             2

32
              4   IN2_ADDR       int32          0..2 -1      32 bit address
              vec_t vIn;
C example     ...
              vstw_v32_direct (mw_8w, vIn, 0, 2);

Comments



Intrinsic     vstw_v32_indexed_imm
name
Spec        vstw {mw [,lp|hp][,concat]} vix[0], (gB+#imm16_6) [,?prSC]
syntax
Return      void
type
                                                                Determines the element size and number
                                 MW_options
            1 MW
                                 enum                           of stored elements (see enum definition
                                                                at vec-mem-modes.h)
            2 IN1_V32            vec_t                          Input vector operand
Operands                                                        Offset for the first DW used from
            3 IN1_OFST           uint8          0,4
                                                                operand 2
            4 IN2_gB_BASE void *                                Pointer register (gB)
                                                -               16 bit immediate post modification in
            5 IN3_IMM16_6        int16
                                                32768..32767    bytes
            void* ptrBase;
            vec_t vIn;
C example   ...
            vstw_v32_indexed_imm (mw_8w, vIn, 0, ptrBase, 2);

Comments



Intrinsic   vstw_v32_indexed_rI
name
Spec        vstw {mw [,lp|hp][,concat]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                                Determines the element size and number
                                 MW_options
            1 MW
                                 enum                           of stored elements (see enum definition
                                                                at vec-mem-modes.h)
            2 IN1_V32            vec_t                          Input vector operand
Operands                                                        Offset for the first DW used from
            3 IN1_OFST           uint8          0,4
                                                                operand 2
            4 IN2_gB_BASE        void *                         Pointer register (gB)
                                                                Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *

base pointer
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rI (mw_8w, vIn, 0, ptrBase, ptrModify);
Comments



Intrinsic   vstw_v32_indexed_rI_pm_imm
name
Spec        vstw {mw [,lp|hp][,concat]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                MW_options
            1 MW
                                enum                          of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_V32           vec_t                         Input vector operand
                                                              Offset for the first DW used from
            3 IN1_OFST          uint8          0,4
Operands                                                      operand 2
            4 IN2_gB_BASE       void *                        Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                              base pointer

            6 IN4_PM_IMM                         31   31      32 bit immediate post modification in
                                int32          -2 ..2 -1
                                                              bytes
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rI_pm_imm (mw_8w, vIn, 0, ptrBase, ptrModify, 2);

Comments



Intrinsic   vstw_v32_indexed_rI_pm_ptr
name
Spec        vstw {mw [,lp|hp][,concat]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                MW_options
            1 MW
                                enum                          of stored elements (see enum definition
                                                              at vec-mem-modes.h)
Operands
            2 IN1_V32           vec_t                         Input vector operand
            3 IN1_OFST          uint8          0,4            Offset for the first DW used from
                                                               operand 2

4 IN2_gB_BASE        void *                        Pointer register (gB)

            5 IN3_rI_OFFSET void *
                                                               Pointer (rI) specifying the offset from the
                                                               base pointer
            6 IN4_PM_PTR         void*                         Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rI_pm_ptr (mw_8w, vIn, 0, ptrBase, ptrModify, ptr);

Comments



Intrinsic   vstw_v32_indexed_rIp
name
Spec        vstw {mw [,lp|hp][,concat]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and number
                                 MW_options
            1 MW
                                 enum                          of stored elements (see enum definition
                                                               at vec-mem-modes.h)
            2 IN1_V32            vec_t                         Input vector operand
                                                               Offset for the first DW used from
Operands    3 IN1_OFST           uint8          0,4
                                                               operand 2
            4 IN2_gB_BASE        void *                        Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                               base pointer
            6 IN3_PART           uint8          LOW,HIGH       Word part which is used for operand 5
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rIp (mw_8w, vIn, 0, ptrBase, ptrModify, LOW);

Comments



Intrinsic   vstw_v32_indexed_rIp_pm_imm
name
Spec        vstw {mw [,lp|hp][,concat]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                MW_options
            1 MW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)

2 IN1_V32           vec_t                        Input vector operand
                                                             Offset for the first DW used from
            3 IN1_OFST          uint8          0,4
                                                             operand 2
Operands    4 IN2_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                             base pointer
            6 IN3_PART          uint8          LOW,HIGH      Word part which is used for operand 5
                                                31   31      32 bit immediate post modification in
            7 IN4_PM_IMM        int32          -2 ..2 -1
                                                             bytes
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rIp_pm_imm (mw_8w, vIn, 0, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic   vstw_v32_indexed_rIp_pm_ptr
name
Spec        vstw {mw [,lp|hp][,concat]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                MW_options
            1 MW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
            2 IN1_V32           vec_t                        Input vector operand
Operands
            3 IN1_OFST
                                                             Offset for the first DW used from
                                uint8          0,4
                                                             operand 2
            4 IN2_gB_BASE       void *                       Pointer register (gB)
            5 IN3_rI_OFFSET void *                           Pointer (rI) specifying the offset from the
                                                              base pointer
            6 IN3_PART           uint8          LOW,HIGH      Word part which is used for operand 5
            7 IN4_PM_PTR         void*                        Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...

vstw_v32_indexed_rIp_pm_ptr (mw_8w, vIn, 0, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic   vstw_v32_pm_imm
name
Spec        vstw {mw [,lp|hp][,concat]} vix[0], (pN)+#imm32_6 [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                               MW_options
            1   MW
                               enum                           of stored elements (see enum definition at
                                                              vec-mem-modes.h)
            2   IN1_V32        vec_t                          Input vector operand
Operands                                                      Offset for the first DW used from
            3   IN1_OFST       uint8          0,4
                                                              operand 2
            4   IN2_PTR        void *                         Pointer register (rN)

            5                                   31     31     32 bit immediate post modification in
                IN3_IMM32_6 int32             -2 ..2 -1
                                                              bytes
            void* ptr;
            vec_t vIn;
C example   ...
            vstw_v32_pm_imm (mw_8w, vIn, 0, ptr, 2);

Comments



Intrinsic   vstw_v32_pm_ptr
name
Spec        vstw {mw [,lp|hp][,concat]} vix[0], (pN)[+pm_x] [,?prSC]
syntax
Return      void
type
                                                           Determines the element size and number
                                 MW_options
              1   MW
                                 enum                      of stored elements (see enum definition at
                                                           vec-mem-modes.h)
              2   IN1_V32        vec_t                     Input vector operand
Operands
              3
                                                           Offset for the first DW used from
                  IN1_OFST       uint8           0,4
                                                           operand 2
              4   IN2_PTR        void *                    Pointer register (rN)
              5   IN3_PM_PTR void*                         Pointer register (rN)
              void* ptr;
              vec_t vIn;
C example     ...
              vstw_v32_pm_ptr (mw_8w, vIn, 0, ptr, ptr);

Comments


Main table → Memory Access → Store → Store 16 bit
Available addressing modes
Intrinsic Names:

vstw_v32_concat
vstw_v32_direct_concat
vstw_v32_indexed_imm_concat
vstw_v32_indexed_rI_concat
vstw_v32_indexed_rI_pm_imm_concat
vstw_v32_indexed_rI_pm_ptr_concat
vstw_v32_indexed_rIp_concat
vstw_v32_indexed_rIp_pm_imm_concat
vstw_v32_indexed_rIp_pm_ptr_concat
vstw_v32_pm_imm_concat
vstw_v32_pm_ptr_concat
Intrinsic     vstw_v32_concat
name
Spec syntax   vstw {mw [,lp|hp][,concat]} vix[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                             Determines the element size and number
                                 MW_options
              1   MW
                                 enum                        of stored elements (see enum definition at
                                                             vec-mem-modes.h)
Operands      2   IN1_V32        vec_t                       Input vector operand

              3   IN1_OFST       uint8          0,4
                                                             Offset for the first DW used from operand
                                                             2

              4   IN2_PTR        void *                      Pointer register (rN)
              void* ptr;
              vec_t vIn;
C example     ...
              vstw_v32_concat (mw_8w, vIn, 0, ptr);

Comments



Intrinsic     vstw_v32_direct_concat
name
Spec syntax   vstw {mw [,lp|hp][,concat]} vix[0], [#address] [,?prSC]

Return        void
type
                                                             Determines the element size and number
                                 MW_options
              1   MW
                                 enum                        of stored elements (see enum definition at
                                                             vec-mem-modes.h)
Operands      2   IN1_V32        vec_t                       Input vector operand

              3   IN1_OFST       uint8          0,4
                                                             Offset for the first DW used from operand
                                                             2
                                                      32
              4   IN2_ADDR       int32          0..2 -1      32 bit address
              vec_t vIn;
C example     ...
              vstw_v32_direct_concat (mw_8w, vIn, 0, 2);

Comments



Intrinsic     vstw_v32_indexed_imm_concat
name
Spec        vstw {mw [,lp|hp][,concat]} vix[0], (gB+#imm16_6) [,?prSC]
syntax
Return      void
type

Determines the element size and number
                                MW_options
            1 MW
                                enum                           of stored elements (see enum definition
                                                               at vec-mem-modes.h)
            2 IN1_V32           vec_t                          Input vector operand
Operands                                                       Offset for the first DW used from
            3 IN1_OFST          uint8           0,4
                                                               operand 2
            4 IN2_gB_BASE void *                               Pointer register (gB)
                                                -              16 bit immediate post modification in
            5 IN3_IMM16_6       int16
                                                32768..32767   bytes
            void* ptrBase;
            vec_t vIn;
C example   ...
            vstw_v32_indexed_imm_concat (mw_8w, vIn, 0, ptrBase, 2);

Comments



Intrinsic   vstw_v32_indexed_rI_concat
name
Spec        vstw {mw [,lp|hp][,concat]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and number
                                 MW_options
            1 MW
                                 enum                          of stored elements (see enum definition
                                                               at vec-mem-modes.h)
            2 IN1_V32            vec_t                         Input vector operand
Operands                                                       Offset for the first DW used from
            3 IN1_OFST           uint8          0,4
                                                               operand 2
            4 IN2_gB_BASE        void *                        Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                               base pointer
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rI_concat (mw_8w, vIn, 0, ptrBase, ptrModify);
Comments



Intrinsic   vstw_v32_indexed_rI_pm_imm_concat
name
Spec        vstw {mw [,lp|hp][,concat]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type

Determines the element size and number
                                MW_options
            1 MW
                                enum                          of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_V32           vec_t                         Input vector operand
                                                              Offset for the first DW used from
            3 IN1_OFST          uint8          0,4
Operands                                                      operand 2
            4 IN2_gB_BASE       void *                        Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                              base pointer

            6 IN4_PM_IMM                         31   31      32 bit immediate post modification in
                                int32          -2 ..2 -1
                                                              bytes
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rI_pm_imm_concat (mw_8w, vIn, 0, ptrBase, ptrModify, 2);

Comments



Intrinsic   vstw_v32_indexed_rI_pm_ptr_concat
name
Spec        vstw {mw [,lp|hp][,concat]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                MW_options
            1 MW
                                enum                          of stored elements (see enum definition
                                                              at vec-mem-modes.h)
Operands
            2 IN1_V32           vec_t                         Input vector operand
            3 IN1_OFST          uint8          0,4            Offset for the first DW used from
                                                               operand 2
            4 IN2_gB_BASE        void *                        Pointer register (gB)

            5 IN3_rI_OFFSET void *
                                                               Pointer (rI) specifying the offset from the
                                                               base pointer
            6 IN4_PM_PTR         void*                         Pointer register (rN)
            void* ptr;

void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rI_pm_ptr_concat (mw_8w, vIn, 0, ptrBase, ptrModify, ptr);

Comments



Intrinsic   vstw_v32_indexed_rIp_concat
name
Spec        vstw {mw [,lp|hp][,concat]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and number
                                 MW_options
            1 MW
                                 enum                          of stored elements (see enum definition
                                                               at vec-mem-modes.h)
            2 IN1_V32            vec_t                         Input vector operand
                                                               Offset for the first DW used from
Operands    3 IN1_OFST           uint8          0,4
                                                               operand 2
            4 IN2_gB_BASE        void *                        Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                               base pointer
            6 IN3_PART           uint8          LOW,HIGH       Word part which is used for operand 5
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rIp_concat (mw_8w, vIn, 0, ptrBase, ptrModify, LOW);

Comments



Intrinsic   vstw_v32_indexed_rIp_pm_imm_concat
name
Spec        vstw {mw [,lp|hp][,concat]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                MW_options
            1 MW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
            2 IN1_V32           vec_t                        Input vector operand
                                                             Offset for the first DW used from
            3 IN1_OFST          uint8         0,4
                                                             operand 2
Operands    4 IN2_gB_BASE       void *                       Pointer register (gB)

Pointer (rI) specifying the offset from the
            5 IN3_rI_OFFSET void *
                                                             base pointer
            6 IN3_PART          uint8         LOW,HIGH       Word part which is used for operand 5
                                                31   31      32 bit immediate post modification in
            7 IN4_PM_IMM        int32         -2 ..2 -1
                                                             bytes
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rIp_pm_imm_concat (mw_8w, vIn, 0, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic   vstw_v32_indexed_rIp_pm_ptr_concat
name
Spec        vstw {mw [,lp|hp][,concat]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                MW_options
            1 MW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
            2 IN1_V32           vec_t                        Input vector operand
Operands
            3 IN1_OFST
                                                             Offset for the first DW used from
                                uint8         0,4
                                                             operand 2
            4 IN2_gB_BASE       void *                       Pointer register (gB)
            5 IN3_rI_OFFSET void *                           Pointer (rI) specifying the offset from the
                                                              base pointer
            6 IN3_PART           uint8         LOW,HIGH       Word part which is used for operand 5
            7 IN4_PM_PTR         void*                        Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rIp_pm_ptr_concat (mw_8w, vIn, 0, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic   vstw_v32_pm_imm_concat
name
Spec        vstw {mw [,lp|hp][,concat]} vix[0], (pN)+#imm32_6 [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                               MW_options
            1   MW

enum                           of stored elements (see enum definition at
                                                              vec-mem-modes.h)
            2   IN1_V32        vec_t                          Input vector operand
Operands                                                      Offset for the first DW used from
            3   IN1_OFST       uint8          0,4
                                                              operand 2
            4   IN2_PTR        void *                         Pointer register (rN)

            5                                   31   31       32 bit immediate post modification in
                IN3_IMM32_6 int32             -2 ..2 -1
                                                              bytes
            void* ptr;
            vec_t vIn;
C example   ...
            vstw_v32_pm_imm_concat (mw_8w, vIn, 0, ptr, 2);

Comments



Intrinsic   vstw_v32_pm_ptr_concat
name
Spec        vstw {mw [,lp|hp][,concat]} vix[0], (pN)[+pm_x] [,?prSC]
syntax
Return      void
type
                                                                 Determines the element size and number
                                MW_options
             1   MW
                                enum                             of stored elements (see enum definition at
                                                                 vec-mem-modes.h)
             2   IN1_V32        vec_t                            Input vector operand
Operands
             3
                                                                 Offset for the first DW used from
                 IN1_OFST       uint8           0,4
                                                                 operand 2
             4   IN2_PTR        void *                           Pointer register (rN)
             5   IN3_PM_PTR void*                                Pointer register (rN)
             void* ptr;
             vec_t vIn;
C example    ...
             vstw_v32_pm_ptr_concat (mw_8w, vIn, 0, ptr, ptr);

Comments


Main table → Memory Access → Store → Store 16 bit
Available addressing modes
Intrinsic Names:
vstw_v32_direct_hp
vstw_v32_hp
vstw_v32_indexed_imm_hp
vstw_v32_indexed_rI_hp
vstw_v32_indexed_rI_pm_imm_hp
vstw_v32_indexed_rI_pm_ptr_hp
vstw_v32_indexed_rIp_hp
vstw_v32_indexed_rIp_pm_imm_hp
vstw_v32_indexed_rIp_pm_ptr_hp
vstw_v32_pm_imm_hp
vstw_v32_pm_ptr_hp
Intrinsic     vstw_v32_direct_hp
name

Spec syntax   vstw {mw [,lp|hp][,concat]} vix[0], [#address] [,?prSC]

Return        void
type
                                                             Determines the element size and number
                                MW_options
              1      MW
                                enum                         of stored elements (see enum definition at
                                                             vec-mem-modes.h)
Operands
              2      IN1_V32    vec_t                        Input vector operand
                                                    32
              3      IN2_ADDR   int32          0..2 -1       32 bit address
              vec_t vIn;
C example     ...
              vstw_v32_direct_hp (mw_8w, vIn, 2);

Comments



Intrinsic     vstw_v32_hp
name
Spec syntax   vstw {mw [,lp|hp][,concat]} vix[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                             Determines the element size and number
                                MW_options
              1      MW
                                enum                         of stored elements (see enum definition at
                                                             vec-mem-modes.h)
Operands
              2      IN1_V32    vec_t                        Input vector operand
              3      IN2_PTR    void *                       Pointer register (rN)
              void* ptr;
              vec_t vIn;
C example     ...
              vstw_v32_hp (mw_8w, vIn, ptr);

Comments



Intrinsic     vstw_v32_indexed_imm_hp
name
Spec          vstw {mw [,lp|hp][,concat]} vix[0], (gB+#imm16_6) [,?prSC]
syntax
Return        void
type
                                                                Determines the element size and number
                                MW_options
            1 MW
                                enum                            of stored elements (see enum definition
                                                                at vec-mem-modes.h)

Operands    2 IN1_V32           vec_t                           Input vector operand
            3 IN2_gB_BASE void *                                Pointer register (gB)
                                               -                16 bit immediate post modification in
            4 IN3_IMM16_6       int16
                                               32768..32767     bytes
            void* ptrBase;
            vec_t vIn;
C example   ...

vstw_v32_indexed_imm_hp (mw_8w, vIn, ptrBase, 2);

Comments



Intrinsic   vstw_v32_indexed_rI_hp
name
Spec        vstw {mw [,lp|hp][,concat]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 MW_options
            1 MW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)

Operands    2 IN1_V32            vec_t                        Input vector operand
            3 IN2_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                              base pointer
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rI_hp (mw_8w, vIn, ptrBase, ptrModify);

Comments



Intrinsic   vstw_v32_indexed_rI_pm_imm_hp
name
Spec        vstw {mw [,lp|hp][,concat]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 MW_options
            1 MW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_V32            vec_t                        Input vector operand
Operands    3 IN2_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                              base pointer
                                                  31   31     32 bit immediate post modification in
            5 IN4_PM_IMM         int32          -2 ..2 -1
                                                              bytes
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rI_pm_imm_hp (mw_8w, vIn, ptrBase, ptrModify, 2);

Comments



Intrinsic   vstw_v32_indexed_rI_pm_ptr_hp
name

Spec        vstw {mw [,lp|hp][,concat]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 MW_options
            1 MW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_V32            vec_t                        Input vector operand
Operands    3 IN2_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                              base pointer
            5 IN4_PM_PTR         void*                        Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rI_pm_ptr_hp (mw_8w, vIn, ptrBase, ptrModify, ptr);

Comments
Intrinsic   vstw_v32_indexed_rIp_hp
name
Spec        vstw {mw [,lp|hp][,concat]} vix[0], (gB+rIp)[+pm] [,?prSC]
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
            vstw_v32_indexed_rIp_hp (mw_8w, vIn, ptrBase, ptrModify, LOW);

Comments



Intrinsic   vstw_v32_indexed_rIp_pm_imm_hp
name
Spec        vstw {mw [,lp|hp][,concat]} vix[0], (gB+rIp)[+pm] [,?prSC]
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
                                                 31   31     32 bit immediate post modification in
            6 IN4_PM_IMM        int32          -2 ..2 -1
                                                             bytes
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rIp_pm_imm_hp (mw_8w, vIn, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic   vstw_v32_indexed_rIp_pm_ptr_hp
name
Spec        vstw {mw [,lp|hp][,concat]} vix[0], (gB+rIp)[+pm] [,?prSC]
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
            6 IN4_PM_PTR        void*                        Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rIp_pm_ptr_hp (mw_8w, vIn, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic   vstw_v32_pm_imm_hp
name

Spec        vstw {mw [,lp|hp][,concat]} vix[0], (pN)+#imm32_6 [,?prSC]
syntax
Return      void
type
                                                            Determines the element size and number
                                MW_options
             1   MW
                                enum                        of stored elements (see enum definition at
                                                            vec-mem-modes.h)

Operands     2   IN1_V32        vec_t                       Input vector operand
             3   IN2_PTR        void *                      Pointer register (rN)
                                                 31   31    32 bit immediate post modification in
             4   IN3_IMM32_6 int32             -2 ..2 -1
                                                            bytes
             void* ptr;
             vec_t vIn;
C example    ...
             vstw_v32_pm_imm_hp (mw_8w, vIn, ptr, 2);

Comments



Intrinsic    vstw_v32_pm_ptr_hp
name
Spec         vstw {mw [,lp|hp][,concat]} vix[0], (pN)[+pm_x] [,?prSC]
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
             vstw_v32_pm_ptr_hp (mw_8w, vIn, ptr, ptr);

Comments


Main table → Memory Access → Store → Store 16 bit
Available addressing modes
Intrinsic Names:
vstw_v32_direct_hp_concat
vstw_v32_hp_concat
vstw_v32_indexed_imm_hp_concat
vstw_v32_indexed_rI_hp_concat
vstw_v32_indexed_rI_pm_imm_hp_concat
vstw_v32_indexed_rI_pm_ptr_hp_concat
vstw_v32_indexed_rIp_hp_concat
vstw_v32_indexed_rIp_pm_imm_hp_concat
vstw_v32_indexed_rIp_pm_ptr_hp_concat
vstw_v32_pm_imm_hp_concat
vstw_v32_pm_ptr_hp_concat
Intrinsic     vstw_v32_direct_hp_concat
name
Spec syntax   vstw {mw [,lp|hp][,concat]} vix[0], [#address] [,?prSC]

Return        void
type
                                                             Determines the element size and number

MW_options
              1      MW
                                enum                         of stored elements (see enum definition at
                                                             vec-mem-modes.h)
Operands
              2      IN1_V32    vec_t                        Input vector operand
                                                  32
              3      IN2_ADDR   int32          0..2 -1       32 bit address
              vec_t vIn;
C example     ...
              vstw_v32_direct_hp_concat (mw_8w, vIn, 2);

Comments



Intrinsic     vstw_v32_hp_concat
name
Spec syntax   vstw {mw [,lp|hp][,concat]} vix[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                             Determines the element size and number
                                MW_options
              1      MW
                                enum                         of stored elements (see enum definition at
                                                             vec-mem-modes.h)
Operands
              2      IN1_V32    vec_t                        Input vector operand
              3      IN2_PTR    void *                       Pointer register (rN)
              void* ptr;
              vec_t vIn;
C example     ...
              vstw_v32_hp_concat (mw_8w, vIn, ptr);

Comments



Intrinsic     vstw_v32_indexed_imm_hp_concat
name
Spec          vstw {mw [,lp|hp][,concat]} vix[0], (gB+#imm16_6) [,?prSC]
syntax
Return        void
type
                                                              Determines the element size and number
                                MW_options
            1 MW
                                enum                          of stored elements (see enum definition
                                                              at vec-mem-modes.h)

Operands    2 IN1_V32           vec_t                         Input vector operand
            3 IN2_gB_BASE void *                              Pointer register (gB)
                                               -              16 bit immediate post modification in
            4 IN3_IMM16_6       int16
                                               32768..32767   bytes
            void* ptrBase;
            vec_t vIn;
C example   ...
            vstw_v32_indexed_imm_hp_concat (mw_8w, vIn, ptrBase, 2);

Comments



Intrinsic   vstw_v32_indexed_rI_hp_concat
name
Spec        vstw {mw [,lp|hp][,concat]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax

Return      void
type
                                                              Determines the element size and number
                                 MW_options
            1 MW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)

Operands    2 IN1_V32            vec_t                        Input vector operand
            3 IN2_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                              base pointer
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rI_hp_concat (mw_8w, vIn, ptrBase, ptrModify);

Comments



Intrinsic   vstw_v32_indexed_rI_pm_imm_hp_concat
name
Spec        vstw {mw [,lp|hp][,concat]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 MW_options
            1 MW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_V32            vec_t                        Input vector operand
Operands    3 IN2_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                              base pointer
                                                 31   31      32 bit immediate post modification in
            5 IN4_PM_IMM         int32         -2 ..2 -1
                                                              bytes
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rI_pm_imm_hp_concat (mw_8w, vIn, ptrBase, ptrModify, 2);

Comments



Intrinsic   vstw_v32_indexed_rI_pm_ptr_hp_concat
name
Spec        vstw {mw [,lp|hp][,concat]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number

MW_options
            1 MW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_V32            vec_t                        Input vector operand
Operands    3 IN2_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                              base pointer
            5 IN4_PM_PTR         void*                        Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rI_pm_ptr_hp_concat (mw_8w, vIn, ptrBase, ptrModify, ptr);

Comments
Intrinsic   vstw_v32_indexed_rIp_hp_concat
name
Spec        vstw {mw [,lp|hp][,concat]} vix[0], (gB+rIp)[+pm] [,?prSC]
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
            vstw_v32_indexed_rIp_hp_concat (mw_8w, vIn, ptrBase, ptrModify, LOW);

Comments



Intrinsic   vstw_v32_indexed_rIp_pm_imm_hp_concat
name
Spec        vstw {mw [,lp|hp][,concat]} vix[0], (gB+rIp)[+pm] [,?prSC]
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
                                                 31   31     32 bit immediate post modification in
            6 IN4_PM_IMM        int32          -2 ..2 -1
                                                             bytes
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rIp_pm_imm_hp_concat (mw_8w, vIn, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic   vstw_v32_indexed_rIp_pm_ptr_hp_concat
name
Spec        vstw {mw [,lp|hp][,concat]} vix[0], (gB+rIp)[+pm] [,?prSC]
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
            6 IN4_PM_PTR        void*                        Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rIp_pm_ptr_hp_concat (mw_8w, vIn, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic   vstw_v32_pm_imm_hp_concat
name
Spec        vstw {mw [,lp|hp][,concat]} vix[0], (pN)+#imm32_6 [,?prSC]
syntax
Return      void
type
                                                                  Determines the element size and number
                                 MW_options

1   MW
                                 enum                             of stored elements (see enum definition at
                                                                  vec-mem-modes.h)

Operands      2   IN1_V32        vec_t                            Input vector operand
              3   IN2_PTR        void *                           Pointer register (rN)
                                                  31   31         32 bit immediate post modification in
              4   IN3_IMM32_6 int32             -2 ..2 -1
                                                                  bytes
              void* ptr;
              vec_t vIn;
C example     ...
              vstw_v32_pm_imm_hp_concat (mw_8w, vIn, ptr, 2);

Comments



Intrinsic     vstw_v32_pm_ptr_hp_concat
name
Spec          vstw {mw [,lp|hp][,concat]} vix[0], (pN)[+pm_x] [,?prSC]
syntax
Return        void
type
                                                                  Determines the element size and number
                                 MW_options
              1   MW
                                 enum                             of stored elements (see enum definition at
                                                                  vec-mem-modes.h)
Operands      2   IN1_V32        vec_t                            Input vector operand
              3   IN2_PTR        void *                           Pointer register (rN)
              4   IN3_PM_PTR void*                                Pointer register (rN)
              void* ptr;
              vec_t vIn;
C example     ...
              vstw_v32_pm_ptr_hp_concat (mw_8w, vIn, ptr, ptr);

Comments


Main table → Memory Access → Store → Store 16 bit
Available addressing modes
Intrinsic Names:
vstw_v32_direct_lp
vstw_v32_indexed_imm_lp
vstw_v32_indexed_rI_lp
vstw_v32_indexed_rI_pm_imm_lp
vstw_v32_indexed_rI_pm_ptr_lp
vstw_v32_indexed_rIp_lp
vstw_v32_indexed_rIp_pm_imm_lp
vstw_v32_indexed_rIp_pm_ptr_lp
vstw_v32_lp
vstw_v32_pm_imm_lp
vstw_v32_pm_ptr_lp
Intrinsic     vstw_v32_direct_lp
name
Spec syntax   vstw {mw [,lp|hp][,concat]} vix[0], [#address] [,?prSC]

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
              vstw_v32_direct_lp (mw_8w, vIn, 2);

Comments



Intrinsic     vstw_v32_indexed_imm_lp
name
Spec          vstw {mw [,lp|hp][,concat]} vix[0], (gB+#imm16_6) [,?prSC]
syntax
Return        void
type
                                                                  Determines the element size and number
                                 MW_options
              1 MW
                                 enum                             of stored elements (see enum definition
                                                                  at vec-mem-modes.h)

Operands      2 IN1_V32          vec_t                            Input vector operand
              3 IN2_gB_BASE void *                                Pointer register (gB)

              4 IN3_IMM16_6
                                                -                 16 bit immediate post modification in
                                 int16
                                                32768..32767      bytes
              void* ptrBase;
              vec_t vIn;
C example     ...
              vstw_v32_indexed_imm_lp (mw_8w, vIn, ptrBase, 2);

Comments



Intrinsic     vstw_v32_indexed_rI_lp
name
Spec          vstw {mw [,lp|hp][,concat]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and number
                                 MW_options
            1 MW
                                 enum                          of stored elements (see enum definition
                                                               at vec-mem-modes.h)

Operands    2 IN1_V32            vec_t                         Input vector operand
            3 IN2_gB_BASE        void *                        Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                               base pointer
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rI_lp (mw_8w, vIn, ptrBase, ptrModify);

Comments

Intrinsic   vstw_v32_indexed_rI_pm_imm_lp
name
Spec        vstw {mw [,lp|hp][,concat]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and number
                                 MW_options
            1 MW
                                 enum                          of stored elements (see enum definition
                                                               at vec-mem-modes.h)
            2 IN1_V32            vec_t                         Input vector operand
Operands    3 IN2_gB_BASE        void *                        Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                               base pointer
                                                  31   31      32 bit immediate post modification in
            5 IN4_PM_IMM         int32          -2 ..2 -1
                                                               bytes
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rI_pm_imm_lp (mw_8w, vIn, ptrBase, ptrModify, 2);

Comments
Intrinsic   vstw_v32_indexed_rI_pm_ptr_lp
name
Spec        vstw {mw [,lp|hp][,concat]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and number
                                 MW_options
            1 MW
                                 enum                          of stored elements (see enum definition
                                                               at vec-mem-modes.h)
            2 IN1_V32            vec_t                         Input vector operand
Operands    3 IN2_gB_BASE        void *                        Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                               base pointer
            5 IN4_PM_PTR         void*                         Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rI_pm_ptr_lp (mw_8w, vIn, ptrBase, ptrModify, ptr);

Comments

Intrinsic   vstw_v32_indexed_rIp_lp
name
Spec        vstw {mw [,lp|hp][,concat]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and number
                                 MW_options
            1 MW
                                 enum                          of stored elements (see enum definition
                                                               at vec-mem-modes.h)
            2 IN1_V32            vec_t                         Input vector operand
Operands    3 IN2_gB_BASE        void *                        Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                               base pointer
            5 IN3_PART           uint8          LOW,HIGH       Word part which is used for operand 4
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rIp_lp (mw_8w, vIn, ptrBase, ptrModify, LOW);

Comments



Intrinsic   vstw_v32_indexed_rIp_pm_imm_lp
name
Spec        vstw {mw [,lp|hp][,concat]} vix[0], (gB+rIp)[+pm] [,?prSC]
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
            5 IN3_PART          uint8          LOW,HIGH      Word part which is used for operand 4
                                                 31   31     32 bit immediate post modification in
            6 IN4_PM_IMM        int32          -2 ..2 -1
                                                             bytes
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...

vstw_v32_indexed_rIp_pm_imm_lp (mw_8w, vIn, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic   vstw_v32_indexed_rIp_pm_ptr_lp
name
Spec        vstw {mw [,lp|hp][,concat]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                MW_options                   Determines the element size and number
Operands    1 MW
                                enum                         of stored elements (see enum definition
                                                                at vec-mem-modes.h)
              2 IN1_V32           vec_t                         Input vector operand
              3 IN2_gB_BASE       void *                        Pointer register (gB)
                                                                Pointer (rI) specifying the offset from the
              4 IN3_rI_OFFSET void *
                                                                base pointer
              5 IN3_PART          uint8          LOW,HIGH       Word part which is used for operand 4
              6 IN4_PM_PTR        void*                         Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec_t vIn;
              ...
              vstw_v32_indexed_rIp_pm_ptr_lp (mw_8w, vIn, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic     vstw_v32_lp
name
Spec syntax   vstw {mw [,lp|hp][,concat]} vix[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                               Determines the element size and number
                                 MW_options
              1   MW
                                 enum                          of stored elements (see enum definition at
                                                               vec-mem-modes.h)
Operands
              2   IN1_V32        vec_t                         Input vector operand
              3   IN2_PTR        void *                        Pointer register (rN)
              void* ptr;
              vec_t vIn;
C example     ...
              vstw_v32_lp (mw_8w, vIn, ptr);

Comments



Intrinsic     vstw_v32_pm_imm_lp
name
Spec          vstw {mw [,lp|hp][,concat]} vix[0], (pN)+#imm32_6 [,?prSC]
syntax
Return        void
type
                                                             Determines the element size and number
                                 MW_options
              1   MW

enum                        of stored elements (see enum definition at
                                                             vec-mem-modes.h)

Operands      2   IN1_V32        vec_t                       Input vector operand
              3   IN2_PTR        void *                      Pointer register (rN)
                                                  31   31    32 bit immediate post modification in
              4   IN3_IMM32_6 int32             -2 ..2 -1
                                                             bytes
              void* ptr;
              vec_t vIn;
C example     ...
              vstw_v32_pm_imm_lp (mw_8w, vIn, ptr, 2);

Comments



Intrinsic     vstw_v32_pm_ptr_lp
name
Spec          vstw {mw [,lp|hp][,concat]} vix[0], (pN)[+pm_x] [,?prSC]
syntax
Return        void
type
                                                             Determines the element size and number
                                 MW_options
              1   MW
                                 enum                        of stored elements (see enum definition at
                                                             vec-mem-modes.h)
Operands      2   IN1_V32        vec_t                       Input vector operand
              3   IN2_PTR        void *                      Pointer register (rN)
              4   IN3_PM_PTR void*                           Pointer register (rN)
              void* ptr;
              vec_t vIn;
C example     ...
              vstw_v32_pm_ptr_lp (mw_8w, vIn, ptr, ptr);

Comments


Main table → Memory Access → Store → Store 16 bit
Available addressing modes
Intrinsic Names:
vstw_v32_direct_lp_concat
vstw_v32_indexed_imm_lp_concat
vstw_v32_indexed_rI_lp_concat
vstw_v32_indexed_rI_pm_imm_lp_concat
vstw_v32_indexed_rI_pm_ptr_lp_concat
vstw_v32_indexed_rIp_lp_concat
vstw_v32_indexed_rIp_pm_imm_lp_concat
vstw_v32_indexed_rIp_pm_ptr_lp_concat
vstw_v32_lp_concat
vstw_v32_pm_imm_lp_concat
vstw_v32_pm_ptr_lp_concat
Intrinsic     vstw_v32_direct_lp_concat
name
Spec syntax   vstw {mw [,lp|hp][,concat]} vix[0], [#address] [,?prSC]

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
              vstw_v32_direct_lp_concat (mw_8w, vIn, 2);

Comments



Intrinsic     vstw_v32_indexed_imm_lp_concat
name
Spec          vstw {mw [,lp|hp][,concat]} vix[0], (gB+#imm16_6) [,?prSC]
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
              vstw_v32_indexed_imm_lp_concat (mw_8w, vIn, ptrBase, 2);

Comments



Intrinsic     vstw_v32_indexed_rI_lp_concat
name
Spec          vstw {mw [,lp|hp][,concat]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 MW_options
            1 MW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)

Operands    2 IN1_V32            vec_t                        Input vector operand
            3 IN2_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                              base pointer
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rI_lp_concat (mw_8w, vIn, ptrBase, ptrModify);

Comments



Intrinsic   vstw_v32_indexed_rI_pm_imm_lp_concat

name
Spec        vstw {mw [,lp|hp][,concat]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 MW_options
            1 MW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_V32            vec_t                        Input vector operand
Operands    3 IN2_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                              base pointer
                                                  31   31     32 bit immediate post modification in
            5 IN4_PM_IMM         int32          -2 ..2 -1
                                                              bytes
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rI_pm_imm_lp_concat (mw_8w, vIn, ptrBase, ptrModify, 2);

Comments
Intrinsic   vstw_v32_indexed_rI_pm_ptr_lp_concat
name
Spec        vstw {mw [,lp|hp][,concat]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 MW_options
            1 MW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_V32            vec_t                        Input vector operand
Operands    3 IN2_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                              base pointer
            5 IN4_PM_PTR         void*                        Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rI_pm_ptr_lp_concat (mw_8w, vIn, ptrBase, ptrModify, ptr);

Comments



Intrinsic   vstw_v32_indexed_rIp_lp_concat
name

Spec        vstw {mw [,lp|hp][,concat]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 MW_options
            1 MW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_V32            vec_t                        Input vector operand
Operands    3 IN2_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                              base pointer
            5 IN3_PART           uint8          LOW,HIGH      Word part which is used for operand 4
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstw_v32_indexed_rIp_lp_concat (mw_8w, vIn, ptrBase, ptrModify, LOW);

Comments



Intrinsic   vstw_v32_indexed_rIp_pm_imm_lp_concat
name
Spec        vstw {mw [,lp|hp][,concat]} vix[0], (gB+rIp)[+pm] [,?prSC]
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
            5 IN3_PART          uint8          LOW,HIGH      Word part which is used for operand 4
                                                 31   31     32 bit immediate post modification in
            6 IN4_PM_IMM        int32          -2 ..2 -1
                                                             bytes
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...

vstw_v32_indexed_rIp_pm_imm_lp_concat (mw_8w, vIn, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic   vstw_v32_indexed_rIp_pm_ptr_lp_concat
name
Spec        vstw {mw [,lp|hp][,concat]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                MW_options                   Determines the element size and number
Operands    1 MW
                                enum                         of stored elements (see enum definition
                                                                at vec-mem-modes.h)
              2 IN1_V32           vec_t                         Input vector operand
              3 IN2_gB_BASE       void *                        Pointer register (gB)
                                                                Pointer (rI) specifying the offset from the
              4 IN3_rI_OFFSET void *
                                                                base pointer
              5 IN3_PART          uint8          LOW,HIGH       Word part which is used for operand 4
              6 IN4_PM_PTR        void*                         Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec_t vIn;
              ...
              vstw_v32_indexed_rIp_pm_ptr_lp_concat (mw_8w, vIn, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic     vstw_v32_lp_concat
name
Spec syntax   vstw {mw [,lp|hp][,concat]} vix[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                               Determines the element size and number
                                 MW_options
              1   MW
                                 enum                          of stored elements (see enum definition at
                                                               vec-mem-modes.h)
Operands
              2   IN1_V32        vec_t                         Input vector operand
              3   IN2_PTR        void *                        Pointer register (rN)
              void* ptr;
              vec_t vIn;
C example     ...
              vstw_v32_lp_concat (mw_8w, vIn, ptr);

Comments



Intrinsic     vstw_v32_pm_imm_lp_concat
name
Spec          vstw {mw [,lp|hp][,concat]} vix[0], (pN)+#imm32_6 [,?prSC]
syntax
Return        void
type
                                                                Determines the element size and number
                               MW_options
            1   MW

enum                             of stored elements (see enum definition at
                                                                vec-mem-modes.h)

Operands    2   IN1_V32        vec_t                            Input vector operand
            3   IN2_PTR        void *                           Pointer register (rN)
                                                31   31         32 bit immediate post modification in
            4   IN3_IMM32_6 int32             -2 ..2 -1
                                                                bytes
            void* ptr;
            vec_t vIn;
C example   ...
            vstw_v32_pm_imm_lp_concat (mw_8w, vIn, ptr, 2);

Comments



Intrinsic   vstw_v32_pm_ptr_lp_concat
name
Spec        vstw {mw [,lp|hp][,concat]} vix[0], (pN)[+pm_x] [,?prSC]
syntax
Return      void
type
                                                                Determines the element size and number
                               MW_options
            1   MW
                               enum                             of stored elements (see enum definition at
                                                                vec-mem-modes.h)
Operands    2   IN1_V32        vec_t                            Input vector operand
            3   IN2_PTR        void *                           Pointer register (rN)
            4   IN3_PM_PTR void*                                Pointer register (rN)
            void* ptr;
            vec_t vIn;
C example   ...
            vstw_v32_pm_ptr_lp_concat (mw_8w, vIn, ptr, ptr);

Comments


Main table → Memory Access → Store → Store 16 bit
Available addressing modes
Intrinsic Names:
vstw_v40_direct_pw
vstw_v40_indexed_imm_pw
vstw_v40_indexed_rI_pm_imm_pw
vstw_v40_indexed_rI_pm_ptr_pw
vstw_v40_indexed_rI_pw
vstw_v40_indexed_rIp_pm_imm_pw
vstw_v40_indexed_rIp_pm_ptr_pw
vstw_v40_indexed_rIp_pw
vstw_v40_pm_imm_pw
vstw_v40_pm_ptr_pw
vstw_v40_pw
Intrinsic     vstw_v40_direct_pw
name
Spec syntax   vstw {pw} vox[0], [#address] [,?prSC]

Return        void
type
                                                               Determines the element size and number
                                PW_options
              1      PW
                                enum                           of stored elements (see enum definition at
                                                               vec-mem-modes.h)
Operands
              2      IN1_V40    vec40_t                        Output vector operand

32
              3      IN2_ADDR   int32          0..2 -1         32 bit address
              vec40_t vIn;
C example     ...
              vstw_v40_direct_pw (pw_16w, vIn, 2);

Comments



Intrinsic     vstw_v40_indexed_imm_pw
name
Spec          vstw {pw} vox[0], (gB+#imm16_6) [,?prSC]
syntax
Return        void
type
                                                               Determines the element size and number
                                 PW_options
              1   PW
                                 enum                          of stored elements (see enum definition
                                                               at vec-mem-modes.h)

Operands      2   IN1_V40        vec40_t                       Output vector operand
              3   IN2_gB_BASE void *                           Pointer register (gB)

              4
                                                -              16 bit immediate post modification in
                  IN3_IMM16_6    int16
                                                32768..32767   bytes
              void* ptrBase;
              vec40_t vIn;
C example     ...
              vstw_v40_indexed_imm_pw (pw_16w, vIn, ptrBase, 2);

Comments



Intrinsic     vstw_v40_indexed_rI_pm_imm_pw
name
Spec          vstw {pw} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 PW_options
            1 PW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_V40            vec40_t                      Output vector operand
Operands    3 IN2_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                              base pointer
                                                 31   31      32 bit immediate post modification in
            5 IN4_PM_IMM         int32         -2 ..2 -1
                                                              bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rI_pm_imm_pw (pw_16w, vIn, ptrBase, ptrModify, 2);

Comments

Intrinsic   vstw_v40_indexed_rI_pm_ptr_pw
name
Spec        vstw {pw} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 PW_options
            1 PW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_V40            vec40_t                      Output vector operand
Operands    3 IN2_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                              base pointer
            5 IN4_PM_PTR         void*                        Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rI_pm_ptr_pw (pw_16w, vIn, ptrBase, ptrModify, ptr);
Comments



Intrinsic   vstw_v40_indexed_rI_pw
name
Spec        vstw {pw} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 PW_options
            1 PW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)

Operands    2 IN1_V40            vec40_t                      Output vector operand
            3 IN2_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                              base pointer
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rI_pw (pw_16w, vIn, ptrBase, ptrModify);

Comments



Intrinsic   vstw_v40_indexed_rIp_pm_imm_pw
name
Spec        vstw {pw} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 PW_options
            1 PW

enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_V40            vec40_t                      Output vector operand
Operands    3 IN2_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                              base pointer
            5 IN3_PART           uint8         LOW,HIGH       Word part which is used for operand 4
                                                 31   31     32 bit immediate post modification in
            6 IN4_PM_IMM        int32          -2 ..2 -1
                                                             bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rIp_pm_imm_pw (pw_16w, vIn, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic   vstw_v40_indexed_rIp_pm_ptr_pw
name
Spec        vstw {pw} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                PW_options
            1 PW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
            2 IN1_V40           vec40_t                      Output vector operand

Operands    3 IN2_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            4 IN3_rI_OFFSET void *
                                                             base pointer
            5 IN3_PART          uint8          LOW,HIGH      Word part which is used for operand 4
            6 IN4_PM_PTR        void*                        Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstw_v40_indexed_rIp_pm_ptr_pw (pw_16w, vIn, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic   vstw_v40_indexed_rIp_pw
name
Spec        vstw {pw} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type

Determines the element size and number
                                PW_options
            1 PW
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
            vstw_v40_indexed_rIp_pw (pw_16w, vIn, ptrBase, ptrModify, LOW);

Comments



Intrinsic   vstw_v40_pm_imm_pw
name
Spec        vstw {pw} vox[0], (pN)+#imm32_6 [,?prSC]
syntax
Return      void
type
                                                            Determines the element size and number
                               PW_options
            1   PW
                               enum                         of stored elements (see enum definition at
                                                            vec-mem-modes.h)

Operands    2   IN1_V40        vec40_t                      Output vector operand
            3   IN2_PTR        void *                       Pointer register (rN)
                                               31   31      32 bit immediate post modification in
            4   IN3_IMM32_6 int32            -2 ..2 -1
                                                            bytes
            void* ptr;
            vec40_t vIn;
C example   ...
            vstw_v40_pm_imm_pw (pw_16w, vIn, ptr, 2);

Comments



Intrinsic   vstw_v40_pm_ptr_pw
name
Spec        vstw {pw} vox[0], (pN)[+pm_x] [,?prSC]
syntax
Return        void
type
                                                            Determines the element size and number
                                 PW_options
              1   PW
                                 enum                       of stored elements (see enum definition at
                                                            vec-mem-modes.h)
Operands      2   IN1_V40        vec40_t                    Output vector operand

3   IN2_PTR        void *                     Pointer register (rN)
              4   IN3_PM_PTR void*                          Pointer register (rN)
              void* ptr;
              vec40_t vIn;
C example     ...
              vstw_v40_pm_ptr_pw (pw_16w, vIn, ptr, ptr);

Comments



Intrinsic     vstw_v40_pw
name
Spec syntax   vstw {pw} vox[0], (pN)[+pm_x] [,?prSC]

Return        void
type
                                                            Determines the element size and number
                                 PW_options
              1   PW
                                 enum                       of stored elements (see enum definition at
                                                            vec-mem-modes.h)
Operands
              2   IN1_V40        vec40_t                    Output vector operand
              3   IN2_PTR        void *                     Pointer register (rN)
              void* ptr;
              vec40_t vIn;
C example     ...
              vstw_v40_pw (pw_16w, vIn, ptr);

Comments


Main table → Memory Access → Store → Store 16 bit
