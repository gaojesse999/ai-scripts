# Memory Access → Load → Load DW into 32 bit register

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Memory Access → Load → Load DW into 32 bit register

Load DW into 32 bit register

Load DW into 32 bit register
Load 32 bit double word
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
vlddw_v32
vlddw_v32_rowstr
vlddw_v32_clone
vlddw_v32_clone_rowstr
vlddw_v32_8dw_intrlv
vlddw_v32_8dw_intrlv_int2dw
vlddw_v32_8dw_intrlv_int2dw_rowstr
vlddw_v32_8dw_intrlv_rowstr
vlddw_v32_clone_8dw_intrlv
vlddw_v32_clone_8dw_intrlv_int2dw
vlddw_v32_clone_8dw_intrlv_int2dw_rowstr
vlddw_v32_clone_8dw_intrlv_rowstr
vlddw_v32_vuX
Instruction details in the instruction set specification
Available addressing modes
Intrinsic Names:
vlddw_direct_v32
vlddw_indexed_imm_v32
vlddw_indexed_rI_pm_imm_v32
vlddw_indexed_rI_pm_ptr_v32
vlddw_indexed_rI_v32
vlddw_indexed_rIp_pm_imm_v32
vlddw_indexed_rIp_pm_ptr_v32
vlddw_indexed_rIp_v32
vlddw_pm_imm_v32
vlddw_pm_ptr_v32
vlddw_v32
Intrinsic   vlddw_direct_v32
name
Spec        vlddw {mdw [,strX]} [#address], viz[Z] [,?prSC]
syntax
Return      vec_t
type
                                                              Determines the element size and number
                             MDW_options
            1   MDW
                             enum                             of loaded elements (see enum definition
                                                              at vec-mem-modes.h)
Operands                                             32
            2   IN1_ADDR     int32            0..2 -1         32 bit address
                                                              Offset for the first DW used from the
            3   OUT_OFST uint8                0..7
                                                              result operand
            vec_t vRes;
C example   ...
            vRes = vlddw_direct_v32 (mdw_8dw, 2, 0);

Comments



Intrinsic   vlddw_indexed_imm_v32
name
Spec        vlddw {mdw[,strX][,rowstr]} (gB+#imm16_6), viz[Z] [,?prSC]
syntax
Return      vec_t
type
                                                               Determines the element size and number
                               MDW_options
            1 MDW
                               enum                            of loaded elements (see enum definition

at vec-mem-modes.h)
            2 IN1_gB_BASE void *                               Pointer register (gB)
Operands
                                               -               16 bit immediate post modification in
            3 IN2_IMM16_6      int16
                                               32768..32767    bytes

            4 OUT_OFST
                                                               Offset for the first DW used from the
                               uint8           0..7
                                                               result operand
            void* ptrBase;
            vec_t vRes;
C example   ...
            vRes = vlddw_indexed_imm_v32 (mdw_8dw, ptrBase, 2, 0);

Comments
Intrinsic   vlddw_indexed_rI_pm_imm_v32
name
Spec        vlddw {mdw [,strX][,rowstr]} (gB+rI)[+pm], viz[Z] [,?prSC]
syntax
Return      vec_t
type
                                                              Determines the element size and number
                                MDW_options
            1 MDW
                                enum                          of loaded elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_gB_BASE       void *                        Pointer register (gB)
                                                              Pointer (rI) specifying the offset from
Operands    3 IN2_rI_OFFSET void *
                                                              the base pointer
                                                  31   31     32 bit immediate post modification in
            4 IN3_PM_IMM        int32           -2 ..2 -1
                                                              bytes
                                                              Offset for the first DW used from the
            5 OUT_OFST          uint8           0..7
                                                              result operand
            void* ptrBase;
            void* ptrModify;
C example   vec_t vRes;
            ...
            vRes = vlddw_indexed_rI_pm_imm_v32 (mdw_8dw, ptrBase, ptrModify, 2, 0);

Comments



Intrinsic   vlddw_indexed_rI_pm_ptr_v32
name
Spec        vlddw {mdw [,strX][,rowstr]} (gB+rI)[+pm], viz[Z] [,?prSC]
syntax
Return      vec_t
type
                                                              Determines the element size and number
                                MDW_options
            1 MDW

enum                          of loaded elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_gB_BASE       void *                        Pointer register (gB)
Operands                                                      Pointer (rI) specifying the offset from
            3 IN2_rI_OFFSET void *
                                                              the base pointer
            4 IN3_PM_PTR        void*                         Pointer register (rN)

            5 OUT_OFST
                                                              Offset for the first DW used from the
                                uint8           0..7
                                                              result operand
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec_t vRes;
            ...
            vRes = vlddw_indexed_rI_pm_ptr_v32 (mdw_8dw, ptrBase, ptrModify, ptr, 0);

Comments



Intrinsic   vlddw_indexed_rI_v32
name
Spec        vlddw {mdw [,strX][,rowstr]} (gB+rI)[+pm], viz[Z] [,?prSC]
syntax
Return      vec_t
type
                                                               Determines the element size and number
                                MDW_options
            1 MDW
                                enum                           of loaded elements (see enum definition
                                                               at vec-mem-modes.h)
            2 IN1_gB_BASE       void *                         Pointer register (gB)
Operands
                                                               Pointer (rI) specifying the offset from
            3 IN2_rI_OFFSET void *
                                                               the base pointer
                                                               Offset for the first DW used from the
            4 OUT_OFST          uint8            0..7
                                                               result operand
            void* ptrBase;
            void* ptrModify;
C example   vec_t vRes;
            ...
            vRes = vlddw_indexed_rI_v32 (mdw_8dw, ptrBase, ptrModify, 0);

Comments



Intrinsic   vlddw_indexed_rIp_pm_imm_v32
name
Spec        vlddw {mdw [,strX][,rowstr]} (gB+rIp)[+pm], viz[Z] [,?prSC]
syntax
Return      vec_t
type
                                                               Determines the element size and number

MDW_options
            1 MDW
                                enum                           of loaded elements (see enum definition
Operands                                                       at vec-mem-modes.h)
            2 IN1_gB_BASE       void *                         Pointer register (gB)
                                                              Pointer (rI) specifying the offset from
            3 IN2_rI_OFFSET void *
                                                              the base pointer
            4 IN2_PART          uint8           LOW,HIGH      Word part which is used for operand 3

            5 IN3_PM_IMM                          31   31     32 bit immediate post modification in
                                int32           -2 ..2 -1
                                                              bytes
                                                              Offset for the first DW used from the
            6 OUT_OFST          uint8           0..7
                                                              result operand
            void* ptrBase;
            void* ptrModify;
C example   vec_t vRes;
            ...
            vRes = vlddw_indexed_rIp_pm_imm_v32 (mdw_8dw, ptrBase, ptrModify, LOW, 2, 0);

Comments



Intrinsic   vlddw_indexed_rIp_pm_ptr_v32
name
Spec        vlddw {mdw [,strX][,rowstr]} (gB+rIp)[+pm], viz[Z] [,?prSC]
syntax
Return      vec_t
type
                                                              Determines the element size and number
                                MDW_options
            1 MDW
                                enum                          of loaded elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_gB_BASE       void *                        Pointer register (gB)
                                                              Pointer (rI) specifying the offset from
            3 IN2_rI_OFFSET void *
Operands                                                      the base pointer
            4 IN2_PART          uint8           LOW,HIGH      Word part which is used for operand 3
            5 IN3_PM_PTR        void*                         Pointer register (rN)
                                                              Offset for the first DW used from the
            6 OUT_OFST          uint8           0..7
                                                              result operand

void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec_t vRes;
            ...
            vRes = vlddw_indexed_rIp_pm_ptr_v32 (mdw_8dw, ptrBase, ptrModify, LOW, ptr, 0);

Comments
Intrinsic   vlddw_indexed_rIp_v32
name
Spec        vlddw {mdw [,strX][,rowstr]} (gB+rIp)[+pm], viz[Z] [,?prSC]
syntax
Return      vec_t
type
                                                              Determines the element size and number
                                MDW_options
            1 MDW
                                enum                          of loaded elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_gB_BASE       void *                        Pointer register (gB)
Operands                                                      Pointer (rI) specifying the offset from
            3 IN2_rI_OFFSET void *
                                                              the base pointer
            4 IN2_PART          uint8           LOW,HIGH      Word part which is used for operand 3
                                                              Offset for the first DW used from the
            5 OUT_OFST          uint8           0..7
                                                              result operand
            void* ptrBase;
            void* ptrModify;
C example   vec_t vRes;
            ...
            vRes = vlddw_indexed_rIp_v32 (mdw_8dw, ptrBase, ptrModify, LOW, 0);

Comments



Intrinsic   vlddw_pm_imm_v32
name
Spec        vlddw {mdw [,strX][,rowstr]} (pN)+#imm32_6, viz[Z] [,?prSC]
syntax
Return      vec_t
type
                                                             Determines the element size and number
                               MDW_options
            1 MDW
                               enum                          of loaded elements (see enum definition
                                                             at vec-mem-modes.h)
            2 IN1_PTR          void *                        Pointer register (rN)
Operands
                                                 31    31    32 bit immediate post modification in
            3 IN2_IMM32_6 int32                -2 ..2 -1
                                                             bytes
                                                             Offset for the first DW used from the
            4 OUT_OFST         uint8           0..7

result operand
            void* ptr;
C example   vec_t vRes;
            ...
            vRes = vlddw_pm_imm_v32 (mdw_8dw, ptr, 2, 0);

Comments



Intrinsic   vlddw_pm_ptr_v32
name
Spec        vlddw {mdw [,strX][,rowstr]} (pN)[+pm_x], viz[Z] [,?prSC]
syntax
Return      vec_t
type
                                                              Determines the element size and number
                              MDW_options
            1 MDW
                              enum                            of loaded elements (see enum definition
                                                              at vec-mem-modes.h)

Operands    2 IN1_PTR         void *                          Pointer register (rN)
            3 IN2_PM_PTR void*                                Pointer register (rN)
                                                              Offset for the first DW used from the
            4 OUT_OFST        uint8            0..7
                                                              result operand
            void* ptr;
            void* vRes;
C example   ...
            ptr = vlddw_pm_ptr_v32 (mdw_8dw, ptr, vRes, 0);

Comments



Intrinsic   vlddw_v32
name
Spec        vlddw {mdw [,strX][,rowstr]} (pN)[+pm_x], viz[Z] [,?prSC]
syntax
Return      vec_t
type
                                                              Determines the element size and number
                              MDW_options
            1   MDW
                              enum                            of loaded elements (see enum definition
                                                              at vec-mem-modes.h)
Operands    2   IN1_PTR       void *                          Pointer register (rN)
                                                              Offset for the first DW used from the
            3   OUT_OFST uint8                0..7
                                                              result operand
            void* ptr;
C example   vec_t vRes;
            ...
              vRes = vlddw_v32 (mdw_8dw, ptr, 0);

Comments


Main table → Memory Access → Load → Load DW into 32 bit register
Available addressing modes
Intrinsic Names:
vlddw_indexed_imm_v32_rowstr
vlddw_indexed_rI_pm_imm_v32_rowstr
vlddw_indexed_rI_pm_ptr_v32_rowstr
vlddw_indexed_rI_v32_rowstr
vlddw_indexed_rIp_pm_imm_v32_rowstr
vlddw_indexed_rIp_pm_ptr_v32_rowstr
vlddw_indexed_rIp_v32_rowstr
vlddw_pm_imm_v32_rowstr
vlddw_pm_ptr_v32_rowstr
vlddw_v32_rowstr

Intrinsic   vlddw_indexed_imm_v32_rowstr
name
Spec        vlddw {mdw[,strX][,rowstr]} (gB+#imm16_6), viz[Z] [,?prSC]
syntax
Return      vec_t
type
                                                              Determines the element size and number
                               MDW_options
            1 MDW
                               enum                           of loaded elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_gB_BASE void *                              Pointer register (gB)
Operands
                                               -              16 bit immediate post modification in
            3 IN2_IMM16_6      int16
                                               32768..32767   bytes
                                                              Offset for the first DW used from the
            4 OUT_OFST         uint8           0..7
                                                              result operand
            void* ptrBase;
            vec_t vRes;
C example   ...
            vRes = vlddw_indexed_imm_v32_rowstr (mdw_8dw, ptrBase, 2, 0);

Comments



Intrinsic   vlddw_indexed_rI_pm_imm_v32_rowstr
name
Spec        vlddw {mdw [,strX][,rowstr]} (gB+rI)[+pm], viz[Z] [,?prSC]
syntax
Return      vec_t
type
                                                              Determines the element size and number
                                MDW_options
            1 MDW
                                enum                          of loaded elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_gB_BASE       void *                        Pointer register (gB)
                                                              Pointer (rI) specifying the offset from
Operands    3 IN2_rI_OFFSET void *
                                                              the base pointer

            4 IN3_PM_IMM                         31   31      32 bit immediate post modification in
                                int32          -2 ..2 -1
                                                              bytes
                                                              Offset for the first DW used from the
            5 OUT_OFST          uint8          0..7
                                                              result operand
            void* ptrBase;
C example   void* ptrModify;

vec_t vRes;
            ...
            vRes = vlddw_indexed_rI_pm_imm_v32_rowstr (mdw_8dw, ptrBase, ptrModify, 2, 0);

Comments



Intrinsic   vlddw_indexed_rI_pm_ptr_v32_rowstr
name
Spec        vlddw {mdw [,strX][,rowstr]} (gB+rI)[+pm], viz[Z] [,?prSC]
syntax
Return      vec_t
type
                                                               Determines the element size and number
                                MDW_options
            1 MDW
                                enum                           of loaded elements (see enum definition
                                                               at vec-mem-modes.h)
            2 IN1_gB_BASE       void *                         Pointer register (gB)
Operands                                                       Pointer (rI) specifying the offset from
            3 IN2_rI_OFFSET void *
                                                               the base pointer
            4 IN3_PM_PTR        void*                          Pointer register (rN)
                                                               Offset for the first DW used from the
            5 OUT_OFST          uint8            0..7
                                                               result operand
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec_t vRes;
            ...
            vRes = vlddw_indexed_rI_pm_ptr_v32_rowstr (mdw_8dw, ptrBase, ptrModify, ptr, 0);

Comments



Intrinsic   vlddw_indexed_rI_v32_rowstr
name
Spec        vlddw {mdw [,strX][,rowstr]} (gB+rI)[+pm], viz[Z] [,?prSC]
syntax
Return      vec_t
type
                                                               Determines the element size and number
                                MDW_options
            1 MDW
                                enum                           of loaded elements (see enum definition
Operands                                                       at vec-mem-modes.h)
            2 IN1_gB_BASE       void *                         Pointer register (gB)
                                                               Pointer (rI) specifying the offset from
            3 IN2_rI_OFFSET void *
                                                               the base pointer
                                                               Offset for the first DW used from the
            4 OUT_OFST          uint8            0..7

result operand
            void* ptrBase;
            void* ptrModify;
C example   vec_t vRes;
            ...
            vRes = vlddw_indexed_rI_v32_rowstr (mdw_8dw, ptrBase, ptrModify, 0);

Comments



Intrinsic   vlddw_indexed_rIp_pm_imm_v32_rowstr
name
Spec        vlddw {mdw [,strX][,rowstr]} (gB+rIp)[+pm], viz[Z] [,?prSC]
syntax
Return      vec_t
type
                                                               Determines the element size and number
                                MDW_options
            1 MDW
                                enum                           of loaded elements (see enum definition
                                                               at vec-mem-modes.h)
            2 IN1_gB_BASE       void *                         Pointer register (gB)
                                                               Pointer (rI) specifying the offset from
            3 IN2_rI_OFFSET void *
Operands                                                       the base pointer
            4 IN2_PART          uint8            LOW,HIGH      Word part which is used for operand 3
                                                   31   31     32 bit immediate post modification in
            5 IN3_PM_IMM        int32            -2 ..2 -1
                                                               bytes
                                                               Offset for the first DW used from the
            6 OUT_OFST          uint8            0..7
                                                               result operand
            void* ptrBase;
            void* ptrModify;
C example   vec_t vRes;
            ...
            vRes = vlddw_indexed_rIp_pm_imm_v32_rowstr (mdw_8dw, ptrBase, ptrModify, LOW, 2, 0);

Comments



Intrinsic   vlddw_indexed_rIp_pm_ptr_v32_rowstr
name
Spec        vlddw {mdw [,strX][,rowstr]} (gB+rIp)[+pm], viz[Z] [,?prSC]
syntax
Return      vec_t
type
                                                              Determines the element size and number
                                MDW_options
            1 MDW
                                enum                          of loaded elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_gB_BASE       void *                        Pointer register (gB)
                                                              Pointer (rI) specifying the offset from

3 IN2_rI_OFFSET void *
Operands                                                      the base pointer
            4 IN2_PART          uint8           LOW,HIGH      Word part which is used for operand 3
            5 IN3_PM_PTR        void*                         Pointer register (rN)
                                                              Offset for the first DW used from the
            6 OUT_OFST          uint8           0..7
                                                              result operand
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec_t vRes;
            ...
            vRes = vlddw_indexed_rIp_pm_ptr_v32_rowstr (mdw_8dw, ptrBase, ptrModify, LOW, ptr, 0);

Comments



Intrinsic   vlddw_indexed_rIp_v32_rowstr
name
Spec        vlddw {mdw [,strX][,rowstr]} (gB+rIp)[+pm], viz[Z] [,?prSC]
syntax
Return      vec_t
type
                                                              Determines the element size and number
                                MDW_options
            1 MDW
                                enum                          of loaded elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_gB_BASE       void *                        Pointer register (gB)
Operands                                                      Pointer (rI) specifying the offset from
            3 IN2_rI_OFFSET void *
                                                              the base pointer
            4 IN2_PART          uint8           LOW,HIGH      Word part which is used for operand 3

            5 OUT_OFST
                                                              Offset for the first DW used from the
                                uint8           0..7
                                                              result operand
            void* ptrBase;
C example   void* ptrModify;
            vec_t vRes;
            ...
            vRes = vlddw_indexed_rIp_v32_rowstr (mdw_8dw, ptrBase, ptrModify, LOW, 0);

Comments



Intrinsic   vlddw_pm_imm_v32_rowstr
name
Spec        vlddw {mdw [,strX][,rowstr]} (pN)+#imm32_6, viz[Z] [,?prSC]
syntax
Return      vec_t
type
                                                             Determines the element size and number
                               MDW_options
            1 MDW
                               enum                          of loaded elements (see enum definition

at vec-mem-modes.h)
            2 IN1_PTR          void *                        Pointer register (rN)
Operands
                                                 31   31     32 bit immediate post modification in
            3 IN2_IMM32_6 int32                -2 ..2 -1
                                                             bytes

            4 OUT_OFST
                                                             Offset for the first DW used from the
                               uint8           0..7
                                                             result operand
            void* ptr;
            vec_t vRes;
C example   ...
            vRes = vlddw_pm_imm_v32_rowstr (mdw_8dw, ptr, 2, 0);

Comments



Intrinsic   vlddw_pm_ptr_v32_rowstr
name
Spec        vlddw {mdw [,strX][,rowstr]} (pN)[+pm_x], viz[Z] [,?prSC]
syntax
Return      vec_t
type
                                                             Determines the element size and number
                              MDW_options
            1 MDW
                              enum                           of loaded elements (see enum definition
                                                             at vec-mem-modes.h)
Operands    2 IN1_PTR         void *                         Pointer register (rN)
            3 IN2_PM_PTR void*                               Pointer register (rN)
            4 OUT_OFST        uint8            0..7          Offset for the first DW used from the
                                                              result operand
             void* ptr;
             void* vRes;
C example    ...
             ptr = vlddw_pm_ptr_v32_rowstr (mdw_8dw, ptr, vRes, 0);

Comments



Intrinsic    vlddw_v32_rowstr
name
Spec         vlddw {mdw [,strX][,rowstr]} (pN)[+pm_x], viz[Z] [,?prSC]
syntax
Return       vec_t
type
                                                              Determines the element size and number
                              MDW_options
             1   MDW
                              enum                            of loaded elements (see enum definition
                                                              at vec-mem-modes.h)
Operands     2   IN1_PTR      void *                          Pointer register (rN)
                                                              Offset for the first DW used from the
             3   OUT_OFST uint8                0..7
                                                              result operand

void* ptr;
             vec_t vRes;
C example    ...
             vRes = vlddw_v32_rowstr (mdw_8dw, ptr, 0);

Comments


Main table → Memory Access → Load → Load DW into 32 bit register
Available addressing modes
Intrinsic Names:
vlddw_direct_v32_clone
vlddw_indexed_imm_v32_clone
vlddw_indexed_rI_pm_imm_v32_clone
vlddw_indexed_rI_pm_ptr_v32_clone
vlddw_indexed_rI_v32_clone
vlddw_indexed_rIp_pm_imm_v32_clone
vlddw_indexed_rIp_pm_ptr_v32_clone
vlddw_indexed_rIp_v32_clone
vlddw_pm_imm_v32_clone
vlddw_pm_ptr_v32_clone
vlddw_v32_clone
Intrinsic   vlddw_direct_v32_clone
name        vlddw_direct_v32_str1

Spec        vlddw {mdw [,strX]} [#address], viz[Z] [,?prSC]
syntax
Return      vec_t
type
                                                              Determines the element size and number
                               MDW_options
            1    MDW
                               enum                           of loaded elements (see enum definition
                                                              at vec-mem-modes.h)
Operands                                             32
            2    IN1_ADDR      int32          0..2 -1         32 bit address
                                                              Offset for the first DW used from the
            3    OUT_OFST uint8               0..7
                                                              result operand
            vec_t vRes;
C example   ...
            vRes = vlddw_direct_v32_clone (mdw_8dw, 2, 0);

                 The same data will be loaded to all vector units (Unless str1 is configured
Comments    1.
                 otherwise).



Intrinsic   vlddw_indexed_imm_v32_clone
name        vlddw_indexed_imm_v32_str1

Spec        vlddw {mdw[,strX][,rowstr]} (gB+#imm16_6), viz[Z] [,?prSC]
syntax
Return      vec_t
type
                                                               Determines the element size and
                                MDW_options
            1    MDW
                                enum                           number of loaded elements (see enum
                                                               definition at vec-mem-modes.h)
            2    IN1_gB_BASE void *                            Pointer register (gB)
Operands
                                               -               16 bit immediate post modification in
            3    IN2_IMM16_6    int16
                                               32768..32767    bytes

            4

Offset for the first DW used from the
                 OUT_OFST       uint8          0..7
                                                               result operand
            void* ptrBase;
            vec_t vRes;
C example   ...
            vRes = vlddw_indexed_imm_v32_clone (mdw_8dw, ptrBase, 2, 0);

                 The same data will be loaded to all vector units (Unless str1 is configured
Comments    1.
                 otherwise).
Intrinsic   vlddw_indexed_rI_pm_imm_v32_clone
name        vlddw_indexed_rI_pm_imm_v32_str1

Spec        vlddw {mdw [,strX][,rowstr]} (gB+rI)[+pm], viz[Z] [,?prSC]
syntax
Return      vec_t
type
                                                              Determines the element size and number
                                MDW_options
            1    MDW
                                enum                          of loaded elements (see enum definition
                                                              at vec-mem-modes.h)
            2    IN1_gB_BASE    void *                        Pointer register (gB)
                                                              Pointer (rI) specifying the offset from
Operands    3    IN2_rI_OFFSET void *
                                                              the base pointer
                                                  31   31     32 bit immediate post modification in
            4    IN3_PM_IMM     int32           -2 ..2 -1
                                                              bytes
                                                              Offset for the first DW used from the
            5    OUT_OFST       uint8           0..7
                                                              result operand
            void* ptrBase;
            void* ptrModify;
C example   vec_t vRes;
            ...
            vRes = vlddw_indexed_rI_pm_imm_v32_clone (mdw_8dw, ptrBase, ptrModify, 2, 0);

                 The same data will be loaded to all vector units (Unless str1 is configured
Comments    1.
                 otherwise).



Intrinsic   vlddw_indexed_rI_pm_ptr_v32_clone
name        vlddw_indexed_rI_pm_ptr_v32_str1

Spec        vlddw {mdw [,strX][,rowstr]} (gB+rI)[+pm], viz[Z] [,?prSC]
syntax
Return      vec_t
type
                                                              Determines the element size and number
                                MDW_options
            1    MDW

enum                          of loaded elements (see enum definition
                                                              at vec-mem-modes.h)
Operands    2    IN1_gB_BASE    void *                        Pointer register (gB)
                                                              Pointer (rI) specifying the offset from
            3    IN2_rI_OFFSET void *
                                                              the base pointer
            4    IN3_PM_PTR      void*                         Pointer register (rN)
                                                               Offset for the first DW used from the
            5    OUT_OFST        uint8           0..7
                                                               result operand
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec_t vRes;
            ...
            vRes = vlddw_indexed_rI_pm_ptr_v32_clone (mdw_8dw, ptrBase, ptrModify, ptr, 0);

                 The same data will be loaded to all vector units (Unless str1 is configured
Comments    1.
                 otherwise).



Intrinsic   vlddw_indexed_rI_v32_clone
name        vlddw_indexed_rI_v32_str1

Spec        vlddw {mdw [,strX][,rowstr]} (gB+rI)[+pm], viz[Z] [,?prSC]
syntax
Return      vec_t
type
                                                               Determines the element size and number
                                 MDW_options
            1    MDW
                                 enum                          of loaded elements (see enum definition
                                                               at vec-mem-modes.h)
            2    IN1_gB_BASE     void *                        Pointer register (gB)
Operands
                                                               Pointer (rI) specifying the offset from
            3    IN2_rI_OFFSET void *
                                                               the base pointer
                                                               Offset for the first DW used from the
            4    OUT_OFST        uint8           0..7
                                                               result operand
            void* ptrBase;
            void* ptrModify;
C example   vec_t vRes;
            ...
            vRes = vlddw_indexed_rI_v32_clone (mdw_8dw, ptrBase, ptrModify, 0);

                 The same data will be loaded to all vector units (Unless str1 is configured
Comments    1.

otherwise).



Intrinsic   vlddw_indexed_rIp_pm_imm_v32_clone
name        vlddw_indexed_rIp_pm_imm_v32_str1

Spec        vlddw {mdw [,strX][,rowstr]} (gB+rIp)[+pm], viz[Z] [,?prSC]
syntax
Return      vec_t
type
                                                             Determines the element size and number
                                MDW_options
            1    MDW
                                enum                         of loaded elements (see enum definition
                                                             at vec-mem-modes.h)
            2    IN1_gB_BASE    void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from
            3    IN2_rI_OFFSET void *
Operands                                                     the base pointer
            4    IN2_PART       uint8           LOW,HIGH     Word part which is used for operand 3
                                                  31   31    32 bit immediate post modification in
            5    IN3_PM_IMM     int32           -2 ..2 -1
                                                             bytes
                                                             Offset for the first DW used from the
            6    OUT_OFST       uint8           0..7
                                                             result operand
            void* ptrBase;
            void* ptrModify;
C example   vec_t vRes;
            ...
            vRes = vlddw_indexed_rIp_pm_imm_v32_clone (mdw_8dw, ptrBase, ptrModify, LOW, 2, 0);

                 The same data will be loaded to all vector units (Unless str1 is configured
Comments    1.
                 otherwise).



Intrinsic   vlddw_indexed_rIp_pm_ptr_v32_clone
name        vlddw_indexed_rIp_pm_ptr_v32_str1

Spec        vlddw {mdw [,strX][,rowstr]} (gB+rIp)[+pm], viz[Z] [,?prSC]
syntax
Return      vec_t
type
                                                             Determines the element size and number
                                MDW_options
            1    MDW
                                enum                         of loaded elements (see enum definition
                                                             at vec-mem-modes.h)
            2    IN1_gB_BASE    void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from

Operands    3    IN2_rI_OFFSET void *
                                                             the base pointer
            4    IN2_PART       uint8           LOW,HIGH     Word part which is used for operand 3
            5    IN3_PM_PTR     void*                        Pointer register (rN)
                                                             Offset for the first DW used from the
            6    OUT_OFST       uint8           0..7
                                                             result operand
            void* ptr;
C example   void* ptrBase;
            void* ptrModify;
            vec_t vRes;
            ...
            vRes = vlddw_indexed_rIp_pm_ptr_v32_clone (mdw_8dw, ptrBase, ptrModify, LOW, ptr, 0);

                 The same data will be loaded to all vector units (Unless str1 is configured
Comments    1.
                 otherwise).



Intrinsic   vlddw_indexed_rIp_v32_clone
name        vlddw_indexed_rIp_v32_str1

Spec        vlddw {mdw [,strX][,rowstr]} (gB+rIp)[+pm], viz[Z] [,?prSC]
syntax
Return      vec_t
type
                                                              Determines the element size and number
                                 MDW_options
            1    MDW
                                 enum                         of loaded elements (see enum definition
                                                              at vec-mem-modes.h)
            2    IN1_gB_BASE     void *                       Pointer register (gB)
Operands                                                      Pointer (rI) specifying the offset from
            3    IN2_rI_OFFSET void *
                                                              the base pointer
            4    IN2_PART        uint8           LOW,HIGH     Word part which is used for operand 3

            5
                                                              Offset for the first DW used from the
                 OUT_OFST        uint8           0..7
                                                              result operand
            void* ptrBase;
            void* ptrModify;
C example   vec_t vRes;
            ...
            vRes = vlddw_indexed_rIp_v32_clone (mdw_8dw, ptrBase, ptrModify, LOW, 0);

                 The same data will be loaded to all vector units (Unless str1 is configured
Comments    1.
                 otherwise).



Intrinsic   vlddw_pm_imm_v32_clone
name        vlddw_pm_imm_v32_str1

Spec        vlddw {mdw [,strX][,rowstr]} (pN)+#imm32_6, viz[Z] [,?prSC]
syntax
Return      vec_t
type
                                                             Determines the element size and number
                               MDW_options
Operands    1    MDW
                               enum                          of loaded elements (see enum definition
                                                             at vec-mem-modes.h)
            2    IN1_PTR       void *                         Pointer register (rN)
                                                 31   31      32 bit immediate post modification in
            3    IN2_IMM32_6 int32             -2 ..2 -1
                                                              bytes

            4
                                                              Offset for the first DW used from the
                 OUT_OFST      uint8           0..7
                                                              result operand
            void* ptr;
            vec_t vRes;
C example   ...
            vRes = vlddw_pm_imm_v32_clone (mdw_8dw, ptr, 2, 0);

                 The same data will be loaded to all vector units (Unless str1 is configured
Comments    1.
                 otherwise).



Intrinsic   vlddw_pm_ptr_v32_clone
name        vlddw_pm_ptr_v32_str1

Spec        vlddw {mdw [,strX][,rowstr]} (pN)[+pm_x], viz[Z] [,?prSC]
syntax
Return      vec_t
type
                                                              Determines the element size and number
                              MDW_options
            1    MDW
                              enum                            of loaded elements (see enum definition
                                                              at vec-mem-modes.h)

Operands    2    IN1_PTR      void *                          Pointer register (rN)
            3    IN2_PM_PTR void*                             Pointer register (rN)
                                                              Offset for the first DW used from the
            4    OUT_OFST     uint8            0..7
                                                              result operand
            void* ptr;
            void* vRes;
C example   ...
            ptr = vlddw_pm_ptr_v32_clone (mdw_8dw, ptr, vRes, 0);

                 The same data will be loaded to all vector units (Unless str1 is configured
Comments    1.
                 otherwise).



Intrinsic   vlddw_v32_clone

name        vlddw_v32_str1

Spec        vlddw {mdw [,strX][,rowstr]} (pN)[+pm_x], viz[Z] [,?prSC]
syntax
Return      vec_t
type
                                                          Determines the element size and number
                               MDW_options
              1    MDW
                               enum                       of loaded elements (see enum definition
                                                          at vec-mem-modes.h)
Operands      2    IN1_PTR     void *                     Pointer register (rN)

              3
                                                          Offset for the first DW used from the
                   OUT_OFST uint8               0..7
                                                          result operand
              void* ptr;
              vec_t vRes;
C example     ...
              vRes = vlddw_v32_clone (mdw_8dw, ptr, 0);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).


Main table → Memory Access → Load → Load DW into 32 bit register
Available addressing modes
Intrinsic Names:
vlddw_indexed_imm_v32_clone_rowstr
vlddw_indexed_rI_pm_imm_v32_clone_rowstr
vlddw_indexed_rI_pm_ptr_v32_clone_rowstr
vlddw_indexed_rI_v32_clone_rowstr
vlddw_indexed_rIp_pm_imm_v32_clone_rowstr
vlddw_indexed_rIp_pm_ptr_v32_clone_rowstr
vlddw_indexed_rIp_v32_clone_rowstr
vlddw_pm_imm_v32_clone_rowstr
vlddw_pm_ptr_v32_clone_rowstr
vlddw_v32_clone_rowstr
Intrinsic   vlddw_indexed_imm_v32_clone_rowstr
name        vlddw_indexed_imm_v32_str1_rowstr

Spec        vlddw {mdw[,strX][,rowstr]} (gB+#imm16_6), viz[Z] [,?prSC]
syntax
Return      vec_t
type
                                                              Determines the element size and
                               MDW_options
            1    MDW
                               enum                           number of loaded elements (see enum
                                                              definition at vec-mem-modes.h)
            2    IN1_gB_BASE void *                           Pointer register (gB)
Operands
                                               -              16 bit immediate post modification in
            3    IN2_IMM16_6   int16
                                               32768..32767   bytes
                                                              Offset for the first DW used from the

4    OUT_OFST      uint8           0..7
                                                              result operand
            void* ptrBase;
            vec_t vRes;
C example   ...
            vRes = vlddw_indexed_imm_v32_clone_rowstr (mdw_8dw, ptrBase, 2, 0);

                 The same data will be loaded to all vector units (Unless str1 is configured
Comments    1.
                 otherwise).



Intrinsic   vlddw_indexed_rI_pm_imm_v32_clone_rowstr
name        vlddw_indexed_rI_pm_imm_v32_str1_rowstr

Spec        vlddw {mdw [,strX][,rowstr]} (gB+rI)[+pm], viz[Z] [,?prSC]
syntax
Return      vec_t
type
                                                              Determines the element size and number
                                MDW_options
            1    MDW
                                enum                          of loaded elements (see enum definition
                                                              at vec-mem-modes.h)
            2    IN1_gB_BASE    void *                        Pointer register (gB)
                                                              Pointer (rI) specifying the offset from
Operands    3    IN2_rI_OFFSET void *
                                                              the base pointer

            4                                     31   31     32 bit immediate post modification in
                 IN3_PM_IMM     int32           -2 ..2 -1
                                                              bytes
                                                              Offset for the first DW used from the
            5    OUT_OFST       uint8           0..7
                                                              result operand
            void* ptrBase;
            void* ptrModify;
C example   vec_t vRes;
            ...
            vRes = vlddw_indexed_rI_pm_imm_v32_clone_rowstr (mdw_8dw, ptrBase, ptrModify, 2, 0);

                 The same data will be loaded to all vector units (Unless str1 is configured
Comments    1.
                 otherwise).



Intrinsic   vlddw_indexed_rI_pm_ptr_v32_clone_rowstr
name        vlddw_indexed_rI_pm_ptr_v32_str1_rowstr

Spec        vlddw {mdw [,strX][,rowstr]} (gB+rI)[+pm], viz[Z] [,?prSC]
syntax
Return      vec_t
type
                                                               Determines the element size and number
                                 MDW_options
            1    MDW

enum                          of loaded elements (see enum definition
                                                               at vec-mem-modes.h)
            2    IN1_gB_BASE     void *                        Pointer register (gB)
Operands                                                       Pointer (rI) specifying the offset from
            3    IN2_rI_OFFSET void *
                                                               the base pointer
            4    IN3_PM_PTR      void*                         Pointer register (rN)
                                                               Offset for the first DW used from the
            5    OUT_OFST        uint8           0..7
                                                               result operand
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec_t vRes;
            ...
            vRes = vlddw_indexed_rI_pm_ptr_v32_clone_rowstr (mdw_8dw, ptrBase, ptrModify, ptr, 0);

                 The same data will be loaded to all vector units (Unless str1 is configured
Comments    1.
                 otherwise).



Intrinsic   vlddw_indexed_rI_v32_clone_rowstr
name        vlddw_indexed_rI_v32_str1_rowstr

Spec        vlddw {mdw [,strX][,rowstr]} (gB+rI)[+pm], viz[Z] [,?prSC]
syntax
Return      vec_t
type
                                 MDW_options
Operands    1    MDW
                                 enum                          Determines the element size and number
                                                               of loaded elements (see enum definition
                                                               at vec-mem-modes.h)
            2    IN1_gB_BASE     void *                        Pointer register (gB)

            3
                                                               Pointer (rI) specifying the offset from
                 IN2_rI_OFFSET void *
                                                               the base pointer
                                                               Offset for the first DW used from the
            4    OUT_OFST        uint8           0..7
                                                               result operand
            void* ptrBase;
            void* ptrModify;
C example   vec_t vRes;
            ...
            vRes = vlddw_indexed_rI_v32_clone_rowstr (mdw_8dw, ptrBase, ptrModify, 0);

The same data will be loaded to all vector units (Unless str1 is configured
Comments    1.
                 otherwise).



Intrinsic   vlddw_indexed_rIp_pm_imm_v32_clone_rowstr
name        vlddw_indexed_rIp_pm_imm_v32_str1_rowstr

Spec        vlddw {mdw [,strX][,rowstr]} (gB+rIp)[+pm], viz[Z] [,?prSC]
syntax
Return      vec_t
type
                                                               Determines the element size and number
                                 MDW_options
            1    MDW
                                 enum                          of loaded elements (see enum definition
                                                               at vec-mem-modes.h)
            2    IN1_gB_BASE     void *                        Pointer register (gB)
                                                               Pointer (rI) specifying the offset from
            3    IN2_rI_OFFSET void *
Operands                                                       the base pointer
            4    IN2_PART        uint8           LOW,HIGH      Word part which is used for operand 3
                                                   31   31     32 bit immediate post modification in
            5    IN3_PM_IMM      int32           -2 ..2 -1
                                                               bytes
                                                               Offset for the first DW used from the
            6    OUT_OFST        uint8           0..7
                                                               result operand
            void* ptrBase;
            void* ptrModify;
C example   vec_t vRes;
            ...
            vRes = vlddw_indexed_rIp_pm_imm_v32_clone_rowstr (mdw_8dw, ptrBase, ptrModify, LOW, 2, 0);

                 The same data will be loaded to all vector units (Unless str1 is configured
Comments    1.
                 otherwise).
Intrinsic   vlddw_indexed_rIp_pm_ptr_v32_clone_rowstr
name        vlddw_indexed_rIp_pm_ptr_v32_str1_rowstr

Spec        vlddw {mdw [,strX][,rowstr]} (gB+rIp)[+pm], viz[Z] [,?prSC]
syntax
Return      vec_t
type
                                                              Determines the element size and number
                                MDW_options
            1    MDW
                                enum                          of loaded elements (see enum definition
                                                              at vec-mem-modes.h)

2    IN1_gB_BASE    void *                        Pointer register (gB)
                                                              Pointer (rI) specifying the offset from
            3    IN2_rI_OFFSET void *
Operands                                                      the base pointer
            4    IN2_PART       uint8            LOW,HIGH     Word part which is used for operand 3
            5    IN3_PM_PTR     void*                         Pointer register (rN)

            6
                                                              Offset for the first DW used from the
                 OUT_OFST       uint8            0..7
                                                              result operand
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec_t vRes;
            ...
            vRes = vlddw_indexed_rIp_pm_ptr_v32_clone_rowstr (mdw_8dw, ptrBase, ptrModify, LOW, ptr, 0);

                 The same data will be loaded to all vector units (Unless str1 is configured
Comments    1.
                 otherwise).



Intrinsic   vlddw_indexed_rIp_v32_clone_rowstr
name        vlddw_indexed_rIp_v32_str1_rowstr

Spec        vlddw {mdw [,strX][,rowstr]} (gB+rIp)[+pm], viz[Z] [,?prSC]
syntax
Return      vec_t
type
                                                              Determines the element size and number
                                MDW_options
            1    MDW
                                enum                          of loaded elements (see enum definition
                                                              at vec-mem-modes.h)
Operands
            2    IN1_gB_BASE    void *                        Pointer register (gB)
            3    IN2_rI_OFFSET void *                         Pointer (rI) specifying the offset from
                                                              the base pointer
            4    IN2_PART       uint8            LOW,HIGH     Word part which is used for operand 3

            5
                                                              Offset for the first DW used from the
                 OUT_OFST       uint8            0..7
                                                              result operand
            void* ptrBase;
            void* ptrModify;
C example   vec_t vRes;
            ...
            vRes = vlddw_indexed_rIp_v32_clone_rowstr (mdw_8dw, ptrBase, ptrModify, LOW, 0);

The same data will be loaded to all vector units (Unless str1 is configured
Comments    1.
                 otherwise).



Intrinsic   vlddw_pm_imm_v32_clone_rowstr
name        vlddw_pm_imm_v32_str1_rowstr

Spec        vlddw {mdw [,strX][,rowstr]} (pN)+#imm32_6, viz[Z] [,?prSC]
syntax
Return      vec_t
type
                                                             Determines the element size and number
                               MDW_options
            1    MDW
                               enum                          of loaded elements (see enum definition
                                                             at vec-mem-modes.h)
            2    IN1_PTR       void *                        Pointer register (rN)
Operands
                                                 31     31   32 bit immediate post modification in
            3    IN2_IMM32_6 int32             -2 ..2 -1
                                                             bytes
                                                             Offset for the first DW used from the
            4    OUT_OFST      uint8           0..7
                                                             result operand
            void* ptr;
            vec_t vRes;
C example   ...
            vRes = vlddw_pm_imm_v32_clone_rowstr (mdw_8dw, ptr, 2, 0);

                 The same data will be loaded to all vector units (Unless str1 is configured
Comments    1.
                 otherwise).



Intrinsic   vlddw_pm_ptr_v32_clone_rowstr
name        vlddw_pm_ptr_v32_str1_rowstr

Spec        vlddw {mdw [,strX][,rowstr]} (pN)[+pm_x], viz[Z] [,?prSC]
syntax
Return      vec_t
type
                                                               Determines the element size and number
                              MDW_options
            1    MDW
                              enum                             of loaded elements (see enum definition
                                                               at vec-mem-modes.h)

Operands    2    IN1_PTR      void *                           Pointer register (rN)
            3    IN2_PM_PTR void*                              Pointer register (rN)
                                                               Offset for the first DW used from the
            4    OUT_OFST     uint8            0..7
                                                               result operand
            void* ptr;
            void* vRes;
C example   ...

ptr = vlddw_pm_ptr_v32_clone_rowstr (mdw_8dw, ptr, vRes, 0);

                 The same data will be loaded to all vector units (Unless str1 is configured
Comments    1.
                 otherwise).



Intrinsic   vlddw_v32_clone_rowstr
name        vlddw_v32_str1_rowstr

Spec        vlddw {mdw [,strX][,rowstr]} (pN)[+pm_x], viz[Z] [,?prSC]
syntax
Return      vec_t
type
                                                               Determines the element size and number
                             MDW_options
            1    MDW
                             enum                              of loaded elements (see enum definition
                                                               at vec-mem-modes.h)
Operands    2    IN1_PTR     void *                            Pointer register (rN)
                                                               Offset for the first DW used from the
            3    OUT_OFST uint8               0..7
                                                               result operand
            void* ptr;
            vec_t vRes;
C example   ...
            vRes = vlddw_v32_clone_rowstr (mdw_8dw, ptr, 0);

                 The same data will be loaded to all vector units (Unless str1 is configured
Comments    1.
                 otherwise).


Main table → Memory Access → Load → Load DW into 32 bit register
Available addressing modes
Intrinsic Names:
vlddw_direct_v32_8dw_intrlv
vlddw_indexed_imm_v32_8dw_intrlv
vlddw_indexed_rI_pm_imm_v32_8dw_intrlv
vlddw_indexed_rI_pm_ptr_v32_8dw_intrlv
vlddw_indexed_rI_v32_8dw_intrlv
vlddw_indexed_rIp_pm_imm_v32_8dw_intrlv
vlddw_indexed_rIp_pm_ptr_v32_8dw_intrlv
vlddw_indexed_rIp_v32_8dw_intrlv
vlddw_pm_imm_v32_8dw_intrlv
vlddw_pm_ptr_v32_8dw_intrlv
vlddw_v32_8dw_intrlv
Intrinsic     vlddw_direct_v32_8dw_intrlv
name
Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX]} [#address], viz[Z] [,?prSC]

Return type   vec_t
                                                    32
              1    IN1_ADDR       int32      0..2 -1          32 bit address
Operands                                                      Offset for the first DW used from the
              2    OUT_OFST       uint8      0..7
                                                              result operand
              vec_t vRes;
C example     ...
              vRes = vlddw_direct_v32_8dw_intrlv (2, 0);

Comments



Intrinsic     vlddw_indexed_imm_v32_8dw_intrlv
name

Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+#imm16_6), viz[Z] [,?prSC]

Return type   vec_t

              1    IN1_gB_BASE void *                         Pointer register (gB)
                                                              16 bit immediate post modification in
              2    IN2_IMM16_6     int16     -32768..32767
Operands                                                      bytes
                                                              Offset for the first DW used from the
              3    OUT_OFST        uint8     0..7
                                                              result operand
              void* ptrBase;
              vec_t vRes;
C example     ...
              vRes = vlddw_indexed_imm_v32_8dw_intrlv (ptrBase, 2, 0);

Comments



Intrinsic     vlddw_indexed_rI_pm_imm_v32_8dw_intrlv
name
Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+rI)[+pm], viz[Z] [,?prSC]

Return type   vec_t

              1   IN1_gB_BASE       void *                    Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
Operands                                                      base pointer
                                                31       31   32 bit immediate post modification in
              3   IN3_PM_IMM        int32     -2 ..2 -1
                                                              bytes
                                                              Offset for the first DW used from the
              4   OUT_OFST          uint8     0..7
                                                              result operand
              void* ptrBase;
              void* ptrModify;
C example     vec_t vRes;
              ...
              vRes = vlddw_indexed_rI_pm_imm_v32_8dw_intrlv (ptrBase, ptrModify, 2, 0);

Comments



Intrinsic     vlddw_indexed_rI_pm_ptr_v32_8dw_intrlv
name
Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+rI)[+pm], viz[Z] [,?prSC]

Return type   vec_t

              1   IN1_gB_BASE       void *                    Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
                                                              base pointer
Operands

3   IN3_PM_PTR        void*                     Pointer register (rN)
                                                              Offset for the first DW used from the
              4   OUT_OFST          uint8     0..7
                                                              result operand
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec_t vRes;
              ...
              vRes = vlddw_indexed_rI_pm_ptr_v32_8dw_intrlv (ptrBase, ptrModify, ptr, 0);

Comments



Intrinsic     vlddw_indexed_rI_v32_8dw_intrlv
name
Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+rI)[+pm], viz[Z] [,?prSC]

Return type   vec_t

              1   IN1_gB_BASE       void *                    Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
Operands                                                      base pointer
                                                              Offset for the first DW used from the
              3   OUT_OFST          uint8     0..7
                                                              result operand
              void* ptrBase;
C example     void* ptrModify;
              vec_t vRes;
              ...
              vRes = vlddw_indexed_rI_v32_8dw_intrlv (ptrBase, ptrModify, 0);

Comments



Intrinsic     vlddw_indexed_rIp_pm_imm_v32_8dw_intrlv
name
Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+rIp)[+pm], viz[Z] [,?prSC]

