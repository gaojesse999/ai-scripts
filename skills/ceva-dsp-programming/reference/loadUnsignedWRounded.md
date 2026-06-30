# Memory Access → Load → Load unsigned W rounded

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Memory Access → Load → Load unsigned W rounded

Load unsigned W rounded

Load unsigned W rounded

Load unsigned 16 bit with rounding. Each result which is written is zero-extended instead of
sign-extended. In addition, each result which is written, the low part is written with 0x8000
Available Switches
2w          Two word loads
4w          Four word loads
dup         The data brought from the memory is duplicated
ew          Number of word loads. ew can be 2w, 4w, 6w or 8w
            Rounding constant. When used, each voz[Z]h which is written, the low part is written
r
            with 0x8000
            When row stride mechanism enabled - the row stride values are taken from ROWSTR0
rowstr
            or ROWSTR1 located under mod4 mode register.
strX        Selects the STR, PMSTR set within mod1 register and ROWSTR at mod4 register.
            When used, each voz[Z] which is written is zero-extended instead of sign-extended (the
u
            default is sign-extension)
            When 'unpk' switch is used 16w words of data are brought from the memory and
unpk
            unpacked into the two vector destinations - each vector is unpacked from 8w.
vuX         Determines the destination VCU of the instruction. X is replaced by 0 or 1.
Intrinsic Names
vldw_v40_clone_u_r
vldw_v40_clone_u_r_rowstr
vldw_v40_u_r
vldw_v40_u_r_rowstr
vldw_v40_2w_dup_u_r
vldw_v40_2w_dup_u_r_rowstr
vldw_v40_4w_dup_u_r
vldw_v40_4w_dup_u_r_rowstr
vldw_v40_clone_2w_dup_u_r
vldw_v40_clone_2w_dup_u_r_rowstr
vldw_v40_clone_4w_dup_u_r
vldw_v40_clone_4w_dup_u_r_rowstr
vldw_v40_v40_8w_unpk_u_r
vldw_v40_v40_8w_unpk_u_r_rowstr
vldw_v40_v40_clone_8w_unpk_u_r
vldw_v40_v40_clone_8w_unpk_u_r_rowstr
vldw_v40_vuX_u_r
Instruction details in the instruction set specification
Available addressing modes
Intrinsic Names:
vldw_direct_v40_clone_u_r
vldw_indexed_imm_v40_clone_u_r
vldw_indexed_rI_pm_imm_v40_clone_u_r
vldw_indexed_rI_pm_ptr_v40_clone_u_r
vldw_indexed_rI_v40_clone_u_r
vldw_indexed_rIp_pm_imm_v40_clone_u_r
vldw_indexed_rIp_pm_ptr_v40_clone_u_r
vldw_indexed_rIp_v40_clone_u_r
vldw_pm_imm_v40_clone_u_r
vldw_pm_ptr_v40_clone_u_r
vldw_v40_clone_u_r
Intrinsic     vldw_direct_v40_clone_u_r
name          vldw_direct_v40_str1_u_r