Return type   vec_t

              1    IN1_gB_BASE      void *                    Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                              base pointer
              3    IN2_PART         uint8     LOW,HIGH        Word part which is used for operand 2
Operands
              4                                 31   31       32 bit immediate post modification in
                   IN3_PM_IMM       int32     -2 ..2 -1
                                                              bytes
                                                              Offset for the first DW used from the
              5    OUT_OFST         uint8     0..7
                                                              result operand
              void* ptrBase;

void* ptrModify;
C example     vec_t vRes;
              ...
              vRes = vlddw_indexed_rIp_pm_imm_v32_8dw_intrlv (ptrBase, ptrModify, LOW, 2, 0);

Comments



Intrinsic     vlddw_indexed_rIp_pm_ptr_v32_8dw_intrlv
name
Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+rIp)[+pm], viz[Z] [,?prSC]

Return type   vec_t

              1    IN1_gB_BASE      void *                    Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                              base pointer
Operands      3    IN2_PART         uint8     LOW,HIGH        Word part which is used for operand 2
              4    IN3_PM_PTR       void*                     Pointer register (rN)
                                                              Offset for the first DW used from the
              5    OUT_OFST         uint8     0..7
                                                              result operand
C example     void* ptr;
              void* ptrBase;
              void* ptrModify;
              vec_t vRes;
              ...
              vRes = vlddw_indexed_rIp_pm_ptr_v32_8dw_intrlv (ptrBase, ptrModify, LOW, ptr, 0);