Spec syntax   vldw {ew [,u][,r_sw][,strX]} [#address], voz[0]h [,?prSC]

Return        vec40_t
type
                                                               Determines the element size and number
                                 EW_options
              1    EW

enum                          of loaded elements (see enum definition
Operands                                                       at vec-mem-modes.h)
                                                   32
              2    IN1_ADDR      int32         0..2 -1         32 bit address
              vec40_t vRes;
C example     ...
              vRes = vldw_direct_v40_clone_u_r (ew_8w, 2);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_imm_v40_clone_u_r
name          vldw_indexed_imm_v40_str1_u_r

Spec          vldw {ew [,u][,r_sw][,strX][,rowstr]} (gB+#imm16_6), voz[0]h [,?prSC]
syntax
Return        vec40_t
type
                                                               Determines the element size and number
                                  EW_options
              1    EW
                                  enum                         of loaded elements (see enum definition
                                                               at vec-mem-modes.h)
Operands      2    IN1_gB_BASE void *                          Pointer register (gB)
                                                -              16 bit immediate post modification in
              3    IN2_IMM16_6    int16
                                                32768..32767   bytes
              void* ptrBase;
              vec40_t vRes;
C example     ...
              vRes = vldw_indexed_imm_v40_clone_u_r (ew_8w, ptrBase, 2);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_rI_pm_imm_v40_clone_u_r
name          vldw_indexed_rI_pm_imm_v40_str1_u_r

Spec          vldw {ew [,u][,r_sw][,strX][,rowstr]} (gB+rI)[+pm], voz[0]h [,?prSC]
syntax
Return      vec40_t
type
                                                              Determines the element size and number
                                 EW_options
            1    EW
                                 enum                         of loaded elements (see enum definition
                                                              at vec-mem-modes.h)
            2    IN1_gB_BASE     void *                       Pointer register (gB)
Operands
                                                              Pointer (rI) specifying the offset from the
            3    IN2_rI_OFFSET void *

base pointer
                                                 31   31      32 bit immediate post modification in
            4    IN3_PM_IMM      int32         -2 ..2 -1
                                                              bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vRes;
            ...
            vRes = vldw_indexed_rI_pm_imm_v40_clone_u_r (ew_8w, ptrBase, ptrModify, 2);

                 The same data will be loaded to all vector units (Unless str1 is configured
Comments    1.
                 otherwise).



Intrinsic   vldw_indexed_rI_pm_ptr_v40_clone_u_r
name        vldw_indexed_rI_pm_ptr_v40_str1_u_r

Spec        vldw {ew [,u][,r_sw][,strX][,rowstr]} (gB+rI)[+pm], voz[0]h [,?prSC]
syntax
Return      vec40_t
type
                                                              Determines the element size and number
                                 EW_options
            1    EW
                                 enum                         of loaded elements (see enum definition
                                                              at vec-mem-modes.h)
Operands    2    IN1_gB_BASE     void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            3    IN2_rI_OFFSET void *
                                                              base pointer
            4    IN3_PM_PTR      void*                        Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vRes;
            ...
            vRes = vldw_indexed_rI_pm_ptr_v40_clone_u_r (ew_8w, ptrBase, ptrModify, ptr);

                 The same data will be loaded to all vector units (Unless str1 is configured
Comments    1.
                 otherwise).
Intrinsic   vldw_indexed_rI_v40_clone_u_r
name        vldw_indexed_rI_v40_str1_u_r

Spec        vldw {ew [,u][,r_sw][,strX][,rowstr]} (gB+rI)[+pm], voz[0]h [,?prSC]
syntax
Return      vec40_t
type
                                                              Determines the element size and number
                                 EW_options
            1    EW
                                 enum                         of loaded elements (see enum definition
                                                              at vec-mem-modes.h)
Operands    2    IN1_gB_BASE     void *                       Pointer register (gB)

Pointer (rI) specifying the offset from the
            3    IN2_rI_OFFSET void *
                                                              base pointer
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vRes;
            ...
            vRes = vldw_indexed_rI_v40_clone_u_r (ew_8w, ptrBase, ptrModify);

                 The same data will be loaded to all vector units (Unless str1 is configured
Comments    1.
                 otherwise).



Intrinsic   vldw_indexed_rIp_pm_imm_v40_clone_u_r
name        vldw_indexed_rIp_pm_imm_v40_str1_u_r

Spec        vldw {ew [,u][,r_sw][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]h [,?prSC]
syntax
Return      vec40_t
type
                                                              Determines the element size and number
                                 EW_options
            1    EW
                                 enum                         of loaded elements (see enum definition
                                                              at vec-mem-modes.h)
            2    IN1_gB_BASE     void *                       Pointer register (gB)
Operands                                                      Pointer (rI) specifying the offset from the
            3    IN2_rI_OFFSET void *
                                                              base pointer
            4    IN2_PART        uint8         LOW,HIGH       Word part which is used for operand 3
                                                 31   31      32 bit immediate post modification in
            5    IN3_PM_IMM      int32         -2 ..2 -1
                                                              bytes
            void* ptrBase;
C example   void* ptrModify;
            vec40_t vRes;
            ...
            vRes = vldw_indexed_rIp_pm_imm_v40_clone_u_r (ew_8w, ptrBase, ptrModify, HIGH, 2);

                 The same data will be loaded to all vector units (Unless str1 is configured
Comments    1.
                 otherwise).



Intrinsic   vldw_indexed_rIp_pm_ptr_v40_clone_u_r
name        vldw_indexed_rIp_pm_ptr_v40_str1_u_r

Spec        vldw {ew [,u][,r_sw][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]h [,?prSC]
syntax
Return      vec40_t
type
                                                             Determines the element size and number
                                 EW_options
            1    EW
                                 enum                        of loaded elements (see enum definition

at vec-mem-modes.h)
            2    IN1_gB_BASE     void *                      Pointer register (gB)
Operands
                                                             Pointer (rI) specifying the offset from the
            3    IN2_rI_OFFSET void *
                                                             base pointer
            4    IN2_PART        uint8         LOW,HIGH      Word part which is used for operand 3
            5    IN3_PM_PTR      void*                       Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vRes;
            ...
            vRes = vldw_indexed_rIp_pm_ptr_v40_clone_u_r (ew_8w, ptrBase, ptrModify, HIGH, ptr);

                 The same data will be loaded to all vector units (Unless str1 is configured
Comments    1.
                 otherwise).



Intrinsic   vldw_indexed_rIp_v40_clone_u_r
name        vldw_indexed_rIp_v40_str1_u_r

Spec        vldw {ew [,u][,r_sw][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]h [,?prSC]
syntax
Return      vec40_t
type
                                                             Determines the element size and number
                                 EW_options
Operands    1    EW
                                 enum                        of loaded elements (see enum definition
                                                             at vec-mem-modes.h)
            2    IN1_gB_BASE     void *                      Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            3    IN2_rI_OFFSET void *
                                                             base pointer
            4    IN2_PART        uint8         LOW,HIGH      Word part which is used for operand 3
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vRes;
            ...
            vRes = vldw_indexed_rIp_v40_clone_u_r (ew_8w, ptrBase, ptrModify, HIGH);

                 The same data will be loaded to all vector units (Unless str1 is configured
Comments    1.
                 otherwise).



Intrinsic   vldw_pm_imm_v40_clone_u_r
name        vldw_pm_imm_v40_str1_u_r

Spec        vldw {ew [,u][,r_sw][,strX][,rowstr]} (pN)+#imm32_6, voz[0]h [,?prSC]
syntax
Return      vec40_t
type
                                                             Determines the element size and number
                               EW_options
            1    EW

enum                          of loaded elements (see enum definition
                                                             at vec-mem-modes.h)
Operands    2    IN1_PTR       void *                        Pointer register (rN)
                                                31   31      32 bit immediate post modification in
            3    IN2_IMM32_6 int32            -2 ..2 -1
                                                             bytes
            void* ptr;
            vec40_t vRes;
C example   ...
            vRes = vldw_pm_imm_v40_clone_u_r (ew_8w, ptr, 2);

                 The same data will be loaded to all vector units (Unless str1 is configured
Comments    1.
                 otherwise).



Intrinsic   vldw_pm_ptr_v40_clone_u_r
name        vldw_pm_ptr_v40_str1_u_r

Spec        vldw {ew [,u][,r_sw][,strX][,rowstr]} (pN)[+pm_x], voz[0]h [,?prSC]
syntax
Return      vec40_t
type
                               EW_options
Operands    1    EW
                               enum                          Determines the element size and number
                                                               of loaded elements (see enum definition
                                                               at vec-mem-modes.h)
              2    IN1_PTR       void *                        Pointer register (rN)
              3    IN2_PM_PTR void*                            Pointer register (rN)
              void* ptr;
              void* vRes;
C example     ...
              ptr = vldw_pm_ptr_v40_clone_u_r (ew_8w, ptr, vRes);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_v40_clone_u_r
name          vldw_v40_str1_u_r

Spec syntax   vldw {ew [,u][,r_sw][,strX][,rowstr]} (pN)[+pm_x], voz[0]h [,?prSC]

Return        vec40_t
type
                                                              Determines the element size and number
                                EW_options
              1    EW
                                enum                          of loaded elements (see enum definition
Operands                                                      at vec-mem-modes.h)
              2    IN1_PTR      void *                        Pointer register (rN)
              void* ptr;
              vec40_t vRes;
C example     ...
              vRes = vldw_v40_clone_u_r (ew_8w, ptr);

The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).


Main table → Memory Access → Load → Load unsigned W rounded
Available addressing modes
Intrinsic Names:
vldw_indexed_imm_v40_clone_u_r_rowstr
vldw_indexed_rI_pm_imm_v40_clone_u_r_rowstr
vldw_indexed_rI_pm_ptr_v40_clone_u_r_rowstr
vldw_indexed_rI_v40_clone_u_r_rowstr
vldw_indexed_rIp_pm_imm_v40_clone_u_r_rowstr
vldw_indexed_rIp_pm_ptr_v40_clone_u_r_rowstr
vldw_indexed_rIp_v40_clone_u_r_rowstr
vldw_pm_imm_v40_clone_u_r_rowstr
vldw_pm_ptr_v40_clone_u_r_rowstr
vldw_v40_clone_u_r_rowstr
Intrinsic   vldw_indexed_imm_v40_clone_u_r_rowstr
name        vldw_indexed_imm_v40_str1_u_r_rowstr

Spec        vldw {ew [,u][,r_sw][,strX][,rowstr]} (gB+#imm16_6), voz[0]h [,?prSC]
syntax
Return      vec40_t
type
                                                             Determines the element size and number
                                EW_options
            1    EW
                                enum                         of loaded elements (see enum definition
                                                             at vec-mem-modes.h)
Operands    2    IN1_gB_BASE void *                          Pointer register (gB)
                                              -              16 bit immediate post modification in
            3    IN2_IMM16_6    int16
                                              32768..32767   bytes
            void* ptrBase;
            vec40_t vRes;
C example   ...
            vRes = vldw_indexed_imm_v40_clone_u_r_rowstr (ew_8w, ptrBase, 2);

                 The same data will be loaded to all vector units (Unless str1 is configured
Comments    1.
                 otherwise).



Intrinsic   vldw_indexed_rI_pm_imm_v40_clone_u_r_rowstr
name        vldw_indexed_rI_pm_imm_v40_str1_u_r_rowstr

Spec        vldw {ew [,u][,r_sw][,strX][,rowstr]} (gB+rI)[+pm], voz[0]h [,?prSC]
syntax
Return      vec40_t
type
                                                             Determines the element size and number
                                 EW_options
            1    EW
                                 enum                        of loaded elements (see enum definition
                                                             at vec-mem-modes.h)
            2    IN1_gB_BASE     void *                      Pointer register (gB)
Operands

Pointer (rI) specifying the offset from the
            3    IN2_rI_OFFSET void *
                                                             base pointer
                                                 31   31     32 bit immediate post modification in
            4    IN3_PM_IMM      int32         -2 ..2 -1
                                                             bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vRes;
            ...
            vRes = vldw_indexed_rI_pm_imm_v40_clone_u_r_rowstr (ew_8w, ptrBase, ptrModify, 2);

Comments    1.   The same data will be loaded to all vector units (Unless str1 is configured
                 otherwise).



Intrinsic   vldw_indexed_rI_pm_ptr_v40_clone_u_r_rowstr
name        vldw_indexed_rI_pm_ptr_v40_str1_u_r_rowstr

Spec        vldw {ew [,u][,r_sw][,strX][,rowstr]} (gB+rI)[+pm], voz[0]h [,?prSC]
syntax
Return      vec40_t
type
                                                              Determines the element size and number
                                 EW_options
            1    EW
                                 enum                         of loaded elements (see enum definition
                                                              at vec-mem-modes.h)

Operands    2    IN1_gB_BASE     void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            3    IN2_rI_OFFSET void *
                                                              base pointer
            4    IN3_PM_PTR      void*                        Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vRes;
            ...
            vRes = vldw_indexed_rI_pm_ptr_v40_clone_u_r_rowstr (ew_8w, ptrBase, ptrModify, ptr);

                 The same data will be loaded to all vector units (Unless str1 is configured
Comments    1.
                 otherwise).



Intrinsic   vldw_indexed_rI_v40_clone_u_r_rowstr
name        vldw_indexed_rI_v40_str1_u_r_rowstr

Spec        vldw {ew [,u][,r_sw][,strX][,rowstr]} (gB+rI)[+pm], voz[0]h [,?prSC]
syntax
Return      vec40_t
type
                                                              Determines the element size and number
                                 EW_options
            1    EW
                                 enum                         of loaded elements (see enum definition

at vec-mem-modes.h)
Operands    2    IN1_gB_BASE     void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            3    IN2_rI_OFFSET void *
                                                              base pointer
            void* ptrBase;
C example   void* ptrModify;
            vec40_t vRes;
            ...
            vRes = vldw_indexed_rI_v40_clone_u_r_rowstr (ew_8w, ptrBase, ptrModify);

                 The same data will be loaded to all vector units (Unless str1 is configured
Comments    1.
                 otherwise).



Intrinsic   vldw_indexed_rIp_pm_imm_v40_clone_u_r_rowstr
name        vldw_indexed_rIp_pm_imm_v40_str1_u_r_rowstr

Spec        vldw {ew [,u][,r_sw][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]h [,?prSC]
syntax
Return      vec40_t
type
                                                              Determines the element size and number
                                 EW_options
            1    EW
                                 enum                         of loaded elements (see enum definition
                                                              at vec-mem-modes.h)
            2    IN1_gB_BASE     void *                       Pointer register (gB)
Operands                                                      Pointer (rI) specifying the offset from the
            3    IN2_rI_OFFSET void *
                                                              base pointer
            4    IN2_PART        uint8         LOW,HIGH       Word part which is used for operand 3
                                                 31   31      32 bit immediate post modification in
            5    IN3_PM_IMM      int32         -2 ..2 -1
                                                              bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vRes;
            ...
            vRes = vldw_indexed_rIp_pm_imm_v40_clone_u_r_rowstr (ew_8w, ptrBase, ptrModify, HIGH, 2);

                 The same data will be loaded to all vector units (Unless str1 is configured
Comments    1.
                 otherwise).



Intrinsic   vldw_indexed_rIp_pm_ptr_v40_clone_u_r_rowstr
name        vldw_indexed_rIp_pm_ptr_v40_str1_u_r_rowstr

Spec        vldw {ew [,u][,r_sw][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]h [,?prSC]
syntax
Return      vec40_t
type

Determines the element size and number
                                 EW_options
Operands    1    EW
                                 enum                         of loaded elements (see enum definition
                                                              at vec-mem-modes.h)
            2    IN1_gB_BASE     void *                      Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            3    IN2_rI_OFFSET void *
                                                             base pointer
            4    IN2_PART        uint8         LOW,HIGH      Word part which is used for operand 3
            5    IN3_PM_PTR      void*                       Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vRes;
            ...
            vRes = vldw_indexed_rIp_pm_ptr_v40_clone_u_r_rowstr (ew_8w, ptrBase, ptrModify, HIGH, ptr);

                 The same data will be loaded to all vector units (Unless str1 is configured
Comments    1.
                 otherwise).



Intrinsic   vldw_indexed_rIp_v40_clone_u_r_rowstr
name        vldw_indexed_rIp_v40_str1_u_r_rowstr

Spec        vldw {ew [,u][,r_sw][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]h [,?prSC]
syntax
Return      vec40_t
type
                                                             Determines the element size and number
                                 EW_options
            1    EW
                                 enum                        of loaded elements (see enum definition
                                                             at vec-mem-modes.h)

Operands    2    IN1_gB_BASE     void *                      Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            3    IN2_rI_OFFSET void *
                                                             base pointer
            4    IN2_PART        uint8         LOW,HIGH      Word part which is used for operand 3
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vRes;
            ...
            vRes = vldw_indexed_rIp_v40_clone_u_r_rowstr (ew_8w, ptrBase, ptrModify, HIGH);

                 The same data will be loaded to all vector units (Unless str1 is configured
Comments    1.
                 otherwise).



Intrinsic   vldw_pm_imm_v40_clone_u_r_rowstr

name        vldw_pm_imm_v40_str1_u_r_rowstr

Spec        vldw {ew [,u][,r_sw][,strX][,rowstr]} (pN)+#imm32_6, voz[0]h [,?prSC]
syntax
Return        vec40_t
type
                                                              Determines the element size and number
                                 EW_options
              1    EW
                                 enum                         of loaded elements (see enum definition
                                                              at vec-mem-modes.h)
Operands      2    IN1_PTR       void *                       Pointer register (rN)
                                                 31   31      32 bit immediate post modification in
              3    IN2_IMM32_6 int32           -2 ..2 -1
                                                              bytes
              void* ptr;
              vec40_t vRes;
C example     ...
              vRes = vldw_pm_imm_v40_clone_u_r_rowstr (ew_8w, ptr, 2);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_pm_ptr_v40_clone_u_r_rowstr
name          vldw_pm_ptr_v40_str1_u_r_rowstr

Spec          vldw {ew [,u][,r_sw][,strX][,rowstr]} (pN)[+pm_x], voz[0]h [,?prSC]
syntax
Return        vec40_t
type
                                                              Determines the element size and number
                                 EW_options
              1    EW
                                 enum                         of loaded elements (see enum definition
                                                              at vec-mem-modes.h)
Operands
              2    IN1_PTR       void *                       Pointer register (rN)
              3    IN2_PM_PTR void*                           Pointer register (rN)
              void* ptr;
              void* vRes;
C example     ...
              ptr = vldw_pm_ptr_v40_clone_u_r_rowstr (ew_8w, ptr, vRes);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_v40_clone_u_r_rowstr
name          vldw_v40_str1_u_r_rowstr

Spec syntax   vldw {ew [,u][,r_sw][,strX][,rowstr]} (pN)[+pm_x], voz[0]h [,?prSC]

Return        vec40_t
type
                                                               Determines the element size and number
                                EW_options
              1    EW

enum                           of loaded elements (see enum definition
Operands                                                       at vec-mem-modes.h)
              2    IN1_PTR      void *                         Pointer register (rN)
              void* ptr;
              vec40_t vRes;
C example     ...
              vRes = vldw_v40_clone_u_r_rowstr (ew_8w, ptr);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).


Main table → Memory Access → Load → Load unsigned W rounded
Available addressing modes
Intrinsic Names:
vldw_direct_v40_u_r
vldw_indexed_imm_v40_u_r
vldw_indexed_rI_pm_imm_v40_u_r
vldw_indexed_rI_pm_ptr_v40_u_r
vldw_indexed_rI_v40_u_r
vldw_indexed_rIp_pm_imm_v40_u_r
vldw_indexed_rIp_pm_ptr_v40_u_r
vldw_indexed_rIp_v40_u_r
vldw_pm_imm_v40_u_r
vldw_pm_ptr_v40_u_r
vldw_v40_u_r
Intrinsic     vldw_direct_v40_u_r
name
Spec syntax   vldw {ew [,u][,r_sw][,strX]} [#address], voz[0]h [,?prSC]

Return        vec40_t
type
                                                               Determines the element size and number
                                 EW_options
              1   EW
                                 enum                          of loaded elements (see enum definition
Operands                                                       at vec-mem-modes.h)
                                                   32
              2   IN1_ADDR       int32         0..2 -1         32 bit address
              vec40_t vRes;
C example     ...
              vRes = vldw_direct_v40_u_r (ew_8w, 2);

Comments



Intrinsic     vldw_indexed_imm_v40_u_r
name
Spec          vldw {ew [,u][,r_sw][,strX][,rowstr]} (gB+#imm16_6), voz[0]h [,?prSC]
syntax
Return        vec40_t
type
                                                               Determines the element size and number
                                  EW_options
              1   EW
                                  enum                         of loaded elements (see enum definition
                                                               at vec-mem-modes.h)
Operands      2   IN1_gB_BASE void *                           Pointer register (gB)
                                                -              16 bit immediate post modification in
              3   IN2_IMM16_6     int16
                                                32768..32767   bytes
              void* ptrBase;
              vec40_t vRes;

C example     ...
              vRes = vldw_indexed_imm_v40_u_r (ew_8w, ptrBase, 2);

Comments



Intrinsic     vldw_indexed_rI_pm_imm_v40_u_r
name
Spec          vldw {ew [,u][,r_sw][,strX][,rowstr]} (gB+rI)[+pm], voz[0]h [,?prSC]
syntax
Return        vec40_t
type
                                                              Determines the element size and number
                                 EW_options
            1 EW
                                 enum                         of loaded elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_gB_BASE        void *                       Pointer register (gB)
Operands
                                                              Pointer (rI) specifying the offset from the
            3 IN2_rI_OFFSET void *
                                                              base pointer
                                                 31   31      32 bit immediate post modification in
            4 IN3_PM_IMM         int32         -2 ..2 -1
                                                              bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vRes;
            ...
            vRes = vldw_indexed_rI_pm_imm_v40_u_r (ew_8w, ptrBase, ptrModify, 2);

Comments



Intrinsic   vldw_indexed_rI_pm_ptr_v40_u_r
name
Spec        vldw {ew [,u][,r_sw][,strX][,rowstr]} (gB+rI)[+pm], voz[0]h [,?prSC]
syntax
Return      vec40_t
type
                                                              Determines the element size and number
                                 EW_options
            1 EW
                                 enum                         of loaded elements (see enum definition
                                                              at vec-mem-modes.h)

Operands    2 IN1_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            3 IN2_rI_OFFSET void *
                                                              base pointer
            4 IN3_PM_PTR         void*                        Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vRes;
            ...
            vRes = vldw_indexed_rI_pm_ptr_v40_u_r (ew_8w, ptrBase, ptrModify, ptr);

Comments



Intrinsic   vldw_indexed_rI_v40_u_r
name

Spec        vldw {ew [,u][,r_sw][,strX][,rowstr]} (gB+rI)[+pm], voz[0]h [,?prSC]
syntax
Return      vec40_t
type
                                                              Determines the element size and number
                                 EW_options
            1 EW
                                 enum                         of loaded elements (see enum definition
                                                              at vec-mem-modes.h)
Operands    2 IN1_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            3 IN2_rI_OFFSET void *
                                                              base pointer
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vRes;
            ...
            vRes = vldw_indexed_rI_v40_u_r (ew_8w, ptrBase, ptrModify);

Comments



Intrinsic   vldw_indexed_rIp_pm_imm_v40_u_r
name
Spec        vldw {ew [,u][,r_sw][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]h [,?prSC]
syntax
Return      vec40_t
type
                                                              Determines the element size and number
                                 EW_options
            1 EW
                                 enum                         of loaded elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_gB_BASE        void *                       Pointer register (gB)
Operands                                                      Pointer (rI) specifying the offset from the
            3 IN2_rI_OFFSET void *
                                                              base pointer
            4 IN2_PART           uint8         LOW,HIGH       Word part which is used for operand 3
                                                 31   31      32 bit immediate post modification in
            5 IN3_PM_IMM         int32         -2 ..2 -1
                                                              bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vRes;
            ...
            vRes = vldw_indexed_rIp_pm_imm_v40_u_r (ew_8w, ptrBase, ptrModify, HIGH, 2);

Comments
Intrinsic   vldw_indexed_rIp_pm_ptr_v40_u_r
name
Spec        vldw {ew [,u][,r_sw][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]h [,?prSC]
syntax
Return      vec40_t
type

Determines the element size and number
                                EW_options
            1 EW
                                enum                         of loaded elements (see enum definition
                                                             at vec-mem-modes.h)
            2 IN1_gB_BASE       void *                       Pointer register (gB)
Operands
                                                             Pointer (rI) specifying the offset from the
            3 IN2_rI_OFFSET void *
                                                             base pointer
            4 IN2_PART          uint8          LOW,HIGH      Word part which is used for operand 3
            5 IN3_PM_PTR        void*                        Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vRes;
            ...
            vRes = vldw_indexed_rIp_pm_ptr_v40_u_r (ew_8w, ptrBase, ptrModify, HIGH, ptr);

Comments



Intrinsic   vldw_indexed_rIp_v40_u_r
name
Spec        vldw {ew [,u][,r_sw][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]h [,?prSC]
syntax
Return      vec40_t
type
                                                             Determines the element size and number
                                EW_options
            1 EW
                                enum                         of loaded elements (see enum definition
                                                             at vec-mem-modes.h)

Operands    2 IN1_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            3 IN2_rI_OFFSET void *
                                                             base pointer
            4 IN2_PART          uint8          LOW,HIGH      Word part which is used for operand 3
C example   void* ptrBase;
            void* ptrModify;
            vec40_t vRes;
            ...
            vRes = vldw_indexed_rIp_v40_u_r (ew_8w, ptrBase, ptrModify, HIGH);

Comments



Intrinsic   vldw_pm_imm_v40_u_r
name
Spec        vldw {ew [,u][,r_sw][,strX][,rowstr]} (pN)+#imm32_6, voz[0]h [,?prSC]
syntax
Return      vec40_t
type
                                                             Determines the element size and number
                               EW_options
            1   EW
                               enum                          of loaded elements (see enum definition

at vec-mem-modes.h)
Operands    2   IN1_PTR        void *                        Pointer register (rN)
                                                31   31      32 bit immediate post modification in
            3   IN2_IMM32_6 int32             -2 ..2 -1
                                                             bytes
            void* ptr;
            vec40_t vRes;
C example   ...
            vRes = vldw_pm_imm_v40_u_r (ew_8w, ptr, 2);

Comments



Intrinsic   vldw_pm_ptr_v40_u_r
name
Spec        vldw {ew [,u][,r_sw][,strX][,rowstr]} (pN)[+pm_x], voz[0]h [,?prSC]
syntax
Return      vec40_t
type
                                                             Determines the element size and number
                               EW_options
            1   EW
                               enum                          of loaded elements (see enum definition
                                                             at vec-mem-modes.h)
Operands
            2   IN1_PTR        void *                        Pointer register (rN)
            3   IN2_PM_PTR void*                             Pointer register (rN)
            void* ptr;
            void* vRes;
C example   ...
            ptr = vldw_pm_ptr_v40_u_r (ew_8w, ptr, vRes);
Comments



Intrinsic     vldw_v40_u_r
name
Spec syntax   vldw {ew [,u][,r_sw][,strX][,rowstr]} (pN)[+pm_x], voz[0]h [,?prSC]

Return        vec40_t
type
                                                             Determines the element size and number
                                EW_options
              1   EW
                                enum                         of loaded elements (see enum definition
Operands                                                     at vec-mem-modes.h)
              2   IN1_PTR       void *                       Pointer register (rN)
              void* ptr;
              vec40_t vRes;
C example     ...
              vRes = vldw_v40_u_r (ew_8w, ptr);

Comments


Main table → Memory Access → Load → Load unsigned W rounded
Available addressing modes
Intrinsic Names:
vldw_indexed_imm_v40_u_r_rowstr
vldw_indexed_rI_pm_imm_v40_u_r_rowstr
vldw_indexed_rI_pm_ptr_v40_u_r_rowstr
vldw_indexed_rI_v40_u_r_rowstr
vldw_indexed_rIp_pm_imm_v40_u_r_rowstr
vldw_indexed_rIp_pm_ptr_v40_u_r_rowstr
vldw_indexed_rIp_v40_u_r_rowstr
vldw_pm_imm_v40_u_r_rowstr
vldw_pm_ptr_v40_u_r_rowstr
vldw_v40_u_r_rowstr
Intrinsic   vldw_indexed_imm_v40_u_r_rowstr
name

Spec        vldw {ew [,u][,r_sw][,strX][,rowstr]} (gB+#imm16_6), voz[0]h [,?prSC]
syntax
Return      vec40_t
type
                                                             Determines the element size and number
                                EW_options
            1   EW
                                enum                         of loaded elements (see enum definition
                                                             at vec-mem-modes.h)
Operands    2   IN1_gB_BASE void *                           Pointer register (gB)
                                              -              16 bit immediate post modification in
            3   IN2_IMM16_6     int16
                                              32768..32767   bytes
            void* ptrBase;
            vec40_t vRes;
C example   ...
            vRes = vldw_indexed_imm_v40_u_r_rowstr (ew_8w, ptrBase, 2);

Comments



Intrinsic   vldw_indexed_rI_pm_imm_v40_u_r_rowstr
name
Spec        vldw {ew [,u][,r_sw][,strX][,rowstr]} (gB+rI)[+pm], voz[0]h [,?prSC]
syntax
Return      vec40_t
type
                                                             Determines the element size and number
                                EW_options
            1 EW
                                enum                         of loaded elements (see enum definition
                                                             at vec-mem-modes.h)
            2 IN1_gB_BASE       void *                       Pointer register (gB)
Operands
                                                             Pointer (rI) specifying the offset from the
            3 IN2_rI_OFFSET void *
                                                             base pointer
                                                31   31      32 bit immediate post modification in
            4 IN3_PM_IMM        int32          -2 ..2 -1
                                                             bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vRes;
            ...
            vRes = vldw_indexed_rI_pm_imm_v40_u_r_rowstr (ew_8w, ptrBase, ptrModify, 2);

Comments
Intrinsic   vldw_indexed_rI_pm_ptr_v40_u_r_rowstr
name
Spec        vldw {ew [,u][,r_sw][,strX][,rowstr]} (gB+rI)[+pm], voz[0]h [,?prSC]
syntax
Return      vec40_t
type
                                                              Determines the element size and number
                                 EW_options
            1 EW

enum                         of loaded elements (see enum definition
                                                              at vec-mem-modes.h)

Operands    2 IN1_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            3 IN2_rI_OFFSET void *
                                                              base pointer
            4 IN3_PM_PTR         void*                        Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vRes;
            ...
            vRes = vldw_indexed_rI_pm_ptr_v40_u_r_rowstr (ew_8w, ptrBase, ptrModify, ptr);

Comments



Intrinsic   vldw_indexed_rI_v40_u_r_rowstr
name
Spec        vldw {ew [,u][,r_sw][,strX][,rowstr]} (gB+rI)[+pm], voz[0]h [,?prSC]
syntax
Return      vec40_t
type
                                                              Determines the element size and number
                                 EW_options
            1 EW
                                 enum                         of loaded elements (see enum definition
                                                              at vec-mem-modes.h)
Operands    2 IN1_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
            3 IN2_rI_OFFSET void *
                                                              base pointer
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vRes;
            ...
            vRes = vldw_indexed_rI_v40_u_r_rowstr (ew_8w, ptrBase, ptrModify);
Comments



Intrinsic   vldw_indexed_rIp_pm_imm_v40_u_r_rowstr
name
Spec        vldw {ew [,u][,r_sw][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]h [,?prSC]
syntax
Return      vec40_t
type
                                                             Determines the element size and number
                                EW_options
            1 EW
                                enum                         of loaded elements (see enum definition
                                                             at vec-mem-modes.h)
            2 IN1_gB_BASE       void *                       Pointer register (gB)
Operands                                                     Pointer (rI) specifying the offset from the
            3 IN2_rI_OFFSET void *

base pointer
            4 IN2_PART          uint8         LOW,HIGH       Word part which is used for operand 3
                                                31   31      32 bit immediate post modification in
            5 IN3_PM_IMM        int32         -2 ..2 -1
                                                             bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vRes;
            ...
            vRes = vldw_indexed_rIp_pm_imm_v40_u_r_rowstr (ew_8w, ptrBase, ptrModify, HIGH, 2);

Comments



Intrinsic   vldw_indexed_rIp_pm_ptr_v40_u_r_rowstr
name
Spec        vldw {ew [,u][,r_sw][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]h [,?prSC]
syntax
Return      vec40_t
type
                                                             Determines the element size and number
                                EW_options
            1 EW
                                enum                         of loaded elements (see enum definition
                                                             at vec-mem-modes.h)

Operands    2 IN1_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            3 IN2_rI_OFFSET void *
                                                             base pointer
            4 IN2_PART          uint8         LOW,HIGH       Word part which is used for operand 3
            5 IN3_PM_PTR        void*                        Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vRes;
            ...
            vRes = vldw_indexed_rIp_pm_ptr_v40_u_r_rowstr (ew_8w, ptrBase, ptrModify, HIGH, ptr);

Comments



Intrinsic   vldw_indexed_rIp_v40_u_r_rowstr
name
Spec        vldw {ew [,u][,r_sw][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]h [,?prSC]
syntax
Return      vec40_t
type
                                                             Determines the element size and number
                                EW_options
            1 EW
                                enum                         of loaded elements (see enum definition
                                                             at vec-mem-modes.h)

Operands    2 IN1_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            3 IN2_rI_OFFSET void *

base pointer
            4 IN2_PART          uint8          LOW,HIGH      Word part which is used for operand 3
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vRes;
            ...
            vRes = vldw_indexed_rIp_v40_u_r_rowstr (ew_8w, ptrBase, ptrModify, HIGH);

Comments



Intrinsic   vldw_pm_imm_v40_u_r_rowstr
name
Spec        vldw {ew [,u][,r_sw][,strX][,rowstr]} (pN)+#imm32_6, voz[0]h [,?prSC]
syntax
Return      vec40_t
type
                                                             Determines the element size and number
                               EW_options
            1   EW
                               enum                          of loaded elements (see enum definition
Operands                                                     at vec-mem-modes.h)
            2   IN1_PTR        void *                        Pointer register (rN)
                                                 31   31      32 bit immediate post modification in
              3   IN2_IMM32_6 int32            -2 ..2 -1
                                                              bytes
              void* ptr;
              vec40_t vRes;
C example     ...
              vRes = vldw_pm_imm_v40_u_r_rowstr (ew_8w, ptr, 2);

Comments



Intrinsic     vldw_pm_ptr_v40_u_r_rowstr
name
Spec          vldw {ew [,u][,r_sw][,strX][,rowstr]} (pN)[+pm_x], voz[0]h [,?prSC]
syntax
Return        vec40_t
type
                                                              Determines the element size and number
                                 EW_options
              1   EW
                                 enum                         of loaded elements (see enum definition
                                                              at vec-mem-modes.h)
Operands
              2   IN1_PTR        void *                       Pointer register (rN)
              3   IN2_PM_PTR void*                            Pointer register (rN)
              void* ptr;
              void* vRes;
C example     ...
              ptr = vldw_pm_ptr_v40_u_r_rowstr (ew_8w, ptr, vRes);

Comments



Intrinsic     vldw_v40_u_r_rowstr
name
Spec syntax   vldw {ew [,u][,r_sw][,strX][,rowstr]} (pN)[+pm_x], voz[0]h [,?prSC]

Return        vec40_t
type
                                                              Determines the element size and number
                                EW_options
              1   EW

enum                          of loaded elements (see enum definition
Operands                                                      at vec-mem-modes.h)
              2   IN1_PTR       void *                        Pointer register (rN)
              void* ptr;
              vec40_t vRes;
C example     ...
              vRes = vldw_v40_u_r_rowstr (ew_8w, ptr);
Comments


Main table → Memory Access → Load → Load unsigned W rounded
Available addressing modes
Intrinsic Names:
vldw_direct_v40_2w_dup_u_r
vldw_indexed_imm_v40_2w_dup_u_r
vldw_indexed_rI_pm_imm_v40_2w_dup_u_r
vldw_indexed_rI_pm_ptr_v40_2w_dup_u_r
vldw_indexed_rI_v40_2w_dup_u_r
vldw_indexed_rIp_pm_imm_v40_2w_dup_u_r
vldw_indexed_rIp_pm_ptr_v40_2w_dup_u_r
vldw_indexed_rIp_v40_2w_dup_u_r
vldw_pm_imm_v40_2w_dup_u_r
vldw_pm_ptr_v40_2w_dup_u_r
vldw_v40_2w_dup_u_r
Intrinsic     vldw_direct_v40_2w_dup_u_r
name
Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX]} [#address], voz[0]h [,?prSC]

Return type   vec40_t
                                               32
Operands      1    IN1_ADDR       int32     0..2 -1         32 bit address
              vec40_t vRes;
C example     ...
              vRes = vldw_direct_v40_2w_dup_u_r (2);

Comments



Intrinsic     vldw_indexed_imm_v40_2w_dup_u_r
name
Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+#imm16_6), voz[0]h [,?prSC]

Return type   vec40_t

              1   IN1_gB_BASE void *                        Pointer register (gB)
Operands                                                    16 bit immediate post modification in
              2   IN2_IMM16_6      int16    -32768..32767
                                                            bytes
              void* ptrBase;
              vec40_t vRes;
C example     ...
              vRes = vldw_indexed_imm_v40_2w_dup_u_r (ptrBase, 2);

Comments



Intrinsic     vldw_indexed_rI_pm_imm_v40_2w_dup_u_r
name
Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+rI)[+pm], voz[0]h [,?prSC]

Return type   vec40_t

              1   IN1_gB_BASE      void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
Operands                                                    base pointer
                                              31    31      32 bit immediate post modification in
              3   IN3_PM_IMM       int32    -2 ..2 -1

bytes
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rI_pm_imm_v40_2w_dup_u_r (ptrBase, ptrModify, 2);
Comments



Intrinsic     vldw_indexed_rI_pm_ptr_v40_2w_dup_u_r
name
Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+rI)[+pm], voz[0]h [,?prSC]

Return type   vec40_t

              1   IN1_gB_BASE       void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
Operands      2   IN2_rI_OFFSET void *
                                                             base pointer
              3   IN3_PM_PTR        void*                    Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rI_pm_ptr_v40_2w_dup_u_r (ptrBase, ptrModify, ptr);

Comments



Intrinsic     vldw_indexed_rI_v40_2w_dup_u_r
name
Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+rI)[+pm], voz[0]h [,?prSC]

Return type   vec40_t

              1   IN1_gB_BASE       void *                   Pointer register (gB)
Operands                                                     Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
                                                             base pointer
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rI_v40_2w_dup_u_r (ptrBase, ptrModify);

Comments



Intrinsic     vldw_indexed_rIp_pm_imm_v40_2w_dup_u_r
name
Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]h [,?prSC]

Return type   vec40_t
              1   IN1_gB_BASE      void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
                                                            base pointer
Operands
              3   IN2_PART         uint8    LOW,HIGH        Word part which is used for operand 2
                                              31   31       32 bit immediate post modification in
              4   IN3_PM_IMM       int32    -2 ..2 -1
                                                            bytes
              void* ptrBase;

void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rIp_pm_imm_v40_2w_dup_u_r (ptrBase, ptrModify, HIGH, 2);

Comments



Intrinsic     vldw_indexed_rIp_pm_ptr_v40_2w_dup_u_r
name
Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]h [,?prSC]

Return type   vec40_t

              1   IN1_gB_BASE      void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
Operands                                                    base pointer
              3   IN2_PART         uint8    LOW,HIGH        Word part which is used for operand 2
              4   IN3_PM_PTR       void*                    Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rIp_pm_ptr_v40_2w_dup_u_r (ptrBase, ptrModify, HIGH, ptr);

Comments



Intrinsic     vldw_indexed_rIp_v40_2w_dup_u_r
name
Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]h [,?prSC]

Return type   vec40_t

              1   IN1_gB_BASE      void *                   Pointer register (gB)
Operands                                                    Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
                                                            base pointer
              3   IN2_PART         uint8    LOW,HIGH          Word part which is used for operand 2
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rIp_v40_2w_dup_u_r (ptrBase, ptrModify, HIGH);

Comments



Intrinsic     vldw_pm_imm_v40_2w_dup_u_r
name
Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (pN)+#imm32_6, voz[0]h [,?prSC]

Return type   vec40_t

              1    IN1_PTR        void *                      Pointer register (rN)
Operands                                     31   31          32 bit immediate post modification in
              2    IN2_IMM32_6 int32       -2 ..2 -1
                                                              bytes
              void* ptr;
              vec40_t vRes;
C example     ...
              vRes = vldw_pm_imm_v40_2w_dup_u_r (ptr, 2);

Comments



Intrinsic     vldw_pm_ptr_v40_2w_dup_u_r
name

Spec syntax   vldw {2w_4w, dup [,u][,r_sw] [,strX][,rowstr]} (pN)[+pm_x], voz[0]h [,?prSC]

Return type   vec40_t

              1    IN1_PTR        void *                      Pointer register (rN)
Operands
              2    IN2_PM_PTR void*                           Pointer register (rN)
              void* ptr;
              void* vRes;
C example     ...
              ptr = vldw_pm_ptr_v40_2w_dup_u_r (ptr, vRes);

Comments



Intrinsic     vldw_v40_2w_dup_u_r
name
Spec syntax   vldw {2w_4w, dup [,u][,r_sw] [,strX][,rowstr]} (pN)[+pm_x], voz[0]h [,?prSC]

Return type   vec40_t
Operands       1   IN1_PTR        void *           Pointer register (rN)
               void* ptr;
               vec40_t vRes;
C example      ...
               vRes = vldw_v40_2w_dup_u_r (ptr);

Comments


Main table → Memory Access → Load → Load unsigned W rounded
Available addressing modes
Intrinsic Names:
vldw_indexed_imm_v40_2w_dup_u_r_rowstr
vldw_indexed_rI_pm_imm_v40_2w_dup_u_r_rowstr
vldw_indexed_rI_pm_ptr_v40_2w_dup_u_r_rowstr
vldw_indexed_rI_v40_2w_dup_u_r_rowstr
vldw_indexed_rIp_pm_imm_v40_2w_dup_u_r_rowstr
vldw_indexed_rIp_pm_ptr_v40_2w_dup_u_r_rowstr
vldw_indexed_rIp_v40_2w_dup_u_r_rowstr
vldw_pm_imm_v40_2w_dup_u_r_rowstr
vldw_pm_ptr_v40_2w_dup_u_r_rowstr
vldw_v40_2w_dup_u_r_rowstr
Intrinsic     vldw_indexed_imm_v40_2w_dup_u_r_rowstr
name
Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+#imm16_6), voz[0]h [,?prSC]

Return type   vec40_t

              1   IN1_gB_BASE void *                        Pointer register (gB)
Operands                                                    16 bit immediate post modification in
              2   IN2_IMM16_6      int16    -32768..32767
                                                            bytes
              void* ptrBase;
              vec40_t vRes;
C example     ...
              vRes = vldw_indexed_imm_v40_2w_dup_u_r_rowstr (ptrBase, 2);

Comments



Intrinsic     vldw_indexed_rI_pm_imm_v40_2w_dup_u_r_rowstr
name
Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+rI)[+pm], voz[0]h [,?prSC]

Return type   vec40_t

              1   IN1_gB_BASE      void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
Operands                                                    base pointer

31   31       32 bit immediate post modification in
              3   IN3_PM_IMM       int32    -2 ..2 -1
                                                            bytes
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rI_pm_imm_v40_2w_dup_u_r_rowstr (ptrBase, ptrModify, 2);

Comments



Intrinsic     vldw_indexed_rI_pm_ptr_v40_2w_dup_u_r_rowstr
name
Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+rI)[+pm], voz[0]h [,?prSC]

Return type   vec40_t

              1   IN1_gB_BASE      void *                   Pointer register (gB)
Operands                                                    Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
                                                            base pointer
              3   IN3_PM_PTR        void*                   Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rI_pm_ptr_v40_2w_dup_u_r_rowstr (ptrBase, ptrModify, ptr);

Comments



Intrinsic     vldw_indexed_rI_v40_2w_dup_u_r_rowstr
name
Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+rI)[+pm], voz[0]h [,?prSC]

Return type   vec40_t

              1   IN1_gB_BASE       void *                  Pointer register (gB)
Operands                                                    Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
                                                            base pointer
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rI_v40_2w_dup_u_r_rowstr (ptrBase, ptrModify);

Comments



Intrinsic     vldw_indexed_rIp_pm_imm_v40_2w_dup_u_r_rowstr
name
Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]h [,?prSC]

Return type   vec40_t

              1   IN1_gB_BASE       void *                  Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
                                                            base pointer
Operands
              3   IN2_PART          uint8    LOW,HIGH       Word part which is used for operand 2

31   31      32 bit immediate post modification in
              4   IN3_PM_IMM        int32    -2 ..2 -1
                                                            bytes
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rIp_pm_imm_v40_2w_dup_u_r_rowstr (ptrBase, ptrModify, HIGH, 2);

Comments
Intrinsic     vldw_indexed_rIp_pm_ptr_v40_2w_dup_u_r_rowstr
name
Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]h [,?prSC]

Return type   vec40_t

              1   IN1_gB_BASE      void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
Operands                                                    base pointer
              3   IN2_PART         uint8    LOW,HIGH        Word part which is used for operand 2
              4   IN3_PM_PTR       void*                    Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rIp_pm_ptr_v40_2w_dup_u_r_rowstr (ptrBase, ptrModify, HIGH, ptr);

Comments



Intrinsic     vldw_indexed_rIp_v40_2w_dup_u_r_rowstr
name
Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]h [,?prSC]

Return type   vec40_t

              1   IN1_gB_BASE      void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
Operands      2   IN2_rI_OFFSET void *
                                                            base pointer
              3   IN2_PART         uint8    LOW,HIGH        Word part which is used for operand 2
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rIp_v40_2w_dup_u_r_rowstr (ptrBase, ptrModify, HIGH);

Comments



Intrinsic     vldw_pm_imm_v40_2w_dup_u_r_rowstr
name
Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (pN)+#imm32_6, voz[0]h [,?prSC]
Return type   vec40_t

              1    IN1_PTR        void *                   Pointer register (rN)
Operands                                     31   31       32 bit immediate post modification in
              2    IN2_IMM32_6 int32       -2 ..2 -1

bytes
              void* ptr;
              vec40_t vRes;
C example     ...
              vRes = vldw_pm_imm_v40_2w_dup_u_r_rowstr (ptr, 2);

Comments



Intrinsic     vldw_pm_ptr_v40_2w_dup_u_r_rowstr
name
Spec syntax   vldw {2w_4w, dup [,u][,r_sw] [,strX][,rowstr]} (pN)[+pm_x], voz[0]h [,?prSC]

Return type   vec40_t

              1    IN1_PTR        void *                   Pointer register (rN)
Operands
              2    IN2_PM_PTR void*                        Pointer register (rN)
              void* ptr;
              void* vRes;
C example     ...
              ptr = vldw_pm_ptr_v40_2w_dup_u_r_rowstr (ptr, vRes);

Comments



Intrinsic     vldw_v40_2w_dup_u_r_rowstr
name
Spec syntax   vldw {2w_4w, dup [,u][,r_sw] [,strX][,rowstr]} (pN)[+pm_x], voz[0]h [,?prSC]

Return type   vec40_t

Operands      1    IN1_PTR        void *                   Pointer register (rN)
              void* ptr;
              vec40_t vRes;
C example     ...
              vRes = vldw_v40_2w_dup_u_r_rowstr (ptr);

Comments


Main table → Memory Access → Load → Load unsigned W rounded
Available addressing modes
Intrinsic Names:
vldw_direct_v40_4w_dup_u_r
vldw_indexed_imm_v40_4w_dup_u_r
vldw_indexed_rI_pm_imm_v40_4w_dup_u_r
vldw_indexed_rI_pm_ptr_v40_4w_dup_u_r
vldw_indexed_rI_v40_4w_dup_u_r
vldw_indexed_rIp_pm_imm_v40_4w_dup_u_r
vldw_indexed_rIp_pm_ptr_v40_4w_dup_u_r
vldw_indexed_rIp_v40_4w_dup_u_r
vldw_pm_imm_v40_4w_dup_u_r
vldw_pm_ptr_v40_4w_dup_u_r
vldw_v40_4w_dup_u_r
Intrinsic     vldw_direct_v40_4w_dup_u_r
name
Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX]} [#address], voz[0]h [,?prSC]

Return type   vec40_t
                                               32
Operands      1    IN1_ADDR       int32     0..2 -1         32 bit address
              vec40_t vRes;
C example     ...
              vRes = vldw_direct_v40_4w_dup_u_r (2);

Comments



Intrinsic     vldw_indexed_imm_v40_4w_dup_u_r
name
Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+#imm16_6), voz[0]h [,?prSC]

Return type   vec40_t

              1   IN1_gB_BASE void *                        Pointer register (gB)
Operands                                                    16 bit immediate post modification in
              2   IN2_IMM16_6      int16    -32768..32767
                                                            bytes
              void* ptrBase;
              vec40_t vRes;
C example     ...
              vRes = vldw_indexed_imm_v40_4w_dup_u_r (ptrBase, 2);

Comments

Intrinsic     vldw_indexed_rI_pm_imm_v40_4w_dup_u_r
name
Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+rI)[+pm], voz[0]h [,?prSC]

Return type   vec40_t

              1   IN1_gB_BASE      void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
Operands                                                    base pointer
                                              31    31      32 bit immediate post modification in
              3   IN3_PM_IMM       int32    -2 ..2 -1
                                                            bytes
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rI_pm_imm_v40_4w_dup_u_r (ptrBase, ptrModify, 2);
Comments



Intrinsic     vldw_indexed_rI_pm_ptr_v40_4w_dup_u_r
name
Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+rI)[+pm], voz[0]h [,?prSC]

Return type   vec40_t

              1   IN1_gB_BASE       void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
Operands      2   IN2_rI_OFFSET void *
                                                             base pointer
              3   IN3_PM_PTR        void*                    Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rI_pm_ptr_v40_4w_dup_u_r (ptrBase, ptrModify, ptr);

Comments



Intrinsic     vldw_indexed_rI_v40_4w_dup_u_r
name
Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+rI)[+pm], voz[0]h [,?prSC]

Return type   vec40_t

              1   IN1_gB_BASE       void *                   Pointer register (gB)
Operands                                                     Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
                                                             base pointer
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rI_v40_4w_dup_u_r (ptrBase, ptrModify);

Comments



Intrinsic     vldw_indexed_rIp_pm_imm_v40_4w_dup_u_r
name
Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]h [,?prSC]

Return type   vec40_t
              1   IN1_gB_BASE      void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
                                                            base pointer
Operands
              3   IN2_PART         uint8    LOW,HIGH        Word part which is used for operand 2
                                              31   31       32 bit immediate post modification in
              4   IN3_PM_IMM       int32    -2 ..2 -1
                                                            bytes
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rIp_pm_imm_v40_4w_dup_u_r (ptrBase, ptrModify, HIGH, 2);

Comments



Intrinsic     vldw_indexed_rIp_pm_ptr_v40_4w_dup_u_r
name
Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]h [,?prSC]