Comments



Intrinsic     vlddw_indexed_rIp_v32_8dw_intrlv
name
Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+rIp)[+pm], viz[Z] [,?prSC]

Return type   vec_t

              1   IN1_gB_BASE       void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
                                                             base pointer
Operands
              3   IN2_PART          uint8    LOW,HIGH        Word part which is used for operand 2
                                                             Offset for the first DW used from the
              4   OUT_OFST          uint8    0..7
                                                             result operand
              void* ptrBase;
              void* ptrModify;
C example     vec_t vRes;
              ...
              vRes = vlddw_indexed_rIp_v32_8dw_intrlv (ptrBase, ptrModify, LOW, 0);

Comments



Intrinsic     vlddw_pm_imm_v32_8dw_intrlv
name
Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (pN)+#imm32_6, viz[Z] [,?prSC]

Return type   vec_t

1    IN1_PTR         void *                    Pointer register (rN)
                                               31   31       32 bit immediate post modification in
              2    IN2_IMM32_6 int32         -2 ..2 -1
Operands                                                     bytes
                                                             Offset for the first DW used from the
              3    OUT_OFST        uint8     0..7
                                                             result operand
              void* ptr;
              vec_t vRes;
C example     ...
              vRes = vlddw_pm_imm_v32_8dw_intrlv (ptr, 2, 0);

Comments
Intrinsic      vlddw_pm_ptr_v32_8dw_intrlv
name
Spec syntax    vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (pN)[+pm_x], viz[Z] [,?prSC]

Return type    vec_t

               1    IN1_PTR         void *                    Pointer register (rN)
               2    IN2_PM_PTR void*                          Pointer register (rN)
Operands
                                                              Offset for the first DW used from the
               3    OUT_OFST        uint8     0..7
                                                              result operand
               void* ptr;
               void* vRes;
C example      ...
               ptr = vlddw_pm_ptr_v32_8dw_intrlv (ptr, vRes, 0);

Comments



Intrinsic      vlddw_v32_8dw_intrlv
name
Spec syntax    vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (pN)[+pm_x], viz[Z] [,?prSC]

Return type    vec_t

               1    IN1_PTR         void *                    Pointer register (rN)
Operands                                                      Offset for the first DW used from the
               2    OUT_OFST        uint8     0..7
                                                              result operand
               void* ptr;
               vec_t vRes;
C example      ...
               vRes = vlddw_v32_8dw_intrlv (ptr, 0);

Comments


Main table → Memory Access → Load → Load DW into 32 bit register
Available addressing modes
Intrinsic Names:
vlddw_direct_v32_8dw_intrlv_int2dw
vlddw_indexed_imm_v32_8dw_intrlv_int2dw
vlddw_indexed_rI_pm_imm_v32_8dw_intrlv_int2dw
vlddw_indexed_rI_pm_ptr_v32_8dw_intrlv_int2dw
vlddw_indexed_rI_v32_8dw_intrlv_int2dw
vlddw_indexed_rIp_pm_imm_v32_8dw_intrlv_int2dw
vlddw_indexed_rIp_pm_ptr_v32_8dw_intrlv_int2dw
vlddw_indexed_rIp_v32_8dw_intrlv_int2dw
vlddw_pm_imm_v32_8dw_intrlv_int2dw
vlddw_pm_ptr_v32_8dw_intrlv_int2dw

vlddw_v32_8dw_intrlv_int2dw
Intrinsic     vlddw_direct_v32_8dw_intrlv_int2dw
name
Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX]} [#address], viz[Z] [,?prSC]

Return type   vec_t
                                                    32
              1    IN1_ADDR       int32      0..2 -1          32 bit address
Operands                                                      Offset for the first DW used from the
              2    OUT_OFST       uint8      0..7
                                                              result operand
              vec_t vRes;
C example     ...
              vRes = vlddw_direct_v32_8dw_intrlv_int2dw (2, 0);

Comments



Intrinsic     vlddw_indexed_imm_v32_8dw_intrlv_int2dw
name
Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+#imm16_6), viz[Z] [,?prSC]

Return type   vec_t

              1    IN1_gB_BASE void *                         Pointer register (gB)
                                                              16 bit immediate post modification in
              2    IN2_IMM16_6     int16     -32768..32767
Operands                                                      bytes
                                                              Offset for the first DW used from the
              3    OUT_OFST        uint8     0..7
                                                              result operand
              void* ptrBase;
              vec_t vRes;
C example     ...
              vRes = vlddw_indexed_imm_v32_8dw_intrlv_int2dw (ptrBase, 2, 0);

Comments



Intrinsic     vlddw_indexed_rI_pm_imm_v32_8dw_intrlv_int2dw
name
Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+rI)[+pm], viz[Z] [,?prSC]

Return type   vec_t

              1   IN1_gB_BASE       void *                    Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
Operands                                                      base pointer
                                                31       31   32 bit immediate post modification in
              3   IN3_PM_IMM        int32     -2 ..2 -1
                                                              bytes
                                                             Offset for the first DW used from the
              4   OUT_OFST          uint8    0..7
                                                             result operand
              void* ptrBase;

void* ptrModify;
C example     vec_t vRes;
              ...
              vRes = vlddw_indexed_rI_pm_imm_v32_8dw_intrlv_int2dw (ptrBase, ptrModify, 2, 0);

Comments



Intrinsic     vlddw_indexed_rI_pm_ptr_v32_8dw_intrlv_int2dw
name
Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+rI)[+pm], viz[Z] [,?prSC]

Return type   vec_t

              1   IN1_gB_BASE       void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
                                                             base pointer
Operands
              3   IN3_PM_PTR        void*                    Pointer register (rN)
                                                             Offset for the first DW used from the
              4   OUT_OFST          uint8    0..7
                                                             result operand
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec_t vRes;
              ...
              vRes = vlddw_indexed_rI_pm_ptr_v32_8dw_intrlv_int2dw (ptrBase, ptrModify, ptr, 0);

Comments



Intrinsic     vlddw_indexed_rI_v32_8dw_intrlv_int2dw
name
Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+rI)[+pm], viz[Z] [,?prSC]

Return type   vec_t

              1   IN1_gB_BASE       void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
Operands                                                     base pointer
                                                             Offset for the first DW used from the
              3   OUT_OFST          uint8    0..7
                                                             result operand
              void* ptrBase;
C example     void* ptrModify;
              vec_t vRes;
              ...
              vRes = vlddw_indexed_rI_v32_8dw_intrlv_int2dw (ptrBase, ptrModify, 0);