Return type   vec40_t

              1   IN1_gB_BASE      void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
Operands                                                    base pointer
              3   IN2_PART         uint8    LOW,HIGH        Word part which is used for operand 2
              4   IN3_PM_PTR       void*                    Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rIp_pm_ptr_v40_4w_dup_u_r (ptrBase, ptrModify, HIGH, ptr);

Comments



Intrinsic     vldw_indexed_rIp_v40_4w_dup_u_r
name
Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]h [,?prSC]

Return type   vec40_t

              1   IN1_gB_BASE      void *                   Pointer register (gB)
Operands                                                    Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
                                                            base pointer
              3   IN2_PART         uint8    LOW,HIGH          Word part which is used for operand 2
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rIp_v40_4w_dup_u_r (ptrBase, ptrModify, HIGH);

Comments



Intrinsic     vldw_pm_imm_v40_4w_dup_u_r
name
Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (pN)+#imm32_6, voz[0]h [,?prSC]

Return type   vec40_t

              1    IN1_PTR        void *                      Pointer register (rN)
Operands                                     31   31          32 bit immediate post modification in
              2    IN2_IMM32_6 int32       -2 ..2 -1
                                                              bytes
              void* ptr;
              vec40_t vRes;
C example     ...
              vRes = vldw_pm_imm_v40_4w_dup_u_r (ptr, 2);

Comments



Intrinsic     vldw_pm_ptr_v40_4w_dup_u_r
name
Spec syntax   vldw {2w_4w, dup [,u][,r_sw] [,strX][,rowstr]} (pN)[+pm_x], voz[0]h [,?prSC]

Return type   vec40_t

              1    IN1_PTR        void *                      Pointer register (rN)
Operands
              2    IN2_PM_PTR void*                           Pointer register (rN)
              void* ptr;
              void* vRes;
C example     ...
              ptr = vldw_pm_ptr_v40_4w_dup_u_r (ptr, vRes);

Comments



Intrinsic     vldw_v40_4w_dup_u_r
name
Spec syntax   vldw {2w_4w, dup [,u][,r_sw] [,strX][,rowstr]} (pN)[+pm_x], voz[0]h [,?prSC]

Return type   vec40_t
Operands       1   IN1_PTR        void *           Pointer register (rN)
               void* ptr;
               vec40_t vRes;
C example      ...
               vRes = vldw_v40_4w_dup_u_r (ptr);

Comments


Main table → Memory Access → Load → Load unsigned W rounded
Available addressing modes
Intrinsic Names:
vldw_indexed_imm_v40_4w_dup_u_r_rowstr
vldw_indexed_rI_pm_imm_v40_4w_dup_u_r_rowstr
vldw_indexed_rI_pm_ptr_v40_4w_dup_u_r_rowstr
vldw_indexed_rI_v40_4w_dup_u_r_rowstr
vldw_indexed_rIp_pm_imm_v40_4w_dup_u_r_rowstr
vldw_indexed_rIp_pm_ptr_v40_4w_dup_u_r_rowstr
vldw_indexed_rIp_v40_4w_dup_u_r_rowstr
vldw_pm_imm_v40_4w_dup_u_r_rowstr
vldw_pm_ptr_v40_4w_dup_u_r_rowstr
vldw_v40_4w_dup_u_r_rowstr
Intrinsic     vldw_indexed_imm_v40_4w_dup_u_r_rowstr
name
Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+#imm16_6), voz[0]h [,?prSC]

Return type   vec40_t

              1   IN1_gB_BASE void *                        Pointer register (gB)
Operands                                                    16 bit immediate post modification in
              2   IN2_IMM16_6      int16    -32768..32767
                                                            bytes
              void* ptrBase;
              vec40_t vRes;

C example     ...
              vRes = vldw_indexed_imm_v40_4w_dup_u_r_rowstr (ptrBase, 2);

Comments



Intrinsic     vldw_indexed_rI_pm_imm_v40_4w_dup_u_r_rowstr
name
Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+rI)[+pm], voz[0]h [,?prSC]

Return type   vec40_t

              1   IN1_gB_BASE      void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
Operands                                                    base pointer
                                              31   31       32 bit immediate post modification in
              3   IN3_PM_IMM       int32    -2 ..2 -1
                                                            bytes
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rI_pm_imm_v40_4w_dup_u_r_rowstr (ptrBase, ptrModify, 2);

Comments



Intrinsic     vldw_indexed_rI_pm_ptr_v40_4w_dup_u_r_rowstr
name
Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+rI)[+pm], voz[0]h [,?prSC]

Return type   vec40_t

              1   IN1_gB_BASE      void *                   Pointer register (gB)
Operands                                                    Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
                                                            base pointer
              3   IN3_PM_PTR        void*                   Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rI_pm_ptr_v40_4w_dup_u_r_rowstr (ptrBase, ptrModify, ptr);

Comments



Intrinsic     vldw_indexed_rI_v40_4w_dup_u_r_rowstr
name
Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+rI)[+pm], voz[0]h [,?prSC]

Return type   vec40_t

              1   IN1_gB_BASE       void *                  Pointer register (gB)
Operands                                                    Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
                                                            base pointer
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rI_v40_4w_dup_u_r_rowstr (ptrBase, ptrModify);

Comments

Intrinsic     vldw_indexed_rIp_pm_imm_v40_4w_dup_u_r_rowstr
name
Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]h [,?prSC]

Return type   vec40_t

              1   IN1_gB_BASE       void *                  Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
                                                            base pointer
Operands
              3   IN2_PART          uint8    LOW,HIGH       Word part which is used for operand 2
                                               31   31      32 bit immediate post modification in
              4   IN3_PM_IMM        int32    -2 ..2 -1
                                                            bytes
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rIp_pm_imm_v40_4w_dup_u_r_rowstr (ptrBase, ptrModify, HIGH, 2);

Comments
Intrinsic     vldw_indexed_rIp_pm_ptr_v40_4w_dup_u_r_rowstr
name
Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]h [,?prSC]

Return type   vec40_t

              1   IN1_gB_BASE      void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
Operands                                                    base pointer
              3   IN2_PART         uint8    LOW,HIGH        Word part which is used for operand 2
              4   IN3_PM_PTR       void*                    Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rIp_pm_ptr_v40_4w_dup_u_r_rowstr (ptrBase, ptrModify, HIGH, ptr);

Comments



Intrinsic     vldw_indexed_rIp_v40_4w_dup_u_r_rowstr
name
Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]h [,?prSC]

Return type   vec40_t

              1   IN1_gB_BASE      void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
Operands      2   IN2_rI_OFFSET void *
                                                            base pointer
              3   IN2_PART         uint8    LOW,HIGH        Word part which is used for operand 2

void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rIp_v40_4w_dup_u_r_rowstr (ptrBase, ptrModify, HIGH);

Comments



Intrinsic     vldw_pm_imm_v40_4w_dup_u_r_rowstr
name
Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (pN)+#imm32_6, voz[0]h [,?prSC]
Return type   vec40_t

              1    IN1_PTR        void *                   Pointer register (rN)
Operands                                     31   31       32 bit immediate post modification in
              2    IN2_IMM32_6 int32       -2 ..2 -1
                                                           bytes
              void* ptr;
              vec40_t vRes;
C example     ...
              vRes = vldw_pm_imm_v40_4w_dup_u_r_rowstr (ptr, 2);

Comments



Intrinsic     vldw_pm_ptr_v40_4w_dup_u_r_rowstr
name
Spec syntax   vldw {2w_4w, dup [,u][,r_sw] [,strX][,rowstr]} (pN)[+pm_x], voz[0]h [,?prSC]

Return type   vec40_t

              1    IN1_PTR       void *                    Pointer register (rN)
Operands
              2    IN2_PM_PTR void*                        Pointer register (rN)
              void* ptr;
              void* vRes;
C example     ...
              ptr = vldw_pm_ptr_v40_4w_dup_u_r_rowstr (ptr, vRes);

Comments