Comments



Intrinsic     vlddw_indexed_rIp_pm_imm_v32_8dw_intrlv_int2dw
name
Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+rIp)[+pm], viz[Z] [,?prSC]

Return type   vec_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the

2    IN2_rI_OFFSET void *
                                                             base pointer
              3    IN2_PART         uint8    LOW,HIGH        Word part which is used for operand 2
Operands
              4                                31   31       32 bit immediate post modification in
                   IN3_PM_IMM       int32    -2 ..2 -1
                                                             bytes
                                                             Offset for the first DW used from the
              5    OUT_OFST         uint8    0..7
                                                             result operand
              void* ptrBase;
              void* ptrModify;
C example     vec_t vRes;
              ...
              vRes = vlddw_indexed_rIp_pm_imm_v32_8dw_intrlv_int2dw (ptrBase, ptrModify, LOW, 2, 0);

Comments



Intrinsic     vlddw_indexed_rIp_pm_ptr_v32_8dw_intrlv_int2dw
name
Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+rIp)[+pm], viz[Z] [,?prSC]

Return type   vec_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
Operands      3    IN2_PART         uint8    LOW,HIGH        Word part which is used for operand 2
              4    IN3_PM_PTR       void*                    Pointer register (rN)
                                                             Offset for the first DW used from the
              5    OUT_OFST         uint8    0..7
                                                             result operand
C example     void* ptr;
              void* ptrBase;
              void* ptrModify;
              vec_t vRes;
              ...
              vRes = vlddw_indexed_rIp_pm_ptr_v32_8dw_intrlv_int2dw (ptrBase, ptrModify, LOW, ptr, 0);

Comments



Intrinsic     vlddw_indexed_rIp_v32_8dw_intrlv_int2dw
name
Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+rIp)[+pm], viz[Z] [,?prSC]

Return type   vec_t

              1   IN1_gB_BASE       void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
                                                             base pointer
Operands

3   IN2_PART          uint8    LOW,HIGH        Word part which is used for operand 2
                                                             Offset for the first DW used from the
              4   OUT_OFST          uint8    0..7
                                                             result operand
              void* ptrBase;
              void* ptrModify;
C example     vec_t vRes;
              ...
              vRes = vlddw_indexed_rIp_v32_8dw_intrlv_int2dw (ptrBase, ptrModify, LOW, 0);

Comments



Intrinsic     vlddw_pm_imm_v32_8dw_intrlv_int2dw
name
Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (pN)+#imm32_6, viz[Z] [,?prSC]

Return type   vec_t

              1    IN1_PTR         void *                   Pointer register (rN)
                                               31   31      32 bit immediate post modification in
              2    IN2_IMM32_6 int32         -2 ..2 -1
Operands                                                    bytes
                                                            Offset for the first DW used from the
              3    OUT_OFST        uint8     0..7
                                                            result operand
              void* ptr;
              vec_t vRes;
C example     ...
              vRes = vlddw_pm_imm_v32_8dw_intrlv_int2dw (ptr, 2, 0);

Comments
Intrinsic      vlddw_pm_ptr_v32_8dw_intrlv_int2dw
name
Spec syntax    vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (pN)[+pm_x], viz[Z] [,?prSC]

Return type    vec_t

               1    IN1_PTR        void *                     Pointer register (rN)
               2    IN2_PM_PTR void*                          Pointer register (rN)
Operands
                                                              Offset for the first DW used from the
               3    OUT_OFST       uint8     0..7
                                                              result operand
               void* ptr;
               void* vRes;
C example      ...
               ptr = vlddw_pm_ptr_v32_8dw_intrlv_int2dw (ptr, vRes, 0);

Comments



Intrinsic      vlddw_v32_8dw_intrlv_int2dw
name
Spec syntax    vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (pN)[+pm_x], viz[Z] [,?prSC]

Return type    vec_t

               1    IN1_PTR        void *                     Pointer register (rN)
Operands                                                      Offset for the first DW used from the
               2    OUT_OFST       uint8     0..7

result operand
               void* ptr;
               vec_t vRes;
C example      ...
               vRes = vlddw_v32_8dw_intrlv_int2dw (ptr, 0);

Comments


Main table → Memory Access → Load → Load DW into 32 bit register
Available addressing modes
Intrinsic Names:
vlddw_indexed_imm_v32_8dw_intrlv_int2dw_rowstr
vlddw_indexed_rI_pm_imm_v32_8dw_intrlv_int2dw_rowstr
vlddw_indexed_rI_pm_ptr_v32_8dw_intrlv_int2dw_rowstr
vlddw_indexed_rI_v32_8dw_intrlv_int2dw_rowstr
vlddw_indexed_rIp_pm_imm_v32_8dw_intrlv_int2dw_rowstr
vlddw_indexed_rIp_pm_ptr_v32_8dw_intrlv_int2dw_rowstr
vlddw_indexed_rIp_v32_8dw_intrlv_int2dw_rowstr
vlddw_pm_imm_v32_8dw_intrlv_int2dw_rowstr
vlddw_pm_ptr_v32_8dw_intrlv_int2dw_rowstr
vlddw_v32_8dw_intrlv_int2dw_rowstr
Intrinsic     vlddw_indexed_imm_v32_8dw_intrlv_int2dw_rowstr
name
Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+#imm16_6), viz[Z] [,?prSC]

Return type   vec_t

              1    IN1_gB_BASE void *                        Pointer register (gB)
                                                             16 bit immediate post modification in
              2    IN2_IMM16_6     int16     -32768..32767
Operands                                                     bytes
                                                             Offset for the first DW used from the
              3    OUT_OFST        uint8     0..7
                                                             result operand
              void* ptrBase;
              vec_t vRes;
C example     ...
              vRes = vlddw_indexed_imm_v32_8dw_intrlv_int2dw_rowstr (ptrBase, 2, 0);

Comments



Intrinsic     vlddw_indexed_rI_pm_imm_v32_8dw_intrlv_int2dw_rowstr
name
Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+rI)[+pm], viz[Z] [,?prSC]

Return type   vec_t

              1   IN1_gB_BASE       void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
                                                             base pointer
Operands                                       31   31       32 bit immediate post modification in
              3   IN3_PM_IMM        int32    -2 ..2 -1
                                                             bytes
                                                             Offset for the first DW used from the
              4   OUT_OFST          uint8    0..7

result operand
              void* ptrBase;
              void* ptrModify;
C example     vec_t vRes;
              ...
              vRes = vlddw_indexed_rI_pm_imm_v32_8dw_intrlv_int2dw_rowstr (ptrBase, ptrModify, 2, 0);

Comments



Intrinsic     vlddw_indexed_rI_pm_ptr_v32_8dw_intrlv_int2dw_rowstr
name
Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+rI)[+pm], viz[Z] [,?prSC]

Return type   vec_t
              1   IN1_gB_BASE       void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
                                                             base pointer
Operands
              3   IN3_PM_PTR        void*                    Pointer register (rN)
                                                             Offset for the first DW used from the
              4   OUT_OFST          uint8    0..7
                                                             result operand
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec_t vRes;
              ...
              vRes = vlddw_indexed_rI_pm_ptr_v32_8dw_intrlv_int2dw_rowstr (ptrBase, ptrModify, ptr, 0);

Comments



Intrinsic     vlddw_indexed_rI_v32_8dw_intrlv_int2dw_rowstr
name
Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+rI)[+pm], viz[Z] [,?prSC]

Return type   vec_t

              1   IN1_gB_BASE       void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
Operands                                                     base pointer
                                                             Offset for the first DW used from the
              3   OUT_OFST          uint8    0..7
                                                             result operand
              void* ptrBase;
              void* ptrModify;
C example     vec_t vRes;
              ...
              vRes = vlddw_indexed_rI_v32_8dw_intrlv_int2dw_rowstr (ptrBase, ptrModify, 0);

Comments



Intrinsic     vlddw_indexed_rIp_pm_imm_v32_8dw_intrlv_int2dw_rowstr
name
Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+rIp)[+pm], viz[Z] [,?prSC]

Return type   vec_t

              1   IN1_gB_BASE       void *                   Pointer register (gB)

Operands                                                     Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
                                                             base pointer
              3   IN2_PART          uint8    LOW,HIGH        Word part which is used for operand 2
                                               31   31       32 bit immediate post modification in
              4   IN3_PM_IMM        int32    -2 ..2 -1
                                                             bytes

              5
                                                             Offset for the first DW used from the
                  OUT_OFST          uint8    0..7
                                                             result operand
              void* ptrBase;
              void* ptrModify;
C example     vec_t vRes;
              ...
              vRes = vlddw_indexed_rIp_pm_imm_v32_8dw_intrlv_int2dw_rowstr (ptrBase, ptrModify, LOW, 2, 0);

Comments



Intrinsic     vlddw_indexed_rIp_pm_ptr_v32_8dw_intrlv_int2dw_rowstr
name
Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+rIp)[+pm], viz[Z] [,?prSC]

Return type   vec_t

              1   IN1_gB_BASE       void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
                                                             base pointer
Operands      3   IN2_PART          uint8    LOW,HIGH        Word part which is used for operand 2
              4   IN3_PM_PTR        void*                    Pointer register (rN)
                                                             Offset for the first DW used from the
              5   OUT_OFST          uint8    0..7
                                                             result operand
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec_t vRes;
              ...
              vRes = vlddw_indexed_rIp_pm_ptr_v32_8dw_intrlv_int2dw_rowstr (ptrBase, ptrModify, LOW, ptr, 0);

Comments



Intrinsic     vlddw_indexed_rIp_v32_8dw_intrlv_int2dw_rowstr
name
Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+rIp)[+pm], viz[Z] [,?prSC]

Return type   vec_t

              1   IN1_gB_BASE       void *                   Pointer register (gB)
Operands

2   IN2_rI_OFFSET void *                       Pointer (rI) specifying the offset from the
                                                             base pointer
              3   IN2_PART          uint8    LOW,HIGH        Word part which is used for operand 2

              4
                                                             Offset for the first DW used from the
                  OUT_OFST          uint8    0..7
                                                             result operand
              void* ptrBase;
              void* ptrModify;
C example     vec_t vRes;
              ...
              vRes = vlddw_indexed_rIp_v32_8dw_intrlv_int2dw_rowstr (ptrBase, ptrModify, LOW, 0);

Comments



Intrinsic     vlddw_pm_imm_v32_8dw_intrlv_int2dw_rowstr
name
Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (pN)+#imm32_6, viz[Z] [,?prSC]

Return type   vec_t

              1    IN1_PTR        void *                    Pointer register (rN)
                                              31    31      32 bit immediate post modification in
              2    IN2_IMM32_6 int32        -2 ..2 -1
Operands                                                    bytes
                                                            Offset for the first DW used from the
              3    OUT_OFST       uint8     0..7
                                                            result operand
              void* ptr;
              vec_t vRes;
C example     ...
              vRes = vlddw_pm_imm_v32_8dw_intrlv_int2dw_rowstr (ptr, 2, 0);

Comments



Intrinsic     vlddw_pm_ptr_v32_8dw_intrlv_int2dw_rowstr
name
Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (pN)[+pm_x], viz[Z] [,?prSC]

Return type   vec_t

              1    IN1_PTR        void *                    Pointer register (rN)
              2    IN2_PM_PTR void*                         Pointer register (rN)
Operands
              3
                                                            Offset for the first DW used from the
                   OUT_OFST       uint8     0..7
                                                            result operand
              void* ptr;
              void* vRes;
C example     ...
              ptr = vlddw_pm_ptr_v32_8dw_intrlv_int2dw_rowstr (ptr, vRes, 0);
Comments



Intrinsic      vlddw_v32_8dw_intrlv_int2dw_rowstr
name
Spec syntax    vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (pN)[+pm_x], viz[Z] [,?prSC]

Return type    vec_t

1    IN1_PTR        void *                    Pointer register (rN)
Operands                                                     Offset for the first DW used from the
               2    OUT_OFST       uint8     0..7
                                                             result operand
               void* ptr;
               vec_t vRes;
C example      ...
               vRes = vlddw_v32_8dw_intrlv_int2dw_rowstr (ptr, 0);

Comments


Main table → Memory Access → Load → Load DW into 32 bit register
Available addressing modes
Intrinsic Names:
vlddw_indexed_imm_v32_8dw_intrlv_rowstr
vlddw_indexed_rI_pm_imm_v32_8dw_intrlv_rowstr
vlddw_indexed_rI_pm_ptr_v32_8dw_intrlv_rowstr
vlddw_indexed_rI_v32_8dw_intrlv_rowstr
vlddw_indexed_rIp_pm_imm_v32_8dw_intrlv_rowstr
vlddw_indexed_rIp_pm_ptr_v32_8dw_intrlv_rowstr
vlddw_indexed_rIp_v32_8dw_intrlv_rowstr
vlddw_pm_imm_v32_8dw_intrlv_rowstr
vlddw_pm_ptr_v32_8dw_intrlv_rowstr
vlddw_v32_8dw_intrlv_rowstr
Intrinsic     vlddw_indexed_imm_v32_8dw_intrlv_rowstr
name
Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+#imm16_6), viz[Z] [,?prSC]

Return type   vec_t

              1    IN1_gB_BASE void *                        Pointer register (gB)
                                                             16 bit immediate post modification in
              2    IN2_IMM16_6     int16     -32768..32767
Operands                                                     bytes
                                                             Offset for the first DW used from the
              3    OUT_OFST        uint8     0..7
                                                             result operand
              void* ptrBase;
              vec_t vRes;
C example     ...
              vRes = vlddw_indexed_imm_v32_8dw_intrlv_rowstr (ptrBase, 2, 0);

Comments



Intrinsic     vlddw_indexed_rI_pm_imm_v32_8dw_intrlv_rowstr
name
Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+rI)[+pm], viz[Z] [,?prSC]

Return type   vec_t

              1   IN1_gB_BASE       void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
                                                             base pointer
Operands                                       31   31       32 bit immediate post modification in
              3   IN3_PM_IMM        int32    -2 ..2 -1