Intrinsic     vldw_v40_4w_dup_u_r_rowstr
name
Spec syntax   vldw {2w_4w, dup [,u][,r_sw] [,strX][,rowstr]} (pN)[+pm_x], voz[0]h [,?prSC]

Return type   vec40_t

Operands      1    IN1_PTR       void *                    Pointer register (rN)
              void* ptr;
              vec40_t vRes;
C example     ...
              vRes = vldw_v40_4w_dup_u_r_rowstr (ptr);

Comments


Main table → Memory Access → Load → Load unsigned W rounded
Available addressing modes
Intrinsic Names:
vldw_direct_v40_clone_2w_dup_u_r
vldw_indexed_imm_v40_clone_2w_dup_u_r
vldw_indexed_rI_pm_imm_v40_clone_2w_dup_u_r
vldw_indexed_rI_pm_ptr_v40_clone_2w_dup_u_r
vldw_indexed_rI_v40_clone_2w_dup_u_r
vldw_indexed_rIp_pm_imm_v40_clone_2w_dup_u_r
vldw_indexed_rIp_pm_ptr_v40_clone_2w_dup_u_r
vldw_indexed_rIp_v40_clone_2w_dup_u_r
vldw_pm_imm_v40_clone_2w_dup_u_r
vldw_pm_ptr_v40_clone_2w_dup_u_r
vldw_v40_clone_2w_dup_u_r
Intrinsic     vldw_direct_v40_clone_2w_dup_u_r
name          vldw_direct_v40_str1_2w_dup_u_r

Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX]} [#address], voz[0]h [,?prSC]

Return type   vec40_t
                                               32

Operands      1    IN1_ADDR       int32     0..2 -1          32 bit address
              vec40_t vRes;
C example     ...
              vRes = vldw_direct_v40_clone_2w_dup_u_r (2);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_imm_v40_clone_2w_dup_u_r
name          vldw_indexed_imm_v40_str1_2w_dup_u_r

Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+#imm16_6), voz[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE void *                        Pointer register (gB)
Operands                                                     16 bit immediate post modification in
              2    IN2_IMM16_6     int16    -32768..32767
                                                             bytes
              void* ptrBase;
              vec40_t vRes;
C example     ...
              vRes = vldw_indexed_imm_v40_clone_2w_dup_u_r (ptrBase, 2);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_rI_pm_imm_v40_clone_2w_dup_u_r
name          vldw_indexed_rI_pm_imm_v40_str1_2w_dup_u_r

Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+rI)[+pm], voz[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                    Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
Operands                                                     base pointer
                                              31    31       32 bit immediate post modification in
              3    IN3_PM_IMM      int32    -2 ..2 -1
                                                             bytes
              void* ptrBase;
C example     void* ptrModify;
              vec40_t vRes;
              ...
              vRes = vldw_indexed_rI_pm_imm_v40_clone_2w_dup_u_r (ptrBase, ptrModify, 2);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_rI_pm_ptr_v40_clone_2w_dup_u_r
name          vldw_indexed_rI_pm_ptr_v40_str1_2w_dup_u_r

Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+rI)[+pm], voz[0]h [,?prSC]

Return type   vec40_t

1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
Operands      2    IN2_rI_OFFSET void *
                                                             base pointer
              3    IN3_PM_PTR       void*                    Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rI_pm_ptr_v40_clone_2w_dup_u_r (ptrBase, ptrModify, ptr);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_rI_v40_clone_2w_dup_u_r
name          vldw_indexed_rI_v40_str1_2w_dup_u_r

Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+rI)[+pm], voz[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
Operands                                                     Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rI_v40_clone_2w_dup_u_r (ptrBase, ptrModify);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).
Intrinsic     vldw_indexed_rIp_pm_imm_v40_clone_2w_dup_u_r
name          vldw_indexed_rIp_pm_imm_v40_str1_2w_dup_u_r

Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                            base pointer
Operands
              3    IN2_PART        uint8    LOW,HIGH        Word part which is used for operand 2
                                              31   31       32 bit immediate post modification in
              4    IN3_PM_IMM      int32    -2 ..2 -1
                                                            bytes
              void* ptrBase;

void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rIp_pm_imm_v40_clone_2w_dup_u_r (ptrBase, ptrModify, HIGH, 2);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_rIp_pm_ptr_v40_clone_2w_dup_u_r
name          vldw_indexed_rIp_pm_ptr_v40_str1_2w_dup_u_r

Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
Operands                                                    base pointer
              3    IN2_PART        uint8    LOW,HIGH        Word part which is used for operand 2
              4    IN3_PM_PTR      void*                    Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rIp_pm_ptr_v40_clone_2w_dup_u_r (ptrBase, ptrModify, HIGH, ptr);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_rIp_v40_clone_2w_dup_u_r
name          vldw_indexed_rIp_v40_str1_2w_dup_u_r
Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
Operands      2    IN2_rI_OFFSET void *
                                                            base pointer
              3    IN2_PART        uint8    LOW,HIGH        Word part which is used for operand 2
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rIp_v40_clone_2w_dup_u_r (ptrBase, ptrModify, HIGH);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_pm_imm_v40_clone_2w_dup_u_r
name          vldw_pm_imm_v40_str1_2w_dup_u_r

Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (pN)+#imm32_6, voz[0]h [,?prSC]

Return type   vec40_t

              1    IN1_PTR        void *                   Pointer register (rN)
Operands                                     31   31       32 bit immediate post modification in
              2    IN2_IMM32_6 int32        -2 ..2 -1
                                                           bytes
              void* ptr;
              vec40_t vRes;
C example     ...
              vRes = vldw_pm_imm_v40_clone_2w_dup_u_r (ptr, 2);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_pm_ptr_v40_clone_2w_dup_u_r
name          vldw_pm_ptr_v40_str1_2w_dup_u_r

Spec syntax   vldw {2w_4w, dup [,u][,r_sw] [,strX][,rowstr]} (pN)[+pm_x], voz[0]h [,?prSC]

Return type   vec40_t

              1    IN1_PTR        void *                   Pointer register (rN)
Operands
              2    IN2_PM_PTR void*                        Pointer register (rN)
              void* ptr;
              void* vRes;
C example     ...
              ptr = vldw_pm_ptr_v40_clone_2w_dup_u_r (ptr, vRes);
                    The same data will be loaded to all vector units (Unless str1 is configured
Comments       1.
                    otherwise).



Intrinsic      vldw_v40_clone_2w_dup_u_r
name           vldw_v40_str1_2w_dup_u_r

Spec syntax    vldw {2w_4w, dup [,u][,r_sw] [,strX][,rowstr]} (pN)[+pm_x], voz[0]h [,?prSC]

Return type    vec40_t

Operands       1    IN1_PTR       void *                   Pointer register (rN)
               void* ptr;
               vec40_t vRes;
C example      ...
               vRes = vldw_v40_clone_2w_dup_u_r (ptr);

                    The same data will be loaded to all vector units (Unless str1 is configured
Comments       1.
                    otherwise).


Main table → Memory Access → Load → Load unsigned W rounded
Available addressing modes
Intrinsic Names:
vldw_indexed_imm_v40_clone_2w_dup_u_r_rowstr
vldw_indexed_rI_pm_imm_v40_clone_2w_dup_u_r_rowstr
vldw_indexed_rI_pm_ptr_v40_clone_2w_dup_u_r_rowstr
vldw_indexed_rI_v40_clone_2w_dup_u_r_rowstr
vldw_indexed_rIp_pm_imm_v40_clone_2w_dup_u_r_rowstr
vldw_indexed_rIp_pm_ptr_v40_clone_2w_dup_u_r_rowstr
vldw_indexed_rIp_v40_clone_2w_dup_u_r_rowstr
vldw_pm_imm_v40_clone_2w_dup_u_r_rowstr
vldw_pm_ptr_v40_clone_2w_dup_u_r_rowstr
vldw_v40_clone_2w_dup_u_r_rowstr

Intrinsic     vldw_indexed_imm_v40_clone_2w_dup_u_r_rowstr
name          vldw_indexed_imm_v40_str1_2w_dup_u_r_rowstr

Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+#imm16_6), voz[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE void *                       Pointer register (gB)
Operands                                                    16 bit immediate post modification in
              2    IN2_IMM16_6     int16    -32768..32767
                                                            bytes
              void* ptrBase;
              vec40_t vRes;
C example     ...
              vRes = vldw_indexed_imm_v40_clone_2w_dup_u_r_rowstr (ptrBase, 2);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_rI_pm_imm_v40_clone_2w_dup_u_r_rowstr
name          vldw_indexed_rI_pm_imm_v40_str1_2w_dup_u_r_rowstr

Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+rI)[+pm], voz[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
Operands                                                    base pointer
                                              31   31       32 bit immediate post modification in
              3    IN3_PM_IMM      int32    -2 ..2 -1
                                                            bytes
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rI_pm_imm_v40_clone_2w_dup_u_r_rowstr (ptrBase, ptrModify, 2);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_rI_pm_ptr_v40_clone_2w_dup_u_r_rowstr
name          vldw_indexed_rI_pm_ptr_v40_str1_2w_dup_u_r_rowstr

Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+rI)[+pm], voz[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)
Operands
              2    IN2_rI_OFFSET void *                     Pointer (rI) specifying the offset from the
                                                            base pointer

3    IN3_PM_PTR       void*                   Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rI_pm_ptr_v40_clone_2w_dup_u_r_rowstr (ptrBase, ptrModify, ptr);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_rI_v40_clone_2w_dup_u_r_rowstr
name          vldw_indexed_rI_v40_str1_2w_dup_u_r_rowstr

Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+rI)[+pm], voz[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE      void *                  Pointer register (gB)
Operands                                                    Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                            base pointer
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rI_v40_clone_2w_dup_u_r_rowstr (ptrBase, ptrModify);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_rIp_pm_imm_v40_clone_2w_dup_u_r_rowstr
name          vldw_indexed_rIp_pm_imm_v40_str1_2w_dup_u_r_rowstr

Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE      void *                  Pointer register (gB)

              2
                                                            Pointer (rI) specifying the offset from the
                   IN2_rI_OFFSET void *
                                                            base pointer
Operands
              3    IN2_PART         uint8    LOW,HIGH       Word part which is used for operand 2
                                               31   31      32 bit immediate post modification in
              4    IN3_PM_IMM       int32    -2 ..2 -1
                                                            bytes
              void* ptrBase;
C example     void* ptrModify;
              vec40_t vRes;
              ...
              vRes = vldw_indexed_rIp_pm_imm_v40_clone_2w_dup_u_r_rowstr (ptrBase, ptrModify, HIGH, 2);

The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_rIp_pm_ptr_v40_clone_2w_dup_u_r_rowstr
name          vldw_indexed_rIp_pm_ptr_v40_str1_2w_dup_u_r_rowstr

Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
Operands                                                    base pointer
              3    IN2_PART        uint8    LOW,HIGH        Word part which is used for operand 2
              4    IN3_PM_PTR      void*                    Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rIp_pm_ptr_v40_clone_2w_dup_u_r_rowstr (ptrBase, ptrModify, HIGH, ptr);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_rIp_v40_clone_2w_dup_u_r_rowstr
name          vldw_indexed_rIp_v40_str1_2w_dup_u_r_rowstr

Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
Operands      2    IN2_rI_OFFSET void *
                                                            base pointer
              3    IN2_PART        uint8    LOW,HIGH        Word part which is used for operand 2
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rIp_v40_clone_2w_dup_u_r_rowstr (ptrBase, ptrModify, HIGH);

Comments      1.   The same data will be loaded to all vector units (Unless str1 is configured
                   otherwise).



Intrinsic     vldw_pm_imm_v40_clone_2w_dup_u_r_rowstr
name          vldw_pm_imm_v40_str1_2w_dup_u_r_rowstr

Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (pN)+#imm32_6, voz[0]h [,?prSC]

Return type   vec40_t

1    IN1_PTR        void *                   Pointer register (rN)
Operands                                     31   31       32 bit immediate post modification in
              2    IN2_IMM32_6 int32       -2 ..2 -1
                                                           bytes
              void* ptr;
              vec40_t vRes;
C example     ...
              vRes = vldw_pm_imm_v40_clone_2w_dup_u_r_rowstr (ptr, 2);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_pm_ptr_v40_clone_2w_dup_u_r_rowstr
name          vldw_pm_ptr_v40_str1_2w_dup_u_r_rowstr

Spec syntax   vldw {2w_4w, dup [,u][,r_sw] [,strX][,rowstr]} (pN)[+pm_x], voz[0]h [,?prSC]

Return type   vec40_t

              1    IN1_PTR        void *                   Pointer register (rN)
Operands
              2    IN2_PM_PTR void*                        Pointer register (rN)
              void* ptr;
              void* vRes;
C example     ...
              ptr = vldw_pm_ptr_v40_clone_2w_dup_u_r_rowstr (ptr, vRes);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_v40_clone_2w_dup_u_r_rowstr
name          vldw_v40_str1_2w_dup_u_r_rowstr

Spec syntax   vldw {2w_4w, dup [,u][,r_sw] [,strX][,rowstr]} (pN)[+pm_x], voz[0]h [,?prSC]

Return type   vec40_t

Operands      1    IN1_PTR        void *                   Pointer register (rN)
              void* ptr;
C example     vec40_t vRes;
              ...
              vRes = vldw_v40_clone_2w_dup_u_r_rowstr (ptr);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).


Main table → Memory Access → Load → Load unsigned W rounded
Available addressing modes
Intrinsic Names:
vldw_direct_v40_clone_4w_dup_u_r
vldw_indexed_imm_v40_clone_4w_dup_u_r
vldw_indexed_rI_pm_imm_v40_clone_4w_dup_u_r
vldw_indexed_rI_pm_ptr_v40_clone_4w_dup_u_r
vldw_indexed_rI_v40_clone_4w_dup_u_r
vldw_indexed_rIp_pm_imm_v40_clone_4w_dup_u_r
vldw_indexed_rIp_pm_ptr_v40_clone_4w_dup_u_r
vldw_indexed_rIp_v40_clone_4w_dup_u_r
vldw_pm_imm_v40_clone_4w_dup_u_r
vldw_pm_ptr_v40_clone_4w_dup_u_r
vldw_v40_clone_4w_dup_u_r
Intrinsic     vldw_direct_v40_clone_4w_dup_u_r
name          vldw_direct_v40_str1_4w_dup_u_r

Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX]} [#address], voz[0]h [,?prSC]

Return type   vec40_t
                                               32
Operands      1    IN1_ADDR       int32     0..2 -1          32 bit address
              vec40_t vRes;
C example     ...
              vRes = vldw_direct_v40_clone_4w_dup_u_r (2);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_imm_v40_clone_4w_dup_u_r
name          vldw_indexed_imm_v40_str1_4w_dup_u_r

Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+#imm16_6), voz[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE void *                        Pointer register (gB)
Operands                                                     16 bit immediate post modification in
              2    IN2_IMM16_6     int16    -32768..32767
                                                             bytes
              void* ptrBase;
              vec40_t vRes;
C example     ...
              vRes = vldw_indexed_imm_v40_clone_4w_dup_u_r (ptrBase, 2);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_rI_pm_imm_v40_clone_4w_dup_u_r
name          vldw_indexed_rI_pm_imm_v40_str1_4w_dup_u_r

Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+rI)[+pm], voz[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                    Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
Operands                                                     base pointer
                                              31    31       32 bit immediate post modification in
              3    IN3_PM_IMM      int32    -2 ..2 -1
                                                             bytes
              void* ptrBase;
C example     void* ptrModify;
              vec40_t vRes;
              ...
              vRes = vldw_indexed_rI_pm_imm_v40_clone_4w_dup_u_r (ptrBase, ptrModify, 2);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_rI_pm_ptr_v40_clone_4w_dup_u_r

name          vldw_indexed_rI_pm_ptr_v40_str1_4w_dup_u_r

Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+rI)[+pm], voz[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
Operands      2    IN2_rI_OFFSET void *
                                                             base pointer
              3    IN3_PM_PTR       void*                    Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rI_pm_ptr_v40_clone_4w_dup_u_r (ptrBase, ptrModify, ptr);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_rI_v40_clone_4w_dup_u_r
name          vldw_indexed_rI_v40_str1_4w_dup_u_r

Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+rI)[+pm], voz[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
Operands                                                     Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rI_v40_clone_4w_dup_u_r (ptrBase, ptrModify);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).
Intrinsic     vldw_indexed_rIp_pm_imm_v40_clone_4w_dup_u_r
name          vldw_indexed_rIp_pm_imm_v40_str1_4w_dup_u_r

Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                            base pointer
Operands
              3    IN2_PART        uint8    LOW,HIGH        Word part which is used for operand 2

31   31       32 bit immediate post modification in
              4    IN3_PM_IMM      int32    -2 ..2 -1
                                                            bytes
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rIp_pm_imm_v40_clone_4w_dup_u_r (ptrBase, ptrModify, HIGH, 2);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_rIp_pm_ptr_v40_clone_4w_dup_u_r
name          vldw_indexed_rIp_pm_ptr_v40_str1_4w_dup_u_r

Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
Operands                                                    base pointer
              3    IN2_PART        uint8    LOW,HIGH        Word part which is used for operand 2
              4    IN3_PM_PTR      void*                    Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rIp_pm_ptr_v40_clone_4w_dup_u_r (ptrBase, ptrModify, HIGH, ptr);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_rIp_v40_clone_4w_dup_u_r
name          vldw_indexed_rIp_v40_str1_4w_dup_u_r
Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
Operands      2    IN2_rI_OFFSET void *
                                                            base pointer
              3    IN2_PART        uint8    LOW,HIGH        Word part which is used for operand 2
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rIp_v40_clone_4w_dup_u_r (ptrBase, ptrModify, HIGH);

The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_pm_imm_v40_clone_4w_dup_u_r
name          vldw_pm_imm_v40_str1_4w_dup_u_r

Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (pN)+#imm32_6, voz[0]h [,?prSC]

Return type   vec40_t

              1    IN1_PTR        void *                   Pointer register (rN)
Operands                                     31   31       32 bit immediate post modification in
              2    IN2_IMM32_6 int32        -2 ..2 -1
                                                           bytes
              void* ptr;
              vec40_t vRes;
C example     ...
              vRes = vldw_pm_imm_v40_clone_4w_dup_u_r (ptr, 2);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_pm_ptr_v40_clone_4w_dup_u_r
name          vldw_pm_ptr_v40_str1_4w_dup_u_r

Spec syntax   vldw {2w_4w, dup [,u][,r_sw] [,strX][,rowstr]} (pN)[+pm_x], voz[0]h [,?prSC]

Return type   vec40_t

              1    IN1_PTR        void *                   Pointer register (rN)
Operands
              2    IN2_PM_PTR void*                        Pointer register (rN)
              void* ptr;
              void* vRes;
C example     ...
              ptr = vldw_pm_ptr_v40_clone_4w_dup_u_r (ptr, vRes);
                    The same data will be loaded to all vector units (Unless str1 is configured
Comments       1.
                    otherwise).



Intrinsic      vldw_v40_clone_4w_dup_u_r
name           vldw_v40_str1_4w_dup_u_r

Spec syntax    vldw {2w_4w, dup [,u][,r_sw] [,strX][,rowstr]} (pN)[+pm_x], voz[0]h [,?prSC]

Return type    vec40_t

Operands       1    IN1_PTR       void *                   Pointer register (rN)
               void* ptr;
               vec40_t vRes;
C example      ...
               vRes = vldw_v40_clone_4w_dup_u_r (ptr);

                    The same data will be loaded to all vector units (Unless str1 is configured
Comments       1.
                    otherwise).


Main table → Memory Access → Load → Load unsigned W rounded
Available addressing modes
Intrinsic Names:
vldw_indexed_imm_v40_clone_4w_dup_u_r_rowstr
vldw_indexed_rI_pm_imm_v40_clone_4w_dup_u_r_rowstr
vldw_indexed_rI_pm_ptr_v40_clone_4w_dup_u_r_rowstr
vldw_indexed_rI_v40_clone_4w_dup_u_r_rowstr
vldw_indexed_rIp_pm_imm_v40_clone_4w_dup_u_r_rowstr

vldw_indexed_rIp_pm_ptr_v40_clone_4w_dup_u_r_rowstr
vldw_indexed_rIp_v40_clone_4w_dup_u_r_rowstr
vldw_pm_imm_v40_clone_4w_dup_u_r_rowstr
vldw_pm_ptr_v40_clone_4w_dup_u_r_rowstr
vldw_v40_clone_4w_dup_u_r_rowstr
Intrinsic     vldw_indexed_imm_v40_clone_4w_dup_u_r_rowstr
name          vldw_indexed_imm_v40_str1_4w_dup_u_r_rowstr

Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+#imm16_6), voz[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE void *                       Pointer register (gB)
Operands                                                    16 bit immediate post modification in
              2    IN2_IMM16_6     int16    -32768..32767
                                                            bytes
              void* ptrBase;
              vec40_t vRes;
C example     ...
              vRes = vldw_indexed_imm_v40_clone_4w_dup_u_r_rowstr (ptrBase, 2);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_rI_pm_imm_v40_clone_4w_dup_u_r_rowstr
name          vldw_indexed_rI_pm_imm_v40_str1_4w_dup_u_r_rowstr

Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+rI)[+pm], voz[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
Operands                                                    base pointer
                                              31   31       32 bit immediate post modification in
              3    IN3_PM_IMM      int32    -2 ..2 -1
                                                            bytes
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rI_pm_imm_v40_clone_4w_dup_u_r_rowstr (ptrBase, ptrModify, 2);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_rI_pm_ptr_v40_clone_4w_dup_u_r_rowstr
name          vldw_indexed_rI_pm_ptr_v40_str1_4w_dup_u_r_rowstr

Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+rI)[+pm], voz[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)
Operands

2    IN2_rI_OFFSET void *                     Pointer (rI) specifying the offset from the
                                                            base pointer
              3    IN3_PM_PTR       void*                   Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rI_pm_ptr_v40_clone_4w_dup_u_r_rowstr (ptrBase, ptrModify, ptr);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_rI_v40_clone_4w_dup_u_r_rowstr