bytes
                                                             Offset for the first DW used from the
              4   OUT_OFST          uint8    0..7
                                                             result operand
              void* ptrBase;
              void* ptrModify;
C example     vec_t vRes;
              ...
              vRes = vlddw_indexed_rI_pm_imm_v32_8dw_intrlv_rowstr (ptrBase, ptrModify, 2, 0);

Comments



Intrinsic     vlddw_indexed_rI_pm_ptr_v32_8dw_intrlv_rowstr
name
Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+rI)[+pm], viz[Z] [,?prSC]

Return type   vec_t
              1   IN1_gB_BASE       void *                    Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
                                                              base pointer
Operands
              3   IN3_PM_PTR        void*                     Pointer register (rN)
                                                              Offset for the first DW used from the
              4   OUT_OFST          uint8    0..7
                                                              result operand
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec_t vRes;
              ...
              vRes = vlddw_indexed_rI_pm_ptr_v32_8dw_intrlv_rowstr (ptrBase, ptrModify, ptr, 0);

Comments



Intrinsic     vlddw_indexed_rI_v32_8dw_intrlv_rowstr
name
Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+rI)[+pm], viz[Z] [,?prSC]

Return type   vec_t

              1   IN1_gB_BASE       void *                    Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
Operands                                                      base pointer
                                                              Offset for the first DW used from the
              3   OUT_OFST          uint8    0..7
                                                              result operand
              void* ptrBase;
              void* ptrModify;
C example     vec_t vRes;
              ...
              vRes = vlddw_indexed_rI_v32_8dw_intrlv_rowstr (ptrBase, ptrModify, 0);

Comments



Intrinsic     vlddw_indexed_rIp_pm_imm_v32_8dw_intrlv_rowstr
name

Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+rIp)[+pm], viz[Z] [,?prSC]

Return type   vec_t

              1   IN1_gB_BASE       void *                    Pointer register (gB)
Operands                                                      Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
                                                              base pointer
              3   IN2_PART          uint8    LOW,HIGH        Word part which is used for operand 2
                                               31   31       32 bit immediate post modification in
              4   IN3_PM_IMM        int32    -2 ..2 -1
                                                             bytes

              5
                                                             Offset for the first DW used from the
                  OUT_OFST          uint8    0..7
                                                             result operand
              void* ptrBase;
              void* ptrModify;
C example     vec_t vRes;
              ...
              vRes = vlddw_indexed_rIp_pm_imm_v32_8dw_intrlv_rowstr (ptrBase, ptrModify, LOW, 2, 0);

Comments



Intrinsic     vlddw_indexed_rIp_pm_ptr_v32_8dw_intrlv_rowstr
name
Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+rIp)[+pm], viz[Z] [,?prSC]

Return type   vec_t

              1   IN1_gB_BASE       void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
                                                             base pointer
Operands      3   IN2_PART          uint8    LOW,HIGH        Word part which is used for operand 2
              4   IN3_PM_PTR        void*                    Pointer register (rN)
                                                             Offset for the first DW used from the
              5   OUT_OFST          uint8    0..7
                                                             result operand
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec_t vRes;
              ...
              vRes = vlddw_indexed_rIp_pm_ptr_v32_8dw_intrlv_rowstr (ptrBase, ptrModify, LOW, ptr, 0);

Comments



Intrinsic     vlddw_indexed_rIp_v32_8dw_intrlv_rowstr
name
Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+rIp)[+pm], viz[Z] [,?prSC]

Return type   vec_t

              1   IN1_gB_BASE       void *                   Pointer register (gB)
Operands
              2   IN2_rI_OFFSET void *                       Pointer (rI) specifying the offset from the
                                                             base pointer
              3   IN2_PART          uint8    LOW,HIGH        Word part which is used for operand 2

              4
                                                             Offset for the first DW used from the
                  OUT_OFST          uint8    0..7
                                                             result operand
              void* ptrBase;
              void* ptrModify;
C example     vec_t vRes;
              ...
              vRes = vlddw_indexed_rIp_v32_8dw_intrlv_rowstr (ptrBase, ptrModify, LOW, 0);

Comments



Intrinsic     vlddw_pm_imm_v32_8dw_intrlv_rowstr
name
Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (pN)+#imm32_6, viz[Z] [,?prSC]

Return type   vec_t

              1    IN1_PTR        void *                     Pointer register (rN)
                                              31    31       32 bit immediate post modification in
              2    IN2_IMM32_6 int32        -2 ..2 -1
Operands                                                     bytes
                                                             Offset for the first DW used from the
              3    OUT_OFST       uint8     0..7
                                                             result operand
              void* ptr;
              vec_t vRes;
C example     ...
              vRes = vlddw_pm_imm_v32_8dw_intrlv_rowstr (ptr, 2, 0);

Comments



Intrinsic     vlddw_pm_ptr_v32_8dw_intrlv_rowstr
name
Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (pN)[+pm_x], viz[Z] [,?prSC]

Return type   vec_t

              1    IN1_PTR        void *                     Pointer register (rN)
              2    IN2_PM_PTR void*                          Pointer register (rN)
Operands
              3
                                                             Offset for the first DW used from the
                   OUT_OFST       uint8     0..7
                                                             result operand
              void* ptr;
              void* vRes;
C example     ...
              ptr = vlddw_pm_ptr_v32_8dw_intrlv_rowstr (ptr, vRes, 0);
Comments



Intrinsic      vlddw_v32_8dw_intrlv_rowstr
name

Spec syntax    vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (pN)[+pm_x], viz[Z] [,?prSC]

Return type    vec_t

               1    IN1_PTR        void *                     Pointer register (rN)
Operands                                                      Offset for the first DW used from the
               2    OUT_OFST       uint8     0..7
                                                              result operand
               void* ptr;
               vec_t vRes;
C example      ...
               vRes = vlddw_v32_8dw_intrlv_rowstr (ptr, 0);

Comments


Main table → Memory Access → Load → Load DW into 32 bit register
Available addressing modes
Intrinsic Names:
vlddw_direct_v32_clone_8dw_intrlv
vlddw_indexed_imm_v32_clone_8dw_intrlv
vlddw_indexed_rI_pm_imm_v32_clone_8dw_intrlv
vlddw_indexed_rI_pm_ptr_v32_clone_8dw_intrlv
vlddw_indexed_rI_v32_clone_8dw_intrlv
vlddw_indexed_rIp_pm_imm_v32_clone_8dw_intrlv
vlddw_indexed_rIp_pm_ptr_v32_clone_8dw_intrlv
vlddw_indexed_rIp_v32_clone_8dw_intrlv
vlddw_pm_imm_v32_clone_8dw_intrlv
vlddw_pm_ptr_v32_clone_8dw_intrlv
vlddw_v32_clone_8dw_intrlv
Intrinsic     vlddw_direct_v32_clone_8dw_intrlv
name          vlddw_direct_v32_str1_8dw_intrlv

Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX]} [#address], viz[Z] [,?prSC]

Return type   vec_t
                                                    32
              1    IN1_ADDR       int32      0..2 -1         32 bit address
Operands                                                     Offset for the first DW used from the
              2    OUT_OFST       uint8      0..7
                                                             result operand
              vec_t vRes;
C example     ...
              vRes = vlddw_direct_v32_clone_8dw_intrlv (2, 0);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_indexed_imm_v32_clone_8dw_intrlv
name          vlddw_indexed_imm_v32_str1_8dw_intrlv

Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+#imm16_6), viz[Z] [,?prSC]

Return type   vec_t

              1    IN1_gB_BASE void *                        Pointer register (gB)
                                                             16 bit immediate post modification in
              2    IN2_IMM16_6     int16     -32768..32767
Operands                                                     bytes

Offset for the first DW used from the
              3    OUT_OFST        uint8     0..7
                                                             result operand
              void* ptrBase;
              vec_t vRes;
C example     ...
              vRes = vlddw_indexed_imm_v32_clone_8dw_intrlv (ptrBase, 2, 0);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_indexed_rI_pm_imm_v32_clone_8dw_intrlv
name          vlddw_indexed_rI_pm_imm_v32_str1_8dw_intrlv

Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+rI)[+pm], viz[Z] [,?prSC]

Return type   vec_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
Operands                                                     Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
                                                31   31       32 bit immediate post modification in
              3    IN3_PM_IMM       int32     -2 ..2 -1
                                                              bytes
                                                              Offset for the first DW used from the
              4    OUT_OFST         uint8     0..7
                                                              result operand
              void* ptrBase;
              void* ptrModify;
C example     vec_t vRes;
              ...
              vRes = vlddw_indexed_rI_pm_imm_v32_clone_8dw_intrlv (ptrBase, ptrModify, 2, 0);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_indexed_rI_pm_ptr_v32_clone_8dw_intrlv
name          vlddw_indexed_rI_pm_ptr_v32_str1_8dw_intrlv

Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+rI)[+pm], viz[Z] [,?prSC]

Return type   vec_t

              1    IN1_gB_BASE      void *                    Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                              base pointer
Operands
              3    IN3_PM_PTR       void*                     Pointer register (rN)

Offset for the first DW used from the
              4    OUT_OFST         uint8     0..7
                                                              result operand
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec_t vRes;
              ...
              vRes = vlddw_indexed_rI_pm_ptr_v32_clone_8dw_intrlv (ptrBase, ptrModify, ptr, 0);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_indexed_rI_v32_clone_8dw_intrlv
name          vlddw_indexed_rI_v32_str1_8dw_intrlv

Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+rI)[+pm], viz[Z] [,?prSC]

Return type   vec_t

              1    IN1_gB_BASE      void *                    Pointer register (gB)
Operands                                                      Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                              base pointer
                                                              Offset for the first DW used from the
              3    OUT_OFST         uint8     0..7
                                                              result operand
              void* ptrBase;
              void* ptrModify;
C example     vec_t vRes;
              ...
              vRes = vlddw_indexed_rI_v32_clone_8dw_intrlv (ptrBase, ptrModify, 0);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_indexed_rIp_pm_imm_v32_clone_8dw_intrlv
name          vlddw_indexed_rIp_pm_imm_v32_str1_8dw_intrlv

Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+rIp)[+pm], viz[Z] [,?prSC]

Return type   vec_t

              1    IN1_gB_BASE      void *                    Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                              base pointer
              3    IN2_PART         uint8     LOW,HIGH        Word part which is used for operand 2
Operands
                                                31   31       32 bit immediate post modification in
              4    IN3_PM_IMM       int32     -2 ..2 -1
                                                              bytes

Offset for the first DW used from the
              5    OUT_OFST         uint8     0..7
                                                              result operand
              void* ptrBase;
              void* ptrModify;
C example     vec_t vRes;
              ...
              vRes = vlddw_indexed_rIp_pm_imm_v32_clone_8dw_intrlv (ptrBase, ptrModify, LOW, 2, 0);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_indexed_rIp_pm_ptr_v32_clone_8dw_intrlv
name          vlddw_indexed_rIp_pm_ptr_v32_str1_8dw_intrlv

Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+rIp)[+pm], viz[Z] [,?prSC]

Return type   vec_t

              1    IN1_gB_BASE      void *                    Pointer register (gB)
Operands                                                      Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                              base pointer
              3    IN2_PART         uint8    LOW,HIGH        Word part which is used for operand 2
              4    IN3_PM_PTR       void*                    Pointer register (rN)

              5
                                                             Offset for the first DW used from the
                   OUT_OFST         uint8    0..7
                                                             result operand
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec_t vRes;
              ...
              vRes = vlddw_indexed_rIp_pm_ptr_v32_clone_8dw_intrlv (ptrBase, ptrModify, LOW, ptr, 0);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_indexed_rIp_v32_clone_8dw_intrlv
name          vlddw_indexed_rIp_v32_str1_8dw_intrlv

Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+rIp)[+pm], viz[Z] [,?prSC]

Return type   vec_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
Operands
              3    IN2_PART         uint8    LOW,HIGH        Word part which is used for operand 2

Offset for the first DW used from the
              4    OUT_OFST         uint8    0..7
                                                             result operand
              void* ptrBase;
              void* ptrModify;
C example     vec_t vRes;
              ...
              vRes = vlddw_indexed_rIp_v32_clone_8dw_intrlv (ptrBase, ptrModify, LOW, 0);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_pm_imm_v32_clone_8dw_intrlv
name          vlddw_pm_imm_v32_str1_8dw_intrlv

Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (pN)+#imm32_6, viz[Z] [,?prSC]

Return type   vec_t

              1    IN1_PTR         void *                    Pointer register (rN)
Operands                                      31    31       32 bit immediate post modification in
              2    IN2_IMM32_6 int32         -2 ..2 -1
                                                             bytes
                                                             Offset for the first DW used from the
              3    OUT_OFST        uint8    0..7
                                                             result operand
              void* ptr;
              vec_t vRes;
C example     ...
              vRes = vlddw_pm_imm_v32_clone_8dw_intrlv (ptr, 2, 0);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_pm_ptr_v32_clone_8dw_intrlv
name          vlddw_pm_ptr_v32_str1_8dw_intrlv

Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (pN)[+pm_x], viz[Z] [,?prSC]

Return type   vec_t

              1    IN1_PTR        void *                     Pointer register (rN)
              2    IN2_PM_PTR void*                          Pointer register (rN)
Operands
                                                             Offset for the first DW used from the
              3    OUT_OFST       uint8     0..7
                                                             result operand
              void* ptr;
              void* vRes;
C example     ...
              ptr = vlddw_pm_ptr_v32_clone_8dw_intrlv (ptr, vRes, 0);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_v32_clone_8dw_intrlv
name          vlddw_v32_str1_8dw_intrlv

Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (pN)[+pm_x], viz[Z] [,?prSC]

Return type   vec_t

              1    IN1_PTR        void *                     Pointer register (rN)
Operands                                                     Offset for the first DW used from the
              2    OUT_OFST       uint8     0..7
                                                             result operand
              void* ptr;
              vec_t vRes;
C example     ...
              vRes = vlddw_v32_clone_8dw_intrlv (ptr, 0);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).