name          vldw_indexed_rI_v40_str1_4w_dup_u_r_rowstr

Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+rI)[+pm], voz[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE      void *                  Pointer register (gB)
Operands                                                    Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                            base pointer
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rI_v40_clone_4w_dup_u_r_rowstr (ptrBase, ptrModify);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_rIp_pm_imm_v40_clone_4w_dup_u_r_rowstr
name          vldw_indexed_rIp_pm_imm_v40_str1_4w_dup_u_r_rowstr

Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE      void *                  Pointer register (gB)

              2
                                                            Pointer (rI) specifying the offset from the
                   IN2_rI_OFFSET void *
                                                            base pointer
Operands
              3    IN2_PART         uint8    LOW,HIGH       Word part which is used for operand 2
                                               31   31      32 bit immediate post modification in
              4    IN3_PM_IMM       int32    -2 ..2 -1
                                                            bytes
              void* ptrBase;
C example     void* ptrModify;
              vec40_t vRes;
              ...

vRes = vldw_indexed_rIp_pm_imm_v40_clone_4w_dup_u_r_rowstr (ptrBase, ptrModify, HIGH, 2);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_rIp_pm_ptr_v40_clone_4w_dup_u_r_rowstr
name          vldw_indexed_rIp_pm_ptr_v40_str1_4w_dup_u_r_rowstr

Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
Operands                                                    base pointer
              3    IN2_PART        uint8    LOW,HIGH        Word part which is used for operand 2
              4    IN3_PM_PTR      void*                    Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rIp_pm_ptr_v40_clone_4w_dup_u_r_rowstr (ptrBase, ptrModify, HIGH, ptr);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_rIp_v40_clone_4w_dup_u_r_rowstr
name          vldw_indexed_rIp_v40_str1_4w_dup_u_r_rowstr

Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
Operands      2    IN2_rI_OFFSET void *
                                                            base pointer
              3    IN2_PART        uint8    LOW,HIGH        Word part which is used for operand 2
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rIp_v40_clone_4w_dup_u_r_rowstr (ptrBase, ptrModify, HIGH);

Comments      1.   The same data will be loaded to all vector units (Unless str1 is configured
                   otherwise).



Intrinsic     vldw_pm_imm_v40_clone_4w_dup_u_r_rowstr
name          vldw_pm_imm_v40_str1_4w_dup_u_r_rowstr

Spec syntax   vldw {2w_4w, dup [,u][,r_sw][,strX][,rowstr]} (pN)+#imm32_6, voz[0]h [,?prSC]

Return type   vec40_t

              1    IN1_PTR        void *                   Pointer register (rN)
Operands                                     31   31       32 bit immediate post modification in
              2    IN2_IMM32_6 int32       -2 ..2 -1
                                                           bytes
              void* ptr;
              vec40_t vRes;
C example     ...
              vRes = vldw_pm_imm_v40_clone_4w_dup_u_r_rowstr (ptr, 2);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_pm_ptr_v40_clone_4w_dup_u_r_rowstr
name          vldw_pm_ptr_v40_str1_4w_dup_u_r_rowstr

Spec syntax   vldw {2w_4w, dup [,u][,r_sw] [,strX][,rowstr]} (pN)[+pm_x], voz[0]h [,?prSC]

Return type   vec40_t

              1    IN1_PTR        void *                   Pointer register (rN)
Operands
              2    IN2_PM_PTR void*                        Pointer register (rN)
              void* ptr;
              void* vRes;
C example     ...
              ptr = vldw_pm_ptr_v40_clone_4w_dup_u_r_rowstr (ptr, vRes);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_v40_clone_4w_dup_u_r_rowstr
name          vldw_v40_str1_4w_dup_u_r_rowstr

Spec syntax   vldw {2w_4w, dup [,u][,r_sw] [,strX][,rowstr]} (pN)[+pm_x], voz[0]h [,?prSC]

Return type   vec40_t

Operands      1    IN1_PTR        void *                   Pointer register (rN)
              void* ptr;
C example     vec40_t vRes;
           ...
           vRes = vldw_v40_clone_4w_dup_u_r_rowstr (ptr);

                The same data will be loaded to all vector units (Unless str1 is configured
Comments   1.
                otherwise).


Main table → Memory Access → Load → Load unsigned W rounded
Available addressing modes
Intrinsic Names:
vldw_direct_v40_v40_8w_unpk_u_r
vldw_indexed_imm_v40_v40_8w_unpk_u_r
vldw_indexed_rI_pm_imm_v40_v40_8w_unpk_u_r
vldw_indexed_rI_pm_ptr_v40_v40_8w_unpk_u_r
vldw_indexed_rI_v40_v40_8w_unpk_u_r
vldw_indexed_rIp_pm_imm_v40_v40_8w_unpk_u_r
vldw_indexed_rIp_pm_ptr_v40_v40_8w_unpk_u_r
vldw_indexed_rIp_v40_v40_8w_unpk_u_r
vldw_pm_imm_v40_v40_8w_unpk_u_r
vldw_pm_ptr_v40_v40_8w_unpk_u_r
vldw_v40_v40_8w_unpk_u_r
Intrinsic     vldw_direct_v40_v40_8w_unpk_u_r
name

Spec syntax   vldw {8w, unpk [,u][,r_sw][,strX]} [#address], voz1[0]h, voz2[0]h [,?prSC]

Return type   vec40_t
                                                32
              1     IN1_ADDR      int32      0..2 -1         32 bit address
Operands
              2     RES2_V40      vec40_t                    Output vector result operand
              vec40_t vRes1;
              vec40_t vRes2;
C example     ...
              vRes1 = vldw_direct_v40_v40_8w_unpk_u_r (2, vRes2);

                    This intrinsic returns two results. The first result variable should be placed to
Comments      1.    the left of the = sign (lvalue). The second result variable should be passed as
                    an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_imm_v40_v40_8w_unpk_u_r
name
Spec syntax   vldw {8w, unpk [,u][,r_sw][,strX][,rowstr]} (gB+#imm16_6), voz1[0]h, voz2[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE void *                        Pointer register (gB)
                                                             16 bit immediate post modification in
Operands      2    IN2_IMM16_6     int16     -32768..32767
                                                             bytes
              3    RES2_V40        vec40_t                   Output vector result operand
              void* ptrBase;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_imm_v40_v40_8w_unpk_u_r (ptrBase, 2, vRes2);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_rI_pm_imm_v40_v40_8w_unpk_u_r
name
Spec syntax   vldw {8w, unpk [,u][,r_sw][,strX][,rowstr]} (gB+rI)[+pm], voz1[0]h, voz2[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                    Pointer register (gB)
Operands
              2    IN2_rI_OFFSET void *                      Pointer (rI) specifying the offset from the
                                                             base pointer
                                               31   31       32 bit immediate post modification in
              3    IN3_PM_IMM      int32     -2 ..2 -1
                                                             bytes

4    RES2_V40        vec40_t                   Output vector result operand
              void* ptrBase;
              void* ptrModify;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_rI_pm_imm_v40_v40_8w_unpk_u_r (ptrBase, ptrModify, 2, vRes2);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_rI_pm_ptr_v40_v40_8w_unpk_u_r
name
Spec syntax   vldw {8w, unpk [,u][,r_sw][,strX][,rowstr]} (gB+rI)[+pm], voz1[0]h, voz2[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                    Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
Operands                                                     base pointer
              3    IN3_PM_PTR      void*                     Pointer register (rN)
              4    RES2_V40        vec40_t                   Output vector result operand
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes1;
              vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_rI_pm_ptr_v40_v40_8w_unpk_u_r (ptrBase, ptrModify, ptr, vRes2);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_rI_v40_v40_8w_unpk_u_r
name
Spec syntax   vldw {8w, unpk [,u][,r_sw][,strX][,rowstr]} (gB+rI)[+pm], voz1[0]h, voz2[0]h [,?prSC]

Return type   vec40_t

Operands      1    IN1_gB_BASE     void *                    Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                            base pointer
              3    RES2_V40        vec40_t                  Output vector result operand
              void* ptrBase;
              void* ptrModify;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...

vRes1 = vldw_indexed_rI_v40_v40_8w_unpk_u_r (ptrBase, ptrModify, vRes2);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_rIp_pm_imm_v40_v40_8w_unpk_u_r
name
Spec syntax   vldw {8w, unpk [,u][,r_sw][,strX][,rowstr]} (gB+rIp)[+pm], voz1[0]h ,voz2[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                            base pointer
Operands      3    IN2_PART        uint8     LOW,HIGH       Word part which is used for operand 2
                                               31   31      32 bit immediate post modification in
              4    IN3_PM_IMM      int32     -2 ..2 -1
                                                            bytes
              5    RES2_V40        vec40_t                  Output vector result operand
              void* ptrBase;
              void* ptrModify;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_rIp_pm_imm_v40_v40_8w_unpk_u_r (ptrBase, ptrModify, LOW, 2, vRes2);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_rIp_pm_ptr_v40_v40_8w_unpk_u_r
name
Spec syntax   vldw {8w, unpk [,u][,r_sw][,strX][,rowstr]} (gB+rIp)[+pm], voz1[0]h ,voz2[0]h [,?prSC]

Return type   vec40_t
              1    IN1_gB_BASE     void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                            base pointer
Operands      3    IN2_PART        uint8     LOW,HIGH       Word part which is used for operand 2
              4    IN3_PM_PTR      void*                    Pointer register (rN)
              5    RES2_V40        vec40_t                  Output vector result operand

void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes1;
              vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_rIp_pm_ptr_v40_v40_8w_unpk_u_r (ptrBase, ptrModify, LOW, ptr, vRes2);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_rIp_v40_v40_8w_unpk_u_r
name
Spec syntax   vldw {8w, unpk [,u][,r_sw][,strX][,rowstr]} (gB+rIp)[+pm], voz1[0]h ,voz2[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
Operands                                                    base pointer
              3    IN2_PART        uint8     LOW,HIGH       Word part which is used for operand 2
              4    RES2_V40        vec40_t                  Output vector result operand
              void* ptrBase;
              void* ptrModify;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_rIp_v40_v40_8w_unpk_u_r (ptrBase, ptrModify, LOW, vRes2);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_pm_imm_v40_v40_8w_unpk_u_r
name
Spec syntax   vldw {8w, unpk [,u][,r_sw][,strX][,rowstr]} (pN)+#imm32_6, voz1[0]h ,voz2[0]h [,?prSC]
Return type   vec40_t

              1    IN1_PTR        void *                   Pointer register (rN)
                                             31   31       32 bit immediate post modification in
Operands      2    IN2_IMM32_6 int32        -2 ..2 -1
                                                           bytes
              3    RES2_V40       vec40_t                  Output vector result operand
              void* ptr;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_pm_imm_v40_v40_8w_unpk_u_r (ptr, 2, vRes2);

This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_pm_ptr_v40_v40_8w_unpk_u_r
name
Spec syntax   vldw {8w, unpk [,u][,r_sw][,strX][,rowstr]} (pN)[+pm_x], voz1[0]h ,voz2[0]h [,?prSC]

Return type   vec40_t

              1    IN1_PTR       void *                    Pointer register (rN)
Operands      2    IN2_PM_PTR void*                        Pointer register (rN)
              3    RES2_V40      vec40_t                   Output vector result operand
              vec40_t ptr;
              void* vRes1;
C example     vec40_t vRes2;
              ...
              vRes2 = vldw_pm_ptr_v40_v40_8w_unpk_u_r (ptr, vRes1, ptr);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_v40_v40_8w_unpk_u_r
name
Spec syntax   vldw {8w, unpk [,u][,r_sw][,strX][,rowstr]} (pN)[+pm_x], voz1[0]h ,voz2[0]h [,?prSC]

Return type   vec40_t

              1    IN1_PTR       void *                    Pointer register (rN)
Operands
              2    RES2_V40      vec40_t                   Output vector result operand
C example     void* ptr;
               vec40_t vRes1;
               vec40_t vRes2;
               ...
               vRes1 = vldw_v40_v40_8w_unpk_u_r (ptr, vRes2);

                    This intrinsic returns two results. The first result variable should be placed to
Comments       1.   the left of the = sign (lvalue). The second result variable should be passed as
                    an additional parameter (RES2_V40).


Main table → Memory Access → Load → Load unsigned W rounded
Available addressing modes
Intrinsic Names:
vldw_indexed_imm_v40_v40_8w_unpk_u_r_rowstr
vldw_indexed_rI_pm_imm_v40_v40_8w_unpk_u_r_rowstr
vldw_indexed_rI_pm_ptr_v40_v40_8w_unpk_u_r_rowstr
vldw_indexed_rI_v40_v40_8w_unpk_u_r_rowstr
vldw_indexed_rIp_pm_imm_v40_v40_8w_unpk_u_r_rowstr
vldw_indexed_rIp_pm_ptr_v40_v40_8w_unpk_u_r_rowstr
vldw_indexed_rIp_v40_v40_8w_unpk_u_r_rowstr
vldw_pm_imm_v40_v40_8w_unpk_u_r_rowstr
vldw_pm_ptr_v40_v40_8w_unpk_u_r_rowstr
vldw_v40_v40_8w_unpk_u_r_rowstr
Intrinsic     vldw_indexed_imm_v40_v40_8w_unpk_u_r_rowstr
name

Spec syntax   vldw {8w, unpk [,u][,r_sw][,strX][,rowstr]} (gB+#imm16_6), voz1[0]h, voz2[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE void *                        Pointer register (gB)
                                                             16 bit immediate post modification in
Operands      2    IN2_IMM16_6     int16     -32768..32767
                                                             bytes
              3    RES2_V40        vec40_t                   Output vector result operand
              void* ptrBase;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_imm_v40_v40_8w_unpk_u_r_rowstr (ptrBase, 2, vRes2);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_rI_pm_imm_v40_v40_8w_unpk_u_r_rowstr
name
Spec syntax   vldw {8w, unpk [,u][,r_sw][,strX][,rowstr]} (gB+rI)[+pm], voz1[0]h, voz2[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                    Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
Operands
                                               31   31       32 bit immediate post modification in
              3    IN3_PM_IMM      int32     -2 ..2 -1
                                                             bytes
              4    RES2_V40        vec40_t                   Output vector result operand
              void* ptrBase;
              void* ptrModify;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_rI_pm_imm_v40_v40_8w_unpk_u_r_rowstr (ptrBase, ptrModify, 2, vRes2);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_rI_pm_ptr_v40_v40_8w_unpk_u_r_rowstr
name
Spec syntax   vldw {8w, unpk [,u][,r_sw][,strX][,rowstr]} (gB+rI)[+pm], voz1[0]h, voz2[0]h [,?prSC]

Return type   vec40_t

1    IN1_gB_BASE     void *                    Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
Operands                                                     base pointer
              3    IN3_PM_PTR      void*                     Pointer register (rN)
              4    RES2_V40        vec40_t                   Output vector result operand
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes1;
              vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_rI_pm_ptr_v40_v40_8w_unpk_u_r_rowstr (ptrBase, ptrModify, ptr, vRes2);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_rI_v40_v40_8w_unpk_u_r_rowstr
name
Spec syntax   vldw {8w, unpk [,u][,r_sw][,strX][,rowstr]} (gB+rI)[+pm], voz1[0]h, voz2[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                    Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
Operands      2    IN2_rI_OFFSET void *
                                                             base pointer
              3    RES2_V40        vec40_t                   Output vector result operand
              void* ptrBase;
              void* ptrModify;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_rI_v40_v40_8w_unpk_u_r_rowstr (ptrBase, ptrModify, vRes2);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_rIp_pm_imm_v40_v40_8w_unpk_u_r_rowstr
name
Spec syntax   vldw {8w, unpk [,u][,r_sw][,strX][,rowstr]} (gB+rIp)[+pm], voz1[0]h ,voz2[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *

base pointer
Operands      3    IN2_PART        uint8     LOW,HIGH       Word part which is used for operand 2
                                               31   31      32 bit immediate post modification in
              4    IN3_PM_IMM      int32     -2 ..2 -1
                                                            bytes
              5    RES2_V40        vec40_t                  Output vector result operand
              void* ptrBase;
              void* ptrModify;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_rIp_pm_imm_v40_v40_8w_unpk_u_r_rowstr (ptrBase, ptrModify, LOW, 2,
              vRes2);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_rIp_pm_ptr_v40_v40_8w_unpk_u_r_rowstr
name
Spec syntax   vldw {8w, unpk [,u][,r_sw][,strX][,rowstr]} (gB+rIp)[+pm], voz1[0]h ,voz2[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)

              2
                                                            Pointer (rI) specifying the offset from the
                   IN2_rI_OFFSET void *
                                                            base pointer
Operands      3    IN2_PART        uint8     LOW,HIGH       Word part which is used for operand 2
              4    IN3_PM_PTR      void*                    Pointer register (rN)
              5    RES2_V40        vec40_t                  Output vector result operand
              void* ptr;
              void* ptrBase;
              void* ptrModify;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_rIp_pm_ptr_v40_v40_8w_unpk_u_r_rowstr (ptrBase, ptrModify, LOW, ptr,
              vRes2);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.
                   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_rIp_v40_v40_8w_unpk_u_r_rowstr
name
Spec syntax   vldw {8w, unpk [,u][,r_sw][,strX][,rowstr]} (gB+rIp)[+pm], voz1[0]h ,voz2[0]h [,?prSC]

Return type   vec40_t

1    IN1_gB_BASE     void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
Operands                                                    base pointer
              3    IN2_PART        uint8      LOW,HIGH      Word part which is used for operand 2
              4    RES2_V40        vec40_t                  Output vector result operand
              void* ptrBase;
              void* ptrModify;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_rIp_v40_v40_8w_unpk_u_r_rowstr (ptrBase, ptrModify, LOW, vRes2);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_pm_imm_v40_v40_8w_unpk_u_r_rowstr
name
Spec syntax   vldw {8w, unpk [,u][,r_sw][,strX][,rowstr]} (pN)+#imm32_6, voz1[0]h ,voz2[0]h [,?prSC]

Return type   vec40_t

              1    IN1_PTR        void *                    Pointer register (rN)
                                              31   31       32 bit immediate post modification in
Operands      2    IN2_IMM32_6 int32         -2 ..2 -1
                                                            bytes
              3    RES2_V40       vec40_t                   Output vector result operand
              void* ptr;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_pm_imm_v40_v40_8w_unpk_u_r_rowstr (ptr, 2, vRes2);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).
Intrinsic     vldw_pm_ptr_v40_v40_8w_unpk_u_r_rowstr
name
Spec syntax   vldw {8w, unpk [,u][,r_sw][,strX][,rowstr]} (pN)[+pm_x], voz1[0]h ,voz2[0]h [,?prSC]

Return type   vec40_t

              1    IN1_PTR       void *                    Pointer register (rN)
Operands      2    IN2_PM_PTR void*                        Pointer register (rN)
              3    RES2_V40      vec40_t                   Output vector result operand
              vec40_t ptr;
              void* vRes1;
C example     vec40_t vRes2;

...
              vRes2 = vldw_pm_ptr_v40_v40_8w_unpk_u_r_rowstr (ptr, vRes1, ptr);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_v40_v40_8w_unpk_u_r_rowstr
name
Spec syntax   vldw {8w, unpk [,u][,r_sw][,strX][,rowstr]} (pN)[+pm_x], voz1[0]h ,voz2[0]h [,?prSC]

Return type   vec40_t

              1    IN1_PTR       void *                    Pointer register (rN)
Operands
              2    RES2_V40      vec40_t                   Output vector result operand
              void* ptr;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_v40_v40_8w_unpk_u_r_rowstr (ptr, vRes2);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).


Main table → Memory Access → Load → Load unsigned W rounded
Available addressing modes
Intrinsic Names:
vldw_direct_v40_v40_clone_8w_unpk_u_r
vldw_indexed_imm_v40_v40_clone_8w_unpk_u_r
vldw_indexed_rI_pm_imm_v40_v40_clone_8w_unpk_u_r
vldw_indexed_rI_pm_ptr_v40_v40_clone_8w_unpk_u_r
vldw_indexed_rI_v40_v40_clone_8w_unpk_u_r
vldw_indexed_rIp_pm_imm_v40_v40_clone_8w_unpk_u_r
vldw_indexed_rIp_pm_ptr_v40_v40_clone_8w_unpk_u_r
vldw_indexed_rIp_v40_v40_clone_8w_unpk_u_r
vldw_pm_imm_v40_v40_clone_8w_unpk_u_r
vldw_pm_ptr_v40_v40_clone_8w_unpk_u_r
vldw_v40_v40_clone_8w_unpk_u_r
Intrinsic     vldw_direct_v40_v40_clone_8w_unpk_u_r
name          vldw_direct_v40_v40_str1_8w_unpk_u_r

Spec syntax   vldw {8w, unpk [,u][,r_sw][,strX]} [#address], voz1[0]h, voz2[0]h [,?prSC]

Return type   vec40_t
                                               32
              1    IN1_ADDR      int32      0..2 -1         32 bit address
Operands
              2    RES2_V40      vec40_t                    Output vector result operand
              vec40_t vRes1;
              vec40_t vRes2;
C example     ...
              vRes1 = vldw_direct_v40_v40_clone_8w_unpk_u_r (2, vRes2);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).

Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_imm_v40_v40_clone_8w_unpk_u_r
name          vldw_indexed_imm_v40_v40_str1_8w_unpk_u_r

Spec syntax   vldw {8w, unpk [,u][,r_sw][,strX][,rowstr]} (gB+#imm16_6), voz1[0]h, voz2[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE void *                       Pointer register (gB)
                                                            16 bit immediate post modification in
Operands      2    IN2_IMM16_6    int16     -32768..32767
                                                            bytes
              3    RES2_V40       vec40_t                   Output vector result operand
              void* ptrBase;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_imm_v40_v40_clone_8w_unpk_u_r (ptrBase, 2, vRes2);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_rI_pm_imm_v40_v40_clone_8w_unpk_u_r
name          vldw_indexed_rI_pm_imm_v40_v40_str1_8w_unpk_u_r
Spec syntax   vldw {8w, unpk [,u][,r_sw][,strX][,rowstr]} (gB+rI)[+pm], voz1[0]h, voz2[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                    Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
Operands
                                               31   31       32 bit immediate post modification in
              3    IN3_PM_IMM      int32     -2 ..2 -1
                                                             bytes
              4    RES2_V40        vec40_t                   Output vector result operand
              void* ptrBase;
              void* ptrModify;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...

vRes1 = vldw_indexed_rI_pm_imm_v40_v40_clone_8w_unpk_u_r (ptrBase, ptrModify, 2, vRes2);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_rI_pm_ptr_v40_v40_clone_8w_unpk_u_r
name          vldw_indexed_rI_pm_ptr_v40_v40_str1_8w_unpk_u_r

Spec syntax   vldw {8w, unpk [,u][,r_sw][,strX][,rowstr]} (gB+rI)[+pm], voz1[0]h, voz2[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                    Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
Operands                                                     base pointer
              3    IN3_PM_PTR      void*                     Pointer register (rN)
              4    RES2_V40        vec40_t                   Output vector result operand
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes1;
              vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_rI_pm_ptr_v40_v40_clone_8w_unpk_u_r (ptrBase, ptrModify, ptr, vRes2);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
Comments           otherwise).
              2.   This intrinsic returns two results. The first result variable should be placed to
                   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_rI_v40_v40_clone_8w_unpk_u_r
name          vldw_indexed_rI_v40_v40_str1_8w_unpk_u_r

Spec syntax   vldw {8w, unpk [,u][,r_sw][,strX][,rowstr]} (gB+rI)[+pm], voz1[0]h, voz2[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
Operands      2    IN2_rI_OFFSET void *
                                                            base pointer

3    RES2_V40        vec40_t                  Output vector result operand
              void* ptrBase;
              void* ptrModify;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_rI_v40_v40_clone_8w_unpk_u_r (ptrBase, ptrModify, vRes2);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_rIp_pm_imm_v40_v40_clone_8w_unpk_u_r
name          vldw_indexed_rIp_pm_imm_v40_v40_str1_8w_unpk_u_r

Spec syntax   vldw {8w, unpk [,u][,r_sw][,strX][,rowstr]} (gB+rIp)[+pm], voz1[0]h ,voz2[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                            base pointer
Operands      3    IN2_PART        uint8     LOW,HIGH       Word part which is used for operand 2
                                               31   31      32 bit immediate post modification in
              4    IN3_PM_IMM      int32     -2 ..2 -1
                                                            bytes
              5    RES2_V40        vec40_t                  Output vector result operand
              void* ptrBase;
C example     void* ptrModify;
              vec40_t vRes1;
              vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_rIp_pm_imm_v40_v40_clone_8w_unpk_u_r (ptrBase, ptrModify, LOW, 2,
              vRes2);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_rIp_pm_ptr_v40_v40_clone_8w_unpk_u_r
name          vldw_indexed_rIp_pm_ptr_v40_v40_str1_8w_unpk_u_r

Spec syntax   vldw {8w, unpk [,u][,r_sw][,strX][,rowstr]} (gB+rIp)[+pm], voz1[0]h ,voz2[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                            base pointer
Operands      3    IN2_PART        uint8     LOW,HIGH       Word part which is used for operand 2
              4    IN3_PM_PTR      void*                    Pointer register (rN)
              5    RES2_V40        vec40_t                  Output vector result operand
              void* ptr;
              void* ptrBase;
              void* ptrModify;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_rIp_pm_ptr_v40_v40_clone_8w_unpk_u_r (ptrBase, ptrModify, LOW, ptr,
              vRes2);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_rIp_v40_v40_clone_8w_unpk_u_r
name          vldw_indexed_rIp_v40_v40_str1_8w_unpk_u_r

Spec syntax   vldw {8w, unpk [,u][,r_sw][,strX][,rowstr]} (gB+rIp)[+pm], voz1[0]h ,voz2[0]h [,?prSC]

Return type   vec40_t
              1    IN1_gB_BASE     void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
Operands                                                    base pointer
              3    IN2_PART        uint8      LOW,HIGH      Word part which is used for operand 2
              4    RES2_V40        vec40_t                  Output vector result operand
              void* ptrBase;
              void* ptrModify;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_rIp_v40_v40_clone_8w_unpk_u_r (ptrBase, ptrModify, LOW, vRes2);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).

Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_pm_imm_v40_v40_clone_8w_unpk_u_r
name          vldw_pm_imm_v40_v40_str1_8w_unpk_u_r

Spec syntax   vldw {8w, unpk [,u][,r_sw][,strX][,rowstr]} (pN)+#imm32_6, voz1[0]h ,voz2[0]h [,?prSC]

Return type   vec40_t

              1    IN1_PTR        void *                   Pointer register (rN)
                                              31   31      32 bit immediate post modification in
Operands      2    IN2_IMM32_6 int32         -2 ..2 -1
                                                           bytes
              3    RES2_V40       vec40_t                  Output vector result operand
              void* ptr;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_pm_imm_v40_v40_clone_8w_unpk_u_r (ptr, 2, vRes2);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_pm_ptr_v40_v40_clone_8w_unpk_u_r
name          vldw_pm_ptr_v40_v40_str1_8w_unpk_u_r
Spec syntax    vldw {8w, unpk [,u][,r_sw][,strX][,rowstr]} (pN)[+pm_x], voz1[0]h ,voz2[0]h [,?prSC]

Return type    vec40_t

               1    IN1_PTR       void *                    Pointer register (rN)
Operands       2    IN2_PM_PTR void*                        Pointer register (rN)
               3    RES2_V40      vec40_t                   Output vector result operand
               vec40_t ptr;
               void* vRes1;
C example      vec40_t vRes2;
               ...
               vRes2 = vldw_pm_ptr_v40_v40_clone_8w_unpk_u_r (ptr, vRes1, ptr);

                    The same data will be loaded to all vector units (Unless str1 is configured
               1.
                    otherwise).
Comments            This intrinsic returns two results. The first result variable should be placed to
               2.   the left of the = sign (lvalue). The second result variable should be passed as

an additional parameter (RES2_V40).



Intrinsic      vldw_v40_v40_clone_8w_unpk_u_r
name           vldw_v40_v40_str1_8w_unpk_u_r

Spec syntax    vldw {8w, unpk [,u][,r_sw][,strX][,rowstr]} (pN)[+pm_x], voz1[0]h ,voz2[0]h [,?prSC]

Return type    vec40_t

               1    IN1_PTR       void *                    Pointer register (rN)
Operands
               2    RES2_V40      vec40_t                   Output vector result operand
               void* ptr;
               vec40_t vRes1;
C example      vec40_t vRes2;
               ...
               vRes1 = vldw_v40_v40_clone_8w_unpk_u_r (ptr, vRes2);

               1.
                    The same data will be loaded to all vector units (Unless str1 is configured
                    otherwise).
Comments            This intrinsic returns two results. The first result variable should be placed to
               2.   the left of the = sign (lvalue). The second result variable should be passed as
                    an additional parameter (RES2_V40).


Main table → Memory Access → Load → Load unsigned W rounded
Available addressing modes
Intrinsic Names:
vldw_indexed_imm_v40_v40_clone_8w_unpk_u_r_rowstr
vldw_indexed_rI_pm_imm_v40_v40_clone_8w_unpk_u_r_rowstr
vldw_indexed_rI_pm_ptr_v40_v40_clone_8w_unpk_u_r_rowstr
vldw_indexed_rI_v40_v40_clone_8w_unpk_u_r_rowstr
vldw_indexed_rIp_pm_imm_v40_v40_clone_8w_unpk_u_r_rowstr
vldw_indexed_rIp_pm_ptr_v40_v40_clone_8w_unpk_u_r_rowstr
vldw_indexed_rIp_v40_v40_clone_8w_unpk_u_r_rowstr
vldw_pm_imm_v40_v40_clone_8w_unpk_u_r_rowstr
vldw_pm_ptr_v40_v40_clone_8w_unpk_u_r_rowstr
vldw_v40_v40_clone_8w_unpk_u_r_rowstr
Intrinsic     vldw_indexed_imm_v40_v40_clone_8w_unpk_u_r_rowstr
name          vldw_indexed_imm_v40_v40_str1_8w_unpk_u_r_rowstr

Spec syntax   vldw {8w, unpk [,u][,r_sw][,strX][,rowstr]} (gB+#imm16_6), voz1[0]h, voz2[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE void *                        Pointer register (gB)
                                                             16 bit immediate post modification in
Operands      2    IN2_IMM16_6     int16     -32768..32767
                                                             bytes
              3    RES2_V40        vec40_t                   Output vector result operand
              void* ptrBase;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_imm_v40_v40_clone_8w_unpk_u_r_rowstr (ptrBase, 2, vRes2);

The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_rI_pm_imm_v40_v40_clone_8w_unpk_u_r_rowstr
name          vldw_indexed_rI_pm_imm_v40_v40_str1_8w_unpk_u_r_rowstr

Spec syntax   vldw {8w, unpk [,u][,r_sw][,strX][,rowstr]} (gB+rI)[+pm], voz1[0]h, voz2[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                    Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
Operands
                                               31   31       32 bit immediate post modification in
              3    IN3_PM_IMM      int32     -2 ..2 -1
                                                             bytes
              4    RES2_V40        vec40_t                   Output vector result operand
              void* ptrBase;
              void* ptrModify;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_rI_pm_imm_v40_v40_clone_8w_unpk_u_r_rowstr (ptrBase, ptrModify, 2,
              vRes2);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
Comments           otherwise).
              2.   This intrinsic returns two results. The first result variable should be placed to
                   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_rI_pm_ptr_v40_v40_clone_8w_unpk_u_r_rowstr
name          vldw_indexed_rI_pm_ptr_v40_v40_str1_8w_unpk_u_r_rowstr

Spec syntax   vldw {8w, unpk [,u][,r_sw][,strX][,rowstr]} (gB+rI)[+pm], voz1[0]h, voz2[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
Operands                                                    base pointer

3    IN3_PM_PTR      void*                    Pointer register (rN)
              4    RES2_V40        vec40_t                  Output vector result operand
              void* ptr;
              void* ptrBase;
              void* ptrModify;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_rI_pm_ptr_v40_v40_clone_8w_unpk_u_r_rowstr (ptrBase, ptrModify, ptr,
              vRes2);

              1.
                   The same data will be loaded to all vector units (Unless str1 is configured
                   otherwise).
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_rI_v40_v40_clone_8w_unpk_u_r_rowstr
name          vldw_indexed_rI_v40_v40_str1_8w_unpk_u_r_rowstr

Spec syntax   vldw {8w, unpk [,u][,r_sw][,strX][,rowstr]} (gB+rI)[+pm], voz1[0]h, voz2[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
Operands      2    IN2_rI_OFFSET void *
                                                            base pointer
              3    RES2_V40        vec40_t                  Output vector result operand
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes1;
              vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_rI_v40_v40_clone_8w_unpk_u_r_rowstr (ptrBase, ptrModify, vRes2);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_rIp_pm_imm_v40_v40_clone_8w_unpk_u_r_rowstr
name          vldw_indexed_rIp_pm_imm_v40_v40_str1_8w_unpk_u_r_rowstr

Spec syntax   vldw {8w, unpk [,u][,r_sw][,strX][,rowstr]} (gB+rIp)[+pm], voz1[0]h ,voz2[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)

Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                            base pointer
Operands      3    IN2_PART        uint8     LOW,HIGH       Word part which is used for operand 2
                                               31   31      32 bit immediate post modification in
              4    IN3_PM_IMM      int32     -2 ..2 -1
                                                            bytes
              5    RES2_V40        vec40_t                  Output vector result operand
              void* ptrBase;
              void* ptrModify;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_rIp_pm_imm_v40_v40_clone_8w_unpk_u_r_rowstr (ptrBase, ptrModify, LOW,
              2, vRes2);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_rIp_pm_ptr_v40_v40_clone_8w_unpk_u_r_rowstr
name          vldw_indexed_rIp_pm_ptr_v40_v40_str1_8w_unpk_u_r_rowstr

Spec syntax   vldw {8w, unpk [,u][,r_sw][,strX][,rowstr]} (gB+rIp)[+pm], voz1[0]h ,voz2[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)
Operands
              2    IN2_rI_OFFSET void *                     Pointer (rI) specifying the offset from the
                                                            base pointer
              3    IN2_PART        uint8     LOW,HIGH       Word part which is used for operand 2
              4    IN3_PM_PTR      void*                    Pointer register (rN)
              5    RES2_V40        vec40_t                  Output vector result operand
              void* ptr;
              void* ptrBase;
              void* ptrModify;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_rIp_pm_ptr_v40_v40_clone_8w_unpk_u_r_rowstr (ptrBase, ptrModify, LOW,
              ptr, vRes2);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).

Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_rIp_v40_v40_clone_8w_unpk_u_r_rowstr
name          vldw_indexed_rIp_v40_v40_str1_8w_unpk_u_r_rowstr

Spec syntax   vldw {8w, unpk [,u][,r_sw][,strX][,rowstr]} (gB+rIp)[+pm], voz1[0]h ,voz2[0]h [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
Operands                                                    base pointer
              3    IN2_PART        uint8     LOW,HIGH       Word part which is used for operand 2
              4    RES2_V40        vec40_t                  Output vector result operand
              void* ptrBase;
              void* ptrModify;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_rIp_v40_v40_clone_8w_unpk_u_r_rowstr (ptrBase, ptrModify, LOW, vRes2);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).
Intrinsic     vldw_pm_imm_v40_v40_clone_8w_unpk_u_r_rowstr
name          vldw_pm_imm_v40_v40_str1_8w_unpk_u_r_rowstr

Spec syntax   vldw {8w, unpk [,u][,r_sw][,strX][,rowstr]} (pN)+#imm32_6, voz1[0]h ,voz2[0]h [,?prSC]

Return type   vec40_t

              1    IN1_PTR        void *                   Pointer register (rN)
                                             31   31       32 bit immediate post modification in
Operands      2    IN2_IMM32_6 int32        -2 ..2 -1
                                                           bytes
              3    RES2_V40       vec40_t                  Output vector result operand
              void* ptr;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_pm_imm_v40_v40_clone_8w_unpk_u_r_rowstr (ptr, 2, vRes2);

The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_pm_ptr_v40_v40_clone_8w_unpk_u_r_rowstr
name          vldw_pm_ptr_v40_v40_str1_8w_unpk_u_r_rowstr

Spec syntax   vldw {8w, unpk [,u][,r_sw][,strX][,rowstr]} (pN)[+pm_x], voz1[0]h ,voz2[0]h [,?prSC]

Return type   vec40_t

              1    IN1_PTR       void *                    Pointer register (rN)
Operands      2    IN2_PM_PTR void*                        Pointer register (rN)
              3    RES2_V40      vec40_t                   Output vector result operand
              vec40_t ptr;
              void* vRes1;
C example     vec40_t vRes2;
              ...
              vRes2 = vldw_pm_ptr_v40_v40_clone_8w_unpk_u_r_rowstr (ptr, vRes1, ptr);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).
Intrinsic     vldw_v40_v40_clone_8w_unpk_u_r_rowstr
name          vldw_v40_v40_str1_8w_unpk_u_r_rowstr

Spec syntax   vldw {8w, unpk [,u][,r_sw][,strX][,rowstr]} (pN)[+pm_x], voz1[0]h ,voz2[0]h [,?prSC]

Return type   vec40_t

              1    IN1_PTR       void *                    Pointer register (rN)
Operands
              2    RES2_V40      vec40_t                   Output vector result operand
              void* ptr;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_v40_v40_clone_8w_unpk_u_r_rowstr (ptr, vRes2);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).


Main table → Memory Access → Load → Load unsigned W rounded

Available addressing modes
Intrinsic Names:
vldw_pm_imm_v40_vuX_u_r
vldw_pm_ptr_v40_vuX_u_r
vldw_v40_vuX_u_r
Intrinsic     vldw_pm_imm_v40_vuX_u_r
name
Spec syntax   vldw {ew, vuX [,u][,r_sw]} (pN)[+pm_x], voz[0]h [,?prSC]

Return        vec40_t
type
                                                              Determines the element size and number
                                 EW_options
              1   EW
                                 enum                         of loaded elements (see enum definition
                                                              at vec-mem-modes.h)

Operands      2   VUX            uint8          0..3          Determines the destination VCU
              3   IN1_PTR        void *                       Pointer register (rN)
                                                  31   31     32 bit immediate post modification in
              4   IN2_PM_IMM int32              -2 ..2 -1
                                                              bytes
              vec40_t 2;
              void* ptr;
C example     ...
              2 = vldw_pm_imm_v40_vuX_u_r (ew_8w, 1, ptr, vRes);

Comments



Intrinsic     vldw_pm_ptr_v40_vuX_u_r
name
Spec          vldw {ew, vuX [,u][,r_sw]} (pN)[+pm_x], voz[0]h [,?prSC]
syntax
Return        vec40_t
type
                                                               Determines the element size and number
                                 EW_options
              1   EW
                                 enum                          of loaded elements (see enum definition
                                                               at vec-mem-modes.h)
Operands      2   VUX            uint8         0..3            Determines the destination VCU
              3   IN1_PTR        void *                        Pointer register (rN)
              4   IN2_PM_PTR void*                             Pointer register (rN)
              void* ptr;
              void* vRes;
C example     ...
              ptr = vldw_pm_ptr_v40_vuX_u_r (ew_8w, 1, ptr, vRes);

Comments



Intrinsic     vldw_v40_vuX_u_r
name
Spec syntax   vldw {ew, vuX [,u][,r_sw]} (pN)[+pm_x], voz[0]h [,?prSC]

Return        vec40_t
type
                                                            Determines the element size and number
                                EW_options
              1   EW
                                enum                        of loaded elements (see enum definition

at vec-mem-modes.h)
Operands
              2   VUX           uint8         0..3          Determines the destination VCU
              3   IN1_PTR       void *                      Pointer register (rN)
              void* ptr;
              vec40_t vRes;
C example     ...
              vRes = vldw_v40_vuX_u_r (ew_8w, 1, ptr);

Comments


Main table → Memory Access → Load → Load unsigned W rounded