Main table → Memory Access → Load → Load DW into 32 bit register
Available addressing modes
Intrinsic Names:
vlddw_direct_v32_clone_8dw_intrlv_int2dw
vlddw_indexed_imm_v32_clone_8dw_intrlv_int2dw
vlddw_indexed_rI_pm_imm_v32_clone_8dw_intrlv_int2dw
vlddw_indexed_rI_pm_ptr_v32_clone_8dw_intrlv_int2dw
vlddw_indexed_rI_v32_clone_8dw_intrlv_int2dw
vlddw_indexed_rIp_pm_imm_v32_clone_8dw_intrlv_int2dw
vlddw_indexed_rIp_pm_ptr_v32_clone_8dw_intrlv_int2dw
vlddw_indexed_rIp_v32_clone_8dw_intrlv_int2dw
vlddw_pm_imm_v32_clone_8dw_intrlv_int2dw
vlddw_pm_ptr_v32_clone_8dw_intrlv_int2dw
vlddw_v32_clone_8dw_intrlv_int2dw
Intrinsic     vlddw_direct_v32_clone_8dw_intrlv_int2dw
name          vlddw_direct_v32_str1_8dw_intrlv_int2dw

Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX]} [#address], viz[Z] [,?prSC]

Return type   vec_t
                                                    32
              1    IN1_ADDR       int32      0..2 -1         32 bit address
Operands                                                     Offset for the first DW used from the
              2    OUT_OFST       uint8      0..7
                                                             result operand
              vec_t vRes;
C example     ...
              vRes = vlddw_direct_v32_clone_8dw_intrlv_int2dw (2, 0);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_indexed_imm_v32_clone_8dw_intrlv_int2dw
name          vlddw_indexed_imm_v32_str1_8dw_intrlv_int2dw

Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+#imm16_6), viz[Z] [,?prSC]

Return type   vec_t

              1    IN1_gB_BASE void *                        Pointer register (gB)

16 bit immediate post modification in
              2    IN2_IMM16_6     int16     -32768..32767
Operands                                                     bytes
                                                             Offset for the first DW used from the
              3    OUT_OFST        uint8     0..7
                                                             result operand
              void* ptrBase;
              vec_t vRes;
C example     ...
              vRes = vlddw_indexed_imm_v32_clone_8dw_intrlv_int2dw (ptrBase, 2, 0);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_indexed_rI_pm_imm_v32_clone_8dw_intrlv_int2dw
name          vlddw_indexed_rI_pm_imm_v32_str1_8dw_intrlv_int2dw

Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+rI)[+pm], viz[Z] [,?prSC]

Return type   vec_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
Operands                                                     Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
                                               31   31       32 bit immediate post modification in
              3    IN3_PM_IMM       int32    -2 ..2 -1
                                                             bytes
                                                             Offset for the first DW used from the
              4    OUT_OFST         uint8    0..7
                                                             result operand
              void* ptrBase;
              void* ptrModify;
C example     vec_t vRes;
              ...
              vRes = vlddw_indexed_rI_pm_imm_v32_clone_8dw_intrlv_int2dw (ptrBase, ptrModify, 2, 0);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_indexed_rI_pm_ptr_v32_clone_8dw_intrlv_int2dw
name          vlddw_indexed_rI_pm_ptr_v32_str1_8dw_intrlv_int2dw

Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+rI)[+pm], viz[Z] [,?prSC]

Return type   vec_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the

2    IN2_rI_OFFSET void *
                                                             base pointer
Operands
              3    IN3_PM_PTR       void*                    Pointer register (rN)
                                                             Offset for the first DW used from the
              4    OUT_OFST         uint8    0..7
                                                             result operand
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec_t vRes;
              ...
              vRes = vlddw_indexed_rI_pm_ptr_v32_clone_8dw_intrlv_int2dw (ptrBase, ptrModify, ptr, 0);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_indexed_rI_v32_clone_8dw_intrlv_int2dw
name          vlddw_indexed_rI_v32_str1_8dw_intrlv_int2dw

Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+rI)[+pm], viz[Z] [,?prSC]

Return type   vec_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
Operands                                                     Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
                                                             Offset for the first DW used from the
              3    OUT_OFST         uint8    0..7
                                                             result operand
              void* ptrBase;
              void* ptrModify;
C example     vec_t vRes;
              ...
              vRes = vlddw_indexed_rI_v32_clone_8dw_intrlv_int2dw (ptrBase, ptrModify, 0);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_indexed_rIp_pm_imm_v32_clone_8dw_intrlv_int2dw
name          vlddw_indexed_rIp_pm_imm_v32_str1_8dw_intrlv_int2dw

Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+rIp)[+pm], viz[Z] [,?prSC]

Return type   vec_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer

3    IN2_PART         uint8    LOW,HIGH        Word part which is used for operand 2
Operands
                                               31   31       32 bit immediate post modification in
              4    IN3_PM_IMM       int32    -2 ..2 -1
                                                             bytes
                                                             Offset for the first DW used from the
              5    OUT_OFST         uint8    0..7
                                                             result operand
              void* ptrBase;
              void* ptrModify;
C example     vec_t vRes;
              ...
              vRes = vlddw_indexed_rIp_pm_imm_v32_clone_8dw_intrlv_int2dw (ptrBase, ptrModify, LOW, 2, 0);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_indexed_rIp_pm_ptr_v32_clone_8dw_intrlv_int2dw
name          vlddw_indexed_rIp_pm_ptr_v32_str1_8dw_intrlv_int2dw

Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+rIp)[+pm], viz[Z] [,?prSC]

Return type   vec_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
Operands                                                     Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
              3    IN2_PART         uint8    LOW,HIGH        Word part which is used for operand 2
              4    IN3_PM_PTR       void*                    Pointer register (rN)

              5
                                                             Offset for the first DW used from the
                   OUT_OFST         uint8    0..7
                                                             result operand
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec_t vRes;
              ...
              vRes = vlddw_indexed_rIp_pm_ptr_v32_clone_8dw_intrlv_int2dw (ptrBase, ptrModify, LOW, ptr, 0);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_indexed_rIp_v32_clone_8dw_intrlv_int2dw
name          vlddw_indexed_rIp_v32_str1_8dw_intrlv_int2dw

Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+rIp)[+pm], viz[Z] [,?prSC]

Return type   vec_t

1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
Operands
              3    IN2_PART         uint8    LOW,HIGH        Word part which is used for operand 2
                                                             Offset for the first DW used from the
              4    OUT_OFST         uint8    0..7
                                                             result operand
              void* ptrBase;
              void* ptrModify;
C example     vec_t vRes;
              ...
              vRes = vlddw_indexed_rIp_v32_clone_8dw_intrlv_int2dw (ptrBase, ptrModify, LOW, 0);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_pm_imm_v32_clone_8dw_intrlv_int2dw
name          vlddw_pm_imm_v32_str1_8dw_intrlv_int2dw

Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (pN)+#imm32_6, viz[Z] [,?prSC]

Return type   vec_t

              1    IN1_PTR         void *                   Pointer register (rN)
Operands                                      31    31      32 bit immediate post modification in
              2    IN2_IMM32_6 int32         -2 ..2 -1
                                                            bytes
                                                             Offset for the first DW used from the
              3    OUT_OFST       uint8     0..7
                                                             result operand
              void* ptr;
              vec_t vRes;
C example     ...
              vRes = vlddw_pm_imm_v32_clone_8dw_intrlv_int2dw (ptr, 2, 0);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_pm_ptr_v32_clone_8dw_intrlv_int2dw
name          vlddw_pm_ptr_v32_str1_8dw_intrlv_int2dw

Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (pN)[+pm_x], viz[Z] [,?prSC]

Return type   vec_t

              1    IN1_PTR        void *                     Pointer register (rN)
              2    IN2_PM_PTR void*                          Pointer register (rN)
Operands

Offset for the first DW used from the
              3    OUT_OFST       uint8     0..7
                                                             result operand
              void* ptr;
              void* vRes;
C example     ...
              ptr = vlddw_pm_ptr_v32_clone_8dw_intrlv_int2dw (ptr, vRes, 0);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_v32_clone_8dw_intrlv_int2dw
name          vlddw_v32_str1_8dw_intrlv_int2dw

Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (pN)[+pm_x], viz[Z] [,?prSC]

Return type   vec_t

              1    IN1_PTR        void *                     Pointer register (rN)
Operands                                                     Offset for the first DW used from the
              2    OUT_OFST       uint8     0..7
                                                             result operand
              void* ptr;
              vec_t vRes;
C example     ...
              vRes = vlddw_v32_clone_8dw_intrlv_int2dw (ptr, 0);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).

Main table → Memory Access → Load → Load DW into 32 bit register
Available addressing modes
Intrinsic Names:
vlddw_indexed_imm_v32_clone_8dw_intrlv_int2dw_rowstr
vlddw_indexed_rI_pm_imm_v32_clone_8dw_intrlv_int2dw_rowstr
vlddw_indexed_rI_pm_ptr_v32_clone_8dw_intrlv_int2dw_rowstr
vlddw_indexed_rI_v32_clone_8dw_intrlv_int2dw_rowstr
vlddw_indexed_rIp_pm_imm_v32_clone_8dw_intrlv_int2dw_rowstr
vlddw_indexed_rIp_pm_ptr_v32_clone_8dw_intrlv_int2dw_rowstr
vlddw_indexed_rIp_v32_clone_8dw_intrlv_int2dw_rowstr
vlddw_pm_imm_v32_clone_8dw_intrlv_int2dw_rowstr
vlddw_pm_ptr_v32_clone_8dw_intrlv_int2dw_rowstr
vlddw_v32_clone_8dw_intrlv_int2dw_rowstr
Intrinsic     vlddw_indexed_imm_v32_clone_8dw_intrlv_int2dw_rowstr
name          vlddw_indexed_imm_v32_str1_8dw_intrlv_int2dw_rowstr

Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+#imm16_6), viz[Z] [,?prSC]

Return type   vec_t

              1    IN1_gB_BASE void *                        Pointer register (gB)
                                                             16 bit immediate post modification in
              2    IN2_IMM16_6     int16     -32768..32767
Operands                                                     bytes

Offset for the first DW used from the
              3    OUT_OFST        uint8     0..7
                                                             result operand
              void* ptrBase;
              vec_t vRes;
C example     ...
              vRes = vlddw_indexed_imm_v32_clone_8dw_intrlv_int2dw_rowstr (ptrBase, 2, 0);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_indexed_rI_pm_imm_v32_clone_8dw_intrlv_int2dw_rowstr
name          vlddw_indexed_rI_pm_imm_v32_str1_8dw_intrlv_int2dw_rowstr

Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+rI)[+pm], viz[Z] [,?prSC]

Return type   vec_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
Operands                                       31   31       32 bit immediate post modification in
              3    IN3_PM_IMM       int32    -2 ..2 -1
                                                             bytes
                                                             Offset for the first DW used from the
              4    OUT_OFST         uint8    0..7
                                                             result operand
              void* ptrBase;
              void* ptrModify;
C example     vec_t vRes;
              ...
              vRes = vlddw_indexed_rI_pm_imm_v32_clone_8dw_intrlv_int2dw_rowstr (ptrBase, ptrModify, 2, 0);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_indexed_rI_pm_ptr_v32_clone_8dw_intrlv_int2dw_rowstr
name          vlddw_indexed_rI_pm_ptr_v32_str1_8dw_intrlv_int2dw_rowstr
Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+rI)[+pm], viz[Z] [,?prSC]

Return type   vec_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
Operands
              3    IN3_PM_PTR       void*                    Pointer register (rN)

Offset for the first DW used from the
              4    OUT_OFST         uint8    0..7
                                                             result operand
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec_t vRes;
              ...
              vRes = vlddw_indexed_rI_pm_ptr_v32_clone_8dw_intrlv_int2dw_rowstr (ptrBase, ptrModify, ptr, 0);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_indexed_rI_v32_clone_8dw_intrlv_int2dw_rowstr
name          vlddw_indexed_rI_v32_str1_8dw_intrlv_int2dw_rowstr

Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+rI)[+pm], viz[Z] [,?prSC]

Return type   vec_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)

              2
                                                             Pointer (rI) specifying the offset from the
                   IN2_rI_OFFSET void *
Operands                                                     base pointer
                                                             Offset for the first DW used from the
              3    OUT_OFST         uint8    0..7
                                                             result operand
              void* ptrBase;
              void* ptrModify;
C example     vec_t vRes;
              ...
              vRes = vlddw_indexed_rI_v32_clone_8dw_intrlv_int2dw_rowstr (ptrBase, ptrModify, 0);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_indexed_rIp_pm_imm_v32_clone_8dw_intrlv_int2dw_rowstr
name          vlddw_indexed_rIp_pm_imm_v32_str1_8dw_intrlv_int2dw_rowstr

Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+rIp)[+pm], viz[Z] [,?prSC]

Return type   vec_t
              1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
              3    IN2_PART         uint8    LOW,HIGH        Word part which is used for operand 2
Operands
                                               31   31       32 bit immediate post modification in

4    IN3_PM_IMM       int32    -2 ..2 -1
                                                             bytes
                                                             Offset for the first DW used from the
              5    OUT_OFST         uint8    0..7
                                                             result operand
              void* ptrBase;
              void* ptrModify;
              vec_t vRes;
C example     ...
              vRes = vlddw_indexed_rIp_pm_imm_v32_clone_8dw_intrlv_int2dw_rowstr (ptrBase, ptrModify, LOW,
              2, 0);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_indexed_rIp_pm_ptr_v32_clone_8dw_intrlv_int2dw_rowstr
name          vlddw_indexed_rIp_pm_ptr_v32_str1_8dw_intrlv_int2dw_rowstr

Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+rIp)[+pm], viz[Z] [,?prSC]

Return type   vec_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
Operands      3    IN2_PART         uint8    LOW,HIGH        Word part which is used for operand 2
              4    IN3_PM_PTR       void*                    Pointer register (rN)

              5
                                                             Offset for the first DW used from the
                   OUT_OFST         uint8    0..7
                                                             result operand
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec_t vRes;
              ...
              vRes = vlddw_indexed_rIp_pm_ptr_v32_clone_8dw_intrlv_int2dw_rowstr (ptrBase, ptrModify, LOW,
              ptr, 0);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_indexed_rIp_v32_clone_8dw_intrlv_int2dw_rowstr
name          vlddw_indexed_rIp_v32_str1_8dw_intrlv_int2dw_rowstr

Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+rIp)[+pm], viz[Z] [,?prSC]

Return type   vec_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)

Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
Operands
              3    IN2_PART         uint8    LOW,HIGH        Word part which is used for operand 2
                                                             Offset for the first DW used from the
              4    OUT_OFST         uint8    0..7
                                                             result operand
              void* ptrBase;
              void* ptrModify;
C example     vec_t vRes;
              ...
              vRes = vlddw_indexed_rIp_v32_clone_8dw_intrlv_int2dw_rowstr (ptrBase, ptrModify, LOW, 0);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_pm_imm_v32_clone_8dw_intrlv_int2dw_rowstr
name          vlddw_pm_imm_v32_str1_8dw_intrlv_int2dw_rowstr

Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (pN)+#imm32_6, viz[Z] [,?prSC]

Return type   vec_t

              1    IN1_PTR         void *                   Pointer register (rN)
                                               31   31      32 bit immediate post modification in
              2    IN2_IMM32_6 int32         -2 ..2 -1
Operands                                                    bytes

              3
                                                            Offset for the first DW used from the
                   OUT_OFST        uint8     0..7
                                                            result operand
              void* ptr;
              vec_t vRes;
C example     ...
              vRes = vlddw_pm_imm_v32_clone_8dw_intrlv_int2dw_rowstr (ptr, 2, 0);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_pm_ptr_v32_clone_8dw_intrlv_int2dw_rowstr
name          vlddw_pm_ptr_v32_str1_8dw_intrlv_int2dw_rowstr

Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (pN)[+pm_x], viz[Z] [,?prSC]

Return type   vec_t
               1    IN1_PTR        void *                    Pointer register (rN)
               2    IN2_PM_PTR void*                         Pointer register (rN)
Operands
               3
                                                             Offset for the first DW used from the
                    OUT_OFST       uint8     0..7

result operand
               void* ptr;
               void* vRes;
C example      ...
               ptr = vlddw_pm_ptr_v32_clone_8dw_intrlv_int2dw_rowstr (ptr, vRes, 0);

                    The same data will be loaded to all vector units (Unless str1 is configured
Comments       1.
                    otherwise).



Intrinsic      vlddw_v32_clone_8dw_intrlv_int2dw_rowstr
name           vlddw_v32_str1_8dw_intrlv_int2dw_rowstr

Spec syntax    vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (pN)[+pm_x], viz[Z] [,?prSC]

Return type    vec_t

               1    IN1_PTR        void *                    Pointer register (rN)
Operands                                                     Offset for the first DW used from the
               2    OUT_OFST       uint8     0..7
                                                             result operand
               void* ptr;
               vec_t vRes;
C example      ...
               vRes = vlddw_v32_clone_8dw_intrlv_int2dw_rowstr (ptr, 0);

                    The same data will be loaded to all vector units (Unless str1 is configured
Comments       1.
                    otherwise).


Main table → Memory Access → Load → Load DW into 32 bit register
Available addressing modes
Intrinsic Names:
vlddw_indexed_imm_v32_clone_8dw_intrlv_rowstr
vlddw_indexed_rI_pm_imm_v32_clone_8dw_intrlv_rowstr
vlddw_indexed_rI_pm_ptr_v32_clone_8dw_intrlv_rowstr
vlddw_indexed_rI_v32_clone_8dw_intrlv_rowstr
vlddw_indexed_rIp_pm_imm_v32_clone_8dw_intrlv_rowstr
vlddw_indexed_rIp_pm_ptr_v32_clone_8dw_intrlv_rowstr
vlddw_indexed_rIp_v32_clone_8dw_intrlv_rowstr
vlddw_pm_imm_v32_clone_8dw_intrlv_rowstr
vlddw_pm_ptr_v32_clone_8dw_intrlv_rowstr
vlddw_v32_clone_8dw_intrlv_rowstr
Intrinsic     vlddw_indexed_imm_v32_clone_8dw_intrlv_rowstr
name          vlddw_indexed_imm_v32_str1_8dw_intrlv_rowstr

Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+#imm16_6), viz[Z] [,?prSC]

Return type   vec_t

              1    IN1_gB_BASE void *                        Pointer register (gB)
                                                             16 bit immediate post modification in
              2    IN2_IMM16_6     int16     -32768..32767
Operands                                                     bytes
                                                             Offset for the first DW used from the
              3    OUT_OFST        uint8     0..7
                                                             result operand

void* ptrBase;
              vec_t vRes;
C example     ...
              vRes = vlddw_indexed_imm_v32_clone_8dw_intrlv_rowstr (ptrBase, 2, 0);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_indexed_rI_pm_imm_v32_clone_8dw_intrlv_rowstr
name          vlddw_indexed_rI_pm_imm_v32_str1_8dw_intrlv_rowstr

Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+rI)[+pm], viz[Z] [,?prSC]

Return type   vec_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
Operands                                       31   31       32 bit immediate post modification in
              3    IN3_PM_IMM       int32    -2 ..2 -1
                                                             bytes
                                                             Offset for the first DW used from the
              4    OUT_OFST         uint8    0..7
                                                             result operand
              void* ptrBase;
              void* ptrModify;
C example     vec_t vRes;
              ...
              vRes = vlddw_indexed_rI_pm_imm_v32_clone_8dw_intrlv_rowstr (ptrBase, ptrModify, 2, 0);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_indexed_rI_pm_ptr_v32_clone_8dw_intrlv_rowstr
name          vlddw_indexed_rI_pm_ptr_v32_str1_8dw_intrlv_rowstr
Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+rI)[+pm], viz[Z] [,?prSC]

Return type   vec_t

              1    IN1_gB_BASE      void *                    Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                              base pointer
Operands
              3    IN3_PM_PTR       void*                     Pointer register (rN)
                                                              Offset for the first DW used from the
              4    OUT_OFST         uint8    0..7

result operand
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec_t vRes;
              ...
              vRes = vlddw_indexed_rI_pm_ptr_v32_clone_8dw_intrlv_rowstr (ptrBase, ptrModify, ptr, 0);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_indexed_rI_v32_clone_8dw_intrlv_rowstr
name          vlddw_indexed_rI_v32_str1_8dw_intrlv_rowstr

Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+rI)[+pm], viz[Z] [,?prSC]

Return type   vec_t

              1    IN1_gB_BASE      void *                    Pointer register (gB)

              2
                                                              Pointer (rI) specifying the offset from the
                   IN2_rI_OFFSET void *
Operands                                                      base pointer
                                                              Offset for the first DW used from the
              3    OUT_OFST         uint8    0..7
                                                              result operand
              void* ptrBase;
              void* ptrModify;
C example     vec_t vRes;
              ...
              vRes = vlddw_indexed_rI_v32_clone_8dw_intrlv_rowstr (ptrBase, ptrModify, 0);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_indexed_rIp_pm_imm_v32_clone_8dw_intrlv_rowstr
name          vlddw_indexed_rIp_pm_imm_v32_str1_8dw_intrlv_rowstr

Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+rIp)[+pm], viz[Z] [,?prSC]

Return type   vec_t
              1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
              3    IN2_PART         uint8    LOW,HIGH        Word part which is used for operand 2
Operands
                                               31   31       32 bit immediate post modification in
              4    IN3_PM_IMM       int32    -2 ..2 -1
                                                             bytes
                                                             Offset for the first DW used from the

5    OUT_OFST         uint8    0..7
                                                             result operand
              void* ptrBase;
              void* ptrModify;
C example     vec_t vRes;
              ...
              vRes = vlddw_indexed_rIp_pm_imm_v32_clone_8dw_intrlv_rowstr (ptrBase, ptrModify, LOW, 2, 0);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_indexed_rIp_pm_ptr_v32_clone_8dw_intrlv_rowstr
name          vlddw_indexed_rIp_pm_ptr_v32_str1_8dw_intrlv_rowstr

Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+rIp)[+pm], viz[Z] [,?prSC]

Return type   vec_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
Operands      3    IN2_PART         uint8    LOW,HIGH        Word part which is used for operand 2
              4    IN3_PM_PTR       void*                    Pointer register (rN)
                                                             Offset for the first DW used from the
              5    OUT_OFST         uint8    0..7
                                                             result operand
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec_t vRes;
              ...
              vRes = vlddw_indexed_rIp_pm_ptr_v32_clone_8dw_intrlv_rowstr (ptrBase, ptrModify, LOW, ptr, 0);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_indexed_rIp_v32_clone_8dw_intrlv_rowstr
name          vlddw_indexed_rIp_v32_str1_8dw_intrlv_rowstr
Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (gB+rIp)[+pm], viz[Z] [,?prSC]

Return type   vec_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
Operands
              3    IN2_PART         uint8    LOW,HIGH        Word part which is used for operand 2

Offset for the first DW used from the
              4    OUT_OFST         uint8    0..7
                                                             result operand
              void* ptrBase;
              void* ptrModify;
C example     vec_t vRes;
              ...
              vRes = vlddw_indexed_rIp_v32_clone_8dw_intrlv_rowstr (ptrBase, ptrModify, LOW, 0);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_pm_imm_v32_clone_8dw_intrlv_rowstr
name          vlddw_pm_imm_v32_str1_8dw_intrlv_rowstr

Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (pN)+#imm32_6, viz[Z] [,?prSC]

Return type   vec_t

              1    IN1_PTR         void *                   Pointer register (rN)
                                               31   31      32 bit immediate post modification in
              2    IN2_IMM32_6 int32         -2 ..2 -1
Operands                                                    bytes
                                                            Offset for the first DW used from the
              3    OUT_OFST        uint8     0..7
                                                            result operand
              void* ptr;
              vec_t vRes;
C example     ...
              vRes = vlddw_pm_imm_v32_clone_8dw_intrlv_rowstr (ptr, 2, 0);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_pm_ptr_v32_clone_8dw_intrlv_rowstr
name          vlddw_pm_ptr_v32_str1_8dw_intrlv_rowstr

Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (pN)[+pm_x], viz[Z] [,?prSC]

Return type   vec_t

Operands      1    IN1_PTR        void *                    Pointer register (rN)
              2    IN2_PM_PTR void*                          Pointer register (rN)
                                                             Offset for the first DW used from the
              3    OUT_OFST       uint8     0..7
                                                             result operand
              void* ptr;
              void* vRes;
C example     ...
              ptr = vlddw_pm_ptr_v32_clone_8dw_intrlv_rowstr (ptr, vRes, 0);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).

Intrinsic     vlddw_v32_clone_8dw_intrlv_rowstr
name          vlddw_v32_str1_8dw_intrlv_rowstr

Spec syntax   vlddw {8dw, intrlv [,int2dw][,strX][,rowstr]} (pN)[+pm_x], viz[Z] [,?prSC]

Return type   vec_t

              1    IN1_PTR        void *                     Pointer register (rN)
Operands                                                     Offset for the first DW used from the
              2    OUT_OFST       uint8     0..7
                                                             result operand
              void* ptr;
              vec_t vRes;
C example     ...
              vRes = vlddw_v32_clone_8dw_intrlv_rowstr (ptr, 0);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).


Main table → Memory Access → Load → Load DW into 32 bit register
Available addressing modes
Intrinsic Names:
vlddw_pm_imm_v32_vuX
vlddw_pm_ptr_v32_vuX
vlddw_v32_vuX
Intrinsic   vlddw_pm_imm_v32_vuX
name
Spec        vlddw {mdw, vuX} (pN)[+pm_x], viz[Z] [,?prSC]
syntax
Return      vec_t
type
                                                            Determines the element size and number
                              MDW_options
            1   MDW
                              enum                          of loaded elements (see enum definition
                                                            at vec-mem-modes.h)
            2   VUX           uint8           0..3          Determines the destination VCU
Operands    3   IN1_PTR       void *                        Pointer register (rN)
                                                31   31     32 bit immediate post modification in
            4   IN2_PM_IMM int32              -2 ..2 -1
                                                            bytes
                                                            Offset for the first DW used from the
            5   OUT_OFST      uint8           0..7
                                                            result operand
            vec_t 2;
            void* ptr;
C example   ...
            2 = vlddw_pm_imm_v32_vuX (mdw_8dw, 1, ptr, vRes, 0);

Comments



Intrinsic   vlddw_pm_ptr_v32_vuX
name
Spec        vlddw {mdw, vuX} (pN)[+pm_x], viz[Z] [,?prSC]
syntax
Return      vec_t
type
                                                            Determines the element size and number
                             MDW_options
            1 MDW

enum                           of loaded elements (see enum definition
                                                            at vec-mem-modes.h)
            2 VUX            uint8           0..3           Determines the destination VCU
Operands    3 IN1_PTR        void *                         Pointer register (rN)
            4 IN2_PM_PTR void*                              Pointer register (rN)
                                                            Offset for the first DW used from the
            5 OUT_OFST       uint8           0..7
                                                            result operand
            void* ptr;
C example   void* vRes;
            ...
            ptr = vlddw_pm_ptr_v32_vuX (mdw_8dw, 1, ptr, vRes, 0);

Comments



Intrinsic   vlddw_v32_vuX
name
Spec        vlddw {mdw, vuX} (pN)[+pm_x], viz[Z] [,?prSC]
syntax
Return      vec_t
type
                                                             Determines the element size and number
                              MDW_options
            1   MDW
                              enum                           of loaded elements (see enum definition
                                                             at vec-mem-modes.h)

Operands    2   VUX           uint8           0..3           Determines the destination VCU
            3   IN1_PTR       void *                         Pointer register (rN)
                                                             Offset for the first DW used from the
            4   OUT_OFST uint8                0..7
                                                             result operand
            void* ptr;
            vec_t vRes;
C example   ...
            vRes = vlddw_v32_vuX (mdw_8dw, 1, ptr, 0);

Comments


Main table → Memory Access → Load → Load DW into 32 bit register
